"""Curated Complete-example snippets for dataviz.classification API pages."""

EXAMPLES = {
    'dataviz.classification.calibration.brier_score_bar_interactive': '''
import numpy as np
from dataviz.classification.calibration import brier_score_bar_interactive

scores = {"Logistic regression": 0.089, "Random forest": 0.076, "Gradient boosting": 0.081}

fig = brier_score_bar_interactive(scores)
fig.show()
''',

    'dataviz.classification.calibration.brier_score_bar_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.calibration import brier_score_bar_static

scores = {"Logistic regression": 0.089, "Random forest": 0.076, "Gradient boosting": 0.081}

ax = brier_score_bar_static(scores)
plt.show()
''',

    'dataviz.classification.calibration.calibration_curve_interactive': '''
import numpy as np
from dataviz.classification.calibration import calibration_curve_interactive

rng = np.random.default_rng(42)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)

fig = calibration_curve_interactive(y_true, y_prob)
fig.show()
''',

    'dataviz.classification.calibration.calibration_curve_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.calibration import calibration_curve_static

rng = np.random.default_rng(42)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)

ax = calibration_curve_static(y_true, y_prob)
plt.show()
''',

    'dataviz.classification.calibration.probability_density_interactive': '''
import numpy as np
from dataviz.classification.calibration import probability_density_interactive

rng = np.random.default_rng(42)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)

fig = probability_density_interactive(y_true, y_prob)
fig.show()
''',

    'dataviz.classification.calibration.probability_density_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.calibration import probability_density_static

rng = np.random.default_rng(42)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)

ax = probability_density_static(y_true, y_prob)
plt.show()
''',

    'dataviz.classification.calibration.probability_histogram_interactive': '''
import numpy as np
from dataviz.classification.calibration import probability_histogram_interactive

rng = np.random.default_rng(42)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)

fig = probability_histogram_interactive(y_true, y_prob)
fig.show()
''',

    'dataviz.classification.calibration.probability_histogram_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.calibration import probability_histogram_static

rng = np.random.default_rng(42)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)

ax = probability_histogram_static(y_true, y_prob)
plt.show()
''',

    'dataviz.classification.calibration_extra.calibration_with_confidence_interactive': '''
import numpy as np
from dataviz.classification.calibration_extra import calibration_with_confidence_interactive

rng = np.random.default_rng(42)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)

fig = calibration_with_confidence_interactive(y_true, y_prob)
fig.show()
''',

    'dataviz.classification.calibration_extra.calibration_with_confidence_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.calibration_extra import calibration_with_confidence_static

rng = np.random.default_rng(42)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)

ax = calibration_with_confidence_static(y_true, y_prob)
plt.show()
''',

    'dataviz.classification.calibration_extra.multiclass_calibration_curve_interactive': '''
import numpy as np
from dataviz.classification.calibration_extra import multiclass_calibration_curve_interactive

rng = np.random.default_rng(42)
logits = rng.normal(size=(200, 3))
exp_logits = np.exp(logits - logits.max(axis=1, keepdims=True))
y_prob_matrix = exp_logits / exp_logits.sum(axis=1, keepdims=True)
y_true = rng.choice(3, size=200, p=[0.4, 0.35, 0.25])

fig = multiclass_calibration_curve_interactive(y_true, y_prob_matrix, labels=["A", "B", "C"])
fig.show()
''',

    'dataviz.classification.calibration_extra.multiclass_calibration_curve_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.calibration_extra import multiclass_calibration_curve_static

rng = np.random.default_rng(42)
logits = rng.normal(size=(200, 3))
exp_logits = np.exp(logits - logits.max(axis=1, keepdims=True))
y_prob_matrix = exp_logits / exp_logits.sum(axis=1, keepdims=True)
y_true = rng.choice(3, size=200, p=[0.4, 0.35, 0.25])

ax = multiclass_calibration_curve_static(y_true, y_prob_matrix, labels=["A", "B", "C"])
plt.show()
''',

    'dataviz.classification.calibration_extra.platt_isotonic_overlay_interactive': '''
import numpy as np
from dataviz.classification.calibration_extra import platt_isotonic_overlay_interactive

rng = np.random.default_rng(42)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)

fig = platt_isotonic_overlay_interactive(y_true, y_prob)
fig.show()
''',

    'dataviz.classification.calibration_extra.platt_isotonic_overlay_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.calibration_extra import platt_isotonic_overlay_static

rng = np.random.default_rng(42)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)

ax = platt_isotonic_overlay_static(y_true, y_prob)
plt.show()
''',

    'dataviz.classification.calibration_extra.score_ecdf_by_class_interactive': '''
import numpy as np
from dataviz.classification.calibration_extra import score_ecdf_by_class_interactive

rng = np.random.default_rng(42)
y_score = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_score)

