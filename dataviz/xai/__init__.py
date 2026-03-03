"""Explainable AI (XAI) visualization charts - static and interactive versions."""

# Static (matplotlib) imports
from .feature_imp import feature_importance_static
from .shap import shap_plot_static
from .partial_dep import partial_dependence_static

# Interactive (plotly) imports
from .feature_imp import feature_importance_interactive
from .shap import shap_plot_interactive
from .partial_dep import partial_dependence_interactive

# Convenience aliases
feature_importance = feature_importance_static
shap_plot = shap_plot_static
partial_dependence = partial_dependence_static

__all__ = [
    # Static versions
    "feature_importance_static",
    "shap_plot_static",
    "partial_dependence_static",
    # Interactive versions
    "feature_importance_interactive",
    "shap_plot_interactive",
    "partial_dependence_interactive",
    # Aliases (default to static)
    "feature_importance",
    "shap_plot",
    "partial_dependence",
]
