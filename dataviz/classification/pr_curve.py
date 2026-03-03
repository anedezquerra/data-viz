"""Precision-Recall curve implementation - static and interactive versions."""

from typing import Optional, Tuple
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from ..utils import setup_plot, apply_theme


def precision_recall_curve_static(
    precision: np.ndarray,
    recall: np.ndarray,
    ap: Optional[float] = None,
    title: Optional[str] = None,
    figsize: Tuple[int, int] = (10, 6),
    color: Optional[str] = None,
    linewidth: float = 2.0,
    linestyle: str = '-',
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
    Create a static Precision-Recall curve using matplotlib.

    Parameters
    ----------
    precision : array
        Precision values
    recall : array
        Recall values
    ap : float, optional
        Average precision value
    title : str, optional
        Chart title
    figsize : tuple, default (10, 6)
        Figure size (width, height)
    color : str, optional
        Curve color
    linewidth : float, default 2.0
        Line width
    linestyle : str, default '-'
        Line style
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
        title = "Precision-Recall Curve"
    
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel='Recall', ylabel='Precision', figsize=figsize)
        fig.set_dpi(dpi)
        
        label = 'Precision-Recall'
        if ap is not None:
            label += f' (AP = {ap:.3f})'
        
        ax.plot(recall, precision, color=color, linewidth=linewidth, linestyle=linestyle, label=label, **kwargs)
        
        ax.set_xlim([0.0, 1.0])
        ax.set_ylim([0.0, 1.05])
        
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


def precision_recall_curve_interactive(
    precision: np.ndarray,
    recall: np.ndarray,
    ap: Optional[float] = None,
    title: Optional[str] = None,
    color: Optional[str] = None,
    marker_color: Optional[str] = None,
    linewidth: float = 2.0,
    showlegend: bool = True,
    hovermode: str = 'closest',
    template: str = 'plotly',
    font_size: int = 12,
    title_size: int = 16,
    height: int = 600,
    width: int = 700,
    **kwargs
) -> go.Figure:
    """
    Create an interactive Precision-Recall curve using plotly.

    Parameters
    ----------
    precision : array
        Precision values
    recall : array
        Recall values
    ap : float, optional
        Average precision value
    title : str, optional
        Chart title
    color : str, optional
        Curve color
    marker_color : str, optional
        Alternative color parameter
    linewidth : float, default 2.0
        Line width
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
    width : int, default 700
        Figure width in pixels
    **kwargs
        Additional plot arguments

    Returns
    -------
    plotly.graph_objects.Figure
        The interactive figure
    """
    if title is None:
        title = "Precision-Recall Curve"
    if color is None:
        color = marker_color
    
    label = 'Precision-Recall'
    if ap is not None:
        label += f' (AP = {ap:.3f})'
    
    fig = go.Figure(data=[
        go.Scatter(
            x=recall,
            y=precision,
            mode='lines',
            name=label,
            line=dict(color=color, width=linewidth),
            **kwargs
        )
    ])
    
    fig.update_layout(
        title=dict(text=title, font=dict(size=title_size)),
        xaxis_title='Recall',
        yaxis_title='Precision',
        xaxis=dict(range=[0, 1]),
        yaxis=dict(range=[0, 1.05]),
        hovermode=hovermode,
        template=template,
        font=dict(size=font_size),
        height=height,
        width=width,
        showlegend=showlegend,
    )
    
    return fig
