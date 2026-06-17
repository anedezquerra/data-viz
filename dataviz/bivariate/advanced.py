"""Advanced bivariate relationship charts."""

from typing import Literal, Optional, Tuple

import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go

from ..types import ArrayLike, FigureSize, MatplotlibAxes, PlotlyFigure, SeriesLike
from ..utils import apply_theme, setup_plot


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
        This helper keeps generated chart titles consistent across functions.
    """
    return getattr(values, "name", None) or fallback


def _as_array(values: ArrayLike) -> np.ndarray:
    """Convert numeric array-like values to a NumPy array.

    Args:
        values (ArrayLike): Numeric values to convert.

    Returns:
        numpy.ndarray: Float array representation of the values.

    Raises:
        TypeError: If values cannot be interpreted as an array.
        ValueError: If values cannot be converted to floats.

    Example:
        ```python
        array = _as_array(values)
        ```

    Notes:
        Conversion is intentionally strict because advanced bivariate charts need numeric data.
    """
    return np.asarray(values, dtype=float)


def _linear_fit(x: ArrayLike, y: ArrayLike, degree: int = 1) -> Tuple[np.ndarray, np.ndarray]:
    """Fit a polynomial line and return sorted x values with predictions.

    Args:
        x (ArrayLike): Numeric x values.
        y (ArrayLike): Numeric y values.
        degree (int): Polynomial degree passed to ``numpy.polyfit``.

    Returns:
        Tuple[numpy.ndarray, numpy.ndarray]: Sorted x values and fitted y values.

    Raises:
        TypeError: If x or y cannot be converted to floats.
        ValueError: If the polynomial degree is invalid for the data length.

    Example:
        ```python
        x_fit, y_fit = _linear_fit(x, y)
        ```

    Notes:
        Sorting x values keeps trend lines visually continuous.
    """
    x_values = _as_array(x)
    y_values = _as_array(y)
    order = np.argsort(x_values)
    x_sorted = x_values[order]
    coefficients = np.polyfit(x_sorted, y_values[order], deg=degree)
    y_fit = np.polyval(coefficients, x_sorted)
    return x_sorted, y_fit


def bubble_plot_static(
    x: SeriesLike,
    y: SeriesLike,
    size: ArrayLike,
    color: Optional[ArrayLike] = None,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    size_scale: float = 300.0,
    alpha: float = 0.6,
    cmap: str = "viridis",
    figsize: FigureSize = (10, 6),
    theme: str = "default",
    style: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Create a static bubble plot for two variables and a size dimension.

    Args:
        x (SeriesLike): Values plotted along the x-axis.
        y (SeriesLike): Values plotted along the y-axis.
        size (ArrayLike): Numeric values mapped to marker area.
        color (Optional[ArrayLike]): Optional numeric values mapped to marker color.
        title (Optional[str]): Chart title. Defaults to a generated title.
        xlabel (Optional[str]): X-axis label. Defaults to the x series name or ``"X"``.
        ylabel (Optional[str]): Y-axis label. Defaults to the y series name or ``"Y"``.
        size_scale (float): Multiplier used to scale marker area.
        alpha (float): Marker opacity.
        cmap (str): Matplotlib colormap for numeric colors.
        figsize (FigureSize): Figure size in inches.
        theme (str): Theme name applied to the axes.
        style (str): Matplotlib style context.
        **kwargs: Additional arguments forwarded to ``Axes.scatter``.

    Returns:
        matplotlib.axes.Axes: Bubble plot axes.

    Raises:
        TypeError: If inputs cannot be interpreted as numeric arrays.
        ValueError: If x, y, and size lengths do not match.

    Example:
        ```python
        ax = dv.bivariate.bubble_plot_static(x, y, population)
        ```

    Notes:
        Use ``bubble_plot_interactive`` for a Plotly figure with hover support.
    """
    xlabel = xlabel or _label(x, "X")
    ylabel = ylabel or _label(y, "Y")
    title = title or f"Bubble Plot: {xlabel} vs {ylabel}"
    sizes = _as_array(size)
    if sizes.max() > 0:
        sizes = (sizes / sizes.max()) * size_scale

    with plt.style.context(style):
        _, ax = setup_plot(figsize=figsize, title=title, xlabel=xlabel, ylabel=ylabel)
        scatter = ax.scatter(x, y, s=sizes, c=color, alpha=alpha, cmap=cmap, **kwargs)
        if color is not None:
            plt.colorbar(scatter, ax=ax)
        apply_theme(ax, theme)
        return ax


