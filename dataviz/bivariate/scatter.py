"""Scatter plot implementation - static and interactive versions."""

from typing import Optional, Sequence, Tuple, Union

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objects as go

from ..types import FigureSize, MatplotlibAxes, PlotlyFigure, SeriesLike
from ..utils import (
    add_plotly_reference_lines,
    add_reference_lines,
    apply_theme,
    resolve_series,
    resolve_xy_data,
    setup_plot,
    validate_alpha,
    validate_equal_length,
    validate_positive_int,
)
from ..utils.validation import NaPolicy


def _fit_line(x: SeriesLike, y: SeriesLike, degree: int) -> Tuple[np.ndarray, np.ndarray]:
    """Fit a polynomial line for scatter overlays.

    Args:
        x (SeriesLike): Numeric x values.
        y (SeriesLike): Numeric y values.
        degree (int): Polynomial degree.

    Returns:
        tuple[numpy.ndarray, numpy.ndarray]: Sorted x values and fitted y values.

    Raises:
        TypeError: If x or y cannot be converted to floats.
        ValueError: If the degree is invalid for the available observations.

    Example:
        ```python
        x_fit, y_fit = _fit_line(x, y, degree=1)
        ```

    Notes:
        This helper keeps the public scatter functions free of repeated fit logic.
    """
    x_values = np.asarray(x, dtype=float)
    y_values = np.asarray(y, dtype=float)
    order = np.argsort(x_values)
    x_sorted = x_values[order]
    coeffs = np.polyfit(x_sorted, y_values[order], degree)
    return x_sorted, np.polyval(coeffs, x_sorted)


def _scatter_row_positions(
    x: Union[str, SeriesLike],
    y: Union[str, SeriesLike],
    data: Optional[pd.DataFrame],
    na_policy: NaPolicy,
) -> Tuple[np.ndarray, int]:
    """Return source-row positions retained by paired missing-value handling."""
    x_source = resolve_series(x, data=data, fallback_name="X")
    y_source = resolve_series(y, data=data, fallback_name="Y")
    validate_equal_length(x_source, y_source, names=("x", "y"))
    frame = pd.DataFrame(
        {"x": x_source.to_numpy(), "y": y_source.to_numpy()}
    )
    if na_policy == "drop":
        retained = np.flatnonzero(~frame.isna().any(axis=1).to_numpy())
    else:
        retained = np.arange(len(frame))
    return retained, len(frame)


def _align_scatter_metadata(
    value: Union[str, SeriesLike],
    data: Optional[pd.DataFrame],
    retained: np.ndarray,
    expected_length: int,
    name: str,
) -> pd.Series:
    """Apply the paired-data row selection to hue or point-label metadata."""
    values = resolve_series(value, data=data, fallback_name=name.title())
    validate_equal_length(range(expected_length), values, names=("x", name))
    normalized = pd.Series(values.to_numpy(), name=values.name)
    return normalized.iloc[retained].reset_index(drop=True)