fig = score_ecdf_by_class_interactive(y_true, y_score)
fig.show()
''',

    'dataviz.classification.calibration_extra.score_ecdf_by_class_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.calibration_extra import score_ecdf_by_class_static

rng = np.random.default_rng(42)
y_score = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_score)

ax = score_ecdf_by_class_static(y_true, y_score)
plt.show()
''',

    'dataviz.classification.calibration_extra.score_qq_by_class_interactive': '''
import numpy as np
from dataviz.classification.calibration_extra import score_qq_by_class_interactive

rng = np.random.default_rng(42)
y_score = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_score)

fig = score_qq_by_class_interactive(y_true, y_score)
fig.show()
''',

    'dataviz.classification.calibration_extra.score_qq_by_class_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.calibration_extra import score_qq_by_class_static

rng = np.random.default_rng(42)
y_score = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_score)

ax = score_qq_by_class_static(y_true, y_score)
plt.show()
''',

    'dataviz.classification.calibration_extra.sharpness_resolution_decomposition_interactive': '''
import numpy as np
from dataviz.classification.calibration_extra import sharpness_resolution_decomposition_interactive

rng = np.random.default_rng(42)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)

fig = sharpness_resolution_decomposition_interactive(y_true, y_prob)
fig.show()
''',

    'dataviz.classification.calibration_extra.sharpness_resolution_decomposition_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.calibration_extra import sharpness_resolution_decomposition_static

rng = np.random.default_rng(42)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)

ax = sharpness_resolution_decomposition_static(y_true, y_prob)
plt.show()
''',

    'dataviz.classification.confusion_extended.confusion_matrix_diff_interactive': '''
import numpy as np
from dataviz.classification.confusion_extended import confusion_matrix_diff_interactive

cm_a = np.array([[32, 4], [5, 29]])
cm_b = np.array([[28, 8], [7, 27]])

fig = confusion_matrix_diff_interactive(cm_a, cm_b)
fig.show()
''',

    'dataviz.classification.confusion_extended.confusion_matrix_diff_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.confusion_extended import confusion_matrix_diff_static

cm_a = np.array([[32, 4], [5, 29]])
cm_b = np.array([[28, 8], [7, 27]])

ax = confusion_matrix_diff_static(cm_a, cm_b)
plt.show()
''',

    'dataviz.classification.decision_boundary.decision_boundary_plot_interactive': '''
import numpy as np
from dataviz.classification.decision_boundary import decision_boundary_plot_interactive

rng = np.random.default_rng(42)
x = rng.normal(size=120)
y = rng.normal(size=120)
labels = (x + y > 0).astype(int)

def predict_fn(points):
    return (points[:, 0] + points[:, 1] > 0).astype(int)

fig = decision_boundary_plot_interactive(x, y, labels, predict_fn, resolution=60)
fig.show()
''',

    'dataviz.classification.decision_boundary.decision_boundary_plot_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.decision_boundary import decision_boundary_plot_static

rng = np.random.default_rng(42)
x = rng.normal(size=120)
y = rng.normal(size=120)
labels = (x + y > 0).astype(int)

def predict_fn(points):
    return (points[:, 0] + points[:, 1] > 0).astype(int)

ax = decision_boundary_plot_static(x, y, labels, predict_fn, resolution=80)
plt.show()
''',

    'dataviz.classification.errors.confidence_by_correctness_histogram_interactive': '''
import numpy as np
from dataviz.classification.errors import confidence_by_correctness_histogram_interactive

rng = np.random.default_rng(42)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)

fig = confidence_by_correctness_histogram_interactive(y_true, y_prob)
fig.show()
''',

    'dataviz.classification.errors.confidence_by_correctness_histogram_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.errors import confidence_by_correctness_histogram_static

rng = np.random.default_rng(42)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)

ax = confidence_by_correctness_histogram_static(y_true, y_prob)
plt.show()
''',

    'dataviz.classification.errors.discrimination_threshold_dashboard_interactive': '''
import numpy as np
from dataviz.classification.errors import discrimination_threshold_dashboard_interactive

rng = np.random.default_rng(42)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)

fig = discrimination_threshold_dashboard_interactive(y_true, y_prob)
fig.show()
''',

    'dataviz.classification.errors.discrimination_threshold_dashboard_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.errors import discrimination_threshold_dashboard_static

rng = np.random.default_rng(42)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)

ax = discrimination_threshold_dashboard_static(y_true, y_prob)
plt.show()
''',

    'dataviz.classification.errors.loss_distribution_plot_interactive': '''
import numpy as np
from dataviz.classification.errors import loss_distribution_plot_interactive

rng = np.random.default_rng(42)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)

fig = loss_distribution_plot_interactive(y_true, y_prob)
fig.show()
''',

    'dataviz.classification.errors.loss_distribution_plot_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.errors import loss_distribution_plot_static

rng = np.random.default_rng(42)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)

ax = loss_distribution_plot_static(y_true, y_prob)
plt.show()
''',

    'dataviz.classification.errors.misclassification_cluster_heatmap_interactive': '''
