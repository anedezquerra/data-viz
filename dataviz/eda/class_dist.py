"""Class distribution implementation - static and interactive versions."""

from typing import Optional, Tuple
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from ..utils import setup_plot, apply_theme


def class_distribution_static(
    series: pd.Series,
    title: Optional[str] = None,
    figsize: Tuple[int, int] = (10, 6),
    color: Optional[str] = None,
    edgecolor: str = 'black',
    linewidth: float = 1.0,
    alpha: float = 0.7,
    sort: bool = True,
    ascending: bool = False,
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
    Create a static class distribution plot using matplotlib.

    Parameters
    ----------
    series : Series
        Categorical data
    title : str, optional
        Chart title
    figsize : tuple, default (10, 6)
        Figure size (width, height)
    color : str, optional
        Bar color
    edgecolor : str, default 'black'
        Bar edge color
    linewidth : float, default 1.0
        Edge line width
    alpha : float, default 0.7
        Transparency
    sort : bool, default True
        Sort by count
    ascending : bool, default False
        Sort in ascending order
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
        title = f"Class Distribution - {series.name if hasattr(series, 'name') else 'Distribution'}"
    
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, figsize=figsize)
        fig.set_dpi(dpi)
        
        value_counts = series.value_counts()
        if sort:
            value_counts = value_counts.sort_values(ascending=ascending)
        
        ax.bar(
            value_counts.index,
            value_counts.values,
            color=color,
            edgecolor=edgecolor,
            linewidth=linewidth,
            alpha=alpha,
            **kwargs
        )
        ax.set_ylabel('Count', fontsize=label_size)
        ax.set_xlabel('Class', fontsize=label_size)
        ax.title.set_fontsize(title_size)
        ax.tick_params(labelsize=font_size)
        
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


def class_distribution_interactive(
    series: pd.Series,
    title: Optional[str] = None,
    color: Optional[str] = None,
    marker_color: Optional[str] = None,
    sort: bool = True,
    ascending: bool = False,
    showlegend: bool = True,
    hovermode: str = 'closest',
    template: str = 'plotly',
    font_size: int = 12,
    title_size: int = 16,
    height: int = 600,
    width: int = 1000,
    **kwargs
) -> go.Figure:
    """
    Create an interactive class distribution plot using plotly.

    Parameters
    ----------
    series : Series
        Categorical data
    title : str, optional
        Chart title
    color : str, optional
        Bar color
    marker_color : str, optional
        Alternative marker color parameter
    sort : bool, default True
        Sort by count
    ascending : bool, default False
        Sort in ascending order
    showlegend : bool, default True
        Show legend
    hovermode : str, default 'closest'
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
        title = f"Class Distribution - {series.name if hasattr(series, 'name') else 'Distribution'}"
    if color is None:
        color = marker_color
    
    value_counts = series.value_counts()
    if sort:
        value_counts = value_counts.sort_values(ascending=ascending)
    
    fig = go.Figure(data=[
        go.Bar(
            x=value_counts.index,
            y=value_counts.values,
            marker_color=color,
            **kwargs
        )
    ])
    
    fig.update_layout(
        title=dict(text=title, font=dict(size=title_size)),
        xaxis_title='Class',
        yaxis_title='Count',
        hovermode=hovermode,
        template=template,
        font=dict(size=font_size),
        height=height,
        width=width,
        showlegend=showlegend,
    )
    
    return fig
