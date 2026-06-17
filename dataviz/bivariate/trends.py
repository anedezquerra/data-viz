"""Trend-oriented bivariate charts."""

from typing import Optional

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
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
        This helper keeps generated trend-chart titles consistent.
    """
    return getattr(values, "name", None) or fallback


def binned_mean_plot_static(
    x: SeriesLike,
    y: SeriesLike,
    bins: int = 10,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    color: str = "steelblue",
    marker: str = "o",
    figsize: FigureSize = (10, 6),
    theme: str = "default",
    style: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Create a static line chart of mean y values across x bins.

    Args:
        x (SeriesLike): Numeric values used to create bins.
        y (SeriesLike): Numeric values averaged within each bin.
        bins (int): Number of x bins.
        title (Optional[str]): Chart title. Defaults to a generated title.
        xlabel (Optional[str]): X-axis label.
        ylabel (Optional[str]): Y-axis label.
        color (str): Line and marker color.
        marker (str): Marker style.
        figsize (FigureSize): Figure size in inches.
        theme (str): Theme name applied to the axes.
        style (str): Matplotlib style context.
        **kwargs: Additional arguments forwarded to ``Axes.plot``.

    Returns:
        matplotlib.axes.Axes: Binned mean plot axes.

    Raises:
        TypeError: If x or y is not numeric.
        ValueError: If x and y lengths differ.

    Example:
        ```python
        ax = dv.bivariate.binned_mean_plot_static(age, income)
        ```

    Notes:
        Binned means help reveal nonlinear relationships in noisy scatter data.
    """
    xlabel = xlabel or _label(x, "X")
    ylabel = ylabel or f"Mean {_label(y, 'Y')}"
    title = title or f"Binned Mean: {ylabel} by {xlabel}"
    frame = pd.DataFrame({"x": x, "y": y})
    frame["bin"] = pd.cut(frame["x"], bins=bins)
    summary = frame.groupby("bin", observed=True)["y"].mean()
    centers = [interval.mid for interval in summary.index]
    with plt.style.context(style):
        _, ax = setup_plot(figsize=figsize, title=title, xlabel=xlabel, ylabel=ylabel)
        ax.plot(centers, summary.values, color=color, marker=marker, **kwargs)
        apply_theme(ax, theme)
        return ax


def binned_mean_plot_interactive(
    x: SeriesLike,
    y: SeriesLike,
    bins: int = 10,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    color: str = "steelblue",
    template: str = "plotly",
    height: int = 600,
    width: int = 900,
    **kwargs,
) -> PlotlyFigure:
    """Create an interactive line chart of mean y values across x bins.

    Args:
        x (SeriesLike): Numeric values used to create bins.
        y (SeriesLike): Numeric values averaged within each bin.
        bins (int): Number of x bins.
        title (Optional[str]): Chart title. Defaults to a generated title.
        xlabel (Optional[str]): X-axis label.
        ylabel (Optional[str]): Y-axis label.
        color (str): Line and marker color.
        template (str): Plotly layout template.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.
        **kwargs: Additional arguments forwarded to ``go.Scatter``.

    Returns:
        plotly.graph_objects.Figure: Interactive binned mean plot.

    Raises:
        TypeError: If x or y is not numeric.
        ValueError: If x and y lengths differ.

    Example:
        ```python
        fig = dv.bivariate.binned_mean_plot_interactive(age, income)
        ```

    Notes:
        Empty bins are omitted from the plotted line.
    """
    xlabel = xlabel or _label(x, "X")
    ylabel = ylabel or f"Mean {_label(y, 'Y')}"
    title = title or f"Binned Mean: {ylabel} by {xlabel}"
    frame = pd.DataFrame({"x": x, "y": y})
    frame["bin"] = pd.cut(frame["x"], bins=bins)
    summary = frame.groupby("bin", observed=True)["y"].mean()
    centers = [interval.mid for interval in summary.index]
    fig = go.Figure(data=[go.Scatter(x=centers, y=summary.values, mode="lines+markers", line=dict(color=color), **kwargs)])
    fig.update_layout(title=title, xaxis_title=xlabel, yaxis_title=ylabel, template=template, height=height, width=width)
    return fig


