"""Regression analysis visualization charts - static and interactive versions."""

# Static (matplotlib) imports
from .residual import residual_plot_static
from .prediction import prediction_plot_static
from .learning import learning_curve_static

# Interactive (plotly) imports
from .residual import residual_plot_interactive
from .prediction import prediction_plot_interactive
from .learning import learning_curve_interactive

# Convenience aliases
residual_plot = residual_plot_static
prediction_plot = prediction_plot_static
learning_curve = learning_curve_static

__all__ = [
    # Static versions
    "residual_plot_static",
    "prediction_plot_static",
    "learning_curve_static",
    # Interactive versions
    "residual_plot_interactive",
    "prediction_plot_interactive",
    "learning_curve_interactive",
    # Aliases (default to static)
    "residual_plot",
    "prediction_plot",
    "learning_curve",
]