def bubble_plot_interactive(
    x: SeriesLike,
    y: SeriesLike,
    size: ArrayLike,
    color: Optional[ArrayLike] = None,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    size_scale: float = 40.0,
    opacity: float = 0.7,
    colorscale: str = "Viridis",
    template: str = "plotly",
    height: int = 600,
    width: int = 900,
    **kwargs,
) -> PlotlyFigure:
    """Create an interactive bubble plot for two variables and a size dimension.

    Args:
        x (SeriesLike): Values plotted along the x-axis.
        y (SeriesLike): Values plotted along the y-axis.
        size (ArrayLike): Numeric values mapped to marker size.
        color (Optional[ArrayLike]): Optional numeric values mapped to marker color.
        title (Optional[str]): Chart title. Defaults to a generated title.
        xlabel (Optional[str]): X-axis label. Defaults to the x series name or ``"X"``.
        ylabel (Optional[str]): Y-axis label. Defaults to the y series name or ``"Y"``.
        size_scale (float): Maximum marker size.
        opacity (float): Marker opacity.
        colorscale (str): Plotly colorscale for numeric colors.
        template (str): Plotly layout template.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.
        **kwargs: Additional arguments forwarded to ``go.Scatter``.

    Returns:
        plotly.graph_objects.Figure: Interactive bubble plot.

    Raises:
        TypeError: If inputs cannot be interpreted as numeric arrays.
        ValueError: If x, y, and size lengths do not match.

    Example:
        ```python
        fig = dv.bivariate.bubble_plot_interactive(x, y, population)
        ```

    Notes:
        Marker colors accept either a single color or one value per observation.
    """
    xlabel = xlabel or _label(x, "X")
    ylabel = ylabel or _label(y, "Y")
    title = title or f"Bubble Plot: {xlabel} vs {ylabel}"
    raw_sizes = _as_array(size)
    marker_sizes = raw_sizes if raw_sizes.max() <= 0 else (raw_sizes / raw_sizes.max()) * size_scale
    fig = go.Figure(
        data=[
            go.Scatter(
                x=x,
                y=y,
                mode="markers",
                marker=dict(size=marker_sizes, color=color, colorscale=colorscale, opacity=opacity, showscale=color is not None),
                **kwargs,
            )
        ]
    )
    fig.update_layout(title=title, xaxis_title=xlabel, yaxis_title=ylabel, template=template, height=height, width=width)
    return fig