def errorbar_plot_static(
    x: SeriesLike,
    y: SeriesLike,
    yerr: Optional[ArrayLike] = None,
    xerr: Optional[ArrayLike] = None,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    color: str = "steelblue",
    marker: str = "o",
    capsize: float = 4.0,
    figsize: FigureSize = (10, 6),
    theme: str = "default",
    style: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Create a static bivariate error-bar plot.

    Args:
        x (SeriesLike): Values plotted along the x-axis.
        y (SeriesLike): Values plotted along the y-axis.
        yerr (Optional[ArrayLike]): Symmetric or asymmetric y-error values.
        xerr (Optional[ArrayLike]): Symmetric or asymmetric x-error values.
        title (Optional[str]): Chart title. Defaults to a generated title.
        xlabel (Optional[str]): X-axis label.
        ylabel (Optional[str]): Y-axis label.
        color (str): Marker and line color.
        marker (str): Marker style.
        capsize (float): Error-bar cap size.
        figsize (FigureSize): Figure size in inches.
        theme (str): Theme name applied to the axes.
        style (str): Matplotlib style context.
        **kwargs: Additional arguments forwarded to ``Axes.errorbar``.

    Returns:
        matplotlib.axes.Axes: Error-bar plot axes.

    Raises:
        TypeError: If error values are incompatible with matplotlib.
        ValueError: If x and y lengths differ.

    Example:
        ```python
        ax = dv.bivariate.errorbar_plot_static(x, mean, yerr=std)
        ```

    Notes:
        Use this chart for estimates with uncertainty intervals.
    """
    xlabel = xlabel or _label(x, "X")
    ylabel = ylabel or _label(y, "Y")
    title = title or f"Error Bar Plot: {xlabel} vs {ylabel}"
    with plt.style.context(style):
        _, ax = setup_plot(figsize=figsize, title=title, xlabel=xlabel, ylabel=ylabel)
        ax.errorbar(x, y, yerr=yerr, xerr=xerr, color=color, marker=marker, capsize=capsize, **kwargs)
        apply_theme(ax, theme)
        return ax


def errorbar_plot_interactive(
    x: SeriesLike,
    y: SeriesLike,
    yerr: Optional[ArrayLike] = None,
    xerr: Optional[ArrayLike] = None,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    color: str = "steelblue",
    template: str = "plotly",
    height: int = 600,
    width: int = 900,
    **kwargs,
) -> PlotlyFigure:
    """Create an interactive bivariate error-bar plot.

    Args:
        x (SeriesLike): Values plotted along the x-axis.
        y (SeriesLike): Values plotted along the y-axis.
        yerr (Optional[ArrayLike]): Symmetric y-error values.
        xerr (Optional[ArrayLike]): Symmetric x-error values.
        title (Optional[str]): Chart title. Defaults to a generated title.
        xlabel (Optional[str]): X-axis label.
        ylabel (Optional[str]): Y-axis label.
        color (str): Marker and line color.
        template (str): Plotly layout template.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.
        **kwargs: Additional arguments forwarded to ``go.Scatter``.

    Returns:
        plotly.graph_objects.Figure: Interactive error-bar plot.

    Raises:
        TypeError: If error values are incompatible with Plotly.
        ValueError: If x and y lengths differ.

    Example:
        ```python
        fig = dv.bivariate.errorbar_plot_interactive(x, mean, yerr=std)
        ```

    Notes:
        Plotly supports symmetric error arrays through ``array`` values.
    """
    xlabel = xlabel or _label(x, "X")
    ylabel = ylabel or _label(y, "Y")
    title = title or f"Error Bar Plot: {xlabel} vs {ylabel}"
    fig = go.Figure(
        data=[
            go.Scatter(
                x=x,
                y=y,
                mode="lines+markers",
                marker=dict(color=color),
                line=dict(color=color),
                error_y=dict(type="data", array=yerr, visible=yerr is not None),
                error_x=dict(type="data", array=xerr, visible=xerr is not None),
                **kwargs,
            )
        ]
    )
    fig.update_layout(title=title, xaxis_title=xlabel, yaxis_title=ylabel, template=template, height=height, width=width)
    return fig


def area_between_static(
    x: SeriesLike,
    y_lower: SeriesLike,
    y_upper: SeriesLike,
    title: str = "Area Between Curves",
    xlabel: str = "X",
    ylabel: str = "Y",
    color: str = "steelblue",
    alpha: float = 0.3,
    figsize: FigureSize = (10, 6),
    theme: str = "default",
    style: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Create a static filled area between two y-series.

    Args:
        x (SeriesLike): Values plotted along the x-axis.
        y_lower (SeriesLike): Lower boundary values.
        y_upper (SeriesLike): Upper boundary values.
        title (str): Chart title.
        xlabel (str): X-axis label.
        ylabel (str): Y-axis label.
        color (str): Fill color.
        alpha (float): Fill opacity.
        figsize (FigureSize): Figure size in inches.
        theme (str): Theme name applied to the axes.
        style (str): Matplotlib style context.
        **kwargs: Additional arguments forwarded to ``Axes.fill_between``.

    Returns:
        matplotlib.axes.Axes: Filled area axes.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If input lengths differ.

    Example:
        ```python
        ax = dv.bivariate.area_between_static(x, lower, upper)
        ```

    Notes:
        This chart is useful for bands, intervals, or envelopes.
    """
    with plt.style.context(style):
        _, ax = setup_plot(figsize=figsize, title=title, xlabel=xlabel, ylabel=ylabel)
        ax.fill_between(x, y_lower, y_upper, color=color, alpha=alpha, **kwargs)
        apply_theme(ax, theme)
        return ax


def area_between_interactive(
    x: SeriesLike,
    y_lower: SeriesLike,
    y_upper: SeriesLike,
    title: str = "Area Between Curves",
    xlabel: str = "X",
    ylabel: str = "Y",
    color: str = "rgba(70, 130, 180, 0.35)",
    line_color: str = "steelblue",
    template: str = "plotly",
    height: int = 600,
    width: int = 900,
) -> PlotlyFigure:
    """Create an interactive filled area between two y-series.

    Args:
        x (SeriesLike): Values plotted along the x-axis.
        y_lower (SeriesLike): Lower boundary values.
        y_upper (SeriesLike): Upper boundary values.
        title (str): Chart title.
        xlabel (str): X-axis label.
        ylabel (str): Y-axis label.
        color (str): Fill color.
        line_color (str): Boundary line color.
        template (str): Plotly layout template.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.

    Returns:
        plotly.graph_objects.Figure: Interactive filled band figure.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If input lengths differ.

    Example:
        ```python
        fig = dv.bivariate.area_between_interactive(x, lower, upper)
        ```

    Notes:
        The upper trace fills to the lower trace using Plotly's ``tonexty`` mode.
    """
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y_lower, mode="lines", line=dict(color=line_color), name="Lower"))
    fig.add_trace(go.Scatter(x=x, y=y_upper, mode="lines", fill="tonexty", fillcolor=color, line=dict(color=line_color), name="Upper"))
    fig.update_layout(title=title, xaxis_title=xlabel, yaxis_title=ylabel, template=template, height=height, width=width)
    return fig


