"""Line plot implementation - static and interactive versions."""

from typing import Optional, Tuple
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from ..utils import setup_plot, apply_theme


def line_plot_static(
    x: pd.Series,
    y: pd.Series,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    figsize: Tuple[int, int] = (10, 6),
    color: Optional[str] = None,
    linewidth: float = 2.0,
    linestyle: str = '-',
    marker: Optional[str] = None,
    markersize: int = 6,
    alpha: float = 1.0,
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = 'default',
    font_size: int = 10,
    title_size: int = 14,
    label_size: int = 11,
    dpi: int = 100,
    style: str = 'default',
    **kwargs
) -> plt.Axes:
    """
    Create a static line plot using matplotlib.

    Parameters
    ----------
    x : Series or array-like
        X-axis data
    y : Series or array-like
        Y-axis data
    title : str, optional
        Chart title
    xlabel : str, optional
        X-axis label
    ylabel : str, optional
        Y-axis label
    figsize : tuple, default (10, 6)
        Figure size (width, height)
    color : str, optional
        Line color
    linewidth : float, default 2.0
        Line width
    linestyle : str, default '-'
        Line style: '-', '--', '-.', ':'
    marker : str, optional
        Marker style ('o', 's', '^', etc.)
    markersize : int, default 6
        Marker size
    alpha : float, default 1.0
        Transparency
    grid : bool, default True
        Show grid
    grid_alpha : float, default 0.3
        Grid transparency
    theme : str, default 'default'
        Theme: 'default', 'dark', 'minimal'
    font_size : int, default 10
        Base font size
    title_size : int, default 14
        Title font size
    label_size : int, default 11
        Axis label font size
    dpi : int, default 100
        Figure DPI
    style : str, default 'default'
        Matplotlib style
    **kwargs
        Additional line plot arguments

    Returns
    -------
    matplotlib.axes.Axes
        The plot axes
    """
    if title is None:
        x_name = xlabel or (x.name if hasattr(x, 'name') else 'X')
        y_name = ylabel or (y.name if hasattr(y, 'name') else 'Y')
        title = f"Line Plot: {x_name} vs {y_name}"
    
    if xlabel is None:
        xlabel = x.name if hasattr(x, 'name') else 'X'
    if ylabel is None:
        ylabel = y.name if hasattr(y, 'name') else 'Y'
    
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel=xlabel, ylabel=ylabel, figsize=figsize)
        fig.set_dpi(dpi)
        
        ax.plot(
            x, y,
            color=color,
            linewidth=linewidth,
            linestyle=linestyle,
            marker=marker,
            markersize=markersize,
            alpha=alpha,
            **kwargs
        )
        
        # Customize fonts
        ax.title.set_fontsize(title_size)
        ax.xaxis.label.set_fontsize(label_size)
        ax.yaxis.label.set_fontsize(label_size)
        ax.tick_params(labelsize=font_size)
        
        # Grid
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


def line_plot_interactive(
    x: pd.Series,
    y: pd.Series,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    color: Optional[str] = None,
    marker_color: Optional[str] = None,
    linewidth: float = 2.0,
    mode: str = 'lines',
    marker_size: int = 8,
    showlegend: bool = True,
    hovermode: str = 'x unified',
    template: str = 'plotly',
    font_size: int = 12,
    title_size: int = 16,
    height: int = 600,
    width: int = 1000,
    **kwargs
) -> go.Figure:
    """
    Create an interactive line plot using plotly.

    Parameters
    ----------
    x : Series or array-like
        X-axis data
    y : Series or array-like
        Y-axis data
    title : str, optional
        Chart title
    xlabel : str, optional
        X-axis label
    ylabel : str, optional
        Y-axis label
    color : str, optional
        Line color
    marker_color : str, optional
        Alternative marker color parameter
    linewidth : float, default 2.0
        Line width
    mode : str, default 'lines'
        Plot mode: 'lines', 'markers', 'lines+markers'
    marker_size : int, default 8
        Marker size
    showlegend : bool, default True
        Show legend
    hovermode : str, default 'x unified'
        Hover mode type
    template : str, default 'plotly'
        Plotly template
    font_size : int, default 12
        Font size
    title_size : int, default 16
        Title font size
    height : int, default 600
        Figure height in pixels
    width : int, default 1000
        Figure width in pixels
    **kwargs
        Additional plot arguments

    Returns
    -------
    plotly.graph_objects.Figure
        The interactive figure
    """
    if title is None:
        x_name = xlabel or (x.name if hasattr(x, 'name') else 'X')
        y_name = ylabel or (y.name if hasattr(y, 'name') else 'Y')
        title = f"Line Plot: {x_name} vs {y_name}"
    
    if xlabel is None:
        xlabel = x.name if hasattr(x, 'name') else 'X'
    if ylabel is None:
        ylabel = y.name if hasattr(y, 'name') else 'Y'
    
    if color is None:
        color = marker_color
    
    fig = go.Figure(data=[
        go.Scatter(
            x=x,
            y=y,
            mode=mode,
            line=dict(
                color=color,
                width=linewidth
            ),
            marker=dict(size=marker_size),
            **kwargs
        )
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
    )
    
    return fig
