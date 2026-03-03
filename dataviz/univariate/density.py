"""Density plot implementation - static and interactive versions."""

from typing import Optional, Tuple
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from ..utils import setup_plot, apply_theme


def density_static(
    data: pd.Series,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    figsize: Tuple[int, int] = (10, 6),
    color: Optional[str] = None,
    linewidth: float = 2.0,
    alpha: float = 0.7,
    fill: bool = True,
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
    Create a static kernel density estimation (KDE) plot using matplotlib.

    Parameters
    ----------
    data : Series or array-like
        Data to visualize
    title : str, optional
        Chart title
    xlabel : str, optional
        X-axis label
    ylabel : str, optional
        Y-axis label
    figsize : tuple, default (10, 6)
        Figure size (width, height)
    color : str, optional
        Line/fill color
    linewidth : float, default 2.0
        Line width
    alpha : float, default 0.7
        Transparency (0-1)
    fill : bool, default True
        Fill under curve
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
        Additional plot arguments

    Returns
    -------
    matplotlib.axes.Axes
        The plot axes
    """
    if title is None:
        title = f"Density Plot - {data.name if hasattr(data, 'name') else 'Distribution'}"
    if xlabel is None:
        xlabel = data.name if hasattr(data, 'name') else 'Value'
    if ylabel is None:
        ylabel = 'Density'
    
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel=xlabel, ylabel=ylabel, figsize=figsize)
        fig.set_dpi(dpi)
        
        data.plot.kde(ax=ax, color=color, linewidth=linewidth, alpha=alpha, fill=fill, **kwargs)
        
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


def density_interactive(
    data: pd.Series,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    color: Optional[str] = None,
    linewidth: float = 2,
    alpha: float = 0.7,
    showlegend: bool = True,
    hovermode: str = 'x unified',
    template: str = 'plotly',
    font_size: int = 12,
    title_size: int = 16,
    height: int = 600,
    width: int = 1000,
    histnorm: str = 'probability density',
    **kwargs
) -> go.Figure:
    """
    Create an interactive density plot using plotly.

    Parameters
    ----------
    data : Series or array-like
        Data to visualize
    title : str, optional
        Chart title
    xlabel : str, optional
        X-axis label
    ylabel : str, optional
        Y-axis label
    color : str, optional
        Line/fill color
    linewidth : float, default 2
        Line width
    alpha : float, default 0.7
        Transparency (0-1)
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
    histnorm : str, default 'probability density'
        Histogram normalization
    **kwargs
        Additional plot arguments

    Returns
    -------
    plotly.graph_objects.Figure
        The interactive figure
    """
    if title is None:
        title = f"Density Plot - {data.name if hasattr(data, 'name') else 'Distribution'}"
    if xlabel is None:
        xlabel = data.name if hasattr(data, 'name') else 'Value'
    if ylabel is None:
        ylabel = 'Density'
    
    fig = go.Figure(data=[
        go.Histogram(x=data, histnorm=histnorm, marker_color=color, opacity=alpha, **kwargs)
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
