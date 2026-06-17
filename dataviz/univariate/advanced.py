"""Advanced univariate visualization functions."""

from typing import Optional

import numpy as np
import pandas as pd
import plotly.graph_objects as go

from ..types import FigureSize, MatplotlibAxes, PlotlyFigure, SeriesLike
from ..utils import apply_theme, setup_plot, validate_alpha
from .categorical import category_counts
from .stats import as_numeric_series, univariate_summary


def rug_plot_static(
    data: SeriesLike,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    figsize: FigureSize = (10, 2),
    color: Optional[str] = None,
    height: float = 0.8,
    alpha: float = 0.7,
    theme: str = "default",
) -> MatplotlibAxes:
    """Create a static rug plot showing every observation along an axis.

    Args:
        data (SeriesLike): Input observations.
        title (Optional[str]): Optional chart title.
        xlabel (Optional[str]): Optional x-axis label.
        figsize (FigureSize): Matplotlib figure size.
        color (Optional[str]): Rug line color.
        height (float): Rug line height in axis units.
        alpha (float): Rug line opacity.
        theme (str): Styling theme name.

    Returns:
        matplotlib.axes.Axes: Axes containing the rug plot.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If opacity is invalid or no observations remain.

    Examples:
        ```python
        ax = rug_plot_static(data)
        ```

    Notes:
        Rug plots are most useful as companions to histograms or KDE charts.
    """
    validate_alpha(alpha)
    values = as_numeric_series(data)
    ax = setup_plot(title=title or "Rug Plot", xlabel=xlabel or values.name, ylabel="", figsize=figsize)[1]
    ax.vlines(values, 0, height, color=color, alpha=alpha)
    ax.set_yticks([])
    apply_theme(ax, theme)
    return ax


def rug_plot_interactive(
    data: SeriesLike,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    color: Optional[str] = None,
    template: str = "plotly",
    height: int = 250,
    width: int = 1000,
) -> PlotlyFigure:
    """Create an interactive rug plot showing every observation along an axis.

    Args:
        data (SeriesLike): Input observations.
        title (Optional[str]): Optional chart title.
        xlabel (Optional[str]): Optional x-axis label.
        color (Optional[str]): Rug marker color.
        template (str): Plotly template name.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.

    Returns:
        plotly.graph_objects.Figure: Interactive rug plot.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If no observations remain.

    Examples:
        ```python
        fig = rug_plot_interactive(data)
        ```

    Notes:
        Interactive rugs use tick markers so individual points remain inspectable.
    """
    values = as_numeric_series(data)
    fig = go.Figure(go.Scatter(x=values, y=np.zeros(len(values)), mode="markers", marker=dict(symbol="line-ns-open", color=color)))
    fig.update_layout(
        title=title or "Rug Plot",
        xaxis_title=xlabel or values.name,
        yaxis=dict(showticklabels=False, zeroline=False),
        template=template,
        height=height,
        width=width,
    )
    return fig


def strip_plot_static(
    data: SeriesLike,
    title: Optional[str] = None,
    ylabel: Optional[str] = None,
    figsize: FigureSize = (6, 8),
    color: Optional[str] = None,
    jitter: float = 0.08,
    alpha: float = 0.7,
    seed: Optional[int] = 0,
    theme: str = "default",
) -> MatplotlibAxes:
    """Create a static jittered strip plot for one numeric variable.

    Args:
        data (SeriesLike): Input observations.
        title (Optional[str]): Optional chart title.
        ylabel (Optional[str]): Optional y-axis label.
        figsize (FigureSize): Matplotlib figure size.
        color (Optional[str]): Marker color.
        jitter (float): Horizontal jitter magnitude.
        alpha (float): Marker opacity.
        seed (Optional[int]): Random seed for reproducible jitter.
        theme (str): Styling theme name.

    Returns:
        matplotlib.axes.Axes: Axes containing the strip plot.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If opacity is invalid or no observations remain.

    Examples:
        ```python
        ax = strip_plot_static(data)
        ```

    Notes:
        Strip plots expose individual observations without binning.
    """
    validate_alpha(alpha)
    values = as_numeric_series(data)
    rng = np.random.default_rng(seed)
    x_values = rng.normal(0, jitter, len(values)) if jitter > 0 else np.zeros(len(values))
    ax = setup_plot(title=title or "Strip Plot", xlabel="", ylabel=ylabel or values.name, figsize=figsize)[1]
    ax.scatter(x_values, values, color=color, alpha=alpha)
    ax.set_xticks([])
    ax.grid(True, axis="y", alpha=0.3)
    apply_theme(ax, theme)
    return ax


