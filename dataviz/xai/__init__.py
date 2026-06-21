"""Explainable AI (XAI) visualization charts.

Comprehensive XAI toolkit organised by family:

* **Feature importance** — single, grouped, distribution and method-comparison
  bars (``feature_importance``, ``permutation_importance_bar``,
  ``feature_importance_grouped_bar``, ``feature_importance_boxplot``,
  ``drop_column_importance_bar``, ``importance_method_scatter``);
* **SHAP** — bee-swarm summary, global mean(|SHAP|) bar, per-feature violin,
  dependence plot, interaction heatmap and waterfall plot
  (``shap_plot``, ``shap_summary_dot``, ``shap_bar_global``, ``shap_violin``,
  ``shap_dependence_plot``, ``shap_interaction_heatmap``, ``shap_waterfall_plot``);
* **Local explanations** — force plot, decision plot and LIME-style bar
  (``shap_force_plot``, ``shap_decision_plot``, ``lime_explanation_bar``);
* **Partial dependence and ICE** — 1-D and 2-D PDP, ICE, centered ICE and ALE
  (``partial_dependence``, ``partial_dependence_2d_heatmap``, ``ice_plot``,
  ``centered_ice_plot``, ``ale_plot_1d``);
* **Surrogate and counterfactual** — surrogate tree and counterfactual recipe
  (``surrogate_tree_plot``, ``counterfactual_change_bar``);
* **Cohort / segment** — per-segment importance heatmap and SHAP cluster
  heatmap (``importance_by_segment_heatmap``, ``shap_cluster_heatmap``).

Every chart family ships a ``*_static`` (matplotlib) and a ``*_interactive``
(plotly) implementation; convenience aliases drop the suffix and default to
the static version.
"""

# Core
from .feature_imp import feature_importance_static, feature_importance_interactive
from .shap import shap_plot_static, shap_plot_interactive
from .partial_dep import partial_dependence_static, partial_dependence_interactive

# Extended feature importance
from .importance_extra import (
    permutation_importance_bar_static, permutation_importance_bar_interactive,
    feature_importance_grouped_bar_static, feature_importance_grouped_bar_interactive,
    feature_importance_boxplot_static, feature_importance_boxplot_interactive,
    drop_column_importance_bar_static, drop_column_importance_bar_interactive,
    importance_method_scatter_static, importance_method_scatter_interactive,
)

# Extended SHAP
from .shap_extra import (
    shap_summary_dot_static, shap_summary_dot_interactive,
    shap_bar_global_static, shap_bar_global_interactive,
    shap_violin_static, shap_violin_interactive,
    shap_dependence_plot_static, shap_dependence_plot_interactive,
    shap_interaction_heatmap_static, shap_interaction_heatmap_interactive,
    shap_waterfall_plot_static, shap_waterfall_plot_interactive,
)

# Local explanations
from .local_explanations import (
    shap_force_plot_static, shap_force_plot_interactive,
    shap_decision_plot_static, shap_decision_plot_interactive,
    lime_explanation_bar_static, lime_explanation_bar_interactive,
)

# PDP / ICE / ALE
from .pdp_extra import (
    partial_dependence_2d_heatmap_static, partial_dependence_2d_heatmap_interactive,
    ice_plot_static, ice_plot_interactive,
    centered_ice_plot_static, centered_ice_plot_interactive,
    ale_plot_1d_static, ale_plot_1d_interactive,
)

# Surrogate / counterfactual
from .surrogate import (
    surrogate_tree_plot_static, surrogate_tree_plot_interactive,
    counterfactual_change_bar_static, counterfactual_change_bar_interactive,
)

# Cohort / segment
from .cohort import (
    importance_by_segment_heatmap_static, importance_by_segment_heatmap_interactive,
    shap_cluster_heatmap_static, shap_cluster_heatmap_interactive,
)