def hexbin_plot_static(
    x: SeriesLike,
    y: SeriesLike,
    gridsize: int = 30,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    cmap: str = "viridis",
    mincnt: Optional[int] = 1,
    figsize: FigureSize = (10, 6),
    theme: str = "default",
    style: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Create a static hexbin density plot for dense bivariate data.

    Args:
        x (SeriesLike): Values plotted along the x-axis.
        y (SeriesLike): Values plotted along the y-axis.
        gridsize (int): Number of hexagons in the x direction.
        title (Optional[str]): Chart title. Defaults to a generated title.
        xlabel (Optional[str]): X-axis label.
        ylabel (Optional[str]): Y-axis label.
        cmap (str): Matplotlib colormap for hexagon counts.
        mincnt (Optional[int]): Minimum observations required to draw a hexagon.
        figsize (FigureSize): Figure size in inches.
        theme (str): Theme name applied to the axes.
        style (str): Matplotlib style context.
        **kwargs: Additional arguments forwarded to ``Axes.hexbin``.

    Returns:
        matplotlib.axes.Axes: Hexbin plot axes.

    Raises:
        TypeError: If x or y is not numeric.
        ValueError: If x and y lengths differ.

    Example:
        ```python
        ax = dv.bivariate.hexbin_plot_static(x, y, gridsize=40)
        ```

    Notes:
        Hexbin charts are useful when scatter points overlap heavily.
    """
    xlabel = xlabel or _label(x, "X")
    ylabel = ylabel or _label(y, "Y")
    title = title or f"Hexbin Density: {xlabel} vs {ylabel}"
    with plt.style.context(style):
        _, ax = setup_plot(figsize=figsize, title=title, xlabel=xlabel, ylabel=ylabel)
        mesh = ax.hexbin(x, y, gridsize=gridsize, cmap=cmap, mincnt=mincnt, **kwargs)
        plt.colorbar(mesh, ax=ax, label="Count")
        apply_theme(ax, theme)
        return ax


def hexbin_plot_interactive(
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
    """Create an interactive bivariate histogram density plot.

    Args:
        x (SeriesLike): Values plotted along the x-axis.
        y (SeriesLike): Values plotted along the y-axis.
        nbinsx (int): Number of bins along the x-axis.
        nbinsy (int): Number of bins along the y-axis.
        title (Optional[str]): Chart title. Defaults to a generated title.
        xlabel (Optional[str]): X-axis label.
        ylabel (Optional[str]): Y-axis label.
        colorscale (str): Plotly colorscale for bin counts.
        template (str): Plotly layout template.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.
        **kwargs: Additional arguments forwarded to ``go.Histogram2d``.

    Returns:
        plotly.graph_objects.Figure: Interactive bivariate density figure.

    Raises:
        TypeError: If x or y is not numeric.
        ValueError: If x and y lengths differ.

    Example:
        ```python
        fig = dv.bivariate.hexbin_plot_interactive(x, y)
        ```

    Notes:
        Plotly does not render true hexagons here; it uses rectangular 2D bins.
    """
    xlabel = xlabel or _label(x, "X")
    ylabel = ylabel or _label(y, "Y")
    title = title or f"2D Density: {xlabel} vs {ylabel}"
    fig = go.Figure(data=[go.Histogram2d(x=x, y=y, nbinsx=nbinsx, nbinsy=nbinsy, colorscale=colorscale, **kwargs)])
    fig.update_layout(title=title, xaxis_title=xlabel, yaxis_title=ylabel, template=template, height=height, width=width)
    return fig


def regression_plot_static(
    x: SeriesLike,
    y: SeriesLike,
    degree: int = 1,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    scatter_color: str = "steelblue",
    line_color: str = "crimson",
    figsize: FigureSize = (10, 6),
    theme: str = "default",
    style: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Create a static scatter plot with a polynomial regression trend line.

    Args:
        x (SeriesLike): Values plotted along the x-axis.
        y (SeriesLike): Values plotted along the y-axis.
        degree (int): Polynomial degree passed to ``numpy.polyfit``.
        title (Optional[str]): Chart title. Defaults to a generated title.
        xlabel (Optional[str]): X-axis label.
        ylabel (Optional[str]): Y-axis label.
        scatter_color (str): Scatter marker color.
        line_color (str): Regression line color.
        figsize (FigureSize): Figure size in inches.
        theme (str): Theme name applied to the axes.
        style (str): Matplotlib style context.
        **kwargs: Additional arguments forwarded to ``Axes.scatter``.

    Returns:
        matplotlib.axes.Axes: Regression plot axes.

    Raises:
        TypeError: If x or y cannot be converted to numeric arrays.
        ValueError: If there are too few observations for the requested polynomial degree.

    Example:
        ```python
        ax = dv.bivariate.regression_plot_static(x, y, degree=2)
        ```

    Notes:
        This function intentionally uses NumPy only; no statsmodels dependency is required.
    """
    xlabel = xlabel or _label(x, "X")
    ylabel = ylabel or _label(y, "Y")
    title = title or f"Regression Plot: {xlabel} vs {ylabel}"
    x_fit, y_fit = _linear_fit(x, y, degree=degree)
    with plt.style.context(style):
        _, ax = setup_plot(figsize=figsize, title=title, xlabel=xlabel, ylabel=ylabel)
        ax.scatter(x, y, color=scatter_color, alpha=0.65, **kwargs)
        ax.plot(x_fit, y_fit, color=line_color, linewidth=2.0, label=f"Degree {degree} fit")
        ax.legend()
        apply_theme(ax, theme)
        return ax


def regression_plot_interactive(
    x: SeriesLike,
    y: SeriesLike,
    degree: int = 1,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    scatter_color: str = "steelblue",
    line_color: str = "crimson",
    template: str = "plotly",
    height: int = 600,
    width: int = 900,
    **kwargs,
) -> PlotlyFigure:
    """Create an interactive scatter plot with a polynomial regression trend line.

    Args:
        x (SeriesLike): Values plotted along the x-axis.
        y (SeriesLike): Values plotted along the y-axis.
        degree (int): Polynomial degree passed to ``numpy.polyfit``.
        title (Optional[str]): Chart title. Defaults to a generated title.
        xlabel (Optional[str]): X-axis label.
        ylabel (Optional[str]): Y-axis label.
        scatter_color (str): Scatter marker color.
        line_color (str): Regression line color.
        template (str): Plotly layout template.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.
        **kwargs: Additional arguments forwarded to the scatter trace.

    Returns:
        plotly.graph_objects.Figure: Interactive regression plot.

    Raises:
        TypeError: If x or y cannot be converted to numeric arrays.
        ValueError: If there are too few observations for the requested polynomial degree.

    Example:
        ```python
        fig = dv.bivariate.regression_plot_interactive(x, y)
        ```

    Notes:
        The fitted line is deterministic and uses all provided observations.
    """
    xlabel = xlabel or _label(x, "X")
    ylabel = ylabel or _label(y, "Y")
    title = title or f"Regression Plot: {xlabel} vs {ylabel}"
    x_fit, y_fit = _linear_fit(x, y, degree=degree)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode="markers", name="Observed", marker=dict(color=scatter_color), **kwargs))
    fig.add_trace(go.Scatter(x=x_fit, y=y_fit, mode="lines", name=f"Degree {degree} fit", line=dict(color=line_color, width=2)))
    fig.update_layout(title=title, xaxis_title=xlabel, yaxis_title=ylabel, template=template, height=height, width=width)
    return fig


