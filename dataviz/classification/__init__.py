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
]
