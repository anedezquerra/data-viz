"""Line plot implementation - static and interactive versions."""

from typing import Optional, Tuple, Union

import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go

from ..types import FigureSize, MatplotlibAxes, PlotlyFigure, SeriesLike
from ..utils import (
    add_plotly_reference_lines,
    add_reference_lines,
    apply_theme,
    resolve_xy_data,
    setup_plot,
    validate_alpha,
    validate_positive_int,
)
from ..utils.validation import NaPolicy


def _maybe_sort(x: pd.Series, y: pd.Series, sort_x: bool) -> Tuple[pd.Series, pd.Series]:
    """Optionally sort paired x and y series by x values.

    Args:
        x (pd.Series): X values.
        y (pd.Series): Y values.
        sort_x (bool): Whether to sort by x values.

    Returns:
        tuple[pandas.Series, pandas.Series]: Original or sorted x and y values.

    Raises:
        TypeError: If x values cannot be sorted.
        ValueError: If x and y lengths differ.

    Example:
        ```python
        x_sorted, y_sorted = _maybe_sort(x, y, True)
        ```

    Notes:
        Sorting is useful for line charts built from unordered observations.
    """
    if not sort_x:
        return x, y
    frame = pd.DataFrame({"x": x, "y": y}).sort_values("x")
    return pd.Series(frame["x"].to_numpy(), name=x.name), pd.Series(frame["y"].to_numpy(), name=y.name)


def line_plot_static(
    x: Union[str, SeriesLike],
    y: Union[str, SeriesLike],
    data: Optional[pd.DataFrame] = None,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    color: Optional[str] = None,
    linewidth: float = 2.0,
    linestyle: str = "-",
    marker: Optional[str] = None,
    markersize: int = 6,
    alpha: float = 1.0,
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = "default",
    font_size: int = 10,
    title_size: int = 14,
    label_size: int = 11,
    dpi: int = 100,
    style: str = "default",
    ax: Optional[MatplotlibAxes] = None,
    na_policy: NaPolicy = "drop",
    sort_x: bool = False,
    rolling_window: Optional[int] = None,
    rolling_color: str = "crimson",
    fill_to: Optional[float] = None,
    fill_alpha: float = 0.2,
    hline: Optional[float] = None,
    vline: Optional[float] = None,
    **kwargs,
) -> MatplotlibAxes:
    """Create a static line plot that shows ordered or time-based changes.

    Args:
        x (Union[str, SeriesLike]): X values or a column name when ``data`` is provided.
        y (Union[str, SeriesLike]): Y values or a column name when ``data`` is provided.
        data (Optional[pd.DataFrame]): Optional dataframe used for column lookup.
        title (Optional[str]): Chart title. Defaults to a generated title.
        xlabel (Optional[str]): X-axis label.
        ylabel (Optional[str]): Y-axis label.
        figsize (FigureSize): Matplotlib figure size in inches.
        color (Optional[str]): Line color.
        linewidth (float): Line width.
        linestyle (str): Line style.
        marker (Optional[str]): Marker style.
        markersize (int): Marker size.
        alpha (float): Line opacity from 0 to 1.
        grid (bool): Whether to show grid lines.
        grid_alpha (float): Grid opacity.
        theme (str): Named style theme.
        font_size (int): Tick and legend font size.
        title_size (int): Title font size.
        label_size (int): Axis-label font size.
        dpi (int): Figure DPI when a new figure is created.
        style (str): Matplotlib style context.
        ax (Optional[MatplotlibAxes]): Existing axes to draw into.
        na_policy (NaPolicy): Missing-value behavior: ``"drop"``, ``"raise"``, or ``"keep"``.
        sort_x (bool): Whether to sort paired observations by x before drawing.
        rolling_window (Optional[int]): Optional rolling mean window for y values.
        rolling_color (str): Rolling mean line color.
        fill_to (Optional[float]): Optional baseline for filled area under the line.
        fill_alpha (float): Area fill opacity.
        hline (Optional[float]): Optional horizontal reference line.
        vline (Optional[float]): Optional vertical reference line.
        **kwargs: Additional keyword arguments forwarded to ``Axes.plot``.

    Returns:
        matplotlib.axes.Axes: Configured matplotlib axes containing the line plot.

    Raises:
        TypeError: If inputs cannot be resolved or plotted.
        ValueError: If input lengths differ, inputs are empty, or options are invalid.

    Example:
        ```python
        ax = dv.line_plot_static("date", "sales", data=df, rolling_window=7)
        ```

    Notes:
        ``sort_x=True`` is helpful when observations are not already ordered.
    """
    validate_alpha(alpha)
    validate_alpha(fill_alpha, name="fill_alpha")
    x_values, y_values = resolve_xy_data(x, y, data=data, na_policy=na_policy)
    x_values, y_values = _maybe_sort(x_values, y_values, sort_x)
    xlabel = xlabel or x_values.name or "X"
    ylabel = ylabel or y_values.name or "Y"
    title = title or f"Line Plot: {xlabel} vs {ylabel}"

    with plt.style.context(style):
        if ax is None:
            fig, ax = setup_plot(title=title, xlabel=xlabel, ylabel=ylabel, figsize=figsize)
            fig.set_dpi(dpi)
        else:
            ax.set_title(title)
            ax.set_xlabel(xlabel)
            ax.set_ylabel(ylabel)

        ax.plot(
            x_values,
            y_values,
            color=color,
            linewidth=linewidth,
            linestyle=linestyle,
            marker=marker,
            markersize=markersize,
            alpha=alpha,
            label=ylabel,
            **kwargs,
        )
        if fill_to is not None:
            ax.fill_between(x_values, y_values, fill_to, color=color, alpha=fill_alpha)
        if rolling_window is not None:
            validate_positive_int(rolling_window, "rolling_window")
            rolling = pd.Series(y_values).rolling(rolling_window, min_periods=1).mean()
            ax.plot(x_values, rolling, color=rolling_color, linewidth=linewidth, label=f"Rolling mean ({rolling_window})")
            ax.legend(fontsize=font_size)

        add_reference_lines(ax, hline=hline, vline=vline)
        ax.title.set_fontsize(title_size)
        ax.xaxis.label.set_fontsize(label_size)
        ax.yaxis.label.set_fontsize(label_size)
        ax.tick_params(labelsize=font_size)
        if grid:
            ax.grid(True, alpha=grid_alpha)
        apply_theme(ax, theme)
        return ax


