"""Curated rich examples for classification member pages."""

EXAMPLES = {
    # --- calibration.py -----------------------------------------------------
    "dataviz.classification.calibration.calibration_curve_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.calibration import calibration_curve_static

rng = np.random.default_rng(42)
n = 160
churn_risk = rng.normal(5.0, 1.5, n)
y_prob = 1.0 / (1.0 + np.exp(-(churn_risk - 5.0)))
y_true = (rng.uniform(size=n) < np.clip(y_prob + 0.08, 0, 1)).astype(int)

ax = calibration_curve_static(
    y_true, y_prob, n_bins=8, strategy="quantile",
    title="Telco churn model: reliability diagram",
)
ax.set_xlabel("Predicted churn probability")
plt.show()''',
    "dataviz.classification.calibration.calibration_curve_interactive": '''import numpy as np
from dataviz.classification.calibration import calibration_curve_interactive

rng = np.random.default_rng(42)
n = 160
churn_risk = rng.normal(5.0, 1.5, n)
y_prob = 1.0 / (1.0 + np.exp(-(churn_risk - 5.0)))
y_true = (rng.uniform(size=n) < np.clip(y_prob + 0.08, 0, 1)).astype(int)

fig = calibration_curve_interactive(
    y_true, y_prob, n_bins=8, strategy="quantile",
    title="Telco churn model: reliability diagram",
)
fig.show()''',
    "dataviz.classification.calibration.probability_histogram_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.calibration import probability_histogram_static

rng = np.random.default_rng(7)
n_fraud, n_legit = 40, 120
y_true = np.concatenate([np.ones(n_fraud, int), np.zeros(n_legit, int)])
y_prob = np.concatenate([
    np.clip(rng.normal(0.72, 0.18, n_fraud), 0.01, 0.99),
    np.clip(rng.normal(0.18, 0.12, n_legit), 0.01, 0.99),
])

ax = probability_histogram_static(
    y_true, y_prob, bins=25,
    title="Card fraud detector: score separation by class",
    positive_label="fraud", negative_label="legitimate",
)
ax.set_ylabel("Number of transactions")
plt.show()''',
    "dataviz.classification.calibration.probability_histogram_interactive": '''import numpy as np
from dataviz.classification.calibration import probability_histogram_interactive

rng = np.random.default_rng(7)
n_fraud, n_legit = 40, 120
y_true = np.concatenate([np.ones(n_fraud, int), np.zeros(n_legit, int)])
y_prob = np.concatenate([
    np.clip(rng.normal(0.72, 0.18, n_fraud), 0.01, 0.99),
    np.clip(rng.normal(0.18, 0.12, n_legit), 0.01, 0.99),
])

fig = probability_histogram_interactive(
    y_true, y_prob, bins=25,
    title="Card fraud detector: score separation by class",
)
fig.show()''',
    "dataviz.classification.calibration.probability_density_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.calibration import probability_density_static

rng = np.random.default_rng(11)
n_pos, n_neg = 50, 100
y_true = np.concatenate([np.ones(n_pos, int), np.zeros(n_neg, int)])
y_prob = np.concatenate([
    np.clip(rng.beta(6, 2, n_pos), 0.01, 0.99),
    np.clip(rng.beta(2, 6, n_neg), 0.01, 0.99),
])

ax = probability_density_static(
    y_true, y_prob, bandwidth=0.08,
    title="Diabetes screening test: probability density by outcome",
)
plt.show()''',
    "dataviz.classification.calibration.probability_density_interactive": '''import numpy as np
from dataviz.classification.calibration import probability_density_interactive

rng = np.random.default_rng(11)
n_pos, n_neg = 50, 100
y_true = np.concatenate([np.ones(n_pos, int), np.zeros(n_neg, int)])
y_prob = np.concatenate([
    np.clip(rng.beta(6, 2, n_pos), 0.01, 0.99),
    np.clip(rng.beta(2, 6, n_neg), 0.01, 0.99),
])

fig = probability_density_interactive(
    y_true, y_prob, bandwidth=0.08,
    title="Diabetes screening test: probability density by outcome",
)
fig.show()''',
    "dataviz.classification.calibration.brier_score_bar_static": '''import matplotlib.pyplot as plt
from dataviz.classification.calibration import brier_score_bar_static

scores = {
    "Logistic regression": 0.142,
    "Random forest": 0.118,
    "Gradient boosting": 0.105,
    "Naive base rate": 0.210,
}

ax = brier_score_bar_static(
    scores, title="Churn models: Brier score on Q4 holdout",
)
ax.set_ylim(0, 0.25)
plt.show()''',
    "dataviz.classification.calibration.brier_score_bar_interactive": '''from dataviz.classification.calibration import brier_score_bar_interactive

scores = {
    "Logistic regression": 0.142,
    "Random forest": 0.118,
    "Gradient boosting": 0.105,
    "Naive base rate": 0.210,
}

fig = brier_score_bar_interactive(
    scores, title="Churn models: Brier score on Q4 holdout",
)
fig.show()''',
    # --- calibration_extra.py -----------------------------------------------
    "dataviz.classification.calibration_extra.multiclass_calibration_curve_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.calibration_extra import (
    multiclass_calibration_curve_static,
)

rng = np.random.default_rng(3)
n = 180
y_true = rng.choice(3, size=n, p=[0.5, 0.3, 0.2])
logits = rng.normal(0, 1.0, (n, 3))
logits[np.arange(n), y_true] += 2.0
y_prob_matrix = np.exp(logits) / np.exp(logits).sum(axis=1, keepdims=True)

axes = multiclass_calibration_curve_static(
    y_true, y_prob_matrix,
    labels=["standard", "premium", "enterprise"], n_bins=6,
    title="Subscription tier classifier: per-class calibration",
)
plt.show()''',
    "dataviz.classification.calibration_extra.multiclass_calibration_curve_interactive": '''import numpy as np
from dataviz.classification.calibration_extra import (
    multiclass_calibration_curve_interactive,
)

rng = np.random.default_rng(3)
n = 180
y_true = rng.choice(3, size=n, p=[0.5, 0.3, 0.2])
logits = rng.normal(0, 1.0, (n, 3))
logits[np.arange(n), y_true] += 2.0
y_prob_matrix = np.exp(logits) / np.exp(logits).sum(axis=1, keepdims=True)

fig = multiclass_calibration_curve_interactive(
    y_true, y_prob_matrix,
    labels=["standard", "premium", "enterprise"], n_bins=6,
    title="Subscription tier classifier: per-class calibration",
)
fig.show()''',
    "dataviz.classification.calibration_extra.calibration_with_confidence_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.calibration_extra import (
    calibration_with_confidence_static,
)

