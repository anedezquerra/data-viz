"""ROC curve implementation - static and interactive versions."""

from typing import Optional, Tuple
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from ..utils import setup_plot, apply_theme


def roc_curve_static(
    fpr: np.ndarray,
    tpr: np.ndarray,
    auc: Optional[float] = None,
    title: Optional[str] = None,
    figsize: Tuple[int, int] = (10, 6),
    color: Optional[str] = None,
    linewidth: float = 2.0,
    linestyle: str = '-',
    reference_color: str = 'black',
    reference_linestyle: str = '--',
    reference_linewidth: float = 1.5,
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
    Create a static ROC curve using matplotlib.

    Parameters
    ----------
    fpr : array
        False positive rates
    tpr : array
        True positive rates
    auc : float, optional
        Area under curve value
    title : str, optional
        Chart title
    figsize : tuple, default (10, 6)
        Figure size (width, height)
    color : str, optional
        ROC curve color
    linewidth : float, default 2.0
        ROC curve line width
    linestyle : str, default '-'
        ROC curve line style
    reference_color : str, default 'black'
        Reference line color
    reference_linestyle : str, default '--'
        Reference line style
    reference_linewidth : float, default 1.5
        Reference line width
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
        title = "ROC Curve"
    
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel='False Positive Rate', ylabel='True Positive Rate', figsize=figsize)
        fig.set_dpi(dpi)
        
        label = 'ROC Curve'
        if auc is not None:
            label += f' (AUC = {auc:.3f})'
        
        ax.plot(fpr, tpr, color=color, linewidth=linewidth, linestyle=linestyle, label=label, **kwargs)
        ax.plot([0, 1], [0, 1], color=reference_color, linestyle=reference_linestyle, linewidth=reference_linewidth, label='Random Classifier')
        
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


def roc_curve_interactive(
    fpr: np.ndarray,
    tpr: np.ndarray,
    auc: Optional[float] = None,
    title: Optional[str] = None,
    color: Optional[str] = None,
    marker_color: Optional[str] = None,
    linewidth: float = 2.0,
    reference_color: str = 'black',
    reference_linestyle: str = 'dash',
    reference_linewidth: float = 1.5,
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
    Create an interactive ROC curve using plotly.

    Parameters
    ----------
    fpr : array
        False positive rates
    tpr : array
        True positive rates
    auc : float, optional
        Area under curve value
    title : str, optional
        Chart title
    color : str, optional
        ROC curve color
    marker_color : str, optional
        Alternative color parameter
    linewidth : float, default 2.0
        Line width
    reference_color : str, default 'black'
        Reference line color
    reference_linestyle : str, default 'dash'
        Reference line style
    reference_linewidth : float, default 1.5
        Reference line width
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
        title = "ROC Curve"
    if color is None:
        color = marker_color
    
    fig = go.Figure()
    
    label = 'ROC Curve'
    if auc is not None:
        label += f' (AUC = {auc:.3f})'
    
    fig.add_trace(go.Scatter(
        x=fpr,
        y=tpr,
        mode='lines',
        name=label,
        line=dict(color=color, width=linewidth),
        **kwargs
    ))
    
    # Random classifier line
    fig.add_trace(go.Scatter(
        x=[0, 1],
        y=[0, 1],
        mode='lines',
        name='Random Classifier',
        line=dict(dash=reference_linestyle, color=reference_color, width=reference_linewidth)
    ))
    
    fig.update_layout(
        title=dict(text=title, font=dict(size=title_size)),
        xaxis_title='False Positive Rate',
        yaxis_title='True Positive Rate',
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
