"""Residual plot implementation - static and interactive versions."""

from typing import Optional, Tuple
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from ..utils import setup_plot, apply_theme


def residual_plot_static(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    title: Optional[str] = None,
    figsize: Tuple[int, int] = (10, 6),
    color: Optional[str] = None,
    edgecolor: str = 'black',
    linewidth: float = 1.0,
    marker_size: int = 50,
    alpha: float = 0.6,
    line_color: str = 'red',
    line_style: str = '--',
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
    Create a static residual plot using matplotlib.

    Parameters
    ----------
    y_true : array
        Actual target values
    y_pred : array
        Predicted values
    title : str, optional
        Chart title
    figsize : tuple, default (10, 6)
        Figure size (width, height)
    color : str, optional
        Marker color
    edgecolor : str, default 'black'
        Marker edge color
    linewidth : float, default 1.0
        Edge line width
    marker_size : int, default 50
        Marker size
    alpha : float, default 0.6
        Transparency
    line_color : str, default 'red'
        Reference line color
    line_style : str, default '--'
        Reference line style
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
        title = "Residual Plot"
    
    residuals = y_true - y_pred
    
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel='Predicted Values', ylabel='Residuals', figsize=figsize)
        fig.set_dpi(dpi)
        
        ax.scatter(
            y_pred, residuals,
            color=color,
            edgecolors=edgecolor,
            linewidth=linewidth,
            s=marker_size,
            alpha=alpha,
            **kwargs
        )
        ax.axhline(y=0, color=line_color, linestyle=line_style, linewidth=2)
        
        # Customize fonts
        ax.title.set_fontsize(title_size)
        ax.xaxis.label.set_fontsize(label_size)
        ax.yaxis.label.set_fontsize(label_size)
        ax.tick_params(labelsize=font_size)
        
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


def residual_plot_interactive(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    title: Optional[str] = None,
    color: Optional[str] = None,
    marker_color: Optional[str] = None,
    marker_size: int = 8,
    line_color: str = 'red',
    line_dash: str = 'dash',
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
    Create an interactive residual plot using plotly.

    Parameters
    ----------
    y_true : array
        Actual target values
    y_pred : array
        Predicted values
    title : str, optional
        Chart title
    color : str, optional
        Marker color
    marker_color : str, optional
        Alternative marker color parameter
    marker_size : int, default 8
        Marker size
    line_color : str, default 'red'
        Reference line color
    line_dash : str, default 'dash'
        Reference line style
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
        title = "Residual Plot"
    if color is None:
        color = marker_color
    
    residuals = y_true - y_pred
    
    fig = go.Figure(data=[
        go.Scatter(
            x=y_pred,
            y=residuals,
            mode='markers',
            marker=dict(size=marker_size, color=color),
            **kwargs
        )
    ])
    
    # Add reference line at y=0
    fig.add_hline(y=0, line_dash=line_dash, line_color=line_color)
    
    fig.update_layout(
        title=dict(text=title, font=dict(size=title_size)),
        xaxis_title='Predicted Values',
        yaxis_title='Residuals',
        hovermode=hovermode,
        template=template,
        font=dict(size=font_size),
        height=height,
        width=width,
        showlegend=showlegend,
    )
    
    return fig
