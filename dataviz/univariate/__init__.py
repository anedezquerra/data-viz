"""Univariate visualization charts - static and interactive versions."""

# Static (matplotlib) imports
from .histogram import histogram_static
from .density import density_static
from .box_plot import box_plot_static
from .violin_plot import violin_plot_static

# Interactive (plotly) imports
from .histogram import histogram_interactive
from .density import density_interactive
from .box_plot import box_plot_interactive
from .violin_plot import violin_plot_interactive

# Convenience aliases
histogram = histogram_static
density_plot = density_static
box_plot = box_plot_static
violin_plot = violin_plot_static

__all__ = [
    # Static versions
    "histogram_static",
    "density_static",
    "box_plot_static",
    "violin_plot_static",
    # Interactive versions
    "histogram_interactive",
    "density_interactive",
    "box_plot_interactive",
    "violin_plot_interactive",
    # Aliases (default to static)
    "histogram",
    "density_plot",
    "box_plot",
    "violin_plot",
]
