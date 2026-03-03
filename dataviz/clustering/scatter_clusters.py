"""Scatter clusters implementation - static and interactive versions."""

from typing import Optional
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from ..utils import setup_plot, apply_theme


def scatter_clusters_static(
    x: np.ndarray,
    y: np.ndarray,
    labels: np.ndarray,
    title: Optional[str] = None,
    xlabel: str = "Feature 1",
    ylabel: str = "Feature 2",
    figsize: tuple = (10, 6),
    cluster_colors: Optional[list] = None,
    marker: str = 'o',
    marker_sizes: Optional[dict] = None,
    alpha: float = 0.7,
    edgecolor: str = 'black',
    linewidth: float = 0.5,
    show_centroids: bool = False,
    centroid_marker: str = 'X',
    centroid_color: str = 'red',
    centroid_size: int = 200,
    font_size: int = 10,
    title_size: int = 14,
    label_size: int = 11,
    theme: str = 'default',
    style: str = 'default',
    dpi: int = 100,
    grid: bool = True,
    grid_alpha: float = 0.3,
    showlegend: bool = True,
    legend_loc: str = 'best',
    **kwargs
) -> plt.Axes:
    """
    Create a static 2D cluster visualization using matplotlib.

    Parameters
    ----------
    x : array
        X-coordinates
    y : array
        Y-coordinates
    labels : array
        Cluster labels
    title : str, optional
        Chart title
    xlabel : str, default "Feature 1"
        X-axis label
    ylabel : str, default "Feature 2"
        Y-axis label
    figsize : tuple, default (10, 6)
        Figure size
    cluster_colors : list, optional
        Colors per cluster
    marker : str, default 'o'
        Marker style
    alpha : float, default 0.7
        Transparency
    edgecolor : str, default 'black'
        Edge color
    linewidth : float, default 0.5
        Edge width
    show_centroids : bool, default False
        Plot centroids
    centroid_marker : str, default 'X'
        Centroid marker
    centroid_color : str, default 'red'
        Centroid color
    centroid_size : int, default 200
        Centroid size
    font_size : int, default 10
        Font size
    title_size : int, default 14
        Title font size
    label_size : int, default 11
        Label font size
    theme : str, default 'default'
        Theme
    style : str, default 'default'
        Style
    dpi : int, default 100
        DPI
    grid : bool, default True
        Grid
    grid_alpha : float, default 0.3
        Grid alpha
    showlegend : bool, default True
        Show legend
    legend_loc : str, default 'best'
        Legend location
    **kwargs
        Additional arguments

    Returns
    -------
    matplotlib.axes.Axes
        The plot axes
    """
    if title is None:
        title = "Cluster Visualization"
    
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel=xlabel, ylabel=ylabel, figsize=figsize)
        fig.set_dpi(dpi)
        
        unique_labels = np.unique(labels)
        
        if cluster_colors is None:
            cluster_colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))
        
        for idx, label in enumerate(unique_labels):
            mask = labels == label
            color = cluster_colors[idx % len(cluster_colors)]
            size = marker_sizes.get(label, 50) if marker_sizes else 50
            
            ax.scatter(x[mask], y[mask], label=f'Cluster {label}', 
                      color=color, marker=marker, s=size, alpha=alpha,
                      edgecolors=edgecolor, linewidth=linewidth, **kwargs)
        
        if show_centroids:
            centroids_x = [x[labels == label].mean() for label in unique_labels]
            centroids_y = [y[labels == label].mean() for label in unique_labels]
            ax.scatter(centroids_x, centroids_y, marker=centroid_marker, 
                      s=centroid_size, color=centroid_color, edgecolors='black', linewidth=1.5)
        
        if showlegend:
            ax.legend(loc=legend_loc, fontsize=font_size)
        
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


def scatter_clusters_interactive(
    x: np.ndarray,
    y: np.ndarray,
    labels: np.ndarray,
    title: Optional[str] = None,
    xlabel: str = "Feature 1",
    ylabel: str = "Feature 2",
    height: int = 600,
    width: int = 900,
    cluster_colors: Optional[list] = None,
    marker_color: Optional[str] = None,
    marker_size: int = 8,
    marker_symbol: str = 'circle',
    opacity: float = 0.7,
    line_width: int = 1,
    show_centroids: bool = False,
    centroid_marker: str = 'x',
    centroid_size: int = 12,
    font_size: int = 12,
    title_size: int = 16,
    label_size: int = 12,
    hovermode: str = 'closest',
    showlegend: bool = True,
    template: str = 'plotly',
    dpi: int = 100,
    **kwargs
) -> go.Figure:
    """
    Create an interactive 2D cluster visualization using plotly.

    Parameters
    ----------
    x : array
        X-coordinates
    y : array
        Y-coordinates
    labels : array
        Cluster labels
    title : str, optional
        Chart title
    xlabel : str, default "Feature 1"
        X-axis label
    ylabel : str, default "Feature 2"
        Y-axis label
    height : int, default 600
        Figure height
    width : int, default 900
        Figure width
    cluster_colors : list, optional
        Colors per cluster
    marker_color : str, optional
        Override color
    marker_size : int, default 8
        Marker size
    marker_symbol : str, default 'circle'
        Marker symbol
    opacity : float, default 0.7
        Opacity
    line_width : int, default 1
        Line width
    show_centroids : bool, default False
        Plot centroids
    centroid_marker : str, default 'x'
        Centroid marker
    centroid_size : int, default 12
        Centroid size
    font_size : int, default 12
        Font size
    title_size : int, default 16
        Title size
    label_size : int, default 12
        Label size
    hovermode : str, default 'closest'
        Hover mode
    showlegend : bool, default True
        Show legend
    template : str, default 'plotly'
        Template
    dpi : int, default 100
        DPI
    **kwargs
        Additional arguments

    Returns
    -------
    plotly.graph_objects.Figure
        The interactive figure
    """
    if title is None:
        title = "Cluster Visualization"
    
    unique_labels = np.unique(labels)
    
    fig = go.Figure()
    
    if cluster_colors is None:
        cluster_colors = px.colors.qualitative.Plotly
    
    for idx, label in enumerate(unique_labels):
        mask = labels == label
        color = marker_color or cluster_colors[idx % len(cluster_colors)]
        
        fig.add_trace(go.Scatter(
            x=x[mask],
            y=y[mask],
            mode='markers',
            name=f'Cluster {label}',
            marker=dict(
                color=color,
                size=marker_size,
                symbol=marker_symbol,
                line=dict(width=line_width),
                opacity=opacity
            ),
            **kwargs
        ))
    
    if show_centroids:
        centroids_x = [x[labels == label].mean() for label in unique_labels]
        centroids_y = [y[labels == label].mean() for label in unique_labels]
        fig.add_trace(go.Scatter(
            x=centroids_x,
            y=centroids_y,
            mode='markers',
            name='Centroids',
            marker=dict(size=centroid_size, symbol=centroid_marker, color='red')
        ))
    
    fig.update_layout(
        title=dict(text=title, font=dict(size=title_size)),
        xaxis_title=xlabel,
        yaxis_title=ylabel,
        height=height,
        width=width,
        hovermode=hovermode,
        showlegend=showlegend,
        template=template,
        font=dict(size=font_size)
    )
    
    return fig