import numpy as np
from dataviz.classification.errors import misclassification_cluster_heatmap_interactive

rng = np.random.default_rng(42)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)

fig = misclassification_cluster_heatmap_interactive(y_true, y_prob)
fig.show()
''',

    'dataviz.classification.errors.misclassification_cluster_heatmap_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.errors import misclassification_cluster_heatmap_static

rng = np.random.default_rng(42)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)

ax = misclassification_cluster_heatmap_static(y_true, y_prob)
plt.show()
''',

    'dataviz.classification.fairness.fairness_disparity_heatmap_interactive': '''
import numpy as np
from dataviz.classification.fairness import fairness_disparity_heatmap_interactive

rng = np.random.default_rng(42)
groups = rng.choice(["Group A", "Group B"], size=200)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)
y_pred = (y_prob > 0.3).astype(int)

fig = fairness_disparity_heatmap_interactive(y_true, y_pred, groups)
fig.show()
''',

    'dataviz.classification.fairness.fairness_disparity_heatmap_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.fairness import fairness_disparity_heatmap_static

rng = np.random.default_rng(42)
groups = rng.choice(["Group A", "Group B"], size=200)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)
y_pred = (y_prob > 0.3).astype(int)

ax = fairness_disparity_heatmap_static(y_true, y_pred, groups)
plt.show()
''',

    'dataviz.classification.fairness.per_segment_metric_bar_interactive': '''
import numpy as np
from dataviz.classification.fairness import per_segment_metric_bar_interactive

rng = np.random.default_rng(42)
groups = rng.choice(["Group A", "Group B"], size=200)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)
y_pred = (y_prob > 0.3).astype(int)

fig = per_segment_metric_bar_interactive(y_true, y_pred, groups)
fig.show()
''',

    'dataviz.classification.fairness.per_segment_metric_bar_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.fairness import per_segment_metric_bar_static

rng = np.random.default_rng(42)
groups = rng.choice(["Group A", "Group B"], size=200)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)
y_pred = (y_prob > 0.3).astype(int)

ax = per_segment_metric_bar_static(y_true, y_pred, groups)
plt.show()
''',

    'dataviz.classification.fairness.segment_calibration_overlay_interactive': '''
import numpy as np
from dataviz.classification.fairness import segment_calibration_overlay_interactive

rng = np.random.default_rng(42)
groups = rng.choice(["Group A", "Group B"], size=200)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)

fig = segment_calibration_overlay_interactive(y_true, y_prob, groups)
fig.show()
''',

    'dataviz.classification.fairness.segment_calibration_overlay_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.fairness import segment_calibration_overlay_static

rng = np.random.default_rng(42)
groups = rng.choice(["Group A", "Group B"], size=200)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)

ax = segment_calibration_overlay_static(y_true, y_prob, groups)
plt.show()
''',

    'dataviz.classification.fairness.segment_roc_overlay_interactive': '''
import numpy as np
from dataviz.classification.fairness import segment_roc_overlay_interactive

rng = np.random.default_rng(42)
groups = rng.choice(["Group A", "Group B"], size=200)
y_score = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_score)

fig = segment_roc_overlay_interactive(y_true, y_score, groups)
fig.show()
''',

    'dataviz.classification.fairness.segment_roc_overlay_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.fairness import segment_roc_overlay_static

rng = np.random.default_rng(42)
groups = rng.choice(["Group A", "Group B"], size=200)
y_score = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_score)

ax = segment_roc_overlay_static(y_true, y_score, groups)
plt.show()
''',

    'dataviz.classification.gain_lift.cumulative_accuracy_profile_interactive': '''
import numpy as np
from dataviz.classification.gain_lift import cumulative_accuracy_profile_interactive

rng = np.random.default_rng(42)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)

fig = cumulative_accuracy_profile_interactive(y_true, y_prob)
fig.show()
''',

    'dataviz.classification.gain_lift.cumulative_accuracy_profile_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.gain_lift import cumulative_accuracy_profile_static

rng = np.random.default_rng(42)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)

ax = cumulative_accuracy_profile_static(y_true, y_prob)
plt.show()
''',

    'dataviz.classification.gain_lift.gain_chart_interactive': '''
import numpy as np
from dataviz.classification.gain_lift import gain_chart_interactive

rng = np.random.default_rng(42)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)

fig = gain_chart_interactive(y_true, y_prob)
fig.show()
''',

    'dataviz.classification.gain_lift.gain_chart_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.gain_lift import gain_chart_static

rng = np.random.default_rng(42)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)

ax = gain_chart_static(y_true, y_prob)
plt.show()
''',

    'dataviz.classification.gain_lift.lift_chart_interactive': '''
import numpy as np
from dataviz.classification.gain_lift import lift_chart_interactive

rng = np.random.default_rng(42)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)

fig = lift_chart_interactive(y_true, y_prob)
fig.show()
''',

    'dataviz.classification.gain_lift.lift_chart_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.gain_lift import lift_chart_static