rng = np.random.default_rng(21)
n = 140
y_prob = np.clip(rng.beta(2, 3, n), 0.01, 0.99)
y_true = (rng.uniform(size=n) < y_prob).astype(int)

ax = calibration_with_confidence_static(
    y_true, y_prob, n_bins=8, n_bootstrap=200, ci=0.90,
    title="Loan default model: calibration with 90% bootstrap CI",
    random_state=42,
)
plt.show()''',
    "dataviz.classification.calibration_extra.calibration_with_confidence_interactive": '''import numpy as np
from dataviz.classification.calibration_extra import (
    calibration_with_confidence_interactive,
)

rng = np.random.default_rng(21)
n = 140
y_prob = np.clip(rng.beta(2, 3, n), 0.01, 0.99)
y_true = (rng.uniform(size=n) < y_prob).astype(int)

fig = calibration_with_confidence_interactive(
    y_true, y_prob, n_bins=8, n_bootstrap=200, ci=0.90,
    title="Loan default model: calibration with 90% bootstrap CI",
    random_state=42,
)
fig.show()''',
    "dataviz.classification.calibration_extra.platt_isotonic_overlay_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.calibration_extra import platt_isotonic_overlay_static

rng = np.random.default_rng(5)
n = 150
signal = rng.normal(0, 1.5, n)
y_true = (signal + rng.normal(0, 0.8, n) > 0).astype(int)
y_prob = 1.0 / (1.0 + np.exp(-2.5 * signal))  # over-confident raw scores
y_prob = np.clip(y_prob, 1e-4, 1 - 1e-4)

ax = platt_isotonic_overlay_static(
    y_true, y_prob, n_bins=10,
    title="SVM spam filter: Platt vs isotonic recalibration",
)
plt.show()''',
    "dataviz.classification.calibration_extra.platt_isotonic_overlay_interactive": '''import numpy as np
from dataviz.classification.calibration_extra import (
    platt_isotonic_overlay_interactive,
)

rng = np.random.default_rng(5)
n = 150
signal = rng.normal(0, 1.5, n)
y_true = (signal + rng.normal(0, 0.8, n) > 0).astype(int)
y_prob = 1.0 / (1.0 + np.exp(-2.5 * signal))  # over-confident raw scores
y_prob = np.clip(y_prob, 1e-4, 1 - 1e-4)

fig = platt_isotonic_overlay_interactive(
    y_true, y_prob, n_bins=10,
    title="SVM spam filter: Platt vs isotonic recalibration",
)
fig.show()''',
    "dataviz.classification.calibration_extra.sharpness_resolution_decomposition_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.calibration_extra import (
    sharpness_resolution_decomposition_static,
)

rng = np.random.default_rng(9)
n = 160
y_prob = np.clip(rng.beta(2.5, 2.5, n), 0.01, 0.99)
y_true = (rng.uniform(size=n) < y_prob).astype(int)

ax = sharpness_resolution_decomposition_static(
    y_true, y_prob, n_bins=8,
    title="Readmission risk model: Murphy decomposition of Brier score",
)
plt.show()''',
    "dataviz.classification.calibration_extra.sharpness_resolution_decomposition_interactive": '''import numpy as np
from dataviz.classification.calibration_extra import (
    sharpness_resolution_decomposition_interactive,
)

rng = np.random.default_rng(9)
n = 160
y_prob = np.clip(rng.beta(2.5, 2.5, n), 0.01, 0.99)
y_true = (rng.uniform(size=n) < y_prob).astype(int)

fig = sharpness_resolution_decomposition_interactive(
    y_true, y_prob, n_bins=8,
    title="Readmission risk model: Murphy decomposition of Brier score",
)
fig.show()''',
    "dataviz.classification.calibration_extra.score_ecdf_by_class_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.calibration_extra import score_ecdf_by_class_static

rng = np.random.default_rng(13)
n_pos, n_neg = 45, 110
y_true = np.concatenate([np.ones(n_pos, int), np.zeros(n_neg, int)])
y_score = np.concatenate([
    rng.normal(0.65, 0.15, n_pos),
    rng.normal(0.30, 0.14, n_neg),
]).clip(0.01, 0.99)

ax = score_ecdf_by_class_static(
    y_true, y_score, labels=[0, 1],
    title="Defect detection: score ECDF for OK vs defective parts",
)
plt.show()''',
    "dataviz.classification.calibration_extra.score_ecdf_by_class_interactive": '''import numpy as np
from dataviz.classification.calibration_extra import (
    score_ecdf_by_class_interactive,
)

rng = np.random.default_rng(13)
n_pos, n_neg = 45, 110
y_true = np.concatenate([np.ones(n_pos, int), np.zeros(n_neg, int)])
y_score = np.concatenate([
    rng.normal(0.65, 0.15, n_pos),
    rng.normal(0.30, 0.14, n_neg),
]).clip(0.01, 0.99)

fig = score_ecdf_by_class_interactive(
    y_true, y_score, labels=[0, 1],
    title="Defect detection: score ECDF for OK vs defective parts",
)
fig.show()''',
    "dataviz.classification.calibration_extra.score_qq_by_class_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.calibration_extra import score_qq_by_class_static

rng = np.random.default_rng(17)
n_pos, n_neg = 50, 100
y_true = np.concatenate([np.ones(n_pos, int), np.zeros(n_neg, int)])
y_score = np.concatenate([
    rng.beta(5, 3, n_pos),
    rng.beta(3, 5, n_neg),
]).clip(0.01, 0.99)

