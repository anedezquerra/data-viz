"""Statistical Process Control (SPC) charts - static and interactive versions."""

# Static (matplotlib) imports
from .control import control_chart_static
from .x_range import x_range_chart_static

# Interactive (plotly) imports
from .control import control_chart_interactive
from .x_range import x_range_chart_interactive

# Convenience aliases
control_chart = control_chart_static
x_range_chart = x_range_chart_static

__all__ = [
    # Static versions
    "control_chart_static",
    "x_range_chart_static",
    # Interactive versions
    "control_chart_interactive",
    "x_range_chart_interactive",
    # Aliases (default to static)
    "control_chart",
    "x_range_chart",
]
