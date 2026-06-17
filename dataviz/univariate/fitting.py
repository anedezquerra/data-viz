"""Distribution fitting and fitted distribution visualizations."""

from dataclasses import dataclass
from typing import Dict, Iterable, Optional, Tuple

import numpy as np
import pandas as pd
import plotly.graph_objects as go
from scipy import stats

from ..types import FigureSize, MatplotlibAxes, PlotlyFigure, SeriesLike
from ..utils import apply_theme, setup_plot, validate_positive_int
from .stats import as_numeric_series


@dataclass(frozen=True)
class DistributionFit:
    """Fitted SciPy distribution summary.

    Args:
        distribution (str): Name of the fitted SciPy distribution.
        parameters (Tuple[float, ...]): Fitted distribution parameters.
        statistic (float): Kolmogorov-Smirnov goodness-of-fit statistic.
        p_value (float): Kolmogorov-Smirnov p-value.
        aic (float): Akaike information criterion.
        bic (float): Bayesian information criterion.

    Returns:
        DistributionFit: Immutable fitted distribution summary.

    Raises:
        TypeError: If values cannot be represented by declared fields.
        ValueError: If values are incompatible with downstream numeric use.

    Examples:
        ```python
        fit = DistributionFit("norm", (0.0, 1.0), 0.05, 0.9, 120.0, 124.0)
        ```

    Notes:
        Smaller AIC or BIC values indicate a better relative fit among candidate distributions.
    """

    distribution: str
    parameters: Tuple[float, ...]
    statistic: float
    p_value: float
    aic: float
    bic: float


def _distribution(name: str) -> object:
    """Resolve a SciPy distribution by name.

    Args:
        name (str): SciPy distribution name.

    Returns:
        object: SciPy continuous distribution object.

    Raises:
        TypeError: If ``name`` is not a string.
        ValueError: If the distribution is not available in ``scipy.stats``.

    Examples:
        ```python
        normal = _distribution("norm")
        ```

    Notes:
        The helper keeps public functions' validation consistent.
    """
    if not isinstance(name, str):
        raise TypeError("distribution name must be a string.")
    if not hasattr(stats, name):
        raise ValueError(f"Unknown scipy.stats distribution: {name!r}.")
    return getattr(stats, name)


def fit_distribution(data: SeriesLike, distribution: str = "norm") -> DistributionFit:
    """Fit a SciPy continuous distribution to one numeric variable.

    Args:
        data (SeriesLike): Input observations.
        distribution (str): SciPy distribution name.

    Returns:
        DistributionFit: Fitted parameters and goodness-of-fit metrics.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If the distribution name is invalid or fitting fails.

    Examples:
        ```python
        fit = fit_distribution(data, distribution="lognorm")
        ```

    Notes:
        AIC and BIC are computed from the fitted log-likelihood.
    """
    values = as_numeric_series(data).to_numpy(dtype=float)
    dist = _distribution(distribution)
    params = tuple(float(value) for value in dist.fit(values))
    statistic, p_value = stats.kstest(values, distribution, args=params)
    pdf_values = np.maximum(dist.pdf(values, *params), np.finfo(float).tiny)
    log_likelihood = float(np.sum(np.log(pdf_values)))
    k = len(params)
    n = len(values)
    return DistributionFit(
        distribution=distribution,
        parameters=params,
        statistic=float(statistic),
        p_value=float(p_value),
        aic=float(2 * k - 2 * log_likelihood),
        bic=float(k * np.log(n) - 2 * log_likelihood),
    )


def compare_distributions(
    data: SeriesLike,
    distributions: Iterable[str] = ("norm", "lognorm", "expon", "gamma", "weibull_min"),
) -> pd.DataFrame:
    """Fit and rank multiple candidate distributions.

    Args:
        data (SeriesLike): Input observations.
        distributions (Iterable[str]): Candidate SciPy distribution names.

    Returns:
        pandas.DataFrame: Fit metrics sorted by AIC ascending.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If no candidate distributions are provided or fitting fails.

    Examples:
        ```python
        table = compare_distributions(data, ["norm", "gamma"])
        ```

    Notes:
        The parameter tuple is retained so callers can reproduce the fitted distribution.
    """
    names = list(distributions)
    if not names:
        raise ValueError("At least one candidate distribution is required.")
    fits = [fit_distribution(data, name) for name in names]
    return pd.DataFrame(
        {
            "distribution": [fit.distribution for fit in fits],
            "parameters": [fit.parameters for fit in fits],
            "ks_statistic": [fit.statistic for fit in fits],
            "p_value": [fit.p_value for fit in fits],
            "aic": [fit.aic for fit in fits],
            "bic": [fit.bic for fit in fits],
        }
    ).sort_values("aic", ignore_index=True)


