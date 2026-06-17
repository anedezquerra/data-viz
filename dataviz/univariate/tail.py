"""Tail, survival, and concentration analysis for univariate data."""

from dataclasses import dataclass
from typing import Optional, Tuple

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objects as go

from ..types import FigureSize, MatplotlibAxes, PlotlyFigure, SeriesLike
from ..utils import apply_theme, setup_plot
from .stats import as_numeric_series


@dataclass(frozen=True)
class ConcentrationStats:
    """Concentration statistics for non-negative values.

    Args:
        total (float): Sum of non-negative values.
        gini (float): Gini coefficient.
        top_10_share (float): Share contributed by the largest 10 percent of observations.
        top_20_share (float): Share contributed by the largest 20 percent of observations.

    Returns:
        ConcentrationStats: Immutable inequality and concentration summary.

    Raises:
        TypeError: If values cannot be represented by the declared fields.
        ValueError: If rates are incompatible with downstream numeric use.

    Examples:
        ```python
        stats = ConcentrationStats(100.0, 0.25, 0.4, 0.6)
        ```

    Notes:
        Concentration metrics assume non-negative values.
    """

    total: float
    gini: float
    top_10_share: float
    top_20_share: float


def survival_values(data: SeriesLike) -> Tuple[np.ndarray, np.ndarray]:
    """Compute empirical survival curve values.

    Args:
        data (SeriesLike): Input observations.

    Returns:
        tuple[numpy.ndarray, numpy.ndarray]: Sorted values and survival probabilities.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If no observations remain.

    Examples:
        ```python
        x, survival = survival_values(data)
        ```

    Notes:
        Survival probability is estimated as ``1 - ECDF`` with rank-based plotting positions.
    """
    values = np.sort(as_numeric_series(data).to_numpy(dtype=float))
    probabilities = 1 - (np.arange(1, len(values) + 1) / len(values))
    return values, probabilities


def exceedance_table(data: SeriesLike, thresholds: SeriesLike) -> pd.DataFrame:
    """Compute exceedance counts and rates for thresholds.

    Args:
        data (SeriesLike): Input observations.
        thresholds (SeriesLike): Threshold values.

    Returns:
        pandas.DataFrame: Threshold, exceedance count, and exceedance rate columns.

    Raises:
        TypeError: If data or thresholds cannot be converted to numeric values.
        ValueError: If no observations or thresholds remain.

    Examples:
        ```python
        table = exceedance_table(values, [10, 20, 30])
        ```

    Notes:
        Exceedance means strictly greater than the threshold.
    """
    values = as_numeric_series(data)
    threshold_values = as_numeric_series(thresholds, name="Threshold")
    rows = []
    for threshold in threshold_values:
        count = int((values > threshold).sum())
        rows.append({"threshold": float(threshold), "count": count, "rate": float(count / len(values))})
    return pd.DataFrame(rows)


def concentration_summary(data: SeriesLike) -> ConcentrationStats:
    """Compute Gini and top-share concentration statistics.

    Args:
        data (SeriesLike): Input non-negative observations.

    Returns:
        ConcentrationStats: Total, Gini coefficient, and top-share metrics.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If values contain negatives or sum to zero.

    Examples:
        ```python
        summary = concentration_summary(revenue)
        ```

    Notes:
        Values are sorted ascending for Gini and descending for top-share calculations.
    """
    values = as_numeric_series(data).to_numpy(dtype=float)
    if (values < 0).any():
        raise ValueError("concentration metrics require non-negative values.")
    total = float(values.sum())
    if total <= 0:
        raise ValueError("values must sum to a positive total.")
    sorted_values = np.sort(values)
    n = len(sorted_values)
    gini = float((2 * np.sum(np.arange(1, n + 1) * sorted_values)) / (n * total) - (n + 1) / n)
    descending = sorted_values[::-1]

    def top_share(proportion: float) -> float:
        """Compute the share contributed by the largest observations.

        Args:
            proportion (float): Population proportion to include from the top tail.

        Returns:
            float: Share of total value contributed by the requested top proportion.

        Raises:
            TypeError: If ``proportion`` is not numeric.
            ValueError: If the proportion produces an invalid slice.

        Examples:
            ```python
            share = top_share(0.1)
            ```

        Notes:
            At least one observation is included for small samples.
        """
        count = max(1, int(np.ceil(proportion * n)))
        return float(descending[:count].sum() / total)

    return ConcentrationStats(total=total, gini=gini, top_10_share=top_share(0.1), top_20_share=top_share(0.2))


def lorenz_curve_values(data: SeriesLike) -> Tuple[np.ndarray, np.ndarray]:
    """Compute Lorenz curve coordinates for non-negative values.

    Args:
        data (SeriesLike): Input non-negative observations.

    Returns:
        tuple[numpy.ndarray, numpy.ndarray]: Cumulative population share and cumulative value share.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If values contain negatives or sum to zero.

    Examples:
        ```python
        population, value_share = lorenz_curve_values(values)
        ```

    Notes:
        The curve starts at ``(0, 0)`` and ends at ``(1, 1)``.
    """
    values = as_numeric_series(data).to_numpy(dtype=float)
    if (values < 0).any():
        raise ValueError("Lorenz curves require non-negative values.")
    total = float(values.sum())
    if total <= 0:
        raise ValueError("values must sum to a positive total.")
    sorted_values = np.sort(values)
    cumulative_values = np.concatenate([[0.0], np.cumsum(sorted_values) / total])
    population = np.linspace(0, 1, len(cumulative_values))
    return population, cumulative_values


