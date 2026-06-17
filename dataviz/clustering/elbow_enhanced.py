"""Elbow plot implementation - static and interactive versions."""

from typing import Optional
from ..types import ArrayLike, FigureSize, MatplotlibAxes, PlotlyFigure
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from ..utils import setup_plot, apply_theme


def elbow_plot_static(
    n_clusters: ArrayLike,
    inertias: ArrayLike,
    title: Optional[str] = None,
    xlabel: str = "Number of Clusters",
    ylabel: str = "Inertia",
    figsize: FigureSize = (10, 6),
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
) -> MatplotlibAxes:
    """Create a static elbow plot for selecting a cluster count.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        n_clusters (ArrayLike): Configuration value for ``n_clusters``.
        inertias (ArrayLike): Within-cluster sum-of-squares or inertia values by cluster count.
        title (Optional[str]): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``None``.
        xlabel (str): Optional x-axis label. Defaults to ``'Number of Clusters'``.
        ylabel (str): Optional y-axis label. Defaults to ``'Inertia'``.
        figsize (FigureSize): Matplotlib figure size as ``(width, height)`` in inches. Defaults to ``(10, 6)``.
        color (str): Configuration value for ``color``. Defaults to ``'blue'``.
        marker (str): Configuration value for ``marker``. Defaults to ``'o'``.
        marker_size (int): Configuration value for ``marker_size``. Defaults to ``50``.
        linestyle (str): Configuration value for ``linestyle``. Defaults to ``'-'``.
        linewidth (float): Configuration value for ``linewidth``. Defaults to ``2.0``.
        marker_edgecolor (str): Configuration value for ``marker_edgecolor``. Defaults to ``'black'``.
        marker_edgewidth (float): Configuration value for ``marker_edgewidth``. Defaults to ``1.0``.
        alpha (float): Configuration value for ``alpha``. Defaults to ``0.7``.
        elbow_idx (Optional[int]): Configuration value for ``elbow_idx``. Defaults to ``None``.
        elbow_marker (str): Configuration value for ``elbow_marker``. Defaults to ``'X'``.
        elbow_color (str): Configuration value for ``elbow_color``. Defaults to ``'red'``.
        elbow_size (int): Configuration value for ``elbow_size``. Defaults to ``200``.
        font_size (int): Configuration value for ``font_size``. Defaults to ``10``.
        title_size (int): Configuration value for ``title_size``. Defaults to ``14``.
        label_size (int): Configuration value for ``label_size``. Defaults to ``11``.
        theme (str): Named styling theme applied after the base plot is created. Defaults to ``'default'``.
        style (str): Matplotlib style context used while building the figure. Defaults to ``'default'``.
        dpi (int): Configuration value for ``dpi``. Defaults to ``100``.
        grid (bool): Configuration value for ``grid``. Defaults to ``True``.
        grid_alpha (float): Configuration value for ``grid_alpha``. Defaults to ``0.3``.
        **kwargs (Any): Additional keyword arguments forwarded to the underlying plotting function.
    
    Returns:
        matplotlib.axes.Axes: Configured matplotlib axes containing the rendered static chart.
    
    Raises:
        TypeError: If required inputs are not compatible with the plotting backend.
        ValueError: If input lengths, matrix shapes, or option values are invalid for the requested chart.
    
    Example:
        ```python
        import dataviz as dv
        result = dv.elbow_plot_static(inertias)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
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
    n_clusters: ArrayLike,
    inertias: ArrayLike,
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
) -> PlotlyFigure:
    """Create an interactive elbow plot for selecting a cluster count.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        n_clusters (ArrayLike): Configuration value for ``n_clusters``.
        inertias (ArrayLike): Within-cluster sum-of-squares or inertia values by cluster count.
        title (Optional[str]): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``None``.
        xlabel (str): Optional x-axis label. Defaults to ``'Number of Clusters'``.
        ylabel (str): Optional y-axis label. Defaults to ``'Inertia'``.
        height (int): Plotly figure height in pixels. Defaults to ``600``.
        width (int): Plotly figure width in pixels. Defaults to ``900``.
        line_color (str): Configuration value for ``line_color``. Defaults to ``'blue'``.
        line_width (int): Configuration value for ``line_width``. Defaults to ``2``.
        marker_size (int): Configuration value for ``marker_size``. Defaults to ``8``.
        marker_symbol (str): Configuration value for ``marker_symbol``. Defaults to ``'circle'``.
        marker_color (Optional[str]): Configuration value for ``marker_color``. Defaults to ``None``.
        opacity (float): Configuration value for ``opacity``. Defaults to ``0.7``.
        elbow_idx (Optional[int]): Configuration value for ``elbow_idx``. Defaults to ``None``.
        elbow_marker (str): Configuration value for ``elbow_marker``. Defaults to ``'x-open-dot'``.
        elbow_color (str): Configuration value for ``elbow_color``. Defaults to ``'red'``.
        font_size (int): Configuration value for ``font_size``. Defaults to ``12``.
        title_size (int): Configuration value for ``title_size``. Defaults to ``16``.
        label_size (int): Configuration value for ``label_size``. Defaults to ``12``.
        hovermode (str): Configuration value for ``hovermode``. Defaults to ``'closest'``.
        showlegend (bool): Configuration value for ``showlegend``. Defaults to ``False``.
        template (str): Plotly template used to style the interactive figure. Defaults to ``'plotly'``.
        **kwargs (Any): Additional keyword arguments forwarded to the underlying plotting function.
    
    Returns:
        plotly.graph_objects.Figure: Configured Plotly figure containing the rendered interactive chart.
    
    Raises:
        TypeError: If required inputs are not compatible with the plotting backend.
        ValueError: If input lengths, matrix shapes, or option values are invalid for the requested chart.
    
    Example:
        ```python
        import dataviz as dv
        result = dv.elbow_plot_interactive(inertias)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
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
