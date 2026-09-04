"""Curated rich examples for xai member pages."""

EXAMPLES = {
    "dataviz.xai.charts.feature_importance": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.xai.charts import feature_importance

rng = np.random.default_rng(42)
features = [
    "credit_score", "debt_to_income", "payment_history", "utilization",
    "annual_income", "loan_amount", "account_age", "inquiries_6m",
]
weights = np.array([0.31, 0.22, 0.17, 0.11, 0.08, 0.05, 0.04, 0.02])
importances = pd.Series(
    weights + rng.normal(0, 0.004, size=len(features)), index=features
)

ax = feature_importance(
    importances,
    title="Credit-Risk Model: Gradient-Boosting Feature Importance",
    top_n=8,
)
ax.set_xlabel("Mean decrease in impurity")
plt.show()''',
    "dataviz.xai.charts.shap_plot": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.charts import shap_plot

rng = np.random.default_rng(42)
features = [
    "tenure_months", "monthly_charges", "support_tickets", "contract_type",
    "num_products", "payment_delay", "usage_score", "discount_pct",
]
scales = np.array([0.45, 0.30, 0.22, 0.15, 0.10, 0.07, 0.05, 0.03])
shap_values = rng.normal(0.0, scales, size=(80, len(features)))

ax = shap_plot(
    shap_values,
    features,
    title="SHAP Feature Impact: Subscription Churn Model",
    color="teal",
)
plt.show()''',
    "dataviz.xai.charts.partial_dependence": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.charts import partial_dependence

grid = np.linspace(300, 850, 40)
pred_default = 1.0 / (1.0 + np.exp((grid - 580.0) / 60.0))

ax = partial_dependence(
    grid,
    pred_default,
    feature_name="Credit score",
    title="Partial Dependence of Default Risk on Credit Score",
    color="darkred",
    linewidth=2,
)
ax.set_ylabel("P(default)")
plt.show()''',
    "dataviz.xai.cohort.importance_by_segment_heatmap_static": '''import matplotlib.pyplot as plt
from dataviz.xai.cohort import importance_by_segment_heatmap_static

features = [
    "credit_score", "debt_to_income", "utilization",
    "annual_income", "loan_amount", "account_age",
]
importances = {
    "Prime (score >= 740)": dict(zip(features, [0.34, 0.18, 0.16, 0.14, 0.10, 0.08])),
    "Near-prime (660-739)": dict(zip(features, [0.28, 0.24, 0.19, 0.11, 0.11, 0.07])),
    "Subprime (< 660)": dict(zip(features, [0.19, 0.30, 0.22, 0.09, 0.12, 0.08])),
    "Thin file": dict(zip(features, [0.12, 0.21, 0.18, 0.20, 0.17, 0.12])),
}

ax = importance_by_segment_heatmap_static(
    importances,
    title="Feature Importance by Applicant Segment",
    cmap="viridis",
)
plt.show()''',
    "dataviz.xai.cohort.importance_by_segment_heatmap_interactive": '''import matplotlib.pyplot as plt
from dataviz.xai.cohort import importance_by_segment_heatmap_interactive

features = [
    "credit_score", "debt_to_income", "utilization",
    "annual_income", "loan_amount", "account_age",
]
importances = {
    "Prime (score >= 740)": dict(zip(features, [0.34, 0.18, 0.16, 0.14, 0.10, 0.08])),
    "Near-prime (660-739)": dict(zip(features, [0.28, 0.24, 0.19, 0.11, 0.11, 0.07])),
    "Subprime (< 660)": dict(zip(features, [0.19, 0.30, 0.22, 0.09, 0.12, 0.08])),
    "Thin file": dict(zip(features, [0.12, 0.21, 0.18, 0.20, 0.17, 0.12])),
}

fig = importance_by_segment_heatmap_interactive(
    importances,
    title="Feature Importance by Applicant Segment",
    height=560,
)
fig.show()''',
    "dataviz.xai.cohort.shap_cluster_heatmap_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.cohort import shap_cluster_heatmap_static

rng = np.random.default_rng(42)
features = [
    "credit_score", "debt_to_income", "utilization",
    "annual_income", "loan_amount", "account_age",
]
prototypes = np.array([
    [0.9, -0.4, 0.3, 0.1, -0.2, 0.0],
    [-0.6, 0.8, -0.5, 0.2, 0.1, -0.1],
    [0.2, -0.2, 0.7, -0.5, 0.4, 0.2],
    [-0.3, 0.1, -0.2, 0.6, -0.3, 0.5],
])
shap_values = np.vstack(
    [p + rng.normal(0, 0.08, size=(20, len(features))) for p in prototypes]
)

ax = shap_cluster_heatmap_static(
    shap_values,
    features,
    n_clusters=4,
    title="SHAP Signature Clusters - Credit Applicants",
)
plt.show()''',
    "dataviz.xai.cohort.shap_cluster_heatmap_interactive": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.cohort import shap_cluster_heatmap_interactive

rng = np.random.default_rng(42)
features = [
    "credit_score", "debt_to_income", "utilization",
    "annual_income", "loan_amount", "account_age",
]
prototypes = np.array([
    [0.9, -0.4, 0.3, 0.1, -0.2, 0.0],
    [-0.6, 0.8, -0.5, 0.2, 0.1, -0.1],
    [0.2, -0.2, 0.7, -0.5, 0.4, 0.2],
    [-0.3, 0.1, -0.2, 0.6, -0.3, 0.5],
])
shap_values = np.vstack(
    [p + rng.normal(0, 0.08, size=(20, len(features))) for p in prototypes]
)

fig = shap_cluster_heatmap_interactive(
    shap_values,
    features,
    n_clusters=4,
    title="SHAP Signature Clusters - Credit Applicants",
)
fig.show()''',
    "dataviz.xai.comparison.importance_comparison_heatmap_static": '''import pandas as pd
import matplotlib.pyplot as plt
from dataviz.xai.comparison import importance_comparison_heatmap_static

features = [
    "credit_score", "debt_to_income", "utilization",
    "annual_income", "loan_amount", "account_age",
]
importance_matrix = pd.DataFrame(
    {
        "LogisticReg": [0.35, 0.22, 0.15, 0.12, 0.09, 0.07],
        "RandomForest": [0.28, 0.25, 0.18, 0.11, 0.10, 0.08],
        "XGBoost": [0.31, 0.21, 0.20, 0.10, 0.12, 0.06],
        "MLP": [0.26, 0.19, 0.22, 0.14, 0.11, 0.08],
    },
    index=features,
)

ax = importance_comparison_heatmap_static(
    importance_matrix,
    title="Default-Model Importance Agreement Across Algorithms",
    cmap="YlGnBu",
)
plt.show()''',
    "dataviz.xai.comparison.importance_comparison_heatmap_interactive": '''import pandas as pd
import matplotlib.pyplot as plt
from dataviz.xai.comparison import importance_comparison_heatmap_interactive

features = [
    "credit_score", "debt_to_income", "utilization",
    "annual_income", "loan_amount", "account_age",
]
importance_matrix = pd.DataFrame(
    {
        "LogisticReg": [0.35, 0.22, 0.15, 0.12, 0.09, 0.07],
        "RandomForest": [0.28, 0.25, 0.18, 0.11, 0.10, 0.08],
        "XGBoost": [0.31, 0.21, 0.20, 0.10, 0.12, 0.06],
        "MLP": [0.26, 0.19, 0.22, 0.14, 0.11, 0.08],
    },
    index=features,
)

fig = importance_comparison_heatmap_interactive(
    importance_matrix,
    title="Default-Model Importance Agreement Across Algorithms",
)
fig.show()''',
    "dataviz.xai.comparison.shap_model_agreement_scatter_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.comparison import shap_model_agreement_scatter_static

rng = np.random.default_rng(42)
features = [
    "credit_score", "debt_to_income", "utilization",
    "annual_income", "loan_amount", "account_age",
]
base = rng.normal(0.0, [0.40, 0.30, 0.25, 0.15, 0.10, 0.05], size=(60, 6))
shap_rf = base + rng.normal(0.0, 0.05, size=base.shape)
shap_xgb = base * 1.1 + rng.normal(0.0, 0.08, size=base.shape)

ax = shap_model_agreement_scatter_static(
    shap_rf,
    shap_xgb,
    model_a="RandomForest",
    model_b="XGBoost",
    feature_names=features,
    title="Per-Instance SHAP Agreement: RandomForest vs XGBoost",
)
plt.show()''',
    "dataviz.xai.comparison.shap_model_agreement_scatter_interactive": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.comparison import shap_model_agreement_scatter_interactive

rng = np.random.default_rng(42)
features = [
    "credit_score", "debt_to_income", "utilization",
    "annual_income", "loan_amount", "account_age",
]
base = rng.normal(0.0, [0.40, 0.30, 0.25, 0.15, 0.10, 0.05], size=(60, 6))
shap_rf = base + rng.normal(0.0, 0.05, size=base.shape)
shap_xgb = base * 1.1 + rng.normal(0.0, 0.08, size=base.shape)

fig = shap_model_agreement_scatter_interactive(
    shap_rf,
    shap_xgb,
    model_a="RandomForest",
    model_b="XGBoost",
    feature_names=features,
    title="Per-Instance SHAP Agreement: RandomForest vs XGBoost",
)
fig.show()''',
    "dataviz.xai.comparison.rashomon_importance_band_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.xai.comparison import rashomon_importance_band_static

rng = np.random.default_rng(42)
features = [
    "credit_score", "debt_to_income", "utilization", "annual_income",
    "loan_amount", "account_age", "inquiries_6m", "open_accounts",
]
medians = np.array([0.30, 0.22, 0.16, 0.11, 0.08, 0.06, 0.04, 0.03])
models = [f"Rashomon-{i:02d}" for i in range(1, 9)]
importances = pd.DataFrame(
    medians[:, None] + rng.normal(0, 0.025, size=(len(features), len(models))),
    index=features,
    columns=models,
)

ax = rashomon_importance_band_static(
    importances,
    top_n=8,
    title="Importance Stability Across the Rashomon Set (8 Near-Optimal Models)",
)
plt.show()''',
    "dataviz.xai.comparison.rashomon_importance_band_interactive": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.xai.comparison import rashomon_importance_band_interactive

rng = np.random.default_rng(42)
features = [
    "credit_score", "debt_to_income", "utilization", "annual_income",
    "loan_amount", "account_age", "inquiries_6m", "open_accounts",
]
medians = np.array([0.30, 0.22, 0.16, 0.11, 0.08, 0.06, 0.04, 0.03])
models = [f"Rashomon-{i:02d}" for i in range(1, 9)]
importances = pd.DataFrame(
    medians[:, None] + rng.normal(0, 0.025, size=(len(features), len(models))),
    index=features,
    columns=models,
)

fig = rashomon_importance_band_interactive(
    importances,
    top_n=8,
    title="Importance Stability Across the Rashomon Set (8 Near-Optimal Models)",
)
fig.show()''',
    "dataviz.xai.concept.concept_activation_bar_static": '''import matplotlib.pyplot as plt
from dataviz.xai.concept import concept_activation_bar_static

scores = {
    "lung opacity": 0.88,
    "pleural effusion": 0.82,
    "cardiomegaly": 0.74,
    "rib fracture": 0.61,
    "medical device": 0.55,
    "text marker": 0.42,
}
p_values = {
    "lung opacity": 0.001,
    "pleural effusion": 0.004,
    "cardiomegaly": 0.012,
    "rib fracture": 0.03,
    "medical device": 0.08,
    "text marker": 0.21,
}

ax = concept_activation_bar_static(
    scores,
    p_values=p_values,
    significance=0.05,
    title="TCAV Concept Scores - Pneumonia X-Ray Classifier",
)
plt.show()''',
    "dataviz.xai.concept.concept_activation_bar_interactive": '''import matplotlib.pyplot as plt
from dataviz.xai.concept import concept_activation_bar_interactive

scores = {
    "lung opacity": 0.88,
    "pleural effusion": 0.82,
    "cardiomegaly": 0.74,
    "rib fracture": 0.61,
    "medical device": 0.55,
    "text marker": 0.42,
}
p_values = {
    "lung opacity": 0.001,
    "pleural effusion": 0.004,
    "cardiomegaly": 0.012,
    "rib fracture": 0.03,
    "medical device": 0.08,
    "text marker": 0.21,
}

fig = concept_activation_bar_interactive(
    scores,
    p_values=p_values,
    significance=0.05,
    title="TCAV Concept Scores - Pneumonia X-Ray Classifier",
)
fig.show()''',
    "dataviz.xai.concept.saliency_overlay_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.concept import saliency_overlay_plot_static

rng = np.random.default_rng(42)
size = 32
yy, xx = np.mgrid[0:size, 0:size]
centers = [(10, 12), (22, 9), (16, 20), (8, 24)]
labels = ["Pneumonia", "Normal", "Effusion", "Mass"]

images, saliencies = [], []
for cx, cy in centers:
    blob = np.exp(-((xx - cx) ** 2 + (yy - cy) ** 2) / 30.0)
    images.append(blob + rng.normal(0, 0.05, size=(size, size)))
    focus = np.exp(-((xx - cx) ** 2 + (yy - cy) ** 2) / 18.0)
    saliencies.append(focus + rng.normal(0, 0.03, size=(size, size)))

ax = saliency_overlay_plot_static(
    images,
    saliencies,
    labels=labels,
    title="Grad-CAM Overlays - Chest X-Ray Classifier",
)
plt.show()''',
    "dataviz.xai.concept.saliency_overlay_plot_interactive": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.concept import saliency_overlay_plot_interactive

rng = np.random.default_rng(42)
size = 32
yy, xx = np.mgrid[0:size, 0:size]
centers = [(10, 12), (22, 9), (16, 20), (8, 24)]
labels = ["Pneumonia", "Normal", "Effusion", "Mass"]

images, saliencies = [], []
for cx, cy in centers:
    blob = np.exp(-((xx - cx) ** 2 + (yy - cy) ** 2) / 30.0)
    images.append(blob + rng.normal(0, 0.05, size=(size, size)))
    focus = np.exp(-((xx - cx) ** 2 + (yy - cy) ** 2) / 18.0)
    saliencies.append(focus + rng.normal(0, 0.03, size=(size, size)))

fig = saliency_overlay_plot_interactive(
    images,
    saliencies,
    labels=labels,
    title="Grad-CAM Overlays - Chest X-Ray Classifier",
)
fig.show()''',
    "dataviz.xai.concept.attention_heatmap_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.concept import attention_heatmap_static

rng = np.random.default_rng(42)
tokens = ["the", "model", "denied", "the", "loan", "due", "to", "debt"]
weights = rng.random((len(tokens), len(tokens))) + 0.6 * np.eye(len(tokens))
attention = weights / weights.sum(axis=1, keepdims=True)

ax = attention_heatmap_static(
    attention,
    tokens,
    title="Attention Weights - Adverse-Action Explanation Head",
    cmap="Blues",
)
plt.show()''',
    "dataviz.xai.concept.attention_heatmap_interactive": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.concept import attention_heatmap_interactive

rng = np.random.default_rng(42)
tokens = ["the", "model", "denied", "the", "loan", "due", "to", "debt"]
weights = rng.random((len(tokens), len(tokens))) + 0.6 * np.eye(len(tokens))
attention = weights / weights.sum(axis=1, keepdims=True)

fig = attention_heatmap_interactive(
    attention,
    tokens,
    title="Attention Weights - Adverse-Action Explanation Head",
)
fig.show()''',
    "dataviz.xai.concept.embedding_projection_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.concept import embedding_projection_plot_static

rng = np.random.default_rng(42)
segments = {
    "loyal": (-2.0, 0.5),
    "at-risk": (0.5, 2.0),
    "churned": (2.0, -1.5),
}
coords, labels = [], []
for name, (cx, cy) in segments.items():
    pts = rng.normal([cx, cy], 0.6, size=(30, 2))
    coords.append(pts)
    labels.extend([name] * len(pts))
coords = np.vstack(coords)

ax = embedding_projection_plot_static(
    coords,
    labels=labels,
    title="Customer Embedding Projection (UMAP 2-D) - Churn Model",
)
plt.show()''',
    "dataviz.xai.concept.embedding_projection_plot_interactive": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.concept import embedding_projection_plot_interactive

rng = np.random.default_rng(42)
segments = {
    "loyal": (-2.0, 0.5),
    "at-risk": (0.5, 2.0),
    "churned": (2.0, -1.5),
}
coords, labels = [], []
for name, (cx, cy) in segments.items():
    pts = rng.normal([cx, cy], 0.6, size=(30, 2))
    coords.append(pts)
    labels.extend([name] * len(pts))
coords = np.vstack(coords)
hover_text = [f"customer segment: {s}" for s in labels]

fig = embedding_projection_plot_interactive(
    coords,
    labels=labels,
    hover_text=hover_text,
    title="Customer Embedding Projection (UMAP 2-D) - Churn Model",
)
fig.show()''',
    "dataviz.xai.counterfactuals.counterfactual_path_plot_static": '''import pandas as pd
import matplotlib.pyplot as plt
from dataviz.xai.counterfactuals import counterfactual_path_plot_static

cols = ["credit_score", "debt_to_income", "utilization"]
steps = pd.DataFrame(
    [
        [612, 0.48, 0.81],
        [630, 0.46, 0.74],
        [655, 0.42, 0.66],
        [690, 0.37, 0.55],
        [718, 0.33, 0.44],
    ],
    columns=cols,
)
predictions = [0.71, 0.66, 0.58, 0.47, 0.39]

ax = counterfactual_path_plot_static(
    steps,
    predictions,
    target_threshold=0.5,
    title="Counterfactual Path to Loan Approval (P(default) below 0.5)",
)
plt.show()''',
    "dataviz.xai.counterfactuals.counterfactual_path_plot_interactive": '''import pandas as pd
import matplotlib.pyplot as plt
from dataviz.xai.counterfactuals import counterfactual_path_plot_interactive

cols = ["credit_score", "debt_to_income", "utilization"]
steps = pd.DataFrame(
    [
        [612, 0.48, 0.81],
        [630, 0.46, 0.74],
        [655, 0.42, 0.66],
        [690, 0.37, 0.55],
        [718, 0.33, 0.44],
    ],
    columns=cols,
)
predictions = [0.71, 0.66, 0.58, 0.47, 0.39]

fig = counterfactual_path_plot_interactive(
    steps,
    predictions,
    target_threshold=0.5,
    title="Counterfactual Path to Loan Approval (P(default) below 0.5)",
)
fig.show()''',
    "dataviz.xai.counterfactuals.diverse_counterfactual_grid_static": '''import pandas as pd
import matplotlib.pyplot as plt
from dataviz.xai.counterfactuals import diverse_counterfactual_grid_static

original = {
    "credit_score": 612,
    "debt_to_income": 0.48,
    "utilization": 0.81,
    "annual_income": 52000,
}
counterfactuals = pd.DataFrame(
    [
        [660, 0.48, 0.81, 52000],
        [612, 0.34, 0.60, 52000],
        [648, 0.40, 0.81, 61000],
        [612, 0.38, 0.62, 57500],
    ],
    columns=list(original),
)

ax = diverse_counterfactual_grid_static(
    original,
    counterfactuals,
    title="Diverse Counterfactuals for Denied Applicant #417",
)
plt.show()''',
    "dataviz.xai.counterfactuals.diverse_counterfactual_grid_interactive": '''import pandas as pd
import matplotlib.pyplot as plt
from dataviz.xai.counterfactuals import diverse_counterfactual_grid_interactive

original = {
    "credit_score": 612,
    "debt_to_income": 0.48,
    "utilization": 0.81,
    "annual_income": 52000,
}
counterfactuals = pd.DataFrame(
    [
        [660, 0.48, 0.81, 52000],
        [612, 0.34, 0.60, 52000],
        [648, 0.40, 0.81, 61000],
        [612, 0.38, 0.62, 57500],
    ],
    columns=list(original),
)

fig = diverse_counterfactual_grid_interactive(
    original,
    counterfactuals,
    title="Diverse Counterfactuals for Denied Applicant #417",
)
fig.show()''',
    "dataviz.xai.counterfactuals.what_if_slider_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.counterfactuals import what_if_slider_plot_static

grid = np.linspace(500, 800, 60)
pred_default = 1.0 / (1.0 + np.exp((grid - 645.0) / 45.0))

ax = what_if_slider_plot_static(
    grid,
    pred_default,
    feature_name="Credit score",
    current_value=612,
    threshold=0.5,
    title="What-If: Sweeping Credit Score for Applicant #417",
)
plt.show()''',
    "dataviz.xai.counterfactuals.what_if_slider_plot_interactive": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.counterfactuals import what_if_slider_plot_interactive

grid = np.linspace(500, 800, 60)
pred_default = 1.0 / (1.0 + np.exp((grid - 645.0) / 45.0))

fig = what_if_slider_plot_interactive(
    grid,
    pred_default,
    feature_name="Credit score",
    current_value=612,
    threshold=0.5,
    title="What-If: Sweeping Credit Score for Applicant #417",
)
fig.show()''',
    "dataviz.xai.dependence_more.pdp_with_ice_overlay_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.dependence_more import pdp_with_ice_overlay_static

rng = np.random.default_rng(42)
grid = np.linspace(300, 850, 30)
base = 1.0 / (1.0 + np.exp((grid - 600.0) / 70.0))
offsets = rng.normal(0.0, 0.08, size=(40, 1))
ice_curves = base[None, :] + offsets + rng.normal(0.0, 0.02, size=(40, grid.size))
pdp = ice_curves.mean(axis=0)
rug = rng.uniform(300, 850, size=25)

ax = pdp_with_ice_overlay_static(
    grid,
    ice_curves,
    pdp,
    feature_name="Credit score",
    rug=rug,
    title="PDP + ICE: Default Risk vs Credit Score",
)
plt.show()''',
    "dataviz.xai.dependence_more.pdp_with_ice_overlay_interactive": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.dependence_more import pdp_with_ice_overlay_interactive

rng = np.random.default_rng(42)
grid = np.linspace(300, 850, 30)
base = 1.0 / (1.0 + np.exp((grid - 600.0) / 70.0))
offsets = rng.normal(0.0, 0.08, size=(40, 1))
ice_curves = base[None, :] + offsets + rng.normal(0.0, 0.02, size=(40, grid.size))
pdp = ice_curves.mean(axis=0)
rug = rng.uniform(300, 850, size=25)

fig = pdp_with_ice_overlay_interactive(
    grid,
    ice_curves,
    pdp,
    feature_name="Credit score",
    title="PDP + ICE: Default Risk vs Credit Score",
)
fig.show()''',
    "dataviz.xai.dependence_more.ale_plot_2d_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.dependence_more import ale_plot_2d_static

rng = np.random.default_rng(42)
x_edges = np.linspace(300, 850, 11)
y_edges = np.linspace(0.0, 0.6, 9)
xc = 0.5 * (x_edges[:-1] + x_edges[1:])
yc = 0.5 * (y_edges[:-1] + y_edges[1:])
ale_grid = (
    -0.4 * np.exp(-(((xc[:, None] - 580.0) / 90.0) ** 2)) * (1.0 + yc[None, :])
    + 0.15 * (yc[None, :] - 0.3)
    + rng.normal(0.0, 0.01, size=(len(xc), len(yc)))
)

ax = ale_plot_2d_static(
    ale_grid,
    x_edges,
    y_edges,
    feature_x="Credit score",
    feature_y="Utilization",
    title="2-D ALE: Credit Score x Utilization Interaction Effect",
)
plt.show()''',
    "dataviz.xai.dependence_more.ale_plot_2d_interactive": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.dependence_more import ale_plot_2d_interactive

rng = np.random.default_rng(42)
x_edges = np.linspace(300, 850, 11)
y_edges = np.linspace(0.0, 0.6, 9)
xc = 0.5 * (x_edges[:-1] + x_edges[1:])
yc = 0.5 * (y_edges[:-1] + y_edges[1:])
ale_grid = (
    -0.4 * np.exp(-(((xc[:, None] - 580.0) / 90.0) ** 2)) * (1.0 + yc[None, :])
    + 0.15 * (yc[None, :] - 0.3)
    + rng.normal(0.0, 0.01, size=(len(xc), len(yc)))
)

fig = ale_plot_2d_interactive(
    ale_grid,
    x_edges,
    y_edges,
    feature_x="Credit score",
    feature_y="Utilization",
    title="2-D ALE: Credit Score x Utilization Interaction Effect",
)
fig.show()''',
    "dataviz.xai.dependence_more.h_statistic_heatmap_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.xai.dependence_more import h_statistic_heatmap_static

features = [
    "credit_score", "debt_to_income", "utilization", "annual_income", "loan_amount",
]
h = np.array([
    [1.00, 0.34, 0.41, 0.05, 0.08],
    [0.34, 1.00, 0.52, 0.07, 0.12],
    [0.41, 0.52, 1.00, 0.04, 0.15],
    [0.05, 0.07, 0.04, 1.00, 0.22],
    [0.08, 0.12, 0.15, 0.22, 1.00],
])
h_matrix = pd.DataFrame(h, index=features, columns=features)

ax = h_statistic_heatmap_static(
    h_matrix,
    title="Friedman H-Statistic - Default Model Feature Interactions",
    cmap="magma",
)
plt.show()''',
    "dataviz.xai.dependence_more.h_statistic_heatmap_interactive": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.xai.dependence_more import h_statistic_heatmap_interactive

features = [
    "credit_score", "debt_to_income", "utilization", "annual_income", "loan_amount",
]
h = np.array([
    [1.00, 0.34, 0.41, 0.05, 0.08],
    [0.34, 1.00, 0.52, 0.07, 0.12],
    [0.41, 0.52, 1.00, 0.04, 0.15],
    [0.05, 0.07, 0.04, 1.00, 0.22],
    [0.08, 0.12, 0.15, 0.22, 1.00],
])
h_matrix = pd.DataFrame(h, index=features, columns=features)

fig = h_statistic_heatmap_interactive(
    h_matrix,
    title="Friedman H-Statistic - Default Model Feature Interactions",
)
fig.show()''',
    "dataviz.xai.dependence_more.interaction_network_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.xai.dependence_more import interaction_network_static

features = [
    "credit_score", "debt_to_income", "utilization",
    "annual_income", "loan_amount", "account_age",
]
h = np.array([
    [0.00, 0.34, 0.41, 0.05, 0.08, 0.03],
    [0.34, 0.00, 0.52, 0.07, 0.12, 0.04],
    [0.41, 0.52, 0.00, 0.04, 0.15, 0.06],
    [0.05, 0.07, 0.04, 0.00, 0.22, 0.18],
    [0.08, 0.12, 0.15, 0.22, 0.00, 0.05],
    [0.03, 0.04, 0.06, 0.18, 0.05, 0.00],
])
interaction_matrix = pd.DataFrame(h, index=features, columns=features)

ax = interaction_network_static(
    interaction_matrix,
    threshold=0.12,
    title="Strongest Feature Interactions - Default Risk Model",
)
plt.show()''',
    "dataviz.xai.dependence_more.interaction_network_interactive": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.xai.dependence_more import interaction_network_interactive

features = [
    "credit_score", "debt_to_income", "utilization",
    "annual_income", "loan_amount", "account_age",
]
h = np.array([
    [0.00, 0.34, 0.41, 0.05, 0.08, 0.03],
    [0.34, 0.00, 0.52, 0.07, 0.12, 0.04],
    [0.41, 0.52, 0.00, 0.04, 0.15, 0.06],
    [0.05, 0.07, 0.04, 0.00, 0.22, 0.18],
    [0.08, 0.12, 0.15, 0.22, 0.00, 0.05],
    [0.03, 0.04, 0.06, 0.18, 0.05, 0.00],
])
interaction_matrix = pd.DataFrame(h, index=features, columns=features)

fig = interaction_network_interactive(
    interaction_matrix,
    threshold=0.12,
    title="Strongest Feature Interactions - Default Risk Model",
)
fig.show()''',
    "dataviz.xai.fairness_xai.disparate_impact_by_segment_static": '''import pandas as pd
import matplotlib.pyplot as plt
from dataviz.xai.fairness_xai import disparate_impact_by_segment_static

segment_metrics = pd.DataFrame(
    {
        "importance": [0.31, 0.24, 0.19, 0.15],
        "positive_rate": [0.78, 0.71, 0.63, 0.55],
    },
    index=["Age 25-34", "Age 35-44", "Age 45-54", "Age 55+"],
)

ax = disparate_impact_by_segment_static(
    segment_metrics,
    importance_col="importance",
    rate_col="positive_rate",
    reference_rate=0.70,
    title="Credit-Score Feature Reliance vs Approval Rate by Age Band",
)
plt.show()''',
    "dataviz.xai.fairness_xai.disparate_impact_by_segment_interactive": '''import pandas as pd
import matplotlib.pyplot as plt
from dataviz.xai.fairness_xai import disparate_impact_by_segment_interactive

segment_metrics = pd.DataFrame(
    {
        "importance": [0.31, 0.24, 0.19, 0.15],
        "positive_rate": [0.78, 0.71, 0.63, 0.55],
    },
    index=["Age 25-34", "Age 35-44", "Age 45-54", "Age 55+"],
)

fig = disparate_impact_by_segment_interactive(
    segment_metrics,
    importance_col="importance",
    rate_col="positive_rate",
    reference_rate=0.70,
    title="Credit-Score Feature Reliance vs Approval Rate by Age Band",
)
fig.show()''',
    "dataviz.xai.fairness_xai.subgroup_shap_divergence_static": '''import matplotlib.pyplot as plt
from dataviz.xai.fairness_xai import subgroup_shap_divergence_static

divergence = {
    "credit_score": 0.42,
    "debt_to_income": 0.35,
    "utilization": 0.28,
    "zip_region": 0.61,
    "annual_income": 0.19,
    "account_age": 0.11,
    "loan_amount": 0.08,
}

ax = subgroup_shap_divergence_static(
    divergence,
    metric="KL",
    title="SHAP Divergence Between Urban and Rural Subgroups",
)
plt.show()''',
    "dataviz.xai.fairness_xai.subgroup_shap_divergence_interactive": '''import matplotlib.pyplot as plt
from dataviz.xai.fairness_xai import subgroup_shap_divergence_interactive

divergence = {
    "credit_score": 0.42,
    "debt_to_income": 0.35,
    "utilization": 0.28,
    "zip_region": 0.61,
    "annual_income": 0.19,
    "account_age": 0.11,
    "loan_amount": 0.08,
}

fig = subgroup_shap_divergence_interactive(
    divergence,
    metric="KL",
    title="SHAP Divergence Between Urban and Rural Subgroups",
)
fig.show()''',
    "dataviz.xai.fairness_xai.intersectional_importance_heatmap_static": '''import pandas as pd
import matplotlib.pyplot as plt
from dataviz.xai.fairness_xai import intersectional_importance_heatmap_static

features = [
    "credit_score", "debt_to_income", "utilization", "annual_income", "loan_amount",
]
importance_cube = pd.DataFrame(
    {
        "urban|high_income": [0.34, 0.20, 0.16, 0.12, 0.10],
        "urban|low_income": [0.26, 0.28, 0.21, 0.09, 0.13],
        "rural|high_income": [0.30, 0.22, 0.15, 0.15, 0.11],
        "rural|low_income": [0.18, 0.31, 0.24, 0.08, 0.16],
    },
    index=features,
)

ax = intersectional_importance_heatmap_static(
    importance_cube,
    title="Importance by Intersectional Segment (Region x Income Band)",
    cmap="cividis",
)
plt.show()''',
    "dataviz.xai.fairness_xai.intersectional_importance_heatmap_interactive": '''import pandas as pd
import matplotlib.pyplot as plt
from dataviz.xai.fairness_xai import intersectional_importance_heatmap_interactive

features = [
    "credit_score", "debt_to_income", "utilization", "annual_income", "loan_amount",
]
importance_cube = pd.DataFrame(
    {
        "urban|high_income": [0.34, 0.20, 0.16, 0.12, 0.10],
        "urban|low_income": [0.26, 0.28, 0.21, 0.09, 0.13],
        "rural|high_income": [0.30, 0.22, 0.15, 0.15, 0.11],
        "rural|low_income": [0.18, 0.31, 0.24, 0.08, 0.16],
    },
    index=features,
)

fig = intersectional_importance_heatmap_interactive(
    importance_cube,
    title="Importance by Intersectional Segment (Region x Income Band)",
)
fig.show()''',
    "dataviz.xai.feature_imp.feature_importance_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.xai.feature_imp import feature_importance_static

rng = np.random.default_rng(42)
features = [
    "credit_score", "debt_to_income", "payment_history", "utilization",
    "annual_income", "loan_amount", "account_age", "inquiries_6m",
    "open_accounts", "delinquencies",
]
weights = np.array([0.28, 0.20, 0.16, 0.12, 0.08, 0.06, 0.04, 0.03, 0.02, 0.01])
importances = pd.Series(
    weights + rng.normal(0, 0.003, size=len(features)), index=features
)

ax = feature_importance_static(
    importances,
    title="Credit-Risk Model: Top Feature Importances",
    top_n=8,
    xlabel="Mean decrease in impurity",
    color="darkslateblue",
    value_format=".3f",
)
plt.show()''',
    "dataviz.xai.feature_imp.feature_importance_interactive": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.xai.feature_imp import feature_importance_interactive

rng = np.random.default_rng(42)
features = [
    "credit_score", "debt_to_income", "payment_history", "utilization",
    "annual_income", "loan_amount", "account_age", "inquiries_6m",
    "open_accounts", "delinquencies",
]
weights = np.array([0.28, 0.20, 0.16, 0.12, 0.08, 0.06, 0.04, 0.03, 0.02, 0.01])
importances = pd.Series(
    weights + rng.normal(0, 0.003, size=len(features)), index=features
)

fig = feature_importance_interactive(
    importances,
    title="Credit-Risk Model: Top Feature Importances",
    top_n=8,
    xlabel="Mean decrease in impurity",
    marker_color="darkslateblue",
    height=560,
)
fig.show()''',
    "dataviz.xai.importance_extra.permutation_importance_bar_static": '''import matplotlib.pyplot as plt
from dataviz.xai.importance_extra import permutation_importance_bar_static

importances = {
    "credit_score": 0.142,
    "debt_to_income": 0.098,
    "utilization": 0.071,
    "payment_history": 0.055,
    "annual_income": 0.031,
    "loan_amount": 0.024,
    "account_age": 0.012,
    "inquiries_6m": 0.008,
}
std = {
    "credit_score": 0.011,
    "debt_to_income": 0.009,
    "utilization": 0.008,
    "payment_history": 0.007,
    "annual_income": 0.006,
    "loan_amount": 0.005,
    "account_age": 0.004,
    "inquiries_6m": 0.003,
}

ax = permutation_importance_bar_static(
    importances,
    std=std,
    top_n=8,
    title="Permutation Importance (ROC-AUC Drop) - Default Model",
    color="seagreen",
)
plt.show()''',
    "dataviz.xai.importance_extra.permutation_importance_bar_interactive": '''import matplotlib.pyplot as plt
from dataviz.xai.importance_extra import permutation_importance_bar_interactive

importances = {
    "credit_score": 0.142,
    "debt_to_income": 0.098,
    "utilization": 0.071,
    "payment_history": 0.055,
    "annual_income": 0.031,
    "loan_amount": 0.024,
    "account_age": 0.012,
    "inquiries_6m": 0.008,
}
std = {
    "credit_score": 0.011,
    "debt_to_income": 0.009,
    "utilization": 0.008,
    "payment_history": 0.007,
    "annual_income": 0.006,
    "loan_amount": 0.005,
    "account_age": 0.004,
    "inquiries_6m": 0.003,
}

fig = permutation_importance_bar_interactive(
    importances,
    std=std,
    top_n=8,
    title="Permutation Importance (ROC-AUC Drop) - Default Model",
)
fig.show()''',
    "dataviz.xai.importance_extra.feature_importance_grouped_bar_static": '''import matplotlib.pyplot as plt
from dataviz.xai.importance_extra import feature_importance_grouped_bar_static

features = [
    "credit_score", "debt_to_income", "utilization",
    "annual_income", "loan_amount", "account_age",
]
importances = {
    "LogisticReg": dict(zip(features, [0.35, 0.22, 0.15, 0.12, 0.09, 0.07])),
    "RandomForest": dict(zip(features, [0.28, 0.25, 0.18, 0.11, 0.10, 0.08])),
    "XGBoost": dict(zip(features, [0.31, 0.21, 0.20, 0.10, 0.12, 0.06])),
}

ax = feature_importance_grouped_bar_static(
    importances,
    top_n=6,
    title="Feature Importance Agreement Across Candidate Models",
)
plt.show()''',
    "dataviz.xai.importance_extra.feature_importance_grouped_bar_interactive": '''import matplotlib.pyplot as plt
from dataviz.xai.importance_extra import feature_importance_grouped_bar_interactive

features = [
    "credit_score", "debt_to_income", "utilization",
    "annual_income", "loan_amount", "account_age",
]
importances = {
    "LogisticReg": dict(zip(features, [0.35, 0.22, 0.15, 0.12, 0.09, 0.07])),
    "RandomForest": dict(zip(features, [0.28, 0.25, 0.18, 0.11, 0.10, 0.08])),
    "XGBoost": dict(zip(features, [0.31, 0.21, 0.20, 0.10, 0.12, 0.06])),
}

fig = feature_importance_grouped_bar_interactive(
    importances,
    top_n=6,
    title="Feature Importance Agreement Across Candidate Models",
)
fig.show()''',
    "dataviz.xai.importance_extra.feature_importance_boxplot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.importance_extra import feature_importance_boxplot_static

rng = np.random.default_rng(42)
centers = {
    "credit_score": 0.142,
    "debt_to_income": 0.098,
    "utilization": 0.071,
    "payment_history": 0.055,
    "annual_income": 0.031,
    "loan_amount": 0.024,
    "account_age": 0.012,
}
per_fold = {
    name: list(rng.normal(c, 0.008, size=12)) for name, c in centers.items()
}

ax = feature_importance_boxplot_static(
    per_fold,
    top_n=7,
    title="Permutation Importance Stability Across 12 Repeats",
)
plt.show()''',
    "dataviz.xai.importance_extra.feature_importance_boxplot_interactive": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.importance_extra import feature_importance_boxplot_interactive

rng = np.random.default_rng(42)
centers = {
    "credit_score": 0.142,
    "debt_to_income": 0.098,
    "utilization": 0.071,
    "payment_history": 0.055,
    "annual_income": 0.031,
    "loan_amount": 0.024,
    "account_age": 0.012,
}
per_fold = {
    name: list(rng.normal(c, 0.008, size=12)) for name, c in centers.items()
}

fig = feature_importance_boxplot_interactive(
    per_fold,
    top_n=7,
    title="Permutation Importance Stability Across 12 Repeats",
)
fig.show()''',
    "dataviz.xai.importance_extra.drop_column_importance_bar_static": '''import matplotlib.pyplot as plt
from dataviz.xai.importance_extra import drop_column_importance_bar_static

deltas = {
    "credit_score": 0.118,
    "debt_to_income": 0.084,
    "utilization": 0.062,
    "payment_history": 0.047,
    "annual_income": 0.019,
    "loan_amount": 0.011,
    "account_age": -0.003,
    "inquiries_6m": -0.006,
}

ax = drop_column_importance_bar_static(
    deltas,
    top_n=8,
    title="Drop-Column Importance (ROC-AUC) - Default Model",
)
plt.show()''',
    "dataviz.xai.importance_extra.drop_column_importance_bar_interactive": '''import matplotlib.pyplot as plt
from dataviz.xai.importance_extra import drop_column_importance_bar_interactive

deltas = {
    "credit_score": 0.118,
    "debt_to_income": 0.084,
    "utilization": 0.062,
    "payment_history": 0.047,
    "annual_income": 0.019,
    "loan_amount": 0.011,
    "account_age": -0.003,
    "inquiries_6m": -0.006,
}

fig = drop_column_importance_bar_interactive(
    deltas,
    top_n=8,
    title="Drop-Column Importance (ROC-AUC) - Default Model",
)
fig.show()''',
    "dataviz.xai.importance_extra.importance_method_scatter_static": '''import matplotlib.pyplot as plt
from dataviz.xai.importance_extra import importance_method_scatter_static

permutation = {
    "credit_score": 0.142,
    "debt_to_income": 0.098,
    "utilization": 0.071,
    "payment_history": 0.055,
    "annual_income": 0.031,
    "loan_amount": 0.024,
    "account_age": 0.012,
    "inquiries_6m": 0.008,
}
shap_mean_abs = {
    "credit_score": 0.151,
    "debt_to_income": 0.090,
    "utilization": 0.078,
    "payment_history": 0.049,
    "annual_income": 0.036,
    "loan_amount": 0.020,
    "account_age": 0.015,
    "inquiries_6m": 0.006,
}

ax = importance_method_scatter_static(
    permutation,
    shap_mean_abs,
    a_name="Permutation (AUC drop)",
    b_name="SHAP (mean |phi|)",
    title="Importance Method Agreement - Default Model",
)
plt.show()''',
    "dataviz.xai.importance_extra.importance_method_scatter_interactive": '''import matplotlib.pyplot as plt
from dataviz.xai.importance_extra import importance_method_scatter_interactive

permutation = {
    "credit_score": 0.142,
    "debt_to_income": 0.098,
    "utilization": 0.071,
    "payment_history": 0.055,
    "annual_income": 0.031,
    "loan_amount": 0.024,
    "account_age": 0.012,
    "inquiries_6m": 0.008,
}
shap_mean_abs = {
    "credit_score": 0.151,
    "debt_to_income": 0.090,
    "utilization": 0.078,
    "payment_history": 0.049,
    "annual_income": 0.036,
    "loan_amount": 0.020,
    "account_age": 0.015,
    "inquiries_6m": 0.006,
}

fig = importance_method_scatter_interactive(
    permutation,
    shap_mean_abs,
    a_name="Permutation (AUC drop)",
    b_name="SHAP (mean |phi|)",
    title="Importance Method Agreement - Default Model",
)
fig.show()''',
}