def strip_plot_interactive(
    data: SeriesLike,
    title: Optional[str] = None,
    ylabel: Optional[str] = None,
    color: Optional[str] = None,
    jitter: float = 0.08,
    seed: Optional[int] = 0,
    template: str = "plotly",
    height: int = 700,
    width: int = 600,
) -> PlotlyFigure:
    """Create an interactive jittered strip plot for one numeric variable.

    Args:
        data (SeriesLike): Input observations.
        title (Optional[str]): Optional chart title.
        ylabel (Optional[str]): Optional y-axis label.
        color (Optional[str]): Marker color.
        jitter (float): Horizontal jitter magnitude.
        seed (Optional[int]): Random seed for reproducible jitter.
        template (str): Plotly template name.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.

    Returns:
        plotly.graph_objects.Figure: Interactive strip plot.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If no observations remain.

    Examples:
        ```python
        fig = strip_plot_interactive(data)
        ```

    Notes:
        Hover labels expose each cleaned observation value.
    """
    values = as_numeric_series(data)
    rng = np.random.default_rng(seed)
    x_values = rng.normal(0, jitter, len(values)) if jitter > 0 else np.zeros(len(values))
    fig = go.Figure(go.Scatter(x=x_values, y=values, mode="markers", marker=dict(color=color), name="Observation"))
    fig.update_layout(
        title=title or "Strip Plot",
        xaxis=dict(showticklabels=False, zeroline=False),
        yaxis_title=ylabel or values.name,
        template=template,
        height=height,
        width=width,
    )
    return fig


def dot_plot_static(
    data: SeriesLike,
    title: Optional[str] = None,
    xlabel: str = "Count",
    ylabel: str = "Category",
    figsize: FigureSize = (10, 6),
    color: Optional[str] = None,
    top_n: Optional[int] = None,
    theme: str = "default",
) -> MatplotlibAxes:
    """Create a static Cleveland dot plot for category counts.

    Args:
        data (SeriesLike): Input categorical observations.
        title (Optional[str]): Optional chart title.
        xlabel (str): X-axis label.
        ylabel (str): Y-axis label.
        figsize (FigureSize): Matplotlib figure size.
        color (Optional[str]): Dot color.
        top_n (Optional[int]): Optional number of categories to keep.
        theme (str): Styling theme name.

    Returns:
        matplotlib.axes.Axes: Axes containing the dot plot.

    Raises:
        TypeError: If input data cannot be represented as a pandas Series.
        ValueError: If no categories remain or ``top_n`` is invalid.

    Examples:
        ```python
        ax = dot_plot_static(categories)
        ```

    Notes:
        Dot plots are quieter than bars when comparing many category counts.
    """
    counts = category_counts(data, top_n=top_n).sort_values()
    ax = setup_plot(title=title or "Dot Plot", xlabel=xlabel, ylabel=ylabel, figsize=figsize)[1]
    ax.scatter(counts.to_numpy(), counts.index.astype(str), color=color)
    ax.grid(True, axis="x", alpha=0.3)
    apply_theme(ax, theme)
    return ax


def dot_plot_interactive(
    data: SeriesLike,
    title: Optional[str] = None,
    xlabel: str = "Count",
    ylabel: str = "Category",
    color: Optional[str] = None,
    top_n: Optional[int] = None,
    template: str = "plotly",
    height: int = 600,
    width: int = 1000,
) -> PlotlyFigure:
    """Create an interactive Cleveland dot plot for category counts.

    Args:
        data (SeriesLike): Input categorical observations.
        title (Optional[str]): Optional chart title.
        xlabel (str): X-axis label.
        ylabel (str): Y-axis label.
        color (Optional[str]): Dot color.
        top_n (Optional[int]): Optional number of categories to keep.
        template (str): Plotly template name.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.

    Returns:
        plotly.graph_objects.Figure: Interactive dot plot.

    Raises:
        TypeError: If input data cannot be represented as a pandas Series.
        ValueError: If no categories remain or ``top_n`` is invalid.

    Examples:
        ```python
        fig = dot_plot_interactive(categories)
        ```

    Notes:
        The sorted y-axis keeps small and large categories easy to compare.
    """
    counts = category_counts(data, top_n=top_n).sort_values()
    fig = go.Figure(go.Scatter(x=counts.to_numpy(), y=counts.index.astype(str), mode="markers", marker=dict(color=color, size=10)))
    fig.update_layout(title=title or "Dot Plot", xaxis_title=xlabel, yaxis_title=ylabel, template=template, height=height, width=width)
    return fig


