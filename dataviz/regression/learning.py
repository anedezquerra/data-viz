"""Learning curve implementation - static and interactive versions."""

from typing import Optional, Tuple
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from ..utils import setup_plot, apply_theme


def learning_curve_static(
    train_sizes: np.ndarray,
    train_scores: np.ndarray,
    val_scores: np.ndarray,
    title: Optional[str] = None,
    figsize: Tuple[int, int] = (10, 6),
    train_color: Optional[str] = None,
    val_color: Optional[str] = None,
    linewidth: float = 2.0,
    marker_size: int = 6,
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
    Create a static learning curve using matplotlib.

    Parameters
    ----------
    train_sizes : array
        Training set sizes
    train_scores : array
        Training scores
    val_scores : array
        Validation scores
    title : str, optional
        Chart title
    figsize : tuple, default (10, 6)
        Figure size (width, height)
    train_color : str, optional
        Training line color
    val_color : str, optional
        Validation line color
    linewidth : float, default 2.0
        Line width
    marker_size : int, default 6
        Marker size
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
        title = "Learning Curve"
    
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel='Training Set Size', ylabel='Score', figsize=figsize)
        fig.set_dpi(dpi)
        
        ax.plot(
            train_sizes, train_scores,
            'o-',
            label='Training Score',
            color=train_color,
            linewidth=linewidth,
            markersize=marker_size,
            alpha=alpha,
            **kwargs
        )
        ax.plot(
            train_sizes, val_scores,
            'o-',
            label='Validation Score',
            color=val_color,
            linewidth=linewidth,
            markersize=marker_size,
            alpha=alpha,
            **kwargs
        )
        
        # Customize fonts
        ax.title.set_fontsize(title_size)
        ax.xaxis.label.set_fontsize(label_size)
        ax.yaxis.label.set_fontsize(label_size)
        ax.tick_params(labelsize=font_size)
        
        if grid:
            ax.grid(True, alpha=grid_alpha)
        
        ax.legend(fontsize=font_size)
        
        # Theme
        if theme == 'dark':
            ax.set_facecolor('#f0f0f0')
        elif theme == 'minimal':
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
        
        apply_theme(ax, theme)
    
    return ax


def learning_curve_interactive(
    train_sizes: np.ndarray,
    train_scores: np.ndarray,
    val_scores: np.ndarray,
    title: Optional[str] = None,
    train_color: Optional[str] = None,
    val_color: Optional[str] = None,
    linewidth: float = 2.0,
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
    Create an interactive learning curve using plotly.

    Parameters
    ----------
    train_sizes : array
        Training set sizes
    train_scores : array
        Training scores
    val_scores : array
        Validation scores
    title : str, optional
        Chart title
    train_color : str, optional
        Training line color
    val_color : str, optional
        Validation line color
    linewidth : float, default 2.0
        Line width
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
        title = "Learning Curve"
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=train_sizes,
        y=train_scores,
        mode='lines+markers',
        name='Training Score',
        line=dict(color=train_color, width=linewidth),
        marker=dict(size=marker_size),
        **kwargs
    ))
    
    fig.add_trace(go.Scatter(
        x=train_sizes,
        y=val_scores,
        mode='lines+markers',
        name='Validation Score',
        line=dict(color=val_color, width=linewidth),
        marker=dict(size=marker_size),
        **kwargs
    ))
    
    fig.update_layout(
        title=dict(text=title, font=dict(size=title_size)),
        xaxis_title='Training Set Size',
        yaxis_title='Score',
        hovermode=hovermode,
        template=template,
        font=dict(size=font_size),
        height=height,
        width=width,
        showlegend=showlegend,
    )
    
    return fig
