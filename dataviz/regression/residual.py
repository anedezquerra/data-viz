"""Residual plot implementation - static and interactive versions."""

from typing import Optional, Tuple
from ..types import ArrayLike, FigureSize, MatplotlibAxes, PlotlyFigure
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from ..utils import setup_plot, apply_theme


def residual_plot_static(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    title: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    color: Optional[str] = None,
    edgecolor: str = 'black',
    linewidth: float = 1.0,
    marker_size: int = 50,
    alpha: float = 0.6,
    line_color: str = 'red',
    line_style: str = '--',
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = 'default',
    font_size: int = 10,
    title_size: int = 14,
    label_size: int = 11,
    dpi: int = 100,
    style: str = 'default',
    **kwargs
) -> MatplotlibAxes:
    """Create a static residual diagnostic plot for regression predictions.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        y_true (ArrayLike): Observed target values.
        y_pred (ArrayLike): Predicted target values.
        title (Optional[str]): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``None``.
        figsize (FigureSize): Matplotlib figure size as ``(width, height)`` in inches. Defaults to ``(10, 6)``.
        color (Optional[str]): Configuration value for ``color``. Defaults to ``None``.
        edgecolor (str): Configuration value for ``edgecolor``. Defaults to ``'black'``.
        linewidth (float): Configuration value for ``linewidth``. Defaults to ``1.0``.
        marker_size (int): Configuration value for ``marker_size``. Defaults to ``50``.
        alpha (float): Configuration value for ``alpha``. Defaults to ``0.6``.
        line_color (str): Configuration value for ``line_color``. Defaults to ``'red'``.
        line_style (str): Configuration value for ``line_style``. Defaults to ``'--'``.
        grid (bool): Configuration value for ``grid``. Defaults to ``True``.
        grid_alpha (float): Configuration value for ``grid_alpha``. Defaults to ``0.3``.
        theme (str): Named styling theme applied after the base plot is created. Defaults to ``'default'``.
        font_size (int): Configuration value for ``font_size``. Defaults to ``10``.
        title_size (int): Configuration value for ``title_size``. Defaults to ``14``.
        label_size (int): Configuration value for ``label_size``. Defaults to ``11``.
        dpi (int): Configuration value for ``dpi``. Defaults to ``100``.
        style (str): Matplotlib style context used while building the figure. Defaults to ``'default'``.
        **kwargs (Any): Additional keyword arguments forwarded to the underlying plotting function.
    
    Returns:
        matplotlib.axes.Axes: Configured matplotlib axes containing the rendered static chart.
    
    Raises:
        TypeError: If required inputs are not compatible with the plotting backend.
        ValueError: If input lengths, matrix shapes, or option values are invalid for the requested chart.
    
    Example:
        ```python
        import dataviz as dv
        result = dv.residual_plot_static(y_true, y_pred)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
    """
    if title is None:
        title = "Residual Plot"
    
    residuals = y_true - y_pred
    
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel='Predicted Values', ylabel='Residuals', figsize=figsize)
        fig.set_dpi(dpi)
        
        ax.scatter(
            y_pred, residuals,
            color=color,
            edgecolors=edgecolor,
            linewidth=linewidth,
            s=marker_size,
            alpha=alpha,
            **kwargs
        )
        ax.axhline(y=0, color=line_color, linestyle=line_style, linewidth=2)
        
        # Customize fonts
        ax.title.set_fontsize(title_size)
        ax.xaxis.label.set_fontsize(label_size)
        ax.yaxis.label.set_fontsize(label_size)
        ax.tick_params(labelsize=font_size)
        
        if grid:
            ax.grid(True, alpha=grid_alpha)
        
        # Theme
        if theme == 'dark':
            ax.set_facecolor('#f0f0f0')
        elif theme == 'minimal':
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
        
        apply_theme(ax, theme)
    
    return ax


def residual_plot_interactive(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    title: Optional[str] = None,
    color: Optional[str] = None,
    marker_color: Optional[str] = None,
    marker_size: int = 8,
    line_color: str = 'red',
    line_dash: str = 'dash',
    showlegend: bool = True,
    hovermode: str = 'closest',
    template: str = 'plotly',
    font_size: int = 12,
    title_size: int = 16,
    height: int = 600,
    width: int = 1000,
    **kwargs
) -> PlotlyFigure:
    """Create an interactive residual diagnostic plot for regression predictions.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        y_true (ArrayLike): Observed target values.
        y_pred (ArrayLike): Predicted target values.
        title (Optional[str]): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``None``.
        color (Optional[str]): Configuration value for ``color``. Defaults to ``None``.
        marker_color (Optional[str]): Configuration value for ``marker_color``. Defaults to ``None``.
        marker_size (int): Configuration value for ``marker_size``. Defaults to ``8``.
        line_color (str): Configuration value for ``line_color``. Defaults to ``'red'``.
        line_dash (str): Configuration value for ``line_dash``. Defaults to ``'dash'``.
        showlegend (bool): Configuration value for ``showlegend``. Defaults to ``True``.
        hovermode (str): Configuration value for ``hovermode``. Defaults to ``'closest'``.
        template (str): Plotly template used to style the interactive figure. Defaults to ``'plotly'``.
        font_size (int): Configuration value for ``font_size``. Defaults to ``12``.
        title_size (int): Configuration value for ``title_size``. Defaults to ``16``.
        height (int): Plotly figure height in pixels. Defaults to ``600``.
        width (int): Plotly figure width in pixels. Defaults to ``1000``.
        **kwargs (Any): Additional keyword arguments forwarded to the underlying plotting function.
    
    Returns:
        plotly.graph_objects.Figure: Configured Plotly figure containing the rendered interactive chart.
    
    Raises:
        TypeError: If required inputs are not compatible with the plotting backend.
        ValueError: If input lengths, matrix shapes, or option values are invalid for the requested chart.
    
    Example:
        ```python
        import dataviz as dv
        result = dv.residual_plot_interactive(y_true, y_pred)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
    """
    if title is None:
        title = "Residual Plot"
    if color is None:
        color = marker_color
    
    residuals = y_true - y_pred
    
    fig = go.Figure(data=[
        go.Scatter(
            x=y_pred,
            y=residuals,
            mode='markers',
            marker=dict(size=marker_size, color=color),
            **kwargs
        )
    ])
    
    # Add reference line at y=0
    fig.add_hline(y=0, line_dash=line_dash, line_color=line_color)
    
    fig.update_layout(
        title=dict(text=title, font=dict(size=title_size)),
        xaxis_title='Predicted Values',
        yaxis_title='Residuals',
        hovermode=hovermode,
        template=template,
        font=dict(size=font_size),
        height=height,
        width=width,
        showlegend=showlegend,
    )
    
    return fig