ax = score_qq_by_class_static(
    y_true, y_score, labels=[0, 1], n_quantiles=30,
    title="Credit approval model: score Q-Q vs uniform by class",
)
plt.show()''',
    "dataviz.classification.calibration_extra.score_qq_by_class_interactive": '''import numpy as np
from dataviz.classification.calibration_extra import (
    score_qq_by_class_interactive,
)

rng = np.random.default_rng(17)
n_pos, n_neg = 50, 100
y_true = np.concatenate([np.ones(n_pos, int), np.zeros(n_neg, int)])
y_score = np.concatenate([
    rng.beta(5, 3, n_pos),
    rng.beta(3, 5, n_neg),
]).clip(0.01, 0.99)

fig = score_qq_by_class_interactive(
    y_true, y_score, labels=[0, 1], n_quantiles=30,
    title="Credit approval model: score Q-Q vs uniform by class",
)
fig.show()''',
    # --- charts.py ----------------------------------------------------------
    "dataviz.classification.charts.confusion_matrix_plot": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.charts import confusion_matrix_plot

rng = np.random.default_rng(42)
n = 150
true_labels = rng.choice(3, size=n, p=[0.5, 0.3, 0.2])
pred_labels = true_labels.copy()
flip = rng.uniform(size=n) < 0.18
pred_labels[flip] = rng.choice(3, size=int(flip.sum()))
classes = ["retained", "at-risk", "churned"]
cm = np.zeros((3, 3), dtype=int)
for t, p in zip(true_labels, pred_labels):
    cm[t, p] += 1

ax = confusion_matrix_plot(
    cm, labels=classes, title="Customer retention model: confusion matrix",
)
plt.show()''',
    "dataviz.classification.charts.roc_curve": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.charts import roc_curve

rng = np.random.default_rng(42)
n_pos, n_neg = 50, 110
y_true = np.concatenate([np.ones(n_pos, int), np.zeros(n_neg, int)])
y_score = np.concatenate([
    rng.normal(0.68, 0.16, n_pos),
    rng.normal(0.32, 0.16, n_neg),
]).clip(0.0, 1.0)

thresholds = np.linspace(1.0, 0.0, 101)
tpr = [(y_score[y_true == 1] >= t).mean() for t in thresholds]
fpr = [(y_score[y_true == 0] >= t).mean() for t in thresholds]
auc = float(np.trapezoid(tpr, fpr))

ax = roc_curve(
    fpr, tpr, auc=abs(auc),
    title="Fraud screening model: ROC curve", color="tab:blue",
)
plt.show()''',
    "dataviz.classification.charts.precision_recall_curve": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.charts import precision_recall_curve

rng = np.random.default_rng(42)
n_pos, n_neg = 40, 120
y_true = np.concatenate([np.ones(n_pos, int), np.zeros(n_neg, int)])
y_score = np.concatenate([
    rng.normal(0.70, 0.17, n_pos),
    rng.normal(0.30, 0.15, n_neg),
]).clip(0.0, 1.0)

thresholds = np.linspace(1.0, 0.0, 101)
precision, recall = [], []
for t in thresholds:
    flagged = y_score >= t
    tp = int((flagged & (y_true == 1)).sum())
    fp = int((flagged & (y_true == 0)).sum())
    fn = int((~flagged & (y_true == 1)).sum())
    precision.append(tp / (tp + fp) if tp + fp else 1.0)
    recall.append(tp / (tp + fn) if tp + fn else 0.0)
ap = float(np.trapezoid(precision[::-1], recall[::-1]))

ax = precision_recall_curve(
    precision, recall, ap=abs(ap),
    title="Rare-disease screening: precision-recall curve", color="tab:green",
)
plt.show()''',
    # --- confusion_extended.py ----------------------------------------------
    "dataviz.classification.confusion_extended.normalized_confusion_matrix_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.confusion_extended import (
    normalized_confusion_matrix_static,
)

rng = np.random.default_rng(8)
n = 180
true_labels = rng.choice(3, size=n, p=[0.5, 0.3, 0.2])
pred_labels = true_labels.copy()
flip = rng.uniform(size=n) < 0.15
pred_labels[flip] = rng.choice(3, size=int(flip.sum()))
cm = np.zeros((3, 3), dtype=int)
for t, p in zip(true_labels, pred_labels):
    cm[t, p] += 1
classes = ["low", "medium", "high"]

ax = normalized_confusion_matrix_static(
    cm, labels=classes, normalize="true",
    title="Support ticket priority: per-class recall matrix",
)
plt.show()''',
    "dataviz.classification.confusion_extended.normalized_confusion_matrix_interactive": '''import numpy as np
from dataviz.classification.confusion_extended import (
    normalized_confusion_matrix_interactive,
)

rng = np.random.default_rng(8)
n = 180
true_labels = rng.choice(3, size=n, p=[0.5, 0.3, 0.2])
pred_labels = true_labels.copy()
flip = rng.uniform(size=n) < 0.15
pred_labels[flip] = rng.choice(3, size=int(flip.sum()))
cm = np.zeros((3, 3), dtype=int)
for t, p in zip(true_labels, pred_labels):
    cm[t, p] += 1
classes = ["low", "medium", "high"]

