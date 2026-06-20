"""Classification analysis visualizations - static and interactive versions.

This sub-package covers a broad range of classification diagnostics:

* core confusion matrix, ROC and precision-recall curves;
* multiclass one-vs-rest ROC / PR plus model-comparison overlays;
* probability calibration (reliability curve, Brier scores, probability
  histograms and KDEs);
* threshold sweeps (precision / recall / F1 / accuracy / specificity vs.
  threshold, KS plot, DET curve, cost curve, decision-curve analysis);
* gain / lift / cumulative-accuracy-profile (CAP) charts;
* per-class report heatmap and grouped bars, class balance, prediction
  distribution per true class;
* normalized confusion matrix, confusion-matrix diff, error-analysis grid;
* per-class score distribution (violin / box / strip);
* 2-D decision boundary visualization for any callable classifier.

Every chart has a ``*_static`` (matplotlib) and a ``*_interactive`` (plotly)
implementation. Convenience aliases drop the suffix and default to the
static version.
"""

# Core
from .confusion_matrix import confusion_matrix_plot_static, confusion_matrix_plot_interactive
from .roc import roc_curve_static, roc_curve_interactive
from .pr_curve import precision_recall_curve_static, precision_recall_curve_interactive

# Multiclass / multi-model
from .multiclass import (
    multiclass_roc_curve_static, multiclass_roc_curve_interactive,
    multiclass_pr_curve_static, multiclass_pr_curve_interactive,
    roc_curve_comparison_static, roc_curve_comparison_interactive,
    pr_curve_comparison_static, pr_curve_comparison_interactive,
)

# Calibration
from .calibration import (
    calibration_curve_static, calibration_curve_interactive,
    probability_histogram_static, probability_histogram_interactive,
    probability_density_static, probability_density_interactive,
    brier_score_bar_static, brier_score_bar_interactive,
)

# Threshold diagnostics
from .threshold import (
    threshold_metric_curve_static, threshold_metric_curve_interactive,
    ks_statistic_plot_static, ks_statistic_plot_interactive,
    det_curve_static, det_curve_interactive,
    cost_curve_static, cost_curve_interactive,
    net_benefit_curve_static, net_benefit_curve_interactive,
)

# Gain / lift / CAP
from .gain_lift import (
    gain_chart_static, gain_chart_interactive,
    lift_chart_static, lift_chart_interactive,
    cumulative_accuracy_profile_static, cumulative_accuracy_profile_interactive,
)

# Per-class report
from .report import (
    classification_report_heatmap_static, classification_report_heatmap_interactive,
    per_class_metrics_bar_static, per_class_metrics_bar_interactive,
    class_balance_bar_static, class_balance_bar_interactive,
    prediction_distribution_static, prediction_distribution_interactive,
)

# Confusion-matrix extensions
from .confusion_extended import (
    normalized_confusion_matrix_static, normalized_confusion_matrix_interactive,
    confusion_matrix_diff_static, confusion_matrix_diff_interactive,
    error_analysis_grid_static, error_analysis_grid_interactive,
)

# Score distribution
from .score_dist import (
    score_distribution_by_class_static, score_distribution_by_class_interactive,
)

# Decision boundary
from .decision_boundary import (
    decision_boundary_plot_static, decision_boundary_plot_interactive,
)

# ---- Additional 36 chart families (72 functions) ----

# Threshold-curve extensions
from .threshold_extra import (
    f_beta_curve_static, f_beta_curve_interactive,
    mcc_curve_static, mcc_curve_interactive,
    youden_j_curve_static, youden_j_curve_interactive,
    balanced_accuracy_curve_static, balanced_accuracy_curve_interactive,
    cohen_kappa_curve_static, cohen_kappa_curve_interactive,
    likelihood_ratio_curve_static, likelihood_ratio_curve_interactive,
    predictive_value_curve_static, predictive_value_curve_interactive,
)

# Calibration extensions
from .calibration_extra import (
    multiclass_calibration_curve_static, multiclass_calibration_curve_interactive,
    calibration_with_confidence_static, calibration_with_confidence_interactive,
    platt_isotonic_overlay_static, platt_isotonic_overlay_interactive,
    sharpness_resolution_decomposition_static, sharpness_resolution_decomposition_interactive,
    score_ecdf_by_class_static, score_ecdf_by_class_interactive,
    score_qq_by_class_static, score_qq_by_class_interactive,
)

