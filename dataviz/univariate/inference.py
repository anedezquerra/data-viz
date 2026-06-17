"""Bootstrap inference helpers for univariate data."""

from dataclasses import dataclass
from typing import Callable, Literal, Optional

import numpy as np
import pandas as pd
import plotly.graph_objects as go

from ..types import FigureSize, MatplotlibAxes, PlotlyFigure, SeriesLike
from ..utils import setup_plot, validate_positive_int
from .stats import as_numeric_series

StatisticName = Literal["mean", "median", "std"]


@dataclass(frozen=True)
class BootstrapCI:
    """Bootstrap confidence interval result.

    Args:
        statistic (str): Statistic name.
        estimate (float): Statistic computed on original data.
        lower (float): Lower confidence bound.
        upper (float): Upper confidence bound.
        confidence_level (float): Confidence level.
        n_resamples (int): Number of bootstrap resamples.

    Returns:
        BootstrapCI: Immutable bootstrap interval summary.

    Raises:
        TypeError: If values cannot be represented by declared fields.
        ValueError: If interval values are incompatible with downstream numeric use.

    Examples:
        ```python
        ci = BootstrapCI("mean", 2.0, 1.5, 2.5, 0.95, 1000)
        ```

    Notes:
        Intervals use the percentile bootstrap method.
    """

    statistic: str
    estimate: float
    lower: float
    upper: float
    confidence_level: float
    n_resamples: int


def _statistic_function(statistic: StatisticName) -> Callable[[np.ndarray], float]:
    """Resolve a statistic name to a NumPy-compatible function.

    Args:
        statistic (StatisticName): Statistic name.

    Returns:
        Callable[[numpy.ndarray], float]: Function computing the statistic.

    Raises:
        TypeError: If ``statistic`` is not a string.
        ValueError: If the statistic is unsupported.

    Examples:
        ```python
        func = _statistic_function("mean")
        ```

    Notes:
        The helper centralizes statistic validation for bootstrap functions.
    """
    if statistic == "mean":
        return lambda values: float(np.mean(values))
    if statistic == "median":
        return lambda values: float(np.median(values))
    if statistic == "std":
        return lambda values: float(np.std(values, ddof=1))
    raise ValueError("statistic must be one of 'mean', 'median', or 'std'.")


def bootstrap_distribution(
    data: SeriesLike,
    statistic: StatisticName = "mean",
    n_resamples: int = 1000,
    seed: Optional[int] = None,
) -> pd.Series:
    """Generate a bootstrap distribution for one statistic.

    Args:
        data (SeriesLike): Input observations.
        statistic (StatisticName): Statistic to bootstrap.
        n_resamples (int): Number of bootstrap samples.
        seed (Optional[int]): Random seed for reproducibility.

    Returns:
        pandas.Series: Bootstrap statistic values.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If ``statistic`` or ``n_resamples`` is invalid.

    Examples:
        ```python
        samples = bootstrap_distribution(data, statistic="median")
        ```

    Notes:
        Bootstrap samples are drawn with replacement and the same size as the observed data.
    """
    validate_positive_int(n_resamples, "n_resamples")
    values = as_numeric_series(data).to_numpy(dtype=float)
    func = _statistic_function(statistic)
    rng = np.random.default_rng(seed)
    samples = np.empty(n_resamples)
    for index in range(n_resamples):
        sample = rng.choice(values, size=len(values), replace=True)
        samples[index] = func(sample)
    return pd.Series(samples, name=f"bootstrap_{statistic}")