def lollipop_chart_static(
    data: SeriesLike,
    title: Optional[str] = None,
    xlabel: str = "Category",
    ylabel: str = "Count",
    figsize: FigureSize = (10, 6),
    color: Optional[str] = None,
    stem_color: str = "gray",
    top_n: Optional[int] = None,
    theme: str = "default",
) -> MatplotlibAxes:
    """Create a static lollipop chart for category counts.

    Args:
        data (SeriesLike): Input categorical observations.
        title (Optional[str]): Optional chart title.
        xlabel (str): X-axis label.
        ylabel (str): Y-axis label.
        figsize (FigureSize): Matplotlib figure size.
        color (Optional[str]): Dot color.
        stem_color (str): Stem line color.
        top_n (Optional[int]): Optional number of categories to keep.
        theme (str): Styling theme name.

    Returns:
        matplotlib.axes.Axes: Axes containing the lollipop chart.

    Raises:
        TypeError: If input data cannot be represented as a pandas Series.
        ValueError: If no categories remain or ``top_n`` is invalid.

    Examples:
        ```python
        ax = lollipop_chart_static(categories)
        ```

    Notes:
        Lollipop charts reduce visual weight compared with full-width bars.
    """
    counts = category_counts(data, top_n=top_n)
    labels = counts.index.astype(str)
    positions = np.arange(len(counts))
    ax = setup_plot(title=title or "Lollipop Chart", xlabel=xlabel, ylabel=ylabel, figsize=figsize)[1]
    ax.vlines(positions, 0, counts.to_numpy(), color=stem_color)
    ax.scatter(positions, counts.to_numpy(), color=color, zorder=3)
    ax.set_xticks(positions)
    ax.set_xticklabels(labels, rotation=45, ha="right")
    ax.grid(True, axis="y", alpha=0.3)
    apply_theme(ax, theme)
    return ax


def lollipop_chart_interactive(
    data: SeriesLike,
    title: Optional[str] = None,
    xlabel: str = "Category",
    ylabel: str = "Count",
    color: Optional[str] = None,
    top_n: Optional[int] = None,
    template: str = "plotly",
    height: int = 600,
    width: int = 1000,
) -> PlotlyFigure:
    """Create an interactive lollipop chart for category counts.

    Args:
        data (SeriesLike): Input categorical observations.
        title (Optional[str]): Optional chart title.
        xlabel (str): X-axis label.
        ylabel (str): Y-axis label.
        color (Optional[str]): Dot and stem color.
        top_n (Optional[int]): Optional number of categories to keep.
        template (str): Plotly template name.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.

    Returns:
        plotly.graph_objects.Figure: Interactive lollipop chart.

    Raises:
        TypeError: If input data cannot be represented as a pandas Series.
        ValueError: If no categories remain or ``top_n`` is invalid.

    Examples:
        ```python
        fig = lollipop_chart_interactive(categories)
        ```

    Notes:
        The line trace draws stems and the marker trace draws the lollipop heads.
    """
    counts = category_counts(data, top_n=top_n)
    labels = counts.index.astype(str)
    fig = go.Figure()
    for label, value in zip(labels, counts.to_numpy()):
        fig.add_trace(go.Scatter(x=[label, label], y=[0, value], mode="lines", line=dict(color=color or "gray"), showlegend=False))
    fig.add_trace(go.Scatter(x=labels, y=counts.to_numpy(), mode="markers", marker=dict(color=color, size=10), name="Count"))
    fig.update_layout(title=title or "Lollipop Chart", xaxis_title=xlabel, yaxis_title=ylabel, template=template, height=height, width=width)
    return fig