fig = normalized_confusion_matrix_interactive(
    cm, labels=classes, normalize="true",
    title="Support ticket priority: per-class recall matrix",
)
fig.show()''',
    "dataviz.classification.confusion_extended.confusion_matrix_diff_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.confusion_extended import confusion_matrix_diff_static

rng = np.random.default_rng(19)
n = 160
true_labels = rng.choice(2, size=n, p=[0.7, 0.3])


def make_cm(error_rate):
    preds = true_labels.copy()
    flips = rng.uniform(size=n) < error_rate
    preds[flips] = 1 - preds[flips]
    m = np.zeros((2, 2), dtype=int)
    for t, p in zip(true_labels, preds):
        m[t, p] += 1
    return m


cm_new = make_cm(0.12)
cm_baseline = make_cm(0.25)

ax = confusion_matrix_diff_static(
    cm_new, cm_baseline, labels=["no-churn", "churn"],
    title="New churn model minus baseline (positive = improvement)",
)
plt.show()''',
    "dataviz.classification.confusion_extended.confusion_matrix_diff_interactive": '''import numpy as np
from dataviz.classification.confusion_extended import (
    confusion_matrix_diff_interactive,
)

rng = np.random.default_rng(19)
n = 160
true_labels = rng.choice(2, size=n, p=[0.7, 0.3])


def make_cm(error_rate):
    preds = true_labels.copy()
    flips = rng.uniform(size=n) < error_rate
    preds[flips] = 1 - preds[flips]
    m = np.zeros((2, 2), dtype=int)
    for t, p in zip(true_labels, preds):
        m[t, p] += 1
    return m


cm_new = make_cm(0.12)
cm_baseline = make_cm(0.25)

fig = confusion_matrix_diff_interactive(
    cm_new, cm_baseline, labels=["no-churn", "churn"],
    title="New churn model minus baseline (positive = improvement)",
)
fig.show()''',
    "dataviz.classification.confusion_extended.error_analysis_grid_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.confusion_extended import error_analysis_grid_static

rng = np.random.default_rng(23)
n = 200
true_labels = rng.choice(4, size=n, p=[0.4, 0.3, 0.2, 0.1])
pred_labels = true_labels.copy()
flip = rng.uniform(size=n) < 0.2
pred_labels[flip] = np.clip(true_labels[flip] + rng.choice([-1, 1],
                            size=int(flip.sum())), 0, 3)
cm = np.zeros((4, 4), dtype=int)
for t, p in zip(true_labels, pred_labels):
    cm[t, p] += 1
classes = ["sedan", "SUV", "truck", "van"]

ax = error_analysis_grid_static(
    cm, labels=classes,
    title="Vehicle image classifier: which classes get confused?",
)
plt.show()''',
    "dataviz.classification.confusion_extended.error_analysis_grid_interactive": '''import numpy as np
from dataviz.classification.confusion_extended import (
    error_analysis_grid_interactive,
)

rng = np.random.default_rng(23)
n = 200
true_labels = rng.choice(4, size=n, p=[0.4, 0.3, 0.2, 0.1])
pred_labels = true_labels.copy()
flip = rng.uniform(size=n) < 0.2
pred_labels[flip] = np.clip(true_labels[flip] + rng.choice([-1, 1],
                            size=int(flip.sum())), 0, 3)
cm = np.zeros((4, 4), dtype=int)
for t, p in zip(true_labels, pred_labels):
    cm[t, p] += 1
classes = ["sedan", "SUV", "truck", "van"]

fig = error_analysis_grid_interactive(
    cm, labels=classes,
    title="Vehicle image classifier: which classes get confused?",
)
fig.show()''',
    # --- confusion_matrix.py -------------------------------------------------
    "dataviz.classification.confusion_matrix.confusion_matrix_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.confusion_matrix import confusion_matrix_plot_static

rng = np.random.default_rng(42)
n = 160
y_prob = np.clip(rng.beta(2, 4, n), 0.01, 0.99)
y_true = (rng.uniform(size=n) < y_prob).astype(int)
y_pred = (y_prob >= 0.35).astype(int)  # low threshold: fraud recall first
cm = np.zeros((2, 2), dtype=int)
for t, p in zip(y_true, y_pred):
    cm[t, p] += 1

ax = confusion_matrix_plot_static(
    cm, labels=["legitimate", "fraud"],
    title="Fraud detector at 0.35 alert threshold",
    cmap="Oranges",
)
plt.show()''',
    "dataviz.classification.confusion_matrix.confusion_matrix_plot_interactive": '''import numpy as np
from dataviz.classification.confusion_matrix import (
    confusion_matrix_plot_interactive,
)

rng = np.random.default_rng(42)
n = 160
y_prob = np.clip(rng.beta(2, 4, n), 0.01, 0.99)
y_true = (rng.uniform(size=n) < y_prob).astype(int)
y_pred = (y_prob >= 0.35).astype(int)  # low threshold: fraud recall first
cm = np.zeros((2, 2), dtype=int)
for t, p in zip(y_true, y_pred):
    cm[t, p] += 1

fig = confusion_matrix_plot_interactive(
    cm, labels=["legitimate", "fraud"],
    title="Fraud detector at 0.35 alert threshold",
    colorscale="Oranges",
)
fig.show()''',
    # --- decision_boundary.py ------------------------------------------------
    "dataviz.classification.decision_boundary.decision_boundary_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.decision_boundary import decision_boundary_plot_static

rng = np.random.default_rng(42)
n = 120
x = rng.uniform(-3, 3, n)
y = rng.uniform(-3, 3, n)
labels = (x ** 2 + y ** 2 + rng.normal(0, 0.4, n) > 2.5).astype(int)


def knn_predict(points, k=5):
    train = np.column_stack([x, y])
    d = ((points[:, None, :] - train[None, :, :]) ** 2).sum(axis=2)
    nearest = np.argsort(d, axis=1)[:, :k]
    return (labels[nearest].mean(axis=1) >= 0.5).astype(int)


ax = decision_boundary_plot_static(
    x, y, labels, knn_predict, resolution=100,
    title="5-NN ring classifier: decision boundary",
)
ax.set_xlabel("sensor reading A")
ax.set_ylabel("sensor reading B")
plt.show()''',
    "dataviz.classification.decision_boundary.decision_boundary_plot_interactive": '''import numpy as np
from dataviz.classification.decision_boundary import (
    decision_boundary_plot_interactive,
)

rng = np.random.default_rng(42)
n = 120
x = rng.uniform(-3, 3, n)
y = rng.uniform(-3, 3, n)
labels = (x ** 2 + y ** 2 + rng.normal(0, 0.4, n) > 2.5).astype(int)