def survival_curve_static(
    data: SeriesLike,
    title: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    color: Optional[str] = None,
    theme: str = "default",
) -> MatplotlibAxes:
    """Create a static empirical survival curve.

    Args:
        data (SeriesLike): Input observations.
        title (Optional[str]): Optional chart title.
        figsize (FigureSize): Matplotlib figure size.
        color (Optional[str]: Line color.
        theme (str): Styling theme name.

    Returns:
        matplotlib.axes.Axes: Axes containing the survival curve.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If no observations remain.

    Examples:
        ```python
        ax = survival_curve_static(data)
        ```

    Notes:
        Survival curves emphasize upper-tail probability.
    """
    x_values, survival = survival_values(data)
    ax = setup_plot(title=title or "Survival Curve", xlabel="Value", ylabel="Survival Probability", figsize=figsize)[1]
    ax.step(x_values, survival, where="post", color=color)
    ax.grid(True, alpha=0.3)
    apply_theme(ax, theme)
    return ax


def survival_curve_interactive(
    data: SeriesLike,
    title: Optional[str] = None,
    color: Optional[str] = None,
    template: str = "plotly",
    height: int = 600,
    width: int = 1000,
) -> PlotlyFigure:
    """Create an interactive empirical survival curve.

    Args:
        data (SeriesLike): Input observations.
        title (Optional[str]): Optional chart title.
        color (Optional[str]: Line color.
        template (str): Plotly template name.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.

    Returns:
        plotly.graph_objects.Figure: Interactive survival curve.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If no observations remain.

    Examples:
        ```python
        fig = survival_curve_interactive(data)
        ```

    Notes:
        The line uses horizontal-vertical steps for empirical survival.
    """
    x_values, survival = survival_values(data)
    fig = go.Figure(go.Scatter(x=x_values, y=survival, mode="lines", line=dict(color=color, shape="hv")))
    fig.update_layout(title=title or "Survival Curve", xaxis_title="Value", yaxis_title="Survival Probability", template=template, height=height, width=width)
    return fig


def lorenz_curve_static(
    data: SeriesLike,
    title: Optional[str] = None,
    figsize: FigureSize = (8, 8),
    color: Optional[str] = None,
    reference_color: str = "gray",
    theme: str = "default",
) -> MatplotlibAxes:
    """Create a static Lorenz curve.

    Args:
        data (SeriesLike): Input non-negative observations.
        title (Optional[str]): Optional chart title.
        figsize (FigureSize): Matplotlib figure size.
        color (Optional[str]: Curve color.
        reference_color (str): Equality reference line color.
        theme (str): Styling theme name.

    Returns:
        matplotlib.axes.Axes: Axes containing the Lorenz curve.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If values contain negatives or sum to zero.

    Examples:
        ```python
        ax = lorenz_curve_static(values)
        ```

    Notes:
        The farther the curve lies below equality, the higher the concentration.
    """
    population, value_share = lorenz_curve_values(data)
    ax = setup_plot(title=title or "Lorenz Curve", xlabel="Cumulative Population Share", ylabel="Cumulative Value Share", figsize=figsize)[1]
    ax.plot(population, value_share, color=color, label="Lorenz")
    ax.plot([0, 1], [0, 1], color=reference_color, linestyle="--", label="Equality")
    ax.legend()
    ax.grid(True, alpha=0.3)
    apply_theme(ax, theme)
    return ax


def lorenz_curve_interactive(
    data: SeriesLike,
    title: Optional[str] = None,
    color: Optional[str] = None,
    reference_color: str = "gray",
    template: str = "plotly",
    height: int = 700,
    width: int = 700,
) -> PlotlyFigure:
    """Create an interactive Lorenz curve.

    Args:
        data (SeriesLike): Input non-negative observations.
        title (Optional[str]): Optional chart title.
        color (Optional[str]: Curve color.
        reference_color (str): Equality reference line color.
        template (str): Plotly template name.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.

    Returns:
        plotly.graph_objects.Figure: Interactive Lorenz curve.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If values contain negatives or sum to zero.

    Examples:
        ```python
        fig = lorenz_curve_interactive(values)
        ```

    Notes:
        The equality reference line represents perfectly even distribution.
    """
    population, value_share = lorenz_curve_values(data)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=population, y=value_share, mode="lines", line=dict(color=color), name="Lorenz"))
    fig.add_trace(go.Scatter(x=[0, 1], y=[0, 1], mode="lines", line=dict(color=reference_color, dash="dash"), name="Equality"))
    fig.update_layout(title=title or "Lorenz Curve", xaxis_title="Cumulative Population Share", yaxis_title="Cumulative Value Share", template=template, height=height, width=width)
    return fig
