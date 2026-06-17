"""Datetime-oriented univariate visualizations and event summaries."""

from typing import Literal, Optional

import pandas as pd
import plotly.graph_objects as go

from ..types import FigureSize, MatplotlibAxes, PlotlyFigure, SeriesLike
from ..utils import apply_theme, setup_plot

DatetimeFreq = Literal["D", "W", "M", "Q", "Y", "H"]


def as_datetime_series(data: SeriesLike, name: str = "Timestamp") -> pd.Series:
    """Convert series-like values to a clean datetime Series.

    Args:
        data (SeriesLike): Input datetime-like observations.
        name (str): Fallback series name.

    Returns:
        pandas.Series: Datetime observations sorted ascending.

    Raises:
        TypeError: If values cannot be converted to datetimes.
        ValueError: If no valid datetime observations remain.

    Examples:
        ```python
        timestamps = as_datetime_series(["2026-01-01", "2026-01-02"])
        ```

    Notes:
        Missing and unparseable timestamps are removed after coercion.
    """
    series = data if isinstance(data, pd.Series) else pd.Series(data, name=name)
    if series.name is None:
        series = series.rename(name)
    converted = pd.to_datetime(series, errors="coerce").dropna().sort_values()
    if converted.empty:
        raise ValueError("data must contain at least one valid datetime value.")
    return converted.reset_index(drop=True)


def event_counts(data: SeriesLike, freq: DatetimeFreq = "D") -> pd.Series:
    """Count datetime events per calendar frequency.

    Args:
        data (SeriesLike): Input datetime-like observations.
        freq (DatetimeFreq): Pandas resampling frequency.

    Returns:
        pandas.Series: Event counts indexed by period start timestamp.

    Raises:
        TypeError: If values cannot be converted to datetimes.
        ValueError: If no valid datetime observations remain.

    Examples:
        ```python
        counts = event_counts(timestamps, freq="W")
        ```

    Notes:
        The result includes empty periods between the first and last observation.
    """
    timestamps = as_datetime_series(data)
    return timestamps.to_frame("event").assign(count=1).set_index("event")["count"].resample(freq).sum().astype(int)


def event_frequency_plot_static(
    data: SeriesLike,
    freq: DatetimeFreq = "D",
    title: Optional[str] = None,
    xlabel: str = "Time",
    ylabel: str = "Event Count",
    figsize: FigureSize = (10, 6),
    color: Optional[str] = None,
    theme: str = "default",
) -> MatplotlibAxes:
    """Create a static event frequency chart from datetime observations.

    Args:
        data (SeriesLike): Input datetime-like observations.
        freq (DatetimeFreq): Pandas resampling frequency.
        title (Optional[str]): Optional chart title.
        xlabel (str): X-axis label.
        ylabel (str): Y-axis label.
        figsize (FigureSize): Matplotlib figure size.
        color (Optional[str]): Line color.
        theme (str): Styling theme name.

    Returns:
        matplotlib.axes.Axes: Axes containing the event frequency chart.

    Raises:
        TypeError: If values cannot be converted to datetimes.
        ValueError: If no valid datetime observations remain.

    Examples:
        ```python
        ax = event_frequency_plot_static(timestamps, freq="M")
        ```

    Notes:
        This view is useful for one-dimensional event streams.
    """
    counts = event_counts(data, freq=freq)
    ax = setup_plot(title=title or "Event Frequency", xlabel=xlabel, ylabel=ylabel, figsize=figsize)[1]
    ax.plot(counts.index, counts.to_numpy(), color=color, marker="o")
    ax.grid(True, alpha=0.3)
    apply_theme(ax, theme)
    return ax


