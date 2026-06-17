"""Scatter clusters implementation - static and interactive versions."""

from typing import Optional
from ..types import ArrayLike, FigureSize, Labels, MatplotlibAxes, PlotlyFigure
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from ..utils import setup_plot, apply_theme


def scatter_clusters_static(
    x: ArrayLike,
    y: ArrayLike,
    labels: ArrayLike,
    title: Optional[str] = None,
    xlabel: str = "Feature 1",
    ylabel: str = "Feature 2",
    figsize: FigureSize = (10, 6),
    cluster_colors: Optional[Labels] = None,
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
) -> MatplotlibAxes:
    """Create a static cluster-labeled scatter plot.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        x (ArrayLike): Values plotted along the x-axis.
        y (ArrayLike): Values plotted along the y-axis.
        labels (ArrayLike): Class, feature, sample, or cluster labels shown on the chart.
        title (Optional[str]): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``None``.
        xlabel (str): Optional x-axis label. Defaults to ``'Feature 1'``.
        ylabel (str): Optional y-axis label. Defaults to ``'Feature 2'``.
        figsize (FigureSize): Matplotlib figure size as ``(width, height)`` in inches. Defaults to ``(10, 6)``.
        cluster_colors (Optional[Labels]): Optional colors used to draw cluster groups. Defaults to ``None``.
        marker (str): Configuration value for ``marker``. Defaults to ``'o'``.
        marker_sizes (Optional[dict]): Configuration value for ``marker_sizes``. Defaults to ``None``.
        alpha (float): Configuration value for ``alpha``. Defaults to ``0.7``.
        edgecolor (str): Configuration value for ``edgecolor``. Defaults to ``'black'``.
        linewidth (float): Configuration value for ``linewidth``. Defaults to ``0.5``.
        show_centroids (bool): Configuration value for ``show_centroids``. Defaults to ``False``.
        centroid_marker (str): Configuration value for ``centroid_marker``. Defaults to ``'X'``.
        centroid_color (str): Configuration value for ``centroid_color``. Defaults to ``'red'``.
        centroid_size (int): Configuration value for ``centroid_size``. Defaults to ``200``.
        font_size (int): Configuration value for ``font_size``. Defaults to ``10``.
        title_size (int): Configuration value for ``title_size``. Defaults to ``14``.
        label_size (int): Configuration value for ``label_size``. Defaults to ``11``.
        theme (str): Named styling theme applied after the base plot is created. Defaults to ``'default'``.
        style (str): Matplotlib style context used while building the figure. Defaults to ``'default'``.
        dpi (int): Configuration value for ``dpi``. Defaults to ``100``.
        grid (bool): Configuration value for ``grid``. Defaults to ``True``.
        grid_alpha (float): Configuration value for ``grid_alpha``. Defaults to ``0.3``.
        showlegend (bool): Configuration value for ``showlegend``. Defaults to ``True``.
        legend_loc (str): Configuration value for ``legend_loc``. Defaults to ``'best'``.
        **kwargs (Any): Additional keyword arguments forwarded to the underlying plotting function.
    
    Returns:
        matplotlib.axes.Axes: Configured matplotlib axes containing the rendered static chart.
    
    Raises:
        TypeError: If required inputs are not compatible with the plotting backend.
        ValueError: If input lengths, matrix shapes, or option values are invalid for the requested chart.
    
    Example:
        ```python
        import dataviz as dv
        result = dv.scatter_clusters_static(x, y)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
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
    x: ArrayLike,
    y: ArrayLike,
    labels: ArrayLike,
    title: Optional[str] = None,
    xlabel: str = "Feature 1",
    ylabel: str = "Feature 2",
    height: int = 600,
    width: int = 900,
    cluster_colors: Optional[Labels] = None,
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
) -> PlotlyFigure:
    """Create an interactive cluster-labeled scatter plot.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        x (ArrayLike): Values plotted along the x-axis.
        y (ArrayLike): Values plotted along the y-axis.
        labels (ArrayLike): Class, feature, sample, or cluster labels shown on the chart.
        title (Optional[str]): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``None``.
        xlabel (str): Optional x-axis label. Defaults to ``'Feature 1'``.
        ylabel (str): Optional y-axis label. Defaults to ``'Feature 2'``.
        height (int): Plotly figure height in pixels. Defaults to ``600``.
        width (int): Plotly figure width in pixels. Defaults to ``900``.
        cluster_colors (Optional[Labels]): Optional colors used to draw cluster groups. Defaults to ``None``.
        marker_color (Optional[str]): Configuration value for ``marker_color``. Defaults to ``None``.
        marker_size (int): Configuration value for ``marker_size``. Defaults to ``8``.
        marker_symbol (str): Configuration value for ``marker_symbol``. Defaults to ``'circle'``.
        opacity (float): Configuration value for ``opacity``. Defaults to ``0.7``.
        line_width (int): Configuration value for ``line_width``. Defaults to ``1``.
        show_centroids (bool): Configuration value for ``show_centroids``. Defaults to ``False``.
        centroid_marker (str): Configuration value for ``centroid_marker``. Defaults to ``'x'``.
        centroid_size (int): Configuration value for ``centroid_size``. Defaults to ``12``.
        font_size (int): Configuration value for ``font_size``. Defaults to ``12``.
        title_size (int): Configuration value for ``title_size``. Defaults to ``16``.
        label_size (int): Configuration value for ``label_size``. Defaults to ``12``.
        hovermode (str): Configuration value for ``hovermode``. Defaults to ``'closest'``.
        showlegend (bool): Configuration value for ``showlegend``. Defaults to ``True``.
        template (str): Plotly template used to style the interactive figure. Defaults to ``'plotly'``.
        dpi (int): Configuration value for ``dpi``. Defaults to ``100``.
        **kwargs (Any): Additional keyword arguments forwarded to the underlying plotting function.
    
    Returns:
        plotly.graph_objects.Figure: Configured Plotly figure containing the rendered interactive chart.
    
    Raises:
        TypeError: If required inputs are not compatible with the plotting backend.
        ValueError: If input lengths, matrix shapes, or option values are invalid for the requested chart.
    
    Example:
        ```python
        import dataviz as dv
        result = dv.scatter_clusters_interactive(x, y)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
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