rng = np.random.default_rng(42)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)

ax = lift_chart_static(y_true, y_prob)
plt.show()
''',

    'dataviz.classification.model_comparison.critical_difference_diagram_interactive': '''
import numpy as np
from dataviz.classification.model_comparison import critical_difference_diagram_interactive

rank_table = {
    "Logistic regression": [2, 3, 1, 2, 3, 2],
    "Random forest": [1, 1, 2, 1, 1, 1],
    "Gradient boosting": [3, 2, 3, 3, 2, 3],
}

fig = critical_difference_diagram_interactive(rank_table, cd=1.2)
fig.show()
''',

    'dataviz.classification.model_comparison.critical_difference_diagram_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.model_comparison import critical_difference_diagram_static

rank_table = {
    "Logistic regression": [2, 3, 1, 2, 3, 2],
    "Random forest": [1, 1, 2, 1, 1, 1],
    "Gradient boosting": [3, 2, 3, 3, 2, 3],
}

ax = critical_difference_diagram_static(rank_table, cd=1.2)
plt.show()
''',

    'dataviz.classification.model_comparison.metrics_radar_chart_interactive': '''
import numpy as np
from dataviz.classification.model_comparison import metrics_radar_chart_interactive

metrics = {
    "Logistic regression": {"accuracy": 0.84, "precision": 0.81, "recall": 0.86, "f1": 0.83},
    "Random forest": {"accuracy": 0.89, "precision": 0.88, "recall": 0.90, "f1": 0.89},
    "Gradient boosting": {"accuracy": 0.87, "precision": 0.85, "recall": 0.89, "f1": 0.87},
}

fig = metrics_radar_chart_interactive(metrics)
fig.show()
''',

    'dataviz.classification.model_comparison.metrics_radar_chart_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.model_comparison import metrics_radar_chart_static

metrics = {
    "Logistic regression": {"accuracy": 0.84, "precision": 0.81, "recall": 0.86, "f1": 0.83},
    "Random forest": {"accuracy": 0.89, "precision": 0.88, "recall": 0.90, "f1": 0.89},
    "Gradient boosting": {"accuracy": 0.87, "precision": 0.85, "recall": 0.89, "f1": 0.87},
}

ax = metrics_radar_chart_static(metrics)
plt.show()
''',

    'dataviz.classification.model_comparison.pareto_tradeoff_bubble_interactive': '''
import numpy as np
from dataviz.classification.model_comparison import pareto_tradeoff_bubble_interactive

models = {
    "Logistic regression": {"precision": 0.81, "recall": 0.86, "auc": 0.90},
    "Random forest": {"precision": 0.88, "recall": 0.90, "auc": 0.95},
    "Gradient boosting": {"precision": 0.85, "recall": 0.89, "auc": 0.93},
    "k-NN": {"precision": 0.78, "recall": 0.80, "auc": 0.84},
}

fig = pareto_tradeoff_bubble_interactive(models)
fig.show()
''',

    'dataviz.classification.model_comparison.pareto_tradeoff_bubble_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.model_comparison import pareto_tradeoff_bubble_static

models = {
    "Logistic regression": {"precision": 0.81, "recall": 0.86, "auc": 0.90},
    "Random forest": {"precision": 0.88, "recall": 0.90, "auc": 0.95},
    "Gradient boosting": {"precision": 0.85, "recall": 0.89, "auc": 0.93},
    "k-NN": {"precision": 0.78, "recall": 0.80, "auc": 0.84},
}

ax = pareto_tradeoff_bubble_static(models)
plt.show()
''',

    'dataviz.classification.model_comparison.psi_bar_interactive': '''
import numpy as np
from dataviz.classification.model_comparison import psi_bar_interactive

rng = np.random.default_rng(42)
scores_reference = rng.beta(2.0, 5.0, size=400)
scores_current = rng.beta(2.5, 4.5, size=400)

fig = psi_bar_interactive(scores_reference, scores_current)
fig.show()
''',

    'dataviz.classification.model_comparison.psi_bar_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.model_comparison import psi_bar_static

rng = np.random.default_rng(42)
scores_reference = rng.beta(2.0, 5.0, size=400)
scores_current = rng.beta(2.5, 4.5, size=400)

ax = psi_bar_static(scores_reference, scores_current)
plt.show()
''',

    'dataviz.classification.model_comparison.score_distribution_drift_interactive': '''
import numpy as np
from dataviz.classification.model_comparison import score_distribution_drift_interactive

rng = np.random.default_rng(42)
scores_reference = rng.beta(2.0, 5.0, size=400)
scores_current = rng.beta(2.5, 4.5, size=400)