def fitted_pdf_values(data: SeriesLike, distribution: str = "norm", points: int = 200) -> Tuple[np.ndarray, np.ndarray, DistributionFit]:
    """Compute fitted probability density curve values.

    Args:
        data (SeriesLike): Input observations.
        distribution (str): SciPy distribution name.
        points (int): Number of curve points to generate.

    Returns:
        Tuple[numpy.ndarray, numpy.ndarray, DistributionFit]: X values, PDF values, and fit summary.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If ``points`` is not positive or fitting fails.

    Examples:
        ```python
        x, y, fit = fitted_pdf_values(data, "norm")
        ```

    Notes:
        The curve spans the observed data range.
    """
    validate_positive_int(points, "points")
    values = as_numeric_series(data).to_numpy(dtype=float)
    fit = fit_distribution(values, distribution)
    dist = _distribution(distribution)
    x_values = np.linspace(float(values.min()), float(values.max()), points)
    y_values = dist.pdf(x_values, *fit.parameters)
    return x_values, y_values, fit


def fitted_distribution_histogram_static(
    data: SeriesLike,
    distribution: str = "norm",
    bins: int = 30,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    color: Optional[str] = None,
    fit_color: str = "crimson",
    theme: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Create a static histogram with a fitted probability density overlay.

    Args:
        data (SeriesLike): Input observations.
        distribution (str): SciPy distribution name.
        bins (int): Number of histogram bins.
        title (Optional[str]): Optional chart title.
        xlabel (Optional[str]): Optional x-axis label.
        figsize (FigureSize): Matplotlib figure size.
        color (Optional[str]): Histogram color.
        fit_color (str): Fitted density line color.
        theme (str): Styling theme name.
        **kwargs: Additional keyword arguments forwarded to ``Axes.hist``.

    Returns:
        matplotlib.axes.Axes: Axes containing the histogram and fitted density.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If ``bins`` is not positive or fitting fails.

    Examples:
        ```python
        ax = fitted_distribution_histogram_static(data, distribution="gamma")
        ```

    Notes:
        The histogram is density-normalized so the fitted PDF is on the same scale.
    """
    validate_positive_int(bins, "bins")
    values = as_numeric_series(data)
    x_values, y_values, fit = fitted_pdf_values(values, distribution)
    ax = setup_plot(
        title=title or f"Fitted {distribution} Distribution",
        xlabel=xlabel or values.name,
        ylabel="Density",
        figsize=figsize,
    )[1]
    ax.hist(values, bins=bins, density=True, color=color, alpha=0.7, edgecolor="black", **kwargs)
    ax.plot(x_values, y_values, color=fit_color, linewidth=2, label=f"{distribution} (KS p={fit.p_value:.3f})")
    ax.legend()
    ax.grid(True, axis="y", alpha=0.3)
    apply_theme(ax, theme)
    return ax


def fitted_distribution_histogram_interactive(
    data: SeriesLike,
    distribution: str = "norm",
    bins: int = 30,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    color: Optional[str] = None,
    fit_color: str = "crimson",
    template: str = "plotly",
    height: int = 600,
    width: int = 1000,
    **kwargs,
) -> PlotlyFigure:
    """Create an interactive histogram with a fitted probability density overlay.

    Args:
        data (SeriesLike): Input observations.
        distribution (str): SciPy distribution name.
        bins (int): Number of histogram bins.
        title (Optional[str]): Optional chart title.
        xlabel (Optional[str]): Optional x-axis label.
        color (Optional[str]): Histogram color.
        fit_color (str): Fitted density line color.
        template (str): Plotly template name.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.
        **kwargs: Additional keyword arguments forwarded to ``go.Histogram``.

    Returns:
        plotly.graph_objects.Figure: Interactive histogram and fitted density.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If ``bins`` is not positive or fitting fails.

    Examples:
        ```python
        fig = fitted_distribution_histogram_interactive(data)
        ```

    Notes:
        The histogram uses probability-density normalization for visual comparability.
    """
    validate_positive_int(bins, "bins")
    values = as_numeric_series(data)
    x_values, y_values, fit = fitted_pdf_values(values, distribution)
    fig = go.Figure()
    fig.add_trace(
        go.Histogram(
            x=values,
            nbinsx=bins,
            histnorm="probability density",
            marker_color=color,
            opacity=0.7,
            name="Observed",
            **kwargs,
        )
    )
    fig.add_trace(
        go.Scatter(
            x=x_values,
            y=y_values,
            mode="lines",
            line=dict(color=fit_color),
            name=f"{distribution} (KS p={fit.p_value:.3f})",
        )
    )
    fig.update_layout(
        title=title or f"Fitted {distribution} Distribution",
        xaxis_title=xlabel or values.name,
        yaxis_title="Density",
        template=template,
        height=height,
        width=width,
    )
    return fig