def scatter_plot_static(
    x: Union[str, SeriesLike],
    y: Union[str, SeriesLike],
    data: Optional[pd.DataFrame] = None,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    color: Optional[str] = None,
    hue: Optional[Union[str, SeriesLike]] = None,
    marker: str = "o",
    size: int = 50,
    alpha: float = 0.6,
    edgecolor: str = "black",
    linewidth: float = 1.0,
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
    hline: Optional[float] = None,
    vline: Optional[float] = None,
    diagonal: bool = False,
    fit_degree: Optional[int] = None,
    fit_color: str = "crimson",
    show_corr: bool = False,
    annotate_points: Optional[Sequence[str]] = None,
    **kwargs,
) -> MatplotlibAxes:
    """Create a static scatter plot to compare two variables.

    Builds the visualization with package defaults while allowing dataframe-column
    inputs, missing-value handling, reference lines, grouped colors, and optional
    polynomial trend overlays.

    Args:
        x (Union[str, SeriesLike]): X values or a column name when ``data`` is provided.
        y (Union[str, SeriesLike]): Y values or a column name when ``data`` is provided.
        data (Optional[pd.DataFrame]): Optional dataframe used for column lookup.
        title (Optional[str]): Chart title. Defaults to a generated title.
        xlabel (Optional[str]): X-axis label. Defaults to the x series name or ``"X"``.
        ylabel (Optional[str]): Y-axis label. Defaults to the y series name or ``"Y"``.
        figsize (FigureSize): Matplotlib figure size in inches.
        color (Optional[str]): Default marker color when ``hue`` is not provided.
        hue (Optional[Union[str, SeriesLike]]): Optional grouping or color values.
        marker (str): Marker style.
        size (int): Marker area.
        alpha (float): Marker opacity from 0 to 1.
        edgecolor (str): Marker edge color.
        linewidth (float): Marker edge width.
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
        hline (Optional[float]): Optional horizontal reference line.
        vline (Optional[float]): Optional vertical reference line.
        diagonal (bool): Whether to draw a y=x reference line.
        fit_degree (Optional[int]): Polynomial degree for an optional trend line.
        fit_color (str): Trend-line color.
        show_corr (bool): Whether to add Pearson correlation to the title.
        annotate_points (Optional[Sequence[str]]): Optional point labels.
        **kwargs: Additional keyword arguments forwarded to ``Axes.scatter``.

    Returns:
        matplotlib.axes.Axes: Configured matplotlib axes containing the scatter plot.

    Raises:
        TypeError: If inputs cannot be resolved or plotted.
        ValueError: If input lengths differ, inputs are empty, or options are invalid.

    Example:
        ```python
        ax = dv.scatter_plot_static("height", "weight", data=df, fit_degree=1)
        ```

    Notes:
        Passing ``ax`` enables subplot workflows without creating a new figure.
    """
    validate_alpha(alpha)
    validate_positive_int(size, "size")
    x_values, y_values = resolve_xy_data(x, y, data=data, na_policy=na_policy)
    retained, input_length = _scatter_row_positions(x, y, data, na_policy)
    xlabel = xlabel or x_values.name or "X"
    ylabel = ylabel or y_values.name or "Y"
    title = title or f"Scatter Plot: {xlabel} vs {ylabel}"
    if show_corr:
        corr = pd.Series(x_values).corr(pd.Series(y_values))
        title = f"{title} (r = {corr:.3f})"

    hue_values = None
    if hue is not None:
        hue_values = _align_scatter_metadata(
            hue, data, retained, input_length, "hue"
        )
    point_labels = None
    if annotate_points is not None:
        point_labels = _align_scatter_metadata(
            annotate_points, None, retained, input_length, "annotate_points"
        )

    with plt.style.context(style):
        if ax is None:
            fig, ax = setup_plot(title=title, xlabel=xlabel, ylabel=ylabel, figsize=figsize)
            fig.set_dpi(dpi)
        else:
            ax.set_title(title)
            ax.set_xlabel(xlabel)
            ax.set_ylabel(ylabel)

        if hue_values is not None and not pd.api.types.is_numeric_dtype(hue_values):
            for group_name in pd.unique(hue_values):
                mask = np.asarray(hue_values == group_name)
                ax.scatter(
                    x_values[mask],
                    y_values[mask],
                    marker=marker,
                    s=size,
                    alpha=alpha,
                    edgecolors=edgecolor,
                    linewidth=linewidth,
                    label=str(group_name),
                    **kwargs,
                )
            ax.legend(fontsize=font_size)
        else:
            ax.scatter(
                x_values,
                y_values,
                marker=marker,
                s=size,
                c=hue_values if hue_values is not None else color,
                alpha=alpha,
                edgecolors=edgecolor,
                linewidth=linewidth,
                **kwargs,
            )

        if fit_degree is not None:
            validate_positive_int(fit_degree, "fit_degree")
            x_fit, y_fit = _fit_line(x_values, y_values, fit_degree)
            ax.plot(x_fit, y_fit, color=fit_color, linewidth=2, label=f"Degree {fit_degree} fit")
            ax.legend(fontsize=font_size)

        if point_labels is not None:
            for x_point, y_point, label in zip(x_values, y_values, point_labels):
                ax.annotate(str(label), (x_point, y_point), fontsize=font_size)

        add_reference_lines(ax, hline=hline, vline=vline, diagonal=diagonal)
        ax.title.set_fontsize(title_size)
        ax.xaxis.label.set_fontsize(label_size)
        ax.yaxis.label.set_fontsize(label_size)
        ax.tick_params(labelsize=font_size)
        if grid:
            ax.grid(True, alpha=grid_alpha)
        apply_theme(ax, theme)
        return ax


