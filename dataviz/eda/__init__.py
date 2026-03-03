"""Exploratory Data Analysis (EDA) visualization charts - static and interactive versions."""

# Static (matplotlib) imports
from .missing_data import missing_data_plot_static
from .distribution import distribution_summary_static
from .class_dist import class_distribution_static

# Interactive (plotly) imports
from .missing_data import missing_data_plot_interactive
from .distribution import distribution_summary_interactive
from .class_dist import class_distribution_interactive

# Convenience aliases
missing_data_plot = missing_data_plot_static
distribution_summary = distribution_summary_static
class_distribution = class_distribution_static

__all__ = [
    # Static versions
    "missing_data_plot_static",
    "distribution_summary_static",
    "class_distribution_static",
    # Interactive versions
    "missing_data_plot_interactive",
    "distribution_summary_interactive",
    "class_distribution_interactive",
    # Aliases (default to static)
    "missing_data_plot",
    "distribution_summary",
    "class_distribution",
]
