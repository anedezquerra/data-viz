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

# Phase 2: importance — gain, stability, correlation, clustermap
from .importance_more import (
    gain_importance_bar_static, gain_importance_bar_interactive,
    importance_stability_plot_static, importance_stability_plot_interactive,
    importance_correlation_heatmap_static, importance_correlation_heatmap_interactive,
    feature_clustermap_static, feature_clustermap_interactive,
)

# Phase 2: SHAP — beeswarm, instance heatmap, stacked force, main vs interaction,
# monotonicity, temporal drift
from .shap_more import (
    shap_beeswarm_plot_static, shap_beeswarm_plot_interactive,
    shap_heatmap_instances_static, shap_heatmap_instances_interactive,
    shap_force_stacked_static, shap_force_stacked_interactive,
    shap_main_vs_interaction_bar_static, shap_main_vs_interaction_bar_interactive,
    shap_monotonicity_plot_static, shap_monotonicity_plot_interactive,
    shap_temporal_drift_static, shap_temporal_drift_interactive,
)

# Phase 2: local — anchors, k-NN, prototypes/criticisms, contrastive
from .local_more import (
    anchor_explanation_plot_static, anchor_explanation_plot_interactive,
    nearest_neighbor_explanation_static, nearest_neighbor_explanation_interactive,
    prototype_criticism_grid_static, prototype_criticism_grid_interactive,
    contrastive_explanation_bar_static, contrastive_explanation_bar_interactive,
)

# Phase 2: dependence — PDP+ICE overlay, 2-D ALE, H-statistic, interaction network
from .dependence_more import (
    pdp_with_ice_overlay_static, pdp_with_ice_overlay_interactive,
    ale_plot_2d_static, ale_plot_2d_interactive,
    h_statistic_heatmap_static, h_statistic_heatmap_interactive,
    interaction_network_static, interaction_network_interactive,
)

# Phase 2: counterfactual — paths, diverse CFs, what-if slider
from .counterfactuals import (
    counterfactual_path_plot_static, counterfactual_path_plot_interactive,
    diverse_counterfactual_grid_static, diverse_counterfactual_grid_interactive,
    what_if_slider_plot_static, what_if_slider_plot_interactive,
)

# Phase 2: fairness — disparate impact, subgroup divergence, intersectional
from .fairness_xai import (
    disparate_impact_by_segment_static, disparate_impact_by_segment_interactive,
    subgroup_shap_divergence_static, subgroup_shap_divergence_interactive,
    intersectional_importance_heatmap_static, intersectional_importance_heatmap_interactive,
)

# Phase 2: uncertainty — predictive uncertainty band, attribution, decomposition
from .uncertainty import (
    prediction_uncertainty_plot_static, prediction_uncertainty_plot_interactive,
    confidence_attribution_bar_static, confidence_attribution_bar_interactive,
    epistemic_vs_aleatoric_plot_static, epistemic_vs_aleatoric_plot_interactive,
)

# Phase 2: concept — TCAV, saliency, attention, embedding
from .concept import (
    concept_activation_bar_static, concept_activation_bar_interactive,
    saliency_overlay_plot_static, saliency_overlay_plot_interactive,
    attention_heatmap_static, attention_heatmap_interactive,
    embedding_projection_plot_static, embedding_projection_plot_interactive,
)

