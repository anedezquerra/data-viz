"""Curated use cases for clustering member pages."""

USE_CASES = {
    # charts.py
    "dataviz.clustering.charts.scatter_clusters": "Use to sanity-check clustering results by coloring points by cluster label in a two-dimensional view.",
    "dataviz.clustering.charts.elbow_plot": "Use when choosing k for k-means by looking for the bend where added clusters stop reducing inertia much.",
    "dataviz.clustering.charts.dendrogram": "Use to inspect hierarchical clustering merges and decide where to cut the tree into flat clusters.",
    # dendrogram.py
    "dataviz.clustering.dendrogram.dendrogram_static": "Use to inspect hierarchical clustering merges and decide where to cut the tree into flat clusters.",
    "dataviz.clustering.dendrogram.dendrogram_interactive": "Use to inspect hierarchical clustering merges and decide where to cut the tree into flat clusters.",
    # elbow.py
    "dataviz.clustering.elbow.elbow_plot_static": "Use when choosing k for k-means by looking for the bend where added clusters stop reducing inertia much.",
    "dataviz.clustering.elbow.elbow_plot_interactive": "Use when choosing k for k-means by looking for the bend where added clusters stop reducing inertia much.",
    # elbow_enhanced.py
    "dataviz.clustering.elbow_enhanced.elbow_plot_static": "Use when choosing k for k-means by looking for the bend where added clusters stop reducing inertia much.",
    "dataviz.clustering.elbow_enhanced.elbow_plot_interactive": "Use when choosing k for k-means by looking for the bend where added clusters stop reducing inertia much.",
    # scatter_clusters.py
    "dataviz.clustering.scatter_clusters.scatter_clusters_static": "Use to sanity-check clustering results by coloring points by cluster label in a two-dimensional view.",
    "dataviz.clustering.scatter_clusters.scatter_clusters_interactive": "Use to sanity-check clustering results by coloring points by cluster label in a two-dimensional view.",
}
