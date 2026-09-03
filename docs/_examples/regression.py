"""Curated Complete-example snippets for dataviz.regression API pages."""

EXAMPLES = {
    "dataviz.regression.autocorrelation.residual_acf_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.autocorrelation import residual_acf_static

rng = np.random.default_rng(42)
y_true = rng.normal(10.0, 2.0, size=60)
y_pred = y_true + rng.normal(0.0, 0.5, size=60)

ax = residual_acf_static(y_true, y_pred, max_lag=10)
plt.show()
''',
    "dataviz.regression.autocorrelation.residual_acf_interactive": '''import numpy as np
from dataviz.regression.autocorrelation import residual_acf_interactive

rng = np.random.default_rng(42)
y_true = rng.normal(10.0, 2.0, size=60)
y_pred = y_true + rng.normal(0.0, 0.5, size=60)

fig = residual_acf_interactive(y_true, y_pred, max_lag=10)
fig.show()
''',
    "dataviz.regression.autocorrelation.residual_pacf_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.autocorrelation import residual_pacf_static

rng = np.random.default_rng(42)
y_true = rng.normal(10.0, 2.0, size=60)
y_pred = y_true + rng.normal(0.0, 0.5, size=60)

ax = residual_pacf_static(y_true, y_pred, max_lag=10)
plt.show()
''',
    "dataviz.regression.autocorrelation.residual_pacf_interactive": '''import numpy as np
from dataviz.regression.autocorrelation import residual_pacf_interactive

rng = np.random.default_rng(42)
y_true = rng.normal(10.0, 2.0, size=60)
y_pred = y_true + rng.normal(0.0, 0.5, size=60)

fig = residual_pacf_interactive(y_true, y_pred, max_lag=10)
fig.show()
''',
    "dataviz.regression.bayesian.posterior_coefficient_density_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.bayesian import posterior_coefficient_density_static

rng = np.random.default_rng(42)
samples_per_coef = [
    rng.normal(2.0, 0.3, size=200),
    rng.normal(-1.0, 0.3, size=200),
    rng.normal(0.5, 0.3, size=200),
]

ax = posterior_coefficient_density_static(
    samples_per_coef, coef_names=["beta0", "beta1", "beta2"]
)
plt.show()
''',
    "dataviz.regression.bayesian.posterior_coefficient_density_interactive": '''import numpy as np
from dataviz.regression.bayesian import posterior_coefficient_density_interactive

rng = np.random.default_rng(42)
samples_per_coef = [
    rng.normal(2.0, 0.3, size=200),
    rng.normal(-1.0, 0.3, size=200),
    rng.normal(0.5, 0.3, size=200),
]

fig = posterior_coefficient_density_interactive(
    samples_per_coef, coef_names=["beta0", "beta1", "beta2"]
)
fig.show()
''',
    "dataviz.regression.bayesian.credible_interval_forest_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.bayesian import credible_interval_forest_static

coef_names = ["beta0", "beta1", "beta2"]
means = np.array([2.0, -1.0, 0.5])
lower = means - 0.4
upper = means + 0.4

ax = credible_interval_forest_static(coef_names, means, lower, upper)
plt.show()
''',
    "dataviz.regression.bayesian.credible_interval_forest_interactive": '''import numpy as np
from dataviz.regression.bayesian import credible_interval_forest_interactive

coef_names = ["beta0", "beta1", "beta2"]
means = np.array([2.0, -1.0, 0.5])
lower = means - 0.4
upper = means + 0.4

fig = credible_interval_forest_interactive(coef_names, means, lower, upper)
fig.show()
''',
    "dataviz.regression.calibration_regression.uncertainty_band_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.calibration_regression import uncertainty_band_plot_static

rng = np.random.default_rng(42)
y_true = rng.normal(10.0, 2.0, size=60)
y_pred = y_true + rng.normal(0.0, 0.5, size=60)
y_std = np.full(60, 0.6)

ax = uncertainty_band_plot_static(y_true, y_pred, y_std)
plt.show()
''',
    "dataviz.regression.calibration_regression.uncertainty_band_plot_interactive": '''import numpy as np
from dataviz.regression.calibration_regression import uncertainty_band_plot_interactive

rng = np.random.default_rng(42)
y_true = rng.normal(10.0, 2.0, size=60)
y_pred = y_true + rng.normal(0.0, 0.5, size=60)
y_std = np.full(60, 0.6)

fig = uncertainty_band_plot_interactive(y_true, y_pred, y_std)
fig.show()
''',
    "dataviz.regression.comparison.multi_model_pred_vs_actual_overlay_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.comparison import multi_model_pred_vs_actual_overlay_static

rng = np.random.default_rng(42)
y_true = rng.normal(10.0, 2.0, size=60)
predictions_per_model = [
    y_true + rng.normal(0.0, 0.5, size=60),
    y_true + rng.normal(0.0, 0.8, size=60),
]

ax = multi_model_pred_vs_actual_overlay_static(
    y_true, predictions_per_model, ["OLS", "Ridge"]
)
plt.show()
''',
    "dataviz.regression.comparison.multi_model_pred_vs_actual_overlay_interactive": '''import numpy as np
from dataviz.regression.comparison import multi_model_pred_vs_actual_overlay_interactive

rng = np.random.default_rng(42)
y_true = rng.normal(10.0, 2.0, size=60)
predictions_per_model = [
    y_true + rng.normal(0.0, 0.5, size=60),
    y_true + rng.normal(0.0, 0.8, size=60),
]

fig = multi_model_pred_vs_actual_overlay_interactive(
    y_true, predictions_per_model, ["OLS", "Ridge"]
)
fig.show()
''',
    "dataviz.regression.comparison.residual_density_overlay_multi_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.comparison import residual_density_overlay_multi_static

rng = np.random.default_rng(42)
residuals_per_model = [
    rng.normal(0.0, 0.5, size=60),
    rng.normal(0.0, 0.8, size=60),
]

ax = residual_density_overlay_multi_static(residuals_per_model, ["OLS", "Ridge"])
plt.show()
''',
    "dataviz.regression.comparison.residual_density_overlay_multi_interactive": '''import numpy as np
from dataviz.regression.comparison import residual_density_overlay_multi_interactive

rng = np.random.default_rng(42)
residuals_per_model = [
    rng.normal(0.0, 0.5, size=60),
    rng.normal(0.0, 0.8, size=60),
]

fig = residual_density_overlay_multi_interactive(residuals_per_model, ["OLS", "Ridge"])
fig.show()
''',
    "dataviz.regression.comparison.error_ecdf_overlay_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.comparison import error_ecdf_overlay_static

rng = np.random.default_rng(42)
errors_per_model = [
    np.abs(rng.normal(0.0, 0.5, size=60)),
    np.abs(rng.normal(0.0, 0.8, size=60)),
]

ax = error_ecdf_overlay_static(errors_per_model, ["OLS", "Ridge"])
plt.show()
''',
    "dataviz.regression.comparison.error_ecdf_overlay_interactive": '''import numpy as np
from dataviz.regression.comparison import error_ecdf_overlay_interactive

rng = np.random.default_rng(42)
errors_per_model = [
    np.abs(rng.normal(0.0, 0.5, size=60)),
    np.abs(rng.normal(0.0, 0.8, size=60)),
]

fig = error_ecdf_overlay_interactive(errors_per_model, ["OLS", "Ridge"])
fig.show()
''',
    "dataviz.regression.comparison.model_winner_heatmap_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.comparison import model_winner_heatmap_static

win_matrix = np.array([[3, 1], [1, 3]])

ax = model_winner_heatmap_static(["OLS", "Ridge"], ["MAE", "RMSE"], win_matrix)
plt.show()
''',
    "dataviz.regression.comparison.model_winner_heatmap_interactive": '''import numpy as np
from dataviz.regression.comparison import model_winner_heatmap_interactive

win_matrix = np.array([[3, 1], [1, 3]])

fig = model_winner_heatmap_interactive(["OLS", "Ridge"], ["MAE", "RMSE"], win_matrix)
fig.show()
''',
    "dataviz.regression.cv_extended.cv_residual_distribution_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.cv_extended import cv_residual_distribution_static

rng = np.random.default_rng(42)
fold_labels = ["Fold 1", "Fold 2", "Fold 3", "Fold 4", "Fold 5"]
residuals_per_fold = [rng.normal(0.0, 0.5 + 0.1 * i, size=20) for i in range(5)]

ax = cv_residual_distribution_static(fold_labels, residuals_per_fold)
plt.show()
''',
    "dataviz.regression.cv_extended.cv_residual_distribution_interactive": '''import numpy as np
from dataviz.regression.cv_extended import cv_residual_distribution_interactive

rng = np.random.default_rng(42)
fold_labels = ["Fold 1", "Fold 2", "Fold 3", "Fold 4", "Fold 5"]
residuals_per_fold = [rng.normal(0.0, 0.5 + 0.1 * i, size=20) for i in range(5)]

fig = cv_residual_distribution_interactive(fold_labels, residuals_per_fold)
fig.show()
''',
    "dataviz.regression.cv_extended.repeated_kfold_violin_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.cv_extended import repeated_kfold_violin_static

rng = np.random.default_rng(42)
repeats = ["Repeat 1", "Repeat 2", "Repeat 3", "Repeat 4"]
scores_per_repeat = [rng.normal(0.8, 0.05, size=5) for _ in range(4)]

ax = repeated_kfold_violin_static(repeats, scores_per_repeat, metric_name="R2")
plt.show()
''',
    "dataviz.regression.cv_extended.repeated_kfold_violin_interactive": '''import numpy as np
from dataviz.regression.cv_extended import repeated_kfold_violin_interactive

rng = np.random.default_rng(42)
repeats = ["Repeat 1", "Repeat 2", "Repeat 3", "Repeat 4"]
scores_per_repeat = [rng.normal(0.8, 0.05, size=5) for _ in range(4)]

fig = repeated_kfold_violin_interactive(repeats, scores_per_repeat, metric_name="R2")
fig.show()
''',
    "dataviz.regression.diagnostics_panel.regression_diagnostic_panel_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.diagnostics_panel import regression_diagnostic_panel_static

rng = np.random.default_rng(42)
X = rng.normal(0.0, 1.0, size=(60, 3))
y_true = rng.normal(10.0, 2.0, size=60)
y_pred = y_true + rng.normal(0.0, 0.5, size=60)

result = regression_diagnostic_panel_static(X, y_true, y_pred)
plt.show()
''',
    "dataviz.regression.diagnostics_panel.regression_diagnostic_panel_interactive": '''import numpy as np
from dataviz.regression.diagnostics_panel import regression_diagnostic_panel_interactive

rng = np.random.default_rng(42)
X = rng.normal(0.0, 1.0, size=(60, 3))
y_true = rng.normal(10.0, 2.0, size=60)
y_pred = y_true + rng.normal(0.0, 0.5, size=60)

fig = regression_diagnostic_panel_interactive(X, y_true, y_pred)
fig.show()
''',
    "dataviz.regression.domain.demand_forecast_fan_chart_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.domain import demand_forecast_fan_chart_static

rng = np.random.default_rng(42)
time = np.arange(24)
central = 100 + 2 * time + rng.normal(0.0, 1.0, size=24)
quantile_bands = [(central - 5, central + 5), (central - 10, central + 10)]

ax = demand_forecast_fan_chart_static(time, central, quantile_bands)
plt.show()
''',
    "dataviz.regression.domain.demand_forecast_fan_chart_interactive": '''import numpy as np
from dataviz.regression.domain import demand_forecast_fan_chart_interactive

rng = np.random.default_rng(42)
time = np.arange(24)
central = 100 + 2 * time + rng.normal(0.0, 1.0, size=24)
quantile_bands = [(central - 5, central + 5), (central - 10, central + 10)]

fig = demand_forecast_fan_chart_interactive(time, central, quantile_bands)
fig.show()
''',
    "dataviz.regression.domain.yield_curve_fit_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.domain import yield_curve_fit_plot_static

rng = np.random.default_rng(42)
maturities = np.array([0.25, 0.5, 1.0, 2.0, 5.0, 10.0, 30.0])
observed_yields = np.array([1.8, 2.0, 2.3, 2.6, 3.0, 3.2, 3.4])
fitted_yields = observed_yields + rng.normal(0.0, 0.03, size=7)

ax = yield_curve_fit_plot_static(maturities, observed_yields, fitted_yields)
plt.show()
''',
    "dataviz.regression.domain.yield_curve_fit_plot_interactive": '''import numpy as np
from dataviz.regression.domain import yield_curve_fit_plot_interactive

rng = np.random.default_rng(42)
maturities = np.array([0.25, 0.5, 1.0, 2.0, 5.0, 10.0, 30.0])
observed_yields = np.array([1.8, 2.0, 2.3, 2.6, 3.0, 3.2, 3.4])
fitted_yields = observed_yields + rng.normal(0.0, 0.03, size=7)

fig = yield_curve_fit_plot_interactive(maturities, observed_yields, fitted_yields)
fig.show()
''',
    "dataviz.regression.effects.ice_plot_regression_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.effects import ice_plot_regression_static

rng = np.random.default_rng(42)
grid = np.linspace(0.0, 1.0, 20)
ice_matrix = np.stack(
    [grid**2 + rng.normal(0.0, 0.05, size=20) for _ in range(10)]
)

ax = ice_plot_regression_static(grid, ice_matrix, feature_name="x1")
plt.show()
''',
    "dataviz.regression.effects.ice_plot_regression_interactive": '''import numpy as np
from dataviz.regression.effects import ice_plot_regression_interactive

rng = np.random.default_rng(42)
grid = np.linspace(0.0, 1.0, 20)
ice_matrix = np.stack(
    [grid**2 + rng.normal(0.0, 0.05, size=20) for _ in range(10)]
)

fig = ice_plot_regression_interactive(grid, ice_matrix, feature_name="x1")
fig.show()
''',
    "dataviz.regression.effects.interaction_effect_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.effects import interaction_effect_plot_static

x_grid = np.linspace(0.0, 1.0, 20)
curves = [x_grid**2, np.sqrt(x_grid), x_grid]

ax = interaction_effect_plot_static(
    x_grid, curves, ["low", "mid", "high"], feature_name="x1"
)
plt.show()
''',
    "dataviz.regression.effects.interaction_effect_plot_interactive": '''import numpy as np
from dataviz.regression.effects import interaction_effect_plot_interactive

x_grid = np.linspace(0.0, 1.0, 20)
curves = [x_grid**2, np.sqrt(x_grid), x_grid]

fig = interaction_effect_plot_interactive(
    x_grid, curves, ["low", "mid", "high"], feature_name="x1"
)
fig.show()
''',
    "dataviz.regression.errors_loss.loss_distribution_violin_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.errors_loss import loss_distribution_violin_static

rng = np.random.default_rng(42)
losses_per_model = [
    np.abs(rng.normal(0.0, 0.5, size=60)),
    np.abs(rng.normal(0.0, 0.8, size=60)),
]

ax = loss_distribution_violin_static(["OLS", "Ridge"], losses_per_model, metric_name="MAE")
plt.show()
''',
    "dataviz.regression.errors_loss.loss_distribution_violin_interactive": '''import numpy as np
from dataviz.regression.errors_loss import loss_distribution_violin_interactive

rng = np.random.default_rng(42)
losses_per_model = [
    np.abs(rng.normal(0.0, 0.5, size=60)),
    np.abs(rng.normal(0.0, 0.8, size=60)),
]

fig = loss_distribution_violin_interactive(["OLS", "Ridge"], losses_per_model, metric_name="MAE")
fig.show()
''',
    "dataviz.regression.errors_loss.ranked_error_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.errors_loss import ranked_error_plot_static

rng = np.random.default_rng(42)
errors = np.abs(rng.normal(0.0, 0.7, size=60))

ax = ranked_error_plot_static(errors)
plt.show()
''',
    "dataviz.regression.errors_loss.ranked_error_plot_interactive": '''import numpy as np
from dataviz.regression.errors_loss import ranked_error_plot_interactive

rng = np.random.default_rng(42)
errors = np.abs(rng.normal(0.0, 0.7, size=60))

fig = ranked_error_plot_interactive(errors)
fig.show()
''',
    "dataviz.regression.forecast.forecast_vs_actual_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.forecast import forecast_vs_actual_static

rng = np.random.default_rng(42)
time = np.arange(60)
y_true = 10 + 0.1 * time + rng.normal(0.0, 1.0, size=60)
y_pred = y_true + rng.normal(0.0, 0.5, size=60)

ax = forecast_vs_actual_static(time, y_true, y_pred)
plt.show()
''',
    "dataviz.regression.forecast.forecast_vs_actual_interactive": '''import numpy as np
from dataviz.regression.forecast import forecast_vs_actual_interactive

rng = np.random.default_rng(42)
time = np.arange(60)
y_true = 10 + 0.1 * time + rng.normal(0.0, 1.0, size=60)
y_pred = y_true + rng.normal(0.0, 0.5, size=60)

fig = forecast_vs_actual_interactive(time, y_true, y_pred)
fig.show()
''',
    "dataviz.regression.forecast.backtest_error_distribution_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.forecast import backtest_error_distribution_static

rng = np.random.default_rng(42)
errors = rng.normal(0.0, 0.7, size=120)

ax = backtest_error_distribution_static(errors)
plt.show()
''',
    "dataviz.regression.forecast.backtest_error_distribution_interactive": '''import numpy as np
from dataviz.regression.forecast import backtest_error_distribution_interactive

rng = np.random.default_rng(42)
errors = rng.normal(0.0, 0.7, size=120)

fig = backtest_error_distribution_interactive(errors)
fig.show()
''',
    "dataviz.regression.forecast.forecast_band_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.forecast import forecast_band_plot_static

rng = np.random.default_rng(42)
time = np.arange(60)
y_true = 10 + 0.1 * time + rng.normal(0.0, 1.0, size=60)
y_pred = y_true + rng.normal(0.0, 0.5, size=60)
lower = y_pred - 1.0
upper = y_pred + 1.0

ax = forecast_band_plot_static(time, y_true, y_pred, lower, upper)
plt.show()
''',
    "dataviz.regression.forecast.forecast_band_plot_interactive": '''import numpy as np
from dataviz.regression.forecast import forecast_band_plot_interactive

rng = np.random.default_rng(42)
time = np.arange(60)
y_true = 10 + 0.1 * time + rng.normal(0.0, 1.0, size=60)
y_pred = y_true + rng.normal(0.0, 0.5, size=60)
lower = y_pred - 1.0
upper = y_pred + 1.0

fig = forecast_band_plot_interactive(time, y_true, y_pred, lower, upper)
fig.show()
''',
    "dataviz.regression.glm.variance_function_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.glm import variance_function_plot_static

mu = np.linspace(0.5, 5.0, 50)

ax = variance_function_plot_static(mu, family="poisson")
plt.show()
''',
    "dataviz.regression.glm.variance_function_plot_interactive": '''import numpy as np
from dataviz.regression.glm import variance_function_plot_interactive

mu = np.linspace(0.5, 5.0, 50)

fig = variance_function_plot_interactive(mu, family="poisson")
fig.show()
''',
    "dataviz.regression.gof.normality_test_panel_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.gof import normality_test_panel_static

rng = np.random.default_rng(42)
residuals = rng.normal(0.0, 1.0, size=80)

result = normality_test_panel_static(residuals)
plt.show()
''',
    "dataviz.regression.gof.normality_test_panel_interactive": '''import numpy as np
from dataviz.regression.gof import normality_test_panel_interactive

rng = np.random.default_rng(42)
residuals = rng.normal(0.0, 1.0, size=80)

fig = normality_test_panel_interactive(residuals)
fig.show()
''',
    "dataviz.regression.gof.durbin_watson_gauge_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.gof import durbin_watson_gauge_static

rng = np.random.default_rng(42)
residuals = rng.normal(0.0, 1.0, size=80)

ax = durbin_watson_gauge_static(residuals)
plt.show()
''',
    "dataviz.regression.gof.durbin_watson_gauge_interactive": '''import numpy as np
from dataviz.regression.gof import durbin_watson_gauge_interactive

rng = np.random.default_rng(42)
residuals = rng.normal(0.0, 1.0, size=80)

fig = durbin_watson_gauge_interactive(residuals)
fig.show()
''',
    "dataviz.regression.gof.ljung_box_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.gof import ljung_box_plot_static

rng = np.random.default_rng(42)
residuals = rng.normal(0.0, 1.0, size=80)

ax = ljung_box_plot_static(residuals, lags=10)
plt.show()
''',
    "dataviz.regression.gof.ljung_box_plot_interactive": '''import numpy as np
from dataviz.regression.gof import ljung_box_plot_interactive

rng = np.random.default_rng(42)
residuals = rng.normal(0.0, 1.0, size=80)

fig = ljung_box_plot_interactive(residuals, lags=10)
fig.show()
''',
    "dataviz.regression.gof.residual_dependence_test_panel_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.gof import residual_dependence_test_panel_static

rng = np.random.default_rng(42)
X = rng.normal(0.0, 1.0, size=(60, 3))
residuals = rng.normal(0.0, 1.0, size=60)

result = residual_dependence_test_panel_static(X, residuals)
plt.show()
''',
    "dataviz.regression.gof.residual_dependence_test_panel_interactive": '''import numpy as np
from dataviz.regression.gof import residual_dependence_test_panel_interactive

rng = np.random.default_rng(42)
X = rng.normal(0.0, 1.0, size=(60, 3))
residuals = rng.normal(0.0, 1.0, size=60)

fig = residual_dependence_test_panel_interactive(X, residuals)
fig.show()
''',
    "dataviz.regression.helpers.influence_statistics": '''import numpy as np
from dataviz.regression.helpers import influence_statistics

rng = np.random.default_rng(42)
X = rng.normal(0.0, 1.0, size=(50, 3))
y_true = rng.normal(10.0, 2.0, size=50)
y_pred = y_true + rng.normal(0.0, 0.5, size=50)

result = influence_statistics(X, y_true, y_pred)
print(result)
''',
    "dataviz.regression.helpers.autocorrelation": '''import numpy as np
from dataviz.regression.helpers import autocorrelation

rng = np.random.default_rng(42)
residuals = rng.normal(0.0, 1.0, size=50)

result = autocorrelation(residuals, max_lag=10)
print(result)
''',
    "dataviz.regression.helpers.partial_autocorrelation": '''import numpy as np
from dataviz.regression.helpers import partial_autocorrelation

rng = np.random.default_rng(42)
residuals = rng.normal(0.0, 1.0, size=50)

result = partial_autocorrelation(residuals, max_lag=10)
print(result)
''',
    "dataviz.regression.helpers.runs_test_signs": '''import numpy as np
from dataviz.regression.helpers import runs_test_signs

rng = np.random.default_rng(42)
residuals = rng.normal(0.0, 1.0, size=50)

result = runs_test_signs(residuals)
print(result)
''',
    "dataviz.regression.helpers.variance_inflation_factors": '''import numpy as np
from dataviz.regression.helpers import variance_inflation_factors

rng = np.random.default_rng(42)
X = rng.normal(0.0, 1.0, size=(50, 3))

result = variance_inflation_factors(X)
print(result)
''',
    "dataviz.regression.helpers.ljung_box_statistic": '''import numpy as np
from dataviz.regression.helpers import ljung_box_statistic

rng = np.random.default_rng(42)
residuals = rng.normal(0.0, 1.0, size=50)

result = ljung_box_statistic(residuals, lags=10)
print(result)
''',
    "dataviz.regression.helpers.jarque_bera_statistic": '''import numpy as np
from dataviz.regression.helpers import jarque_bera_statistic

rng = np.random.default_rng(42)
residuals = rng.normal(0.0, 1.0, size=50)

result = jarque_bera_statistic(residuals)
print(result)
''',
    "dataviz.regression.helpers.durbin_watson_statistic": '''import numpy as np
from dataviz.regression.helpers import durbin_watson_statistic

rng = np.random.default_rng(42)
residuals = rng.normal(0.0, 1.0, size=50)

result = durbin_watson_statistic(residuals)
print(result)
''',
    "dataviz.regression.helpers.conformal_quantile": '''import numpy as np
from dataviz.regression.helpers import conformal_quantile

rng = np.random.default_rng(42)
residuals_calibration = rng.normal(0.0, 1.0, size=50)

result = conformal_quantile(residuals_calibration, alpha=0.1)
print(result)
''',
    "dataviz.regression.helpers.jackknife_plus_intervals": '''import numpy as np
from dataviz.regression.helpers import jackknife_plus_intervals

rng = np.random.default_rng(42)
leave_one_out_predictions = rng.normal(5.0, 1.0, size=(50, 10))
y_calibration = rng.normal(5.0, 1.0, size=50)
new_predictions = rng.normal(5.0, 1.0, size=10)

result = jackknife_plus_intervals(
    leave_one_out_predictions, y_calibration, new_predictions, alpha=0.1
)
print(result)
''',
    "dataviz.regression.influence.leverage_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.influence import leverage_plot_static

rng = np.random.default_rng(42)
X = rng.normal(0.0, 1.0, size=(60, 3))
y_true = rng.normal(10.0, 2.0, size=60)
y_pred = y_true + rng.normal(0.0, 0.5, size=60)

ax = leverage_plot_static(X, y_true, y_pred)
plt.show()
''',
    "dataviz.regression.influence.leverage_plot_interactive": '''import numpy as np
from dataviz.regression.influence import leverage_plot_interactive

rng = np.random.default_rng(42)
X = rng.normal(0.0, 1.0, size=(60, 3))
y_true = rng.normal(10.0, 2.0, size=60)
y_pred = y_true + rng.normal(0.0, 0.5, size=60)

fig = leverage_plot_interactive(X, y_true, y_pred)
fig.show()
''',
    "dataviz.regression.influence.cooks_distance_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.influence import cooks_distance_plot_static

rng = np.random.default_rng(42)
X = rng.normal(0.0, 1.0, size=(60, 3))
y_true = rng.normal(10.0, 2.0, size=60)
y_pred = y_true + rng.normal(0.0, 0.5, size=60)

ax = cooks_distance_plot_static(X, y_true, y_pred)
plt.show()
''',
    "dataviz.regression.influence.cooks_distance_plot_interactive": '''import numpy as np
from dataviz.regression.influence import cooks_distance_plot_interactive

rng = np.random.default_rng(42)
X = rng.normal(0.0, 1.0, size=(60, 3))
y_true = rng.normal(10.0, 2.0, size=60)
y_pred = y_true + rng.normal(0.0, 0.5, size=60)

fig = cooks_distance_plot_interactive(X, y_true, y_pred)
fig.show()
''',
    "dataviz.regression.influence.influence_bubble_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.influence import influence_bubble_plot_static

rng = np.random.default_rng(42)
X = rng.normal(0.0, 1.0, size=(60, 3))
y_true = rng.normal(10.0, 2.0, size=60)
y_pred = y_true + rng.normal(0.0, 0.5, size=60)

ax = influence_bubble_plot_static(X, y_true, y_pred)
plt.show()
''',
    "dataviz.regression.influence.influence_bubble_plot_interactive": '''import numpy as np
from dataviz.regression.influence import influence_bubble_plot_interactive

rng = np.random.default_rng(42)
X = rng.normal(0.0, 1.0, size=(60, 3))
y_true = rng.normal(10.0, 2.0, size=60)
y_pred = y_true + rng.normal(0.0, 0.5, size=60)

fig = influence_bubble_plot_interactive(X, y_true, y_pred)
fig.show()
''',
    "dataviz.regression.influence.dfbetas_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.influence import dfbetas_plot_static

rng = np.random.default_rng(42)
X = rng.normal(0.0, 1.0, size=(60, 3))
y_true = rng.normal(10.0, 2.0, size=60)
y_pred = y_true + rng.normal(0.0, 0.5, size=60)

ax = dfbetas_plot_static(X, y_true, y_pred, feature_names=["x1", "x2", "x3"])
plt.show()
''',
    "dataviz.regression.influence.dfbetas_plot_interactive": '''import numpy as np
from dataviz.regression.influence import dfbetas_plot_interactive

rng = np.random.default_rng(42)
X = rng.normal(0.0, 1.0, size=(60, 3))
y_true = rng.normal(10.0, 2.0, size=60)
y_pred = y_true + rng.normal(0.0, 0.5, size=60)

fig = dfbetas_plot_interactive(X, y_true, y_pred, feature_names=["x1", "x2", "x3"])
fig.show()
''',
    "dataviz.regression.metrics.metric_comparison_bar_static": '''import matplotlib.pyplot as plt
from dataviz.regression.metrics import metric_comparison_bar_static

model_metrics = {
    "OLS": {"mae": 0.40, "rmse": 0.55, "r2": 0.93},
    "Ridge": {"mae": 0.42, "rmse": 0.57, "r2": 0.92},
}

ax = metric_comparison_bar_static(model_metrics)
plt.show()
''',
    "dataviz.regression.metrics.metric_comparison_bar_interactive": '''from dataviz.regression.metrics import metric_comparison_bar_interactive

model_metrics = {
    "OLS": {"mae": 0.40, "rmse": 0.55, "r2": 0.93},
    "Ridge": {"mae": 0.42, "rmse": 0.57, "r2": 0.92},
}

fig = metric_comparison_bar_interactive(model_metrics)
fig.show()
''',
    "dataviz.regression.metrics.metric_radar_static": '''import matplotlib.pyplot as plt
from dataviz.regression.metrics import metric_radar_static

model_metrics = {
    "OLS": {"mae": 0.40, "rmse": 0.55, "medae": 0.30, "r2": 0.93,
            "explained_variance": 0.94},
    "Ridge": {"mae": 0.42, "rmse": 0.57, "medae": 0.33, "r2": 0.92,
              "explained_variance": 0.93},
}

ax = metric_radar_static(model_metrics)
plt.show()
''',
    "dataviz.regression.metrics.metric_radar_interactive": '''from dataviz.regression.metrics import metric_radar_interactive

model_metrics = {
    "OLS": {"mae": 0.40, "rmse": 0.55, "medae": 0.30, "r2": 0.93,
            "explained_variance": 0.94},
    "Ridge": {"mae": 0.42, "rmse": 0.57, "medae": 0.33, "r2": 0.92,
              "explained_variance": 0.93},
}

fig = metric_radar_interactive(model_metrics)
fig.show()
''',
    "dataviz.regression.metrics.per_segment_metrics_heatmap_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.metrics import per_segment_metrics_heatmap_static

rng = np.random.default_rng(42)
y_true = rng.normal(10.0, 2.0, size=60)
y_pred = y_true + rng.normal(0.0, 0.5, size=60)
segments = rng.choice(["A", "B", "C"], size=60)

ax = per_segment_metrics_heatmap_static(y_true, y_pred, segments)
plt.show()
''',
    "dataviz.regression.metrics.per_segment_metrics_heatmap_interactive": '''import numpy as np
from dataviz.regression.metrics import per_segment_metrics_heatmap_interactive

rng = np.random.default_rng(42)
y_true = rng.normal(10.0, 2.0, size=60)
y_pred = y_true + rng.normal(0.0, 0.5, size=60)
segments = rng.choice(["A", "B", "C"], size=60)

fig = per_segment_metrics_heatmap_interactive(y_true, y_pred, segments)
fig.show()
''',
    "dataviz.regression.mixed_effects.group_means_vs_predicted_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.mixed_effects import group_means_vs_predicted_static

group_labels = ["G1", "G2", "G3", "G4"]
group_observed_means = np.array([9.5, 10.2, 10.8, 9.9])
group_predicted_means = group_observed_means + np.array([0.1, -0.2, 0.15, -0.05])

ax = group_means_vs_predicted_static(
    group_labels, group_observed_means, group_predicted_means
)
plt.show()
''',
    "dataviz.regression.mixed_effects.group_means_vs_predicted_interactive": '''import numpy as np
from dataviz.regression.mixed_effects import group_means_vs_predicted_interactive

group_labels = ["G1", "G2", "G3", "G4"]
group_observed_means = np.array([9.5, 10.2, 10.8, 9.9])
group_predicted_means = group_observed_means + np.array([0.1, -0.2, 0.15, -0.05])

fig = group_means_vs_predicted_interactive(
    group_labels, group_observed_means, group_predicted_means
)
fig.show()
''',
    "dataviz.regression.multicollinearity.condition_index_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.multicollinearity import condition_index_plot_static

rng = np.random.default_rng(42)
x1 = rng.normal(0.0, 1.0, size=60)
X = np.column_stack([x1, 0.9 * x1 + rng.normal(0.0, 0.1, size=60), rng.normal(0.0, 1.0, size=60)])

ax = condition_index_plot_static(X)
plt.show()
''',
    "dataviz.regression.multicollinearity.condition_index_plot_interactive": '''import numpy as np
from dataviz.regression.multicollinearity import condition_index_plot_interactive

rng = np.random.default_rng(42)
x1 = rng.normal(0.0, 1.0, size=60)
X = np.column_stack([x1, 0.9 * x1 + rng.normal(0.0, 0.1, size=60), rng.normal(0.0, 1.0, size=60)])

fig = condition_index_plot_interactive(X)
fig.show()
''',
    "dataviz.regression.multicollinearity.correlation_heatmap_with_clustering_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.multicollinearity import correlation_heatmap_with_clustering_static

rng = np.random.default_rng(42)
x1 = rng.normal(0.0, 1.0, size=60)
X = np.column_stack([x1, 0.9 * x1 + rng.normal(0.0, 0.1, size=60), rng.normal(0.0, 1.0, size=60)])

ax = correlation_heatmap_with_clustering_static(X, feature_names=["x1", "x2", "x3"])
plt.show()
''',
    "dataviz.regression.multicollinearity.correlation_heatmap_with_clustering_interactive": '''import numpy as np
from dataviz.regression.multicollinearity import correlation_heatmap_with_clustering_interactive

rng = np.random.default_rng(42)
x1 = rng.normal(0.0, 1.0, size=60)
X = np.column_stack([x1, 0.9 * x1 + rng.normal(0.0, 0.1, size=60), rng.normal(0.0, 1.0, size=60)])

fig = correlation_heatmap_with_clustering_interactive(X, feature_names=["x1", "x2", "x3"])
fig.show()
''',
    "dataviz.regression.multicollinearity.eigenvalue_scree_predictors_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.multicollinearity import eigenvalue_scree_predictors_static

rng = np.random.default_rng(42)
x1 = rng.normal(0.0, 1.0, size=60)
X = np.column_stack([x1, 0.9 * x1 + rng.normal(0.0, 0.1, size=60), rng.normal(0.0, 1.0, size=60)])

ax = eigenvalue_scree_predictors_static(X)
plt.show()
''',
    "dataviz.regression.multicollinearity.eigenvalue_scree_predictors_interactive": '''import numpy as np
from dataviz.regression.multicollinearity import eigenvalue_scree_predictors_interactive

rng = np.random.default_rng(42)
x1 = rng.normal(0.0, 1.0, size=60)
X = np.column_stack([x1, 0.9 * x1 + rng.normal(0.0, 0.1, size=60), rng.normal(0.0, 1.0, size=60)])

fig = eigenvalue_scree_predictors_interactive(X)
fig.show()
''',
    "dataviz.regression.quantile.quantile_regression_band_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.quantile import quantile_regression_band_static

rng = np.random.default_rng(42)
x = np.linspace(0.0, 10.0, 60)
y = 2 * x + rng.normal(0.0, 1.0, size=60)
y_low = 2 * x - 1.5
y_med = 2 * x
y_high = 2 * x + 1.5

ax = quantile_regression_band_static(x, y, y_low, y_med, y_high)
plt.show()
''',
    "dataviz.regression.quantile.quantile_regression_band_interactive": '''import numpy as np
from dataviz.regression.quantile import quantile_regression_band_interactive

rng = np.random.default_rng(42)
x = np.linspace(0.0, 10.0, 60)
y = 2 * x + rng.normal(0.0, 1.0, size=60)
y_low = 2 * x - 1.5
y_med = 2 * x
y_high = 2 * x + 1.5

fig = quantile_regression_band_interactive(x, y, y_low, y_med, y_high)
fig.show()
''',
    "dataviz.regression.quantile.huber_vs_ols_overlay_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.quantile import huber_vs_ols_overlay_static

rng = np.random.default_rng(42)
x = np.linspace(0.0, 10.0, 60)
y = 2 * x + rng.normal(0.0, 1.0, size=60)
y_ols = 2 * x + 0.1
y_huber = 2 * x - 0.05

ax = huber_vs_ols_overlay_static(x, y, y_ols, y_huber)
plt.show()
''',
    "dataviz.regression.quantile.huber_vs_ols_overlay_interactive": '''import numpy as np
from dataviz.regression.quantile import huber_vs_ols_overlay_interactive

rng = np.random.default_rng(42)
x = np.linspace(0.0, 10.0, 60)
y = 2 * x + rng.normal(0.0, 1.0, size=60)
y_ols = 2 * x + 0.1
y_huber = 2 * x - 0.05

fig = huber_vs_ols_overlay_interactive(x, y, y_ols, y_huber)
fig.show()
''',
    "dataviz.regression.quantile.weighted_residual_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.quantile import weighted_residual_plot_static

rng = np.random.default_rng(42)
y_pred = rng.normal(10.0, 2.0, size=60)
residuals = rng.normal(0.0, 0.7, size=60)
weights = rng.uniform(0.5, 1.5, size=60)

ax = weighted_residual_plot_static(y_pred, residuals, weights)
plt.show()
''',
    "dataviz.regression.quantile.weighted_residual_plot_interactive": '''import numpy as np
from dataviz.regression.quantile import weighted_residual_plot_interactive

rng = np.random.default_rng(42)
y_pred = rng.normal(10.0, 2.0, size=60)
residuals = rng.normal(0.0, 0.7, size=60)
weights = rng.uniform(0.5, 1.5, size=60)

fig = weighted_residual_plot_interactive(y_pred, residuals, weights)
fig.show()
''',
    "dataviz.regression.regularization.regularization_validation_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.regularization import regularization_validation_plot_static

alphas = np.logspace(-3, 2, 20)
train_scores = 0.95 - 0.02 * np.log10(alphas + 1e-3)
test_scores = train_scores - 0.05 - 0.01 * np.abs(np.log10(alphas))

ax = regularization_validation_plot_static(alphas, train_scores, test_scores, score_name="R2")
plt.show()
''',
    "dataviz.regression.regularization.regularization_validation_plot_interactive": '''import numpy as np
from dataviz.regression.regularization import regularization_validation_plot_interactive

alphas = np.logspace(-3, 2, 20)
train_scores = 0.95 - 0.02 * np.log10(alphas + 1e-3)
test_scores = train_scores - 0.05 - 0.01 * np.abs(np.log10(alphas))

fig = regularization_validation_plot_interactive(alphas, train_scores, test_scores, score_name="R2")
fig.show()
''',
    "dataviz.regression.residual_extended.residual_boxplot_by_group_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.residual_extended import residual_boxplot_by_group_static

rng = np.random.default_rng(42)
y_true = rng.normal(10.0, 2.0, size=60)
y_pred = y_true + rng.normal(0.0, 0.5, size=60)
groups = rng.choice(["A", "B", "C"], size=60)

ax = residual_boxplot_by_group_static(y_true, y_pred, groups)
plt.show()
''',
    "dataviz.regression.residual_extended.residual_boxplot_by_group_interactive": '''import numpy as np
from dataviz.regression.residual_extended import residual_boxplot_by_group_interactive

rng = np.random.default_rng(42)
y_true = rng.normal(10.0, 2.0, size=60)
y_pred = y_true + rng.normal(0.0, 0.5, size=60)
groups = rng.choice(["A", "B", "C"], size=60)

fig = residual_boxplot_by_group_interactive(y_true, y_pred, groups)
fig.show()
''',
    "dataviz.regression.residual_features.residual_vs_feature_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.residual_features import residual_vs_feature_static

rng = np.random.default_rng(42)
feature = rng.normal(0.0, 1.0, size=60)
y_true = 10 + 2 * feature + rng.normal(0.0, 1.0, size=60)
y_pred = y_true + rng.normal(0.0, 0.5, size=60)

ax = residual_vs_feature_static(feature, y_true, y_pred, feature_name="x1")
plt.show()
''',
    "dataviz.regression.residual_features.residual_vs_feature_interactive": '''import numpy as np
from dataviz.regression.residual_features import residual_vs_feature_interactive

rng = np.random.default_rng(42)
feature = rng.normal(0.0, 1.0, size=60)
y_true = 10 + 2 * feature + rng.normal(0.0, 1.0, size=60)
y_pred = y_true + rng.normal(0.0, 0.5, size=60)

fig = residual_vs_feature_interactive(feature, y_true, y_pred, feature_name="x1")
fig.show()
''',
    "dataviz.regression.residual_features.partial_residual_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.residual_features import partial_residual_plot_static

rng = np.random.default_rng(42)
X = rng.normal(0.0, 1.0, size=(60, 3))
y_true = 10 + X @ np.array([2.0, -1.0, 0.5]) + rng.normal(0.0, 0.5, size=60)

ax = partial_residual_plot_static(X, y_true, feature_index=0, feature_name="x1")
plt.show()
''',
    "dataviz.regression.residual_features.partial_residual_plot_interactive": '''import numpy as np
from dataviz.regression.residual_features import partial_residual_plot_interactive

rng = np.random.default_rng(42)
X = rng.normal(0.0, 1.0, size=(60, 3))
y_true = 10 + X @ np.array([2.0, -1.0, 0.5]) + rng.normal(0.0, 0.5, size=60)

fig = partial_residual_plot_interactive(X, y_true, feature_index=0, feature_name="x1")
fig.show()
''',
    "dataviz.regression.residual_features.ccpr_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.residual_features import ccpr_plot_static

rng = np.random.default_rng(42)
X = rng.normal(0.0, 1.0, size=(60, 3))
y_true = 10 + X @ np.array([2.0, -1.0, 0.5]) + rng.normal(0.0, 0.5, size=60)

ax = ccpr_plot_static(X, y_true, feature_index=0, feature_name="x1")
plt.show()
''',
    "dataviz.regression.residual_features.ccpr_plot_interactive": '''import numpy as np
from dataviz.regression.residual_features import ccpr_plot_interactive

rng = np.random.default_rng(42)
X = rng.normal(0.0, 1.0, size=(60, 3))
y_true = 10 + X @ np.array([2.0, -1.0, 0.5]) + rng.normal(0.0, 0.5, size=60)

fig = ccpr_plot_interactive(X, y_true, feature_index=0, feature_name="x1")
fig.show()
''',
    "dataviz.regression.residual_features.added_variable_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.residual_features import added_variable_plot_static

rng = np.random.default_rng(42)
X = rng.normal(0.0, 1.0, size=(60, 3))
y_true = 10 + X @ np.array([2.0, -1.0, 0.5]) + rng.normal(0.0, 0.5, size=60)

ax = added_variable_plot_static(X, y_true, feature_index=0, feature_name="x1")
plt.show()
''',
    "dataviz.regression.residual_features.added_variable_plot_interactive": '''import numpy as np
from dataviz.regression.residual_features import added_variable_plot_interactive

rng = np.random.default_rng(42)
X = rng.normal(0.0, 1.0, size=(60, 3))
y_true = 10 + X @ np.array([2.0, -1.0, 0.5]) + rng.normal(0.0, 0.5, size=60)

fig = added_variable_plot_interactive(X, y_true, feature_index=0, feature_name="x1")
fig.show()
''',
    "dataviz.regression.selection.aic_bic_bar_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.selection import aic_bic_bar_static

model_names = ["M1", "M2", "M3"]
aic = np.array([120.5, 115.2, 118.7])
bic = np.array([125.5, 119.7, 124.7])

ax = aic_bic_bar_static(model_names, aic, bic)
plt.show()
''',
    "dataviz.regression.selection.aic_bic_bar_interactive": '''import numpy as np
from dataviz.regression.selection import aic_bic_bar_interactive

model_names = ["M1", "M2", "M3"]
aic = np.array([120.5, 115.2, 118.7])
bic = np.array([125.5, 119.7, 124.7])

fig = aic_bic_bar_interactive(model_names, aic, bic)
fig.show()
''',
    "dataviz.regression.spatial.spatial_residual_map_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.spatial import spatial_residual_map_static

rng = np.random.default_rng(42)
longitudes = rng.uniform(-5.0, 5.0, size=60)
latitudes = rng.uniform(40.0, 50.0, size=60)
residuals = rng.normal(0.0, 0.7, size=60)

ax = spatial_residual_map_static(longitudes, latitudes, residuals)
plt.show()
''',
    "dataviz.regression.spatial.spatial_residual_map_interactive": '''import numpy as np
from dataviz.regression.spatial import spatial_residual_map_interactive

rng = np.random.default_rng(42)
longitudes = rng.uniform(-5.0, 5.0, size=60)
latitudes = rng.uniform(40.0, 50.0, size=60)
residuals = rng.normal(0.0, 0.7, size=60)

fig = spatial_residual_map_interactive(longitudes, latitudes, residuals)
fig.show()
''',
    "dataviz.regression.survival.km_predicted_vs_observed_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.survival import km_predicted_vs_observed_static

times = np.linspace(0.0, 24.0, 25)
km_observed = np.exp(-times / 18.0)
km_predicted = np.exp(-times / 20.0)

ax = km_predicted_vs_observed_static(times, km_observed, km_predicted)
plt.show()
''',
    "dataviz.regression.survival.km_predicted_vs_observed_interactive": '''import numpy as np
from dataviz.regression.survival import km_predicted_vs_observed_interactive

times = np.linspace(0.0, 24.0, 25)
km_observed = np.exp(-times / 18.0)
km_predicted = np.exp(-times / 20.0)

fig = km_predicted_vs_observed_interactive(times, km_observed, km_predicted)
fig.show()
''',
    "dataviz.regression.transforms.power_transform_residual_panel_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.transforms import power_transform_residual_panel_static

rng = np.random.default_rng(42)
y_pred = rng.normal(10.0, 2.0, size=60)
residuals_orig = rng.normal(0.0, 1.2, size=60)
residuals_log = residuals_orig * 0.6
residuals_sqrt = residuals_orig * 0.8

result = power_transform_residual_panel_static(
    y_pred, residuals_orig, residuals_log, residuals_sqrt
)
plt.show()
''',
    "dataviz.regression.transforms.power_transform_residual_panel_interactive": '''import numpy as np
from dataviz.regression.transforms import power_transform_residual_panel_interactive

rng = np.random.default_rng(42)
y_pred = rng.normal(10.0, 2.0, size=60)
residuals_orig = rng.normal(0.0, 1.2, size=60)
residuals_log = residuals_orig * 0.6
residuals_sqrt = residuals_orig * 0.8

fig = power_transform_residual_panel_interactive(
    y_pred, residuals_orig, residuals_log, residuals_sqrt
)
fig.show()
''',
    "dataviz.regression.uncertainty.conformal_interval_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.uncertainty import conformal_interval_plot_static

rng = np.random.default_rng(42)
y_true = rng.normal(10.0, 2.0, size=60)
y_pred = y_true + rng.normal(0.0, 0.5, size=60)
lower = y_pred - 1.0
upper = y_pred + 1.0

ax = conformal_interval_plot_static(y_true, y_pred, lower, upper)
plt.show()
''',
    "dataviz.regression.uncertainty.conformal_interval_plot_interactive": '''import numpy as np
from dataviz.regression.uncertainty import conformal_interval_plot_interactive

rng = np.random.default_rng(42)
y_true = rng.normal(10.0, 2.0, size=60)
y_pred = y_true + rng.normal(0.0, 0.5, size=60)
lower = y_pred - 1.0
upper = y_pred + 1.0

fig = conformal_interval_plot_interactive(y_true, y_pred, lower, upper)
fig.show()
''',
    "dataviz.regression.uncertainty.jackknife_plus_band_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.uncertainty import jackknife_plus_band_static

rng = np.random.default_rng(42)
y_true = rng.normal(10.0, 2.0, size=60)
y_pred = y_true + rng.normal(0.0, 0.5, size=60)
lower = y_pred - 1.2
upper = y_pred + 1.2

ax = jackknife_plus_band_static(y_true, y_pred, lower, upper)
plt.show()
''',
    "dataviz.regression.uncertainty.jackknife_plus_band_interactive": '''import numpy as np
from dataviz.regression.uncertainty import jackknife_plus_band_interactive

rng = np.random.default_rng(42)
y_true = rng.normal(10.0, 2.0, size=60)
y_pred = y_true + rng.normal(0.0, 0.5, size=60)
lower = y_pred - 1.2
upper = y_pred + 1.2

fig = jackknife_plus_band_interactive(y_true, y_pred, lower, upper)
fig.show()
''',
    "dataviz.regression.validation.validation_curve_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.validation import validation_curve_static

rng = np.random.default_rng(42)
param_values = np.arange(1, 11)
train_scores = np.clip(
    0.90 + 0.01 * param_values[:, None] + rng.normal(0.0, 0.01, size=(10, 5)), 0, 1
)
test_scores = np.clip(
    0.75 + 0.015 * param_values[:, None] - 0.002 * param_values[:, None] ** 2
    + rng.normal(0.0, 0.015, size=(10, 5)),
    0, 1,
)

ax = validation_curve_static(param_values, train_scores, test_scores, param_name="depth")
plt.show()
''',
    "dataviz.regression.validation.validation_curve_interactive": '''import numpy as np
from dataviz.regression.validation import validation_curve_interactive

rng = np.random.default_rng(42)
param_values = np.arange(1, 11)
train_scores = np.clip(
    0.90 + 0.01 * param_values[:, None] + rng.normal(0.0, 0.01, size=(10, 5)), 0, 1
)
test_scores = np.clip(
    0.75 + 0.015 * param_values[:, None] - 0.002 * param_values[:, None] ** 2
    + rng.normal(0.0, 0.015, size=(10, 5)),
    0, 1,
)

fig = validation_curve_interactive(param_values, train_scores, test_scores, param_name="depth")
fig.show()
''',
    "dataviz.regression.validation.training_history_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.validation import training_history_static

epochs = np.linspace(0.0, 2.0, 50)
history = {
    "loss": list(np.exp(-epochs) + 0.10),
    "val_loss": list(np.exp(-0.8 * epochs) + 0.15),
}

ax = training_history_static(history)
plt.show()
''',
    "dataviz.regression.validation.training_history_interactive": '''import numpy as np
from dataviz.regression.validation import training_history_interactive

epochs = np.linspace(0.0, 2.0, 50)
history = {
    "loss": list(np.exp(-epochs) + 0.10),
    "val_loss": list(np.exp(-0.8 * epochs) + 0.15),
}

fig = training_history_interactive(history)
fig.show()
''',
    "dataviz.regression.validation.cv_score_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.validation import cv_score_plot_static

rng = np.random.default_rng(42)
fold_scores = rng.normal(0.85, 0.03, size=10)

ax = cv_score_plot_static(fold_scores, model_name="Ridge")
plt.show()
''',
    "dataviz.regression.validation.cv_score_plot_interactive": '''import numpy as np
from dataviz.regression.validation import cv_score_plot_interactive

rng = np.random.default_rng(42)
fold_scores = rng.normal(0.85, 0.03, size=10)

fig = cv_score_plot_interactive(fold_scores, model_name="Ridge")
fig.show()
''',
    "dataviz.regression.validation.bias_variance_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.validation import bias_variance_plot_static

complexity = np.arange(1, 11)
bias_squared = 0.5 / complexity
variance = 0.002 * complexity**2
noise = np.full(10, 0.05)

ax = bias_variance_plot_static(complexity, bias_squared, variance, noise=noise)
plt.show()
''',
    "dataviz.regression.validation.bias_variance_plot_interactive": '''import numpy as np
from dataviz.regression.validation import bias_variance_plot_interactive

complexity = np.arange(1, 11)
bias_squared = 0.5 / complexity
variance = 0.002 * complexity**2
noise = np.full(10, 0.05)

fig = bias_variance_plot_interactive(complexity, bias_squared, variance, noise=noise)
fig.show()
''',
}
