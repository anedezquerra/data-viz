"""Violin plot implementation - static and interactive versions."""

from typing import Optional, Tuple
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
from ..utils import setup_plot, apply_theme


def violin_plot_static(
    data: pd.DataFrame,
    x: Optional[str] = None,
    y: Optional[str] = None,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    figsize: Tuple[int, int] = (10, 6),
    color: Optional[str] = None,
    palette: Optional[str] = None,
    inner: str = 'box',
    cut: float = 0.0,
    alpha: float = 0.7,
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = 'default',
    font_size: int = 10,
    title_size: int = 14,
    label_size: int = 11,
    dpi: int = 100,
    style: str = 'default',
    linewidth: float = 1.5,
    **kwargs
) -> plt.Axes:
    """
    Create a static violin plot using seaborn.

    Parameters
    ----------
    data : DataFrame
        Data to visualize
    x : str, optional
        Column for x-axis
    y : str, optional
        Column for y-axis
    title : str, optional
        Chart title
    xlabel : str, optional
        X-axis label
    ylabel : str, optional
        Y-axis label
    figsize : tuple, default (10, 6)
        Figure size (width, height)
    color : str, optional
        Single color for all violins
    palette : str, optional
        Color palette
    inner : str, default 'box'
        Inner plot: 'box', 'quartile', 'point', 'stick', None
    cut : float, default 0.0
        Extend range of density estimate
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
    linewidth : float, default 1.5
        Line width
    **kwargs
        Additional seaborn violin_plot arguments

    Returns
    -------
    matplotlib.axes.Axes
        The plot axes
    """
    if title is None:
        title = "Violin Plot"
    
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel=xlabel, ylabel=ylabel, figsize=figsize)
        fig.set_dpi(dpi)
        
        ax = sns.violinplot(
            data=data,
            x=x,
            y=y,
            color=color,
            palette=palette,
            inner=inner,
            cut=cut,
            alpha=alpha,
            linewidth=linewidth,
            ax=ax,
            **kwargs
        )
        
        # Customize fonts
        ax.title.set_fontsize(title_size)
        if xlabel:
            ax.xaxis.label.set_fontsize(label_size)
        if ylabel:
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


def violin_plot_interactive(
    data: pd.DataFrame,
    x: Optional[str] = None,
    y: Optional[str] = None,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    color: Optional[str] = None,
    marker_color: Optional[str] = None,
    showlegend: bool = True,
    hovermode: str = 'closest',
    template: str = 'plotly',
    font_size: int = 12,
    title_size: int = 16,
    height: int = 600,
    width: int = 1000,
    meanline: bool = True,
    points: bool = False,
    **kwargs
) -> go.Figure:
    """
    Create an interactive violin plot using plotly.

    Parameters
    ----------
    data : DataFrame
        Data to visualize
    x : str, optional
        Column for x-axis
    y : str, optional
        Column for y-axis
    title : str, optional
        Chart title
    xlabel : str, optional
        X-axis label
    ylabel : str, optional
        Y-axis label
    color : str, optional
        Violin color
    marker_color : str, optional
        Marker color (alternative)
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
    meanline : bool, default True
        Show mean line
    points : bool, default False
        Show individual points
    **kwargs
        Additional plot arguments

    Returns
    -------
    plotly.graph_objects.Figure
        The interactive figure
    """
    if title is None:
        title = "Violin Plot"
    if color is None:
        color = marker_color
    
    fig = go.Figure()
    
    if x and isinstance(data, pd.DataFrame):
        groups = data[x].unique()
        for group in groups:
            group_data = data[data[x] == group][y] if y else data[data[x] == group]
            fig.add_trace(go.Violin(
                y=group_data,
                name=str(group),
                marker_color=color,
                meanline_visible=meanline,
                points='all' if points else False,
                **kwargs
            ))
    else:
        fig.add_trace(go.Violin(
            y=data,
            marker_color=color,
            meanline_visible=meanline,
            points='all' if points else False,
            **kwargs
        ))
    
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
