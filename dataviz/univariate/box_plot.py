"""Box plot implementation - static and interactive versions."""

from typing import Optional, Tuple
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from ..utils import setup_plot, apply_theme


def box_plot_static(
    data: pd.DataFrame,
    title: Optional[str] = None,
    ylabel: Optional[str] = None,
    figsize: Tuple[int, int] = (10, 6),
    color: Optional[str] = None,
    patch_artist: bool = True,
    notch: bool = False,
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = 'default',
    font_size: int = 10,
    title_size: int = 14,
    label_size: int = 11,
    dpi: int = 100,
    style: str = 'default',
    widths: float = 0.6,
    **kwargs
) -> plt.Axes:
    """
    Create a static box plot using matplotlib.

    Parameters
    ----------
    data : DataFrame or array-like
        Data to visualize
    title : str, optional
        Chart title
    ylabel : str, optional
        Y-axis label
    figsize : tuple, default (10, 6)
        Figure size (width, height)
    color : str, optional
        Box color
    patch_artist : bool, default True
        Use patch artist for boxes
    notch : bool, default False
        Show notches
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
    widths : float, default 0.6
        Box width
    **kwargs
        Additional boxplot arguments

    Returns
    -------
    matplotlib.axes.Axes
        The plot axes
    """
    if title is None:
        title = "Box Plot"
    if ylabel is None:
        ylabel = 'Value'
    
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, ylabel=ylabel, figsize=figsize)
        fig.set_dpi(dpi)
        
        bp = ax.boxplot(data, patch_artist=patch_artist, notch=notch, widths=widths, **kwargs)
        
        # Color boxes
        if color and patch_artist:
            for box in bp['boxes']:
                box.set_facecolor(color)
        
        # Customize fonts
        ax.title.set_fontsize(title_size)
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


def box_plot_interactive(
    data: pd.DataFrame,
    title: Optional[str] = None,
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
    boxmean: bool = True,
    points: str = 'outliers',
    **kwargs
) -> go.Figure:
    """
    Create an interactive box plot using plotly.

    Parameters
    ----------
    data : DataFrame or Series
        Data to visualize
    title : str, optional
        Chart title
    ylabel : str, optional
        Y-axis label
    color : str, optional
        Box color (color name or hex)
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
    boxmean : bool, default True
        Show mean line
    points : str, default 'outliers'
        Show points: 'all', 'outliers', 'suspectedoutliers', False
    **kwargs
        Additional plot arguments

    Returns
    -------
    plotly.graph_objects.Figure
        The interactive figure
    """
    if title is None:
        title = "Box Plot"
    if ylabel is None:
        ylabel = 'Value'
    if color is None:
        color = marker_color
    
    fig = go.Figure()
    
    if isinstance(data, pd.DataFrame):
        for col in data.columns:
            fig.add_trace(go.Box(
                y=data[col],
                name=str(col),
                marker_color=color,
                boxmean=boxmean,
                points=points,
                **kwargs
            ))
    else:
        fig.add_trace(go.Box(
            y=data,
            marker_color=color,
            boxmean=boxmean,
            points=points,
            **kwargs
        ))
    
    fig.update_layout(
        title=dict(text=title, font=dict(size=title_size)),
        yaxis_title=ylabel,
        hovermode=hovermode,
        template=template,
        font=dict(size=font_size),
        height=height,
        width=width,
        showlegend=showlegend,
    )
    
    return fig
