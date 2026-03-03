"""Bivariate visualization charts - static and interactive versions."""

# Static (matplotlib) imports
from .scatter import scatter_plot_static
from .line import line_plot_static
from .correlation import correlation_heatmap_static

# Interactive (plotly) imports
from .scatter import scatter_plot_interactive
from .line import line_plot_interactive
from .correlation import correlation_heatmap_interactive

# Convenience aliases
scatter_plot = scatter_plot_static
line_plot = line_plot_static
correlation_heatmap = correlation_heatmap_static

__all__ = [
    # Static versions
    "scatter_plot_static",
    "line_plot_static",
    "correlation_heatmap_static",
    # Interactive versions
    "scatter_plot_interactive",
    "line_plot_interactive",
    "correlation_heatmap_interactive",
    # Aliases (default to static)
    "scatter_plot",
    "line_plot",
    "correlation_heatmap",
]
