"""Elbow plot implementation - static and interactive versions."""

from typing import Optional
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from ..utils import setup_plot, apply_theme


def elbow_plot_static(
    n_clusters: np.ndarray,
    inertias: np.ndarray,
    title: Optional[str] = None,
    xlabel: str = "Number of Clusters",
    ylabel: str = "Inertia",
    figsize: tuple = (10, 6),
    color: str = 'blue',
    marker: str = 'o',
    marker_size: int = 50,
    linestyle: str = '-',
    linewidth: float = 2.0,
    marker_edgecolor: str = 'black',
    marker_edgewidth: float = 1.0,
    alpha: float = 0.7,
    elbow_idx: Optional[int] = None,
    elbow_marker: str = 'X',
    elbow_color: str = 'red',
    elbow_size: int = 200,
    font_size: int = 10,
    title_size: int = 14,
    label_size: int = 11,
    theme: str = 'default',
    style: str = 'default',
    dpi: int = 100,
    grid: bool = True,
    grid_alpha: float = 0.3,
    **kwargs
) -> plt.Axes:
    """
    Create a static elbow plot using matplotlib.

    Parameters
    ----------
    n_clusters : array
        Number of clusters
    inertias : array
        Inertia values for each cluster count
    title : str, optional
        Chart title (auto-generated if None)
    xlabel : str, default "Number of Clusters"
        X-axis label
    ylabel : str, default "Inertia"
        Y-axis label
    figsize : tuple, default (10, 6)
        Figure size
    color : str, default 'blue'
        Line color
    marker : str, default 'o'
        Marker style
    marker_size : int, default 50
        Marker size
    linestyle : str, default '-'
        Line style
    linewidth : float, default 2.0
        Line width
    marker_edgecolor : str, default 'black'
        Marker edge color
    marker_edgewidth : float, default 1.0
        Marker edge width
    alpha : float, default 0.7
        Line transparency
    elbow_idx : int, optional
        Index of elbow point to highlight
    elbow_marker : str, default 'X'
        Elbow marker style
    elbow_color : str, default 'red'
        Elbow highlight color
    elbow_size : int, default 200
        Elbow marker size
    font_size : int, default 10
        Base font size
    title_size : int, default 14
        Title font size
    label_size : int, default 11
        Axis label font size
    theme : str, default 'default'
        Plot theme
    style : str, default 'default'
        Matplotlib style
    dpi : int, default 100
        Figure DPI
    grid : bool, default True
        Show grid
    grid_alpha : float, default 0.3
        Grid transparency
    **kwargs
        Additional plot arguments

    Returns
    -------
    matplotlib.axes.Axes
        The plot axes
    """
    if title is None:
        title = "Elbow Plot"
    
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel=xlabel, ylabel=ylabel, figsize=figsize)
        fig.set_dpi(dpi)
        
        ax.plot(n_clusters, inertias, marker=marker, markersize=marker_size,
               linestyle=linestyle, linewidth=linewidth, color=color, alpha=alpha,
               markeredgecolor=marker_edgecolor, markeredgewidth=marker_edgewidth, **kwargs)
        
        if elbow_idx is not None:
            ax.scatter(n_clusters[elbow_idx], inertias[elbow_idx], 
                      marker=elbow_marker, s=elbow_size, color=elbow_color,
                      edgecolors='black', linewidth=1.5, zorder=5)
        
        ax.set_xlabel(xlabel, fontsize=label_size)
        ax.set_ylabel(ylabel, fontsize=label_size)
        ax.title.set_fontsize(title_size)
        ax.tick_params(labelsize=font_size)
        
        if grid:
            ax.grid(True, alpha=grid_alpha)
        
        if theme == 'dark':
            ax.set_facecolor('#f0f0f0')
        elif theme == 'minimal':
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
        
        apply_theme(ax, theme)
    
    return ax


def elbow_plot_interactive(
    n_clusters: np.ndarray,
    inertias: np.ndarray,
    title: Optional[str] = None,
    xlabel: str = "Number of Clusters",
    ylabel: str = "Inertia",
    height: int = 600,
    width: int = 900,
    line_color: str = 'blue',
    line_width: int = 2,
    marker_size: int = 8,
    marker_symbol: str = 'circle',
    marker_color: Optional[str] = None,
    opacity: float = 0.7,
    elbow_idx: Optional[int] = None,
    elbow_marker: str = 'x-open-dot',
    elbow_color: str = 'red',
    font_size: int = 12,
    title_size: int = 16,
    label_size: int = 12,
    hovermode: str = 'closest',
    showlegend: bool = False,
    template: str = 'plotly',
    **kwargs
) -> go.Figure:
    """
    Create an interactive elbow plot using plotly.

    Parameters
    ----------
    n_clusters : array
        Number of clusters
    inertias : array
        Inertia values for each cluster count
    title : str, optional
        Chart title (auto-generated if None)
    xlabel : str, default "Number of Clusters"
        X-axis label
    ylabel : str, default "Inertia"
        Y-axis label
    height : int, default 600
        Figure height
    width : int, default 900
        Figure width
    line_color : str, default 'blue'
        Line color
    line_width : int, default 2
        Line width
    marker_size : int, default 8
        Marker size
    marker_symbol : str, default 'circle'
        Marker symbol
    marker_color : str, optional
        Marker color (defaults to line color)
    opacity : float, default 0.7
        Line/marker opacity
    elbow_idx : int, optional
        Index of elbow point to highlight
    elbow_marker : str, default 'x-open-dot'
        Elbow marker symbol
    elbow_color : str, default 'red'
        Elbow highlight color
    font_size : int, default 12
        Base font size
    title_size : int, default 16
        Title font size
    label_size : int, default 12
        Axis label font size
    hovermode : str, default 'closest'
        Hover mode
    showlegend : bool, default False
        Show legend
    template : str, default 'plotly'
        Plotly template
    **kwargs
        Additional plot arguments

    Returns
    -------
    plotly.graph_objects.Figure
        The interactive figure
    """
    if title is None:
        title = "Elbow Plot"
    
    if marker_color is None:
        marker_color = line_color
    
    fig = go.Figure(data=[
        go.Scatter(
            x=n_clusters,
            y=inertias,
            mode='lines+markers',
            line=dict(color=line_color, width=line_width),
            marker=dict(size=marker_size, symbol=marker_symbol, color=marker_color),
            opacity=opacity,
            **kwargs
        )
    ])
    
    if elbow_idx is not None:
        fig.add_trace(go.Scatter(
            x=[n_clusters[elbow_idx]],
            y=[inertias[elbow_idx]],
            mode='markers',
            marker=dict(size=15, symbol=elbow_marker, color=elbow_color),
            name='Elbow Point',
            showlegend=True
        ))
    
    fig.update_layout(
        title=dict(text=title, font=dict(size=title_size)),
        xaxis_title=xlabel,
        yaxis_title=ylabel,
        xaxis=dict(title_font=dict(size=label_size)),
        yaxis=dict(title_font=dict(size=label_size)),
        height=height,
        width=width,
        hovermode=hovermode,
        showlegend=showlegend,
        template=template,
        font=dict(size=font_size)
    )
    
    return fig


# Default to static version
elbow_plot = elbow_plot_static
