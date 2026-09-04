"""Curated rich examples for xai member pages."""

EXAMPLES = {
    "dataviz.xai.importance_more.gain_importance_bar_static": '''import matplotlib.pyplot as plt
from dataviz.xai.importance_more import gain_importance_bar_static

gain = {
    "credit_score": 42.7, "debt_to_income": 31.4, "loan_amount": 24.9,
    "employment_years": 18.2, "annual_income": 15.6,
    "num_open_accounts": 9.8, "age": 7.3, "num_credit_cards": 5.1,
}
split_count = {
    "credit_score": 184, "debt_to_income": 152, "loan_amount": 131,
    "employment_years": 98, "annual_income": 87, "num_open_accounts": 54,
    "age": 41, "num_credit_cards": 26,
}
ax = gain_importance_bar_static(
    gain, split_count=split_count, top_n=8,
    title="XGBoost gain importance - credit default model",
)
ax.set_xlabel("Total gain (bars) vs split count (line)")
plt.show()''',
    "dataviz.xai.importance_more.gain_importance_bar_interactive": '''from dataviz.xai.importance_more import gain_importance_bar_interactive

gain = {
    "credit_score": 42.7, "debt_to_income": 31.4, "loan_amount": 24.9,
    "employment_years": 18.2, "annual_income": 15.6,
    "num_open_accounts": 9.8, "age": 7.3, "num_credit_cards": 5.1,
}
split_count = {
    "credit_score": 184, "debt_to_income": 152, "loan_amount": 131,
    "employment_years": 98, "annual_income": 87, "num_open_accounts": 54,
    "age": 41, "num_credit_cards": 26,
}
fig = gain_importance_bar_interactive(
    gain, split_count=split_count, top_n=8,
    title="XGBoost gain importance - credit default model",
)
fig.show()''',
    "dataviz.xai.importance_more.importance_stability_plot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.xai.importance_more import importance_stability_plot_static

rng = np.random.default_rng(42)
features = [
    "credit_score", "debt_to_income", "loan_amount",
    "employment_years", "annual_income", "num_open_accounts",
]
base = np.array([0.42, 0.31, 0.24, 0.18, 0.15, 0.09])
folds = np.clip(base + rng.normal(0, 0.03, size=(8, len(features))), 0, None)
fold_importances = pd.DataFrame(
    folds, columns=features,
    index=[f"fold_{k}" for k in range(1, 9)],
)
ax = importance_stability_plot_static(
    fold_importances, top_n=6,
    title="Permutation importance stability across 8 CV folds",
)
ax.set_xlabel("Mean decrease in ROC AUC")
plt.show()''',
    "dataviz.xai.importance_more.importance_stability_plot_interactive": '''import numpy as np
import pandas as pd
from dataviz.xai.importance_more import importance_stability_plot_interactive

rng = np.random.default_rng(42)
features = [
    "credit_score", "debt_to_income", "loan_amount",
    "employment_years", "annual_income", "num_open_accounts",
]
base = np.array([0.42, 0.31, 0.24, 0.18, 0.15, 0.09])
folds = np.clip(base + rng.normal(0, 0.03, size=(8, len(features))), 0, None)
fold_importances = pd.DataFrame(
    folds, columns=features,
    index=[f"fold_{k}" for k in range(1, 9)],
)
fig = importance_stability_plot_interactive(
    fold_importances, top_n=6,
    title="Permutation importance stability across 8 CV folds",
)
fig.show()''',
    "dataviz.xai.importance_more.importance_correlation_heatmap_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.xai.importance_more import importance_correlation_heatmap_static

rng = np.random.default_rng(42)
features = [
    "credit_score", "debt_to_income", "loan_amount",
    "employment_years", "annual_income", "num_open_accounts", "age",
]
latent = np.array([0.40, 0.30, 0.24, 0.18, 0.15, 0.10, 0.08])
models = ["xgboost", "lightgbm", "random_forest", "logistic"]
data = {
    m: np.clip(latent + rng.normal(0, 0.04, size=len(features)), 0, None)
    for m in models
}
importances_by_model = pd.DataFrame(data, index=features)
ax = importance_correlation_heatmap_static(
    importances_by_model,
    title="Do four churn models agree on feature importance?",
)
plt.show()''',
    "dataviz.xai.importance_more.importance_correlation_heatmap_interactive": '''import numpy as np
import pandas as pd
from dataviz.xai.importance_more import importance_correlation_heatmap_interactive

rng = np.random.default_rng(42)
features = [
    "credit_score", "debt_to_income", "loan_amount",
    "employment_years", "annual_income", "num_open_accounts", "age",
]
latent = np.array([0.40, 0.30, 0.24, 0.18, 0.15, 0.10, 0.08])
models = ["xgboost", "lightgbm", "random_forest", "logistic"]
data = {
    m: np.clip(latent + rng.normal(0, 0.04, size=len(features)), 0, None)
    for m in models
}
importances_by_model = pd.DataFrame(data, index=features)
fig = importance_correlation_heatmap_interactive(
    importances_by_model,
    title="Do four churn models agree on feature importance?",
)
fig.show()''',
    "dataviz.xai.importance_more.feature_clustermap_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.xai.importance_more import feature_clustermap_static

rng = np.random.default_rng(42)
features = [
    "credit_score", "debt_to_income", "loan_amount", "annual_income",
    "employment_years", "num_open_accounts", "age", "num_credit_cards",
]
latent = np.array([0.40, 0.38, 0.25, 0.23, 0.18, 0.10, 0.09, 0.07])
folds = [f"fold_{k}" for k in range(1, 6)]
importance_matrix = pd.DataFrame(
    np.clip(latent[:, None] + rng.normal(0, 0.03, size=(len(features), 5)), 0, None),
    index=features, columns=folds,
)
ax = feature_clustermap_static(
    importance_matrix,
    title="Feature clustering by importance signature (5 folds)",
)
plt.show()''',
    "dataviz.xai.importance_more.feature_clustermap_interactive": '''import numpy as np
import pandas as pd
from dataviz.xai.importance_more import feature_clustermap_interactive

rng = np.random.default_rng(42)
features = [
    "credit_score", "debt_to_income", "loan_amount", "annual_income",
    "employment_years", "num_open_accounts", "age", "num_credit_cards",
]
latent = np.array([0.40, 0.38, 0.25, 0.23, 0.18, 0.10, 0.09, 0.07])
folds = [f"fold_{k}" for k in range(1, 6)]
importance_matrix = pd.DataFrame(
    np.clip(latent[:, None] + rng.normal(0, 0.03, size=(len(features), 5)), 0, None),
    index=features, columns=folds,
)
fig = feature_clustermap_interactive(
    importance_matrix,
    title="Feature clustering by importance signature (5 folds)",
)
fig.show()''',
    "dataviz.xai.local_explanations.shap_force_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.local_explanations import shap_force_plot_static

feature_names = [
    "tenure_months", "monthly_charges", "contract_two_year",
    "num_support_calls", "avg_session_min", "late_payments",
    "plan_premium", "age",
]
shap_values_instance = np.array(
    [0.85, 0.42, -0.61, 0.37, 0.12, 0.28, -0.15, -0.06]
)
ax = shap_force_plot_static(
    shap_values_instance, feature_names, base_value=-1.10, top_n=8,
    title="Why customer #417 is predicted to churn (log-odds)",
)
ax.set_xlabel("Model output (log-odds of churn)")
plt.show()''',
    "dataviz.xai.local_explanations.shap_force_plot_interactive": '''import numpy as np
from dataviz.xai.local_explanations import shap_force_plot_interactive

feature_names = [
    "tenure_months", "monthly_charges", "contract_two_year",
    "num_support_calls", "avg_session_min", "late_payments",
    "plan_premium", "age",
]
shap_values_instance = np.array(
    [0.85, 0.42, -0.61, 0.37, 0.12, 0.28, -0.15, -0.06]
)
fig = shap_force_plot_interactive(
    shap_values_instance, feature_names, base_value=-1.10, top_n=8,
    title="Why customer #417 is predicted to churn (log-odds)",
)
fig.show()''',
    "dataviz.xai.local_explanations.shap_decision_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.local_explanations import shap_decision_plot_static

rng = np.random.default_rng(42)
feature_names = [
    "tenure_months", "monthly_charges", "contract_two_year",
    "num_support_calls", "avg_session_min", "late_payments",
    "plan_premium", "age",
]
scale = np.array([0.8, 0.4, 0.6, 0.35, 0.15, 0.3, 0.15, 0.1])
shap_values = rng.normal(0, 1, size=(25, 8)) * scale
ax = shap_decision_plot_static(
    shap_values, feature_names, base_value=-1.10, top_n=8,
    title="Decision paths for 25 churn-model customers",
)
plt.show()''',
    "dataviz.xai.local_explanations.shap_decision_plot_interactive": '''import numpy as np
from dataviz.xai.local_explanations import shap_decision_plot_interactive

rng = np.random.default_rng(42)
feature_names = [
    "tenure_months", "monthly_charges", "contract_two_year",
    "num_support_calls", "avg_session_min", "late_payments",
    "plan_premium", "age",
]
scale = np.array([0.8, 0.4, 0.6, 0.35, 0.15, 0.3, 0.15, 0.1])
shap_values = rng.normal(0, 1, size=(25, 8)) * scale
fig = shap_decision_plot_interactive(
    shap_values, feature_names, base_value=-1.10, top_n=8,
    title="Decision paths for 25 churn-model customers",
)
fig.show()''',
    "dataviz.xai.local_explanations.lime_explanation_bar_static": '''import matplotlib.pyplot as plt
from dataviz.xai.local_explanations import lime_explanation_bar_static

contributions = [
    ("tenure_months <= 6", 0.31),
    ("num_support_calls > 3", 0.22),
    ("contract_two_year = 0", 0.18),
    ("late_payments > 1", 0.09),
    ("plan_premium = 1", -0.07),
    ("monthly_charges <= 55", -0.14),
    ("avg_session_min > 40", -0.21),
    ("age > 45", -0.06),
]
ax = lime_explanation_bar_static(
    contributions,
    title="LIME explanation - churn prediction for customer #417",
)
ax.set_xlabel("Weight in local linear surrogate")
plt.show()''',
    "dataviz.xai.local_explanations.lime_explanation_bar_interactive": '''from dataviz.xai.local_explanations import lime_explanation_bar_interactive

contributions = [
    ("tenure_months <= 6", 0.31),
    ("num_support_calls > 3", 0.22),
    ("contract_two_year = 0", 0.18),
    ("late_payments > 1", 0.09),
    ("plan_premium = 1", -0.07),
    ("monthly_charges <= 55", -0.14),
    ("avg_session_min > 40", -0.21),
    ("age > 45", -0.06),
]
fig = lime_explanation_bar_interactive(
    contributions,
    title="LIME explanation - churn prediction for customer #417",
)
fig.show()''',
    "dataviz.xai.local_more.anchor_explanation_plot_static": '''import matplotlib.pyplot as plt
from dataviz.xai.local_more import anchor_explanation_plot_static

rules = [
    "tenure <= 6 AND support_calls > 3",
    "tenure <= 6 AND contract = month-to-month",
    "late_payments > 1 AND monthly_charges > 80",
    "tenure <= 12 AND no_auto_pay",
]
precision = [0.97, 0.93, 0.88, 0.81]
coverage = [0.12, 0.21, 0.15, 0.27]
ax = anchor_explanation_plot_static(
    rules, precision, coverage,
    title="Anchor rules for high-risk churn segment",
)
plt.show()''',
    "dataviz.xai.local_more.anchor_explanation_plot_interactive": '''from dataviz.xai.local_more import anchor_explanation_plot_interactive

rules = [
    "tenure <= 6 AND support_calls > 3",
    "tenure <= 6 AND contract = month-to-month",
    "late_payments > 1 AND monthly_charges > 80",
    "tenure <= 12 AND no_auto_pay",
]
precision = [0.97, 0.93, 0.88, 0.81]
coverage = [0.12, 0.21, 0.15, 0.27]
fig = anchor_explanation_plot_interactive(
    rules, precision, coverage,
    title="Anchor rules for high-risk churn segment",
)
fig.show()''',
    "dataviz.xai.local_more.nearest_neighbor_explanation_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.xai.local_more import nearest_neighbor_explanation_static

rng = np.random.default_rng(42)
cols = [
    "credit_score", "debt_to_income", "loan_amount",
    "annual_income", "employment_years", "late_payments",
]
query = {
    "credit_score": 612.0, "debt_to_income": 0.41, "loan_amount": 18500.0,
    "annual_income": 52000.0, "employment_years": 2.0, "late_payments": 2.0,
}
neighbors = pd.DataFrame(
    {
        "credit_score": 612 + rng.normal(0, 8, size=5),
        "debt_to_income": 0.41 + rng.normal(0, 0.03, size=5),
        "loan_amount": 18500 + rng.normal(0, 900, size=5),
        "annual_income": 52000 + rng.normal(0, 2500, size=5),
        "employment_years": 2 + rng.normal(0, 0.5, size=5),
        "late_payments": np.array([2, 1, 2, 3, 2], dtype=float),
    }
)
target = [1, 0, 1, 1, 0]
ax = nearest_neighbor_explanation_static(
    query, neighbors, target=target,
    title="Denied applicant #2048 vs 5 most similar past decisions",
)
plt.show()''',
    "dataviz.xai.local_more.nearest_neighbor_explanation_interactive": '''import numpy as np
import pandas as pd
from dataviz.xai.local_more import nearest_neighbor_explanation_interactive

rng = np.random.default_rng(42)
cols = [
    "credit_score", "debt_to_income", "loan_amount",
    "annual_income", "employment_years", "late_payments",
]
query = {
    "credit_score": 612.0, "debt_to_income": 0.41, "loan_amount": 18500.0,
    "annual_income": 52000.0, "employment_years": 2.0, "late_payments": 2.0,
}
neighbors = pd.DataFrame(
    {
        "credit_score": 612 + rng.normal(0, 8, size=5),
        "debt_to_income": 0.41 + rng.normal(0, 0.03, size=5),
        "loan_amount": 18500 + rng.normal(0, 900, size=5),
        "annual_income": 52000 + rng.normal(0, 2500, size=5),
        "employment_years": 2 + rng.normal(0, 0.5, size=5),
        "late_payments": np.array([2, 1, 2, 3, 2], dtype=float),
    }
)
target = [1, 0, 1, 1, 0]
fig = nearest_neighbor_explanation_interactive(
    query, neighbors, target=target,
    title="Denied applicant #2048 vs 5 most similar past decisions",
)
fig.show()''',
    "dataviz.xai.local_more.prototype_criticism_grid_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.xai.local_more import prototype_criticism_grid_static

rng = np.random.default_rng(42)
cols = [
    "tenure_months", "monthly_charges", "num_support_calls",
    "avg_session_min", "late_payments", "age",
]
prototypes = pd.DataFrame(
    np.array([
        [36, 65, 0, 42, 0, 45],
        [48, 82, 1, 35, 0, 52],
        [24, 55, 0, 50, 0, 31],
    ], dtype=float), columns=cols,
)
criticisms = pd.DataFrame(
    np.array([
        [2, 118, 7, 4, 4, 23],
        [60, 39, 5, 61, 3, 68],
    ], dtype=float), columns=cols,
)
ax = prototype_criticism_grid_static(
    prototypes, criticisms,
    title="Typical vs atypical retained customers (MMD critic)",
)
plt.show()''',
    "dataviz.xai.local_more.prototype_criticism_grid_interactive": '''import numpy as np
import pandas as pd
from dataviz.xai.local_more import prototype_criticism_grid_interactive

rng = np.random.default_rng(42)
cols = [
    "tenure_months", "monthly_charges", "num_support_calls",
    "avg_session_min", "late_payments", "age",
]
prototypes = pd.DataFrame(
    np.array([
        [36, 65, 0, 42, 0, 45],
        [48, 82, 1, 35, 0, 52],
        [24, 55, 0, 50, 0, 31],
    ], dtype=float), columns=cols,
)
criticisms = pd.DataFrame(
    np.array([
        [2, 118, 7, 4, 4, 23],
        [60, 39, 5, 61, 3, 68],
    ], dtype=float), columns=cols,
)
fig = prototype_criticism_grid_interactive(
    prototypes, criticisms,
    title="Typical vs atypical retained customers (MMD critic)",
)
fig.show()''',
    "dataviz.xai.local_more.contrastive_explanation_bar_static": '''import matplotlib.pyplot as plt
from dataviz.xai.local_more import contrastive_explanation_bar_static

pertinent_positives = {
    "credit_score": 0.34, "employment_years": 0.21,
    "annual_income": 0.18, "debt_to_income": 0.12,
}
pertinent_negatives = {
    "late_payments": 0.27, "num_open_accounts": 0.15,
    "loan_amount": 0.09, "debt_to_income": 0.05,
}
ax = contrastive_explanation_bar_static(
    pertinent_positives, pertinent_negatives,
    title="Why approved vs what would flip to denial - applicant #771",
)
plt.show()''',
    "dataviz.xai.local_more.contrastive_explanation_bar_interactive": '''from dataviz.xai.local_more import contrastive_explanation_bar_interactive

pertinent_positives = {
    "credit_score": 0.34, "employment_years": 0.21,
    "annual_income": 0.18, "debt_to_income": 0.12,
}
pertinent_negatives = {
    "late_payments": 0.27, "num_open_accounts": 0.15,
    "loan_amount": 0.09, "debt_to_income": 0.05,
}
fig = contrastive_explanation_bar_interactive(
    pertinent_positives, pertinent_negatives,
    title="Why approved vs what would flip to denial - applicant #771",
)
fig.show()''',
    "dataviz.xai.partial_dep.partial_dependence_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.partial_dep import partial_dependence_static

rng = np.random.default_rng(42)
credit_score = np.linspace(300, 850, 40)
logit = -4.0 + 0.010 * (credit_score - 300)
predictions = 1.0 / (1.0 + np.exp(-logit))
predictions = predictions + rng.normal(0, 0.01, size=credit_score.size)
spread = 0.04 + 0.02 * (credit_score - 300) / 550
ci = np.column_stack([predictions - spread, predictions + spread])
ax = partial_dependence_static(
    credit_score, predictions, feature_name="credit_score",
    title="Partial dependence of default risk on credit score",
    ylabel="Predicted default probability", color="darkred",
    show_confidence=True, confidence_interval=ci,
)
ax.set_ylim(0, 1)
plt.show()''',
    "dataviz.xai.partial_dep.partial_dependence_interactive": '''import numpy as np
from dataviz.xai.partial_dep import partial_dependence_interactive

rng = np.random.default_rng(42)
credit_score = np.linspace(300, 850, 40)
logit = -4.0 + 0.010 * (credit_score - 300)
predictions = 1.0 / (1.0 + np.exp(-logit))
predictions = predictions + rng.normal(0, 0.01, size=credit_score.size)
spread = 0.04 + 0.02 * (credit_score - 300) / 550
ci = np.column_stack([predictions - spread, predictions + spread])
fig = partial_dependence_interactive(
    credit_score, predictions, feature_name="credit_score",
    title="Partial dependence of default risk on credit score",
    ylabel="Predicted default probability", color="darkred",
    show_confidence=True, confidence_interval=ci,
)
fig.show()''',
    "dataviz.xai.pdp_extra.partial_dependence_2d_heatmap_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.pdp_extra import partial_dependence_2d_heatmap_static

credit_score = np.linspace(300, 850, 25)
dti = np.linspace(0.0, 0.6, 20)
xx, yy = np.meshgrid(credit_score, dti)
logit = -3.0 + 0.008 * (xx - 300) + 6.0 * yy - 0.006 * (xx - 300) * yy
pdp = 1.0 / (1.0 + np.exp(-logit))
ax = partial_dependence_2d_heatmap_static(
    credit_score, dti, pdp,
    feature_x="credit_score", feature_y="debt_to_income",
    title="Default risk: credit score x debt-to-income interaction",
    cmap="magma",
)
plt.show()''',
    "dataviz.xai.pdp_extra.partial_dependence_2d_heatmap_interactive": '''import numpy as np
from dataviz.xai.pdp_extra import partial_dependence_2d_heatmap_interactive

credit_score = np.linspace(300, 850, 25)
dti = np.linspace(0.0, 0.6, 20)
xx, yy = np.meshgrid(credit_score, dti)
logit = -3.0 + 0.008 * (xx - 300) + 6.0 * yy - 0.006 * (xx - 300) * yy
pdp = 1.0 / (1.0 + np.exp(-logit))
fig = partial_dependence_2d_heatmap_interactive(
    credit_score, dti, pdp,
    feature_x="credit_score", feature_y="debt_to_income",
    title="Default risk: credit score x debt-to-income interaction",
    colorscale="Magma",
)
fig.show()''',
    "dataviz.xai.pdp_extra.ice_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.pdp_extra import ice_plot_static

rng = np.random.default_rng(42)
tenure = np.linspace(0, 72, 30)
n_instances = 40
offsets = rng.normal(0, 0.8, size=(n_instances, 1))
curves = 1.6 - 0.035 * tenure + 0.0002 * tenure ** 2
ice_curves = curves + offsets + rng.normal(0, 0.03, size=(n_instances, tenure.size))
ax = ice_plot_static(
    tenure, ice_curves, feature_name="tenure_months",
    title="ICE curves - churn log-odds vs customer tenure",
    line_alpha=0.25,
)
ax.set_ylabel("Predicted churn log-odds")
plt.show()''',
    "dataviz.xai.pdp_extra.ice_plot_interactive": '''import numpy as np
from dataviz.xai.pdp_extra import ice_plot_interactive

rng = np.random.default_rng(42)
tenure = np.linspace(0, 72, 30)
n_instances = 40
offsets = rng.normal(0, 0.8, size=(n_instances, 1))
curves = 1.6 - 0.035 * tenure + 0.0002 * tenure ** 2
ice_curves = curves + offsets + rng.normal(0, 0.03, size=(n_instances, tenure.size))
fig = ice_plot_interactive(
    tenure, ice_curves, feature_name="tenure_months",
    title="ICE curves - churn log-odds vs customer tenure",
    line_alpha=0.25,
)
fig.show()''',
    "dataviz.xai.pdp_extra.centered_ice_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.pdp_extra import centered_ice_plot_static

rng = np.random.default_rng(42)
tenure = np.linspace(0, 72, 30)
n_instances = 40
offsets = rng.normal(0, 0.8, size=(n_instances, 1))
curves = 1.6 - 0.035 * tenure + 0.0002 * tenure ** 2
ice_curves = curves + offsets + rng.normal(0, 0.03, size=(n_instances, tenure.size))
ax = centered_ice_plot_static(
    tenure, ice_curves, feature_name="tenure_months",
    title="Centered ICE - heterogeneity in the tenure effect",
)
ax.axhline(0, color="grey", linewidth=0.6)
plt.show()''',
    "dataviz.xai.pdp_extra.centered_ice_plot_interactive": '''import numpy as np
from dataviz.xai.pdp_extra import centered_ice_plot_interactive

rng = np.random.default_rng(42)
tenure = np.linspace(0, 72, 30)
n_instances = 40
offsets = rng.normal(0, 0.8, size=(n_instances, 1))
curves = 1.6 - 0.035 * tenure + 0.0002 * tenure ** 2
ice_curves = curves + offsets + rng.normal(0, 0.03, size=(n_instances, tenure.size))
fig = centered_ice_plot_interactive(
    tenure, ice_curves, feature_name="tenure_months",
    title="Centered ICE - heterogeneity in the tenure effect",
)
fig.show()''',
    "dataviz.xai.pdp_extra.ale_plot_1d_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.pdp_extra import ale_plot_1d_static

bin_edges = np.linspace(0.0, 0.6, 11)
centers = (bin_edges[:-1] + bin_edges[1:]) / 2
ale = 2.1 * centers - 0.9 * centers ** 2
ale = ale - ale.mean()
ax = ale_plot_1d_static(
    bin_edges, ale, feature_name="debt_to_income",
    title="ALE of debt-to-income on default log-odds",
)
plt.show()''',
    "dataviz.xai.pdp_extra.ale_plot_1d_interactive": '''import numpy as np
from dataviz.xai.pdp_extra import ale_plot_1d_interactive

bin_edges = np.linspace(0.0, 0.6, 11)
centers = (bin_edges[:-1] + bin_edges[1:]) / 2
ale = 2.1 * centers - 0.9 * centers ** 2
ale = ale - ale.mean()
fig = ale_plot_1d_interactive(
    bin_edges, ale, feature_name="debt_to_income",
    title="ALE of debt-to-income on default log-odds",
)
fig.show()''',
    "dataviz.xai.shap.shap_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.shap import shap_plot_static

rng = np.random.default_rng(42)
feature_names = [
    "credit_score", "debt_to_income", "loan_amount",
    "employment_years", "annual_income", "late_payments",
    "num_open_accounts", "age",
]
coef = np.array([-0.6, 0.5, 0.3, -0.25, -0.2, 0.35, 0.1, -0.05])
X = rng.normal(0, 1, size=(60, 8))
shap_values = X * coef + rng.normal(0, 0.05, size=(60, 8))
ax = shap_plot_static(
    shap_values, feature_names,
    title="Mean signed SHAP values - credit default model",
    xlabel="Mean SHAP value (log-odds)",
)
plt.show()''',
    "dataviz.xai.shap.shap_plot_interactive": '''import numpy as np
from dataviz.xai.shap import shap_plot_interactive

rng = np.random.default_rng(42)
feature_names = [
    "credit_score", "debt_to_income", "loan_amount",
    "employment_years", "annual_income", "late_payments",
    "num_open_accounts", "age",
]
coef = np.array([-0.6, 0.5, 0.3, -0.25, -0.2, 0.35, 0.1, -0.05])
X = rng.normal(0, 1, size=(60, 8))
shap_values = X * coef + rng.normal(0, 0.05, size=(60, 8))
fig = shap_plot_interactive(
    shap_values, feature_names,
    title="Mean signed SHAP values - credit default model",
    xlabel="Mean SHAP value (log-odds)",
)
fig.show()''',
    "dataviz.xai.shap_extra.shap_summary_dot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.shap_extra import shap_summary_dot_static

rng = np.random.default_rng(42)
feature_names = [
    "tenure_months", "monthly_charges", "contract_two_year",
    "num_support_calls", "avg_session_min", "late_payments",
    "plan_premium", "age",
]
X = rng.normal(0, 1, size=(60, 8))
coef = np.array([-0.7, 0.4, -0.5, 0.35, -0.15, 0.3, 0.1, -0.08])
shap_values = X * coef + rng.normal(0, 0.05, size=(60, 8))
ax = shap_summary_dot_static(
    shap_values, X, feature_names, top_n=8,
    title="SHAP summary - telecom churn model (60 customers)",
)
plt.show()''',
    "dataviz.xai.shap_extra.shap_summary_dot_interactive": '''import numpy as np
from dataviz.xai.shap_extra import shap_summary_dot_interactive

rng = np.random.default_rng(42)
feature_names = [
    "tenure_months", "monthly_charges", "contract_two_year",
    "num_support_calls", "avg_session_min", "late_payments",
    "plan_premium", "age",
]
X = rng.normal(0, 1, size=(60, 8))
coef = np.array([-0.7, 0.4, -0.5, 0.35, -0.15, 0.3, 0.1, -0.08])
shap_values = X * coef + rng.normal(0, 0.05, size=(60, 8))
fig = shap_summary_dot_interactive(
    shap_values, X, feature_names, top_n=8,
    title="SHAP summary - telecom churn model (60 customers)",
)
fig.show()''',
    "dataviz.xai.shap_extra.shap_bar_global_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.shap_extra import shap_bar_global_static

rng = np.random.default_rng(42)
feature_names = [
    "tenure_months", "monthly_charges", "contract_two_year",
    "num_support_calls", "avg_session_min", "late_payments",
    "plan_premium", "age",
]
X = rng.normal(0, 1, size=(60, 8))
coef = np.array([-0.7, 0.4, -0.5, 0.35, -0.15, 0.3, 0.1, -0.08])
shap_values = X * coef + rng.normal(0, 0.05, size=(60, 8))
ax = shap_bar_global_static(
    shap_values, feature_names, top_n=8, color="teal",
    title="Global SHAP importance - churn model",
)
plt.show()''',
    "dataviz.xai.shap_extra.shap_bar_global_interactive": '''import numpy as np
from dataviz.xai.shap_extra import shap_bar_global_interactive

rng = np.random.default_rng(42)
feature_names = [
    "tenure_months", "monthly_charges", "contract_two_year",
    "num_support_calls", "avg_session_min", "late_payments",
    "plan_premium", "age",
]
X = rng.normal(0, 1, size=(60, 8))
coef = np.array([-0.7, 0.4, -0.5, 0.35, -0.15, 0.3, 0.1, -0.08])
shap_values = X * coef + rng.normal(0, 0.05, size=(60, 8))
fig = shap_bar_global_interactive(
    shap_values, feature_names, top_n=8,
    title="Global SHAP importance - churn model",
)
fig.show()''',
    "dataviz.xai.shap_extra.shap_violin_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.shap_extra import shap_violin_static

rng = np.random.default_rng(42)
feature_names = [
    "tenure_months", "monthly_charges", "contract_two_year",
    "num_support_calls", "avg_session_min", "late_payments",
    "plan_premium", "age",
]
X = rng.normal(0, 1, size=(60, 8))
coef = np.array([-0.7, 0.4, -0.5, 0.35, -0.15, 0.3, 0.1, -0.08])
shap_values = X * coef + rng.normal(0, 0.05, size=(60, 8))
ax = shap_violin_static(
    shap_values, feature_names, top_n=8,
    title="Distribution of SHAP values per churn feature",
)
plt.show()''',
    "dataviz.xai.shap_extra.shap_violin_interactive": '''import numpy as np
from dataviz.xai.shap_extra import shap_violin_interactive

rng = np.random.default_rng(42)
feature_names = [
    "tenure_months", "monthly_charges", "contract_two_year",
    "num_support_calls", "avg_session_min", "late_payments",
    "plan_premium", "age",
]
X = rng.normal(0, 1, size=(60, 8))
coef = np.array([-0.7, 0.4, -0.5, 0.35, -0.15, 0.3, 0.1, -0.08])
shap_values = X * coef + rng.normal(0, 0.05, size=(60, 8))
fig = shap_violin_interactive(
    shap_values, feature_names, top_n=8,
    title="Distribution of SHAP values per churn feature",
)
fig.show()''',
    "dataviz.xai.shap_extra.shap_dependence_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.shap_extra import shap_dependence_plot_static

rng = np.random.default_rng(42)
monthly_charges = rng.uniform(20, 130, size=60)
tenure_months = rng.uniform(1, 72, size=60)
shap_charges = (
    0.012 * (monthly_charges - 75)
    - 0.0004 * (monthly_charges - 75) * tenure_months / 10
    + rng.normal(0, 0.05, size=60)
)
ax = shap_dependence_plot_static(
    shap_charges, monthly_charges,
    interaction_values=tenure_months,
    feature_name="monthly_charges", interaction_name="tenure_months",
    title="SHAP dependence: charges effect weakens with tenure",
)
plt.show()''',
    "dataviz.xai.shap_extra.shap_dependence_plot_interactive": '''import numpy as np
from dataviz.xai.shap_extra import shap_dependence_plot_interactive

rng = np.random.default_rng(42)
monthly_charges = rng.uniform(20, 130, size=60)
tenure_months = rng.uniform(1, 72, size=60)
shap_charges = (
    0.012 * (monthly_charges - 75)
    - 0.0004 * (monthly_charges - 75) * tenure_months / 10
    + rng.normal(0, 0.05, size=60)
)
fig = shap_dependence_plot_interactive(
    shap_charges, monthly_charges,
    interaction_values=tenure_months,
    feature_name="monthly_charges", interaction_name="tenure_months",
    title="SHAP dependence: charges effect weakens with tenure",
)
fig.show()''',
    "dataviz.xai.shap_extra.shap_interaction_heatmap_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.shap_extra import shap_interaction_heatmap_static

feature_names = [
    "tenure_months", "monthly_charges", "contract_two_year",
    "num_support_calls", "avg_session_min", "late_payments",
    "plan_premium", "age",
]
diag = np.array([0.55, 0.40, 0.38, 0.30, 0.16, 0.26, 0.12, 0.09])
off = np.array([
    [0.00, 0.21, 0.12, 0.10, 0.05, 0.06, 0.03, 0.02],
    [0.21, 0.00, 0.09, 0.08, 0.04, 0.05, 0.04, 0.02],
    [0.12, 0.09, 0.00, 0.06, 0.03, 0.04, 0.05, 0.01],
    [0.10, 0.08, 0.06, 0.00, 0.04, 0.07, 0.02, 0.02],
    [0.05, 0.04, 0.03, 0.04, 0.00, 0.02, 0.02, 0.01],
    [0.06, 0.05, 0.04, 0.07, 0.02, 0.00, 0.01, 0.01],
    [0.03, 0.04, 0.05, 0.02, 0.02, 0.01, 0.00, 0.01],
    [0.02, 0.02, 0.01, 0.02, 0.01, 0.01, 0.01, 0.00],
])
interaction_matrix = off + np.diag(diag)
ax = shap_interaction_heatmap_static(
    interaction_matrix, feature_names, top_n=8,
    title="Mean absolute SHAP interactions - churn model",
)
plt.show()''',
    "dataviz.xai.shap_extra.shap_interaction_heatmap_interactive": '''import numpy as np
from dataviz.xai.shap_extra import shap_interaction_heatmap_interactive

feature_names = [
    "tenure_months", "monthly_charges", "contract_two_year",
    "num_support_calls", "avg_session_min", "late_payments",
    "plan_premium", "age",
]
diag = np.array([0.55, 0.40, 0.38, 0.30, 0.16, 0.26, 0.12, 0.09])
off = np.array([
    [0.00, 0.21, 0.12, 0.10, 0.05, 0.06, 0.03, 0.02],
    [0.21, 0.00, 0.09, 0.08, 0.04, 0.05, 0.04, 0.02],
    [0.12, 0.09, 0.00, 0.06, 0.03, 0.04, 0.05, 0.01],
    [0.10, 0.08, 0.06, 0.00, 0.04, 0.07, 0.02, 0.02],
    [0.05, 0.04, 0.03, 0.04, 0.00, 0.02, 0.02, 0.01],
    [0.06, 0.05, 0.04, 0.07, 0.02, 0.00, 0.01, 0.01],
    [0.03, 0.04, 0.05, 0.02, 0.02, 0.01, 0.00, 0.01],
    [0.02, 0.02, 0.01, 0.02, 0.01, 0.01, 0.01, 0.00],
])
interaction_matrix = off + np.diag(diag)
fig = shap_interaction_heatmap_interactive(
    interaction_matrix, feature_names, top_n=8,
    title="Mean absolute SHAP interactions - churn model",
)
fig.show()''',
    "dataviz.xai.shap_extra.shap_waterfall_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.shap_extra import shap_waterfall_plot_static

feature_names = [
    "tenure_months", "monthly_charges", "contract_two_year",
    "num_support_calls", "avg_session_min", "late_payments",
    "plan_premium", "age",
]
shap_values_instance = np.array(
    [0.85, 0.42, -0.61, 0.37, 0.12, 0.28, -0.15, -0.06]
)
ax = shap_waterfall_plot_static(
    shap_values_instance, feature_names, base_value=-1.10, top_n=6,
    title="SHAP waterfall - churn explanation for customer #417",
)
plt.show()''',
    "dataviz.xai.shap_extra.shap_waterfall_plot_interactive": '''import numpy as np
from dataviz.xai.shap_extra import shap_waterfall_plot_interactive

feature_names = [
    "tenure_months", "monthly_charges", "contract_two_year",
    "num_support_calls", "avg_session_min", "late_payments",
    "plan_premium", "age",
]
shap_values_instance = np.array(
    [0.85, 0.42, -0.61, 0.37, 0.12, 0.28, -0.15, -0.06]
)
fig = shap_waterfall_plot_interactive(
    shap_values_instance, feature_names, base_value=-1.10, top_n=6,
    title="SHAP waterfall - churn explanation for customer #417",
)
fig.show()''',
    "dataviz.xai.shap_more.shap_beeswarm_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.shap_more import shap_beeswarm_plot_static

rng = np.random.default_rng(42)
feature_names = [
    "credit_score", "debt_to_income", "loan_amount",
    "employment_years", "annual_income", "late_payments",
    "num_open_accounts", "age",
]
X = rng.normal(0, 1, size=(80, 8))
coef = np.array([-0.6, 0.5, 0.3, -0.25, -0.2, 0.35, 0.1, -0.05])
shap_values = X * coef + rng.normal(0, 0.05, size=(80, 8))
ax = shap_beeswarm_plot_static(
    shap_values, X, feature_names, top_n=8,
    title="SHAP beeswarm - credit default model (80 applicants)",
)
plt.show()''',
    "dataviz.xai.shap_more.shap_beeswarm_plot_interactive": '''import numpy as np
from dataviz.xai.shap_more import shap_beeswarm_plot_interactive

rng = np.random.default_rng(42)
feature_names = [
    "credit_score", "debt_to_income", "loan_amount",
    "employment_years", "annual_income", "late_payments",
    "num_open_accounts", "age",
]
X = rng.normal(0, 1, size=(80, 8))
coef = np.array([-0.6, 0.5, 0.3, -0.25, -0.2, 0.35, 0.1, -0.05])
shap_values = X * coef + rng.normal(0, 0.05, size=(80, 8))
fig = shap_beeswarm_plot_interactive(
    shap_values, X, feature_names, top_n=8,
    title="SHAP beeswarm - credit default model (80 applicants)",
)
fig.show()''',
    "dataviz.xai.shap_more.shap_heatmap_instances_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.shap_more import shap_heatmap_instances_static

rng = np.random.default_rng(42)
feature_names = [
    "credit_score", "debt_to_income", "loan_amount",
    "employment_years", "annual_income", "late_payments",
    "num_open_accounts", "age",
]
coef = np.array([-0.6, 0.5, 0.3, -0.25, -0.2, 0.35, 0.1, -0.05])
group_a = rng.normal(-1, 0.5, size=(20, 8)) * coef
group_b = rng.normal(1, 0.5, size=(20, 8)) * coef
shap_values = np.vstack([group_a, group_b])
ax = shap_heatmap_instances_static(
    shap_values, feature_names, top_n_features=8,
    title="Per-instance SHAP heatmap reveals two applicant segments",
)
plt.show()''',
    "dataviz.xai.shap_more.shap_heatmap_instances_interactive": '''import numpy as np
from dataviz.xai.shap_more import shap_heatmap_instances_interactive

rng = np.random.default_rng(42)
feature_names = [
    "credit_score", "debt_to_income", "loan_amount",
    "employment_years", "annual_income", "late_payments",
    "num_open_accounts", "age",
]
coef = np.array([-0.6, 0.5, 0.3, -0.25, -0.2, 0.35, 0.1, -0.05])
group_a = rng.normal(-1, 0.5, size=(20, 8)) * coef
group_b = rng.normal(1, 0.5, size=(20, 8)) * coef
shap_values = np.vstack([group_a, group_b])
fig = shap_heatmap_instances_interactive(
    shap_values, feature_names, top_n_features=8,
    title="Per-instance SHAP heatmap reveals two applicant segments",
)
fig.show()''',
    "dataviz.xai.shap_more.shap_force_stacked_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.shap_more import shap_force_stacked_static

rng = np.random.default_rng(42)
feature_names = [
    "tenure_months", "monthly_charges", "contract_two_year",
    "num_support_calls", "avg_session_min", "late_payments",
    "plan_premium", "age",
]
scale = np.array([0.8, 0.4, 0.6, 0.35, 0.15, 0.3, 0.15, 0.1])
shap_values = rng.normal(0, 1, size=(40, 8)) * scale
ax = shap_force_stacked_static(
    shap_values, -1.10, feature_names, top_n=6,
    title="Stacked SHAP forces across 40 scored customers",
)
plt.show()''',
    "dataviz.xai.shap_more.shap_force_stacked_interactive": '''import numpy as np
from dataviz.xai.shap_more import shap_force_stacked_interactive

rng = np.random.default_rng(42)
feature_names = [
    "tenure_months", "monthly_charges", "contract_two_year",
    "num_support_calls", "avg_session_min", "late_payments",
    "plan_premium", "age",
]
scale = np.array([0.8, 0.4, 0.6, 0.35, 0.15, 0.3, 0.15, 0.1])
shap_values = rng.normal(0, 1, size=(40, 8)) * scale
fig = shap_force_stacked_interactive(
    shap_values, -1.10, feature_names, top_n=6,
    title="Stacked SHAP forces across 40 scored customers",
)
fig.show()''',
    "dataviz.xai.shap_more.shap_main_vs_interaction_bar_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.shap_more import shap_main_vs_interaction_bar_static

rng = np.random.default_rng(42)
feature_names = [
    "tenure_months", "monthly_charges", "contract_two_year",
    "num_support_calls", "avg_session_min", "late_payments",
    "plan_premium", "age",
]
main_scale = np.array([0.7, 0.45, 0.5, 0.3, 0.15, 0.28, 0.12, 0.08])
inter_scale = np.array([0.15, 0.25, 0.08, 0.12, 0.05, 0.07, 0.04, 0.02])
main_effects = rng.normal(0, 1, size=(60, 8)) * main_scale
interaction_effects = rng.normal(0, 1, size=(60, 8)) * inter_scale
ax = shap_main_vs_interaction_bar_static(
    main_effects, interaction_effects, feature_names, top_n=8,
    title="Main effects dominate, but charges interact strongly",
)
plt.show()''',
    "dataviz.xai.shap_more.shap_main_vs_interaction_bar_interactive": '''import numpy as np
from dataviz.xai.shap_more import shap_main_vs_interaction_bar_interactive

rng = np.random.default_rng(42)
feature_names = [
    "tenure_months", "monthly_charges", "contract_two_year",
    "num_support_calls", "avg_session_min", "late_payments",
    "plan_premium", "age",
]
main_scale = np.array([0.7, 0.45, 0.5, 0.3, 0.15, 0.28, 0.12, 0.08])
inter_scale = np.array([0.15, 0.25, 0.08, 0.12, 0.05, 0.07, 0.04, 0.02])
main_effects = rng.normal(0, 1, size=(60, 8)) * main_scale
interaction_effects = rng.normal(0, 1, size=(60, 8)) * inter_scale
fig = shap_main_vs_interaction_bar_interactive(
    main_effects, interaction_effects, feature_names, top_n=8,
    title="Main effects dominate, but charges interact strongly",
)
fig.show()''',
    "dataviz.xai.shap_more.shap_monotonicity_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.shap_more import shap_monotonicity_plot_static

rng = np.random.default_rng(42)
credit_score = rng.uniform(300, 850, size=80)
shap_values = (
    -0.004 * (credit_score - 575)
    + rng.normal(0, 0.08, size=credit_score.size)
)
ax = shap_monotonicity_plot_static(
    credit_score, shap_values, "credit_score",
    title="Monotonicity check: higher score always lowers risk",
)
plt.show()''',
    "dataviz.xai.shap_more.shap_monotonicity_plot_interactive": '''import numpy as np
from dataviz.xai.shap_more import shap_monotonicity_plot_interactive

rng = np.random.default_rng(42)
credit_score = rng.uniform(300, 850, size=80)
shap_values = (
    -0.004 * (credit_score - 575)
    + rng.normal(0, 0.08, size=credit_score.size)
)
fig = shap_monotonicity_plot_interactive(
    credit_score, shap_values, "credit_score",
    title="Monotonicity check: higher score always lowers risk",
)
fig.show()''',
    "dataviz.xai.shap_more.shap_temporal_drift_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.xai.shap_more import shap_temporal_drift_static

rng = np.random.default_rng(42)
feature_names = [
    "tenure_months", "monthly_charges", "contract_two_year",
    "num_support_calls", "avg_session_min", "late_payments",
]
n_days = 84
timestamps = pd.Series(pd.date_range("2024-01-01", periods=n_days, freq="D"))
scale = np.array([0.8, 0.4, 0.6, 0.35, 0.15, 0.3])
shap_values = rng.normal(0, 1, size=(n_days, len(feature_names))) * scale
trend = np.linspace(0, 0.5, n_days)
shap_values[:, 3] = shap_values[:, 3] + trend
ax = shap_temporal_drift_static(
    timestamps, shap_values, feature_names, freq="W", top_n=4,
    title="Weekly SHAP drift - support calls gain importance",
)
plt.show()''',
    "dataviz.xai.shap_more.shap_temporal_drift_interactive": '''import numpy as np
import pandas as pd
from dataviz.xai.shap_more import shap_temporal_drift_interactive

rng = np.random.default_rng(42)
feature_names = [
    "tenure_months", "monthly_charges", "contract_two_year",
    "num_support_calls", "avg_session_min", "late_payments",
]
n_days = 84
timestamps = pd.Series(pd.date_range("2024-01-01", periods=n_days, freq="D"))
scale = np.array([0.8, 0.4, 0.6, 0.35, 0.15, 0.3])
shap_values = rng.normal(0, 1, size=(n_days, len(feature_names))) * scale
trend = np.linspace(0, 0.5, n_days)
shap_values[:, 3] = shap_values[:, 3] + trend
fig = shap_temporal_drift_interactive(
    timestamps, shap_values, feature_names, freq="W", top_n=4,
    title="Weekly SHAP drift - support calls gain importance",
)
fig.show()''',
    "dataviz.xai.surrogate.surrogate_tree_plot_static": '''import matplotlib.pyplot as plt
from dataviz.xai.surrogate import surrogate_tree_plot_static

rules = [
    {"depth": 0, "condition": "credit_score < 620"},
    {"depth": 1, "parent": 0, "condition": "debt_to_income >= 0.43"},
    {"depth": 1, "parent": 0, "condition": "debt_to_income < 0.43"},
    {"depth": 2, "parent": 1, "condition": "late_payments > 0",
     "prediction": "deny (p=0.91)"},
    {"depth": 2, "parent": 1, "condition": "late_payments = 0",
     "prediction": "manual review (p=0.55)"},
    {"depth": 2, "parent": 2, "condition": "employment_years < 2",
     "prediction": "deny (p=0.74)"},
    {"depth": 2, "parent": 2, "condition": "employment_years >= 2",
     "prediction": "approve (p=0.68)"},
]
ax = surrogate_tree_plot_static(
    rules, title="Surrogate tree approximating the credit-risk black box",
)
plt.show()''',
    "dataviz.xai.surrogate.surrogate_tree_plot_interactive": '''from dataviz.xai.surrogate import surrogate_tree_plot_interactive

rules = [
    {"depth": 0, "condition": "credit_score < 620"},
    {"depth": 1, "parent": 0, "condition": "debt_to_income >= 0.43"},
    {"depth": 1, "parent": 0, "condition": "debt_to_income < 0.43"},
    {"depth": 2, "parent": 1, "condition": "late_payments > 0",
     "prediction": "deny (p=0.91)"},
    {"depth": 2, "parent": 1, "condition": "late_payments = 0",
     "prediction": "manual review (p=0.55)"},
    {"depth": 2, "parent": 2, "condition": "employment_years < 2",
     "prediction": "deny (p=0.74)"},
    {"depth": 2, "parent": 2, "condition": "employment_years >= 2",
     "prediction": "approve (p=0.68)"},
]
fig = surrogate_tree_plot_interactive(
    rules, title="Surrogate tree approximating the credit-risk black box",
)
fig.show()''',
    "dataviz.xai.surrogate.counterfactual_change_bar_static": '''import matplotlib.pyplot as plt
from dataviz.xai.surrogate import counterfactual_change_bar_static

original = {
    "credit_score": 598.0, "debt_to_income": 0.46,
    "loan_amount": 22000.0, "annual_income": 48000.0,
    "employment_years": 1.0, "late_payments": 2.0,
}
counterfactual = {
    "credit_score": 645.0, "debt_to_income": 0.38,
    "loan_amount": 18000.0, "annual_income": 48000.0,
    "employment_years": 1.0, "late_payments": 0.0,
}
ax = counterfactual_change_bar_static(
    original, counterfactual, top_n=6,
    title="Smallest changes to flip applicant #2048 to approval",
)
plt.show()''',
    "dataviz.xai.surrogate.counterfactual_change_bar_interactive": '''from dataviz.xai.surrogate import counterfactual_change_bar_interactive

original = {
    "credit_score": 598.0, "debt_to_income": 0.46,
    "loan_amount": 22000.0, "annual_income": 48000.0,
    "employment_years": 1.0, "late_payments": 2.0,
}
counterfactual = {
    "credit_score": 645.0, "debt_to_income": 0.38,
    "loan_amount": 18000.0, "annual_income": 48000.0,
    "employment_years": 1.0, "late_payments": 0.0,
}
fig = counterfactual_change_bar_interactive(
    original, counterfactual, top_n=6,
    title="Smallest changes to flip applicant #2048 to approval",
)
fig.show()''',
    "dataviz.xai.uncertainty.prediction_uncertainty_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.uncertainty import prediction_uncertainty_plot_static

rng = np.random.default_rng(42)
annual_income = np.linspace(20000, 150000, 50)
logit = -2.5 + 2.0 * (annual_income - 20000) / 130000
predictions = 1.0 / (1.0 + np.exp(-logit))
uncertainty = 0.03 + 0.10 * np.abs(annual_income - 85000) / 65000
ax = prediction_uncertainty_plot_static(
    annual_income, predictions, uncertainty, "annual_income",
    title="Approval probability with ensemble std band",
)
ax.set_ylabel("Predicted approval probability")
plt.show()''',
    "dataviz.xai.uncertainty.prediction_uncertainty_plot_interactive": '''import numpy as np
from dataviz.xai.uncertainty import prediction_uncertainty_plot_interactive

rng = np.random.default_rng(42)
annual_income = np.linspace(20000, 150000, 50)
logit = -2.5 + 2.0 * (annual_income - 20000) / 130000
predictions = 1.0 / (1.0 + np.exp(-logit))
uncertainty = 0.03 + 0.10 * np.abs(annual_income - 85000) / 65000
fig = prediction_uncertainty_plot_interactive(
    annual_income, predictions, uncertainty, "annual_income",
    title="Approval probability with ensemble std band",
)
fig.show()''',
    "dataviz.xai.uncertainty.confidence_attribution_bar_static": '''import matplotlib.pyplot as plt
from dataviz.xai.uncertainty import confidence_attribution_bar_static

attribution = {
    "thin_credit_history": 0.142,
    "num_open_accounts": 0.087,
    "employment_years": 0.064,
    "loan_amount": 0.031,
    "annual_income": -0.028,
    "credit_score": -0.052,
}
ax = confidence_attribution_bar_static(
    attribution,
    title="Which features drive predictive uncertainty - applicant #992",
)
plt.show()''',
    "dataviz.xai.uncertainty.confidence_attribution_bar_interactive": '''from dataviz.xai.uncertainty import confidence_attribution_bar_interactive

attribution = {
    "thin_credit_history": 0.142,
    "num_open_accounts": 0.087,
    "employment_years": 0.064,
    "loan_amount": 0.031,
    "annual_income": -0.028,
    "credit_score": -0.052,
}
fig = confidence_attribution_bar_interactive(
    attribution,
    title="Which features drive predictive uncertainty - applicant #992",
)
fig.show()''',
    "dataviz.xai.uncertainty.epistemic_vs_aleatoric_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.uncertainty import epistemic_vs_aleatoric_plot_static

bin_centers = np.linspace(0.0, 1.0, 20)
epistemic = 0.05 + 0.12 * (bin_centers - 0.5) ** 2 * 4
aleatoric = 0.08 + 0.05 * np.sin(np.pi * bin_centers)
ax = epistemic_vs_aleatoric_plot_static(
    bin_centers, epistemic, aleatoric,
    title="Uncertainty decomposition across predicted-risk deciles",
)
ax.set_xlabel("Predicted default risk (binned)")
plt.show()''',
    "dataviz.xai.uncertainty.epistemic_vs_aleatoric_plot_interactive": '''import numpy as np
from dataviz.xai.uncertainty import epistemic_vs_aleatoric_plot_interactive

bin_centers = np.linspace(0.0, 1.0, 20)
epistemic = 0.05 + 0.12 * (bin_centers - 0.5) ** 2 * 4
aleatoric = 0.08 + 0.05 * np.sin(np.pi * bin_centers)
fig = epistemic_vs_aleatoric_plot_interactive(
    bin_centers, epistemic, aleatoric,
    title="Uncertainty decomposition across predicted-risk deciles",
)
fig.show()''',
}
