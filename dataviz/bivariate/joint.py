"""Joint bivariate distribution charts."""

from typing import Optional

import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from ..types import FigureSize, MatplotlibAxes, PlotlyFigure, SeriesLike
from ..utils import apply_theme


def _label(values: object, fallback: str) -> str:
    """Return a plotting label from a named object or fallback text.

    Args:
        values (object): Object that may expose a ``name`` attribute.
        fallback (str): Label used when no name is available.

    Returns:
        str: Label for an axis, legend, or title.

    Raises:
        TypeError: If fallback cannot be represented as text.

    Example:
        ```python
        label = _label(series, "X")
        ```

    Notes:
        This helper keeps joint-chart labels consistent.
    """
    return getattr(values, "name", None) or fallback


def joint_scatter_hist_static(
    x: SeriesLike,
    y: SeriesLike,
    bins: int = 30,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    scatter_color: str = "steelblue",
    hist_color: str = "gray",
    figsize: FigureSize = (8, 8),
    theme: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Create a static joint scatter plot with marginal histograms.

    Args:
        x (SeriesLike): Values plotted along the x-axis.
        y (SeriesLike): Values plotted along the y-axis.
        bins (int): Number of bins used in marginal histograms.
        title (Optional[str]): Chart title. Defaults to a generated title.
        xlabel (Optional[str]): X-axis label.
        ylabel (Optional[str]): Y-axis label.
        scatter_color (str): Scatter marker color.
        hist_color (str): Histogram bar color.
        figsize (FigureSize): Figure size in inches.
        theme (str): Theme name applied to the main axes.
        **kwargs: Additional arguments forwarded to ``Axes.scatter``.

    Returns:
        matplotlib.axes.Axes: Main scatter axes.

    Raises:
        TypeError: If x or y is incompatible with matplotlib.
        ValueError: If x and y lengths differ.

    Example:
        ```python
        ax = dv.bivariate.joint_scatter_hist_static(x, y)
        ```

    Notes:
        The returned axes is the main scatter panel; marginal axes are attached to the same figure.
    """
    xlabel = xlabel or _label(x, "X")
    ylabel = ylabel or _label(y, "Y")
    title = title or f"Joint Distribution: {xlabel} vs {ylabel}"
    fig = plt.figure(figsize=figsize)
    grid = fig.add_gridspec(4, 4, hspace=0.05, wspace=0.05)
    ax = fig.add_subplot(grid[1:, :-1])
    ax_histx = fig.add_subplot(grid[0, :-1], sharex=ax)
    ax_histy = fig.add_subplot(grid[1:, -1], sharey=ax)
    ax.scatter(x, y, color=scatter_color, alpha=0.65, **kwargs)
    ax_histx.hist(x, bins=bins, color=hist_color, alpha=0.7)
    ax_histy.hist(y, bins=bins, orientation="horizontal", color=hist_color, alpha=0.7)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax_histx.tick_params(labelbottom=False)
    ax_histy.tick_params(labelleft=False)
    fig.suptitle(title)
    apply_theme(ax, theme)
    return ax


def joint_scatter_hist_interactive(
    x: SeriesLike,
    y: SeriesLike,
    bins: int = 30,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    scatter_color: str = "steelblue",
    hist_color: str = "gray",
    template: str = "plotly",
    height: int = 800,
    width: int = 800,
    **kwargs,
) -> PlotlyFigure:
    """Create an interactive joint scatter plot with marginal histograms.

    Args:
        x (SeriesLike): Values plotted along the x-axis.
        y (SeriesLike): Values plotted along the y-axis.
        bins (int): Number of bins used in marginal histograms.
        title (Optional[str]): Chart title. Defaults to a generated title.
        xlabel (Optional[str]): X-axis label.
        ylabel (Optional[str]): Y-axis label.
        scatter_color (str): Scatter marker color.
        hist_color (str): Histogram bar color.
        template (str): Plotly layout template.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.
        **kwargs: Additional arguments forwarded to the scatter trace.

    Returns:
        plotly.graph_objects.Figure: Interactive joint distribution figure.

    Raises:
        TypeError: If x or y is incompatible with Plotly.
        ValueError: If x and y lengths differ.

    Example:
        ```python
        fig = dv.bivariate.joint_scatter_hist_interactive(x, y)
        ```

    Notes:
        Marginal histograms share axes with the central scatter plot.
    """
    xlabel = xlabel or _label(x, "X")
    ylabel = ylabel or _label(y, "Y")
    title = title or f"Joint Distribution: {xlabel} vs {ylabel}"
    fig = make_subplots(
        rows=2,
        cols=2,
        shared_xaxes=True,
        shared_yaxes=True,
        row_heights=[0.25, 0.75],
        column_widths=[0.75, 0.25],
        horizontal_spacing=0.03,
        vertical_spacing=0.03,
    )
    fig.add_trace(go.Histogram(x=x, nbinsx=bins, marker_color=hist_color, showlegend=False), row=1, col=1)
    fig.add_trace(go.Scatter(x=x, y=y, mode="markers", marker=dict(color=scatter_color), showlegend=False, **kwargs), row=2, col=1)
    fig.add_trace(go.Histogram(y=y, nbinsy=bins, marker_color=hist_color, showlegend=False), row=2, col=2)
    fig.update_layout(title=title, template=template, height=height, width=width, bargap=0.05)
    fig.update_xaxes(title_text=xlabel, row=2, col=1)
    fig.update_yaxes(title_text=ylabel, row=2, col=1)
    return fig


def bivariate_histogram_static(
    x: SeriesLike,
    y: SeriesLike,
    bins: int = 30,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    cmap: str = "viridis",
    figsize: FigureSize = (10, 6),
    theme: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Create a static rectangular two-dimensional histogram.

    Args:
        x (SeriesLike): Values plotted along the x-axis.
        y (SeriesLike): Values plotted along the y-axis.
        bins (int): Number of bins in each direction.
        title (Optional[str]): Chart title. Defaults to a generated title.
        xlabel (Optional[str]): X-axis label.
        ylabel (Optional[str]): Y-axis label.
        cmap (str): Matplotlib colormap.
        figsize (FigureSize): Figure size in inches.
        theme (str): Theme name applied to the axes.
        **kwargs: Additional arguments forwarded to ``Axes.hist2d``.

    Returns:
        matplotlib.axes.Axes: Two-dimensional histogram axes.

    Raises:
        TypeError: If x or y is not numeric.
        ValueError: If x and y lengths differ.

    Example:
        ```python
        ax = dv.bivariate.bivariate_histogram_static(x, y)
        ```

    Notes:
        This is the rectangular-bin companion to a hexbin plot.
    """
    xlabel = xlabel or _label(x, "X")
    ylabel = ylabel or _label(y, "Y")
    title = title or f"2D Histogram: {xlabel} vs {ylabel}"
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    image = ax.hist2d(x, y, bins=bins, cmap=cmap, **kwargs)
    fig.colorbar(image[3], ax=ax, label="Count")
    apply_theme(ax, theme)
    return ax


def bivariate_histogram_interactive(
    x: SeriesLike,
    y: SeriesLike,
    nbinsx: int = 30,
    nbinsy: int = 30,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    colorscale: str = "Viridis",
    template: str = "plotly",
    height: int = 600,
    width: int = 900,
    **kwargs,
) -> PlotlyFigure:
    """Create an interactive rectangular two-dimensional histogram.

    Args:
        x (SeriesLike): Values plotted along the x-axis.
        y (SeriesLike): Values plotted along the y-axis.
        nbinsx (int): Number of x-axis bins.
        nbinsy (int): Number of y-axis bins.
        title (Optional[str]): Chart title. Defaults to a generated title.
        xlabel (Optional[str]): X-axis label.
        ylabel (Optional[str]): Y-axis label.
        colorscale (str): Plotly colorscale.
        template (str): Plotly layout template.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.
        **kwargs: Additional arguments forwarded to ``go.Histogram2d``.

    Returns:
        plotly.graph_objects.Figure: Interactive two-dimensional histogram.

    Raises:
        TypeError: If x or y is not numeric.
        ValueError: If x and y lengths differ.

    Example:
        ```python
        fig = dv.bivariate.bivariate_histogram_interactive(x, y)
        ```

    Notes:
        This function is useful for dense data where individual markers are hard to read.
    """
    xlabel = xlabel or _label(x, "X")
    ylabel = ylabel or _label(y, "Y")
    title = title or f"2D Histogram: {xlabel} vs {ylabel}"
    fig = go.Figure(data=[go.Histogram2d(x=x, y=y, nbinsx=nbinsx, nbinsy=nbinsy, colorscale=colorscale, **kwargs)])
    fig.update_layout(title=title, xaxis_title=xlabel, yaxis_title=ylabel, template=template, height=height, width=width)
    return fig
