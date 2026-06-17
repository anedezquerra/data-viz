"""Univariate data quality summaries and visualizations."""

from dataclasses import dataclass
from typing import Optional

import pandas as pd
import plotly.graph_objects as go

from ..types import FigureSize, MatplotlibAxes, PlotlyFigure, SeriesLike
from ..utils import apply_theme, setup_plot


@dataclass(frozen=True)
class DataQualitySummary:
    """Univariate data quality summary.

    Args:
        count (int): Total number of observations.
        missing (int): Number of missing observations.
        missing_rate (float): Share of observations that are missing.
        unique (int): Number of unique non-missing values.
        duplicate_rate (float): Share of non-missing observations that repeat a previous value.
        zero_rate (float): Share of numeric observations equal to zero.
        negative_rate (float): Share of numeric observations below zero.

    Returns:
        DataQualitySummary: Immutable data quality profile.

    Raises:
        TypeError: If values cannot be represented by the declared fields.
        ValueError: If rates are incompatible with downstream numeric use.

    Examples:
        ```python
        profile = DataQualitySummary(10, 1, 0.1, 4, 0.5, 0.2, 0.1)
        ```

    Notes:
        Numeric-only rates are zero when no numeric observations are available.
    """

    count: int
    missing: int
    missing_rate: float
    unique: int
    duplicate_rate: float
    zero_rate: float
    negative_rate: float


def data_quality_summary(data: SeriesLike) -> DataQualitySummary:
    """Compute basic data quality metrics for one variable.

    Args:
        data (SeriesLike): Input observations.

    Returns:
        DataQualitySummary: Missingness, uniqueness, duplicate, zero, and negative rates.

    Raises:
        TypeError: If input data cannot be represented as a pandas Series.
        ValueError: If the input has no observations.

    Examples:
        ```python
        summary = data_quality_summary(series)
        ```

    Notes:
        This summary is intentionally type-tolerant so it works for numeric and categorical variables.
    """
    series = pd.Series(data)
    if len(series) == 0:
        raise ValueError("data must contain at least one observation.")
    non_missing = series.dropna()
    numeric = pd.to_numeric(non_missing, errors="coerce").dropna()
    numeric_count = len(numeric)
    duplicate_count = int(non_missing.duplicated().sum())
    return DataQualitySummary(
        count=int(len(series)),
        missing=int(series.isna().sum()),
        missing_rate=float(series.isna().mean()),
        unique=int(non_missing.nunique()),
        duplicate_rate=float(duplicate_count / len(non_missing)) if len(non_missing) else 0.0,
        zero_rate=float((numeric == 0).mean()) if numeric_count else 0.0,
        negative_rate=float((numeric < 0).mean()) if numeric_count else 0.0,
    )


def quality_bar_static(
    data: SeriesLike,
    title: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    color: Optional[str] = None,
    theme: str = "default",
) -> MatplotlibAxes:
    """Create a static bar chart of univariate quality rates.

    Args:
        data (SeriesLike): Input observations.
        title (Optional[str]): Optional chart title.
        figsize (FigureSize): Matplotlib figure size.
        color (Optional[str]: Bar color.
        theme (str): Styling theme name.

    Returns:
        matplotlib.axes.Axes: Axes containing quality-rate bars.

    Raises:
        TypeError: If input data cannot be represented as a pandas Series.
        ValueError: If the input has no observations.

    Examples:
        ```python
        ax = quality_bar_static(series)
        ```

    Notes:
        Rates are shown on the inclusive ``[0, 1]`` scale.
    """
    summary = data_quality_summary(data)
    labels = ["Missing", "Duplicate", "Zero", "Negative"]
    values = [summary.missing_rate, summary.duplicate_rate, summary.zero_rate, summary.negative_rate]
    ax = setup_plot(title=title or "Data Quality Rates", xlabel="Metric", ylabel="Rate", figsize=figsize)[1]
    ax.bar(labels, values, color=color)
    ax.set_ylim(0, 1)
    ax.grid(True, axis="y", alpha=0.3)
    apply_theme(ax, theme)
    return ax


def quality_bar_interactive(
    data: SeriesLike,
    title: Optional[str] = None,
    color: Optional[str] = None,
    template: str = "plotly",
    height: int = 600,
    width: int = 1000,
) -> PlotlyFigure:
    """Create an interactive bar chart of univariate quality rates.

    Args:
        data (SeriesLike): Input observations.
        title (Optional[str]): Optional chart title.
        color (Optional[str]: Bar color.
        template (str): Plotly template name.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.

    Returns:
        plotly.graph_objects.Figure: Interactive quality-rate chart.

    Raises:
        TypeError: If input data cannot be represented as a pandas Series.
        ValueError: If the input has no observations.

    Examples:
        ```python
        fig = quality_bar_interactive(series)
        ```

    Notes:
        Quality rates provide a quick screen before selecting downstream visualizations.
    """
    summary = data_quality_summary(data)
    labels = ["Missing", "Duplicate", "Zero", "Negative"]
    values = [summary.missing_rate, summary.duplicate_rate, summary.zero_rate, summary.negative_rate]
    fig = go.Figure(go.Bar(x=labels, y=values, marker_color=color))
    fig.update_layout(title=title or "Data Quality Rates", xaxis_title="Metric", yaxis_title="Rate", yaxis=dict(range=[0, 1]), template=template, height=height, width=width)
    return fig


def sentinel_value_counts(data: SeriesLike, sentinels: SeriesLike) -> pd.Series:
    """Count configured sentinel values in one variable.

    Args:
        data (SeriesLike): Input observations.
        sentinels (SeriesLike): Values that should be treated as sentinel markers.

    Returns:
        pandas.Series: Counts indexed by sentinel value.

    Raises:
        TypeError: If input data cannot be represented as pandas Series.
        ValueError: If no sentinel values are provided.

    Examples:
        ```python
        counts = sentinel_value_counts(values, [-999, "N/A"])
        ```

    Notes:
        Sentinel values are counted before any type coercion.
    """
    sentinel_series = pd.Series(sentinels).dropna()
    if sentinel_series.empty:
        raise ValueError("sentinels must contain at least one value.")
    series = pd.Series(data)
    return pd.Series({sentinel: int((series == sentinel).sum()) for sentinel in sentinel_series})


def sentinel_rate(data: SeriesLike, sentinels: SeriesLike) -> float:
    """Compute the rate of values matching configured sentinels.

    Args:
        data (SeriesLike): Input observations.
        sentinels (SeriesLike): Values that should be treated as sentinel markers.

    Returns:
        float: Share of observations matching any sentinel value.

    Raises:
        TypeError: If input data cannot be represented as pandas Series.
        ValueError: If no observations or sentinels are provided.

    Examples:
        ```python
        rate = sentinel_rate(values, [-999])
        ```

    Notes:
        This helper catches common data-quality placeholders that are not missing values.
    """
    series = pd.Series(data)
    if series.empty:
        raise ValueError("data must contain at least one observation.")
    counts = sentinel_value_counts(series, sentinels)
    return float(counts.sum() / len(series))