def knn_predict(points, k=5):
    train = np.column_stack([x, y])
    d = ((points[:, None, :] - train[None, :, :]) ** 2).sum(axis=2)
    nearest = np.argsort(d, axis=1)[:, :k]
    return (labels[nearest].mean(axis=1) >= 0.5).astype(int)


fig = decision_boundary_plot_interactive(
    x, y, labels, knn_predict, resolution=80,
    title="5-NN ring classifier: decision boundary",
)
fig.show()''',
    # --- errors.py -----------------------------------------------------------
    "dataviz.classification.errors.confidence_by_correctness_histogram_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.errors import (
    confidence_by_correctness_histogram_static,
)

rng = np.random.default_rng(31)
n = 150
skill = rng.normal(0, 1.4, n)
y_prob = 1.0 / (1.0 + np.exp(-skill))
y_true = (skill + rng.normal(0, 1.0, n) > 0).astype(int)

ax = confidence_by_correctness_histogram_static(
    y_true, y_prob, threshold=0.5, bins=25,
    title="Email spam filter: is the model confident when wrong?",
)
plt.show()''',
    "dataviz.classification.errors.confidence_by_correctness_histogram_interactive": '''import numpy as np
from dataviz.classification.errors import (
    confidence_by_correctness_histogram_interactive,
)

rng = np.random.default_rng(31)
n = 150
skill = rng.normal(0, 1.4, n)
y_prob = 1.0 / (1.0 + np.exp(-skill))
y_true = (skill + rng.normal(0, 1.0, n) > 0).astype(int)

fig = confidence_by_correctness_histogram_interactive(
    y_true, y_prob, threshold=0.5, bins=25,
    title="Email spam filter: is the model confident when wrong?",
)
fig.show()''',
    "dataviz.classification.errors.discrimination_threshold_dashboard_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.errors import (
    discrimination_threshold_dashboard_static,
)

rng = np.random.default_rng(37)
n_pos, n_neg = 45, 115
y_true = np.concatenate([np.ones(n_pos, int), np.zeros(n_neg, int)])
y_prob = np.concatenate([
    rng.normal(0.66, 0.16, n_pos),
    rng.normal(0.34, 0.16, n_neg),
]).clip(0.01, 0.99)

ax = discrimination_threshold_dashboard_static(
    y_true, y_prob, n_thresholds=80,
    title="Churn outreach: picking the operating threshold",
)
plt.show()''',
    "dataviz.classification.errors.discrimination_threshold_dashboard_interactive": '''import numpy as np
from dataviz.classification.errors import (
    discrimination_threshold_dashboard_interactive,
)

rng = np.random.default_rng(37)
n_pos, n_neg = 45, 115
y_true = np.concatenate([np.ones(n_pos, int), np.zeros(n_neg, int)])
y_prob = np.concatenate([
    rng.normal(0.66, 0.16, n_pos),
    rng.normal(0.34, 0.16, n_neg),
]).clip(0.01, 0.99)

fig = discrimination_threshold_dashboard_interactive(
    y_true, y_prob, n_thresholds=80,
    title="Churn outreach: picking the operating threshold",
)
fig.show()''',
    "dataviz.classification.errors.misclassification_cluster_heatmap_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.errors import (
    misclassification_cluster_heatmap_static,
)

rng = np.random.default_rng(41)
n = 170
y_prob = np.clip(rng.beta(2, 2.5, n), 0.01, 0.99)
noise = rng.normal(0, 0.25, n)
y_true = (y_prob + noise > 0.55).astype(int)

ax = misclassification_cluster_heatmap_static(
    y_true, y_prob, n_score_bins=8, threshold=0.5,
    title="Claims triage model: mistake rate by score band",
)
plt.show()''',
    "dataviz.classification.errors.misclassification_cluster_heatmap_interactive": '''import numpy as np
from dataviz.classification.errors import (
    misclassification_cluster_heatmap_interactive,
)

rng = np.random.default_rng(41)
n = 170
y_prob = np.clip(rng.beta(2, 2.5, n), 0.01, 0.99)
noise = rng.normal(0, 0.25, n)
y_true = (y_prob + noise > 0.55).astype(int)

fig = misclassification_cluster_heatmap_interactive(
    y_true, y_prob, n_score_bins=8, threshold=0.5,
    title="Claims triage model: mistake rate by score band",
)
fig.show()''',
    "dataviz.classification.errors.loss_distribution_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.errors import loss_distribution_plot_static

rng = np.random.default_rng(43)
n = 160
signal = rng.normal(0, 1.3, n)
y_prob = np.clip(1.0 / (1.0 + np.exp(-signal)), 1e-4, 1 - 1e-4)
y_true = (signal + rng.normal(0, 0.9, n) > 0).astype(int)
# a few hard mislabeled samples create high-loss outliers
y_true[:4] = 1 - y_true[:4]
y_prob[:4] = np.clip(y_prob[:4], 0.85, 0.98)

ax = loss_distribution_plot_static(
    y_true, y_prob, bins=30,
    title="Document classifier: per-sample log loss outlier hunt",
)
plt.show()''',
    "dataviz.classification.errors.loss_distribution_plot_interactive": '''import numpy as np
from dataviz.classification.errors import loss_distribution_plot_interactive

rng = np.random.default_rng(43)
n = 160
signal = rng.normal(0, 1.3, n)
y_prob = np.clip(1.0 / (1.0 + np.exp(-signal)), 1e-4, 1 - 1e-4)
y_true = (signal + rng.normal(0, 0.9, n) > 0).astype(int)
# a few hard mislabeled samples create high-loss outliers
y_true[:4] = 1 - y_true[:4]
y_prob[:4] = np.clip(y_prob[:4], 0.85, 0.98)