fig = score_distribution_drift_interactive(scores_reference, scores_current)
fig.show()
''',

    'dataviz.classification.model_comparison.score_distribution_drift_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.model_comparison import score_distribution_drift_static

rng = np.random.default_rng(42)
scores_reference = rng.beta(2.0, 5.0, size=400)
scores_current = rng.beta(2.5, 4.5, size=400)

ax = score_distribution_drift_static(scores_reference, scores_current)
plt.show()
''',

    'dataviz.classification.multiclass.multiclass_pr_curve_interactive': '''
import numpy as np
from dataviz.classification.multiclass import multiclass_pr_curve_interactive

curves = {
    "Class 0": (np.array([0.0, 0.5, 1.0]), np.array([0.9, 0.85, 0.6])),
    "Class 1": (np.array([0.0, 0.5, 1.0]), np.array([0.8, 0.7, 0.5])),
    "Class 2": (np.array([0.0, 0.5, 1.0]), np.array([0.7, 0.6, 0.4])),
}

fig = multiclass_pr_curve_interactive(curves)
fig.show()
''',

    'dataviz.classification.multiclass.multiclass_pr_curve_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.multiclass import multiclass_pr_curve_static

curves = {
    "Class 0": (np.array([0.0, 0.5, 1.0]), np.array([0.9, 0.85, 0.6])),
    "Class 1": (np.array([0.0, 0.5, 1.0]), np.array([0.8, 0.7, 0.5])),
    "Class 2": (np.array([0.0, 0.5, 1.0]), np.array([0.7, 0.6, 0.4])),
}

ax = multiclass_pr_curve_static(curves)
plt.show()
''',

    'dataviz.classification.multiclass.multiclass_roc_curve_interactive': '''
import numpy as np
from dataviz.classification.multiclass import multiclass_roc_curve_interactive

curves = {
    "Class 0": (np.array([0.0, 0.1, 0.3, 1.0]), np.array([0.0, 0.8, 0.9, 1.0])),
    "Class 1": (np.array([0.0, 0.2, 0.4, 1.0]), np.array([0.0, 0.6, 0.8, 1.0])),
    "Class 2": (np.array([0.0, 0.3, 0.5, 1.0]), np.array([0.0, 0.5, 0.75, 1.0])),
}

fig = multiclass_roc_curve_interactive(curves)
fig.show()
''',

    'dataviz.classification.multiclass.multiclass_roc_curve_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.multiclass import multiclass_roc_curve_static

curves = {
    "Class 0": (np.array([0.0, 0.1, 0.3, 1.0]), np.array([0.0, 0.8, 0.9, 1.0])),
    "Class 1": (np.array([0.0, 0.2, 0.4, 1.0]), np.array([0.0, 0.6, 0.8, 1.0])),
    "Class 2": (np.array([0.0, 0.3, 0.5, 1.0]), np.array([0.0, 0.5, 0.75, 1.0])),
}

ax = multiclass_roc_curve_static(curves)
plt.show()
''',

    'dataviz.classification.multiclass.pr_curve_comparison_interactive': '''
import numpy as np
from dataviz.classification.multiclass import pr_curve_comparison_interactive

models = {
    "Logistic regression": (np.array([0.0, 0.5, 1.0]), np.array([0.85, 0.8, 0.55])),
    "Random forest": (np.array([0.0, 0.5, 1.0]), np.array([0.9, 0.88, 0.65])),
    "Gradient boosting": (np.array([0.0, 0.5, 1.0]), np.array([0.88, 0.84, 0.6])),
}

fig = pr_curve_comparison_interactive(models)
fig.show()
''',

    'dataviz.classification.multiclass.pr_curve_comparison_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.multiclass import pr_curve_comparison_static

models = {
    "Logistic regression": (np.array([0.0, 0.5, 1.0]), np.array([0.85, 0.8, 0.55])),
    "Random forest": (np.array([0.0, 0.5, 1.0]), np.array([0.9, 0.88, 0.65])),
    "Gradient boosting": (np.array([0.0, 0.5, 1.0]), np.array([0.88, 0.84, 0.6])),
}

ax = pr_curve_comparison_static(models)
plt.show()
''',

    'dataviz.classification.multiclass.roc_curve_comparison_interactive': '''
import numpy as np
from dataviz.classification.multiclass import roc_curve_comparison_interactive

models = {
    "Logistic regression": (np.array([0.0, 0.1, 0.3, 1.0]), np.array([0.0, 0.7, 0.9, 1.0])),
    "Random forest": (np.array([0.0, 0.05, 0.2, 1.0]), np.array([0.0, 0.8, 0.95, 1.0])),
    "Gradient boosting": (np.array([0.0, 0.08, 0.25, 1.0]), np.array([0.0, 0.75, 0.92, 1.0])),
}