# Multiclass extensions
from .multiclass_extra import (
    per_class_auc_bar_static, per_class_auc_bar_interactive,
    per_class_ap_bar_static, per_class_ap_bar_interactive,
    top_k_accuracy_curve_static, top_k_accuracy_curve_interactive,
    confusion_sankey_static, confusion_sankey_interactive,
)

# Multilabel diagnostics
from .multilabel import (
    multilabel_confusion_grid_static, multilabel_confusion_grid_interactive,
    label_cooccurrence_heatmap_static, label_cooccurrence_heatmap_interactive,
    hamming_subset_accuracy_bar_static, hamming_subset_accuracy_bar_interactive,
)

# Fairness / segments
from .fairness import (
    per_segment_metric_bar_static, per_segment_metric_bar_interactive,
    fairness_disparity_heatmap_static, fairness_disparity_heatmap_interactive,
    segment_roc_overlay_static, segment_roc_overlay_interactive,
    segment_calibration_overlay_static, segment_calibration_overlay_interactive,
)

# Error / confidence diagnostics
from .errors import (
    confidence_by_correctness_histogram_static, confidence_by_correctness_histogram_interactive,
    discrimination_threshold_dashboard_static, discrimination_threshold_dashboard_interactive,
    misclassification_cluster_heatmap_static, misclassification_cluster_heatmap_interactive,
    loss_distribution_plot_static, loss_distribution_plot_interactive,
)

# Model comparison / monitoring
from .model_comparison import (
    metrics_radar_chart_static, metrics_radar_chart_interactive,
    pareto_tradeoff_bubble_static, pareto_tradeoff_bubble_interactive,
    critical_difference_diagram_static, critical_difference_diagram_interactive,
    score_distribution_drift_static, score_distribution_drift_interactive,
    psi_bar_static, psi_bar_interactive,
)

# Training diagnostics
from .training import (
    validation_curve_static, validation_curve_interactive,
    cv_score_boxplot_static, cv_score_boxplot_interactive,
    training_history_curve_static, training_history_curve_interactive,
)

# Convenience aliases (default to static)
confusion_matrix_plot = confusion_matrix_plot_static
roc_curve = roc_curve_static
precision_recall_curve = precision_recall_curve_static
multiclass_roc_curve = multiclass_roc_curve_static
multiclass_pr_curve = multiclass_pr_curve_static
roc_curve_comparison = roc_curve_comparison_static
pr_curve_comparison = pr_curve_comparison_static
calibration_curve = calibration_curve_static
probability_histogram = probability_histogram_static
probability_density = probability_density_static
brier_score_bar = brier_score_bar_static
threshold_metric_curve = threshold_metric_curve_static
ks_statistic_plot = ks_statistic_plot_static
det_curve = det_curve_static
cost_curve = cost_curve_static
net_benefit_curve = net_benefit_curve_static
gain_chart = gain_chart_static
lift_chart = lift_chart_static
cumulative_accuracy_profile = cumulative_accuracy_profile_static
classification_report_heatmap = classification_report_heatmap_static
per_class_metrics_bar = per_class_metrics_bar_static
class_balance_bar = class_balance_bar_static
prediction_distribution = prediction_distribution_static
normalized_confusion_matrix = normalized_confusion_matrix_static
confusion_matrix_diff = confusion_matrix_diff_static
error_analysis_grid = error_analysis_grid_static
score_distribution_by_class = score_distribution_by_class_static
decision_boundary_plot = decision_boundary_plot_static

