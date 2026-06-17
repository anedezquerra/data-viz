"""Dendrogram implementation - static and interactive versions."""

from typing import Optional
from ..types import FigureSize, Labels, MatplotlibAxes, MatrixLike, PlotlyFigure
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from scipy.cluster.hierarchy import dendrogram as scipy_dendrogram
from ..utils import setup_plot, apply_theme


def dendrogram_static(
    linkage_matrix: MatrixLike,
    labels: Optional[Labels] = None,
    title: Optional[str] = None,
    xlabel: str = "Sample Index",
    ylabel: str = "Distance",
    figsize: FigureSize = (12, 6),
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
) -> MatplotlibAxes:
    """Create a static dendrogram from hierarchical clustering linkage data.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        linkage_matrix (MatrixLike): Hierarchical clustering linkage matrix.
        labels (Optional[Labels]): Class, feature, sample, or cluster labels shown on the chart. Defaults to ``None``.
        title (Optional[str]): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``None``.
        xlabel (str): Optional x-axis label. Defaults to ``'Sample Index'``.
        ylabel (str): Optional y-axis label. Defaults to ``'Distance'``.
        figsize (FigureSize): Matplotlib figure size as ``(width, height)`` in inches. Defaults to ``(12, 6)``.
        color_threshold (Optional[float]): Configuration value for ``color_threshold``. Defaults to ``None``.
        above_threshold_color (str): Configuration value for ``above_threshold_color``. Defaults to ``'gray'``.
        orientation (str): Configuration value for ``orientation``. Defaults to ``'top'``.
        leaf_rotation (float): Configuration value for ``leaf_rotation``. Defaults to ``90.0``.
        leaf_font_size (int): Configuration value for ``leaf_font_size``. Defaults to ``10``.
        font_size (int): Configuration value for ``font_size``. Defaults to ``10``.
        title_size (int): Configuration value for ``title_size``. Defaults to ``14``.
        label_size (int): Configuration value for ``label_size``. Defaults to ``11``.
        theme (str): Named styling theme applied after the base plot is created. Defaults to ``'default'``.
        style (str): Matplotlib style context used while building the figure. Defaults to ``'default'``.
        dpi (int): Configuration value for ``dpi``. Defaults to ``100``.
        grid (bool): Configuration value for ``grid``. Defaults to ``True``.
        grid_alpha (float): Configuration value for ``grid_alpha``. Defaults to ``0.3``.
        show_leaf_counts (bool): Configuration value for ``show_leaf_counts``. Defaults to ``True``.
        line_color (str): Configuration value for ``line_color``. Defaults to ``'black'``.
        line_width (float): Configuration value for ``line_width``. Defaults to ``1.5``.
        **kwargs (Any): Additional keyword arguments forwarded to the underlying plotting function.
    
    Returns:
        matplotlib.axes.Axes: Configured matplotlib axes containing the rendered static chart.
    
    Raises:
        TypeError: If required inputs are not compatible with the plotting backend.
        ValueError: If input lengths, matrix shapes, or option values are invalid for the requested chart.
    
    Example:
        ```python
        import dataviz as dv
        result = dv.dendrogram_static(linkage_matrix)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
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
    linkage_matrix: MatrixLike,
    labels: Optional[Labels] = None,
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
) -> PlotlyFigure:
    """Create an interactive dendrogram from hierarchical clustering linkage data.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        linkage_matrix (MatrixLike): Hierarchical clustering linkage matrix.
        labels (Optional[Labels]): Class, feature, sample, or cluster labels shown on the chart. Defaults to ``None``.
        title (Optional[str]): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``None``.
        xlabel (str): Optional x-axis label. Defaults to ``'Samples'``.
        ylabel (str): Optional y-axis label. Defaults to ``'Distance'``.
        height (int): Plotly figure height in pixels. Defaults to ``600``.
        width (int): Plotly figure width in pixels. Defaults to ``900``.
        line_color (str): Configuration value for ``line_color``. Defaults to ``'black'``.
        line_width (int): Configuration value for ``line_width``. Defaults to ``2``.
        font_size (int): Configuration value for ``font_size``. Defaults to ``12``.
        title_size (int): Configuration value for ``title_size``. Defaults to ``16``.
        label_size (int): Configuration value for ``label_size``. Defaults to ``12``.
        hovermode (str): Configuration value for ``hovermode``. Defaults to ``'closest'``.
        showlegend (bool): Configuration value for ``showlegend``. Defaults to ``False``.
        template (str): Plotly template used to style the interactive figure. Defaults to ``'plotly'``.
        color_threshold (Optional[float]): Configuration value for ``color_threshold``. Defaults to ``None``.
        **kwargs (Any): Additional keyword arguments forwarded to the underlying plotting function.
    
    Returns:
        plotly.graph_objects.Figure: Configured Plotly figure containing the rendered interactive chart.
    
    Raises:
        TypeError: If required inputs are not compatible with the plotting backend.
        ValueError: If input lengths, matrix shapes, or option values are invalid for the requested chart.
    
    Example:
        ```python
        import dataviz as dv
        result = dv.dendrogram_interactive(linkage_matrix)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
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
