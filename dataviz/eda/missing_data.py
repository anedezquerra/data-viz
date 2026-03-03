"""Missing data plot implementation - static and interactive versions."""

from typing import Optional, Tuple
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from ..utils import setup_plot, apply_theme


def missing_data_plot_static(
    df: pd.DataFrame,
    title: Optional[str] = None,
    figsize: Tuple[int, int] = (12, 6),
    color: Optional[str] = None,
    edgecolor: str = 'black',
    linewidth: float = 1.0,
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
) -> plt.Axes:
    """
    Create a static missing data visualization using matplotlib.

    Parameters
    ----------
    df : DataFrame
        Input data
    title : str, optional
        Chart title
    figsize : tuple, default (12, 6)
        Figure size (width, height)
    color : str, optional
        Bar color
    edgecolor : str, default 'black'
        Bar edge color
    linewidth : float, default 1.0
        Edge line width
    alpha : float, default 0.7
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
        Additional plot arguments

    Returns
    -------
    matplotlib.axes.Axes
        The plot axes
    """
    if title is None:
        title = "Missing Data Analysis"
    
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, figsize=figsize)
        fig.set_dpi(dpi)
        
        missing = df.isnull().sum()
        missing_pct = (missing / len(df)) * 100
        
        if missing.sum() > 0:
            ax.barh(
                missing[missing > 0].index,
                missing_pct[missing > 0],
                color=color,
                edgecolor=edgecolor,
                linewidth=linewidth,
                alpha=alpha,
                **kwargs
            )
            ax.set_xlabel('Percentage Missing (%)', fontsize=label_size)
            if grid:
                ax.grid(True, alpha=grid_alpha, axis='x')
        else:
            ax.text(0.5, 0.5, 'No missing data found', 
                    ha='center', va='center', transform=ax.transAxes,
                    fontsize=font_size)
        
        # Customize fonts
        ax.title.set_fontsize(title_size)
        ax.tick_params(labelsize=font_size)
        
        # Theme
        if theme == 'dark':
            ax.set_facecolor('#f0f0f0')
        elif theme == 'minimal':
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
        
        apply_theme(ax, theme)
    
    return ax


def missing_data_plot_interactive(
    df: pd.DataFrame,
    title: Optional[str] = None,
    color: Optional[str] = None,
    marker_color: Optional[str] = None,
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
    Create an interactive missing data visualization using plotly.

    Parameters
    ----------
    df : DataFrame
        Input data
    title : str, optional
        Chart title
    color : str, optional
        Bar color
    marker_color : str, optional
        Alternative marker color parameter
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
        title = "Missing Data Analysis"
    if color is None:
        color = marker_color
    
    missing = df.isnull().sum()
    missing_pct = (missing / len(df)) * 100
    
    if missing.sum() > 0:
        fig = go.Figure(data=[
            go.Bar(
                y=missing[missing > 0].index,
                x=missing_pct[missing > 0],
                orientation='h',
                marker_color=color,
                **kwargs
            )
        ])
        fig.update_layout(
            title=dict(text=title, font=dict(size=title_size)),
            xaxis_title='Percentage Missing (%)',
            hovermode=hovermode,
            template=template,
            font=dict(size=font_size),
            height=height,
            width=width,
            showlegend=showlegend,
        )
    else:
        fig = go.Figure()
        fig.add_annotation(
            text='No missing data found',
            xref='paper', yref='paper',
            x=0.5, y=0.5, showarrow=False,
            font=dict(size=font_size)
        )
        fig.update_layout(
            title=dict(text=title, font=dict(size=title_size)),
            template=template,
            height=height,
            width=width,
        )
    
    return fig
