"""Histogram chart implementation - static and interactive versions."""

from typing import Optional, List, Tuple
from ..types import FigureSize, MatplotlibAxes, PlotlyFigure, SeriesLike
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from ..utils import setup_plot, apply_theme


def histogram_static(
    data: SeriesLike,
    bins: int = 30,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    color: Optional[str] = None,
    edgecolor: str = 'black',
    alpha: float = 0.7,
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
    """Create a static histogram that summarizes the frequency distribution of one variable.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        data (SeriesLike): Input observations, measurements, or values used to build the chart.
        bins (int): Number of bins used for histogram-like displays. Defaults to ``30``.
        title (Optional[str]): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``None``.
        xlabel (Optional[str]): Optional x-axis label. Defaults to ``None``.
        ylabel (Optional[str]): Optional y-axis label. Defaults to ``None``.
        figsize (FigureSize): Matplotlib figure size as ``(width, height)`` in inches. Defaults to ``(10, 6)``.
        color (Optional[str]): Configuration value for ``color``. Defaults to ``None``.
        edgecolor (str): Configuration value for ``edgecolor``. Defaults to ``'black'``.
        alpha (float): Configuration value for ``alpha``. Defaults to ``0.7``.
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
    
    Examples:
        ```python
        import dataviz as dv
        result = dv.histogram_static(data)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
    """
    if title is None:
        title = f"Histogram - {data.name if hasattr(data, 'name') else 'Distribution'}"
    if xlabel is None:
        xlabel = data.name if hasattr(data, 'name') else 'Value'
    if ylabel is None:
        ylabel = 'Frequency'
    
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel=xlabel, ylabel=ylabel, figsize=figsize)
        fig.set_dpi(dpi)
        
        ax.hist(data, bins=bins, color=color, edgecolor=edgecolor, alpha=alpha, **kwargs)
        
        # Customize fonts
        ax.title.set_fontsize(title_size)
        ax.xaxis.label.set_fontsize(label_size)
        ax.yaxis.label.set_fontsize(label_size)
        ax.tick_params(labelsize=font_size)
        
        # Grid
        if grid:
            ax.grid(True, alpha=grid_alpha, axis='y')
        
        # Theme
        if theme == 'dark':
            ax.set_facecolor('#f0f0f0')
        elif theme == 'minimal':
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
        
        apply_theme(ax, theme)
    
    return ax


def histogram_interactive(
    data: SeriesLike,
    bins: int = 30,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    color: Optional[str] = None,
    marker_color: Optional[str] = None,
    alpha: float = 0.7,
    showlegend: bool = True,
    hovermode: str = 'x unified',
    template: str = 'plotly',
    font_size: int = 12,
    title_size: int = 16,
    height: int = 600,
    width: int = 1000,
    bargap: float = 0.1,
    **kwargs
) -> PlotlyFigure:
    """Create an interactive histogram that summarizes the frequency distribution of one variable.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        data (SeriesLike): Input observations, measurements, or values used to build the chart.
        bins (int): Number of bins used for histogram-like displays. Defaults to ``30``.
        title (Optional[str]): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``None``.
        xlabel (Optional[str]): Optional x-axis label. Defaults to ``None``.
        ylabel (Optional[str]): Optional y-axis label. Defaults to ``None``.
        color (Optional[str]): Configuration value for ``color``. Defaults to ``None``.
        marker_color (Optional[str]): Configuration value for ``marker_color``. Defaults to ``None``.
        alpha (float): Configuration value for ``alpha``. Defaults to ``0.7``.
        showlegend (bool): Configuration value for ``showlegend``. Defaults to ``True``.
        hovermode (str): Configuration value for ``hovermode``. Defaults to ``'x unified'``.
        template (str): Plotly template used to style the interactive figure. Defaults to ``'plotly'``.
        font_size (int): Configuration value for ``font_size``. Defaults to ``12``.
        title_size (int): Configuration value for ``title_size``. Defaults to ``16``.
        height (int): Plotly figure height in pixels. Defaults to ``600``.
        width (int): Plotly figure width in pixels. Defaults to ``1000``.
        bargap (float): Configuration value for ``bargap``. Defaults to ``0.1``.
        **kwargs (Any): Additional keyword arguments forwarded to the underlying plotting function.
    
    Returns:
        plotly.graph_objects.Figure: Configured Plotly figure containing the rendered interactive chart.
    
    Raises:
        TypeError: If required inputs are not compatible with the plotting backend.
        ValueError: If input lengths, matrix shapes, or option values are invalid for the requested chart.
    
    Examples:
        ```python
        import dataviz as dv
        result = dv.histogram_interactive(data)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
    """
    if title is None:
        title = f"Histogram - {data.name if hasattr(data, 'name') else 'Distribution'}"
    if xlabel is None:
        xlabel = data.name if hasattr(data, 'name') else 'Value'
    if ylabel is None:
        ylabel = 'Frequency'
    if color is None:
        color = marker_color
    
    fig = go.Figure(data=[
        go.Histogram(x=data, nbinsx=bins, marker_color=color, opacity=alpha, **kwargs)
    ])
    
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
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True),
        bargap=bargap,
    )
    
    return fig
