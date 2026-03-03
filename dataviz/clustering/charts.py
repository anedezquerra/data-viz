"""Clustering analysis visualization charts."""

from typing import Optional
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ..utils import setup_plot, apply_theme


def scatter_clusters(
    x: np.ndarray,
    y: np.ndarray,
    labels: np.ndarray,
    title: str = "Cluster Visualization",
    **kwargs
) -> plt.Axes:
    """
    Visualize clusters in 2D scatter plot.

    Parameters
    ----------
    x : array
        X-coordinates
    y : array
        Y-coordinates
    labels : array
        Cluster labels
    title : str, default "Cluster Visualization"
        Chart title
    **kwargs
        Additional plot arguments

    Returns
    -------
    matplotlib.axes.Axes
        The plot axes
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
    n_clusters: np.ndarray,
    inertias: np.ndarray,
    title: str = "Elbow Plot",
    **kwargs
) -> plt.Axes:
    """
    Plot elbow curve for determining optimal number of clusters.

    Parameters
    ----------
    n_clusters : array
        Number of clusters
    inertias : array
        Inertia values for each cluster count
    title : str, default "Elbow Plot"
        Chart title
    **kwargs
        Additional plot arguments

    Returns
    -------
    matplotlib.axes.Axes
        The plot axes
    """
    fig, ax = setup_plot(title=title, xlabel='Number of Clusters', ylabel='Inertia')
    
    ax.plot(n_clusters, inertias, 'o-', **kwargs)
    ax.grid(True, alpha=0.3)
    
    apply_theme(ax)
    
    return ax


def dendrogram(
    linkage_matrix: np.ndarray,
    labels: Optional[list] = None,
    title: str = "Dendrogram",
    **kwargs
) -> plt.Axes:
    """
    Plot hierarchical clustering dendrogram.

    Parameters
    ----------
    linkage_matrix : array
        Linkage matrix from hierarchical clustering
    labels : list, optional
        Sample labels
    title : str, default "Dendrogram"
        Chart title
    **kwargs
        Additional plot arguments

    Returns
    -------
    matplotlib.axes.Axes
        The plot axes
    """
    from scipy.cluster.hierarchy import dendrogram as scipy_dendrogram
    
    fig, ax = setup_plot(title=title, figsize=(12, 6))
    
    scipy_dendrogram(linkage_matrix, labels=labels, ax=ax, **kwargs)
    
    ax.set_ylabel('Distance')
    
    return ax