def bootstrap_ci(
    data: SeriesLike,
    statistic: StatisticName = "mean",
    confidence_level: float = 0.95,
    n_resamples: int = 1000,
    seed: Optional[int] = None,
) -> BootstrapCI:
    """Compute a percentile bootstrap confidence interval.

    Args:
        data (SeriesLike): Input observations.
        statistic (StatisticName): Statistic to bootstrap.
        confidence_level (float): Confidence level in the open ``(0, 1)`` interval.
        n_resamples (int): Number of bootstrap samples.
        seed (Optional[int]): Random seed for reproducibility.

    Returns:
        BootstrapCI: Original estimate and bootstrap confidence interval.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If options are invalid.

    Examples:
        ```python
        ci = bootstrap_ci(data, statistic="mean")
        ```

    Notes:
        The percentile method is simple, stable, and dependency-light.
    """
    if confidence_level <= 0 or confidence_level >= 1:
        raise ValueError("confidence_level must be between 0 and 1.")
    values = as_numeric_series(data).to_numpy(dtype=float)
    func = _statistic_function(statistic)
    distribution = bootstrap_distribution(values, statistic=statistic, n_resamples=n_resamples, seed=seed)
    alpha = 1 - confidence_level
    return BootstrapCI(
        statistic=statistic,
        estimate=func(values),
        lower=float(distribution.quantile(alpha / 2)),
        upper=float(distribution.quantile(1 - alpha / 2)),
        confidence_level=confidence_level,
        n_resamples=n_resamples,
    )


def bootstrap_distribution_plot_static(
    data: SeriesLike,
    statistic: StatisticName = "mean",
    n_resamples: int = 1000,
    seed: Optional[int] = None,
    title: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    color: Optional[str] = None,
) -> MatplotlibAxes:
    """Create a static histogram of bootstrap statistic values.

    Args:
        data (SeriesLike): Input observations.
        statistic (StatisticName): Statistic to bootstrap.
        n_resamples (int): Number of bootstrap samples.
        seed (Optional[int]): Random seed for reproducibility.
        title (Optional[str]): Optional chart title.
        figsize (FigureSize): Matplotlib figure size.
        color (Optional[str]: Histogram color.

    Returns:
        matplotlib.axes.Axes: Axes containing the bootstrap distribution.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If options are invalid.

    Examples:
        ```python
        ax = bootstrap_distribution_plot_static(data)
        ```

    Notes:
        The original-sample statistic is shown as a vertical reference line.
    """
    distribution = bootstrap_distribution(data, statistic=statistic, n_resamples=n_resamples, seed=seed)
    estimate = _statistic_function(statistic)(as_numeric_series(data).to_numpy(dtype=float))
    ax = setup_plot(title=title or f"Bootstrap Distribution ({statistic})", xlabel=statistic, ylabel="Frequency", figsize=figsize)[1]
    ax.hist(distribution, bins="auto", color=color, alpha=0.7, edgecolor="black")
    ax.axvline(estimate, color="crimson", linestyle="--", label="Estimate")
    ax.legend()
    return ax


def bootstrap_distribution_plot_interactive(
    data: SeriesLike,
    statistic: StatisticName = "mean",
    n_resamples: int = 1000,
    seed: Optional[int] = None,
    title: Optional[str] = None,
    color: Optional[str] = None,
    template: str = "plotly",
    height: int = 600,
    width: int = 1000,
) -> PlotlyFigure:
    """Create an interactive histogram of bootstrap statistic values.

    Args:
        data (SeriesLike): Input observations.
        statistic (StatisticName): Statistic to bootstrap.
        n_resamples (int): Number of bootstrap samples.
        seed (Optional[int]): Random seed for reproducibility.
        title (Optional[str]): Optional chart title.
        color (Optional[str]: Histogram color.
        template (str): Plotly template name.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.

    Returns:
        plotly.graph_objects.Figure: Interactive bootstrap distribution.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If options are invalid.

    Examples:
        ```python
        fig = bootstrap_distribution_plot_interactive(data)
        ```

    Notes:
        The original-sample statistic is shown as a vertical reference line.
    """
    distribution = bootstrap_distribution(data, statistic=statistic, n_resamples=n_resamples, seed=seed)
    estimate = _statistic_function(statistic)(as_numeric_series(data).to_numpy(dtype=float))
    fig = go.Figure(go.Histogram(x=distribution, marker_color=color, opacity=0.7))
    fig.add_vline(x=estimate, line_color="crimson", line_dash="dash", annotation_text="Estimate")
    fig.update_layout(title=title or f"Bootstrap Distribution ({statistic})", xaxis_title=statistic, yaxis_title="Frequency", template=template, height=height, width=width)
    return fig

