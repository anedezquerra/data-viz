"""Weighted univariate statistics and visualizations."""

from dataclasses import dataclass
from typing import Optional, Tuple

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objects as go

from ..types import FigureSize, MatplotlibAxes, PlotlyFigure, SeriesLike
from ..utils import apply_theme, setup_plot, validate_positive_int
from .stats import as_numeric_series


@dataclass(frozen=True)
class WeightedStats:
    """Weighted summary statistics for one numeric variable.

    Args:
        count (int): Number of observations after missing-value removal.
        weight_sum (float): Sum of non-negative weights.
        mean (float): Weighted arithmetic mean.
        variance (float): Weighted population variance.
        std (float): Weighted population standard deviation.
        q1 (float): Weighted first quartile.
        median (float): Weighted median.
        q3 (float): Weighted third quartile.

    Returns:
        WeightedStats: Immutable weighted summary record.

    Raises:
        TypeError: If values cannot be represented by the declared fields.
        ValueError: If summary values are incompatible with downstream numeric use.

    Examples:
        ```python
        stats = WeightedStats(3, 6.0, 2.3, 0.5, 0.7, 1.0, 2.0, 3.0)
        ```

    Notes:
        Weighted summaries are useful for survey data, grouped data, and importance-weighted samples.
    """

    count: int
    weight_sum: float
    mean: float
    variance: float
    std: float
    q1: float
    median: float
    q3: float


def resolve_weighted_series(data: SeriesLike, weights: SeriesLike) -> Tuple[pd.Series, pd.Series]:
    """Resolve values and weights into aligned numeric Series.

    Args:
        data (SeriesLike): Input observations.
        weights (SeriesLike): Non-negative observation weights.

    Returns:
        tuple[pandas.Series, pandas.Series]: Cleaned values and aligned weights.

    Raises:
        TypeError: If values or weights cannot be converted to numeric data.
        ValueError: If lengths differ, weights are negative, or total weight is not positive.

    Examples:
        ```python
        values, weights = resolve_weighted_series([1, 2], [0.4, 0.6])
        ```

    Notes:
        Rows with missing values or missing weights are removed together.
    """
    values = pd.to_numeric(pd.Series(data, name="Value"), errors="raise")
    weight_values = pd.to_numeric(pd.Series(weights, name="Weight"), errors="raise")
    if len(values) != len(weight_values):
        raise ValueError("data and weights must have the same length.")
    frame = pd.DataFrame({"value": values, "weight": weight_values}).dropna()
    if frame.empty:
        raise ValueError("data and weights must contain at least one complete observation.")
    if (frame["weight"] < 0).any():
        raise ValueError("weights must be non-negative.")
    if frame["weight"].sum() <= 0:
        raise ValueError("weights must sum to a positive value.")
    return frame["value"].reset_index(drop=True), frame["weight"].reset_index(drop=True)


def weighted_quantile(data: SeriesLike, weights: SeriesLike, quantile: float) -> float:
    """Compute a weighted quantile.

    Args:
        data (SeriesLike): Input observations.
        weights (SeriesLike): Non-negative observation weights.
        quantile (float): Desired quantile in the inclusive ``[0, 1]`` range.

    Returns:
        float: Weighted quantile value.

    Raises:
        TypeError: If values or weights cannot be converted to numeric data.
        ValueError: If ``quantile`` is outside ``[0, 1]`` or weights are invalid.

    Examples:
        ```python
        median = weighted_quantile(values, weights, 0.5)
        ```

    Notes:
        The implementation uses the first sorted value whose cumulative weight reaches the target.
    """
    if quantile < 0 or quantile > 1:
        raise ValueError("quantile must be between 0 and 1.")
    values, weight_values = resolve_weighted_series(data, weights)
    order = np.argsort(values.to_numpy(dtype=float))
    sorted_values = values.to_numpy(dtype=float)[order]
    sorted_weights = weight_values.to_numpy(dtype=float)[order]
    cumulative = np.cumsum(sorted_weights)
    cutoff = quantile * cumulative[-1]
    index = int(np.searchsorted(cumulative, cutoff, side="left"))
    return float(sorted_values[min(index, len(sorted_values) - 1)])