def reference_band_histogram_static(
    data: SeriesLike,
    bins: int = 30,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    color: Optional[str] = None,
    band_color: str = "gold",
    mean_color: str = "crimson",
    theme: str = "default",
) -> MatplotlibAxes:
    """Create a static histogram with mean and standard-deviation reference bands.

    Args:
        data (SeriesLike): Input observations.
        bins (int): Number of histogram bins.
        title (Optional[str]): Optional chart title.
        xlabel (Optional[str]): Optional x-axis label.
        figsize (FigureSize): Matplotlib figure size.
        color (Optional[str]): Histogram color.
        band_color (str): Reference band color.
        mean_color (str): Mean line color.
        theme (str): Styling theme name.

    Returns:
        matplotlib.axes.Axes: Axes containing the reference-band histogram.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If no observations remain.

    Examples:
        ```python
        ax = reference_band_histogram_static(data)
        ```

    Notes:
        The shaded band spans one sample standard deviation around the mean.
    """
    values = as_numeric_series(data)
    summary = univariate_summary(values)
    ax = setup_plot(title=title or "Reference Band Histogram", xlabel=xlabel or values.name, ylabel="Frequency", figsize=figsize)[1]
    ax.hist(values, bins=bins, color=color, alpha=0.7, edgecolor="black")
    ax.axvspan(summary.mean - summary.std, summary.mean + summary.std, color=band_color, alpha=0.25, label="+/- 1 std")
    ax.axvline(summary.mean, color=mean_color, linestyle="--", label="Mean")
    ax.axvline(summary.median, color="black", linestyle=":", label="Median")
    ax.legend()
    ax.grid(True, axis="y", alpha=0.3)
    apply_theme(ax, theme)
    return ax


def reference_band_histogram_interactive(
    data: SeriesLike,
    bins: int = 30,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    color: Optional[str] = None,
    band_color: str = "gold",
    mean_color: str = "crimson",
    template: str = "plotly",
    height: int = 600,
    width: int = 1000,
) -> PlotlyFigure:
    """Create an interactive histogram with mean and standard-deviation reference bands.

    Args:
        data (SeriesLike): Input observations.
        bins (int): Number of histogram bins.
        title (Optional[str]): Optional chart title.
        xlabel (Optional[str]): Optional x-axis label.
        color (Optional[str]): Histogram color.
        band_color (str): Reference band color.
        mean_color (str): Mean line color.
        template (str): Plotly template name.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.

    Returns:
        plotly.graph_objects.Figure: Interactive reference-band histogram.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If no observations remain.

    Examples:
        ```python
        fig = reference_band_histogram_interactive(data)
        ```

    Notes:
        The standard-deviation band is represented as a translucent rectangle.
    """
    values = as_numeric_series(data)
    summary = univariate_summary(values)
    fig = go.Figure(go.Histogram(x=values, nbinsx=bins, marker_color=color, opacity=0.7, name="Distribution"))
    fig.add_vrect(x0=summary.mean - summary.std, x1=summary.mean + summary.std, fillcolor=band_color, opacity=0.25, line_width=0)
    fig.add_vline(x=summary.mean, line_color=mean_color, line_dash="dash", annotation_text="Mean")
    fig.add_vline(x=summary.median, line_color="black", line_dash="dot", annotation_text="Median")
    fig.update_layout(title=title or "Reference Band Histogram", xaxis_title=xlabel or values.name, yaxis_title="Frequency", template=template, height=height, width=width)
    return fig


def raincloud_plot_static(
    data: SeriesLike,
    title: Optional[str] = None,
    ylabel: Optional[str] = None,
    figsize: FigureSize = (7, 8),
    color: Optional[str] = None,
    alpha: float = 0.6,
    theme: str = "default",
) -> MatplotlibAxes:
    """Create a static raincloud-style plot for one numeric variable.

    Args:
        data (SeriesLike): Input observations.
        title (Optional[str]): Optional chart title.
        ylabel (Optional[str]): Optional y-axis label.
        figsize (FigureSize): Matplotlib figure size.
        color (Optional[str]): Primary plot color.
        alpha (float): Point opacity.
        theme (str): Styling theme name.

    Returns:
        matplotlib.axes.Axes: Axes containing violin, box, and raw points.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If opacity is invalid or no observations remain.

    Examples:
        ```python
        ax = raincloud_plot_static(data)
        ```

    Notes:
        The implementation approximates a raincloud with familiar matplotlib primitives.
    """
    validate_alpha(alpha)
    values = as_numeric_series(data)
    ax = setup_plot(title=title or "Raincloud Plot", xlabel="", ylabel=ylabel or values.name, figsize=figsize)[1]
    ax.violinplot(values, positions=[0], showmeans=False, showmedians=False)
    ax.boxplot(values, positions=[0], widths=0.15)
    rng = np.random.default_rng(0)
    ax.scatter(rng.normal(0.25, 0.035, len(values)), values, alpha=alpha, color=color)
    ax.set_xticks([])
    ax.grid(True, axis="y", alpha=0.3)
    apply_theme(ax, theme)
    return ax


