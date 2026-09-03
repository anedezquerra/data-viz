"""Curated Complete-example snippets for dataviz.xai API pages."""

EXAMPLES = {
    "dataviz.xai.charts.feature_importance": '''import pandas as pd
import matplotlib.pyplot as plt
from dataviz.xai.charts import feature_importance

importances = pd.Series(
    [0.32, 0.21, 0.15, 0.09],
    index=["age", "income", "tenure", "region_score"],
)

ax = feature_importance(importances)
plt.show()
''',
    "dataviz.xai.cohort.importance_by_segment_heatmap_static": '''import matplotlib.pyplot as plt
from dataviz.xai.cohort import importance_by_segment_heatmap_static

importances = {
    "young": {"age": 0.30, "income": 0.12, "tenure": 0.08},
    "middle": {"age": 0.18, "income": 0.25, "tenure": 0.10},
    "senior": {"age": 0.10, "income": 0.20, "tenure": 0.22},
}

ax = importance_by_segment_heatmap_static(importances)
plt.show()
''',
    "dataviz.xai.cohort.importance_by_segment_heatmap_interactive": '''from dataviz.xai.cohort import importance_by_segment_heatmap_interactive

importances = {
    "young": {"age": 0.30, "income": 0.12, "tenure": 0.08},
    "middle": {"age": 0.18, "income": 0.25, "tenure": 0.10},
    "senior": {"age": 0.10, "income": 0.20, "tenure": 0.22},
}

fig = importance_by_segment_heatmap_interactive(importances)
fig.show()
''',
    "dataviz.xai.cohort.shap_cluster_heatmap_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.cohort import shap_cluster_heatmap_static

rng = np.random.default_rng(7)
shap_values = rng.normal(0.0, 0.2, size=(48, 5))
feature_names = ["age", "income", "tenure", "debt", "region_score"]

ax = shap_cluster_heatmap_static(shap_values, feature_names)
plt.show()
''',
    "dataviz.xai.cohort.shap_cluster_heatmap_interactive": '''import numpy as np
from dataviz.xai.cohort import shap_cluster_heatmap_interactive

rng = np.random.default_rng(7)
shap_values = rng.normal(0.0, 0.2, size=(48, 5))
feature_names = ["age", "income", "tenure", "debt", "region_score"]

fig = shap_cluster_heatmap_interactive(shap_values, feature_names)
fig.show()
''',
    "dataviz.xai.comparison.importance_comparison_heatmap_static": '''import pandas as pd
import matplotlib.pyplot as plt
from dataviz.xai.comparison import importance_comparison_heatmap_static

importance_matrix = pd.DataFrame(
    {
        "age": [0.30, 0.22, 0.26],
        "income": [0.25, 0.31, 0.28],
        "tenure": [0.10, 0.08, 0.12],
    },
    index=["logistic", "random_forest", "gradient_boosting"],
)

ax = importance_comparison_heatmap_static(importance_matrix)
plt.show()
''',
    "dataviz.xai.comparison.importance_comparison_heatmap_interactive": '''import pandas as pd
from dataviz.xai.comparison import importance_comparison_heatmap_interactive

importance_matrix = pd.DataFrame(
    {
        "age": [0.30, 0.22, 0.26],
        "income": [0.25, 0.31, 0.28],
        "tenure": [0.10, 0.08, 0.12],
    },
    index=["logistic", "random_forest", "gradient_boosting"],
)

fig = importance_comparison_heatmap_interactive(importance_matrix)
fig.show()
''',
    "dataviz.xai.comparison.shap_model_agreement_scatter_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.comparison import shap_model_agreement_scatter_static

rng = np.random.default_rng(11)
shap_a = rng.normal(0.0, 0.3, size=(60, 4))
shap_b = shap_a + rng.normal(0.0, 0.05, size=(60, 4))
feature_names = ["age", "income", "tenure", "debt"]

ax = shap_model_agreement_scatter_static(
    shap_a, shap_b, model_a="random forest", model_b="xgboost",
    feature_names=feature_names,
)
plt.show()
''',
    "dataviz.xai.comparison.shap_model_agreement_scatter_interactive": '''import numpy as np
from dataviz.xai.comparison import shap_model_agreement_scatter_interactive

rng = np.random.default_rng(11)
shap_a = rng.normal(0.0, 0.3, size=(60, 4))
shap_b = shap_a + rng.normal(0.0, 0.05, size=(60, 4))
feature_names = ["age", "income", "tenure", "debt"]

fig = shap_model_agreement_scatter_interactive(
    shap_a, shap_b, model_a="random forest", model_b="xgboost",
    feature_names=feature_names,
)
fig.show()
''',
    "dataviz.xai.comparison.rashomon_importance_band_static": '''import pandas as pd
import matplotlib.pyplot as plt
from dataviz.xai.comparison import rashomon_importance_band_static

importances_by_model = pd.DataFrame(
    {
        "age": [0.30, 0.26, 0.33, 0.28],
        "income": [0.25, 0.29, 0.22, 0.27],
        "tenure": [0.10, 0.12, 0.09, 0.11],
    },
    index=["model_1", "model_2", "model_3", "model_4"],
)

ax = rashomon_importance_band_static(importances_by_model)
plt.show()
''',
    "dataviz.xai.comparison.rashomon_importance_band_interactive": '''import pandas as pd
from dataviz.xai.comparison import rashomon_importance_band_interactive

importances_by_model = pd.DataFrame(
    {
        "age": [0.30, 0.26, 0.33, 0.28],
        "income": [0.25, 0.29, 0.22, 0.27],
        "tenure": [0.10, 0.12, 0.09, 0.11],
    },
    index=["model_1", "model_2", "model_3", "model_4"],
)

fig = rashomon_importance_band_interactive(importances_by_model)
fig.show()
''',
    "dataviz.xai.concept.concept_activation_bar_static": '''import matplotlib.pyplot as plt
from dataviz.xai.concept import concept_activation_bar_static

scores = {"striped": 0.62, "dotted": 0.35, "metallic": 0.12, "wooden": 0.48}
p_values = {"striped": 0.001, "dotted": 0.04, "metallic": 0.30, "wooden": 0.008}

ax = concept_activation_bar_static(scores, p_values=p_values)
plt.show()
''',
    "dataviz.xai.concept.concept_activation_bar_interactive": '''from dataviz.xai.concept import concept_activation_bar_interactive

scores = {"striped": 0.62, "dotted": 0.35, "metallic": 0.12, "wooden": 0.48}
p_values = {"striped": 0.001, "dotted": 0.04, "metallic": 0.30, "wooden": 0.008}

fig = concept_activation_bar_interactive(scores, p_values=p_values)
fig.show()
''',
    "dataviz.xai.concept.saliency_overlay_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.concept import saliency_overlay_plot_static

rng = np.random.default_rng(3)
images = [rng.random((12, 12)) for _ in range(3)]
saliencies = [rng.random((12, 12)) for _ in range(3)]
labels = ["sample A", "sample B", "sample C"]

ax = saliency_overlay_plot_static(images, saliencies, labels=labels)
plt.show()
''',
    "dataviz.xai.concept.saliency_overlay_plot_interactive": '''import numpy as np
from dataviz.xai.concept import saliency_overlay_plot_interactive

rng = np.random.default_rng(3)
images = [rng.random((12, 12)) for _ in range(3)]
saliencies = [rng.random((12, 12)) for _ in range(3)]
labels = ["sample A", "sample B", "sample C"]

fig = saliency_overlay_plot_interactive(images, saliencies, labels=labels)
fig.show()
''',
    "dataviz.xai.concept.attention_heatmap_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.concept import attention_heatmap_static

rng = np.random.default_rng(5)
attention = rng.random((4, 4))
tokens_x = ["loan", "amount", "risk", "score"]

ax = attention_heatmap_static(attention, tokens_x)
plt.show()
''',
    "dataviz.xai.concept.embedding_projection_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.concept import embedding_projection_plot_static

rng = np.random.default_rng(9)
coords = rng.normal(0.0, 1.0, size=(40, 2))
labels = ["low" if v < 0 else "high" for v in coords[:, 0]]

ax = embedding_projection_plot_static(coords, labels=labels)
plt.show()
''',
    "dataviz.xai.concept.embedding_projection_plot_interactive": '''import numpy as np
from dataviz.xai.concept import embedding_projection_plot_interactive

rng = np.random.default_rng(9)
coords = rng.normal(0.0, 1.0, size=(40, 2))
labels = ["low" if v < 0 else "high" for v in coords[:, 0]]

fig = embedding_projection_plot_interactive(coords, labels=labels)
fig.show()
''',
    "dataviz.xai.counterfactuals.counterfactual_path_plot_static": '''import pandas as pd
import matplotlib.pyplot as plt
from dataviz.xai.counterfactuals import counterfactual_path_plot_static

steps = pd.DataFrame(
    {
        "income": [45.0, 52.0, 52.0, 61.0],
        "debt": [30.0, 30.0, 22.0, 22.0],
        "tenure": [2.0, 2.0, 2.0, 3.5],
    }
)
predictions = [0.32, 0.41, 0.47, 0.58]

ax = counterfactual_path_plot_static(steps, predictions)
plt.show()
''',
    "dataviz.xai.counterfactuals.counterfactual_path_plot_interactive": '''import pandas as pd
from dataviz.xai.counterfactuals import counterfactual_path_plot_interactive

steps = pd.DataFrame(
    {
        "income": [45.0, 52.0, 52.0, 61.0],
        "debt": [30.0, 30.0, 22.0, 22.0],
        "tenure": [2.0, 2.0, 2.0, 3.5],
    }
)
predictions = [0.32, 0.41, 0.47, 0.58]

fig = counterfactual_path_plot_interactive(steps, predictions)
fig.show()
''',
    "dataviz.xai.counterfactuals.diverse_counterfactual_grid_static": '''import pandas as pd
import matplotlib.pyplot as plt
from dataviz.xai.counterfactuals import diverse_counterfactual_grid_static

original = {"income": 45.0, "debt": 30.0, "tenure": 2.0}
counterfactuals = pd.DataFrame(
    {
        "income": [55.0, 48.0, 62.0],
        "debt": [24.0, 26.0, 30.0],
        "tenure": [2.0, 3.0, 4.0],
    }
)

ax = diverse_counterfactual_grid_static(original, counterfactuals)
plt.show()
''',
    "dataviz.xai.counterfactuals.diverse_counterfactual_grid_interactive": '''import pandas as pd
from dataviz.xai.counterfactuals import diverse_counterfactual_grid_interactive

original = {"income": 45.0, "debt": 30.0, "tenure": 2.0}
counterfactuals = pd.DataFrame(
    {
        "income": [55.0, 48.0, 62.0],
        "debt": [24.0, 26.0, 30.0],
        "tenure": [2.0, 3.0, 4.0],
    }
)

fig = diverse_counterfactual_grid_interactive(original, counterfactuals)
fig.show()
''',
    "dataviz.xai.counterfactuals.what_if_slider_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.counterfactuals import what_if_slider_plot_static

feature_grid = np.linspace(20.0, 80.0, 25)
predictions = 1.0 / (1.0 + np.exp(-(feature_grid - 50.0) / 8.0))

ax = what_if_slider_plot_static(
    feature_grid, predictions, feature_name="income",
    current_value=45.0, threshold=0.5,
)
plt.show()
''',
    "dataviz.xai.counterfactuals.what_if_slider_plot_interactive": '''import numpy as np
from dataviz.xai.counterfactuals import what_if_slider_plot_interactive

feature_grid = np.linspace(20.0, 80.0, 25)
predictions = 1.0 / (1.0 + np.exp(-(feature_grid - 50.0) / 8.0))

fig = what_if_slider_plot_interactive(
    feature_grid, predictions, feature_name="income",
    current_value=45.0, threshold=0.5,
)
fig.show()
''',
    "dataviz.xai.dependence_more.pdp_with_ice_overlay_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.dependence_more import pdp_with_ice_overlay_static

rng = np.random.default_rng(17)
grid = np.linspace(0.0, 10.0, 20)
ice_curves = (
    np.sin(grid)[None, :] * rng.uniform(0.5, 1.5, size=(15, 1))
    + rng.normal(0.0, 0.05, size=(15, 20))
)
pdp = ice_curves.mean(axis=0)

ax = pdp_with_ice_overlay_static(grid, ice_curves, pdp, feature_name="income")
plt.show()
''',
    "dataviz.xai.dependence_more.pdp_with_ice_overlay_interactive": '''import numpy as np
from dataviz.xai.dependence_more import pdp_with_ice_overlay_interactive

rng = np.random.default_rng(17)
grid = np.linspace(0.0, 10.0, 20)
ice_curves = (
    np.sin(grid)[None, :] * rng.uniform(0.5, 1.5, size=(15, 1))
    + rng.normal(0.0, 0.05, size=(15, 20))
)
pdp = ice_curves.mean(axis=0)

fig = pdp_with_ice_overlay_interactive(grid, ice_curves, pdp, feature_name="income")
fig.show()
''',
    "dataviz.xai.dependence_more.ale_plot_2d_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.dependence_more import ale_plot_2d_static

rng = np.random.default_rng(19)
x_edges = np.linspace(0.0, 5.0, 6)
y_edges = np.linspace(0.0, 4.0, 5)
ale_grid = rng.normal(0.0, 0.3, size=(5, 4))

ax = ale_plot_2d_static(
    ale_grid, x_edges, y_edges, feature_x="income", feature_y="tenure",
)
plt.show()
''',
    "dataviz.xai.dependence_more.ale_plot_2d_interactive": '''import numpy as np
from dataviz.xai.dependence_more import ale_plot_2d_interactive

rng = np.random.default_rng(19)
x_edges = np.linspace(0.0, 5.0, 6)
y_edges = np.linspace(0.0, 4.0, 5)
ale_grid = rng.normal(0.0, 0.3, size=(5, 4))

fig = ale_plot_2d_interactive(
    ale_grid, x_edges, y_edges, feature_x="income", feature_y="tenure",
)
fig.show()
''',
    "dataviz.xai.dependence_more.h_statistic_heatmap_static": '''import pandas as pd
import matplotlib.pyplot as plt
from dataviz.xai.dependence_more import h_statistic_heatmap_static

h_matrix = pd.DataFrame(
    [[1.0, 0.32, 0.05], [0.32, 1.0, 0.11], [0.05, 0.11, 1.0]],
    index=["age", "income", "tenure"],
    columns=["age", "income", "tenure"],
)

ax = h_statistic_heatmap_static(h_matrix)
plt.show()
''',
    "dataviz.xai.dependence_more.h_statistic_heatmap_interactive": '''import pandas as pd
from dataviz.xai.dependence_more import h_statistic_heatmap_interactive

h_matrix = pd.DataFrame(
    [[1.0, 0.32, 0.05], [0.32, 1.0, 0.11], [0.05, 0.11, 1.0]],
    index=["age", "income", "tenure"],
    columns=["age", "income", "tenure"],
)

fig = h_statistic_heatmap_interactive(h_matrix)
fig.show()
''',
    "dataviz.xai.dependence_more.interaction_network_static": '''import pandas as pd
import matplotlib.pyplot as plt
from dataviz.xai.dependence_more import interaction_network_static

interaction_matrix = pd.DataFrame(
    [[0.0, 0.32, 0.05], [0.32, 0.0, 0.11], [0.05, 0.11, 0.0]],
    index=["age", "income", "tenure"],
    columns=["age", "income", "tenure"],
)

ax = interaction_network_static(interaction_matrix)
plt.show()
''',
    "dataviz.xai.dependence_more.interaction_network_interactive": '''import pandas as pd
from dataviz.xai.dependence_more import interaction_network_interactive

interaction_matrix = pd.DataFrame(
    [[0.0, 0.32, 0.05], [0.32, 0.0, 0.11], [0.05, 0.11, 0.0]],
    index=["age", "income", "tenure"],
    columns=["age", "income", "tenure"],
)

fig = interaction_network_interactive(interaction_matrix)
fig.show()
''',
    "dataviz.xai.fairness_xai.disparate_impact_by_segment_static": '''import pandas as pd
import matplotlib.pyplot as plt
from dataviz.xai.fairness_xai import disparate_impact_by_segment_static

segment_metrics = pd.DataFrame(
    {"importance": [0.28, 0.22, 0.15], "positive_rate": [0.62, 0.55, 0.41]},
    index=["group_a", "group_b", "group_c"],
)

ax = disparate_impact_by_segment_static(segment_metrics, reference_rate=0.62)
plt.show()
''',
    "dataviz.xai.fairness_xai.disparate_impact_by_segment_interactive": '''import pandas as pd
from dataviz.xai.fairness_xai import disparate_impact_by_segment_interactive

segment_metrics = pd.DataFrame(
    {"importance": [0.28, 0.22, 0.15], "positive_rate": [0.62, 0.55, 0.41]},
    index=["group_a", "group_b", "group_c"],
)

fig = disparate_impact_by_segment_interactive(segment_metrics, reference_rate=0.62)
fig.show()
''',
    "dataviz.xai.fairness_xai.subgroup_shap_divergence_static": '''import matplotlib.pyplot as plt
from dataviz.xai.fairness_xai import subgroup_shap_divergence_static

divergence = {"age": 0.18, "income": 0.42, "tenure": 0.07, "debt": 0.25}

ax = subgroup_shap_divergence_static(divergence)
plt.show()
''',
    "dataviz.xai.fairness_xai.subgroup_shap_divergence_interactive": '''from dataviz.xai.fairness_xai import subgroup_shap_divergence_interactive

divergence = {"age": 0.18, "income": 0.42, "tenure": 0.07, "debt": 0.25}

fig = subgroup_shap_divergence_interactive(divergence)
fig.show()
''',
    "dataviz.xai.fairness_xai.intersectional_importance_heatmap_static": '''import pandas as pd
import matplotlib.pyplot as plt
from dataviz.xai.fairness_xai import intersectional_importance_heatmap_static

importance_cube = pd.DataFrame(
    {
        "age": [0.30, 0.24, 0.18, 0.27],
        "income": [0.22, 0.29, 0.31, 0.25],
        "tenure": [0.10, 0.08, 0.14, 0.09],
    },
    index=["young-a", "young-b", "senior-a", "senior-b"],
)

ax = intersectional_importance_heatmap_static(importance_cube)
plt.show()
''',
    "dataviz.xai.fairness_xai.intersectional_importance_heatmap_interactive": '''import pandas as pd
from dataviz.xai.fairness_xai import intersectional_importance_heatmap_interactive

importance_cube = pd.DataFrame(
    {
        "age": [0.30, 0.24, 0.18, 0.27],
        "income": [0.22, 0.29, 0.31, 0.25],
        "tenure": [0.10, 0.08, 0.14, 0.09],
    },
    index=["young-a", "young-b", "senior-a", "senior-b"],
)

fig = intersectional_importance_heatmap_interactive(importance_cube)
fig.show()
''',
    "dataviz.xai.feature_imp.feature_importance_static": '''import pandas as pd
import matplotlib.pyplot as plt
from dataviz.xai.feature_imp import feature_importance_static

importances = pd.Series(
    [0.32, 0.21, 0.15, 0.09],
    index=["age", "income", "tenure", "region_score"],
)

ax = feature_importance_static(importances)
plt.show()
''',
    "dataviz.xai.feature_imp.feature_importance_interactive": '''import pandas as pd
from dataviz.xai.feature_imp import feature_importance_interactive

importances = pd.Series(
    [0.32, 0.21, 0.15, 0.09],
    index=["age", "income", "tenure", "region_score"],
)

fig = feature_importance_interactive(importances)
fig.show()
''',
    "dataviz.xai.importance_extra.permutation_importance_bar_static": '''import matplotlib.pyplot as plt
from dataviz.xai.importance_extra import permutation_importance_bar_static

importances = {"age": 0.045, "income": 0.120, "tenure": 0.012, "debt": 0.067}
std = {"age": 0.008, "income": 0.020, "tenure": 0.004, "debt": 0.011}

ax = permutation_importance_bar_static(importances, std=std)
plt.show()
''',
    "dataviz.xai.importance_extra.permutation_importance_bar_interactive": '''from dataviz.xai.importance_extra import permutation_importance_bar_interactive

importances = {"age": 0.045, "income": 0.120, "tenure": 0.012, "debt": 0.067}
std = {"age": 0.008, "income": 0.020, "tenure": 0.004, "debt": 0.011}

fig = permutation_importance_bar_interactive(importances, std=std)
fig.show()
''',
    "dataviz.xai.importance_extra.feature_importance_grouped_bar_static": '''import matplotlib.pyplot as plt
from dataviz.xai.importance_extra import feature_importance_grouped_bar_static

importances = {
    "permutation": {"age": 0.05, "income": 0.12, "tenure": 0.02},
    "gain": {"age": 0.08, "income": 0.15, "tenure": 0.03},
}

ax = feature_importance_grouped_bar_static(importances)
plt.show()
''',
    "dataviz.xai.importance_extra.feature_importance_grouped_bar_interactive": '''from dataviz.xai.importance_extra import feature_importance_grouped_bar_interactive

importances = {
    "permutation": {"age": 0.05, "income": 0.12, "tenure": 0.02},
    "gain": {"age": 0.08, "income": 0.15, "tenure": 0.03},
}

fig = feature_importance_grouped_bar_interactive(importances)
fig.show()
''',
    "dataviz.xai.importance_extra.feature_importance_boxplot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.importance_extra import feature_importance_boxplot_static

rng = np.random.default_rng(23)
per_fold = {
    "age": rng.normal(0.05, 0.01, 5).tolist(),
    "income": rng.normal(0.12, 0.02, 5).tolist(),
    "tenure": rng.normal(0.02, 0.005, 5).tolist(),
}

ax = feature_importance_boxplot_static(per_fold)
plt.show()
''',
    "dataviz.xai.importance_extra.feature_importance_boxplot_interactive": '''import numpy as np
from dataviz.xai.importance_extra import feature_importance_boxplot_interactive

rng = np.random.default_rng(23)
per_fold = {
    "age": rng.normal(0.05, 0.01, 5).tolist(),
    "income": rng.normal(0.12, 0.02, 5).tolist(),
    "tenure": rng.normal(0.02, 0.005, 5).tolist(),
}

fig = feature_importance_boxplot_interactive(per_fold)
fig.show()
''',
    "dataviz.xai.importance_extra.drop_column_importance_bar_static": '''import matplotlib.pyplot as plt
from dataviz.xai.importance_extra import drop_column_importance_bar_static

deltas = {"age": 0.018, "income": 0.074, "tenure": 0.004, "debt": 0.031}

ax = drop_column_importance_bar_static(deltas)
plt.show()
''',
    "dataviz.xai.importance_extra.drop_column_importance_bar_interactive": '''from dataviz.xai.importance_extra import drop_column_importance_bar_interactive

deltas = {"age": 0.018, "income": 0.074, "tenure": 0.004, "debt": 0.031}

fig = drop_column_importance_bar_interactive(deltas)
fig.show()
''',
    "dataviz.xai.importance_extra.importance_method_scatter_static": '''import matplotlib.pyplot as plt
from dataviz.xai.importance_extra import importance_method_scatter_static

permutation = {"age": 0.05, "income": 0.12, "tenure": 0.02, "debt": 0.07}
gain = {"age": 0.08, "income": 0.15, "tenure": 0.03, "debt": 0.05}

ax = importance_method_scatter_static(
    permutation, gain, a_name="permutation", b_name="gain",
)
plt.show()
''',
    "dataviz.xai.importance_extra.importance_method_scatter_interactive": '''from dataviz.xai.importance_extra import importance_method_scatter_interactive

permutation = {"age": 0.05, "income": 0.12, "tenure": 0.02, "debt": 0.07}
gain = {"age": 0.08, "income": 0.15, "tenure": 0.03, "debt": 0.05}

fig = importance_method_scatter_interactive(
    permutation, gain, a_name="permutation", b_name="gain",
)
fig.show()
''',
    "dataviz.xai.importance_more.gain_importance_bar_static": '''import matplotlib.pyplot as plt
from dataviz.xai.importance_more import gain_importance_bar_static

gain = {"age": 0.18, "income": 0.34, "tenure": 0.07, "debt": 0.12}
split_count = {"age": 42.0, "income": 65.0, "tenure": 18.0, "debt": 27.0}

ax = gain_importance_bar_static(gain, split_count=split_count)
plt.show()
''',
    "dataviz.xai.importance_more.gain_importance_bar_interactive": '''from dataviz.xai.importance_more import gain_importance_bar_interactive

gain = {"age": 0.18, "income": 0.34, "tenure": 0.07, "debt": 0.12}
split_count = {"age": 42.0, "income": 65.0, "tenure": 18.0, "debt": 27.0}

fig = gain_importance_bar_interactive(gain, split_count=split_count)
fig.show()
''',
    "dataviz.xai.importance_more.importance_stability_plot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.xai.importance_more import importance_stability_plot_static

rng = np.random.default_rng(27)
fold_importances = pd.DataFrame(
    rng.normal([0.05, 0.12, 0.02], [0.01, 0.02, 0.005], size=(6, 3)),
    columns=["age", "income", "tenure"],
)

ax = importance_stability_plot_static(fold_importances)
plt.show()
''',
    "dataviz.xai.importance_more.importance_stability_plot_interactive": '''import numpy as np
import pandas as pd
from dataviz.xai.importance_more import importance_stability_plot_interactive

rng = np.random.default_rng(27)
fold_importances = pd.DataFrame(
    rng.normal([0.05, 0.12, 0.02], [0.01, 0.02, 0.005], size=(6, 3)),
    columns=["age", "income", "tenure"],
)

fig = importance_stability_plot_interactive(fold_importances)
fig.show()
''',
    "dataviz.xai.importance_more.importance_correlation_heatmap_static": '''import pandas as pd
import matplotlib.pyplot as plt
from dataviz.xai.importance_more import importance_correlation_heatmap_static

importances_by_model = pd.DataFrame(
    {
        "logistic": [0.30, 0.25, 0.10],
        "random_forest": [0.22, 0.31, 0.08],
        "xgboost": [0.26, 0.28, 0.12],
    },
    index=["age", "income", "tenure"],
)

ax = importance_correlation_heatmap_static(importances_by_model)
plt.show()
''',
    "dataviz.xai.importance_more.importance_correlation_heatmap_interactive": '''import pandas as pd
from dataviz.xai.importance_more import importance_correlation_heatmap_interactive

importances_by_model = pd.DataFrame(
    {
        "logistic": [0.30, 0.25, 0.10],
        "random_forest": [0.22, 0.31, 0.08],
        "xgboost": [0.26, 0.28, 0.12],
    },
    index=["age", "income", "tenure"],
)

fig = importance_correlation_heatmap_interactive(importances_by_model)
fig.show()
''',
    "dataviz.xai.importance_more.feature_clustermap_static": '''import pandas as pd
import matplotlib.pyplot as plt
from dataviz.xai.importance_more import feature_clustermap_static

importance_matrix = pd.DataFrame(
    {
        "logistic": [0.30, 0.25, 0.10, 0.05],
        "random_forest": [0.22, 0.31, 0.08, 0.12],
        "xgboost": [0.26, 0.28, 0.12, 0.09],
    },
    index=["age", "income", "tenure", "debt"],
)

ax = feature_clustermap_static(importance_matrix)
plt.show()
''',
    "dataviz.xai.importance_more.feature_clustermap_interactive": '''import pandas as pd
from dataviz.xai.importance_more import feature_clustermap_interactive

importance_matrix = pd.DataFrame(
    {
        "logistic": [0.30, 0.25, 0.10, 0.05],
        "random_forest": [0.22, 0.31, 0.08, 0.12],
        "xgboost": [0.26, 0.28, 0.12, 0.09],
    },
    index=["age", "income", "tenure", "debt"],
)

fig = feature_clustermap_interactive(importance_matrix)
fig.show()
''',
    "dataviz.xai.local_explanations.shap_force_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.local_explanations import shap_force_plot_static

shap_instance = np.array([0.25, -0.10, 0.05, -0.02])
feature_names = ["age", "income", "tenure", "debt"]

ax = shap_force_plot_static(shap_instance, feature_names, base_value=0.40)
plt.show()
''',
    "dataviz.xai.local_explanations.shap_force_plot_interactive": '''import numpy as np
from dataviz.xai.local_explanations import shap_force_plot_interactive

shap_instance = np.array([0.25, -0.10, 0.05, -0.02])
feature_names = ["age", "income", "tenure", "debt"]

fig = shap_force_plot_interactive(shap_instance, feature_names, base_value=0.40)
fig.show()
''',
    "dataviz.xai.local_explanations.lime_explanation_bar_static": '''import matplotlib.pyplot as plt
from dataviz.xai.local_explanations import lime_explanation_bar_static

contributions = [
    ("income > 50k", 0.21),
    ("tenure <= 2", -0.13),
    ("debt > 10k", -0.08),
    ("age > 40", 0.05),
]

ax = lime_explanation_bar_static(contributions)
plt.show()
''',
    "dataviz.xai.local_explanations.lime_explanation_bar_interactive": '''from dataviz.xai.local_explanations import lime_explanation_bar_interactive

contributions = [
    ("income > 50k", 0.21),
    ("tenure <= 2", -0.13),
    ("debt > 10k", -0.08),
    ("age > 40", 0.05),
]

fig = lime_explanation_bar_interactive(contributions)
fig.show()
''',
    "dataviz.xai.local_more.anchor_explanation_plot_static": '''import matplotlib.pyplot as plt
from dataviz.xai.local_more import anchor_explanation_plot_static

rules = [
    "income > 50k",
    "income > 50k AND tenure > 3",
    "income > 50k AND tenure > 3 AND debt <= 5k",
]
precision = [0.72, 0.85, 0.93]
coverage = [0.40, 0.25, 0.12]

ax = anchor_explanation_plot_static(rules, precision, coverage)
plt.show()
''',
    "dataviz.xai.local_more.anchor_explanation_plot_interactive": '''from dataviz.xai.local_more import anchor_explanation_plot_interactive

rules = [
    "income > 50k",
    "income > 50k AND tenure > 3",
    "income > 50k AND tenure > 3 AND debt <= 5k",
]
precision = [0.72, 0.85, 0.93]
coverage = [0.40, 0.25, 0.12]

fig = anchor_explanation_plot_interactive(rules, precision, coverage)
fig.show()
''',
    "dataviz.xai.local_more.nearest_neighbor_explanation_static": '''import pandas as pd
import matplotlib.pyplot as plt
from dataviz.xai.local_more import nearest_neighbor_explanation_static

query = {"income": 52.0, "debt": 8.0, "tenure": 4.0}
neighbors = pd.DataFrame(
    {
        "income": [50.0, 55.0, 49.0],
        "debt": [9.0, 7.5, 10.0],
        "tenure": [3.5, 4.5, 4.0],
    }
)
target = [1, 1, 0]

ax = nearest_neighbor_explanation_static(query, neighbors, target=target)
plt.show()
''',
    "dataviz.xai.local_more.nearest_neighbor_explanation_interactive": '''import pandas as pd
from dataviz.xai.local_more import nearest_neighbor_explanation_interactive

query = {"income": 52.0, "debt": 8.0, "tenure": 4.0}
neighbors = pd.DataFrame(
    {
        "income": [50.0, 55.0, 49.0],
        "debt": [9.0, 7.5, 10.0],
        "tenure": [3.5, 4.5, 4.0],
    }
)
target = [1, 1, 0]

fig = nearest_neighbor_explanation_interactive(query, neighbors, target=target)
fig.show()
''',
    "dataviz.xai.local_more.prototype_criticism_grid_static": '''import pandas as pd
import matplotlib.pyplot as plt
from dataviz.xai.local_more import prototype_criticism_grid_static

prototypes = pd.DataFrame(
    {"income": [35.0, 60.0], "debt": [5.0, 12.0], "tenure": [1.0, 6.0]}
)
criticisms = pd.DataFrame(
    {"income": [48.0], "debt": [20.0], "tenure": [2.5]}
)

ax = prototype_criticism_grid_static(prototypes, criticisms)
plt.show()
''',
    "dataviz.xai.local_more.prototype_criticism_grid_interactive": '''import pandas as pd
from dataviz.xai.local_more import prototype_criticism_grid_interactive

prototypes = pd.DataFrame(
    {"income": [35.0, 60.0], "debt": [5.0, 12.0], "tenure": [1.0, 6.0]}
)
criticisms = pd.DataFrame(
    {"income": [48.0], "debt": [20.0], "tenure": [2.5]}
)

fig = prototype_criticism_grid_interactive(prototypes, criticisms)
fig.show()
''',
    "dataviz.xai.local_more.contrastive_explanation_bar_static": '''import matplotlib.pyplot as plt
from dataviz.xai.local_more import contrastive_explanation_bar_static

pertinent_positives = {"income": 52.0, "tenure": 4.0}
pertinent_negatives = {"debt": 8.0, "region_score": 0.3}

ax = contrastive_explanation_bar_static(pertinent_positives, pertinent_negatives)
plt.show()
''',
    "dataviz.xai.local_more.contrastive_explanation_bar_interactive": '''from dataviz.xai.local_more import contrastive_explanation_bar_interactive

pertinent_positives = {"income": 52.0, "tenure": 4.0}
pertinent_negatives = {"debt": 8.0, "region_score": 0.3}

fig = contrastive_explanation_bar_interactive(pertinent_positives, pertinent_negatives)
fig.show()
''',
    "dataviz.xai.pdp_extra.partial_dependence_2d_heatmap_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.pdp_extra import partial_dependence_2d_heatmap_static

rng = np.random.default_rng(31)
x_grid = np.linspace(0.0, 5.0, 6)
y_grid = np.linspace(0.0, 4.0, 5)
pdp = rng.normal(0.5, 0.1, size=(5, 6))

ax = partial_dependence_2d_heatmap_static(
    x_grid, y_grid, pdp, feature_x="income", feature_y="tenure",
)
plt.show()
''',
    "dataviz.xai.pdp_extra.partial_dependence_2d_heatmap_interactive": '''import numpy as np
from dataviz.xai.pdp_extra import partial_dependence_2d_heatmap_interactive

rng = np.random.default_rng(31)
x_grid = np.linspace(0.0, 5.0, 6)
y_grid = np.linspace(0.0, 4.0, 5)
pdp = rng.normal(0.5, 0.1, size=(5, 6))

fig = partial_dependence_2d_heatmap_interactive(
    x_grid, y_grid, pdp, feature_x="income", feature_y="tenure",
)
fig.show()
''',
    "dataviz.xai.pdp_extra.ice_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.pdp_extra import ice_plot_static

rng = np.random.default_rng(33)
feature_values = np.linspace(20.0, 80.0, 15)
ice_curves = np.log(feature_values)[None, :] * rng.uniform(0.6, 1.4, size=(12, 1))

ax = ice_plot_static(feature_values, ice_curves, feature_name="income")
plt.show()
''',
    "dataviz.xai.pdp_extra.ice_plot_interactive": '''import numpy as np
from dataviz.xai.pdp_extra import ice_plot_interactive

rng = np.random.default_rng(33)
feature_values = np.linspace(20.0, 80.0, 15)
ice_curves = np.log(feature_values)[None, :] * rng.uniform(0.6, 1.4, size=(12, 1))

fig = ice_plot_interactive(feature_values, ice_curves, feature_name="income")
fig.show()
''',
    "dataviz.xai.pdp_extra.centered_ice_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.pdp_extra import centered_ice_plot_static

rng = np.random.default_rng(33)
feature_values = np.linspace(20.0, 80.0, 15)
ice_curves = np.log(feature_values)[None, :] * rng.uniform(0.6, 1.4, size=(12, 1))

ax = centered_ice_plot_static(feature_values, ice_curves, feature_name="income")
plt.show()
''',
    "dataviz.xai.pdp_extra.centered_ice_plot_interactive": '''import numpy as np
from dataviz.xai.pdp_extra import centered_ice_plot_interactive

rng = np.random.default_rng(33)
feature_values = np.linspace(20.0, 80.0, 15)
ice_curves = np.log(feature_values)[None, :] * rng.uniform(0.6, 1.4, size=(12, 1))

fig = centered_ice_plot_interactive(feature_values, ice_curves, feature_name="income")
fig.show()
''',
    "dataviz.xai.pdp_extra.ale_plot_1d_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.pdp_extra import ale_plot_1d_static

bin_edges = np.linspace(20.0, 80.0, 7)
ale = np.array([-0.12, -0.05, 0.01, 0.06, 0.10, 0.14])

ax = ale_plot_1d_static(bin_edges, ale, feature_name="income")
plt.show()
''',
    "dataviz.xai.shap_extra.shap_summary_dot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.shap_extra import shap_summary_dot_static

rng = np.random.default_rng(37)
shap_values = rng.normal(0.0, 0.2, size=(60, 4))
feature_values = rng.normal(0.0, 1.0, size=(60, 4))
feature_names = ["age", "income", "tenure", "debt"]

ax = shap_summary_dot_static(shap_values, feature_values, feature_names)
plt.show()
''',
    "dataviz.xai.shap_extra.shap_summary_dot_interactive": '''import numpy as np
from dataviz.xai.shap_extra import shap_summary_dot_interactive

rng = np.random.default_rng(37)
shap_values = rng.normal(0.0, 0.2, size=(60, 4))
feature_values = rng.normal(0.0, 1.0, size=(60, 4))
feature_names = ["age", "income", "tenure", "debt"]

fig = shap_summary_dot_interactive(shap_values, feature_values, feature_names)
fig.show()
''',
    "dataviz.xai.shap_extra.shap_dependence_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.shap_extra import shap_dependence_plot_static

rng = np.random.default_rng(39)
feature_values = rng.uniform(20.0, 80.0, 80)
shap_age = 0.02 * (feature_values - 50.0) + rng.normal(0.0, 0.03, 80)
interaction = rng.uniform(0.0, 1.0, 80)

ax = shap_dependence_plot_static(
    shap_age, feature_values, interaction_values=interaction,
    feature_name="age", interaction_name="tenure",
)
plt.show()
''',
    "dataviz.xai.shap_extra.shap_dependence_plot_interactive": '''import numpy as np
from dataviz.xai.shap_extra import shap_dependence_plot_interactive

rng = np.random.default_rng(39)
feature_values = rng.uniform(20.0, 80.0, 80)
shap_age = 0.02 * (feature_values - 50.0) + rng.normal(0.0, 0.03, 80)
interaction = rng.uniform(0.0, 1.0, 80)

fig = shap_dependence_plot_interactive(
    shap_age, feature_values, interaction_values=interaction,
    feature_name="age", interaction_name="tenure",
)
fig.show()
''',
    "dataviz.xai.shap_extra.shap_interaction_heatmap_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.shap_extra import shap_interaction_heatmap_static

interaction_matrix = np.array(
    [
        [0.20, 0.05, 0.02, 0.01],
        [0.05, 0.30, 0.04, 0.02],
        [0.02, 0.04, 0.15, 0.03],
        [0.01, 0.02, 0.03, 0.10],
    ]
)
feature_names = ["age", "income", "tenure", "debt"]

ax = shap_interaction_heatmap_static(interaction_matrix, feature_names)
plt.show()
''',
    "dataviz.xai.shap_extra.shap_waterfall_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.shap_extra import shap_waterfall_plot_static

shap_instance = np.array([0.18, -0.09, 0.05, -0.03, 0.02])
feature_names = ["age", "income", "tenure", "debt", "region_score"]

ax = shap_waterfall_plot_static(shap_instance, feature_names, base_value=0.35)
plt.show()
''',
    "dataviz.xai.shap_extra.shap_waterfall_plot_interactive": '''import numpy as np
from dataviz.xai.shap_extra import shap_waterfall_plot_interactive

shap_instance = np.array([0.18, -0.09, 0.05, -0.03, 0.02])
feature_names = ["age", "income", "tenure", "debt", "region_score"]

fig = shap_waterfall_plot_interactive(shap_instance, feature_names, base_value=0.35)
fig.show()
''',
    "dataviz.xai.shap_more.shap_beeswarm_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.shap_more import shap_beeswarm_plot_static

rng = np.random.default_rng(41)
shap_values = rng.normal(0.0, 0.2, size=(80, 4))
feature_values = rng.normal(0.0, 1.0, size=(80, 4))
feature_names = ["age", "income", "tenure", "debt"]

ax = shap_beeswarm_plot_static(shap_values, feature_values, feature_names)
plt.show()
''',
    "dataviz.xai.shap_more.shap_beeswarm_plot_interactive": '''import numpy as np
from dataviz.xai.shap_more import shap_beeswarm_plot_interactive

rng = np.random.default_rng(41)
shap_values = rng.normal(0.0, 0.2, size=(80, 4))
feature_values = rng.normal(0.0, 1.0, size=(80, 4))
feature_names = ["age", "income", "tenure", "debt"]

fig = shap_beeswarm_plot_interactive(shap_values, feature_values, feature_names)
fig.show()
''',
    "dataviz.xai.shap_more.shap_force_stacked_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.shap_more import shap_force_stacked_static

rng = np.random.default_rng(43)
shap_values = rng.normal(0.0, 0.15, size=(6, 4))
feature_names = ["age", "income", "tenure", "debt"]

ax = shap_force_stacked_static(shap_values, base_value=0.5, feature_names=feature_names)
plt.show()
''',
    "dataviz.xai.shap_more.shap_force_stacked_interactive": '''import numpy as np
from dataviz.xai.shap_more import shap_force_stacked_interactive

rng = np.random.default_rng(43)
shap_values = rng.normal(0.0, 0.15, size=(6, 4))
feature_names = ["age", "income", "tenure", "debt"]

fig = shap_force_stacked_interactive(shap_values, base_value=0.5, feature_names=feature_names)
fig.show()
''',
    "dataviz.xai.shap_more.shap_main_vs_interaction_bar_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.shap_more import shap_main_vs_interaction_bar_static

rng = np.random.default_rng(45)
main_effects = rng.normal([0.20, 0.12, 0.05, 0.03], 0.05, size=(50, 4))
interaction_effects = rng.normal([0.04, 0.06, 0.01, 0.02], 0.02, size=(50, 4))
feature_names = ["age", "income", "tenure", "debt"]

ax = shap_main_vs_interaction_bar_static(
    main_effects, interaction_effects, feature_names,
)
plt.show()
''',
    "dataviz.xai.shap_more.shap_main_vs_interaction_bar_interactive": '''import numpy as np
from dataviz.xai.shap_more import shap_main_vs_interaction_bar_interactive

rng = np.random.default_rng(45)
main_effects = rng.normal([0.20, 0.12, 0.05, 0.03], 0.05, size=(50, 4))
interaction_effects = rng.normal([0.04, 0.06, 0.01, 0.02], 0.02, size=(50, 4))
feature_names = ["age", "income", "tenure", "debt"]

fig = shap_main_vs_interaction_bar_interactive(
    main_effects, interaction_effects, feature_names,
)
fig.show()
''',
    "dataviz.xai.shap_more.shap_monotonicity_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.shap_more import shap_monotonicity_plot_static

rng = np.random.default_rng(47)
feature_values = np.sort(rng.uniform(20.0, 80.0, 60))
shap_values = 0.015 * (feature_values - 50.0) + rng.normal(0.0, 0.02, 60)

ax = shap_monotonicity_plot_static(feature_values, shap_values, feature_name="age")
plt.show()
''',
    "dataviz.xai.shap_more.shap_monotonicity_plot_interactive": '''import numpy as np
from dataviz.xai.shap_more import shap_monotonicity_plot_interactive

rng = np.random.default_rng(47)
feature_values = np.sort(rng.uniform(20.0, 80.0, 60))
shap_values = 0.015 * (feature_values - 50.0) + rng.normal(0.0, 0.02, 60)

fig = shap_monotonicity_plot_interactive(feature_values, shap_values, feature_name="age")
fig.show()
''',
    "dataviz.xai.shap_more.shap_temporal_drift_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.xai.shap_more import shap_temporal_drift_static

rng = np.random.default_rng(49)
timestamps = pd.Series(pd.date_range("2024-01-01", periods=56, freq="D"))
shap_values = rng.normal(0.0, 0.2, size=(56, 4))
feature_names = ["age", "income", "tenure", "debt"]

ax = shap_temporal_drift_static(timestamps, shap_values, feature_names)
plt.show()
''',
    "dataviz.xai.shap_more.shap_temporal_drift_interactive": '''import numpy as np
import pandas as pd
from dataviz.xai.shap_more import shap_temporal_drift_interactive

rng = np.random.default_rng(49)
timestamps = pd.Series(pd.date_range("2024-01-01", periods=56, freq="D"))
shap_values = rng.normal(0.0, 0.2, size=(56, 4))
feature_names = ["age", "income", "tenure", "debt"]

fig = shap_temporal_drift_interactive(timestamps, shap_values, feature_names)
fig.show()
''',
    "dataviz.xai.surrogate.surrogate_tree_plot_static": '''import matplotlib.pyplot as plt
from dataviz.xai.surrogate import surrogate_tree_plot_static

rules = [
    {"depth": 0, "condition": "income <= 50k"},
    {"depth": 1, "condition": "debt <= 10k", "parent": 0, "prediction": "approve"},
    {"depth": 1, "condition": "debt > 10k", "parent": 0, "prediction": "review"},
    {"depth": 0, "condition": "income > 50k", "prediction": "approve"},
]

ax = surrogate_tree_plot_static(rules)
plt.show()
''',
    "dataviz.xai.surrogate.surrogate_tree_plot_interactive": '''from dataviz.xai.surrogate import surrogate_tree_plot_interactive

rules = [
    {"depth": 0, "condition": "income <= 50k"},
    {"depth": 1, "condition": "debt <= 10k", "parent": 0, "prediction": "approve"},
    {"depth": 1, "condition": "debt > 10k", "parent": 0, "prediction": "review"},
    {"depth": 0, "condition": "income > 50k", "prediction": "approve"},
]

fig = surrogate_tree_plot_interactive(rules)
fig.show()
''',
    "dataviz.xai.surrogate.counterfactual_change_bar_static": '''import matplotlib.pyplot as plt
from dataviz.xai.surrogate import counterfactual_change_bar_static

original = {"income": 45.0, "debt": 30.0, "tenure": 2.0}
counterfactual = {"income": 58.0, "debt": 22.0, "tenure": 2.0}

ax = counterfactual_change_bar_static(original, counterfactual)
plt.show()
''',
    "dataviz.xai.surrogate.counterfactual_change_bar_interactive": '''from dataviz.xai.surrogate import counterfactual_change_bar_interactive

original = {"income": 45.0, "debt": 30.0, "tenure": 2.0}
counterfactual = {"income": 58.0, "debt": 22.0, "tenure": 2.0}

fig = counterfactual_change_bar_interactive(original, counterfactual)
fig.show()
''',
    "dataviz.xai.uncertainty.prediction_uncertainty_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.uncertainty import prediction_uncertainty_plot_static

rng = np.random.default_rng(53)
feature_values = np.sort(rng.uniform(20.0, 80.0, 40))
predictions = 1.0 / (1.0 + np.exp(-(feature_values - 50.0) / 10.0))
uncertainty = 0.05 + 0.04 * np.abs(feature_values - 50.0) / 30.0

ax = prediction_uncertainty_plot_static(
    feature_values, predictions, uncertainty, feature_name="income",
)
plt.show()
''',
    "dataviz.xai.uncertainty.prediction_uncertainty_plot_interactive": '''import numpy as np
from dataviz.xai.uncertainty import prediction_uncertainty_plot_interactive

rng = np.random.default_rng(53)
feature_values = np.sort(rng.uniform(20.0, 80.0, 40))
predictions = 1.0 / (1.0 + np.exp(-(feature_values - 50.0) / 10.0))
uncertainty = 0.05 + 0.04 * np.abs(feature_values - 50.0) / 30.0

fig = prediction_uncertainty_plot_interactive(
    feature_values, predictions, uncertainty, feature_name="income",
)
fig.show()
''',
    "dataviz.xai.uncertainty.confidence_attribution_bar_static": '''import matplotlib.pyplot as plt
from dataviz.xai.uncertainty import confidence_attribution_bar_static

attribution = {
    "entropy": 0.42,
    "margin": 0.31,
    "variance": 0.18,
    "disagreement": 0.09,
}

ax = confidence_attribution_bar_static(attribution)
plt.show()
''',
    "dataviz.xai.uncertainty.confidence_attribution_bar_interactive": '''from dataviz.xai.uncertainty import confidence_attribution_bar_interactive

attribution = {
    "entropy": 0.42,
    "margin": 0.31,
    "variance": 0.18,
    "disagreement": 0.09,
}

fig = confidence_attribution_bar_interactive(attribution)
fig.show()
''',
    "dataviz.xai.uncertainty.epistemic_vs_aleatoric_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.xai.uncertainty import epistemic_vs_aleatoric_plot_static

bin_centers = np.linspace(0.1, 0.9, 9)
epistemic = np.array([0.08, 0.06, 0.05, 0.04, 0.04, 0.05, 0.05, 0.06, 0.08])
aleatoric = np.array([0.03, 0.04, 0.05, 0.07, 0.08, 0.07, 0.05, 0.04, 0.03])

ax = epistemic_vs_aleatoric_plot_static(bin_centers, epistemic, aleatoric)
plt.show()
''',
    "dataviz.xai.uncertainty.epistemic_vs_aleatoric_plot_interactive": '''import numpy as np
from dataviz.xai.uncertainty import epistemic_vs_aleatoric_plot_interactive

bin_centers = np.linspace(0.1, 0.9, 9)
epistemic = np.array([0.08, 0.06, 0.05, 0.04, 0.04, 0.05, 0.05, 0.06, 0.08])
aleatoric = np.array([0.03, 0.04, 0.05, 0.07, 0.08, 0.07, 0.05, 0.04, 0.03])

fig = epistemic_vs_aleatoric_plot_interactive(bin_centers, epistemic, aleatoric)
fig.show()
''',
}