def density_contour_static(
    x: SeriesLike,
    y: SeriesLike,
    bins: int = 30,
    levels: int = 8,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    cmap: str = "viridis",
    fill: bool = False,
    figsize: FigureSize = (10, 6),
    theme: str = "default",
    style: str = "default",
) -> MatplotlibAxes:
    """Create a static contour plot from a two-dimensional histogram.

    Args:
        x (SeriesLike): Values plotted along the x-axis.
        y (SeriesLike): Values plotted along the y-axis.
        bins (int): Number of bins used to estimate density.
        levels (int): Number of contour levels.
        title (Optional[str]): Chart title. Defaults to a generated title.
        xlabel (Optional[str]): X-axis label.
        ylabel (Optional[str]): Y-axis label.
        cmap (str): Matplotlib colormap.
        fill (bool): Whether to draw filled contours.
        figsize (FigureSize): Figure size in inches.
        theme (str): Theme name applied to the axes.
        style (str): Matplotlib style context.

    Returns:
        matplotlib.axes.Axes: Density contour axes.

    Raises:
        TypeError: If x or y is not numeric.
        ValueError: If x and y lengths differ.

    Example:
        ```python
        ax = dv.bivariate.density_contour_static(x, y, fill=True)
        ```

    Notes:
        Density is estimated with ``numpy.histogram2d``.
    """
    xlabel = xlabel or _label(x, "X")
    ylabel = ylabel or _label(y, "Y")
    title = title or f"Density Contour: {xlabel} vs {ylabel}"
    counts, x_edges, y_edges = np.histogram2d(_as_array(x), _as_array(y), bins=bins)
    x_centers = (x_edges[:-1] + x_edges[1:]) / 2
    y_centers = (y_edges[:-1] + y_edges[1:]) / 2
    with plt.style.context(style):
        _, ax = setup_plot(figsize=figsize, title=title, xlabel=xlabel, ylabel=ylabel)
        contour_fn = ax.contourf if fill else ax.contour
        contour = contour_fn(x_centers, y_centers, counts.T, levels=levels, cmap=cmap)
        plt.colorbar(contour, ax=ax, label="Count")
        apply_theme(ax, theme)
        return ax


def density_contour_interactive(
    x: SeriesLike,
    y: SeriesLike,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    colorscale: str = "Viridis",
    contours_coloring: Literal["fill", "heatmap", "lines", "none"] = "fill",
    template: str = "plotly",
    height: int = 600,
    width: int = 900,
    **kwargs,
) -> PlotlyFigure:
    """Create an interactive density contour plot.

    Args:
        x (SeriesLike): Values plotted along the x-axis.
        y (SeriesLike): Values plotted along the y-axis.
        title (Optional[str]): Chart title. Defaults to a generated title.
        xlabel (Optional[str]): X-axis label.
        ylabel (Optional[str]): Y-axis label.
        colorscale (str): Plotly colorscale.
        contours_coloring (Literal["fill", "heatmap", "lines", "none"]): Contour coloring mode.
        template (str): Plotly layout template.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.
        **kwargs: Additional arguments forwarded to ``go.Histogram2dContour``.

    Returns:
        plotly.graph_objects.Figure: Interactive density contour figure.

    Raises:
        TypeError: If x or y is not numeric.
        ValueError: If x and y lengths differ.

    Example:
        ```python
        fig = dv.bivariate.density_contour_interactive(x, y)
        ```

    Notes:
        Plotly estimates the two-dimensional density from the supplied points.
    """
    xlabel = xlabel or _label(x, "X")
    ylabel = ylabel or _label(y, "Y")
    title = title or f"Density Contour: {xlabel} vs {ylabel}"
    fig = go.Figure(data=[go.Histogram2dContour(x=x, y=y, colorscale=colorscale, contours_coloring=contours_coloring, **kwargs)])
    fig.update_layout(title=title, xaxis_title=xlabel, yaxis_title=ylabel, template=template, height=height, width=width)
    return fig