# Aliases for 36 additional families
f_beta_curve = f_beta_curve_static
mcc_curve = mcc_curve_static
youden_j_curve = youden_j_curve_static
balanced_accuracy_curve = balanced_accuracy_curve_static
cohen_kappa_curve = cohen_kappa_curve_static
likelihood_ratio_curve = likelihood_ratio_curve_static
predictive_value_curve = predictive_value_curve_static
multiclass_calibration_curve = multiclass_calibration_curve_static
calibration_with_confidence = calibration_with_confidence_static
platt_isotonic_overlay = platt_isotonic_overlay_static
sharpness_resolution_decomposition = sharpness_resolution_decomposition_static
score_ecdf_by_class = score_ecdf_by_class_static
score_qq_by_class = score_qq_by_class_static
per_class_auc_bar = per_class_auc_bar_static
per_class_ap_bar = per_class_ap_bar_static
top_k_accuracy_curve = top_k_accuracy_curve_static
confusion_sankey = confusion_sankey_static
multilabel_confusion_grid = multilabel_confusion_grid_static
label_cooccurrence_heatmap = label_cooccurrence_heatmap_static
hamming_subset_accuracy_bar = hamming_subset_accuracy_bar_static
per_segment_metric_bar = per_segment_metric_bar_static
fairness_disparity_heatmap = fairness_disparity_heatmap_static
segment_roc_overlay = segment_roc_overlay_static
segment_calibration_overlay = segment_calibration_overlay_static
confidence_by_correctness_histogram = confidence_by_correctness_histogram_static
discrimination_threshold_dashboard = discrimination_threshold_dashboard_static
misclassification_cluster_heatmap = misclassification_cluster_heatmap_static
loss_distribution_plot = loss_distribution_plot_static
metrics_radar_chart = metrics_radar_chart_static
pareto_tradeoff_bubble = pareto_tradeoff_bubble_static
critical_difference_diagram = critical_difference_diagram_static
score_distribution_drift = score_distribution_drift_static
psi_bar = psi_bar_static
validation_curve = validation_curve_static
cv_score_boxplot = cv_score_boxplot_static
training_history_curve = training_history_curve_static