fig = loss_distribution_plot_interactive(
    y_true, y_prob, bins=30,
    title="Document classifier: per-sample log loss outlier hunt",
)
fig.show()''',
    # --- fairness.py ---------------------------------------------------------
    "dataviz.classification.fairness.per_segment_metric_bar_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.fairness import per_segment_metric_bar_static

rng = np.random.default_rng(47)
n = 180
groups = rng.choice(["urban", "suburban", "rural"], size=n, p=[0.45, 0.35, 0.2])
base = {"urban": 0.55, "suburban": 0.50, "rural": 0.42}
y_prob = np.array([base[g] for g in groups]) + rng.normal(0, 0.2, n)
y_true = (rng.uniform(size=n) < np.clip(y_prob, 0.02, 0.98)).astype(int)
y_pred = (y_prob >= 0.5).astype(int)

ax = per_segment_metric_bar_static(
    y_true, y_pred, groups,
    metrics=("accuracy", "tpr", "fpr", "selection_rate"),
    title="Housing assistance model: metrics by region",
)
plt.show()''',
    "dataviz.classification.fairness.per_segment_metric_bar_interactive": '''import numpy as np
from dataviz.classification.fairness import per_segment_metric_bar_interactive

rng = np.random.default_rng(47)
n = 180
groups = rng.choice(["urban", "suburban", "rural"], size=n, p=[0.45, 0.35, 0.2])
base = {"urban": 0.55, "suburban": 0.50, "rural": 0.42}
y_prob = np.array([base[g] for g in groups]) + rng.normal(0, 0.2, n)
y_true = (rng.uniform(size=n) < np.clip(y_prob, 0.02, 0.98)).astype(int)
y_pred = (y_prob >= 0.5).astype(int)

fig = per_segment_metric_bar_interactive(
    y_true, y_pred, groups,
    metrics=("accuracy", "tpr", "fpr", "selection_rate"),
    title="Housing assistance model: metrics by region",
)
fig.show()''',
    "dataviz.classification.fairness.fairness_disparity_heatmap_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.fairness import fairness_disparity_heatmap_static

rng = np.random.default_rng(53)
n = 180
groups = rng.choice(["group A", "group B", "group C"], size=n,
                    p=[0.5, 0.3, 0.2])
shift = {"group A": 0.08, "group B": 0.0, "group C": -0.10}
y_prob = np.clip(0.5 + np.array([shift[g] for g in groups])
                 + rng.normal(0, 0.22, n), 0.02, 0.98)
y_true = (rng.uniform(size=n) < y_prob).astype(int)
y_pred = (y_prob >= 0.5).astype(int)

ax = fairness_disparity_heatmap_static(
    y_true, y_pred, groups,
    title="Hiring screen: deviation from population mean per group",
)
plt.show()''',
    "dataviz.classification.fairness.fairness_disparity_heatmap_interactive": '''import numpy as np
from dataviz.classification.fairness import fairness_disparity_heatmap_interactive

rng = np.random.default_rng(53)
n = 180
groups = rng.choice(["group A", "group B", "group C"], size=n,
                    p=[0.5, 0.3, 0.2])
shift = {"group A": 0.08, "group B": 0.0, "group C": -0.10}
y_prob = np.clip(0.5 + np.array([shift[g] for g in groups])
                 + rng.normal(0, 0.22, n), 0.02, 0.98)
y_true = (rng.uniform(size=n) < y_prob).astype(int)
y_pred = (y_prob >= 0.5).astype(int)

fig = fairness_disparity_heatmap_interactive(
    y_true, y_pred, groups,
    title="Hiring screen: deviation from population mean per group",
)
fig.show()''',
    "dataviz.classification.fairness.segment_roc_overlay_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.fairness import segment_roc_overlay_static

rng = np.random.default_rng(59)
n = 180
groups = rng.choice(["north", "south", "west"], size=n, p=[0.4, 0.35, 0.25])
sep = {"north": 0.9, "south": 0.7, "west": 0.45}  # weaker signal out west
y_true = (rng.uniform(size=n) < 0.35).astype(int)
y_score = np.array([
    rng.normal(sep[g], 0.55) if t == 1 else rng.normal(0.0, 0.55)
    for g, t in zip(groups, y_true)
])

ax = segment_roc_overlay_static(
    y_true, y_score, groups,
    title="Fraud model ROC by region: disparity check",
)
plt.show()''',
    "dataviz.classification.fairness.segment_roc_overlay_interactive": '''import numpy as np
from dataviz.classification.fairness import segment_roc_overlay_interactive

rng = np.random.default_rng(59)
n = 180
groups = rng.choice(["north", "south", "west"], size=n, p=[0.4, 0.35, 0.25])
sep = {"north": 0.9, "south": 0.7, "west": 0.45}  # weaker signal out west
y_true = (rng.uniform(size=n) < 0.35).astype(int)
y_score = np.array([
    rng.normal(sep[g], 0.55) if t == 1 else rng.normal(0.0, 0.55)
    for g, t in zip(groups, y_true)
])

fig = segment_roc_overlay_interactive(
    y_true, y_score, groups,
    title="Fraud model ROC by region: disparity check",
)
fig.show()''',
    "dataviz.classification.fairness.segment_calibration_overlay_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.fairness import segment_calibration_overlay_static

rng = np.random.default_rng(61)
n = 180
groups = rng.choice(["app", "web", "branch"], size=n, p=[0.5, 0.3, 0.2])
y_prob = np.clip(rng.beta(2, 3, n), 0.01, 0.99)
bias = {"app": 0.0, "web": 0.05, "branch": -0.07}
y_true = (rng.uniform(size=n)
          < np.clip(y_prob + np.array([bias[g] for g in groups]), 0, 1)
          ).astype(int)

ax = segment_calibration_overlay_static(
    y_true, y_prob, groups, n_bins=6,
    title="Loan approval model: calibration by application channel",
)
plt.show()''',
    "dataviz.classification.fairness.segment_calibration_overlay_interactive": '''import numpy as np
from dataviz.classification.fairness import (
    segment_calibration_overlay_interactive,
)

rng = np.random.default_rng(61)
n = 180
groups = rng.choice(["app", "web", "branch"], size=n, p=[0.5, 0.3, 0.2])
y_prob = np.clip(rng.beta(2, 3, n), 0.01, 0.99)
bias = {"app": 0.0, "web": 0.05, "branch": -0.07}
y_true = (rng.uniform(size=n)
          < np.clip(y_prob + np.array([bias[g] for g in groups]), 0, 1)
          ).astype(int)