def raincloud_plot_interactive(
    data: SeriesLike,
    title: Optional[str] = None,
    ylabel: Optional[str] = None,
    color: Optional[str] = None,
    template: str = "plotly",
    height: int = 700,
    width: int = 700,
) -> PlotlyFigure:
    """Create an interactive raincloud-style plot for one numeric variable.

    Args:
        data (SeriesLike): Input observations.
        title (Optional[str]): Optional chart title.
        ylabel (Optional[str]): Optional y-axis label.
        color (Optional[str]): Primary plot color.
        template (str): Plotly template name.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.

    Returns:
        plotly.graph_objects.Figure: Interactive raincloud-style plot.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If no observations remain.

    Examples:
        ```python
        fig = raincloud_plot_interactive(data)
        ```

    Notes:
        Plotly violin traces can display violin, box, meanline, and raw points together.
    """
    values = as_numeric_series(data)
    fig = go.Figure(
        go.Violin(
            y=values,
            box_visible=True,
            meanline_visible=True,
            points="all",
            marker_color=color,
            name=values.name,
        )
    )
    fig.update_layout(title=title or "Raincloud Plot", yaxis_title=ylabel or values.name, template=template, height=height, width=width)
    return fig


def ridgeline_plot_static(
    data: pd.DataFrame,
    title: Optional[str] = None,
    xlabel: str = "Value",
    figsize: FigureSize = (10, 8),
    color: Optional[str] = None,
    theme: str = "default",
) -> MatplotlibAxes:
    """Create a static ridgeline-style density plot for numeric dataframe columns.

    Args:
        data (pandas.DataFrame): Dataframe containing numeric columns.
        title (Optional[str]): Optional chart title.
        xlabel (str): X-axis label.
        figsize (FigureSize): Matplotlib figure size.
        color (Optional[str]): Density line color.
        theme (str): Styling theme name.

    Returns:
        matplotlib.axes.Axes: Axes containing offset density curves.

    Raises:
        TypeError: If ``data`` is not a dataframe.
        ValueError: If no numeric columns are available.

    Examples:
        ```python
        ax = ridgeline_plot_static(df[["a", "b", "c"]])
        ```

    Notes:
        This single-axes implementation avoids adding a seaborn dependency beyond package runtime.
    """
    if not isinstance(data, pd.DataFrame):
        raise TypeError("data must be a pandas DataFrame.")
    numeric = data.select_dtypes(include=[np.number]).dropna(axis=1, how="all")
    if numeric.empty:
        raise ValueError("data must contain at least one numeric column.")
    ax = setup_plot(title=title or "Ridgeline Plot", xlabel=xlabel, ylabel="", figsize=figsize)[1]
    offset = 0.0
    for column in numeric.columns:
        values = as_numeric_series(numeric[column])
        density = pd.Series(values).plot.kde()
        line = density.lines[-1]
        x_values = line.get_xdata()
        y_values = line.get_ydata()
        line.remove()
        ax.fill_between(x_values, offset, y_values + offset, alpha=0.35, color=color)
        ax.plot(x_values, y_values + offset, color=color)
        ax.text(float(np.min(x_values)), offset, str(column), va="bottom")
        offset += 1.0
    ax.set_yticks([])
    apply_theme(ax, theme)
    return ax


def ridgeline_plot_interactive(
    data: pd.DataFrame,
    title: Optional[str] = None,
    xlabel: str = "Value",
    template: str = "plotly",
    height: int = 700,
    width: int = 1000,
) -> PlotlyFigure:
    """Create an interactive ridgeline-style density plot for numeric dataframe columns.

    Args:
        data (pandas.DataFrame): Dataframe containing numeric columns.
        title (Optional[str]): Optional chart title.
        xlabel (str): X-axis label.
        template (str): Plotly template name.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.

    Returns:
        plotly.graph_objects.Figure: Interactive ridgeline-style density plot.

    Raises:
        TypeError: If ``data`` is not a dataframe.
        ValueError: If no numeric columns are available.

    Examples:
        ```python
        fig = ridgeline_plot_interactive(df[["a", "b"]])
        ```

    Notes:
        Violin traces provide a compact interactive ridgeline approximation.
    """
    if not isinstance(data, pd.DataFrame):
        raise TypeError("data must be a pandas DataFrame.")
    numeric = data.select_dtypes(include=[np.number]).dropna(axis=1, how="all")
    if numeric.empty:
        raise ValueError("data must contain at least one numeric column.")
    fig = go.Figure()
    for column in numeric.columns:
        fig.add_trace(go.Violin(x=as_numeric_series(numeric[column]), name=str(column), orientation="h", side="positive", width=1.5, points=False))
    fig.update_layout(title=title or "Ridgeline Plot", xaxis_title=xlabel, template=template, height=height, width=width, violingap=0, violinmode="overlay")
    return fig
