"""Generate example PNGs for the documentation gallery.

Run from the repository root:

    python docs/_tools/generate_examples.py

Generated files land under ``docs/source/_static/examples/`` and are committed
to the repository. The script is intentionally self-contained and uses only
synthetic data so it can be regenerated deterministically.
"""

from __future__ import annotations

import os
import sys
import traceback
from pathlib import Path

os.environ.setdefault("MPLBACKEND", "Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import dataviz as dv

OUT = Path(__file__).resolve().parents[1] / "source" / "_static" / "examples"
OUT.mkdir(parents=True, exist_ok=True)

rng = np.random.default_rng(0)


def save(ax_or_fig, name: str) -> None:
    fig = ax_or_fig.figure if hasattr(ax_or_fig, "figure") else ax_or_fig
    fig.set_size_inches(7.5, 4.5)
    fig.tight_layout()
    fig.savefig(OUT / f"{name}.png", dpi=130, bbox_inches="tight")
    plt.close(fig)


# --- Univariate -------------------------------------------------------------
def ex_histogram():
    values = rng.normal(loc=12.5, scale=0.6, size=400)
    ax = dv.histogram_static(values, bins=30, title="Cycle-time distribution")
    ax.set_xlabel("Cycle time (s)")
    save(ax, "univariate_histogram")


def ex_density():
    values = pd.Series(rng.normal(loc=0, scale=1, size=500), name="z-score")
    ax = dv.density_static(values, fill=False, title="Kernel density estimate")
    save(ax, "univariate_density")


def ex_box_plot():
    values = pd.Series(rng.gamma(2.0, 1.5, size=300), name="Service time (min)")
    ax = dv.box_plot_static(values, title="Service-time spread")
    save(ax, "univariate_box_plot")


def ex_violin_plot():
    values = pd.Series(rng.normal(0, 1, size=400), name="Standardized score")
    ax = dv.violin_plot_static(values, title="Score distribution shape")
    save(ax, "univariate_violin_plot")


def ex_ecdf():
    values = pd.Series(rng.exponential(scale=3, size=300), name="Wait time (min)")
    ax = dv.ecdf_plot_static(values, title="Empirical CDF of wait times")
    save(ax, "univariate_ecdf")


def ex_qq_plot():
    values = pd.Series(rng.normal(0, 1, size=200), name="Sample")
    ax = dv.qq_plot_static(values, title="Q-Q plot vs. normal")
    save(ax, "univariate_qq")


def ex_cumulative_histogram():
    values = pd.Series(rng.normal(50, 10, size=500), name="Latency (ms)")
    ax = dv.cumulative_histogram_static(values, bins=40, title="Cumulative latency")
    save(ax, "univariate_cumhist")


def ex_outlier_plot():
    base = rng.normal(0, 1, size=200)
    outliers = np.array([6.0, -5.5, 7.2])
    values = pd.Series(np.concatenate([base, outliers]), name="Measurement")
    ax = dv.outlier_plot_static(values, title="Outlier inspection")
    save(ax, "univariate_outlier")


def ex_strip():
    values = pd.Series(rng.normal(size=80), name="Score")
    ax = dv.strip_plot_static(values, title="Strip plot")
    save(ax, "univariate_strip")


def ex_dot_plot():
    values = pd.Series(rng.integers(1, 11, size=40), name="Rating")
    ax = dv.dot_plot_static(values, title="Dot plot of ratings")
    save(ax, "univariate_dot")


def ex_lollipop():
    s = pd.Series(rng.integers(10, 100, size=8),
                  index=[f"item{i}" for i in range(8)],
                  name="Count")
    ax = dv.lollipop_chart_static(s, title="Lollipop chart")
    save(ax, "univariate_lollipop")


def ex_lorenz():
    values = pd.Series(rng.exponential(scale=10, size=200), name="Income")
    ax = dv.lorenz_curve_static(values, title="Lorenz curve of income")
    save(ax, "univariate_lorenz")


def ex_ridgeline():
    df = pd.DataFrame({
        "group_A": rng.normal(-2, 1, size=200),
        "group_B": rng.normal(0, 1, size=200),
        "group_C": rng.normal(2, 1, size=200),
        "group_D": rng.normal(4, 1, size=200),
    })
    ax = dv.ridgeline_plot_static(df, title="Ridgeline plot by group")
    save(ax, "univariate_ridgeline")


def ex_frequency_bar():
    values = pd.Series(rng.choice(list("ABCDE"), size=200, p=[0.4, 0.25, 0.15, 0.12, 0.08]),
                       name="Category")
    ax = dv.frequency_bar_static(values, title="Category frequencies")
    save(ax, "univariate_frequency_bar")


# --- Bivariate --------------------------------------------------------------
def ex_scatter():
    x = pd.Series(rng.normal(size=300), name="Feature X")
    y = pd.Series(2.0 * x + rng.normal(scale=0.5, size=300), name="Target Y")
    ax = dv.scatter_plot_static(x, y, title="Feature vs. target")
    save(ax, "bivariate_scatter")


def ex_line():
    t = pd.Series(np.arange(180), name="Day")
    y = pd.Series(np.cumsum(rng.normal(0, 1, size=180)) + 50, name="Index value")
    ax = dv.line_plot_static(t, y, title="Index over time")
    save(ax, "bivariate_line")


def ex_correlation_heatmap():
    df = pd.DataFrame(rng.normal(size=(200, 6)),
                      columns=[f"f{i}" for i in range(6)])
    df["target"] = df["f0"] * 1.5 + df["f1"] * -0.7 + rng.normal(size=200)
    ax = dv.correlation_heatmap_static(df, title="Feature correlation matrix")
    save(ax, "bivariate_correlation")


def ex_hexbin():
    x = pd.Series(rng.normal(size=5000), name="X")
    y = pd.Series(0.5 * x + rng.normal(scale=0.8, size=5000), name="Y")
    ax = dv.hexbin_plot_static(x, y, gridsize=30, title="Hexbin density")
    save(ax, "bivariate_hexbin")


def ex_regression():
    x = pd.Series(np.linspace(0, 10, 120), name="Hours studied")
    y = pd.Series(3 + 1.2 * x + rng.normal(scale=1.5, size=120), name="Exam score")
    ax = dv.regression_plot_static(x, y, title="Hours vs. score (OLS fit)")
    save(ax, "bivariate_regression")


def ex_bubble():
    x = pd.Series(rng.normal(size=80), name="Marketing spend")
    y = pd.Series(2 * x + rng.normal(size=80), name="Revenue")
    sizes = rng.integers(20, 500, size=80).astype(float)
    ax = dv.bubble_plot_static(x, y, size=sizes,
                               title="Spend vs. revenue (sized by customers)")
    save(ax, "bivariate_bubble")


def ex_grouped_bar():
    category = pd.Series(["Q1", "Q2", "Q3", "Q4"] * 12, name="Quarter")
    values = pd.Series(rng.integers(80, 200, size=48), name="Revenue")
    ax = dv.grouped_bar_static(category, values,
                               title="Average revenue by quarter")
    save(ax, "bivariate_grouped_bar")


def ex_step_plot():
    t = pd.Series(np.arange(50), name="Day")
    y = pd.Series(np.cumsum(rng.integers(-2, 3, size=50)) + 100, name="Inventory")
    ax = dv.step_plot_static(t, y, title="Daily inventory level")
    save(ax, "bivariate_step")


def ex_bland_altman():
    a = pd.Series(rng.normal(100, 15, size=80), name="Device A")
    b = a + rng.normal(0, 3, size=80)
    ax = dv.bland_altman_static(a, b, title="Bland-Altman agreement")
    save(ax, "bivariate_bland_altman")


def ex_box_by_category():
    category = pd.Series(rng.choice(["A", "B", "C"], size=300), name="Group")
    values = pd.Series(rng.normal(size=300), name="Value")
    ax = dv.box_by_category_static(category, values,
                                   title="Value distribution by group")
    save(ax, "bivariate_box_by_category")


def ex_errorbar():
    x = pd.Series(np.arange(10), name="Day")
    y = pd.Series(rng.normal(loc=10, scale=1.5, size=10), name="Measurement")
    err = pd.Series(np.abs(rng.normal(scale=0.5, size=10)), name="Error")
    ax = dv.errorbar_plot_static(x, y, yerr=err,
                                 title="Measurement with uncertainty")
    save(ax, "bivariate_errorbar")


def ex_lag_plot():
    series = pd.Series(np.cumsum(rng.normal(size=200)), name="Signal")
    ax = dv.lag_plot_static(series, series, lag=1, title="Lag-1 plot")
    save(ax, "bivariate_lag")


# --- Multivariate -----------------------------------------------------------
def ex_heatmap():
    df = pd.DataFrame(rng.normal(size=(12, 8)),
                      index=[f"row{i}" for i in range(12)],
                      columns=[f"col{i}" for i in range(8)])
    ax = dv.multivariate.heatmap_static(df, title="Value heatmap")
    save(ax, "multivariate_heatmap")


def ex_pairplot():
    df = pd.DataFrame(rng.normal(size=(150, 4)),
                      columns=["alpha", "beta", "gamma", "delta"])
    df["alpha"] += df["beta"] * 0.5
    fig = dv.multivariate.pairplot_static(df, title="Pairwise feature view")
    save(fig, "multivariate_pairplot")


def ex_parallel_coordinates():
    df = pd.DataFrame(rng.normal(size=(120, 5)),
                      columns=["feat_a", "feat_b", "feat_c", "feat_d", "feat_e"])
    ax = dv.multivariate.parallel_coordinates_static(
        df, title="Parallel coordinates")
    save(ax, "multivariate_parallel")


# --- EDA --------------------------------------------------------------------
def ex_missing_data():
    df = pd.DataFrame(rng.normal(size=(100, 6)), columns=list("ABCDEF"))
    mask = rng.random(df.shape) < 0.15
    df = df.mask(mask)
    ax = dv.missing_data_plot_static(df, title="Missingness map")
    save(ax, "eda_missing")


def ex_distribution_summary():
    df = pd.DataFrame({
        "x1": rng.normal(0, 1, size=300),
        "x2": rng.exponential(1.0, size=300),
        "x3": rng.gamma(2.0, 1.0, size=300),
    })
    ax = dv.distribution_summary_static(df,
                                        title="Distribution summary across features")
    save(ax, "eda_distribution_summary")


def ex_class_distribution():
    labels = pd.Series(rng.choice(["healthy", "warning", "fault"],
                                  size=400, p=[0.7, 0.2, 0.1]),
                       name="Status")
    ax = dv.class_distribution_static(labels, title="Class balance")
    save(ax, "eda_class_distribution")


# --- SPC --------------------------------------------------------------------
def ex_control_chart():
    values = pd.Series(rng.normal(10, 0.5, size=60), name="Diameter (mm)")
    ax = dv.control_chart_static(values, title="Individuals control chart")
    save(ax, "spc_control")


def ex_x_range_chart():
    values = pd.Series(rng.normal(10, 0.5, size=150), name="Measurement")
    ax = dv.x_range_chart_static(values, subgroup_size=5,
                                 title="X-bar / R chart")
    save(ax, "spc_x_range")


def ex_run_chart():
    values = pd.Series(rng.normal(50, 3, size=80), name="Throughput")
    ax = dv.run_chart_static(values, title="Daily throughput run chart")
    save(ax, "spc_run")


def ex_rule_violations():
    values = pd.Series(rng.normal(0, 1, size=40))
    values.iloc[20:25] += 2.5
    ax = dv.rule_violation_chart_static(values,
                                        title="Western Electric rule violations")
    save(ax, "spc_rules")


def ex_capability_histogram():
    values = pd.Series(rng.normal(10, 0.3, size=300), name="Critical dimension")
    ax = dv.capability_histogram_static(values, lsl=9.0, usl=11.0,
                                        title="Process capability")
    save(ax, "spc_capability")


def ex_moving_range_chart():
    values = pd.Series(rng.normal(20, 1.5, size=50), name="Pressure (psi)")
    ax = dv.moving_range_chart_static(values, title="Moving range chart")
    save(ax, "spc_moving_range")


def ex_ewma_chart():
    values = pd.Series(rng.normal(10, 0.5, size=80))
    values.iloc[50:] += 0.6
    ax = dv.ewma_chart_static(values, lambda_=0.2,
                              title="EWMA chart, small shift")
    save(ax, "spc_ewma")


def ex_cusum_chart():
    values = pd.Series(rng.normal(0, 1, size=60))
    values.iloc[30:] += 0.7
    ax = dv.cusum_chart_static(values, target=0.0, title="CUSUM chart")
    save(ax, "spc_cusum")


# --- Regression -------------------------------------------------------------
def ex_residual():
    n = 200
    x = rng.normal(size=n)
    y_true = 2 * x + 1
    y_pred = y_true + rng.normal(scale=0.5, size=n)
    ax = dv.residual_plot_static(y_true, y_pred, title="Residuals vs. fitted")
    save(ax, "regression_residual")


def ex_prediction():
    n = 200
    y_true = rng.normal(size=n)
    y_pred = y_true + rng.normal(scale=0.3, size=n)
    ax = dv.prediction_plot_static(y_true, y_pred, title="Predicted vs. actual")
    save(ax, "regression_prediction")


def ex_learning_curve():
    sizes = np.linspace(50, 500, 10).astype(int)
    train = 1 - 0.4 * np.exp(-sizes / 200) + rng.normal(scale=0.01, size=10)
    val = 1 - 0.6 * np.exp(-sizes / 200) + rng.normal(scale=0.02, size=10)
    ax = dv.learning_curve_static(sizes, train, val, title="Learning curve")
    save(ax, "regression_learning")


# --- Classification ---------------------------------------------------------
def ex_confusion_matrix():
    y_true = rng.choice([0, 1, 2], size=200, p=[0.5, 0.3, 0.2])
    y_pred = y_true.copy()
    flip = rng.random(200) < 0.15
    y_pred[flip] = rng.choice([0, 1, 2], size=flip.sum())
    cm = np.zeros((3, 3), dtype=int)
    for t, p in zip(y_true, y_pred):
        cm[t, p] += 1
    ax = dv.confusion_matrix_plot_static(cm, labels=["A", "B", "C"],
                                         title="Confusion matrix")
    save(ax, "classification_confusion")


def ex_roc():
    fpr = np.sort(rng.random(50))
    tpr = np.clip(fpr + 0.2 + rng.normal(scale=0.05, size=50), 0, 1)
    auc_val = float(np.trapezoid(tpr, fpr))
    ax = dv.roc_curve_static(fpr, tpr, auc=auc_val, title="ROC curve")
    save(ax, "classification_roc")


def ex_pr_curve():
    recall = np.linspace(0, 1, 50)
    precision = np.clip(1 - 0.5 * recall + rng.normal(scale=0.05, size=50), 0, 1)
    ax = dv.precision_recall_curve_static(recall, precision,
                                          title="Precision-recall curve")
    save(ax, "classification_pr")


# --- Clustering -------------------------------------------------------------
def ex_scatter_clusters():
    n = 300
    centers = [(-3, -3), (0, 0), (3, 3)]
    points, labels = [], []
    for i, (cx, cy) in enumerate(centers):
        pts = rng.normal(loc=(cx, cy), scale=0.8, size=(n // 3, 2))
        points.append(pts)
        labels.extend([i] * (n // 3))
    pts_arr = np.vstack(points)
    ax = dv.clustering.scatter_clusters_static(
        x=pts_arr[:, 0], y=pts_arr[:, 1], labels=np.array(labels),
        title="K-means cluster assignments")
    save(ax, "clustering_scatter")


def ex_elbow():
    k = np.arange(1, 11)
    inertia = 1000 * np.exp(-k / 3) + rng.normal(scale=10, size=10)
    ax = dv.clustering.elbow_plot_static(k, inertia,
                                         title="Elbow plot for k selection")
    save(ax, "clustering_elbow")


def ex_dendrogram():
    from scipy.cluster.hierarchy import linkage
    data = rng.normal(size=(20, 4))
    Z = linkage(data, method="ward")
    ax = dv.clustering.dendrogram_static(Z,
                                         title="Hierarchical clustering dendrogram")
    save(ax, "clustering_dendrogram")


# --- XAI --------------------------------------------------------------------
def ex_feature_importance():
    features = [f"feat_{i}" for i in range(8)]
    importances = pd.Series(np.sort(rng.exponential(1.0, size=8))[::-1],
                            index=features, name="importance")
    ax = dv.xai.feature_importance_static(importances,
                                          title="Permutation feature importance")
    save(ax, "xai_feature_importance")


def ex_shap():
    features = [f"feat_{i}" for i in range(6)]
    shap_values = rng.normal(size=(80, 6))
    ax = dv.xai.shap_plot_static(shap_values, features, title="SHAP summary")
    save(ax, "xai_shap")


def ex_partial_dependence():
    grid = np.linspace(-3, 3, 50)
    pdp = np.tanh(grid) + rng.normal(scale=0.05, size=50)
    ax = dv.xai.partial_dependence_static(grid, pdp, feature_name="feat_0",
                                          title="Partial dependence")
    save(ax, "xai_partial_dependence")


EXAMPLES = [
    ("univariate_histogram", ex_histogram),
    ("univariate_density", ex_density),
    ("univariate_box_plot", ex_box_plot),
    ("univariate_violin_plot", ex_violin_plot),
    ("univariate_ecdf", ex_ecdf),
    ("univariate_qq", ex_qq_plot),
    ("univariate_cumhist", ex_cumulative_histogram),
    ("univariate_outlier", ex_outlier_plot),
    ("univariate_strip", ex_strip),
    ("univariate_dot", ex_dot_plot),
    ("univariate_lollipop", ex_lollipop),
    ("univariate_lorenz", ex_lorenz),
    ("univariate_ridgeline", ex_ridgeline),
    ("univariate_frequency_bar", ex_frequency_bar),

    ("bivariate_scatter", ex_scatter),
    ("bivariate_line", ex_line),
    ("bivariate_correlation", ex_correlation_heatmap),
    ("bivariate_hexbin", ex_hexbin),
    ("bivariate_regression", ex_regression),
    ("bivariate_bubble", ex_bubble),
    ("bivariate_grouped_bar", ex_grouped_bar),
    ("bivariate_step", ex_step_plot),
    ("bivariate_bland_altman", ex_bland_altman),
    ("bivariate_box_by_category", ex_box_by_category),
    ("bivariate_errorbar", ex_errorbar),
    ("bivariate_lag", ex_lag_plot),

    ("multivariate_heatmap", ex_heatmap),
    ("multivariate_pairplot", ex_pairplot),
    ("multivariate_parallel", ex_parallel_coordinates),

    ("eda_missing", ex_missing_data),
    ("eda_distribution_summary", ex_distribution_summary),
    ("eda_class_distribution", ex_class_distribution),

    ("spc_control", ex_control_chart),
    ("spc_x_range", ex_x_range_chart),
    ("spc_run", ex_run_chart),
    ("spc_rules", ex_rule_violations),
    ("spc_capability", ex_capability_histogram),
    ("spc_moving_range", ex_moving_range_chart),
    ("spc_ewma", ex_ewma_chart),
    ("spc_cusum", ex_cusum_chart),

    ("regression_residual", ex_residual),
    ("regression_prediction", ex_prediction),
    ("regression_learning", ex_learning_curve),

    ("classification_confusion", ex_confusion_matrix),
    ("classification_roc", ex_roc),
    ("classification_pr", ex_pr_curve),

    ("clustering_scatter", ex_scatter_clusters),
    ("clustering_elbow", ex_elbow),
    ("clustering_dendrogram", ex_dendrogram),

    ("xai_feature_importance", ex_feature_importance),
    ("xai_shap", ex_shap),
    ("xai_partial_dependence", ex_partial_dependence),
]


def main() -> int:
    failures = []
    for name, fn in EXAMPLES:
        try:
            fn()
            print(f"OK   {name}")
        except Exception as exc:
            print(f"FAIL {name}: {exc}")
            failures.append(name)
    print(f"\nGenerated {len(EXAMPLES) - len(failures)} / {len(EXAMPLES)} images.")
    if failures:
        print("Failed:", ", ".join(failures))
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
