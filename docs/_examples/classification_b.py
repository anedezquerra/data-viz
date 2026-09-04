"""Curated rich examples for classification member pages."""

BINARY_SETUP = '''import numpy as np
rng = np.random.default_rng(42)
n = 150
y_true = (rng.random(n) < 0.35).astype(int)
y_prob = np.clip(
    y_true * rng.beta(7, 2.5, n) + (1 - y_true) * rng.beta(2.5, 7, n), 0, 1)
'''

EXAMPLES = {
    # ------------------------------------------------------------------ roc.py
    "dataviz.classification.roc.roc_curve_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.roc import roc_curve_static

rng = np.random.default_rng(42)
n = 150
y_true = (rng.random(n) < 0.35).astype(int)  # churn flag, 35% prevalence
y_prob = np.clip(
    y_true * rng.beta(7, 2.5, n) + (1 - y_true) * rng.beta(2.5, 7, n), 0, 1)
order = np.argsort(-y_prob)
fpr, tpr, tp, fp = [0.0], [0.0], 0, 0
for i in order:
    if y_true[i] == 1:
        tp += 1
    else:
        fp += 1
    tpr.append(tp / max((y_true == 1).sum(), 1))
    fpr.append(fp / max((y_true == 0).sum(), 1))
fpr, tpr = np.array(fpr), np.array(tpr)
auc = float(np.trapezoid(tpr, fpr))

ax = roc_curve_static(fpr, tpr, auc=auc,
                      title="Churn model ROC (holdout quarter)")
ax.annotate(f"AUC = {auc:.3f}", xy=(0.6, 0.2), fontsize=11)
plt.show()''',

    "dataviz.classification.roc.roc_curve_interactive": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.roc import roc_curve_interactive

rng = np.random.default_rng(42)
n = 150
y_true = (rng.random(n) < 0.35).astype(int)  # churn flag, 35% prevalence
y_prob = np.clip(
    y_true * rng.beta(7, 2.5, n) + (1 - y_true) * rng.beta(2.5, 7, n), 0, 1)
order = np.argsort(-y_prob)
fpr, tpr, tp, fp = [0.0], [0.0], 0, 0
for i in order:
    if y_true[i] == 1:
        tp += 1
    else:
        fp += 1
    tpr.append(tp / max((y_true == 1).sum(), 1))
    fpr.append(fp / max((y_true == 0).sum(), 1))
fpr, tpr = np.array(fpr), np.array(tpr)
auc = float(np.trapezoid(tpr, fpr))

fig = roc_curve_interactive(fpr, tpr, auc=auc,
                            title="Churn model ROC (holdout quarter)")
fig.show()''',

    # -------------------------------------------------------------- pr_curve.py
    "dataviz.classification.pr_curve.precision_recall_curve_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.pr_curve import precision_recall_curve_static

rng = np.random.default_rng(42)
n = 150
# rare-event fraud detector: only 8% of transactions are fraud
y_true = (rng.random(n) < 0.08).astype(int)
y_prob = np.clip(
    y_true * rng.beta(6, 2, n) + (1 - y_true) * rng.beta(2, 8, n), 0, 1)
order = np.argsort(-y_prob)
precision, recall, tp, fp = [1.0], [0.0], 0, 0
for i in order:
    if y_true[i] == 1:
        tp += 1
    else:
        fp += 1
    precision.append(tp / max(tp + fp, 1))
    recall.append(tp / max((y_true == 1).sum(), 1))
ap = float(np.trapezoid(precision, recall))

ax = precision_recall_curve_static(precision, recall, ap=abs(ap),
                                   title="Fraud detector precision-recall")
plt.show()''',

    "dataviz.classification.pr_curve.precision_recall_curve_interactive": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.pr_curve import precision_recall_curve_interactive

rng = np.random.default_rng(42)
n = 150
# rare-event fraud detector: only 8% of transactions are fraud
y_true = (rng.random(n) < 0.08).astype(int)
y_prob = np.clip(
    y_true * rng.beta(6, 2, n) + (1 - y_true) * rng.beta(2, 8, n), 0, 1)
order = np.argsort(-y_prob)
precision, recall, tp, fp = [1.0], [0.0], 0, 0
for i in order:
    if y_true[i] == 1:
        tp += 1
    else:
        fp += 1
    precision.append(tp / max(tp + fp, 1))
    recall.append(tp / max((y_true == 1).sum(), 1))
ap = float(np.trapezoid(precision, recall))

fig = precision_recall_curve_interactive(precision, recall, ap=abs(ap),
                                         title="Fraud detector precision-recall")
fig.show()''',

    # ------------------------------------------------------------ multiclass.py
    "dataviz.classification.multiclass.multiclass_roc_curve_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.multiclass import multiclass_roc_curve_static

rng = np.random.default_rng(42)
# 3-class support-ticket triage model, one-vs-rest ROC per class
def ovr_roc(scores, truth):
    order = np.argsort(-scores)
    fpr, tpr, tp, fp = [0.0], [0.0], 0, 0
    for i in order:
        if truth[i] == 1:
            tp += 1
        else:
            fp += 1
        tpr.append(tp / max(truth.sum(), 1))
        fpr.append(fp / max((1 - truth).sum(), 1))
    return np.array(fpr), np.array(tpr)

n = 120
y = rng.integers(0, 3, n)
curves = {}
for k, name in enumerate(["Billing", "Technical", "Account"]):
    truth = (y == k).astype(int)
    score = np.clip(truth * rng.beta(6, 3, n) + (1 - truth) * rng.beta(3, 6, n), 0, 1)
    curves[name] = ovr_roc(score, truth)

ax = multiclass_roc_curve_static(curves,
                                 title="Ticket triage: one-vs-rest ROC")
plt.show()''',

    "dataviz.classification.multiclass.multiclass_roc_curve_interactive": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.multiclass import multiclass_roc_curve_interactive

rng = np.random.default_rng(42)
# 3-class support-ticket triage model, one-vs-rest ROC per class
def ovr_roc(scores, truth):
    order = np.argsort(-scores)
    fpr, tpr, tp, fp = [0.0], [0.0], 0, 0
    for i in order:
        if truth[i] == 1:
            tp += 1
        else:
            fp += 1
        tpr.append(tp / max(truth.sum(), 1))
        fpr.append(fp / max((1 - truth).sum(), 1))
    return np.array(fpr), np.array(tpr)

n = 120
y = rng.integers(0, 3, n)
curves = {}
for k, name in enumerate(["Billing", "Technical", "Account"]):
    truth = (y == k).astype(int)
    score = np.clip(truth * rng.beta(6, 3, n) + (1 - truth) * rng.beta(3, 6, n), 0, 1)
    curves[name] = ovr_roc(score, truth)

fig = multiclass_roc_curve_interactive(curves,
                                       title="Ticket triage: one-vs-rest ROC")
fig.show()''',

    "dataviz.classification.multiclass.multiclass_pr_curve_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.multiclass import multiclass_pr_curve_static

rng = np.random.default_rng(42)
# 3-class support-ticket triage model, one-vs-rest PR per class
def ovr_pr(scores, truth):
    order = np.argsort(-scores)
    precision, recall, tp, fp = [1.0], [0.0], 0, 0
    for i in order:
        if truth[i] == 1:
            tp += 1
        else:
            fp += 1
        precision.append(tp / max(tp + fp, 1))
        recall.append(tp / max(truth.sum(), 1))
    return np.array(recall), np.array(precision)

n = 120
y = rng.integers(0, 3, n)
curves = {}
for k, name in enumerate(["Billing", "Technical", "Account"]):
    truth = (y == k).astype(int)
    score = np.clip(truth * rng.beta(6, 3, n) + (1 - truth) * rng.beta(3, 6, n), 0, 1)
    curves[name] = ovr_pr(score, truth)

ax = multiclass_pr_curve_static(curves,
                                title="Ticket triage: one-vs-rest PR")
plt.show()''',

    "dataviz.classification.multiclass.multiclass_pr_curve_interactive": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.multiclass import multiclass_pr_curve_interactive

rng = np.random.default_rng(42)
# 3-class support-ticket triage model, one-vs-rest PR per class
def ovr_pr(scores, truth):
    order = np.argsort(-scores)
    precision, recall, tp, fp = [1.0], [0.0], 0, 0
    for i in order:
        if truth[i] == 1:
            tp += 1
        else:
            fp += 1
        precision.append(tp / max(tp + fp, 1))
        recall.append(tp / max(truth.sum(), 1))
    return np.array(recall), np.array(precision)

n = 120
y = rng.integers(0, 3, n)
curves = {}
for k, name in enumerate(["Billing", "Technical", "Account"]):
    truth = (y == k).astype(int)
    score = np.clip(truth * rng.beta(6, 3, n) + (1 - truth) * rng.beta(3, 6, n), 0, 1)
    curves[name] = ovr_pr(score, truth)

fig = multiclass_pr_curve_interactive(curves,
                                      title="Ticket triage: one-vs-rest PR")
fig.show()''',

    "dataviz.classification.multiclass.roc_curve_comparison_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.multiclass import roc_curve_comparison_static

rng = np.random.default_rng(42)
# churn screening: compare three candidate models on the same holdout
n = 150
y_true = (rng.random(n) < 0.3).astype(int)

def roc(scores):
    order = np.argsort(-scores)
    fpr, tpr, tp, fp = [0.0], [0.0], 0, 0
    for i in order:
        if y_true[i] == 1:
            tp += 1
        else:
            fp += 1
        tpr.append(tp / max(y_true.sum(), 1))
        fpr.append(fp / max((1 - y_true).sum(), 1))
    return np.array(fpr), np.array(tpr)

def scores(a_pos, b_pos, a_neg, b_neg):
    return np.clip(y_true * rng.beta(a_pos, b_pos, n)
                   + (1 - y_true) * rng.beta(a_neg, b_neg, n), 0, 1)

models = {
    "Gradient boosting": roc(scores(8, 2, 2, 8)),
    "Logistic regression": roc(scores(6, 3, 3, 6)),
    "Naive Bayes": roc(scores(4, 3, 3, 4)),
}

ax = roc_curve_comparison_static(models,
                                 title="Churn models: ROC comparison")
plt.show()''',

    "dataviz.classification.multiclass.roc_curve_comparison_interactive": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.multiclass import roc_curve_comparison_interactive

rng = np.random.default_rng(42)
# churn screening: compare three candidate models on the same holdout
n = 150
y_true = (rng.random(n) < 0.3).astype(int)

def roc(scores):
    order = np.argsort(-scores)
    fpr, tpr, tp, fp = [0.0], [0.0], 0, 0
    for i in order:
        if y_true[i] == 1:
            tp += 1
        else:
            fp += 1
        tpr.append(tp / max(y_true.sum(), 1))
        fpr.append(fp / max((1 - y_true).sum(), 1))
    return np.array(fpr), np.array(tpr)

def scores(a_pos, b_pos, a_neg, b_neg):
    return np.clip(y_true * rng.beta(a_pos, b_pos, n)
                   + (1 - y_true) * rng.beta(a_neg, b_neg, n), 0, 1)

models = {
    "Gradient boosting": roc(scores(8, 2, 2, 8)),
    "Logistic regression": roc(scores(6, 3, 3, 6)),
    "Naive Bayes": roc(scores(4, 3, 3, 4)),
}

fig = roc_curve_comparison_interactive(models,
                                       title="Churn models: ROC comparison")
fig.show()''',

    "dataviz.classification.multiclass.pr_curve_comparison_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.multiclass import pr_curve_comparison_static

rng = np.random.default_rng(42)
# fraud screening: PR comparison matters under heavy class imbalance
n = 150
y_true = (rng.random(n) < 0.08).astype(int)

def pr(scores):
    order = np.argsort(-scores)
    precision, recall, tp, fp = [1.0], [0.0], 0, 0
    for i in order:
        if y_true[i] == 1:
            tp += 1
        else:
            fp += 1
        precision.append(tp / max(tp + fp, 1))
        recall.append(tp / max(y_true.sum(), 1))
    return np.array(recall), np.array(precision)

def scores(a_pos, b_pos, a_neg, b_neg):
    return np.clip(y_true * rng.beta(a_pos, b_pos, n)
                   + (1 - y_true) * rng.beta(a_neg, b_neg, n), 0, 1)

models = {
    "Gradient boosting": pr(scores(8, 2, 2, 8)),
    "Logistic regression": pr(scores(6, 3, 3, 6)),
    "Naive Bayes": pr(scores(4, 3, 3, 4)),
}

ax = pr_curve_comparison_static(models,
                                title="Fraud models: PR comparison")
plt.show()''',

    "dataviz.classification.multiclass.pr_curve_comparison_interactive": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.multiclass import pr_curve_comparison_interactive

rng = np.random.default_rng(42)
# fraud screening: PR comparison matters under heavy class imbalance
n = 150
y_true = (rng.random(n) < 0.08).astype(int)

def pr(scores):
    order = np.argsort(-scores)
    precision, recall, tp, fp = [1.0], [0.0], 0, 0
    for i in order:
        if y_true[i] == 1:
            tp += 1
        else:
            fp += 1
        precision.append(tp / max(tp + fp, 1))
        recall.append(tp / max(y_true.sum(), 1))
    return np.array(recall), np.array(precision)

def scores(a_pos, b_pos, a_neg, b_neg):
    return np.clip(y_true * rng.beta(a_pos, b_pos, n)
                   + (1 - y_true) * rng.beta(a_neg, b_neg, n), 0, 1)

models = {
    "Gradient boosting": pr(scores(8, 2, 2, 8)),
    "Logistic regression": pr(scores(6, 3, 3, 6)),
    "Naive Bayes": pr(scores(4, 3, 3, 4)),
}

fig = pr_curve_comparison_interactive(models,
                                      title="Fraud models: PR comparison")
fig.show()''',

    # ----------------------------------------------------- multiclass_extra.py
    "dataviz.classification.multiclass_extra.per_class_auc_bar_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.multiclass_extra import per_class_auc_bar_static

# per-class one-vs-rest AUC from a 5-class document-topic classifier
auc_per_class = {
    "sports": 0.94,
    "politics": 0.88,
    "tech": 0.91,
    "finance": 0.82,
    "culture": 0.76,
}

ax = per_class_auc_bar_static(auc_per_class,
                              title="Topic classifier: per-class AUC",
                              color="#2a6f97")
plt.show()''',

    "dataviz.classification.multiclass_extra.per_class_auc_bar_interactive": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.multiclass_extra import per_class_auc_bar_interactive

# per-class one-vs-rest AUC from a 5-class document-topic classifier
auc_per_class = {
    "sports": 0.94,
    "politics": 0.88,
    "tech": 0.91,
    "finance": 0.82,
    "culture": 0.76,
}

fig = per_class_auc_bar_interactive(auc_per_class,
                                    title="Topic classifier: per-class AUC")
fig.show()''',

    "dataviz.classification.multiclass_extra.per_class_ap_bar_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.multiclass_extra import per_class_ap_bar_static

# per-class average precision from a 4-class defect-inspection model
ap_per_class = {
    "scratch": 0.71,
    "dent": 0.64,
    "discoloration": 0.55,
    "crack": 0.83,
}

ax = per_class_ap_bar_static(ap_per_class,
                             title="Defect model: per-class AP",
                             color="#4c956c")
plt.show()''',

    "dataviz.classification.multiclass_extra.per_class_ap_bar_interactive": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.multiclass_extra import per_class_ap_bar_interactive

# per-class average precision from a 4-class defect-inspection model
ap_per_class = {
    "scratch": 0.71,
    "dent": 0.64,
    "discoloration": 0.55,
    "crack": 0.83,
}

fig = per_class_ap_bar_interactive(ap_per_class,
                                   title="Defect model: per-class AP")
fig.show()''',

    "dataviz.classification.multiclass_extra.top_k_accuracy_curve_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.multiclass_extra import top_k_accuracy_curve_static

rng = np.random.default_rng(42)
# 6-class product recommender: does the right item appear in the top-K?
n = 120
n_classes = 6
y_true = rng.integers(0, n_classes, n)
logits = rng.normal(0, 1, (n, n_classes))
logits[np.arange(n), y_true] += 2.2  # model signal on the true class
probs = np.exp(logits) / np.exp(logits).sum(axis=1, keepdims=True)

ax = top_k_accuracy_curve_static(y_true, probs,
                                 title="Recommender top-K accuracy")
plt.show()''',

    "dataviz.classification.multiclass_extra.top_k_accuracy_curve_interactive": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.multiclass_extra import top_k_accuracy_curve_interactive

rng = np.random.default_rng(42)
# 6-class product recommender: does the right item appear in the top-K?
n = 120
n_classes = 6
y_true = rng.integers(0, n_classes, n)
logits = rng.normal(0, 1, (n, n_classes))
logits[np.arange(n), y_true] += 2.2  # model signal on the true class
probs = np.exp(logits) / np.exp(logits).sum(axis=1, keepdims=True)

fig = top_k_accuracy_curve_interactive(y_true, probs,
                                       title="Recommender top-K accuracy")
fig.show()''',

    "dataviz.classification.multiclass_extra.confusion_sankey_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.multiclass_extra import confusion_sankey_static

rng = np.random.default_rng(42)
# 3-stage fault classifier: true vs predicted flow
n = 120
labels = ["minor", "major", "critical"]
y_true = np.array([labels[i] for i in rng.integers(0, 3, n)])
flip = rng.random(n) < 0.18  # 18% of cases are misclassified
y_pred = y_true.copy()
y_pred[flip] = np.array([labels[i] for i in rng.integers(0, 3, flip.sum())])

ax = confusion_sankey_static(y_true, y_pred, labels=labels,
                             title="Fault triage: true vs predicted flow")
plt.show()''',

    "dataviz.classification.multiclass_extra.confusion_sankey_interactive": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.multiclass_extra import confusion_sankey_interactive

rng = np.random.default_rng(42)
# 3-stage fault classifier: true vs predicted flow
n = 120
labels = ["minor", "major", "critical"]
y_true = np.array([labels[i] for i in rng.integers(0, 3, n)])
flip = rng.random(n) < 0.18  # 18% of cases are misclassified
y_pred = y_true.copy()
y_pred[flip] = np.array([labels[i] for i in rng.integers(0, 3, flip.sum())])

fig = confusion_sankey_interactive(y_true, y_pred, labels=labels,
                                   title="Fault triage: true vs predicted flow")
fig.show()''',

    # ------------------------------------------------------------ multilabel.py
    "dataviz.classification.multilabel.multilabel_confusion_grid_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.multilabel import multilabel_confusion_grid_static

rng = np.random.default_rng(42)
# multilabel movie-tagging model: 5 genre tags, 120 movies
n, n_labels = 120, 5
labels = ["action", "comedy", "drama", "romance", "scifi"]
Y_true = (rng.random((n, n_labels)) < 0.3).astype(int)
noise = rng.random((n, n_labels)) < 0.12
Y_pred = np.where(noise, 1 - Y_true, Y_true)

axes = multilabel_confusion_grid_static(Y_true, Y_pred, labels=labels,
                                        title="Movie tagger: per-tag matrices")
plt.show()''',

    "dataviz.classification.multilabel.multilabel_confusion_grid_interactive": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.multilabel import multilabel_confusion_grid_interactive

rng = np.random.default_rng(42)
# multilabel movie-tagging model: 5 genre tags, 120 movies
n, n_labels = 120, 5
labels = ["action", "comedy", "drama", "romance", "scifi"]
Y_true = (rng.random((n, n_labels)) < 0.3).astype(int)
noise = rng.random((n, n_labels)) < 0.12
Y_pred = np.where(noise, 1 - Y_true, Y_true)

fig = multilabel_confusion_grid_interactive(Y_true, Y_pred, labels=labels,
                                            title="Movie tagger: per-tag matrices")
fig.show()''',

    "dataviz.classification.multilabel.label_cooccurrence_heatmap_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.multilabel import label_cooccurrence_heatmap_static

rng = np.random.default_rng(42)
# symptom tags on clinic visits; "fever" and "cough" co-occur often
n = 150
labels = ["fever", "cough", "fatigue", "nausea", "rash"]
base = rng.random((n, len(labels)))
Y = (base < 0.25).astype(int)
pair = rng.random(n) < 0.6
Y[pair, 0] = 1
Y[pair, 1] = 1

ax = label_cooccurrence_heatmap_static(Y, labels=labels,
                                       title="Symptom tag co-occurrence (Jaccard)")
plt.show()''',

    "dataviz.classification.multilabel.label_cooccurrence_heatmap_interactive": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.multilabel import label_cooccurrence_heatmap_interactive

rng = np.random.default_rng(42)
# symptom tags on clinic visits; "fever" and "cough" co-occur often
n = 150
labels = ["fever", "cough", "fatigue", "nausea", "rash"]
base = rng.random((n, len(labels)))
Y = (base < 0.25).astype(int)
pair = rng.random(n) < 0.6
Y[pair, 0] = 1
Y[pair, 1] = 1

fig = label_cooccurrence_heatmap_interactive(Y, labels=labels,
                                             title="Symptom tag co-occurrence (Jaccard)")
fig.show()''',

    "dataviz.classification.multilabel.hamming_subset_accuracy_bar_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.multilabel import hamming_subset_accuracy_bar_static

rng = np.random.default_rng(42)
# multilabel movie tagger: per-tag accuracy vs exact full-tag-set accuracy
n, n_labels = 120, 5
Y_true = (rng.random((n, n_labels)) < 0.3).astype(int)
noise = rng.random((n, n_labels)) < 0.09
Y_pred = np.where(noise, 1 - Y_true, Y_true)

ax = hamming_subset_accuracy_bar_static(
    Y_true, Y_pred, title="Movie tagger: Hamming vs subset accuracy")
plt.show()''',

    "dataviz.classification.multilabel.hamming_subset_accuracy_bar_interactive": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.multilabel import hamming_subset_accuracy_bar_interactive

rng = np.random.default_rng(42)
# multilabel movie tagger: per-tag accuracy vs exact full-tag-set accuracy
n, n_labels = 120, 5
Y_true = (rng.random((n, n_labels)) < 0.3).astype(int)
noise = rng.random((n, n_labels)) < 0.09
Y_pred = np.where(noise, 1 - Y_true, Y_true)

fig = hamming_subset_accuracy_bar_interactive(
    Y_true, Y_pred, title="Movie tagger: Hamming vs subset accuracy")
fig.show()''',

    # ---------------------------------------------------------------- report.py
    "dataviz.classification.report.classification_report_heatmap_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.report import classification_report_heatmap_static

rng = np.random.default_rng(42)
# 4-class land-cover classifier on satellite tiles
n = 160
labels = ["forest", "water", "urban", "crops"]
y_true = np.array([labels[i] for i in rng.integers(0, 4, n)])
err = rng.random(n) < 0.15
y_pred = y_true.copy()
y_pred[err] = np.array([labels[i] for i in rng.integers(0, 4, err.sum())])

ax = classification_report_heatmap_static(
    y_true, y_pred, labels=labels,
    title="Land-cover classifier: per-class report")
plt.show()''',

    "dataviz.classification.report.classification_report_heatmap_interactive": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.report import classification_report_heatmap_interactive

rng = np.random.default_rng(42)
# 4-class land-cover classifier on satellite tiles
n = 160
labels = ["forest", "water", "urban", "crops"]
y_true = np.array([labels[i] for i in rng.integers(0, 4, n)])
err = rng.random(n) < 0.15
y_pred = y_true.copy()
y_pred[err] = np.array([labels[i] for i in rng.integers(0, 4, err.sum())])

fig = classification_report_heatmap_interactive(
    y_true, y_pred, labels=labels,
    title="Land-cover classifier: per-class report")
fig.show()''',

    "dataviz.classification.report.per_class_metrics_bar_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.report import per_class_metrics_bar_static

rng = np.random.default_rng(42)
# 4-class land-cover classifier on satellite tiles
n = 160
labels = ["forest", "water", "urban", "crops"]
y_true = np.array([labels[i] for i in rng.integers(0, 4, n)])
err = rng.random(n) < 0.15
y_pred = y_true.copy()
y_pred[err] = np.array([labels[i] for i in rng.integers(0, 4, err.sum())])

ax = per_class_metrics_bar_static(y_true, y_pred, labels=labels,
                                  title="Land-cover classifier: precision / recall / F1")
plt.show()''',

    "dataviz.classification.report.per_class_metrics_bar_interactive": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.report import per_class_metrics_bar_interactive

rng = np.random.default_rng(42)
# 4-class land-cover classifier on satellite tiles
n = 160
labels = ["forest", "water", "urban", "crops"]
y_true = np.array([labels[i] for i in rng.integers(0, 4, n)])
err = rng.random(n) < 0.15
y_pred = y_true.copy()
y_pred[err] = np.array([labels[i] for i in rng.integers(0, 4, err.sum())])

fig = per_class_metrics_bar_interactive(y_true, y_pred, labels=labels,
                                        title="Land-cover classifier: precision / recall / F1")
fig.show()''',

    "dataviz.classification.report.class_balance_bar_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.report import class_balance_bar_static

rng = np.random.default_rng(42)
# imbalanced support-ticket queue: does the model under-predict "urgent"?
labels = ["low", "normal", "high", "urgent"]
y_true = np.array([labels[i] for i in rng.choice(4, 140, p=[0.4, 0.35, 0.18, 0.07])])
y_pred = y_true.copy()
shift = rng.random(140) < 0.2
y_pred[shift] = "normal"  # model collapses rare classes toward "normal"

ax = class_balance_bar_static(y_true, y_pred, labels=labels,
                              title="Ticket priority: true vs predicted balance")
plt.show()''',

    "dataviz.classification.report.class_balance_bar_interactive": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.report import class_balance_bar_interactive

rng = np.random.default_rng(42)
# imbalanced support-ticket queue: does the model under-predict "urgent"?
labels = ["low", "normal", "high", "urgent"]
y_true = np.array([labels[i] for i in rng.choice(4, 140, p=[0.4, 0.35, 0.18, 0.07])])
y_pred = y_true.copy()
shift = rng.random(140) < 0.2
y_pred[shift] = "normal"  # model collapses rare classes toward "normal"

fig = class_balance_bar_interactive(y_true, y_pred, labels=labels,
                                    title="Ticket priority: true vs predicted balance")
fig.show()''',

    "dataviz.classification.report.prediction_distribution_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.report import prediction_distribution_static

rng = np.random.default_rng(42)
# 3-class wine-quality model: where do predictions go per true class?
labels = ["low", "medium", "high"]
y_true = np.array([labels[i] for i in rng.choice(3, 150, p=[0.3, 0.5, 0.2])])
y_pred = y_true.copy()
adjacent = rng.random(150) < 0.22  # errors land on neighbouring grades
idx = {l: k for k, l in enumerate(labels)}
for i in np.where(adjacent)[0]:
    k = idx[y_pred[i]]
    y_pred[i] = labels[min(max(k + rng.choice([-1, 1]), 0), 2)]

ax = prediction_distribution_static(y_true, y_pred, labels=labels,
                                    title="Wine-quality model: predicted share per grade")
plt.show()''',

    "dataviz.classification.report.prediction_distribution_interactive": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.report import prediction_distribution_interactive

rng = np.random.default_rng(42)
# 3-class wine-quality model: where do predictions go per true class?
labels = ["low", "medium", "high"]
y_true = np.array([labels[i] for i in rng.choice(3, 150, p=[0.3, 0.5, 0.2])])
y_pred = y_true.copy()
adjacent = rng.random(150) < 0.22  # errors land on neighbouring grades
idx = {l: k for k, l in enumerate(labels)}
for i in np.where(adjacent)[0]:
    k = idx[y_pred[i]]
    y_pred[i] = labels[min(max(k + rng.choice([-1, 1]), 0), 2)]

fig = prediction_distribution_interactive(y_true, y_pred, labels=labels,
                                          title="Wine-quality model: predicted share per grade")
fig.show()''',

    # ----------------------------------------------------------- score_dist.py
    "dataviz.classification.score_dist.score_distribution_by_class_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.score_dist import score_distribution_by_class_static

rng = np.random.default_rng(42)
# credit-default scorecard: score spread for defaulters vs payers
n = 160
is_default = (rng.random(n) < 0.25).astype(int)
y_true = np.where(is_default == 1, "defaulter", "payer")
y_score = np.clip(
    is_default * rng.beta(6, 3, n) + (1 - is_default) * rng.beta(3, 6, n), 0, 1)

ax = score_distribution_by_class_static(
    y_true, y_score, labels=["payer", "defaulter"], kind="violin",
    title="Credit scorecard: score distribution by outcome")
plt.show()''',

    "dataviz.classification.score_dist.score_distribution_by_class_interactive": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.score_dist import score_distribution_by_class_interactive

rng = np.random.default_rng(42)
# credit-default scorecard: score spread for defaulters vs payers
n = 160
is_default = (rng.random(n) < 0.25).astype(int)
y_true = np.where(is_default == 1, "defaulter", "payer")
y_score = np.clip(
    is_default * rng.beta(6, 3, n) + (1 - is_default) * rng.beta(3, 6, n), 0, 1)

fig = score_distribution_by_class_interactive(
    y_true, y_score, labels=["payer", "defaulter"], kind="violin",
    title="Credit scorecard: score distribution by outcome")
fig.show()''',

    # ------------------------------------------------------------- threshold.py
    "dataviz.classification.threshold.threshold_metric_curve_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.threshold import threshold_metric_curve_static

rng = np.random.default_rng(42)
# churn model: pick an operating threshold balancing precision and recall
n = 150
y_true = (rng.random(n) < 0.3).astype(int)
y_prob = np.clip(
    y_true * rng.beta(6, 2.5, n) + (1 - y_true) * rng.beta(2.5, 6, n), 0, 1)

ax = threshold_metric_curve_static(
    y_true, y_prob,
    metrics=("precision", "recall", "f1", "specificity"),
    title="Churn model: metrics vs threshold")
plt.show()''',

    "dataviz.classification.threshold.threshold_metric_curve_interactive": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.threshold import threshold_metric_curve_interactive

rng = np.random.default_rng(42)
# churn model: pick an operating threshold balancing precision and recall
n = 150
y_true = (rng.random(n) < 0.3).astype(int)
y_prob = np.clip(
    y_true * rng.beta(6, 2.5, n) + (1 - y_true) * rng.beta(2.5, 6, n), 0, 1)

fig = threshold_metric_curve_interactive(
    y_true, y_prob,
    metrics=("precision", "recall", "f1", "specificity"),
    title="Churn model: metrics vs threshold")
fig.show()''',

    "dataviz.classification.threshold.ks_statistic_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.threshold import ks_statistic_plot_static

rng = np.random.default_rng(42)
# credit scorecard: KS separation between defaulters and payers
n = 150
y_true = (rng.random(n) < 0.25).astype(int)
y_prob = np.clip(
    y_true * rng.beta(6, 2.5, n) + (1 - y_true) * rng.beta(2.5, 6, n), 0, 1)

ax = ks_statistic_plot_static(y_true, y_prob,
                              title="Credit scorecard: KS plot")
plt.show()''',

    "dataviz.classification.threshold.ks_statistic_plot_interactive": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.threshold import ks_statistic_plot_interactive

rng = np.random.default_rng(42)
# credit scorecard: KS separation between defaulters and payers
n = 150
y_true = (rng.random(n) < 0.25).astype(int)
y_prob = np.clip(
    y_true * rng.beta(6, 2.5, n) + (1 - y_true) * rng.beta(2.5, 6, n), 0, 1)

fig = ks_statistic_plot_interactive(y_true, y_prob,
                                    title="Credit scorecard: KS plot")
fig.show()''',

    "dataviz.classification.threshold.det_curve_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.threshold import det_curve_static

rng = np.random.default_rng(42)
# biometric access system: DET curve on a probit scale
n = 150
y_true = (rng.random(n) < 0.4).astype(int)
y_prob = np.clip(
    y_true * rng.beta(7, 2.5, n) + (1 - y_true) * rng.beta(2.5, 7, n), 0, 1)

ax = det_curve_static(y_true, y_prob,
                      title="Access system: detection-error tradeoff")
plt.show()''',

    "dataviz.classification.threshold.det_curve_interactive": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.threshold import det_curve_interactive

rng = np.random.default_rng(42)
# biometric access system: DET curve on a probit scale
n = 150
y_true = (rng.random(n) < 0.4).astype(int)
y_prob = np.clip(
    y_true * rng.beta(7, 2.5, n) + (1 - y_true) * rng.beta(2.5, 7, n), 0, 1)

fig = det_curve_interactive(y_true, y_prob,
                            title="Access system: detection-error tradeoff")
fig.show()''',

    "dataviz.classification.threshold.cost_curve_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.threshold import cost_curve_static

rng = np.random.default_rng(42)
# fraud screening: a missed fraud costs 8x a false alarm review
n = 150
y_true = (rng.random(n) < 0.08).astype(int)
y_prob = np.clip(
    y_true * rng.beta(6, 2, n) + (1 - y_true) * rng.beta(2, 8, n), 0, 1)

ax = cost_curve_static(y_true, y_prob, cost_fp=1.0, cost_fn=8.0,
                       title="Fraud screening: total cost vs threshold")
plt.show()''',

    "dataviz.classification.threshold.cost_curve_interactive": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.threshold import cost_curve_interactive

rng = np.random.default_rng(42)
# fraud screening: a missed fraud costs 8x a false alarm review
n = 150
y_true = (rng.random(n) < 0.08).astype(int)
y_prob = np.clip(
    y_true * rng.beta(6, 2, n) + (1 - y_true) * rng.beta(2, 8, n), 0, 1)

fig = cost_curve_interactive(y_true, y_prob, cost_fp=1.0, cost_fn=8.0,
                             title="Fraud screening: total cost vs threshold")
fig.show()''',

    "dataviz.classification.threshold.net_benefit_curve_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.threshold import net_benefit_curve_static

rng = np.random.default_rng(42)
# medical screening: decision-curve analysis vs treat-all / treat-none
n = 150
y_true = (rng.random(n) < 0.2).astype(int)
y_prob = np.clip(
    y_true * rng.beta(6, 2.5, n) + (1 - y_true) * rng.beta(2.5, 6, n), 0, 1)

ax = net_benefit_curve_static(y_true, y_prob,
                              title="Screening test: net benefit")
ax.set_ylim(-0.05, 0.25)
plt.show()''',

    "dataviz.classification.threshold.net_benefit_curve_interactive": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.threshold import net_benefit_curve_interactive

rng = np.random.default_rng(42)
# medical screening: decision-curve analysis vs treat-all / treat-none
n = 150
y_true = (rng.random(n) < 0.2).astype(int)
y_prob = np.clip(
    y_true * rng.beta(6, 2.5, n) + (1 - y_true) * rng.beta(2.5, 6, n), 0, 1)

fig = net_benefit_curve_interactive(y_true, y_prob,
                                    title="Screening test: net benefit")
fig.show()''',

    # ------------------------------------------------------- threshold_extra.py
    "dataviz.classification.threshold_extra.f_beta_curve_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.threshold_extra import f_beta_curve_static

rng = np.random.default_rng(42)
# defect detector: recall-weighted (F2) vs precision-weighted (F0.5) views
n = 150
y_true = (rng.random(n) < 0.3).astype(int)
y_prob = np.clip(
    y_true * rng.beta(6, 2.5, n) + (1 - y_true) * rng.beta(2.5, 6, n), 0, 1)

ax = f_beta_curve_static(y_true, y_prob, betas=(0.5, 1.0, 2.0),
                         title="Defect detector: F-beta vs threshold")
plt.show()''',

    "dataviz.classification.threshold_extra.f_beta_curve_interactive": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.threshold_extra import f_beta_curve_interactive

rng = np.random.default_rng(42)
# defect detector: recall-weighted (F2) vs precision-weighted (F0.5) views
n = 150
y_true = (rng.random(n) < 0.3).astype(int)
y_prob = np.clip(
    y_true * rng.beta(6, 2.5, n) + (1 - y_true) * rng.beta(2.5, 6, n), 0, 1)

fig = f_beta_curve_interactive(y_true, y_prob, betas=(0.5, 1.0, 2.0),
                               title="Defect detector: F-beta vs threshold")
fig.show()''',

    "dataviz.classification.threshold_extra.mcc_curve_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.threshold_extra import mcc_curve_static

rng = np.random.default_rng(42)
# rare-event churn alert: MCC stays informative under imbalance
n = 150
y_true = (rng.random(n) < 0.15).astype(int)
y_prob = np.clip(
    y_true * rng.beta(6, 2, n) + (1 - y_true) * rng.beta(2, 6, n), 0, 1)

ax = mcc_curve_static(y_true, y_prob,
                      title="Churn alert: MCC vs threshold")
plt.show()''',

    "dataviz.classification.threshold_extra.mcc_curve_interactive": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.threshold_extra import mcc_curve_interactive

rng = np.random.default_rng(42)
# rare-event churn alert: MCC stays informative under imbalance
n = 150
y_true = (rng.random(n) < 0.15).astype(int)
y_prob = np.clip(
    y_true * rng.beta(6, 2, n) + (1 - y_true) * rng.beta(2, 6, n), 0, 1)

fig = mcc_curve_interactive(y_true, y_prob,
                            title="Churn alert: MCC vs threshold")
fig.show()''',

    "dataviz.classification.threshold_extra.youden_j_curve_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.threshold_extra import youden_j_curve_static

rng = np.random.default_rng(42)
# screening assay: choose the cut-off maximising Youden's J
n = 150
y_true = (rng.random(n) < 0.3).astype(int)
y_prob = np.clip(
    y_true * rng.beta(6, 2.5, n) + (1 - y_true) * rng.beta(2.5, 6, n), 0, 1)

ax = youden_j_curve_static(y_true, y_prob,
                           title="Screening assay: Youden's J")
plt.show()''',

    "dataviz.classification.threshold_extra.youden_j_curve_interactive": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.threshold_extra import youden_j_curve_interactive

rng = np.random.default_rng(42)
# screening assay: choose the cut-off maximising Youden's J
n = 150
y_true = (rng.random(n) < 0.3).astype(int)
y_prob = np.clip(
    y_true * rng.beta(6, 2.5, n) + (1 - y_true) * rng.beta(2.5, 6, n), 0, 1)

fig = youden_j_curve_interactive(y_true, y_prob,
                                 title="Screening assay: Youden's J")
fig.show()''',

    "dataviz.classification.threshold_extra.balanced_accuracy_curve_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.threshold_extra import balanced_accuracy_curve_static

rng = np.random.default_rng(42)
# imbalanced fraud model: balanced accuracy is fairer than raw accuracy
n = 150
y_true = (rng.random(n) < 0.1).astype(int)
y_prob = np.clip(
    y_true * rng.beta(6, 2, n) + (1 - y_true) * rng.beta(2, 6, n), 0, 1)

ax = balanced_accuracy_curve_static(y_true, y_prob,
                                    title="Fraud model: balanced accuracy")
plt.show()''',

    "dataviz.classification.threshold_extra.balanced_accuracy_curve_interactive": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.threshold_extra import balanced_accuracy_curve_interactive

rng = np.random.default_rng(42)
# imbalanced fraud model: balanced accuracy is fairer than raw accuracy
n = 150
y_true = (rng.random(n) < 0.1).astype(int)
y_prob = np.clip(
    y_true * rng.beta(6, 2, n) + (1 - y_true) * rng.beta(2, 6, n), 0, 1)

fig = balanced_accuracy_curve_interactive(y_true, y_prob,
                                          title="Fraud model: balanced accuracy")
fig.show()''',

    "dataviz.classification.threshold_extra.cohen_kappa_curve_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.threshold_extra import cohen_kappa_curve_static

rng = np.random.default_rng(42)
# churn model: agreement with ground truth beyond chance
n = 150
y_true = (rng.random(n) < 0.3).astype(int)
y_prob = np.clip(
    y_true * rng.beta(6, 2.5, n) + (1 - y_true) * rng.beta(2.5, 6, n), 0, 1)

ax = cohen_kappa_curve_static(y_true, y_prob,
                              title="Churn model: Cohen's kappa vs threshold")
plt.show()''',

    "dataviz.classification.threshold_extra.cohen_kappa_curve_interactive": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.threshold_extra import cohen_kappa_curve_interactive

rng = np.random.default_rng(42)
# churn model: agreement with ground truth beyond chance
n = 150
y_true = (rng.random(n) < 0.3).astype(int)
y_prob = np.clip(
    y_true * rng.beta(6, 2.5, n) + (1 - y_true) * rng.beta(2.5, 6, n), 0, 1)

fig = cohen_kappa_curve_interactive(y_true, y_prob,
                                    title="Churn model: Cohen's kappa vs threshold")
fig.show()''',

    "dataviz.classification.threshold_extra.likelihood_ratio_curve_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.threshold_extra import likelihood_ratio_curve_static

rng = np.random.default_rng(42)
# clinical test: LR+ / LR- inform post-test odds at each cut-off
n = 150
y_true = (rng.random(n) < 0.3).astype(int)
y_prob = np.clip(
    y_true * rng.beta(6, 2.5, n) + (1 - y_true) * rng.beta(2.5, 6, n), 0, 1)

ax = likelihood_ratio_curve_static(y_true, y_prob,
                                   title="Clinical test: likelihood ratios")
plt.show()''',

    "dataviz.classification.threshold_extra.likelihood_ratio_curve_interactive": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.threshold_extra import likelihood_ratio_curve_interactive

rng = np.random.default_rng(42)
# clinical test: LR+ / LR- inform post-test odds at each cut-off
n = 150
y_true = (rng.random(n) < 0.3).astype(int)
y_prob = np.clip(
    y_true * rng.beta(6, 2.5, n) + (1 - y_true) * rng.beta(2.5, 6, n), 0, 1)

fig = likelihood_ratio_curve_interactive(y_true, y_prob,
                                         title="Clinical test: likelihood ratios")
fig.show()''',

    "dataviz.classification.threshold_extra.predictive_value_curve_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.threshold_extra import predictive_value_curve_static

# fixed test characteristics: PPV collapses at low prevalence
ax = predictive_value_curve_static(
    sensitivity=0.92, specificity=0.88,
    prevalences=np.linspace(0.001, 0.5, 150),
    title="Screening test: PPV / NPV vs prevalence")
ax.axvline(0.02, color="grey", linestyle=":", linewidth=1)
plt.show()''',

    "dataviz.classification.threshold_extra.predictive_value_curve_interactive": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.threshold_extra import predictive_value_curve_interactive

# fixed test characteristics: PPV collapses at low prevalence
fig = predictive_value_curve_interactive(
    sensitivity=0.92, specificity=0.88,
    prevalences=np.linspace(0.001, 0.5, 150),
    title="Screening test: PPV / NPV vs prevalence")
fig.show()''',

    # -------------------------------------------------------------- training.py
    "dataviz.classification.training.validation_curve_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.training import validation_curve_static

rng = np.random.default_rng(42)
# random-forest depth sweep with 5-fold CV on a churn dataset
depths = np.array([2, 4, 6, 8, 10, 12])
train_scores = np.array([
    [0.71, 0.70, 0.72, 0.71, 0.70],
    [0.78, 0.77, 0.79, 0.78, 0.77],
    [0.85, 0.84, 0.86, 0.85, 0.84],
    [0.91, 0.90, 0.92, 0.91, 0.90],
    [0.95, 0.94, 0.96, 0.95, 0.94],
    [0.97, 0.96, 0.98, 0.97, 0.96],
])
val_scores = np.array([
    [0.68, 0.67, 0.69, 0.68, 0.67],
    [0.74, 0.73, 0.75, 0.74, 0.72],
    [0.79, 0.78, 0.80, 0.79, 0.77],
    [0.81, 0.80, 0.82, 0.81, 0.79],
    [0.80, 0.79, 0.81, 0.80, 0.78],
    [0.78, 0.77, 0.79, 0.78, 0.76],
])

ax = validation_curve_static(depths, train_scores, val_scores,
                             param_name="max_depth",
                             title="Churn RF: validation curve")
plt.show()''',

    "dataviz.classification.training.validation_curve_interactive": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.training import validation_curve_interactive

rng = np.random.default_rng(42)
# random-forest depth sweep with 5-fold CV on a churn dataset
depths = np.array([2, 4, 6, 8, 10, 12])
train_scores = np.array([
    [0.71, 0.70, 0.72, 0.71, 0.70],
    [0.78, 0.77, 0.79, 0.78, 0.77],
    [0.85, 0.84, 0.86, 0.85, 0.84],
    [0.91, 0.90, 0.92, 0.91, 0.90],
    [0.95, 0.94, 0.96, 0.95, 0.94],
    [0.97, 0.96, 0.98, 0.97, 0.96],
])
val_scores = np.array([
    [0.68, 0.67, 0.69, 0.68, 0.67],
    [0.74, 0.73, 0.75, 0.74, 0.72],
    [0.79, 0.78, 0.80, 0.79, 0.77],
    [0.81, 0.80, 0.82, 0.81, 0.79],
    [0.80, 0.79, 0.81, 0.80, 0.78],
    [0.78, 0.77, 0.79, 0.78, 0.76],
])

fig = validation_curve_interactive(depths, train_scores, val_scores,
                                   param_name="max_depth",
                                   title="Churn RF: validation curve")
fig.show()''',

    "dataviz.classification.training.cv_score_boxplot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.training import cv_score_boxplot_static

rng = np.random.default_rng(42)
# 10-fold CV F1 scores for four churn model candidates
cv_scores = {
    "logreg": rng.normal(0.72, 0.03, 10),
    "random forest": rng.normal(0.79, 0.025, 10),
    "gradient boost": rng.normal(0.81, 0.02, 10),
    "naive bayes": rng.normal(0.66, 0.04, 10),
}

ax = cv_score_boxplot_static(cv_scores,
                             title="Churn models: 10-fold CV F1")
plt.show()''',

    "dataviz.classification.training.cv_score_boxplot_interactive": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.training import cv_score_boxplot_interactive

rng = np.random.default_rng(42)
# 10-fold CV F1 scores for four churn model candidates
cv_scores = {
    "logreg": rng.normal(0.72, 0.03, 10),
    "random forest": rng.normal(0.79, 0.025, 10),
    "gradient boost": rng.normal(0.81, 0.02, 10),
    "naive bayes": rng.normal(0.66, 0.04, 10),
}

fig = cv_score_boxplot_interactive(cv_scores,
                                   title="Churn models: 10-fold CV F1")
fig.show()''',

    "dataviz.classification.training.training_history_curve_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.training import training_history_curve_static

# neural churn classifier: 40-epoch log-loss history
epochs = np.arange(1, 41)
loss = 0.9 * np.exp(-epochs / 9.0) + 0.32
val_loss = 0.9 * np.exp(-epochs / 8.0) + 0.36 + np.maximum(epochs - 25, 0) * 0.004
history = {"loss": loss.tolist(), "val_loss": val_loss.tolist()}

ax = training_history_curve_static(history,
                                   title="Churn MLP: training history")
plt.show()''',

    "dataviz.classification.training.training_history_curve_interactive": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.classification.training import training_history_curve_interactive

# neural churn classifier: 40-epoch log-loss history
epochs = np.arange(1, 41)
loss = 0.9 * np.exp(-epochs / 9.0) + 0.32
val_loss = 0.9 * np.exp(-epochs / 8.0) + 0.36 + np.maximum(epochs - 25, 0) * 0.004
history = {"loss": loss.tolist(), "val_loss": val_loss.tolist()}

fig = training_history_curve_interactive(history,
                                         title="Churn MLP: training history")
fig.show()''',
}
