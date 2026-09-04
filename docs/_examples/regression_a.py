"""Curated rich examples for regression member pages."""

EXAMPLES = {
    # ------------------------------------------------------------------
    # dataviz.regression.autocorrelation
    # ------------------------------------------------------------------
    "dataviz.regression.autocorrelation.residual_acf_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.autocorrelation import residual_acf_static

rng = np.random.default_rng(42)
batch = np.arange(36)
fill = pd.Series(500 + 0.8 * np.sin(batch / 4.0) + rng.normal(0, 1.5, 36),
                 name="fill_volume_ml")
pred = pd.Series(500 + 0.6 * np.sin(batch / 4.0), name="predicted_fill_ml")

ax = residual_acf_static(fill, pred, max_lag=12,
                         title="Bottling Line Fill Model: Residual ACF",
                         color="#2a7f62", theme="minimal")
ax.set_xlabel("Lag (batches)")
plt.show()''',
    "dataviz.regression.autocorrelation.residual_acf_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.autocorrelation import residual_acf_interactive

rng = np.random.default_rng(42)
batch = np.arange(36)
fill = pd.Series(500 + 0.8 * np.sin(batch / 4.0) + rng.normal(0, 1.5, 36),
                 name="fill_volume_ml")
pred = pd.Series(500 + 0.6 * np.sin(batch / 4.0), name="predicted_fill_ml")

fig = residual_acf_interactive(fill, pred, max_lag=12,
                               title="Bottling Line Fill Model: Residual ACF",
                               color="#2a7f62", template="plotly_white")
fig.show()''',
    "dataviz.regression.autocorrelation.residual_pacf_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.autocorrelation import residual_pacf_static

rng = np.random.default_rng(42)
week = np.arange(30)
sales = pd.Series(1200 + 40 * np.sin(week / 2.5) + rng.normal(0, 25, 30),
                  name="weekly_units")
fitted = pd.Series(1200 + 38 * np.sin(week / 2.5), name="fitted_units")

ax = residual_pacf_static(sales, fitted, max_lag=10,
                          title="Weekly Demand Model: Residual PACF",
                          color="#8c5aa8")
plt.show()''',
    "dataviz.regression.autocorrelation.residual_pacf_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.autocorrelation import residual_pacf_interactive

rng = np.random.default_rng(42)
week = np.arange(30)
sales = pd.Series(1200 + 40 * np.sin(week / 2.5) + rng.normal(0, 25, 30),
                  name="weekly_units")
fitted = pd.Series(1200 + 38 * np.sin(week / 2.5), name="fitted_units")

fig = residual_pacf_interactive(sales, fitted, max_lag=10,
                                title="Weekly Demand Model: Residual PACF",
                                color="#8c5aa8", template="plotly_white")
fig.show()''',
    "dataviz.regression.autocorrelation.residual_runs_plot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.autocorrelation import residual_runs_plot_static

rng = np.random.default_rng(42)
run = np.arange(28)
strength = pd.Series(32 + 0.15 * run + rng.normal(0, 0.9, 28),
                     name="tensile_strength_mpa")
fitted = pd.Series(np.full(28, 32.0 + 0.15 * 13.5), name="mean_only_fit")

ax = residual_runs_plot_static(strength, fitted,
                               title="Tensile Strength: Residual Runs Chart",
                               positive_color="#2a7f62",
                               negative_color="#c0392b")
plt.show()''',
    "dataviz.regression.autocorrelation.residual_runs_plot_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.autocorrelation import residual_runs_plot_interactive

rng = np.random.default_rng(42)
run = np.arange(28)
strength = pd.Series(32 + 0.15 * run + rng.normal(0, 0.9, 28),
                     name="tensile_strength_mpa")
fitted = pd.Series(np.full(28, 32.0 + 0.15 * 13.5), name="mean_only_fit")

fig = residual_runs_plot_interactive(strength, fitted,
                                     title="Tensile Strength: Residual Runs Chart",
                                     positive_color="#2a7f62",
                                     negative_color="#c0392b",
                                     template="plotly_white")
fig.show()''',
    "dataviz.regression.autocorrelation.residual_time_plot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.autocorrelation import residual_time_plot_static

rng = np.random.default_rng(42)
days = pd.date_range("2024-01-01", periods=30, freq="D")
load = pd.Series(85 + 6 * np.sin(np.arange(30) / 4.5) + rng.normal(0, 2.0, 30),
                 name="plant_load_mw")
fitted = pd.Series(85 + 6 * np.sin(np.arange(30) / 4.5), name="forecast_mw")

ax = residual_time_plot_static(load, fitted, time=days,
                               title="Energy Load Forecast: Residuals Over Time",
                               color="#b25b16", marker="s")
ax.axhline(2.0, color="#888", linestyle=":", linewidth=1)
plt.show()''',
    "dataviz.regression.autocorrelation.residual_time_plot_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.autocorrelation import residual_time_plot_interactive

rng = np.random.default_rng(42)
days = pd.date_range("2024-01-01", periods=30, freq="D")
load = pd.Series(85 + 6 * np.sin(np.arange(30) / 4.5) + rng.normal(0, 2.0, 30),
                 name="plant_load_mw")
fitted = pd.Series(85 + 6 * np.sin(np.arange(30) / 4.5), name="forecast_mw")

fig = residual_time_plot_interactive(load, fitted, time=days,
                                     title="Energy Load Forecast: Residuals Over Time",
                                     color="#b25b16", template="plotly_white")
fig.show()''',
    # ------------------------------------------------------------------
    # dataviz.regression.bayesian
    # ------------------------------------------------------------------
    "dataviz.regression.bayesian.posterior_coefficient_density_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.bayesian import posterior_coefficient_density_static

rng = np.random.default_rng(42)
samples = [rng.normal(2.1, 0.4, 600),
           rng.normal(-0.7, 0.25, 600),
           rng.normal(0.05, 0.5, 600),
           rng.normal(1.3, 0.3, 600)]
names = ["sqft", "bedrooms", "age_years", "dist_transit_km"]

ax = posterior_coefficient_density_static(
    samples, coef_names=names,
    title="Hedonic Pricing Model: Posterior Coefficient Densities",
    cmap="plasma")
ax.axvline(0.0, color="#444", linestyle=":", linewidth=1)
plt.show()''',
    "dataviz.regression.bayesian.posterior_coefficient_density_interactive": '''import numpy as np
from dataviz.regression.bayesian import posterior_coefficient_density_interactive

rng = np.random.default_rng(42)
samples = [rng.normal(2.1, 0.4, 600),
           rng.normal(-0.7, 0.25, 600),
           rng.normal(0.05, 0.5, 600),
           rng.normal(1.3, 0.3, 600)]
names = ["sqft", "bedrooms", "age_years", "dist_transit_km"]

fig = posterior_coefficient_density_interactive(
    samples, coef_names=names,
    title="Hedonic Pricing Model: Posterior Coefficient Densities",
    template="plotly_white")
fig.show()''',
    "dataviz.regression.bayesian.posterior_predictive_check_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.bayesian import posterior_predictive_check_static

rng = np.random.default_rng(42)
recovery = pd.Series(rng.normal(14.0, 3.0, 40), name="recovery_days")
draws = recovery.to_numpy()[None, :] + rng.normal(0, 1.2, (40, 40))

ax = posterior_predictive_check_static(
    recovery, draws,
    title="Clinical Trial: Posterior Predictive Check (Recovery Days)",
    bins=25, true_color="#c0392b")
ax.set_xlabel("Recovery time (days)")
plt.show()''',
    "dataviz.regression.bayesian.posterior_predictive_check_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.bayesian import posterior_predictive_check_interactive

rng = np.random.default_rng(42)
recovery = pd.Series(rng.normal(14.0, 3.0, 40), name="recovery_days")
draws = recovery.to_numpy()[None, :] + rng.normal(0, 1.2, (40, 40))

fig = posterior_predictive_check_interactive(
    recovery, draws,
    title="Clinical Trial: Posterior Predictive Check (Recovery Days)",
    true_color="#c0392b", template="plotly_white")
fig.show()''',
    "dataviz.regression.bayesian.trace_plot_coefficients_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.bayesian import trace_plot_coefficients_static

rng = np.random.default_rng(42)
iters = np.arange(500)
traces = [1.8 * (1 - np.exp(-iters / 80)) + rng.normal(0, 0.15, 500),
          -0.6 * (1 - np.exp(-iters / 60)) + rng.normal(0, 0.1, 500),
          rng.normal(0.9, 0.2, 500)]
names = ["intercept", "dose_mg", "age_years"]

ax = trace_plot_coefficients_static(traces, coef_names=names,
                                    title="MCMC Traces: Dose-Response Model",
                                    cmap="Dark2")
ax.set_xlabel("Iteration")
plt.show()''',
    "dataviz.regression.bayesian.trace_plot_coefficients_interactive": '''import numpy as np
from dataviz.regression.bayesian import trace_plot_coefficients_interactive

rng = np.random.default_rng(42)
iters = np.arange(500)
traces = [1.8 * (1 - np.exp(-iters / 80)) + rng.normal(0, 0.15, 500),
          -0.6 * (1 - np.exp(-iters / 60)) + rng.normal(0, 0.1, 500),
          rng.normal(0.9, 0.2, 500)]
names = ["intercept", "dose_mg", "age_years"]

fig = trace_plot_coefficients_interactive(traces, coef_names=names,
                                          title="MCMC Traces: Dose-Response Model",
                                          template="plotly_white")
fig.show()''',
    "dataviz.regression.bayesian.credible_interval_forest_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.bayesian import credible_interval_forest_static

names = ["ad_spend", "price_index", "seasonality", "distribution"]
means = np.array([0.42, -1.15, 0.28, 0.66])
lower = means - np.array([0.18, 0.30, 0.22, 0.25])
upper = means + np.array([0.20, 0.28, 0.24, 0.27])

ax = credible_interval_forest_static(
    names, means, lower, upper,
    title="Marketing Mix Model: 94% Credible Intervals",
    color="#2a7f62")
ax.set_xlabel("Effect on weekly sales (log units)")
plt.show()''',
    "dataviz.regression.bayesian.credible_interval_forest_interactive": '''import numpy as np
from dataviz.regression.bayesian import credible_interval_forest_interactive

names = ["ad_spend", "price_index", "seasonality", "distribution"]
means = np.array([0.42, -1.15, 0.28, 0.66])
lower = means - np.array([0.18, 0.30, 0.22, 0.25])
upper = means + np.array([0.20, 0.28, 0.24, 0.27])

fig = credible_interval_forest_interactive(
    names, means, lower, upper,
    title="Marketing Mix Model: 94% Credible Intervals",
    color="#2a7f62", template="plotly_white")
fig.show()''',
    # ------------------------------------------------------------------
    # dataviz.regression.calibration_regression
    # ------------------------------------------------------------------
    "dataviz.regression.calibration_regression.calibration_curve_regression_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.calibration_regression import calibration_curve_regression_static

rng = np.random.default_rng(42)
n = 32
pred_price = pd.Series(rng.uniform(180, 520, n), name="predicted_price_k")
actual_price = pd.Series(pred_price * rng.normal(1.0, 0.08, n),
                         name="actual_price_k")

ax = calibration_curve_regression_static(
    actual_price, pred_price, n_bins=6,
    title="Home Appraisal Model: Calibration Curve",
    color="#1f6fb2")
ax.set_xlabel("Predicted price (bin mean, k USD)")
plt.show()''',
    "dataviz.regression.calibration_regression.calibration_curve_regression_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.calibration_regression import calibration_curve_regression_interactive

rng = np.random.default_rng(42)
n = 32
pred_price = pd.Series(rng.uniform(180, 520, n), name="predicted_price_k")
actual_price = pd.Series(pred_price * rng.normal(1.0, 0.08, n),
                         name="actual_price_k")

fig = calibration_curve_regression_interactive(
    actual_price, pred_price, n_bins=6,
    title="Home Appraisal Model: Calibration Curve",
    color="#1f6fb2", template="plotly_white")
fig.show()''',
    "dataviz.regression.calibration_regression.prediction_interval_coverage_plot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.calibration_regression import prediction_interval_coverage_plot_static

rng = np.random.default_rng(42)
n = 40
forecast = pd.Series(rng.uniform(50, 150, n), name="forecast_demand")
observed = pd.Series(forecast + rng.normal(0, 12, n), name="observed_demand")

ax = prediction_interval_coverage_plot_static(
    observed, forecast,
    levels=(0.5, 0.7, 0.8, 0.9, 0.95), method="empirical",
    title="Spare-Parts Demand: Interval Coverage",
    coverage_color="#2a7f62")
ax.set_ylabel("Empirical coverage")
plt.show()''',
    "dataviz.regression.calibration_regression.prediction_interval_coverage_plot_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.calibration_regression import prediction_interval_coverage_plot_interactive

rng = np.random.default_rng(42)
n = 40
forecast = pd.Series(rng.uniform(50, 150, n), name="forecast_demand")
observed = pd.Series(forecast + rng.normal(0, 12, n), name="observed_demand")

fig = prediction_interval_coverage_plot_interactive(
    observed, forecast,
    levels=(0.5, 0.7, 0.8, 0.9, 0.95), method="empirical",
    title="Spare-Parts Demand: Interval Coverage",
    coverage_color="#2a7f62", template="plotly_white")
fig.show()''',
    "dataviz.regression.calibration_regression.uncertainty_band_plot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.calibration_regression import uncertainty_band_plot_static

rng = np.random.default_rng(42)
n = 30
mean_pred = pd.Series(np.sort(rng.uniform(200, 800, n)), name="gp_mean_cycles")
sigma = pd.Series(rng.uniform(20, 60, n), name="gp_std_cycles")
observed = pd.Series(mean_pred + rng.normal(0, 1, n) * sigma,
                     name="observed_cycles")

ax = uncertainty_band_plot_static(
    observed, mean_pred, sigma, z=1.96,
    title="Battery Life GP Model: Predictive Uncertainty Band",
    line_color="#c0392b")
ax.set_ylabel("Charge cycles")
plt.show()''',
    "dataviz.regression.calibration_regression.uncertainty_band_plot_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.calibration_regression import uncertainty_band_plot_interactive

rng = np.random.default_rng(42)
n = 30
mean_pred = pd.Series(np.sort(rng.uniform(200, 800, n)), name="gp_mean_cycles")
sigma = pd.Series(rng.uniform(20, 60, n), name="gp_std_cycles")
observed = pd.Series(mean_pred + rng.normal(0, 1, n) * sigma,
                     name="observed_cycles")

fig = uncertainty_band_plot_interactive(
    observed, mean_pred, sigma, z=1.96,
    title="Battery Life GP Model: Predictive Uncertainty Band",
    line_color="#c0392b", template="plotly_white")
fig.show()''',
    # ------------------------------------------------------------------
    # dataviz.regression.charts
    # ------------------------------------------------------------------
    "dataviz.regression.charts.residual_plot": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.charts import residual_plot

rng = np.random.default_rng(42)
n = 26
predicted = rng.uniform(30, 95, n)
actual = predicted + rng.normal(0, 5, n) + 0.002 * (predicted - 60) ** 2

ax = residual_plot(actual, predicted,
                   title="Compressor Efficiency Model: Residuals",
                   color="#2a7f62", edgecolor="white")
ax.axhline(5.0, color="#888", linestyle=":", linewidth=1)
plt.show()''',
    "dataviz.regression.charts.prediction_plot": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.charts import prediction_plot

rng = np.random.default_rng(42)
n = 26
actual = rng.uniform(120, 480, n)
predicted = actual * rng.normal(1.0, 0.06, n)

ax = prediction_plot(actual, predicted,
                     title="Insurance Claim Severity: Predicted vs Actual",
                     color="#1f6fb2", edgecolor="white")
ax.set_xlabel("Actual claim cost (k USD)")
plt.show()''',
    "dataviz.regression.charts.learning_curve": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.charts import learning_curve

train_sizes = np.array([20, 40, 60, 80, 100, 120])
train_scores = np.array([0.99, 0.97, 0.96, 0.95, 0.945, 0.94])
val_scores = np.array([0.62, 0.71, 0.77, 0.81, 0.83, 0.845])

ax = learning_curve(train_sizes, train_scores, val_scores,
                    title="Yield Prediction: Learning Curve (R2)")
ax.set_ylim(0.5, 1.02)
plt.show()''',
    # ------------------------------------------------------------------
    # dataviz.regression.coefficients
    # ------------------------------------------------------------------
    "dataviz.regression.coefficients.coefficient_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.coefficients import coefficient_plot_static

features = ["temperature_c", "pressure_bar", "catalyst_g", "residence_min",
            "humidity_pct"]
coefs = np.array([1.85, -0.42, 2.30, 0.66, -0.12])

ax = coefficient_plot_static(coefs, feature_names=features,
                             title="Polymer Yield Model: Coefficients",
                             positive_color="#2a7f62",
                             negative_color="#c0392b", sort=True)
ax.set_xlabel("Coefficient (kg yield per unit)")
plt.show()''',
    "dataviz.regression.coefficients.coefficient_plot_interactive": '''import numpy as np
from dataviz.regression.coefficients import coefficient_plot_interactive

features = ["temperature_c", "pressure_bar", "catalyst_g", "residence_min",
            "humidity_pct"]
coefs = np.array([1.85, -0.42, 2.30, 0.66, -0.12])

fig = coefficient_plot_interactive(coefs, feature_names=features,
                                   title="Polymer Yield Model: Coefficients",
                                   positive_color="#2a7f62",
                                   negative_color="#c0392b", sort=True,
                                   template="plotly_white")
fig.show()''',
    "dataviz.regression.coefficients.coefficient_forest_plot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.coefficients import coefficient_forest_plot_static

rng = np.random.default_rng(42)
n = 30
X = pd.DataFrame({
    "sqft_k": rng.uniform(0.8, 3.5, n),
    "bedrooms": rng.integers(1, 6, n).astype(float),
    "age_years": rng.uniform(0, 60, n),
})
y = pd.Series(80 + 120 * X["sqft_k"] + 8 * X["bedrooms"]
              - 0.6 * X["age_years"] + rng.normal(0, 15, n),
              name="price_k")

ax = coefficient_forest_plot_static(X, y, feature_names=list(X.columns),
                                    include_intercept=True,
                                    title="Housing Price OLS: 95% CI Forest",
                                    color="#1f6fb2")
plt.show()''',
    "dataviz.regression.coefficients.coefficient_forest_plot_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.coefficients import coefficient_forest_plot_interactive

rng = np.random.default_rng(42)
n = 30
X = pd.DataFrame({
    "sqft_k": rng.uniform(0.8, 3.5, n),
    "bedrooms": rng.integers(1, 6, n).astype(float),
    "age_years": rng.uniform(0, 60, n),
})
y = pd.Series(80 + 120 * X["sqft_k"] + 8 * X["bedrooms"]
              - 0.6 * X["age_years"] + rng.normal(0, 15, n),
              name="price_k")

fig = coefficient_forest_plot_interactive(X, y, feature_names=list(X.columns),
                                          include_intercept=True,
                                          title="Housing Price OLS: 95% CI Forest",
                                          color="#1f6fb2",
                                          template="plotly_white")
fig.show()''',
    "dataviz.regression.coefficients.standardized_coefficient_plot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.coefficients import standardized_coefficient_plot_static

rng = np.random.default_rng(42)
n = 30
X = pd.DataFrame({
    "miles_driven_k": rng.uniform(2, 25, n),
    "vehicle_age_yr": rng.uniform(0, 15, n),
    "engine_l": rng.uniform(1.2, 5.0, n),
})
y = pd.Series(300 + 18 * X["miles_driven_k"] + 45 * X["vehicle_age_yr"]
              + 30 * X["engine_l"] + rng.normal(0, 60, n),
              name="annual_maintenance_usd")

ax = standardized_coefficient_plot_static(
    X, y, feature_names=list(X.columns),
    title="Fleet Maintenance Cost: Standardized Coefficients",
    positive_color="#2a7f62", negative_color="#c0392b")
plt.show()''',
    "dataviz.regression.coefficients.standardized_coefficient_plot_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.coefficients import standardized_coefficient_plot_interactive

rng = np.random.default_rng(42)
n = 30
X = pd.DataFrame({
    "miles_driven_k": rng.uniform(2, 25, n),
    "vehicle_age_yr": rng.uniform(0, 15, n),
    "engine_l": rng.uniform(1.2, 5.0, n),
})
y = pd.Series(300 + 18 * X["miles_driven_k"] + 45 * X["vehicle_age_yr"]
              + 30 * X["engine_l"] + rng.normal(0, 60, n),
              name="annual_maintenance_usd")

fig = standardized_coefficient_plot_interactive(
    X, y, feature_names=list(X.columns),
    title="Fleet Maintenance Cost: Standardized Coefficients",
    positive_color="#2a7f62", negative_color="#c0392b",
    template="plotly_white")
fig.show()''',
    "dataviz.regression.coefficients.coefficient_path_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.coefficients import coefficient_path_plot_static

alphas = np.logspace(-3, 1, 20)
features = ["income", "debt_ratio", "credit_age", "utilization"]
true_betas = np.array([0.9, -1.4, 0.5, -0.8])
paths = true_betas[None, :] * (1 - np.exp(-alphas[:, None] * 5))

ax = coefficient_path_plot_static(alphas, paths, feature_names=features,
                                  log_x=True,
                                  title="Credit Risk Lasso: Coefficient Path",
                                  cmap="tab10")
ax.set_xlabel("Regularization strength (log)")
plt.show()''',
    "dataviz.regression.coefficients.coefficient_path_plot_interactive": '''import numpy as np
from dataviz.regression.coefficients import coefficient_path_plot_interactive

alphas = np.logspace(-3, 1, 20)
features = ["income", "debt_ratio", "credit_age", "utilization"]
true_betas = np.array([0.9, -1.4, 0.5, -0.8])
paths = true_betas[None, :] * (1 - np.exp(-alphas[:, None] * 5))

fig = coefficient_path_plot_interactive(alphas, paths, feature_names=features,
                                        log_x=True,
                                        title="Credit Risk Lasso: Coefficient Path",
                                        template="plotly_white")
fig.show()''',
    # ------------------------------------------------------------------
    # dataviz.regression.comparison
    # ------------------------------------------------------------------
    "dataviz.regression.comparison.multi_model_pred_vs_actual_overlay_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.comparison import multi_model_pred_vs_actual_overlay_static

rng = np.random.default_rng(42)
actual = pd.Series(rng.uniform(40, 160, 30), name="actual_throughput")
preds = [actual + rng.normal(0, 6, 30),
         actual * rng.normal(1.0, 0.09, 30),
         actual + rng.normal(4, 10, 30)]
labels = ["Linear", "Random Forest", "Gradient Boosting"]

ax = multi_model_pred_vs_actual_overlay_static(
    actual, preds, labels,
    title="Line Throughput: Predicted vs Actual by Model",
    cmap="Dark2")
ax.set_xlabel("Actual units/hour")
plt.show()''',
    "dataviz.regression.comparison.multi_model_pred_vs_actual_overlay_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.comparison import multi_model_pred_vs_actual_overlay_interactive

rng = np.random.default_rng(42)
actual = pd.Series(rng.uniform(40, 160, 30), name="actual_throughput")
preds = [actual + rng.normal(0, 6, 30),
         actual * rng.normal(1.0, 0.09, 30),
         actual + rng.normal(4, 10, 30)]
labels = ["Linear", "Random Forest", "Gradient Boosting"]

fig = multi_model_pred_vs_actual_overlay_interactive(
    actual, preds, labels,
    title="Line Throughput: Predicted vs Actual by Model",
    template="plotly_white")
fig.show()''',
    "dataviz.regression.comparison.residual_density_overlay_multi_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.comparison import residual_density_overlay_multi_static

rng = np.random.default_rng(42)
residuals = [rng.normal(0, 5, 40),
             rng.normal(0.5, 8, 40),
             rng.normal(-1.5, 12, 40)]
labels = ["Ridge", "SVR", "KNN"]

ax = residual_density_overlay_multi_static(
    residuals, labels,
    title="Energy Demand Models: Residual Density Overlay",
    cmap="viridis")
ax.set_xlabel("Residual (MWh)")
plt.show()''',
    "dataviz.regression.comparison.residual_density_overlay_multi_interactive": '''import numpy as np
from dataviz.regression.comparison import residual_density_overlay_multi_interactive

rng = np.random.default_rng(42)
residuals = [rng.normal(0, 5, 40),
             rng.normal(0.5, 8, 40),
             rng.normal(-1.5, 12, 40)]
labels = ["Ridge", "SVR", "KNN"]

fig = residual_density_overlay_multi_interactive(
    residuals, labels,
    title="Energy Demand Models: Residual Density Overlay",
    template="plotly_white")
fig.show()''',
    "dataviz.regression.comparison.error_ecdf_overlay_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.comparison import error_ecdf_overlay_static

rng = np.random.default_rng(42)
errors = [rng.normal(0, 4, 35),
          rng.normal(0, 7, 35),
          rng.normal(2, 10, 35)]
labels = ["OLS", "Huber", "Quantile (median)"]

ax = error_ecdf_overlay_static(errors, labels,
                               title="Delivery-Time Models: |Error| ECDF",
                               cmap="plasma")
ax.set_xlabel("Absolute error (minutes)")
plt.show()''',
    "dataviz.regression.comparison.error_ecdf_overlay_interactive": '''import numpy as np
from dataviz.regression.comparison import error_ecdf_overlay_interactive

rng = np.random.default_rng(42)
errors = [rng.normal(0, 4, 35),
          rng.normal(0, 7, 35),
          rng.normal(2, 10, 35)]
labels = ["OLS", "Huber", "Quantile (median)"]

fig = error_ecdf_overlay_interactive(errors, labels,
                                     title="Delivery-Time Models: |Error| ECDF",
                                     template="plotly_white")
fig.show()''',
    "dataviz.regression.comparison.model_winner_heatmap_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.comparison import model_winner_heatmap_static

models = ["Linear", "Random Forest", "XGBoost"]
metrics = ["MAE", "RMSE", "MAPE", "R2"]
wins = np.array([[0, 0, 0, 0],
                 [1, 0, 1, 0],
                 [0, 1, 0, 1]])

ax = model_winner_heatmap_static(models, metrics, wins,
                                 title="Warranty Cost Models: Winner per Metric",
                                 cmap="YlGn")
plt.show()''',
    "dataviz.regression.comparison.model_winner_heatmap_interactive": '''import numpy as np
from dataviz.regression.comparison import model_winner_heatmap_interactive

models = ["Linear", "Random Forest", "XGBoost"]
metrics = ["MAE", "RMSE", "MAPE", "R2"]
wins = np.array([[0, 0, 0, 0],
                 [1, 0, 1, 0],
                 [0, 1, 0, 1]])

fig = model_winner_heatmap_interactive(models, metrics, wins,
                                       title="Warranty Cost Models: Winner per Metric",
                                       colorscale="YlGn",
                                       template="plotly_white")
fig.show()''',
    # ------------------------------------------------------------------
    # dataviz.regression.cv_extended
    # ------------------------------------------------------------------
    "dataviz.regression.cv_extended.learning_curve_with_band_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.cv_extended import learning_curve_with_band_static

train_sizes = np.array([25, 50, 75, 100, 125, 150])
mean_rmse = np.array([18.5, 14.2, 12.1, 11.0, 10.4, 10.1])
std_rmse = np.array([3.1, 2.2, 1.7, 1.4, 1.2, 1.1])

ax = learning_curve_with_band_static(
    train_sizes, mean_rmse, std_rmse,
    title="Cycle-Time Model: Learning Curve (5-fold CV)",
    metric_name="RMSE (seconds)", color="#1f6fb2")
plt.show()''',
    "dataviz.regression.cv_extended.learning_curve_with_band_interactive": '''import numpy as np
from dataviz.regression.cv_extended import learning_curve_with_band_interactive

train_sizes = np.array([25, 50, 75, 100, 125, 150])
mean_rmse = np.array([18.5, 14.2, 12.1, 11.0, 10.4, 10.1])
std_rmse = np.array([3.1, 2.2, 1.7, 1.4, 1.2, 1.1])

fig = learning_curve_with_band_interactive(
    train_sizes, mean_rmse, std_rmse,
    title="Cycle-Time Model: Learning Curve (5-fold CV)",
    metric_name="RMSE (seconds)", color="#1f6fb2",
    template="plotly_white")
fig.show()''',
    "dataviz.regression.cv_extended.nested_cv_score_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.cv_extended import nested_cv_score_plot_static

outer_folds = ["Fold 1", "Fold 2", "Fold 3", "Fold 4", "Fold 5"]
scores = np.array([0.81, 0.77, 0.84, 0.79, 0.82])

ax = nested_cv_score_plot_static(outer_folds, scores,
                                 title="Churn Value Model: Nested CV R2",
                                 metric_name="R2", color="#2a7f62")
ax.set_ylim(0.6, 0.9)
plt.show()''',
    "dataviz.regression.cv_extended.nested_cv_score_plot_interactive": '''import numpy as np
from dataviz.regression.cv_extended import nested_cv_score_plot_interactive

outer_folds = ["Fold 1", "Fold 2", "Fold 3", "Fold 4", "Fold 5"]
scores = np.array([0.81, 0.77, 0.84, 0.79, 0.82])

fig = nested_cv_score_plot_interactive(outer_folds, scores,
                                       title="Churn Value Model: Nested CV R2",
                                       metric_name="R2", color="#2a7f62",
                                       template="plotly_white")
fig.show()''',
    "dataviz.regression.cv_extended.cv_residual_distribution_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.cv_extended import cv_residual_distribution_static

rng = np.random.default_rng(42)
folds = ["Fold 1", "Fold 2", "Fold 3", "Fold 4"]
residuals = [rng.normal(0, 4, 15),
             rng.normal(1.5, 5, 15),
             rng.normal(-0.8, 3.5, 15),
             rng.normal(0.4, 6, 15)]

ax = cv_residual_distribution_static(
    folds, residuals,
    title="Concrete Strength Model: Residuals per CV Fold",
    color="#1f6fb2")
ax.set_ylabel("Residual (MPa)")
plt.show()''',
    "dataviz.regression.cv_extended.cv_residual_distribution_interactive": '''import numpy as np
from dataviz.regression.cv_extended import cv_residual_distribution_interactive

rng = np.random.default_rng(42)
folds = ["Fold 1", "Fold 2", "Fold 3", "Fold 4"]
residuals = [rng.normal(0, 4, 15),
             rng.normal(1.5, 5, 15),
             rng.normal(-0.8, 3.5, 15),
             rng.normal(0.4, 6, 15)]

fig = cv_residual_distribution_interactive(
    folds, residuals,
    title="Concrete Strength Model: Residuals per CV Fold",
    color="#1f6fb2", template="plotly_white")
fig.show()''',
    "dataviz.regression.cv_extended.repeated_kfold_violin_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.cv_extended import repeated_kfold_violin_static

rng = np.random.default_rng(42)
repeats = ["Repeat 1", "Repeat 2", "Repeat 3"]
scores = [rng.normal(0.78, 0.04, 5),
          rng.normal(0.81, 0.03, 5),
          rng.normal(0.79, 0.05, 5)]

ax = repeated_kfold_violin_static(
    repeats, scores,
    title="Soil Moisture Model: Repeated 5-Fold R2",
    metric_name="R2", color="#2a7f62")
plt.show()''',
    "dataviz.regression.cv_extended.repeated_kfold_violin_interactive": '''import numpy as np
from dataviz.regression.cv_extended import repeated_kfold_violin_interactive

rng = np.random.default_rng(42)
repeats = ["Repeat 1", "Repeat 2", "Repeat 3"]
scores = [rng.normal(0.78, 0.04, 5),
          rng.normal(0.81, 0.03, 5),
          rng.normal(0.79, 0.05, 5)]

fig = repeated_kfold_violin_interactive(
    repeats, scores,
    title="Soil Moisture Model: Repeated 5-Fold R2",
    metric_name="R2", color="#2a7f62", template="plotly_white")
fig.show()''',
    "dataviz.regression.cv_extended.group_cv_score_strip_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.cv_extended import group_cv_score_strip_static

plants = ["Plant A", "Plant B", "Plant C", "Plant D", "Plant E"]
scores = np.array([0.72, 0.83, 0.68, 0.79, 0.75])

ax = group_cv_score_strip_static(plants, scores,
                                 title="OEE Model: Leave-One-Plant-Out R2",
                                 metric_name="R2", color="#c0392b")
ax.set_ylim(0.5, 1.0)
plt.show()''',
    "dataviz.regression.cv_extended.group_cv_score_strip_interactive": '''import numpy as np
from dataviz.regression.cv_extended import group_cv_score_strip_interactive

plants = ["Plant A", "Plant B", "Plant C", "Plant D", "Plant E"]
scores = np.array([0.72, 0.83, 0.68, 0.79, 0.75])

fig = group_cv_score_strip_interactive(plants, scores,
                                       title="OEE Model: Leave-One-Plant-Out R2",
                                       metric_name="R2", color="#c0392b",
                                       template="plotly_white")
fig.show()''',
    # ------------------------------------------------------------------
    # dataviz.regression.diagnostics_panel
    # ------------------------------------------------------------------
    "dataviz.regression.diagnostics_panel.regression_diagnostic_panel_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.diagnostics_panel import regression_diagnostic_panel_static

rng = np.random.default_rng(42)
n = 30
X = pd.DataFrame({
    "temperature_c": rng.uniform(15, 35, n),
    "rainfall_mm": rng.uniform(200, 1200, n),
    "fertilizer_kg": rng.uniform(50, 300, n),
})
y = pd.Series(2.1 * X["temperature_c"] + 0.004 * X["rainfall_mm"]
              + 0.015 * X["fertilizer_kg"] + rng.normal(0, 4, n),
              name="yield_t_ha")
fitted = pd.Series(2.1 * X["temperature_c"] + 0.004 * X["rainfall_mm"]
                   + 0.015 * X["fertilizer_kg"], name="fitted")

fig = regression_diagnostic_panel_static(
    X, y, fitted, title="Crop Yield Model: Diagnostic Panel",
    color="#1f6fb2", line_color="#c0392b")
plt.show()''',
    "dataviz.regression.diagnostics_panel.regression_diagnostic_panel_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.diagnostics_panel import regression_diagnostic_panel_interactive

rng = np.random.default_rng(42)
n = 30
X = pd.DataFrame({
    "temperature_c": rng.uniform(15, 35, n),
    "rainfall_mm": rng.uniform(200, 1200, n),
    "fertilizer_kg": rng.uniform(50, 300, n),
})
y = pd.Series(2.1 * X["temperature_c"] + 0.004 * X["rainfall_mm"]
              + 0.015 * X["fertilizer_kg"] + rng.normal(0, 4, n),
              name="yield_t_ha")
fitted = pd.Series(2.1 * X["temperature_c"] + 0.004 * X["rainfall_mm"]
                   + 0.015 * X["fertilizer_kg"], name="fitted")

fig = regression_diagnostic_panel_interactive(
    X, y, fitted, title="Crop Yield Model: Diagnostic Panel",
    color="#1f6fb2", line_color="#c0392b", template="plotly_white")
fig.show()''',
    "dataviz.regression.diagnostics_panel.regression_dashboard_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.diagnostics_panel import regression_dashboard_static

rng = np.random.default_rng(42)
n = 32
actual = pd.Series(rng.uniform(15, 90, n), name="actual_wait_min")
predicted = pd.Series(actual + rng.normal(0, 6, n), name="predicted_wait_min")

fig = regression_dashboard_static(
    actual, predicted, n_features=4,
    title="Clinic Wait-Time Model: Performance Dashboard",
    color="#2a7f62", line_color="#c0392b")
plt.show()''',
    "dataviz.regression.diagnostics_panel.regression_dashboard_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.diagnostics_panel import regression_dashboard_interactive

rng = np.random.default_rng(42)
n = 32
actual = pd.Series(rng.uniform(15, 90, n), name="actual_wait_min")
predicted = pd.Series(actual + rng.normal(0, 6, n), name="predicted_wait_min")

fig = regression_dashboard_interactive(
    actual, predicted, n_features=4,
    title="Clinic Wait-Time Model: Performance Dashboard",
    color="#2a7f62", line_color="#c0392b", template="plotly_white")
fig.show()''',
    # ------------------------------------------------------------------
    # dataviz.regression.domain
    # ------------------------------------------------------------------
    "dataviz.regression.domain.price_elasticity_curve_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.domain import price_elasticity_curve_static

rng = np.random.default_rng(42)
price = pd.Series(rng.uniform(8, 30, 24), name="price_usd")
quantity = pd.Series(900 * price ** -1.4 * rng.normal(1, 0.06, 24),
                     name="units_sold")
fitted = 900 * price ** -1.4

ax = price_elasticity_curve_static(price, quantity, fitted_curve=fitted,
                                   title="Snack Line: Price Elasticity Curve",
                                   color="#1f6fb2")
ax.set_ylabel("Weekly units sold")
plt.show()''',
    "dataviz.regression.domain.price_elasticity_curve_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.domain import price_elasticity_curve_interactive

rng = np.random.default_rng(42)
price = pd.Series(rng.uniform(8, 30, 24), name="price_usd")
quantity = pd.Series(900 * price ** -1.4 * rng.normal(1, 0.06, 24),
                     name="units_sold")
fitted = 900 * price ** -1.4

fig = price_elasticity_curve_interactive(price, quantity, fitted_curve=fitted,
                                         title="Snack Line: Price Elasticity Curve",
                                         color="#1f6fb2",
                                         template="plotly_white")
fig.show()''',
    "dataviz.regression.domain.dose_response_curve_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.domain import dose_response_curve_static

rng = np.random.default_rng(42)
dose = pd.Series(np.logspace(-1, 2, 14), name="dose_mg")
response = pd.Series(100 / (1 + (dose / 12) ** -1.1) + rng.normal(0, 3, 14),
                     name="response_pct")
lo = response - 6.0
hi = response + 6.0

ax = dose_response_curve_static(dose, response, lower=lo, upper=hi,
                                title="Compound B: Dose-Response (EC50)",
                                color="#2a7f62")
ax.set_ylabel("Response (% of max)")
plt.show()''',
    "dataviz.regression.domain.dose_response_curve_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.domain import dose_response_curve_interactive

rng = np.random.default_rng(42)
dose = pd.Series(np.logspace(-1, 2, 14), name="dose_mg")
response = pd.Series(100 / (1 + (dose / 12) ** -1.1) + rng.normal(0, 3, 14),
                     name="response_pct")
lo = response - 6.0
hi = response + 6.0

fig = dose_response_curve_interactive(dose, response, lower=lo, upper=hi,
                                      title="Compound B: Dose-Response (EC50)",
                                      color="#2a7f62",
                                      template="plotly_white")
fig.show()''',
    "dataviz.regression.domain.demand_forecast_fan_chart_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.domain import demand_forecast_fan_chart_static

weeks = pd.Series(np.arange(1, 21), name="week_ahead")
central = pd.Series(1000 * (1.02 ** weeks), name="central_forecast")
spread = 30 * np.sqrt(weeks)
bands = [(central - 1.96 * spread, central + 1.96 * spread),
         (central - 1.28 * spread, central + 1.28 * spread),
         (central - 0.67 * spread, central + 0.67 * spread)]

ax = demand_forecast_fan_chart_static(
    weeks, central, bands,
    title="Grocery SKU: 20-Week Demand Forecast Fan",
    color="#c0392b", cmap="Blues")
ax.set_xlabel("Weeks ahead")
plt.show()''',
    "dataviz.regression.domain.demand_forecast_fan_chart_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.domain import demand_forecast_fan_chart_interactive

weeks = pd.Series(np.arange(1, 21), name="week_ahead")
central = pd.Series(1000 * (1.02 ** weeks), name="central_forecast")
spread = 30 * np.sqrt(weeks)
bands = [(central - 1.96 * spread, central + 1.96 * spread),
         (central - 1.28 * spread, central + 1.28 * spread),
         (central - 0.67 * spread, central + 0.67 * spread)]

fig = demand_forecast_fan_chart_interactive(
    weeks, central, bands,
    title="Grocery SKU: 20-Week Demand Forecast Fan",
    color="#c0392b", template="plotly_white")
fig.show()''',
    "dataviz.regression.domain.yield_curve_fit_plot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.domain import yield_curve_fit_plot_static

rng = np.random.default_rng(42)
maturities = pd.Series([0.25, 0.5, 1, 2, 3, 5, 7, 10, 15, 20, 30],
                       name="maturity_years")
observed = pd.Series(4.2 - 1.8 * np.exp(-maturities / 3)
                     + rng.normal(0, 0.05, maturities.size), name="yield_pct")
fitted = pd.Series(4.2 - 1.8 * np.exp(-maturities / 3), name="fitted_pct")

ax = yield_curve_fit_plot_static(maturities, observed, fitted,
                                 title="Treasury Yield Curve: Nelson-Siegel Fit",
                                 obs_color="#1f6fb2", fit_color="#c0392b")
ax.set_xlabel("Maturity (years)")
plt.show()''',
    "dataviz.regression.domain.yield_curve_fit_plot_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.domain import yield_curve_fit_plot_interactive

rng = np.random.default_rng(42)
maturities = pd.Series([0.25, 0.5, 1, 2, 3, 5, 7, 10, 15, 20, 30],
                       name="maturity_years")
observed = pd.Series(4.2 - 1.8 * np.exp(-maturities / 3)
                     + rng.normal(0, 0.05, maturities.size), name="yield_pct")
fitted = pd.Series(4.2 - 1.8 * np.exp(-maturities / 3), name="fitted_pct")

fig = yield_curve_fit_plot_interactive(maturities, observed, fitted,
                                       title="Treasury Yield Curve: Nelson-Siegel Fit",
                                       obs_color="#1f6fb2", fit_color="#c0392b",
                                       template="plotly_white")
fig.show()''',
    # ------------------------------------------------------------------
    # dataviz.regression.effects
    # ------------------------------------------------------------------
    "dataviz.regression.effects.partial_dependence_regression_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.effects import partial_dependence_regression_static

grid = pd.Series(np.linspace(500, 4000, 25), name="sqft")
pd_values = pd.Series(60 + 0.09 * grid + 12 * np.log(grid / 500),
                      name="pd_price_k")

ax = partial_dependence_regression_static(
    grid, pd_values,
    title="Partial Dependence: Living Area on Price",
    feature_name="living area (sqft)", color="#1f6fb2")
ax.set_ylabel("Predicted price (k USD)")
plt.show()''',
    "dataviz.regression.effects.partial_dependence_regression_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.effects import partial_dependence_regression_interactive

grid = pd.Series(np.linspace(500, 4000, 25), name="sqft")
pd_values = pd.Series(60 + 0.09 * grid + 12 * np.log(grid / 500),
                      name="pd_price_k")

fig = partial_dependence_regression_interactive(
    grid, pd_values,
    title="Partial Dependence: Living Area on Price",
    feature_name="living area (sqft)", color="#1f6fb2",
    template="plotly_white")
fig.show()''',
    "dataviz.regression.effects.ice_plot_regression_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.effects import ice_plot_regression_static

rng = np.random.default_rng(42)
grid = np.linspace(0, 40, 20)
ice = np.vstack([50 + 1.8 * grid + rng.normal(0, 8) + 0.02 * grid ** 2
                 for _ in range(15)])

ax = ice_plot_regression_static(grid, ice,
                                title="ICE: Commute Distance on Rent",
                                feature_name="distance to downtown (km)",
                                alpha=0.25)
ax.set_ylabel("Predicted rent (USD)")
plt.show()''',
    "dataviz.regression.effects.ice_plot_regression_interactive": '''import numpy as np
from dataviz.regression.effects import ice_plot_regression_interactive

rng = np.random.default_rng(42)
grid = np.linspace(0, 40, 20)
ice = np.vstack([50 + 1.8 * grid + rng.normal(0, 8) + 0.02 * grid ** 2
                 for _ in range(15)])

fig = ice_plot_regression_interactive(grid, ice,
                                      title="ICE: Commute Distance on Rent",
                                      feature_name="distance to downtown (km)",
                                      opacity=0.25, template="plotly_white")
fig.show()''',
    "dataviz.regression.effects.marginal_effects_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.effects import marginal_effects_plot_static

features = ["discount_pct", "shelf_position", "weekend", "ad_impressions_k"]
effects = np.array([1.9, 0.7, 0.4, 0.15])
lo = effects - np.array([0.4, 0.3, 0.35, 0.2])
hi = effects + np.array([0.45, 0.3, 0.35, 0.22])

ax = marginal_effects_plot_static(
    features, effects, ci_lower=lo, ci_upper=hi,
    title="Promo Response Model: Average Marginal Effects",
    color="#2a7f62")
ax.set_xlabel("Effect on daily units sold")
plt.show()''',
    "dataviz.regression.effects.marginal_effects_plot_interactive": '''import numpy as np
from dataviz.regression.effects import marginal_effects_plot_interactive

features = ["discount_pct", "shelf_position", "weekend", "ad_impressions_k"]
effects = np.array([1.9, 0.7, 0.4, 0.15])
lo = effects - np.array([0.4, 0.3, 0.35, 0.2])
hi = effects + np.array([0.45, 0.3, 0.35, 0.22])

fig = marginal_effects_plot_interactive(
    features, effects, ci_lower=lo, ci_upper=hi,
    title="Promo Response Model: Average Marginal Effects",
    color="#2a7f62", template="plotly_white")
fig.show()''',
    "dataviz.regression.effects.interaction_effect_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.effects import interaction_effect_plot_static

grid = np.linspace(20, 90, 20)
curves = np.vstack([
    100 + 0.5 * grid,
    100 + 0.9 * grid + 0.01 * grid ** 2,
    100 + 1.4 * grid + 0.03 * grid ** 2,
])
labels = ["low humidity", "medium humidity", "high humidity"]

ax = interaction_effect_plot_static(
    grid, curves, labels,
    title="Interaction: Temperature x Humidity on Drying Time",
    feature_name="temperature (C)", cmap="viridis")
ax.set_ylabel("Predicted drying time (min)")
plt.show()''',
    "dataviz.regression.effects.interaction_effect_plot_interactive": '''import numpy as np
from dataviz.regression.effects import interaction_effect_plot_interactive

grid = np.linspace(20, 90, 20)
curves = np.vstack([
    100 + 0.5 * grid,
    100 + 0.9 * grid + 0.01 * grid ** 2,
    100 + 1.4 * grid + 0.03 * grid ** 2,
])
labels = ["low humidity", "medium humidity", "high humidity"]

fig = interaction_effect_plot_interactive(
    grid, curves, labels,
    title="Interaction: Temperature x Humidity on Drying Time",
    feature_name="temperature (C)", template="plotly_white")
fig.show()''',
    "dataviz.regression.effects.conditional_expectation_curve_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.effects import conditional_expectation_curve_static

grid = pd.Series(np.linspace(18, 42, 24), name="bmi")
ce = pd.Series(70 + 0.9 * (grid - 25) + 0.06 * (grid - 25) ** 2,
               name="e_bp")
lo = ce - 3.0
hi = ce + 3.0

ax = conditional_expectation_curve_static(
    grid, ce, ci_lower=lo, ci_upper=hi,
    title="E[Systolic BP | BMI] with 95% Band",
    feature_name="BMI", color="#c0392b")
ax.set_ylabel("E[Systolic BP | BMI] (mmHg)")
plt.show()''',
    "dataviz.regression.effects.conditional_expectation_curve_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.effects import conditional_expectation_curve_interactive

grid = pd.Series(np.linspace(18, 42, 24), name="bmi")
ce = pd.Series(70 + 0.9 * (grid - 25) + 0.06 * (grid - 25) ** 2,
               name="e_bp")
lo = ce - 3.0
hi = ce + 3.0

fig = conditional_expectation_curve_interactive(
    grid, ce, ci_lower=lo, ci_upper=hi,
    title="E[Systolic BP | BMI] with 95% Band",
    feature_name="BMI", color="#c0392b", template="plotly_white")
fig.show()''',
    "dataviz.regression.effects.elasticity_plot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.effects import elasticity_plot_static

price_grid = pd.Series(np.linspace(5, 40, 22), name="price_usd")
elasticity = pd.Series(-1.8 + 0.9 * np.exp(-price_grid / 12),
                       name="elasticity")

ax = elasticity_plot_static(price_grid, elasticity,
                            title="Own-Price Elasticity by Price Point",
                            feature_name="price (USD)", color="#1f6fb2")
ax.axhline(-1.0, color="#c0392b", linestyle=":", linewidth=1)
plt.show()''',
    "dataviz.regression.effects.elasticity_plot_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.effects import elasticity_plot_interactive

price_grid = pd.Series(np.linspace(5, 40, 22), name="price_usd")
elasticity = pd.Series(-1.8 + 0.9 * np.exp(-price_grid / 12),
                       name="elasticity")

fig = elasticity_plot_interactive(price_grid, elasticity,
                                  title="Own-Price Elasticity by Price Point",
                                  feature_name="price (USD)", color="#1f6fb2",
                                  template="plotly_white")
fig.show()''',
    # ------------------------------------------------------------------
    # dataviz.regression.errors_loss
    # ------------------------------------------------------------------
    "dataviz.regression.errors_loss.loss_distribution_violin_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.errors_loss import loss_distribution_violin_static

rng = np.random.default_rng(42)
models = ["Ridge", "Random Forest", "XGBoost"]
losses = [np.abs(rng.normal(0, 5, 30)),
          np.abs(rng.normal(0, 3.5, 30)),
          np.abs(rng.normal(0, 3.0, 30))]

ax = loss_distribution_violin_static(
    models, losses,
    title="Freight Cost Models: Per-Shipment Absolute Loss",
    metric_name="absolute error (USD)", color="#1f6fb2")
plt.show()''',
    "dataviz.regression.errors_loss.loss_distribution_violin_interactive": '''import numpy as np
from dataviz.regression.errors_loss import loss_distribution_violin_interactive

rng = np.random.default_rng(42)
models = ["Ridge", "Random Forest", "XGBoost"]
losses = [np.abs(rng.normal(0, 5, 30)),
          np.abs(rng.normal(0, 3.5, 30)),
          np.abs(rng.normal(0, 3.0, 30))]

fig = loss_distribution_violin_interactive(
    models, losses,
    title="Freight Cost Models: Per-Shipment Absolute Loss",
    metric_name="absolute error (USD)", color="#1f6fb2",
    template="plotly_white")
fig.show()''',
    "dataviz.regression.errors_loss.ranked_error_plot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.errors_loss import ranked_error_plot_static

rng = np.random.default_rng(42)
actual = pd.Series(rng.uniform(200, 900, 28), name="actual_repair_cost")
predicted = pd.Series(actual * rng.normal(1.0, 0.12, 28),
                      name="predicted_repair_cost")
errors = actual - predicted

ax = ranked_error_plot_static(errors,
                              title="Repair Cost Model: Ranked Errors",
                              color="#c0392b")
ax.set_xlabel("Rank (sorted by error)")
plt.show()''',
    "dataviz.regression.errors_loss.ranked_error_plot_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.errors_loss import ranked_error_plot_interactive

rng = np.random.default_rng(42)
actual = pd.Series(rng.uniform(200, 900, 28), name="actual_repair_cost")
predicted = pd.Series(actual * rng.normal(1.0, 0.12, 28),
                      name="predicted_repair_cost")
errors = actual - predicted

fig = ranked_error_plot_interactive(errors,
                                    title="Repair Cost Model: Ranked Errors",
                                    color="#c0392b", template="plotly_white")
fig.show()''',
    "dataviz.regression.errors_loss.worst_k_predictions_chart_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.errors_loss import worst_k_predictions_chart_static

rng = np.random.default_rng(42)
actual = pd.Series(rng.uniform(10, 120, 25), name="actual_los_days")
predicted = pd.Series(actual + rng.normal(0, 9, 25), name="predicted_los_days")

ax = worst_k_predictions_chart_static(
    actual, predicted, k=8,
    title="Hospital Stay Model: 8 Worst Predictions",
    color="#c0392b")
ax.set_ylabel("Absolute error (days)")
plt.show()''',
    "dataviz.regression.errors_loss.worst_k_predictions_chart_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.errors_loss import worst_k_predictions_chart_interactive

rng = np.random.default_rng(42)
actual = pd.Series(rng.uniform(10, 120, 25), name="actual_los_days")
predicted = pd.Series(actual + rng.normal(0, 9, 25), name="predicted_los_days")

fig = worst_k_predictions_chart_interactive(
    actual, predicted, k=8,
    title="Hospital Stay Model: 8 Worst Predictions",
    color="#c0392b", template="plotly_white")
fig.show()''',
    "dataviz.regression.errors_loss.error_decomposition_bar_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.errors_loss import error_decomposition_bar_static

components = ["bias^2", "variance", "irreducible noise"]
values = np.array([12.4, 28.7, 9.1])

ax = error_decomposition_bar_static(
    components, values,
    title="Turbine Output Model: Bias-Variance Decomposition",
    color="#1f6fb2")
ax.set_ylabel("Contribution to MSE (kW^2)")
plt.show()''',
    "dataviz.regression.errors_loss.error_decomposition_bar_interactive": '''import numpy as np
from dataviz.regression.errors_loss import error_decomposition_bar_interactive

components = ["bias^2", "variance", "irreducible noise"]
values = np.array([12.4, 28.7, 9.1])

fig = error_decomposition_bar_interactive(
    components, values,
    title="Turbine Output Model: Bias-Variance Decomposition",
    color="#1f6fb2", template="plotly_white")
fig.show()''',
}