def scatter_plot_interactive(
    x: Union[str, SeriesLike],
    y: Union[str, SeriesLike],
    data: Optional[pd.DataFrame] = None,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    color: Optional[str] = None,
    marker_color: Optional[str] = None,
    hue: Optional[Union[str, SeriesLike]] = None,
    size: int = 8,
    mode: str = "markers",
    showlegend: bool = True,
    hovermode: str = "closest",
    template: str = "plotly",
    font_size: int = 12,
    title_size: int = 16,
    height: int = 600,
    width: int = 1000,
    na_policy: NaPolicy = "drop",
    hline: Optional[float] = None,
    vline: Optional[float] = None,
    diagonal: bool = False,
    fit_degree: Optional[int] = None,
    fit_color: str = "crimson",
    show_corr: bool = False,
    text: Optional[Sequence[str]] = None,
    **kwargs,
) -> PlotlyFigure:
    """Create an interactive scatter plot to compare two variables.

    Builds a Plotly scatter plot with dataframe-column lookup, missing-value
    handling, optional grouping, reference lines, and optional polynomial trend
    overlays.

    Args:
        x (Union[str, SeriesLike]): X values or a column name when ``data`` is provided.
        y (Union[str, SeriesLike]): Y values or a column name when ``data`` is provided.
        data (Optional[pd.DataFrame]): Optional dataframe used for column lookup.
        title (Optional[str]): Chart title. Defaults to a generated title.
        xlabel (Optional[str]): X-axis label. Defaults to the x series name or ``"X"``.
        ylabel (Optional[str]): Y-axis label. Defaults to the y series name or ``"Y"``.
        color (Optional[str]): Marker color when ``hue`` is not provided.
        marker_color (Optional[str]): Alias for ``color``.
        hue (Optional[Union[str, SeriesLike]]): Optional color/grouping values.
        size (int): Marker size.
        mode (str): Plotly scatter mode.
        showlegend (bool): Whether to show the legend.
        hovermode (str): Plotly hover mode.
        template (str): Plotly template.
        font_size (int): Base font size.
        title_size (int): Title font size.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.
        na_policy (NaPolicy): Missing-value behavior: ``"drop"``, ``"raise"``, or ``"keep"``.
        hline (Optional[float]): Optional horizontal reference line.
        vline (Optional[float]): Optional vertical reference line.
        diagonal (bool): Whether to draw a y=x reference line.
        fit_degree (Optional[int]): Polynomial degree for an optional trend line.
        fit_color (str): Trend-line color.
        show_corr (bool): Whether to add Pearson correlation to the title.
        text (Optional[Sequence[str]]): Optional point labels or hover text.
        **kwargs: Additional keyword arguments forwarded to ``go.Scatter``.

    Returns:
        plotly.graph_objects.Figure: Configured Plotly scatter figure.

    Raises:
        TypeError: If inputs cannot be resolved or plotted.
        ValueError: If input lengths differ, inputs are empty, or options are invalid.

    Example:
        ```python
        fig = dv.scatter_plot_interactive("height", "weight", data=df, hue="species")
        ```

    Notes:
        Categorical ``hue`` values are rendered as separate traces.
    """
    validate_positive_int(size, "size")
    x_values, y_values = resolve_xy_data(x, y, data=data, na_policy=na_policy)
    retained, input_length = _scatter_row_positions(x, y, data, na_policy)
    xlabel = xlabel or x_values.name or "X"
    ylabel = ylabel or y_values.name or "Y"
    title = title or f"Scatter Plot: {xlabel} vs {ylabel}"
    if show_corr:
        corr = pd.Series(x_values).corr(pd.Series(y_values))
        title = f"{title} (r = {corr:.3f})"
    if color is None:
        color = marker_color

    fig = go.Figure()
    hue_values = (
        _align_scatter_metadata(hue, data, retained, input_length, "hue")
        if hue is not None
        else None
    )
    text_values = (
        _align_scatter_metadata(text, None, retained, input_length, "text")
        if text is not None
        else None
    )
    if hue_values is not None and not pd.api.types.is_numeric_dtype(hue_values):
        for group_name in pd.unique(hue_values):
            mask = np.asarray(hue_values == group_name)
            fig.add_trace(
                go.Scatter(
                    x=x_values[mask],
                    y=y_values[mask],
                    mode=mode,
                    name=str(group_name),
                    text=text_values[mask] if text_values is not None else None,
                    marker=dict(size=size),
                    **kwargs,
                )
            )
    else:
        marker = dict(size=size, color=hue_values if hue_values is not None else color)
        fig.add_trace(
            go.Scatter(
                x=x_values,
                y=y_values,
                mode=mode,
                text=text_values,
                marker=marker,
                **kwargs,
            )
        )

    if fit_degree is not None:
        validate_positive_int(fit_degree, "fit_degree")
        x_fit, y_fit = _fit_line(x_values, y_values, fit_degree)
        fig.add_trace(
            go.Scatter(
                x=x_fit,
                y=y_fit,
                mode="lines",
                name=f"Degree {fit_degree} fit",
                line=dict(color=fit_color, width=2),
            )
        )

    add_plotly_reference_lines(fig, hline=hline, vline=vline, diagonal=diagonal, x_values=x_values, y_values=y_values)
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
