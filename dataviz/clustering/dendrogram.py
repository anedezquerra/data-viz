"""Dendrogram implementation - static and interactive versions."""

from typing import Optional
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from scipy.cluster.hierarchy import dendrogram as scipy_dendrogram
from ..utils import setup_plot, apply_theme


def dendrogram_static(
    linkage_matrix: np.ndarray,
    labels: Optional[list] = None,
    title: Optional[str] = None,
    xlabel: str = "Sample Index",
    ylabel: str = "Distance",
    figsize: tuple = (12, 6),
    color_threshold: Optional[float] = None,
    above_threshold_color: str = 'gray',
    orientation: str = 'top',
    leaf_rotation: float = 90.0,
    leaf_font_size: int = 10,
    font_size: int = 10,
    title_size: int = 14,
    label_size: int = 11,
    theme: str = 'default',
    style: str = 'default',
    dpi: int = 100,
    grid: bool = True,
    grid_alpha: float = 0.3,
    show_leaf_counts: bool = True,
    line_color: str = 'black',
    line_width: float = 1.5,
    **kwargs
) -> plt.Axes:
    """
    Create a static dendrogram using matplotlib.

    Parameters
    ----------
    linkage_matrix : array
        Linkage matrix from hierarchical clustering
    labels : list, optional
        Sample labels
    title : str, optional
        Chart title (auto-generated if None)
    xlabel : str, default "Sample Index"
        X-axis label
    ylabel : str, default "Distance"
        Y-axis label
    figsize : tuple, default (12, 6)
        Figure size
    color_threshold : float, optional
        Threshold for coloring clusters
    above_threshold_color : str, default 'gray'
        Color above threshold
    orientation : str, default 'top'
        Orientation ('top', 'bottom', 'left', 'right')
    leaf_rotation : float, default 90.0
        Leaf rotation angle
    leaf_font_size : int, default 10
        Leaf font size
    font_size : int, default 10
        Base font size
    title_size : int, default 14
        Title font size
    label_size : int, default 11
        Label font size
    theme : str, default 'default'
        Theme ('default', 'dark', 'minimal')
    style : str, default 'default'
        Matplotlib style
    dpi : int, default 100
        Figure DPI
    grid : bool, default True
        Show grid
    grid_alpha : float, default 0.3
        Grid transparency
    show_leaf_counts : bool, default True
        Show leaf counts
    line_color : str, default 'black'
        Dendrogram line color
    line_width : float, default 1.5
        Dendrogram line width
    **kwargs
        Additional plot arguments

    Returns
    -------
    matplotlib.axes.Axes
        The plot axes
    """
    if title is None:
        title = "Dendrogram"
    
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel=xlabel, ylabel=ylabel, figsize=figsize)
        fig.set_dpi(dpi)
        
        scipy_dendrogram(
            linkage_matrix,
            labels=labels,
            ax=ax,
            color_threshold=color_threshold,
            above_threshold_color=above_threshold_color,
            orientation=orientation,
            leaf_rotation=leaf_rotation,
            leaf_font_size=leaf_font_size,
            **kwargs
        )
        
        ax.set_xlabel(xlabel, fontsize=label_size)
        ax.set_ylabel(ylabel, fontsize=label_size)
        ax.title.set_fontsize(title_size)
        ax.tick_params(labelsize=font_size)
        
        # Set dendrogram line appearance
        for line in ax.get_lines():
            line.set_color(line_color)
            line.set_linewidth(line_width)
        
        if grid:
            ax.grid(True, alpha=grid_alpha)
        
        if theme == 'dark':
            ax.set_facecolor('#f0f0f0')
        elif theme == 'minimal':
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
        
        apply_theme(ax, theme)
    
    return ax


def dendrogram_interactive(
    linkage_matrix: np.ndarray,
    labels: Optional[list] = None,
    title: Optional[str] = None,
    xlabel: str = "Samples",
    ylabel: str = "Distance",
    height: int = 600,
    width: int = 900,
    line_color: str = 'black',
    line_width: int = 2,
    font_size: int = 12,
    title_size: int = 16,
    label_size: int = 12,
    hovermode: str = 'closest',
    showlegend: bool = False,
    template: str = 'plotly',
    color_threshold: Optional[float] = None,
    **kwargs
) -> go.Figure:
    """
    Create an interactive dendrogram using plotly.

    Parameters
    ----------
    linkage_matrix : array
        Linkage matrix from hierarchical clustering
    labels : list, optional
        Sample labels
    title : str, optional
        Chart title (auto-generated if None)
    xlabel : str, default "Samples"
        X-axis label
    ylabel : str, default "Distance"
        Y-axis label
    height : int, default 600
        Figure height
    width : int, default 900
        Figure width
    line_color : str, default 'black'
        Dendrogram line color
    line_width : int, default 2
        Dendrogram line width
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
    color_threshold : float, optional
        Threshold for coloring
    **kwargs
        Additional plot arguments

    Returns
    -------
    plotly.graph_objects.Figure
        The interactive figure
    """
    if title is None:
        title = "Dendrogram"
    
    from scipy.cluster.hierarchy import dendrogram as scipy_dendrogram
    
    # Create the dendrogram plot data
    dendro = scipy_dendrogram(linkage_matrix, labels=labels, no_plot=True)
    
    # Extract dendrogram data
    icoord = np.array(dendro['icoord'])
    dcoord = np.array(dendro['dcoord'])
    
    fig = go.Figure()
    
    # Plot dendrogram lines
    for i in range(len(icoord)):
        fig.add_trace(go.Scatter(
            x=icoord[i],
            y=dcoord[i],
            mode='lines',
            line=dict(color=line_color, width=line_width),
            hoverinfo='skip',
            showlegend=False
        ))
    
    # Add labels if provided
    if labels is not None:
        x_labels = []
        for label in dendro['ivl']:
            if label.isdigit():
                x_labels.append(labels[int(label)] if int(label) < len(labels) else label)
            else:
                x_labels.append(label)
    else:
        x_labels = dendro['ivl']
    
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


# Default alias
dendrogram = dendrogram_static
