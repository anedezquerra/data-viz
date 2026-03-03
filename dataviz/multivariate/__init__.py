"""Multivariate visualization charts - static and interactive versions."""

# Static (matplotlib) imports
from .pairplot import pairplot_static
from .heatmap import heatmap_static
from .parallel import parallel_coordinates_static

# Interactive (plotly) imports
from .pairplot import pairplot_interactive
from .heatmap import heatmap_interactive
from .parallel import parallel_coordinates_interactive

# Convenience aliases
pairplot = pairplot_static
heatmap = heatmap_static
parallel_coordinates = parallel_coordinates_static

__all__ = [
    # Static versions
    "pairplot_static",
    "heatmap_static",
    "parallel_coordinates_static",
    # Interactive versions
    "pairplot_interactive",
    "heatmap_interactive", 
    "parallel_coordinates_interactive",
    # Aliases (default to static)
    "pairplot",
    "heatmap",
    "parallel_coordinates",
]