fig = segment_calibration_overlay_interactive(
    y_true, y_prob, groups, n_bins=6,
    title="Loan approval model: calibration by application channel",
)
fig.show()''',
    # --- gain_lift.py --------------------------------------------------------
    "dataviz.classification.gain_lift.gain_chart_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.gain_lift import gain_chart_static

rng = np.random.default_rng(67)
n_pos, n_neg = 40, 120
y_true = np.concatenate([np.ones(n_pos, int), np.zeros(n_neg, int)])
y_prob = np.concatenate([
    rng.normal(0.70, 0.16, n_pos),
    rng.normal(0.30, 0.15, n_neg),
]).clip(0.01, 0.99)

ax = gain_chart_static(
    y_true, y_prob,
    title="Direct-mail campaign: cumulative gains of response model",
)
ax.annotate("top 20% captures most responders", xy=(0.2, 0.7),
            xytext=(0.35, 0.45),
            arrowprops=dict(arrowstyle="->", color="grey"))
plt.show()''',
    "dataviz.classification.gain_lift.gain_chart_interactive": '''import numpy as np
from dataviz.classification.gain_lift import gain_chart_interactive

rng = np.random.default_rng(67)
n_pos, n_neg = 40, 120
y_true = np.concatenate([np.ones(n_pos, int), np.zeros(n_neg, int)])
y_prob = np.concatenate([
    rng.normal(0.70, 0.16, n_pos),
    rng.normal(0.30, 0.15, n_neg),
]).clip(0.01, 0.99)

fig = gain_chart_interactive(
    y_true, y_prob,
    title="Direct-mail campaign: cumulative gains of response model",
)
fig.show()''',
    "dataviz.classification.gain_lift.lift_chart_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.gain_lift import lift_chart_static

rng = np.random.default_rng(67)
n_pos, n_neg = 40, 120
y_true = np.concatenate([np.ones(n_pos, int), np.zeros(n_neg, int)])
y_prob = np.concatenate([
    rng.normal(0.70, 0.16, n_pos),
    rng.normal(0.30, 0.15, n_neg),
]).clip(0.01, 0.99)

ax = lift_chart_static(
    y_true, y_prob, n_bins=10,
    title="Direct-mail campaign: lift per score decile",
)
ax.set_ylabel("Lift vs random mailing")
plt.show()''',
    "dataviz.classification.gain_lift.lift_chart_interactive": '''import numpy as np
from dataviz.classification.gain_lift import lift_chart_interactive

rng = np.random.default_rng(67)
n_pos, n_neg = 40, 120
y_true = np.concatenate([np.ones(n_pos, int), np.zeros(n_neg, int)])
y_prob = np.concatenate([
    rng.normal(0.70, 0.16, n_pos),
    rng.normal(0.30, 0.15, n_neg),
]).clip(0.01, 0.99)

fig = lift_chart_interactive(
    y_true, y_prob, n_bins=10,
    title="Direct-mail campaign: lift per score decile",
)
fig.show()''',
    "dataviz.classification.gain_lift.cumulative_accuracy_profile_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.gain_lift import cumulative_accuracy_profile_static

rng = np.random.default_rng(71)
n_pos, n_neg = 35, 125
y_true = np.concatenate([np.ones(n_pos, int), np.zeros(n_neg, int)])
y_prob = np.concatenate([
    rng.normal(0.68, 0.17, n_pos),
    rng.normal(0.32, 0.15, n_neg),
]).clip(0.01, 0.99)

ax = cumulative_accuracy_profile_static(
    y_true, y_prob,
    title="Credit default model: CAP curve and accuracy ratio",
)
plt.show()''',
    "dataviz.classification.gain_lift.cumulative_accuracy_profile_interactive": '''import numpy as np
from dataviz.classification.gain_lift import (
    cumulative_accuracy_profile_interactive,
)

rng = np.random.default_rng(71)
n_pos, n_neg = 35, 125
y_true = np.concatenate([np.ones(n_pos, int), np.zeros(n_neg, int)])
y_prob = np.concatenate([
    rng.normal(0.68, 0.17, n_pos),
    rng.normal(0.32, 0.15, n_neg),
]).clip(0.01, 0.99)

fig = cumulative_accuracy_profile_interactive(
    y_true, y_prob,
    title="Credit default model: CAP curve and accuracy ratio",
)
fig.show()''',
    # --- model_comparison.py -------------------------------------------------
    "dataviz.classification.model_comparison.metrics_radar_chart_static": '''import matplotlib.pyplot as plt
from dataviz.classification.model_comparison import metrics_radar_chart_static

metrics = {
    "Logistic regression": {"accuracy": 0.82, "precision": 0.78,
                            "recall": 0.71, "f1": 0.74, "auc": 0.85},
    "Random forest": {"accuracy": 0.88, "precision": 0.85,
                      "recall": 0.80, "f1": 0.82, "auc": 0.91},
    "Gradient boosting": {"accuracy": 0.89, "precision": 0.87,
                          "recall": 0.79, "f1": 0.83, "auc": 0.92},
}

ax = metrics_radar_chart_static(
    metrics, title="Churn model bake-off: cross-validated metrics",
)
plt.show()''',
    "dataviz.classification.model_comparison.metrics_radar_chart_interactive": '''from dataviz.classification.model_comparison import (
    metrics_radar_chart_interactive,
)

metrics = {
    "Logistic regression": {"accuracy": 0.82, "precision": 0.78,
                            "recall": 0.71, "f1": 0.74, "auc": 0.85},
    "Random forest": {"accuracy": 0.88, "precision": 0.85,
                      "recall": 0.80, "f1": 0.82, "auc": 0.91},
    "Gradient boosting": {"accuracy": 0.89, "precision": 0.87,
                          "recall": 0.79, "f1": 0.83, "auc": 0.92},
}

fig = metrics_radar_chart_interactive(
    metrics, title="Churn model bake-off: cross-validated metrics",
)
fig.show()''',
    "dataviz.classification.model_comparison.pareto_tradeoff_bubble_static": '''import matplotlib.pyplot as plt
from dataviz.classification.model_comparison import (
    pareto_tradeoff_bubble_static,
)

models = {
    "logreg": {"precision": 0.78, "recall": 0.72, "auc": 0.85},
    "rf-shallow": {"precision": 0.83, "recall": 0.75, "auc": 0.89},
    "rf-deep": {"precision": 0.86, "recall": 0.70, "auc": 0.91},
    "gbm": {"precision": 0.84, "recall": 0.81, "auc": 0.92},
    "knn": {"precision": 0.70, "recall": 0.65, "auc": 0.76},
    "mlp": {"precision": 0.80, "recall": 0.78, "auc": 0.88},
}

ax = pareto_tradeoff_bubble_static(
    models, x_metric="precision", y_metric="recall", size_metric="auc",
    title="Fraud models: precision-recall trade-off (bubble = AUC)",
)
ax.set_xlim(0.6, 0.95)
plt.show()''',
    "dataviz.classification.model_comparison.pareto_tradeoff_bubble_interactive": '''from dataviz.classification.model_comparison import (
    pareto_tradeoff_bubble_interactive,
)

models = {
    "logreg": {"precision": 0.78, "recall": 0.72, "auc": 0.85},
    "rf-shallow": {"precision": 0.83, "recall": 0.75, "auc": 0.89},
    "rf-deep": {"precision": 0.86, "recall": 0.70, "auc": 0.91},
    "gbm": {"precision": 0.84, "recall": 0.81, "auc": 0.92},
    "knn": {"precision": 0.70, "recall": 0.65, "auc": 0.76},
    "mlp": {"precision": 0.80, "recall": 0.78, "auc": 0.88},
}

fig = pareto_tradeoff_bubble_interactive(
    models, x_metric="precision", y_metric="recall", size_metric="auc",
    title="Fraud models: precision-recall trade-off (bubble = AUC)",
)
fig.show()''',
    "dataviz.classification.model_comparison.critical_difference_diagram_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.model_comparison import (
    critical_difference_diagram_static,
)