fig = roc_curve_comparison_interactive(models)
fig.show()
''',

    'dataviz.classification.multiclass.roc_curve_comparison_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.multiclass import roc_curve_comparison_static

models = {
    "Logistic regression": (np.array([0.0, 0.1, 0.3, 1.0]), np.array([0.0, 0.7, 0.9, 1.0])),
    "Random forest": (np.array([0.0, 0.05, 0.2, 1.0]), np.array([0.0, 0.8, 0.95, 1.0])),
    "Gradient boosting": (np.array([0.0, 0.08, 0.25, 1.0]), np.array([0.0, 0.75, 0.92, 1.0])),
}

ax = roc_curve_comparison_static(models)
plt.show()
''',

    'dataviz.classification.multiclass_extra.per_class_ap_bar_interactive': '''
import numpy as np
from dataviz.classification.multiclass_extra import per_class_ap_bar_interactive

ap_per_class = {"Class 0": 0.88, "Class 1": 0.79, "Class 2": 0.71}

fig = per_class_ap_bar_interactive(ap_per_class)
fig.show()
''',

    'dataviz.classification.multiclass_extra.per_class_ap_bar_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.multiclass_extra import per_class_ap_bar_static

ap_per_class = {"Class 0": 0.88, "Class 1": 0.79, "Class 2": 0.71}

ax = per_class_ap_bar_static(ap_per_class)
plt.show()
''',

    'dataviz.classification.multiclass_extra.per_class_auc_bar_interactive': '''
import numpy as np
from dataviz.classification.multiclass_extra import per_class_auc_bar_interactive

auc_per_class = {"Class 0": 0.92, "Class 1": 0.85, "Class 2": 0.78}

fig = per_class_auc_bar_interactive(auc_per_class)
fig.show()
''',

    'dataviz.classification.multiclass_extra.per_class_auc_bar_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.multiclass_extra import per_class_auc_bar_static

auc_per_class = {"Class 0": 0.92, "Class 1": 0.85, "Class 2": 0.78}

ax = per_class_auc_bar_static(auc_per_class)
plt.show()
''',

    'dataviz.classification.multiclass_extra.top_k_accuracy_curve_interactive': '''
import numpy as np
from dataviz.classification.multiclass_extra import top_k_accuracy_curve_interactive

rng = np.random.default_rng(42)
logits = rng.normal(size=(200, 4))
exp_logits = np.exp(logits - logits.max(axis=1, keepdims=True))
y_prob_matrix = exp_logits / exp_logits.sum(axis=1, keepdims=True)
y_true = rng.choice(4, size=200)

fig = top_k_accuracy_curve_interactive(y_true, y_prob_matrix)
fig.show()
''',

    'dataviz.classification.multiclass_extra.top_k_accuracy_curve_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.multiclass_extra import top_k_accuracy_curve_static

rng = np.random.default_rng(42)
logits = rng.normal(size=(200, 4))
exp_logits = np.exp(logits - logits.max(axis=1, keepdims=True))
y_prob_matrix = exp_logits / exp_logits.sum(axis=1, keepdims=True)
y_true = rng.choice(4, size=200)

ax = top_k_accuracy_curve_static(y_true, y_prob_matrix)
plt.show()
''',

    'dataviz.classification.multilabel.hamming_subset_accuracy_bar_interactive': '''
import numpy as np
from dataviz.classification.multilabel import hamming_subset_accuracy_bar_interactive

rng = np.random.default_rng(42)
Y_true = rng.binomial(1, 0.4, size=(120, 4))
Y_pred = rng.binomial(1, 0.4, size=(120, 4))

fig = hamming_subset_accuracy_bar_interactive(Y_true, Y_pred)
fig.show()
''',

    'dataviz.classification.multilabel.hamming_subset_accuracy_bar_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.multilabel import hamming_subset_accuracy_bar_static

rng = np.random.default_rng(42)
Y_true = rng.binomial(1, 0.4, size=(120, 4))
Y_pred = rng.binomial(1, 0.4, size=(120, 4))

ax = hamming_subset_accuracy_bar_static(Y_true, Y_pred)
plt.show()
''',

    'dataviz.classification.multilabel.multilabel_confusion_grid_interactive': '''
import numpy as np
from dataviz.classification.multilabel import multilabel_confusion_grid_interactive

rng = np.random.default_rng(42)
Y_true = rng.binomial(1, 0.4, size=(120, 4))
Y_pred = rng.binomial(1, 0.4, size=(120, 4))

fig = multilabel_confusion_grid_interactive(Y_true, Y_pred, labels=["sports", "tech", "politics", "health"])
fig.show()
''',

    'dataviz.classification.multilabel.multilabel_confusion_grid_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.multilabel import multilabel_confusion_grid_static

rng = np.random.default_rng(42)
Y_true = rng.binomial(1, 0.4, size=(120, 4))
Y_pred = rng.binomial(1, 0.4, size=(120, 4))

ax = multilabel_confusion_grid_static(Y_true, Y_pred, labels=["sports", "tech", "politics", "health"])
plt.show()
''',

    'dataviz.classification.score_dist.score_distribution_by_class_interactive': '''
