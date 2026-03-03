"""Classification analysis visualization charts - static and interactive versions."""

# Static (matplotlib) imports
from .confusion_matrix import confusion_matrix_plot_static
from .roc import roc_curve_static
from .pr_curve import precision_recall_curve_static

# Interactive (plotly) imports
from .confusion_matrix import confusion_matrix_plot_interactive
from .roc import roc_curve_interactive
from .pr_curve import precision_recall_curve_interactive

# Convenience aliases
confusion_matrix_plot = confusion_matrix_plot_static
roc_curve = roc_curve_static
precision_recall_curve = precision_recall_curve_static

__all__ = [
    # Static versions
    "confusion_matrix_plot_static",
    "roc_curve_static",
    "precision_recall_curve_static",
    # Interactive versions
    "confusion_matrix_plot_interactive",
    "roc_curve_interactive",
    "precision_recall_curve_interactive",
    # Aliases (default to static)
    "confusion_matrix_plot",
    "roc_curve",
    "precision_recall_curve",
]
