"""Clustering analysis visualization charts."""

from typing import Optional
from ..types import ArrayLike, Labels, MatplotlibAxes, MatrixLike
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ..utils import setup_plot, apply_theme


def scatter_clusters(
    x: ArrayLike,
    y: ArrayLike,
    labels: ArrayLike,
    title: str = "Cluster Visualization",
    **kwargs
) -> MatplotlibAxes:
    """Create a cluster-labeled scatter plot.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        x (ArrayLike): Values plotted along the x-axis.
        y (ArrayLike): Values plotted along the y-axis.
        labels (ArrayLike): Class, feature, sample, or cluster labels shown on the chart.
        title (str): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``'Cluster Visualization'``.
        **kwargs (Any): Additional keyword arguments forwarded to the underlying plotting function.
    
    Returns:
        matplotlib.axes.Axes: Configured matplotlib axes containing the rendered static chart.
    
    Raises:
        TypeError: If required inputs are not compatible with the plotting backend.
        ValueError: If input lengths, matrix shapes, or option values are invalid for the requested chart.
    
    Example:
        ```python
        import dataviz as dv
        result = dv.scatter_clusters(x, y)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
    """
    fig, ax = setup_plot(title=title, xlabel='Feature 1', ylabel='Feature 2')
    
    unique_labels = np.unique(labels)
    colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))
    
    for label, color in zip(unique_labels, colors):
        mask = labels == label
        ax.scatter(x[mask], y[mask], label=f'Cluster {label}', 
                  color=color, alpha=0.6, **kwargs)
    
    ax.legend()
    apply_theme(ax)
    
    return ax


def elbow_plot(
    n_clusters: ArrayLike,
    inertias: ArrayLike,
    title: str = "Elbow Plot",
    **kwargs
) -> MatplotlibAxes:
    """Create an elbow plot for selecting a cluster count.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        n_clusters (ArrayLike): Configuration value for ``n_clusters``.
        inertias (ArrayLike): Within-cluster sum-of-squares or inertia values by cluster count.
        title (str): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``'Elbow Plot'``.
        **kwargs (Any): Additional keyword arguments forwarded to the underlying plotting function.
    
    Returns:
        matplotlib.axes.Axes: Configured matplotlib axes containing the rendered static chart.
    
    Raises:
        TypeError: If required inputs are not compatible with the plotting backend.
        ValueError: If input lengths, matrix shapes, or option values are invalid for the requested chart.
    
    Example:
        ```python
        import dataviz as dv
        result = dv.elbow_plot(inertias)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
    """
    fig, ax = setup_plot(title=title, xlabel='Number of Clusters', ylabel='Inertia')
    
    ax.plot(n_clusters, inertias, 'o-', **kwargs)
    ax.grid(True, alpha=0.3)
    
    apply_theme(ax)
    
    return ax


def dendrogram(
    linkage_matrix: MatrixLike,
    labels: Optional[Labels] = None,
    title: str = "Dendrogram",
    **kwargs
) -> MatplotlibAxes:
    """Create a dendrogram from hierarchical clustering linkage data.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        linkage_matrix (MatrixLike): Hierarchical clustering linkage matrix.
        labels (Optional[Labels]): Class, feature, sample, or cluster labels shown on the chart. Defaults to ``None``.
        title (str): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``'Dendrogram'``.
        **kwargs (Any): Additional keyword arguments forwarded to the underlying plotting function.
    
    Returns:
        matplotlib.axes.Axes: Configured matplotlib axes containing the rendered static chart.
    
    Raises:
        TypeError: If required inputs are not compatible with the plotting backend.
        ValueError: If input lengths, matrix shapes, or option values are invalid for the requested chart.
    
    Example:
        ```python
        import dataviz as dv
        result = dv.dendrogram(linkage_matrix)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
    """
    from scipy.cluster.hierarchy import dendrogram as scipy_dendrogram
    
    fig, ax = setup_plot(title=title, figsize=(12, 6))
    
    scipy_dendrogram(linkage_matrix, labels=labels, ax=ax, **kwargs)
    
    ax.set_ylabel('Distance')
    
    return ax