import numpy as np
from dataviz.classification.score_dist import score_distribution_by_class_interactive

rng = np.random.default_rng(42)
y_score = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_score)

fig = score_distribution_by_class_interactive(y_true, y_score)
fig.show()
''',

    'dataviz.classification.score_dist.score_distribution_by_class_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.score_dist import score_distribution_by_class_static

rng = np.random.default_rng(42)
y_score = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_score)

ax = score_distribution_by_class_static(y_true, y_score)
plt.show()
''',

    'dataviz.classification.threshold.cost_curve_interactive': '''
import numpy as np
from dataviz.classification.threshold import cost_curve_interactive

rng = np.random.default_rng(42)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)

fig = cost_curve_interactive(y_true, y_prob)
fig.show()
''',

    'dataviz.classification.threshold.cost_curve_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.threshold import cost_curve_static

rng = np.random.default_rng(42)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)

ax = cost_curve_static(y_true, y_prob)
plt.show()
''',

    'dataviz.classification.threshold.det_curve_interactive': '''
import numpy as np
from dataviz.classification.threshold import det_curve_interactive

rng = np.random.default_rng(42)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)

fig = det_curve_interactive(y_true, y_prob)
fig.show()
''',

    'dataviz.classification.threshold.det_curve_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.threshold import det_curve_static

rng = np.random.default_rng(42)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)

ax = det_curve_static(y_true, y_prob)
plt.show()
''',

    'dataviz.classification.threshold.ks_statistic_plot_interactive': '''
import numpy as np
from dataviz.classification.threshold import ks_statistic_plot_interactive

rng = np.random.default_rng(42)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)

fig = ks_statistic_plot_interactive(y_true, y_prob)
fig.show()
''',

    'dataviz.classification.threshold.ks_statistic_plot_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.threshold import ks_statistic_plot_static

rng = np.random.default_rng(42)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)

ax = ks_statistic_plot_static(y_true, y_prob)
plt.show()
''',

    'dataviz.classification.threshold.net_benefit_curve_interactive': '''
import numpy as np
from dataviz.classification.threshold import net_benefit_curve_interactive

rng = np.random.default_rng(42)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)

fig = net_benefit_curve_interactive(y_true, y_prob)
fig.show()
''',

    'dataviz.classification.threshold.net_benefit_curve_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.threshold import net_benefit_curve_static

rng = np.random.default_rng(42)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)

ax = net_benefit_curve_static(y_true, y_prob)
plt.show()
''',

    'dataviz.classification.threshold.threshold_metric_curve_interactive': '''
import numpy as np
from dataviz.classification.threshold import threshold_metric_curve_interactive

rng = np.random.default_rng(42)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)

fig = threshold_metric_curve_interactive(y_true, y_prob)
fig.show()
''',

    'dataviz.classification.threshold.threshold_metric_curve_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.threshold import threshold_metric_curve_static

rng = np.random.default_rng(42)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)

ax = threshold_metric_curve_static(y_true, y_prob)
plt.show()
''',

    'dataviz.classification.threshold_extra.balanced_accuracy_curve_interactive': '''
import numpy as np
from dataviz.classification.threshold_extra import balanced_accuracy_curve_interactive

rng = np.random.default_rng(42)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)

fig = balanced_accuracy_curve_interactive(y_true, y_prob)
fig.show()
''',

    'dataviz.classification.threshold_extra.balanced_accuracy_curve_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.threshold_extra import balanced_accuracy_curve_static

rng = np.random.default_rng(42)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)

ax = balanced_accuracy_curve_static(y_true, y_prob)
plt.show()
''',

    'dataviz.classification.threshold_extra.cohen_kappa_curve_interactive': '''
import numpy as np
from dataviz.classification.threshold_extra import cohen_kappa_curve_interactive

rng = np.random.default_rng(42)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)

fig = cohen_kappa_curve_interactive(y_true, y_prob)
fig.show()
''',

    'dataviz.classification.threshold_extra.cohen_kappa_curve_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.threshold_extra import cohen_kappa_curve_static

rng = np.random.default_rng(42)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)

ax = cohen_kappa_curve_static(y_true, y_prob)
plt.show()
''',

    'dataviz.classification.threshold_extra.f_beta_curve_interactive': '''
import numpy as np
from dataviz.classification.threshold_extra import f_beta_curve_interactive

rng = np.random.default_rng(42)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)

fig = f_beta_curve_interactive(y_true, y_prob)
fig.show()
''',

    'dataviz.classification.threshold_extra.f_beta_curve_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.threshold_extra import f_beta_curve_static

rng = np.random.default_rng(42)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)

ax = f_beta_curve_static(y_true, y_prob)
plt.show()
''',

    'dataviz.classification.threshold_extra.likelihood_ratio_curve_interactive': '''
import numpy as np
from dataviz.classification.threshold_extra import likelihood_ratio_curve_interactive

rng = np.random.default_rng(42)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)

fig = likelihood_ratio_curve_interactive(y_true, y_prob)
fig.show()
''',

    'dataviz.classification.threshold_extra.likelihood_ratio_curve_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.threshold_extra import likelihood_ratio_curve_static