def step_plot_static(
    x: SeriesLike,
    y: SeriesLike,
    where: str = "post",
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    color: str = "steelblue",
    figsize: FigureSize = (10, 6),
    theme: str = "default",
    style: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Create a static step plot for ordered bivariate data.

    Args:
        x (SeriesLike): Values plotted along the x-axis.
        y (SeriesLike): Values plotted along the y-axis.
        where (str): Step placement accepted by ``Axes.step``.
        title (Optional[str]): Chart title. Defaults to a generated title.
        xlabel (Optional[str]): X-axis label.
        ylabel (Optional[str]): Y-axis label.
        color (str): Line color.
        figsize (FigureSize): Figure size in inches.
        theme (str): Theme name applied to the axes.
        style (str): Matplotlib style context.
        **kwargs: Additional arguments forwarded to ``Axes.step``.

    Returns:
        matplotlib.axes.Axes: Step plot axes.

    Raises:
        TypeError: If x or y is incompatible with matplotlib.
        ValueError: If x and y lengths differ.

    Example:
        ```python
        ax = dv.bivariate.step_plot_static(time, state)
        ```

    Notes:
        Step plots are useful for piecewise-constant series.
    """
    xlabel = xlabel or _label(x, "X")
    ylabel = ylabel or _label(y, "Y")
    title = title or f"Step Plot: {xlabel} vs {ylabel}"
    with plt.style.context(style):
        _, ax = setup_plot(figsize=figsize, title=title, xlabel=xlabel, ylabel=ylabel)
        ax.step(x, y, where=where, color=color, **kwargs)
        apply_theme(ax, theme)
        return ax


def step_plot_interactive(
    x: SeriesLike,
    y: SeriesLike,
    shape: str = "hv",
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    color: str = "steelblue",
    template: str = "plotly",
    height: int = 600,
    width: int = 900,
    **kwargs,
) -> PlotlyFigure:
    """Create an interactive step plot for ordered bivariate data.

    Args:
        x (SeriesLike): Values plotted along the x-axis.
        y (SeriesLike): Values plotted along the y-axis.
        shape (str): Plotly line shape, such as ``"hv"`` or ``"vh"``.
        title (Optional[str]): Chart title. Defaults to a generated title.
        xlabel (Optional[str]): X-axis label.
        ylabel (Optional[str]): Y-axis label.
        color (str): Line color.
        template (str): Plotly layout template.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.
        **kwargs: Additional arguments forwarded to ``go.Scatter``.

    Returns:
        plotly.graph_objects.Figure: Interactive step plot.

    Raises:
        TypeError: If x or y is incompatible with Plotly.
        ValueError: If x and y lengths differ.

    Example:
        ```python
        fig = dv.bivariate.step_plot_interactive(time, state)
        ```

    Notes:
        Plotly step behavior is controlled by the trace line shape.
    """
    xlabel = xlabel or _label(x, "X")
    ylabel = ylabel or _label(y, "Y")
    title = title or f"Step Plot: {xlabel} vs {ylabel}"
    fig = go.Figure(data=[go.Scatter(x=x, y=y, mode="lines", line=dict(color=color, shape=shape), **kwargs)])
    fig.update_layout(title=title, xaxis_title=xlabel, yaxis_title=ylabel, template=template, height=height, width=width)
    return fig