rng = np.random.default_rng(73)
# ranks of 4 models on 12 benchmark datasets (1 = best)
rank_table = {
    "gbm": np.clip(rng.normal(1.8, 0.6, 12), 1, 4),
    "random forest": np.clip(rng.normal(2.2, 0.7, 12), 1, 4),
    "logreg": np.clip(rng.normal(3.0, 0.6, 12), 1, 4),
    "knn": np.clip(rng.normal(3.4, 0.5, 12), 1, 4),
}

ax = critical_difference_diagram_static(
    rank_table, cd=1.15,
    title="CD diagram: tabular benchmarks (Nemenyi, alpha=0.05)",
)
plt.show()''',
    "dataviz.classification.model_comparison.critical_difference_diagram_interactive": '''import numpy as np
from dataviz.classification.model_comparison import (
    critical_difference_diagram_interactive,
)

rng = np.random.default_rng(73)
# ranks of 4 models on 12 benchmark datasets (1 = best)
rank_table = {
    "gbm": np.clip(rng.normal(1.8, 0.6, 12), 1, 4),
    "random forest": np.clip(rng.normal(2.2, 0.7, 12), 1, 4),
    "logreg": np.clip(rng.normal(3.0, 0.6, 12), 1, 4),
    "knn": np.clip(rng.normal(3.4, 0.5, 12), 1, 4),
}

fig = critical_difference_diagram_interactive(
    rank_table, cd=1.15,
    title="CD diagram: tabular benchmarks (Nemenyi, alpha=0.05)",
)
fig.show()''',
    "dataviz.classification.model_comparison.score_distribution_drift_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.model_comparison import (
    score_distribution_drift_static,
)

rng = np.random.default_rng(79)
scores_reference = np.clip(rng.beta(2, 4, 150), 0.01, 0.99)
# production traffic shifted toward higher risk scores last month
scores_current = np.clip(rng.beta(2.6, 3.6, 150), 0.01, 0.99)

ax = score_distribution_drift_static(
    scores_reference, scores_current, bins=30,
    title="Fraud scoring service: training vs last-month traffic",
)
plt.show()''',
    "dataviz.classification.model_comparison.score_distribution_drift_interactive": '''import numpy as np
from dataviz.classification.model_comparison import (
    score_distribution_drift_interactive,
)

rng = np.random.default_rng(79)
scores_reference = np.clip(rng.beta(2, 4, 150), 0.01, 0.99)
# production traffic shifted toward higher risk scores last month
scores_current = np.clip(rng.beta(2.6, 3.6, 150), 0.01, 0.99)

fig = score_distribution_drift_interactive(
    scores_reference, scores_current, bins=30,
    title="Fraud scoring service: training vs last-month traffic",
)
fig.show()''',
    "dataviz.classification.model_comparison.psi_bar_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.model_comparison import psi_bar_static

rng = np.random.default_rng(83)
scores_reference = np.clip(rng.beta(2, 4, 150), 0.01, 0.99)
# seasonal campaign pushed noticeably higher-risk applicants into the funnel
scores_current = np.clip(rng.beta(3.0, 3.4, 150), 0.01, 0.99)

ax = psi_bar_static(
    scores_reference, scores_current, n_bins=8,
    title="Application risk score: PSI vs training baseline",
)
plt.show()''',
    "dataviz.classification.model_comparison.psi_bar_interactive": '''import numpy as np
from dataviz.classification.model_comparison import psi_bar_interactive

rng = np.random.default_rng(83)
scores_reference = np.clip(rng.beta(2, 4, 150), 0.01, 0.99)
# seasonal campaign pushed noticeably higher-risk applicants into the funnel
scores_current = np.clip(rng.beta(3.0, 3.4, 150), 0.01, 0.99)

fig = psi_bar_interactive(
    scores_reference, scores_current, n_bins=8,
    title="Application risk score: PSI vs training baseline",
)
fig.show()''',
}