rng = np.random.default_rng(42)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)

ax = likelihood_ratio_curve_static(y_true, y_prob)
plt.show()
''',

    'dataviz.classification.threshold_extra.mcc_curve_interactive': '''
import numpy as np
from dataviz.classification.threshold_extra import mcc_curve_interactive

rng = np.random.default_rng(42)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)

fig = mcc_curve_interactive(y_true, y_prob)
fig.show()
''',

    'dataviz.classification.threshold_extra.mcc_curve_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.threshold_extra import mcc_curve_static

rng = np.random.default_rng(42)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)

ax = mcc_curve_static(y_true, y_prob)
plt.show()
''',

    'dataviz.classification.threshold_extra.predictive_value_curve_interactive': '''
import numpy as np
from dataviz.classification.threshold_extra import predictive_value_curve_interactive

prevalences = np.linspace(0.01, 0.5, 25)

fig = predictive_value_curve_interactive(0.85, 0.90, prevalences=prevalences)
fig.show()
''',

    'dataviz.classification.threshold_extra.predictive_value_curve_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.threshold_extra import predictive_value_curve_static

prevalences = np.linspace(0.01, 0.5, 25)

ax = predictive_value_curve_static(0.85, 0.90, prevalences=prevalences)
plt.show()
''',

    'dataviz.classification.threshold_extra.youden_j_curve_interactive': '''
import numpy as np
from dataviz.classification.threshold_extra import youden_j_curve_interactive

rng = np.random.default_rng(42)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)

fig = youden_j_curve_interactive(y_true, y_prob)
fig.show()
''',

    'dataviz.classification.threshold_extra.youden_j_curve_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.threshold_extra import youden_j_curve_static

rng = np.random.default_rng(42)
y_prob = rng.beta(2.0, 5.0, size=200)
y_true = rng.binomial(1, y_prob)

ax = youden_j_curve_static(y_true, y_prob)
plt.show()
''',

    'dataviz.classification.training.cv_score_boxplot_interactive': '''
import numpy as np
from dataviz.classification.training import cv_score_boxplot_interactive

cv_scores = {
    "Logistic regression": [0.81, 0.83, 0.80, 0.82, 0.84],
    "Random forest": [0.87, 0.89, 0.88, 0.86, 0.90],
    "Gradient boosting": [0.85, 0.87, 0.86, 0.88, 0.87],
}

fig = cv_score_boxplot_interactive(cv_scores)
fig.show()
''',

    'dataviz.classification.training.cv_score_boxplot_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.training import cv_score_boxplot_static

cv_scores = {
    "Logistic regression": [0.81, 0.83, 0.80, 0.82, 0.84],
    "Random forest": [0.87, 0.89, 0.88, 0.86, 0.90],
    "Gradient boosting": [0.85, 0.87, 0.86, 0.88, 0.87],
}

ax = cv_score_boxplot_static(cv_scores)
plt.show()
''',

    'dataviz.classification.training.training_history_curve_interactive': '''
import numpy as np
from dataviz.classification.training import training_history_curve_interactive

history = {
    "loss": [0.90, 0.62, 0.45, 0.36, 0.30, 0.27],
    "val_loss": [0.95, 0.70, 0.55, 0.50, 0.51, 0.53],
}

fig = training_history_curve_interactive(history)
fig.show()
''',

    'dataviz.classification.training.training_history_curve_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.training import training_history_curve_static

history = {
    "loss": [0.90, 0.62, 0.45, 0.36, 0.30, 0.27],
    "val_loss": [0.95, 0.70, 0.55, 0.50, 0.51, 0.53],
}

ax = training_history_curve_static(history)
plt.show()
''',

    'dataviz.classification.training.validation_curve_interactive': '''
import numpy as np
from dataviz.classification.training import validation_curve_interactive

param_values = np.array([0.001, 0.01, 0.1, 1.0, 10.0, 100.0])
train_scores = np.array([0.78, 0.82, 0.88, 0.93, 0.97, 0.99])
val_scores = np.array([0.77, 0.81, 0.86, 0.87, 0.84, 0.80])

fig = validation_curve_interactive(param_values, train_scores, val_scores, param_name="C")
fig.show()
''',

    'dataviz.classification.training.validation_curve_static': '''
import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.training import validation_curve_static

param_values = np.array([0.001, 0.01, 0.1, 1.0, 10.0, 100.0])
train_scores = np.array([0.78, 0.82, 0.88, 0.93, 0.97, 0.99])
val_scores = np.array([0.77, 0.81, 0.86, 0.87, 0.84, 0.80])

ax = validation_curve_static(param_values, train_scores, val_scores, param_name="C")
plt.show()
''',
}