# Convenience aliases (default to static)
feature_importance = feature_importance_static
shap_plot = shap_plot_static
partial_dependence = partial_dependence_static
permutation_importance_bar = permutation_importance_bar_static
feature_importance_grouped_bar = feature_importance_grouped_bar_static
feature_importance_boxplot = feature_importance_boxplot_static
drop_column_importance_bar = drop_column_importance_bar_static
importance_method_scatter = importance_method_scatter_static
shap_summary_dot = shap_summary_dot_static
shap_bar_global = shap_bar_global_static
shap_violin = shap_violin_static
shap_dependence_plot = shap_dependence_plot_static
shap_interaction_heatmap = shap_interaction_heatmap_static
shap_waterfall_plot = shap_waterfall_plot_static
shap_force_plot = shap_force_plot_static
shap_decision_plot = shap_decision_plot_static
lime_explanation_bar = lime_explanation_bar_static
partial_dependence_2d_heatmap = partial_dependence_2d_heatmap_static
ice_plot = ice_plot_static
centered_ice_plot = centered_ice_plot_static
ale_plot_1d = ale_plot_1d_static
surrogate_tree_plot = surrogate_tree_plot_static
counterfactual_change_bar = counterfactual_change_bar_static
importance_by_segment_heatmap = importance_by_segment_heatmap_static
shap_cluster_heatmap = shap_cluster_heatmap_static

__all__ = [
    # Static
    "feature_importance_static", "shap_plot_static", "partial_dependence_static",
    "permutation_importance_bar_static",
    "feature_importance_grouped_bar_static",
    "feature_importance_boxplot_static",
    "drop_column_importance_bar_static",
    "importance_method_scatter_static",
    "shap_summary_dot_static", "shap_bar_global_static", "shap_violin_static",
    "shap_dependence_plot_static", "shap_interaction_heatmap_static",
    "shap_waterfall_plot_static",
    "shap_force_plot_static", "shap_decision_plot_static",
    "lime_explanation_bar_static",
    "partial_dependence_2d_heatmap_static",
    "ice_plot_static", "centered_ice_plot_static", "ale_plot_1d_static",
    "surrogate_tree_plot_static", "counterfactual_change_bar_static",
    "importance_by_segment_heatmap_static", "shap_cluster_heatmap_static",
    # Interactive
    "feature_importance_interactive", "shap_plot_interactive",
    "partial_dependence_interactive",
    "permutation_importance_bar_interactive",
    "feature_importance_grouped_bar_interactive",
    "feature_importance_boxplot_interactive",
    "drop_column_importance_bar_interactive",
    "importance_method_scatter_interactive",
    "shap_summary_dot_interactive", "shap_bar_global_interactive",
    "shap_violin_interactive", "shap_dependence_plot_interactive",
    "shap_interaction_heatmap_interactive", "shap_waterfall_plot_interactive",
    "shap_force_plot_interactive", "shap_decision_plot_interactive",
    "lime_explanation_bar_interactive",
    "partial_dependence_2d_heatmap_interactive",
    "ice_plot_interactive", "centered_ice_plot_interactive",
    "ale_plot_1d_interactive",
    "surrogate_tree_plot_interactive", "counterfactual_change_bar_interactive",
    "importance_by_segment_heatmap_interactive",
    "shap_cluster_heatmap_interactive",
    # Aliases
    "feature_importance", "shap_plot", "partial_dependence",
    "permutation_importance_bar", "feature_importance_grouped_bar",
    "feature_importance_boxplot", "drop_column_importance_bar",
    "importance_method_scatter",
    "shap_summary_dot", "shap_bar_global", "shap_violin",
    "shap_dependence_plot", "shap_interaction_heatmap", "shap_waterfall_plot",
    "shap_force_plot", "shap_decision_plot", "lime_explanation_bar",
    "partial_dependence_2d_heatmap", "ice_plot", "centered_ice_plot",
    "ale_plot_1d", "surrogate_tree_plot", "counterfactual_change_bar",
    "importance_by_segment_heatmap", "shap_cluster_heatmap",
]