def event_frequency_plot_interactive(
    data: SeriesLike,
    freq: DatetimeFreq = "D",
    title: Optional[str] = None,
    xlabel: str = "Time",
    ylabel: str = "Event Count",
    color: Optional[str] = None,
    template: str = "plotly",
    height: int = 600,
    width: int = 1000,
) -> PlotlyFigure:
    """Create an interactive event frequency chart from datetime observations.

    Args:
        data (SeriesLike): Input datetime-like observations.
        freq (DatetimeFreq): Pandas resampling frequency.
        title (Optional[str]): Optional chart title.
        xlabel (str): X-axis label.
        ylabel (str): Y-axis label.
        color (Optional[str]): Line color.
        template (str): Plotly template name.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.

    Returns:
        plotly.graph_objects.Figure: Interactive event frequency chart.

    Raises:
        TypeError: If values cannot be converted to datetimes.
        ValueError: If no valid datetime observations remain.

    Examples:
        ```python
        fig = event_frequency_plot_interactive(timestamps)
        ```

    Notes:
        Hover labels expose period-level event counts.
    """
    counts = event_counts(data, freq=freq)
    fig = go.Figure(go.Scatter(x=counts.index, y=counts.to_numpy(), mode="lines+markers", line=dict(color=color)))
    fig.update_layout(title=title or "Event Frequency", xaxis_title=xlabel, yaxis_title=ylabel, template=template, height=height, width=width)
    return fig


def interarrival_times(data: SeriesLike, unit: str = "D") -> pd.Series:
    """Compute elapsed time between consecutive datetime observations.

    Args:
        data (SeriesLike): Input datetime-like observations.
        unit (str): Output unit accepted by pandas timedeltas, such as ``"D"`` or ``"h"``.

    Returns:
        pandas.Series: Interarrival durations in the requested unit.

    Raises:
        TypeError: If values cannot be converted to datetimes.
        ValueError: If fewer than two datetime observations are available.

    Examples:
        ```python
        gaps = interarrival_times(timestamps, unit="h")
        ```

    Notes:
        Durations are computed after sorting timestamps ascending.
    """
    timestamps = as_datetime_series(data)
    if len(timestamps) < 2:
        raise ValueError("At least two datetime observations are required.")
    deltas = timestamps.diff().dropna()
    return deltas / pd.Timedelta(1, unit=unit)


def interarrival_plot_static(
    data: SeriesLike,
    unit: str = "D",
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    color: Optional[str] = None,
    theme: str = "default",
) -> MatplotlibAxes:
    """Create a static histogram of interarrival times.

    Args:
        data (SeriesLike): Input datetime-like observations.
        unit (str): Output unit for elapsed times.
        title (Optional[str]): Optional chart title.
        xlabel (Optional[str]): Optional x-axis label.
        figsize (FigureSize): Matplotlib figure size.
        color (Optional[str]): Histogram color.
        theme (str): Styling theme name.

    Returns:
        matplotlib.axes.Axes: Axes containing the interarrival histogram.

    Raises:
        TypeError: If values cannot be converted to datetimes.
        ValueError: If fewer than two datetime observations are available.

    Examples:
        ```python
        ax = interarrival_plot_static(timestamps)
        ```

    Notes:
        Interarrival plots reveal clustering or regularity in event streams.
    """
    gaps = interarrival_times(data, unit=unit)
    ax = setup_plot(title=title or "Interarrival Times", xlabel=xlabel or f"Elapsed Time ({unit})", ylabel="Frequency", figsize=figsize)[1]
    ax.hist(gaps, bins="auto", color=color, alpha=0.7, edgecolor="black")
    ax.grid(True, axis="y", alpha=0.3)
    apply_theme(ax, theme)
    return ax


def interarrival_plot_interactive(
    data: SeriesLike,
    unit: str = "D",
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    color: Optional[str] = None,
    template: str = "plotly",
    height: int = 600,
    width: int = 1000,
) -> PlotlyFigure:
    """Create an interactive histogram of interarrival times.

    Args:
        data (SeriesLike): Input datetime-like observations.
        unit (str): Output unit for elapsed times.
        title (Optional[str]): Optional chart title.
        xlabel (Optional[str]): Optional x-axis label.
        color (Optional[str]): Histogram color.
        template (str): Plotly template name.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.

    Returns:
        plotly.graph_objects.Figure: Interactive interarrival histogram.

    Raises:
        TypeError: If values cannot be converted to datetimes.
        ValueError: If fewer than two datetime observations are available.

    Examples:
        ```python
        fig = interarrival_plot_interactive(timestamps)
        ```

    Notes:
        The x-axis unit should be chosen to match the event process scale.
    """
    gaps = interarrival_times(data, unit=unit)
    fig = go.Figure(go.Histogram(x=gaps, marker_color=color, opacity=0.7))
    fig.update_layout(title=title or "Interarrival Times", xaxis_title=xlabel or f"Elapsed Time ({unit})", yaxis_title="Frequency", template=template, height=height, width=width)
    return fig
