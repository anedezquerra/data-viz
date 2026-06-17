"""Robust univariate statistics, transformations, and visual summaries."""

from dataclasses import dataclass
from typing import Optional

import numpy as np
import pandas as pd
import plotly.graph_objects as go
from scipy import stats

from ..types import FigureSize, MatplotlibAxes, PlotlyFigure, SeriesLike
from ..utils import apply_theme, setup_plot
from .stats import as_numeric_series


@dataclass(frozen=True)
class RobustStats:
    """Robust summary statistics for one numeric variable.

    Args:
        count (int): Number of non-missing numeric observations.
        median (float): Median value.
        mad (float): Median absolute deviation from the median.
        scaled_mad (float): MAD scaled by ``1.4826`` for normal consistency.
        trimmed_mean (float): Mean after trimming both tails.
        winsorized_mean (float): Mean after winsorizing both tails.
        q1 (float): First quartile.
        q3 (float): Third quartile.
        iqr (float): Interquartile range.
        lower_fence (float): Tukey lower outlier fence.
        upper_fence (float): Tukey upper outlier fence.

    Returns:
        RobustStats: Immutable robust summary record.

    Raises:
        TypeError: If values cannot be represented by the declared fields.
        ValueError: If values are incompatible with downstream numeric use.

    Examples:
        ```python
        summary = RobustStats(5, 3.0, 1.0, 1.4826, 3.0, 3.0, 2.0, 4.0, 2.0, -1.0, 7.0)
        ```

    Notes:
        Robust summaries are less sensitive to heavy tails and isolated extreme observations.
    """

    count: int
    median: float
    mad: float
    scaled_mad: float
    trimmed_mean: float
    winsorized_mean: float
    q1: float
    q3: float
    iqr: float
    lower_fence: float
    upper_fence: float


def validate_proportion(value: float, name: str) -> None:
    """Validate a tail proportion.

    Args:
        value (float): Proportion value to validate.
        name (str): Parameter name used in error messages.

    Returns:
        None: The function returns only when validation succeeds.

    Raises:
        TypeError: If ``value`` is not numeric.
        ValueError: If ``value`` is outside the half-open ``[0, 0.5)`` interval.

    Examples:
        ```python
        validate_proportion(0.1, "proportion")
        ```

    Notes:
        Trimming or winsorizing at 50 percent would remove all center information.
    """
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be numeric.")
    if value < 0 or value >= 0.5:
        raise ValueError(f"{name} must be greater than or equal to 0 and less than 0.5.")


def mad_zscores(data: SeriesLike, scale: float = 1.4826) -> pd.Series:
    """Compute robust z-scores using the median absolute deviation.

    Args:
        data (SeriesLike): Input observations.
        scale (float): MAD scaling constant.

    Returns:
        pandas.Series: Robust z-scores aligned to cleaned numeric observations.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If ``scale`` is not positive or no observations remain.

    Examples:
        ```python
        scores = mad_zscores([1, 2, 3, 100])
        ```

    Notes:
        A zero MAD returns zeros because robust spread cannot be estimated.
    """
    if scale <= 0:
        raise ValueError("scale must be positive.")
    values = as_numeric_series(data)
    median = values.median()
    mad = (values - median).abs().median()
    if mad == 0:
        return pd.Series(0.0, index=values.index, name="mad_zscore")
    return pd.Series((values - median) / (scale * mad), index=values.index, name="mad_zscore")


def mad_outliers(data: SeriesLike, threshold: float = 3.5) -> pd.Series:
    """Flag observations with large robust MAD z-scores.

    Args:
        data (SeriesLike): Input observations.
        threshold (float): Absolute MAD z-score threshold.

    Returns:
        pandas.Series: Boolean mask where ``True`` marks a robust outlier.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If ``threshold`` is not positive or no observations remain.

    Examples:
        ```python
        mask = mad_outliers([1, 2, 3, 100])
        ```

    Notes:
        MAD outliers are useful when the mean and standard deviation are distorted by extremes.
    """
    if threshold <= 0:
        raise ValueError("threshold must be positive.")
    return mad_zscores(data).abs() > threshold


def trimmed_mean(data: SeriesLike, proportion: float = 0.1) -> float:
    """Compute the trimmed mean after dropping both tails.

    Args:
        data (SeriesLike): Input observations.
        proportion (float): Fraction trimmed from each tail.

    Returns:
        float: Trimmed arithmetic mean.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If ``proportion`` is invalid or no observations remain.

    Examples:
        ```python
        value = trimmed_mean(data, proportion=0.1)
        ```

    Notes:
        This function uses SciPy's ``trim_mean`` implementation.
    """
    validate_proportion(proportion, "proportion")
    values = as_numeric_series(data)
    return float(stats.trim_mean(values.to_numpy(dtype=float), proportion))


def winsorize_series(data: SeriesLike, limits: float = 0.05) -> pd.Series:
    """Winsorize a numeric series by clipping both tails.

    Args:
        data (SeriesLike): Input observations.
        limits (float): Fraction clipped from each tail.

    Returns:
        pandas.Series: Winsorized observations.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If ``limits`` is invalid or no observations remain.

    Examples:
        ```python
        clipped = winsorize_series(data, limits=0.05)
        ```

    Notes:
        Winsorization preserves the sample size while reducing tail influence.
    """
    validate_proportion(limits, "limits")
    values = as_numeric_series(data)
    lower = float(values.quantile(limits))
    upper = float(values.quantile(1 - limits))
    return values.clip(lower=lower, upper=upper)