def weighted_summary(data: SeriesLike, weights: SeriesLike) -> WeightedStats:
    """Compute weighted summary statistics for one numeric variable.

    Args:
        data (SeriesLike): Input observations.
        weights (SeriesLike): Non-negative observation weights.

    Returns:
        WeightedStats: Weighted center, spread, and quartile summary.

    Raises:
        TypeError: If values or weights cannot be converted to numeric data.
        ValueError: If weights are invalid or no observations remain.

    Examples:
        ```python
        summary = weighted_summary(values, weights)
        ```

    Notes:
        Variance is computed as a weighted population variance.
    """
    values, weight_values = resolve_weighted_series(data, weights)
    value_array = values.to_numpy(dtype=float)
    weight_array = weight_values.to_numpy(dtype=float)
    mean = float(np.average(value_array, weights=weight_array))
    variance = float(np.average((value_array - mean) ** 2, weights=weight_array))
    return WeightedStats(
        count=int(len(values)),
        weight_sum=float(weight_array.sum()),
        mean=mean,
        variance=variance,
        std=float(np.sqrt(variance)),
        q1=weighted_quantile(values, weight_values, 0.25),
        median=weighted_quantile(values, weight_values, 0.5),
        q3=weighted_quantile(values, weight_values, 0.75),
    )