# Phase 2: model comparison — importance matrix, SHAP agreement, Rashomon band
from .comparison import (
    importance_comparison_heatmap_static, importance_comparison_heatmap_interactive,
    shap_model_agreement_scatter_static, shap_model_agreement_scatter_interactive,
    rashomon_importance_band_static, rashomon_importance_band_interactive,
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
# Phase 2 aliases
gain_importance_bar = gain_importance_bar_static
importance_stability_plot = importance_stability_plot_static
importance_correlation_heatmap = importance_correlation_heatmap_static
feature_clustermap = feature_clustermap_static
shap_beeswarm_plot = shap_beeswarm_plot_static
shap_heatmap_instances = shap_heatmap_instances_static
shap_force_stacked = shap_force_stacked_static
shap_main_vs_interaction_bar = shap_main_vs_interaction_bar_static
shap_monotonicity_plot = shap_monotonicity_plot_static
shap_temporal_drift = shap_temporal_drift_static
anchor_explanation_plot = anchor_explanation_plot_static
nearest_neighbor_explanation = nearest_neighbor_explanation_static
prototype_criticism_grid = prototype_criticism_grid_static
contrastive_explanation_bar = contrastive_explanation_bar_static
pdp_with_ice_overlay = pdp_with_ice_overlay_static
ale_plot_2d = ale_plot_2d_static
h_statistic_heatmap = h_statistic_heatmap_static
interaction_network = interaction_network_static
counterfactual_path_plot = counterfactual_path_plot_static
diverse_counterfactual_grid = diverse_counterfactual_grid_static
what_if_slider_plot = what_if_slider_plot_static
disparate_impact_by_segment = disparate_impact_by_segment_static
subgroup_shap_divergence = subgroup_shap_divergence_static
intersectional_importance_heatmap = intersectional_importance_heatmap_static
prediction_uncertainty_plot = prediction_uncertainty_plot_static
confidence_attribution_bar = confidence_attribution_bar_static
epistemic_vs_aleatoric_plot = epistemic_vs_aleatoric_plot_static
concept_activation_bar = concept_activation_bar_static
saliency_overlay_plot = saliency_overlay_plot_static
attention_heatmap = attention_heatmap_static
embedding_projection_plot = embedding_projection_plot_static
importance_comparison_heatmap = importance_comparison_heatmap_static
shap_model_agreement_scatter = shap_model_agreement_scatter_static
rashomon_importance_band = rashomon_importance_band_static

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
    # Phase 2 static
    "gain_importance_bar_static", "importance_stability_plot_static",
    "importance_correlation_heatmap_static", "feature_clustermap_static",
    "shap_beeswarm_plot_static", "shap_heatmap_instances_static",
    "shap_force_stacked_static", "shap_main_vs_interaction_bar_static",
    "shap_monotonicity_plot_static", "shap_temporal_drift_static",
    "anchor_explanation_plot_static", "nearest_neighbor_explanation_static",
    "prototype_criticism_grid_static", "contrastive_explanation_bar_static",
    "pdp_with_ice_overlay_static", "ale_plot_2d_static",
    "h_statistic_heatmap_static", "interaction_network_static",
    "counterfactual_path_plot_static", "diverse_counterfactual_grid_static",
    "what_if_slider_plot_static",
    "disparate_impact_by_segment_static", "subgroup_shap_divergence_static",
    "intersectional_importance_heatmap_static",
    "prediction_uncertainty_plot_static", "confidence_attribution_bar_static",
    "epistemic_vs_aleatoric_plot_static",
    "concept_activation_bar_static", "saliency_overlay_plot_static",
    "attention_heatmap_static", "embedding_projection_plot_static",
    "importance_comparison_heatmap_static", "shap_model_agreement_scatter_static",
    "rashomon_importance_band_static",
    # Phase 2 interactive
    "gain_importance_bar_interactive", "importance_stability_plot_interactive",
    "importance_correlation_heatmap_interactive", "feature_clustermap_interactive",
    "shap_beeswarm_plot_interactive", "shap_heatmap_instances_interactive",
    "shap_force_stacked_interactive", "shap_main_vs_interaction_bar_interactive",
    "shap_monotonicity_plot_interactive", "shap_temporal_drift_interactive",
    "anchor_explanation_plot_interactive", "nearest_neighbor_explanation_interactive",
    "prototype_criticism_grid_interactive", "contrastive_explanation_bar_interactive",
    "pdp_with_ice_overlay_interactive", "ale_plot_2d_interactive",
    "h_statistic_heatmap_interactive", "interaction_network_interactive",
    "counterfactual_path_plot_interactive", "diverse_counterfactual_grid_interactive",
    "what_if_slider_plot_interactive",
    "disparate_impact_by_segment_interactive", "subgroup_shap_divergence_interactive",
    "intersectional_importance_heatmap_interactive",
    "prediction_uncertainty_plot_interactive", "confidence_attribution_bar_interactive",
    "epistemic_vs_aleatoric_plot_interactive",
    "concept_activation_bar_interactive", "saliency_overlay_plot_interactive",
    "attention_heatmap_interactive", "embedding_projection_plot_interactive",
    "importance_comparison_heatmap_interactive",
    "shap_model_agreement_scatter_interactive",
    "rashomon_importance_band_interactive",
    # Phase 2 aliases
    "gain_importance_bar", "importance_stability_plot",
    "importance_correlation_heatmap", "feature_clustermap",
    "shap_beeswarm_plot", "shap_heatmap_instances", "shap_force_stacked",
    "shap_main_vs_interaction_bar", "shap_monotonicity_plot",
    "shap_temporal_drift",
    "anchor_explanation_plot", "nearest_neighbor_explanation",
    "prototype_criticism_grid", "contrastive_explanation_bar",
    "pdp_with_ice_overlay", "ale_plot_2d", "h_statistic_heatmap",
    "interaction_network",
    "counterfactual_path_plot", "diverse_counterfactual_grid",
    "what_if_slider_plot",
    "disparate_impact_by_segment", "subgroup_shap_divergence",
    "intersectional_importance_heatmap",
    "prediction_uncertainty_plot", "confidence_attribution_bar",
    "epistemic_vs_aleatoric_plot",
    "concept_activation_bar", "saliency_overlay_plot",
    "attention_heatmap", "embedding_projection_plot",
    "importance_comparison_heatmap", "shap_model_agreement_scatter",
    "rashomon_importance_band",
]