def robust_summary(
    data: SeriesLike,
    trim_proportion: float = 0.1,
    winsor_limits: float = 0.05,
    fence_multiplier: float = 1.5,
) -> RobustStats:
    """Compute robust summary statistics for one numeric variable.

    Args:
        data (SeriesLike): Input observations.
        trim_proportion (float): Fraction trimmed from each tail for the trimmed mean.
        winsor_limits (float): Fraction winsorized from each tail for the winsorized mean.
        fence_multiplier (float): IQR multiplier used for Tukey fences.

    Returns:
        RobustStats: Robust center, spread, and fence summary.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If proportions or fence multiplier are invalid.

    Examples:
        ```python
        summary = robust_summary(data)
        ```

    Notes:
        Robust summaries complement, rather than replace, classical descriptive statistics.
    """
    if fence_multiplier <= 0:
        raise ValueError("fence_multiplier must be positive.")
    values = as_numeric_series(data)
    median = float(values.median())
    mad = float((values - median).abs().median())
    q1 = float(values.quantile(0.25))
    q3 = float(values.quantile(0.75))
    iqr = q3 - q1
    return RobustStats(
        count=int(values.count()),
        median=median,
        mad=mad,
        scaled_mad=float(1.4826 * mad),
        trimmed_mean=trimmed_mean(values, trim_proportion),
        winsorized_mean=float(winsorize_series(values, winsor_limits).mean()),
        q1=q1,
        q3=q3,
        iqr=float(iqr),
        lower_fence=float(q1 - fence_multiplier * iqr),
        upper_fence=float(q3 + fence_multiplier * iqr),
    )


def robust_location_plot_static(
    data: SeriesLike,
    title: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    color: Optional[str] = None,
    median_color: str = "crimson",
    trimmed_color: str = "darkgreen",
    winsor_color: str = "darkorange",
    theme: str = "default",
) -> MatplotlibAxes:
    """Create a static histogram with robust location reference lines.

    Args:
        data (SeriesLike): Input observations.
        title (Optional[str]): Optional chart title.
        figsize (FigureSize): Matplotlib figure size.
        color (Optional[str]): Histogram color.
        median_color (str): Median reference line color.
        trimmed_color (str): Trimmed mean reference line color.
        winsor_color (str): Winsorized mean reference line color.
        theme (str): Styling theme name.

    Returns:
        matplotlib.axes.Axes: Axes containing histogram and robust reference lines.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If robust statistics cannot be computed.

    Examples:
        ```python
        ax = robust_location_plot_static(data)
        ```

    Notes:
        The plot makes disagreements between classical and robust centers easy to see.
    """
    values = as_numeric_series(data)
    summary = robust_summary(values)
    ax = setup_plot(title=title or "Robust Location Summary", xlabel=values.name, ylabel="Frequency", figsize=figsize)[1]
    ax.hist(values, bins="auto", color=color, alpha=0.7, edgecolor="black")
    ax.axvline(summary.median, color=median_color, linestyle="-", label="Median")
    ax.axvline(summary.trimmed_mean, color=trimmed_color, linestyle="--", label="Trimmed mean")
    ax.axvline(summary.winsorized_mean, color=winsor_color, linestyle=":", label="Winsorized mean")
    ax.legend()
    ax.grid(True, axis="y", alpha=0.3)
    apply_theme(ax, theme)
    return ax


def robust_location_plot_interactive(
    data: SeriesLike,
    title: Optional[str] = None,
    color: Optional[str] = None,
    median_color: str = "crimson",
    trimmed_color: str = "darkgreen",
    winsor_color: str = "darkorange",
    template: str = "plotly",
    height: int = 600,
    width: int = 1000,
) -> PlotlyFigure:
    """Create an interactive histogram with robust location reference lines.

    Args:
        data (SeriesLike): Input observations.
        title (Optional[str]): Optional chart title.
        color (Optional[str]): Histogram color.
        median_color (str): Median reference line color.
        trimmed_color (str): Trimmed mean reference line color.
        winsor_color (str): Winsorized mean reference line color.
        template (str): Plotly template name.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.

    Returns:
        plotly.graph_objects.Figure: Interactive robust location chart.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If robust statistics cannot be computed.

    Examples:
        ```python
        fig = robust_location_plot_interactive(data)
        ```

    Notes:
        Reference lines are added as Plotly layout shapes.
    """
    values = as_numeric_series(data)
    summary = robust_summary(values)
    fig = go.Figure(go.Histogram(x=values, marker_color=color, opacity=0.7, name="Distribution"))
    for value, label, line_color, dash in [
        (summary.median, "Median", median_color, "solid"),
        (summary.trimmed_mean, "Trimmed mean", trimmed_color, "dash"),
        (summary.winsorized_mean, "Winsorized mean", winsor_color, "dot"),
    ]:
        fig.add_vline(x=value, line_color=line_color, line_dash=dash, annotation_text=label)
    fig.update_layout(
        title=title or "Robust Location Summary",
        xaxis_title=values.name,
        yaxis_title="Frequency",
        template=template,
        height=height,
        width=width,
    )
    return fig
