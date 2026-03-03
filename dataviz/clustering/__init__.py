"""Clustering analysis visualization charts - static and interactive versions."""

# Static (matplotlib) imports
from .scatter_clusters import scatter_clusters_static
from .dendrogram import dendrogram_static
from .elbow import elbow_plot_static

# Interactive (plotly) imports
from .scatter_clusters import scatter_clusters_interactive
from .dendrogram import dendrogram_interactive
from .elbow import elbow_plot_interactive

# Convenience aliases
scatter_clusters = scatter_clusters_static
dendrogram = dendrogram_static
elbow_plot = elbow_plot_static

__all__ = [
    # Static versions
    "scatter_clusters_static",
    "dendrogram_static",
    "elbow_plot_static",
    # Interactive versions
    "scatter_clusters_interactive",
    "dendrogram_interactive",
    "elbow_plot_interactive",
    # Aliases (default to static)
    "scatter_clusters",
    "dendrogram",
    "elbow_plot",
]