__all__ = [
    # Static
    "confusion_matrix_plot_static", "roc_curve_static", "precision_recall_curve_static",
    "multiclass_roc_curve_static", "multiclass_pr_curve_static",
    "roc_curve_comparison_static", "pr_curve_comparison_static",
    "calibration_curve_static", "probability_histogram_static",
    "probability_density_static", "brier_score_bar_static",
    "threshold_metric_curve_static", "ks_statistic_plot_static",
    "det_curve_static", "cost_curve_static", "net_benefit_curve_static",
    "gain_chart_static", "lift_chart_static", "cumulative_accuracy_profile_static",
    "classification_report_heatmap_static", "per_class_metrics_bar_static",
    "class_balance_bar_static", "prediction_distribution_static",
    "normalized_confusion_matrix_static", "confusion_matrix_diff_static",
    "error_analysis_grid_static", "score_distribution_by_class_static",
    "decision_boundary_plot_static",
    # Interactive
    "confusion_matrix_plot_interactive", "roc_curve_interactive",
    "precision_recall_curve_interactive", "multiclass_roc_curve_interactive",
    "multiclass_pr_curve_interactive", "roc_curve_comparison_interactive",
    "pr_curve_comparison_interactive", "calibration_curve_interactive",
    "probability_histogram_interactive", "probability_density_interactive",
    "brier_score_bar_interactive", "threshold_metric_curve_interactive",
    "ks_statistic_plot_interactive", "det_curve_interactive",
    "cost_curve_interactive", "net_benefit_curve_interactive",
    "gain_chart_interactive", "lift_chart_interactive",
    "cumulative_accuracy_profile_interactive",
    "classification_report_heatmap_interactive", "per_class_metrics_bar_interactive",
    "class_balance_bar_interactive", "prediction_distribution_interactive",
    "normalized_confusion_matrix_interactive", "confusion_matrix_diff_interactive",
    "error_analysis_grid_interactive", "score_distribution_by_class_interactive",
    "decision_boundary_plot_interactive",
    # Aliases
    "confusion_matrix_plot", "roc_curve", "precision_recall_curve",
    "multiclass_roc_curve", "multiclass_pr_curve",
    "roc_curve_comparison", "pr_curve_comparison",
    "calibration_curve", "probability_histogram", "probability_density",
    "brier_score_bar", "threshold_metric_curve", "ks_statistic_plot",
    "det_curve", "cost_curve", "net_benefit_curve",
    "gain_chart", "lift_chart", "cumulative_accuracy_profile",
    "classification_report_heatmap", "per_class_metrics_bar",
    "class_balance_bar", "prediction_distribution",
    "normalized_confusion_matrix", "confusion_matrix_diff",
    "error_analysis_grid", "score_distribution_by_class",
    "decision_boundary_plot",
    # New aliases (36)
    "f_beta_curve", "mcc_curve", "youden_j_curve", "balanced_accuracy_curve",
    "cohen_kappa_curve", "likelihood_ratio_curve", "predictive_value_curve",
    "multiclass_calibration_curve", "calibration_with_confidence",
    "platt_isotonic_overlay", "sharpness_resolution_decomposition",
    "score_ecdf_by_class", "score_qq_by_class",
    "per_class_auc_bar", "per_class_ap_bar", "top_k_accuracy_curve",
    "confusion_sankey",
    "multilabel_confusion_grid", "label_cooccurrence_heatmap",
    "hamming_subset_accuracy_bar",
    "per_segment_metric_bar", "fairness_disparity_heatmap",
    "segment_roc_overlay", "segment_calibration_overlay",
    "confidence_by_correctness_histogram",
    "discrimination_threshold_dashboard",
    "misclassification_cluster_heatmap", "loss_distribution_plot",
    "metrics_radar_chart", "pareto_tradeoff_bubble",
    "critical_difference_diagram", "score_distribution_drift", "psi_bar",
    "validation_curve", "cv_score_boxplot", "training_history_curve",
    # New static (36 families)
    "f_beta_curve_static", "mcc_curve_static", "youden_j_curve_static",
    "balanced_accuracy_curve_static", "cohen_kappa_curve_static",
    "likelihood_ratio_curve_static", "predictive_value_curve_static",
    "multiclass_calibration_curve_static", "calibration_with_confidence_static",
    "platt_isotonic_overlay_static", "sharpness_resolution_decomposition_static",
    "score_ecdf_by_class_static", "score_qq_by_class_static",
    "per_class_auc_bar_static", "per_class_ap_bar_static",
    "top_k_accuracy_curve_static", "confusion_sankey_static",
    "multilabel_confusion_grid_static", "label_cooccurrence_heatmap_static",
    "hamming_subset_accuracy_bar_static",
    "per_segment_metric_bar_static", "fairness_disparity_heatmap_static",
    "segment_roc_overlay_static", "segment_calibration_overlay_static",
    "confidence_by_correctness_histogram_static",
    "discrimination_threshold_dashboard_static",
    "misclassification_cluster_heatmap_static", "loss_distribution_plot_static",
    "metrics_radar_chart_static", "pareto_tradeoff_bubble_static",
    "critical_difference_diagram_static", "score_distribution_drift_static",
    "psi_bar_static",
    "validation_curve_static", "cv_score_boxplot_static",
    "training_history_curve_static",
    # New interactive (36 families)
    "f_beta_curve_interactive", "mcc_curve_interactive",
    "youden_j_curve_interactive", "balanced_accuracy_curve_interactive",
    "cohen_kappa_curve_interactive", "likelihood_ratio_curve_interactive",
    "predictive_value_curve_interactive",
    "multiclass_calibration_curve_interactive",
    "calibration_with_confidence_interactive",
    "platt_isotonic_overlay_interactive",
    "sharpness_resolution_decomposition_interactive",
    "score_ecdf_by_class_interactive", "score_qq_by_class_interactive",
    "per_class_auc_bar_interactive", "per_class_ap_bar_interactive",
    "top_k_accuracy_curve_interactive", "confusion_sankey_interactive",
    "multilabel_confusion_grid_interactive",
    "label_cooccurrence_heatmap_interactive",
    "hamming_subset_accuracy_bar_interactive",
    "per_segment_metric_bar_interactive",
    "fairness_disparity_heatmap_interactive",
    "segment_roc_overlay_interactive",
    "segment_calibration_overlay_interactive",
    "confidence_by_correctness_histogram_interactive",
    "discrimination_threshold_dashboard_interactive",
    "misclassification_cluster_heatmap_interactive",
    "loss_distribution_plot_interactive",
    "metrics_radar_chart_interactive", "pareto_tradeoff_bubble_interactive",
    "critical_difference_diagram_interactive",
    "score_distribution_drift_interactive", "psi_bar_interactive",
    "validation_curve_interactive", "cv_score_boxplot_interactive",
    "training_history_curve_interactive",
]