def line_plot_interactive(
    x: Union[str, SeriesLike],
    y: Union[str, SeriesLike],
    data: Optional[pd.DataFrame] = None,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    color: Optional[str] = None,
    marker_color: Optional[str] = None,
    linewidth: float = 2.0,
    mode: str = "lines",
    marker_size: int = 8,
    showlegend: bool = True,
    hovermode: str = "x unified",
    template: str = "plotly",
    font_size: int = 12,
    title_size: int = 16,
    height: int = 600,
    width: int = 1000,
    na_policy: NaPolicy = "drop",
    sort_x: bool = False,
    rolling_window: Optional[int] = None,
    rolling_color: str = "crimson",
    fill_to: Optional[float] = None,
    hline: Optional[float] = None,
    vline: Optional[float] = None,
    **kwargs,
) -> PlotlyFigure:
    """Create an interactive line plot that shows ordered or time-based changes.

    Args:
        x (Union[str, SeriesLike]): X values or a column name when ``data`` is provided.
        y (Union[str, SeriesLike]): Y values or a column name when ``data`` is provided.
        data (Optional[pd.DataFrame]): Optional dataframe used for column lookup.
        title (Optional[str]): Chart title. Defaults to a generated title.
        xlabel (Optional[str]): X-axis label.
        ylabel (Optional[str]): Y-axis label.
        color (Optional[str]): Line color.
        marker_color (Optional[str]): Alias for ``color``.
        linewidth (float): Line width.
        mode (str): Plotly scatter mode.
        marker_size (int): Marker size.
        showlegend (bool): Whether to show the legend.
        hovermode (str): Plotly hover mode.
        template (str): Plotly template.
        font_size (int): Base font size.
        title_size (int): Title font size.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.
        na_policy (NaPolicy): Missing-value behavior: ``"drop"``, ``"raise"``, or ``"keep"``.
        sort_x (bool): Whether to sort paired observations by x before drawing.
        rolling_window (Optional[int]): Optional rolling mean window for y values.
        rolling_color (str): Rolling mean line color.
        fill_to (Optional[float]): Optional baseline for filled area under the line.
        hline (Optional[float]): Optional horizontal reference line.
        vline (Optional[float]): Optional vertical reference line.
        **kwargs: Additional keyword arguments forwarded to ``go.Scatter``.

    Returns:
        plotly.graph_objects.Figure: Configured Plotly line figure.

    Raises:
        TypeError: If inputs cannot be resolved or plotted.
        ValueError: If input lengths differ, inputs are empty, or options are invalid.

    Example:
        ```python
        fig = dv.line_plot_interactive("date", "sales", data=df, sort_x=True)
        ```

    Notes:
        Area fill is implemented with Plotly's ``tozeroy`` mode when ``fill_to`` is zero.
    """
    validate_positive_int(marker_size, "marker_size")
    x_values, y_values = resolve_xy_data(x, y, data=data, na_policy=na_policy)
    x_values, y_values = _maybe_sort(x_values, y_values, sort_x)
    xlabel = xlabel or x_values.name or "X"
    ylabel = ylabel or y_values.name or "Y"
    title = title or f"Line Plot: {xlabel} vs {ylabel}"
    if color is None:
        color = marker_color

    fill = "tozeroy" if fill_to == 0 else None
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=x_values,
            y=y_values,
            mode=mode,
            name=ylabel,
            fill=fill,
            line=dict(color=color, width=linewidth),
            marker=dict(size=marker_size),
            **kwargs,
        )
    )
    if rolling_window is not None:
        validate_positive_int(rolling_window, "rolling_window")
        rolling = pd.Series(y_values).rolling(rolling_window, min_periods=1).mean()
        fig.add_trace(
            go.Scatter(
                x=x_values,
                y=rolling,
                mode="lines",
                name=f"Rolling mean ({rolling_window})",
                line=dict(color=rolling_color, width=linewidth),
            )
        )

    add_plotly_reference_lines(fig, hline=hline, vline=vline)
    fig.update_layout(
        title=dict(text=title, font=dict(size=title_size)),
        xaxis_title=xlabel,
        yaxis_title=ylabel,
        hovermode=hovermode,
        template=template,
        font=dict(size=font_size),
        height=height,
        width=width,
        showlegend=showlegend,
    )
    return fig