def weighted_histogram_static(
    data: SeriesLike,
    weights: SeriesLike,
    bins: int = 30,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    color: Optional[str] = None,
    theme: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Create a static weighted histogram.

    Args:
        data (SeriesLike): Input observations.
        weights (SeriesLike): Non-negative observation weights.
        bins (int): Number of histogram bins.
        title (Optional[str]): Optional chart title.
        xlabel (Optional[str]): Optional x-axis label.
        figsize (FigureSize): Matplotlib figure size.
        color (Optional[str]: Histogram color.
        theme (str): Styling theme name.
        **kwargs: Additional keyword arguments forwarded to ``Axes.hist``.

    Returns:
        matplotlib.axes.Axes: Axes containing the weighted histogram.

    Raises:
        TypeError: If values or weights cannot be converted to numeric data.
        ValueError: If weights or ``bins`` are invalid.

    Examples:
        ```python
        ax = weighted_histogram_static(values, weights)
        ```

    Notes:
        Weighted histograms are useful when rows represent unequal sample mass.
    """
    validate_positive_int(bins, "bins")
    values, weight_values = resolve_weighted_series(data, weights)
    ax = setup_plot(title=title or "Weighted Histogram", xlabel=xlabel or "Value", ylabel="Weighted Frequency", figsize=figsize)[1]
    ax.hist(values, weights=weight_values, bins=bins, color=color, alpha=0.7, edgecolor="black", **kwargs)
    ax.grid(True, axis="y", alpha=0.3)
    apply_theme(ax, theme)
    return ax


def weighted_histogram_interactive(
    data: SeriesLike,
    weights: SeriesLike,
    bins: int = 30,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    color: Optional[str] = None,
    template: str = "plotly",
    height: int = 600,
    width: int = 1000,
    **kwargs,
) -> PlotlyFigure:
    """Create an interactive weighted histogram.

    Args:
        data (SeriesLike): Input observations.
        weights (SeriesLike): Non-negative observation weights.
        bins (int): Number of histogram bins.
        title (Optional[str]): Optional chart title.
        xlabel (Optional[str]): Optional x-axis label.
        color (Optional[str]: Histogram color.
        template (str): Plotly template name.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.
        **kwargs: Additional keyword arguments forwarded to ``go.Histogram``.

    Returns:
        plotly.graph_objects.Figure: Interactive weighted histogram.

    Raises:
        TypeError: If values or weights cannot be converted to numeric data.
        ValueError: If weights or ``bins`` are invalid.

    Examples:
        ```python
        fig = weighted_histogram_interactive(values, weights)
        ```

    Notes:
        Plotly uses the ``histfunc="sum"`` pattern over supplied weights.
    """
    validate_positive_int(bins, "bins")
    values, weight_values = resolve_weighted_series(data, weights)
    fig = go.Figure(
        go.Histogram(
            x=values,
            y=weight_values,
            histfunc="sum",
            nbinsx=bins,
            marker_color=color,
            opacity=0.7,
            **kwargs,
        )
    )
    fig.update_layout(
        title=title or "Weighted Histogram",
        xaxis_title=xlabel or "Value",
        yaxis_title="Weighted Frequency",
        template=template,
        height=height,
        width=width,
    )
    return fig


def weighted_ecdf_values(data: SeriesLike, weights: SeriesLike) -> Tuple[np.ndarray, np.ndarray]:
    """Compute weighted empirical cumulative distribution values.

    Args:
        data (SeriesLike): Input observations.
        weights (SeriesLike): Non-negative observation weights.

    Returns:
        Tuple[numpy.ndarray, numpy.ndarray]: Sorted values and weighted cumulative probabilities.

    Raises:
        TypeError: If values or weights cannot be converted to numeric data.
        ValueError: If weights are invalid or no observations remain.

    Examples:
        ```python
        x, y = weighted_ecdf_values(values, weights)
        ```

    Notes:
        Weighted probabilities are normalized by the total weight.
    """
    values, weight_values = resolve_weighted_series(data, weights)
    order = np.argsort(values.to_numpy(dtype=float))
    sorted_values = values.to_numpy(dtype=float)[order]
    sorted_weights = weight_values.to_numpy(dtype=float)[order]
    cumulative = np.cumsum(sorted_weights) / sorted_weights.sum()
    return sorted_values, cumulative


def weighted_ecdf_plot_static(
    data: SeriesLike,
    weights: SeriesLike,
    title: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    color: Optional[str] = None,
    theme: str = "default",
) -> MatplotlibAxes:
    """Create a static weighted empirical cumulative distribution plot.

    Args:
        data (SeriesLike): Input observations.
        weights (SeriesLike): Non-negative observation weights.
        title (Optional[str]): Optional chart title.
        figsize (FigureSize): Matplotlib figure size.
        color (Optional[str]): Line color.
        theme (str): Styling theme name.

    Returns:
        matplotlib.axes.Axes: Axes containing the weighted ECDF chart.

    Raises:
        TypeError: If values or weights cannot be converted to numeric data.
        ValueError: If weights are invalid or no observations remain.

    Examples:
        ```python
        ax = weighted_ecdf_plot_static(values, weights)
        ```

    Notes:
        Weighted ECDFs are useful for survey-weighted or importance-weighted samples.
    """
    x_values, probabilities = weighted_ecdf_values(data, weights)
    ax = setup_plot(title=title or "Weighted ECDF", xlabel="Value", ylabel="Weighted Cumulative Probability", figsize=figsize)[1]
    ax.step(x_values, probabilities, where="post", color=color)
    ax.grid(True, alpha=0.3)
    apply_theme(ax, theme)
    return ax


def weighted_ecdf_plot_interactive(
    data: SeriesLike,
    weights: SeriesLike,
    title: Optional[str] = None,
    color: Optional[str] = None,
    template: str = "plotly",
    height: int = 600,
    width: int = 1000,
) -> PlotlyFigure:
    """Create an interactive weighted empirical cumulative distribution plot.

    Args:
        data (SeriesLike): Input observations.
        weights (SeriesLike): Non-negative observation weights.
        title (Optional[str]): Optional chart title.
        color (Optional[str]): Line color.
        template (str): Plotly template name.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.

    Returns:
        plotly.graph_objects.Figure: Interactive weighted ECDF chart.

    Raises:
        TypeError: If values or weights cannot be converted to numeric data.
        ValueError: If weights are invalid or no observations remain.

    Examples:
        ```python
        fig = weighted_ecdf_plot_interactive(values, weights)
        ```

    Notes:
        The line shape uses horizontal-vertical steps.
    """
    x_values, probabilities = weighted_ecdf_values(data, weights)
    fig = go.Figure(go.Scatter(x=x_values, y=probabilities, mode="lines", line=dict(color=color, shape="hv")))
    fig.update_layout(title=title or "Weighted ECDF", xaxis_title="Value", yaxis_title="Weighted Cumulative Probability", template=template, height=height, width=width)
    return fig
