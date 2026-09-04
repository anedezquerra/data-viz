"""Curated rich examples for regression member pages."""

EXAMPLES = {}

# ---------------------------------------------------------------------------
# forecast.py (12 members)
# ---------------------------------------------------------------------------

_FORECAST_SETUP = '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.forecast import {func}

rng = np.random.default_rng(42)
weeks = pd.date_range("2025-01-06", periods=24, freq="W-MON")
seasonal = 4.0 * np.sin(2 * np.pi * np.arange(24) / 12.0)
actual = pd.Series(52.0 + seasonal + rng.normal(0, 1.5, 24), index=weeks,
                   name="weekly_demand_kwh")
forecast = pd.Series(52.0 + seasonal + rng.normal(0, 0.9, 24), index=weeks,
                     name="arima_forecast")
'''

EXAMPLES["dataviz.regression.forecast.forecast_vs_actual_static"] = (
    _FORECAST_SETUP.format(func="forecast_vs_actual_static") + '''
ax = forecast_vs_actual_static(weeks, actual, forecast,
                               title="Plant Energy Demand: ARIMA Forecast vs Actual",
                               true_color="#1f77b4", pred_color="#d62728")
ax.set_ylabel("Demand (MWh)")
plt.show()''')

EXAMPLES["dataviz.regression.forecast.forecast_vs_actual_interactive"] = (
    _FORECAST_SETUP.format(func="forecast_vs_actual_interactive") + '''
fig = forecast_vs_actual_interactive(weeks, actual, forecast,
                                     title="Plant Energy Demand: ARIMA Forecast vs Actual",
                                     template="plotly_white")
fig.show()''')

_HORIZON_SETUP = '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.forecast import {func}

rng = np.random.default_rng(42)
horizons = np.arange(1, 15)
rmse_by_horizon = pd.Series(1.8 + 0.35 * horizons + rng.normal(0, 0.15, 14),
                            index=horizons, name="rmse_celsius")
'''

EXAMPLES["dataviz.regression.forecast.forecast_error_over_horizon_static"] = (
    _HORIZON_SETUP.format(func="forecast_error_over_horizon_static") + '''
ax = forecast_error_over_horizon_static(
    horizons, rmse_by_horizon,
    title="Cold-Chain Temperature Forecast: RMSE by Horizon",
    color="#2ca02c")
ax.set_ylabel("RMSE (deg C)")
plt.show()''')

EXAMPLES["dataviz.regression.forecast.forecast_error_over_horizon_interactive"] = (
    _HORIZON_SETUP.format(func="forecast_error_over_horizon_interactive") + '''
fig = forecast_error_over_horizon_interactive(
    horizons, rmse_by_horizon,
    title="Cold-Chain Temperature Forecast: RMSE by Horizon",
    color="#2ca02c", template="plotly_white")
fig.show()''')

_ORIGIN_SETUP = '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.forecast import {func}

rng = np.random.default_rng(42)
origins = pd.date_range("2024-01-31", periods=18, freq="ME")
mape_scores = pd.Series(8.5 - 0.15 * np.arange(18) + rng.normal(0, 0.6, 18),
                        index=origins, name="mape_pct")
'''

EXAMPLES["dataviz.regression.forecast.rolling_forecast_origin_static"] = (
    _ORIGIN_SETUP.format(func="rolling_forecast_origin_static") + '''
ax = rolling_forecast_origin_static(
    origins, mape_scores,
    title="Retail Sales Model: MAPE Across Rolling Origins",
    color="#9467bd")
ax.set_ylabel("MAPE (%)")
plt.show()''')

EXAMPLES["dataviz.regression.forecast.rolling_forecast_origin_interactive"] = (
    _ORIGIN_SETUP.format(func="rolling_forecast_origin_interactive") + '''
fig = rolling_forecast_origin_interactive(
    origins, mape_scores,
    title="Retail Sales Model: MAPE Across Rolling Origins",
    color="#9467bd", template="plotly_white")
fig.show()''')

_BACKTEST_SETUP = '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.forecast import {func}

rng = np.random.default_rng(42)
backtest_errors = pd.Series(
    rng.normal(0.5, 4.0, 400) + rng.choice([0.0, 6.0], size=400, p=[0.9, 0.1]),
    name="backtest_error_bbl")
'''

EXAMPLES["dataviz.regression.forecast.backtest_error_distribution_static"] = (
    _BACKTEST_SETUP.format(func="backtest_error_distribution_static") + '''
ax = backtest_error_distribution_static(
    backtest_errors,
    title="Oil Production Forecast: Backtest Error Distribution",
    bins=40, color="#17becf")
ax.set_xlabel("Forecast error (bbl/day)")
plt.show()''')

EXAMPLES["dataviz.regression.forecast.backtest_error_distribution_interactive"] = (
    _BACKTEST_SETUP.format(func="backtest_error_distribution_interactive") + '''
fig = backtest_error_distribution_interactive(
    backtest_errors,
    title="Oil Production Forecast: Backtest Error Distribution",
    nbins=40, color="#17becf", template="plotly_white")
fig.show()''')

_WINDOW_SETUP = '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.forecast import {func}

rng = np.random.default_rng(42)
window_sizes = np.arange(30, 211, 20)
r2_curve = pd.Series(1.0 - np.exp(-window_sizes / 90.0) + rng.normal(0, 0.01, 10),
                     index=window_sizes, name="cv_r2")
'''

EXAMPLES["dataviz.regression.forecast.expanding_window_metric_curve_static"] = (
    _WINDOW_SETUP.format(func="expanding_window_metric_curve_static") + '''
ax = expanding_window_metric_curve_static(
    window_sizes, r2_curve,
    title="Ticket Volume Model: R2 vs Expanding Training Window",
    metric_name="CV R-squared", color="#e377c2")
plt.show()''')

EXAMPLES["dataviz.regression.forecast.expanding_window_metric_curve_interactive"] = (
    _WINDOW_SETUP.format(func="expanding_window_metric_curve_interactive") + '''
fig = expanding_window_metric_curve_interactive(
    window_sizes, r2_curve,
    title="Ticket Volume Model: R2 vs Expanding Training Window",
    metric_name="CV R-squared", color="#e377c2", template="plotly_white")
fig.show()''')

_BAND_SETUP = '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.forecast import {func}

rng = np.random.default_rng(42)
days = pd.date_range("2025-03-01", periods=20, freq="D")
trend = 120.0 + 0.8 * np.arange(20)
central = pd.Series(trend + rng.normal(0, 1.0, 20), index=days,
                    name="price_forecast")
actual = pd.Series(trend + rng.normal(0, 3.0, 20), index=days,
                   name="spot_price")
lower = central - 5.0
upper = central + 5.0
'''

EXAMPLES["dataviz.regression.forecast.forecast_band_plot_static"] = (
    _BAND_SETUP.format(func="forecast_band_plot_static") + '''
ax = forecast_band_plot_static(
    days, actual, central, lower, upper,
    title="Wholesale Coffee Price: Forecast with 90% Band",
    pred_color="#1f77b4", band_color="#aec7e8")
ax.set_ylabel("Price (USD/kg)")
plt.show()''')

EXAMPLES["dataviz.regression.forecast.forecast_band_plot_interactive"] = (
    _BAND_SETUP.format(func="forecast_band_plot_interactive") + '''
fig = forecast_band_plot_interactive(
    days, actual, central, lower, upper,
    title="Wholesale Coffee Price: Forecast with 90% Band",
    template="plotly_white")
fig.show()''')

# ---------------------------------------------------------------------------
# glm.py (12 members)
# ---------------------------------------------------------------------------

_GLM_POISSON_SETUP = '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.glm import {func}

rng = np.random.default_rng(42)
exposure = rng.uniform(0.5, 3.0, 60)
mu = pd.Series(np.exp(0.8 + 0.4 * exposure), name="expected_claims")
claims = pd.Series(rng.poisson(mu), name="observed_claims")
'''

EXAMPLES["dataviz.regression.glm.link_function_plot_static"] = (
    _GLM_POISSON_SETUP.format(func="link_function_plot_static") + '''
ax = link_function_plot_static(claims, mu, link="log",
                               title="Auto Insurance Claims: Log Link Check",
                               color="#1f77b4")
ax.set_xlabel("Linear predictor scale")
plt.show()''')

EXAMPLES["dataviz.regression.glm.link_function_plot_interactive"] = (
    _GLM_POISSON_SETUP.format(func="link_function_plot_interactive") + '''
fig = link_function_plot_interactive(claims, mu, link="log",
                                     title="Auto Insurance Claims: Log Link Check",
                                     template="plotly_white")
fig.show()''')

EXAMPLES["dataviz.regression.glm.deviance_residual_plot_static"] = (
    _GLM_POISSON_SETUP.format(func="deviance_residual_plot_static") + '''
ax = deviance_residual_plot_static(claims, mu, family="poisson",
                                   title="Auto Insurance Claims: Deviance Residuals",
                                   color="#2ca02c")
ax.set_xlabel("Fitted mean claims")
plt.show()''')

EXAMPLES["dataviz.regression.glm.deviance_residual_plot_interactive"] = (
    _GLM_POISSON_SETUP.format(func="deviance_residual_plot_interactive") + '''
fig = deviance_residual_plot_interactive(
    claims, mu, family="poisson",
    title="Auto Insurance Claims: Deviance Residuals",
    template="plotly_white")
fig.show()''')

_GLM_BINOMIAL_SETUP = '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.glm import {func}

rng = np.random.default_rng(42)
dose_mg = rng.uniform(10.0, 100.0, 48)
prob = pd.Series(1.0 / (1.0 + np.exp(-(dose_mg - 55.0) / 12.0)),
                 name="response_prob")
responded = pd.Series(rng.binomial(1, prob), name="responded")
'''

EXAMPLES["dataviz.regression.glm.pearson_residual_plot_static"] = (
    _GLM_BINOMIAL_SETUP.format(func="pearson_residual_plot_static") + '''
ax = pearson_residual_plot_static(responded, prob, family="binomial",
                                  title="Clinical Trial Dose-Response: Pearson Residuals",
                                  color="#d62728")
plt.show()''')

EXAMPLES["dataviz.regression.glm.pearson_residual_plot_interactive"] = (
    _GLM_BINOMIAL_SETUP.format(func="pearson_residual_plot_interactive") + '''
fig = pearson_residual_plot_interactive(
    responded, prob, family="binomial",
    title="Clinical Trial Dose-Response: Pearson Residuals",
    template="plotly_white")
fig.show()''')

EXAMPLES["dataviz.regression.glm.working_residual_plot_static"] = (
    _GLM_BINOMIAL_SETUP.format(func="working_residual_plot_static") + '''
ax = working_residual_plot_static(responded, prob, link="logit",
                                  title="Clinical Trial Dose-Response: Working Residuals",
                                  color="#9467bd")
plt.show()''')

EXAMPLES["dataviz.regression.glm.working_residual_plot_interactive"] = (
    _GLM_BINOMIAL_SETUP.format(func="working_residual_plot_interactive") + '''
fig = working_residual_plot_interactive(
    responded, prob, link="logit",
    title="Clinical Trial Dose-Response: Working Residuals",
    template="plotly_white")
fig.show()''')

_VARIANCE_SETUP = '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.glm import {func}

rng = np.random.default_rng(42)
mu_grid = pd.Series(np.exp(np.linspace(np.log(0.5), np.log(25.0), 30)),
                    name="mean_defect_count")
'''

EXAMPLES["dataviz.regression.glm.variance_function_plot_static"] = (
    _VARIANCE_SETUP.format(func="variance_function_plot_static") + '''
ax = variance_function_plot_static(mu_grid, family="poisson",
                                   title="Defect Count Model: Poisson Variance Function",
                                   color="#8c564b")
ax.set_ylabel("V(mu)")
plt.show()''')

EXAMPLES["dataviz.regression.glm.variance_function_plot_interactive"] = (
    _VARIANCE_SETUP.format(func="variance_function_plot_interactive") + '''
fig = variance_function_plot_interactive(
    mu_grid, family="poisson",
    title="Defect Count Model: Poisson Variance Function",
    template="plotly_white")
fig.show()''')

EXAMPLES["dataviz.regression.glm.glm_diagnostic_panel_static"] = (
    _GLM_POISSON_SETUP.format(func="glm_diagnostic_panel_static") + '''
fig = glm_diagnostic_panel_static(claims, mu, family="poisson", link="log",
                                  title="Auto Insurance Claims GLM: Diagnostic Panel")
plt.show()''')

EXAMPLES["dataviz.regression.glm.glm_diagnostic_panel_interactive"] = (
    _GLM_POISSON_SETUP.format(func="glm_diagnostic_panel_interactive") + '''
fig = glm_diagnostic_panel_interactive(
    claims, mu, family="poisson", link="log",
    title="Auto Insurance Claims GLM: Diagnostic Panel",
    template="plotly_white")
fig.show()''')

# ---------------------------------------------------------------------------
# gof.py (12 members)
# ---------------------------------------------------------------------------

_GOF_RESID_SETUP = '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.gof import {func}

rng = np.random.default_rng(42)
n = 40
square_feet = rng.uniform(800.0, 4000.0, n)
bedrooms = rng.integers(1, 6, n).astype(float)
X = pd.DataFrame({{"square_feet": square_feet, "bedrooms": bedrooms}})
price = 50.0 + 0.15 * square_feet + 12.0 * bedrooms
residuals = pd.Series(rng.normal(0.0, 18.0, n), name="price_residuals_kusd")
'''

EXAMPLES["dataviz.regression.gof.normality_test_panel_static"] = (
    _GOF_RESID_SETUP.format(func="normality_test_panel_static") + '''
fig = normality_test_panel_static(residuals,
                                  title="Housing Price Model: Residual Normality",
                                  bins=20, color="#1f77b4")
plt.show()''')

EXAMPLES["dataviz.regression.gof.normality_test_panel_interactive"] = (
    _GOF_RESID_SETUP.format(func="normality_test_panel_interactive") + '''
fig = normality_test_panel_interactive(
    residuals, title="Housing Price Model: Residual Normality",
    nbins=20, template="plotly_white")
fig.show()''')

_HETERO_SETUP = '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.gof import {func}

rng = np.random.default_rng(42)
n = 36
machine_speed = rng.uniform(200.0, 900.0, n)
tool_age_hrs = rng.uniform(10.0, 500.0, n)
X = pd.DataFrame({{"machine_speed_rpm": machine_speed,
                   "tool_age_hrs": tool_age_hrs}})
residuals = pd.Series(rng.normal(0.0, 0.5 + 0.002 * machine_speed, n),
                      name="roughness_residuals_um")
'''

EXAMPLES["dataviz.regression.gof.breusch_pagan_plot_static"] = (
    _HETERO_SETUP.format(func="breusch_pagan_plot_static") + '''
ax = breusch_pagan_plot_static(X, residuals,
                               title="Milling Line: Breusch-Pagan Test",
                               color="#d62728")
ax.set_ylabel("Squared residual")
plt.show()''')

EXAMPLES["dataviz.regression.gof.breusch_pagan_plot_interactive"] = (
    _HETERO_SETUP.format(func="breusch_pagan_plot_interactive") + '''
fig = breusch_pagan_plot_interactive(X, residuals,
                                     title="Milling Line: Breusch-Pagan Test",
                                     template="plotly_white")
fig.show()''')

EXAMPLES["dataviz.regression.gof.white_test_plot_static"] = (
    _HETERO_SETUP.format(func="white_test_plot_static") + '''
ax = white_test_plot_static(X, residuals,
                            title="Milling Line: White Heteroscedasticity Test",
                            color="#ff7f0e")
ax.set_ylabel("Squared residual")
plt.show()''')

EXAMPLES["dataviz.regression.gof.white_test_plot_interactive"] = (
    _HETERO_SETUP.format(func="white_test_plot_interactive") + '''
fig = white_test_plot_interactive(X, residuals,
                                  title="Milling Line: White Heteroscedasticity Test",
                                  template="plotly_white")
fig.show()''')

_AUTOCORR_SETUP = '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.gof import {func}

rng = np.random.default_rng(42)
n = 30
noise = rng.normal(0.0, 1.0, n)
residuals = pd.Series(
    np.array([noise[0]] + [0.6 * noise[i - 1] + noise[i] for i in range(1, n)]),
    index=pd.date_range("2025-04-01", periods=n, freq="D"),
    name="daily_yield_residuals")
'''

EXAMPLES["dataviz.regression.gof.durbin_watson_gauge_static"] = (
    _AUTOCORR_SETUP.format(func="durbin_watson_gauge_static") + '''
ax = durbin_watson_gauge_static(residuals,
                                title="Crop Yield Model: Durbin-Watson Gauge",
                                color="#d62728")
plt.show()''')

EXAMPLES["dataviz.regression.gof.durbin_watson_gauge_interactive"] = (
    _AUTOCORR_SETUP.format(func="durbin_watson_gauge_interactive") + '''
fig = durbin_watson_gauge_interactive(
    residuals, title="Crop Yield Model: Durbin-Watson Gauge",
    template="plotly_white")
fig.show()''')

EXAMPLES["dataviz.regression.gof.ljung_box_plot_static"] = (
    _AUTOCORR_SETUP.format(func="ljung_box_plot_static") + '''
ax = ljung_box_plot_static(residuals, lags=12, alpha=0.05,
                           title="Crop Yield Model: Ljung-Box p-values",
                           color="#2ca02c")
plt.show()''')

EXAMPLES["dataviz.regression.gof.ljung_box_plot_interactive"] = (
    _AUTOCORR_SETUP.format(func="ljung_box_plot_interactive") + '''
fig = ljung_box_plot_interactive(residuals, lags=12, alpha=0.05,
                                 title="Crop Yield Model: Ljung-Box p-values",
                                 template="plotly_white")
fig.show()''')

EXAMPLES["dataviz.regression.gof.residual_dependence_test_panel_static"] = (
    _HETERO_SETUP.format(func="residual_dependence_test_panel_static") + '''
fig = residual_dependence_test_panel_static(
    X, residuals, title="Milling Line: Residual Dependence Test Panel")
plt.show()''')

EXAMPLES["dataviz.regression.gof.residual_dependence_test_panel_interactive"] = (
    _HETERO_SETUP.format(func="residual_dependence_test_panel_interactive") + '''
fig = residual_dependence_test_panel_interactive(
    X, residuals, title="Milling Line: Residual Dependence Test Panel",
    template="plotly_white")
fig.show()''')

# ---------------------------------------------------------------------------
# helpers.py (19 members)
# ---------------------------------------------------------------------------

_REGDATA_SETUP = '''import numpy as np
import pandas as pd
from dataviz.regression.helpers import {func}

rng = np.random.default_rng(42)
n = 30
square_feet = rng.uniform(900.0, 3500.0, n)
bedrooms = rng.integers(1, 6, n).astype(float)
age_years = rng.uniform(0.0, 40.0, n)
X = pd.DataFrame({{"square_feet": square_feet, "bedrooms": bedrooms,
                   "age_years": age_years}})
y = pd.Series(60.0 + 0.16 * square_feet + 10.0 * bedrooms - 0.8 * age_years
              + rng.normal(0.0, 15.0, n), name="price_kusd")
'''

EXAMPLES["dataviz.regression.helpers.RegressionMetrics"] = _REGDATA_SETUP.format(
    func="RegressionMetrics") + '''
result = RegressionMetrics(
    n=n, mae=11.2, mse=198.4, rmse=14.1, medae=9.3, mape=4.1, smape=4.0,
    r2=0.93, adj_r2=0.92, explained_variance=0.93, max_error=41.7)
print(result)
print(result.as_dict()["rmse"])'''

EXAMPLES["dataviz.regression.helpers.InfluenceStatistics"] = _REGDATA_SETUP.format(
    func="InfluenceStatistics") + '''
result = InfluenceStatistics(
    leverage=np.full(n, 2.0 / n), residuals=rng.normal(0.0, 10.0, n),
    standardized_residuals=rng.normal(0.0, 1.0, n),
    studentized_residuals=rng.normal(0.0, 1.0, n),
    cooks_distance=np.abs(rng.normal(0.0, 0.05, n)),
    dffits=rng.normal(0.0, 0.3, n),
    dfbetas=rng.normal(0.0, 0.2, (n, 4)),
    sigma_hat=12.4, n_features=3)
print(result)'''

EXAMPLES["dataviz.regression.helpers.compute_regression_metrics"] = (
    _REGDATA_SETUP.format(func="compute_regression_metrics") + '''
y_pred = 60.0 + 0.16 * square_feet + 10.0 * bedrooms - 0.8 * age_years
result = compute_regression_metrics(y, y_pred, n_features=3)
print(result)''')

EXAMPLES["dataviz.regression.helpers.influence_statistics"] = _REGDATA_SETUP.format(
    func="influence_statistics") + '''
y_pred = 60.0 + 0.16 * square_feet + 10.0 * bedrooms - 0.8 * age_years
result = influence_statistics(X, y, y_pred, include_intercept=True)
print(result.n_features)
print(result.cooks_distance.round(4))'''

EXAMPLES["dataviz.regression.helpers.prediction_intervals"] = _REGDATA_SETUP.format(
    func="prediction_intervals") + '''
y_pred = 60.0 + 0.16 * square_feet + 10.0 * bedrooms - 0.8 * age_years
residuals = y - y_pred
result = prediction_intervals(y_pred, residuals, confidence=0.90,
                              method="empirical")
print(result)'''

EXAMPLES["dataviz.regression.helpers.coefficient_table"] = _REGDATA_SETUP.format(
    func="coefficient_table") + '''
result = coefficient_table(X, y, feature_names=list(X.columns),
                           include_intercept=True)
print(result.round(3))'''

_SERIES_SETUP = '''import numpy as np
import pandas as pd
from dataviz.regression.helpers import {func}

rng = np.random.default_rng(42)
noise = rng.normal(0.0, 1.0, 30)
residuals = pd.Series(
    np.array([noise[0]] + [0.55 * noise[i - 1] + noise[i] for i in range(1, 30)]),
    index=pd.date_range("2025-01-01", periods=30, freq="D"),
    name="streamflow_residuals")
'''

EXAMPLES["dataviz.regression.helpers.autocorrelation"] = _SERIES_SETUP.format(
    func="autocorrelation") + '''
result = autocorrelation(residuals, max_lag=10)
print(result.round(3))'''

EXAMPLES["dataviz.regression.helpers.partial_autocorrelation"] = (
    _SERIES_SETUP.format(func="partial_autocorrelation") + '''
result = partial_autocorrelation(residuals, max_lag=10)
print(result.round(3))''')

EXAMPLES["dataviz.regression.helpers.runs_test_signs"] = _SERIES_SETUP.format(
    func="runs_test_signs") + '''
runs, n_pos, n_neg = runs_test_signs(residuals)
print(f"runs={runs}, positive={n_pos}, negative={n_neg}")'''

EXAMPLES["dataviz.regression.helpers.variance_inflation_factors"] = (
    _REGDATA_SETUP.format(func="variance_inflation_factors") + '''
X["lot_size_sqft"] = X["square_feet"] * 2.5 + rng.normal(0.0, 100.0, n)
result = variance_inflation_factors(X, include_intercept=True)
print(pd.Series(result.round(2), index=X.columns, name="vif"))''')

EXAMPLES["dataviz.regression.helpers.breusch_pagan_statistic"] = (
    _REGDATA_SETUP.format(func="breusch_pagan_statistic") + '''
y_pred = 60.0 + 0.16 * square_feet + 10.0 * bedrooms - 0.8 * age_years
residuals = y - y_pred + square_feet / 500.0
result = breusch_pagan_statistic(X, residuals)
print(f"LM={result[0]:.3f}, p-value={result[1]:.4f}")''')

EXAMPLES["dataviz.regression.helpers.white_test_statistic"] = _REGDATA_SETUP.format(
    func="white_test_statistic") + '''
y_pred = 60.0 + 0.16 * square_feet + 10.0 * bedrooms - 0.8 * age_years
residuals = y - y_pred + square_feet / 500.0
result = white_test_statistic(X, residuals)
print(f"LM={result[0]:.3f}, p-value={result[1]:.4f}")'''

EXAMPLES["dataviz.regression.helpers.ljung_box_statistic"] = _SERIES_SETUP.format(
    func="ljung_box_statistic") + '''
result = ljung_box_statistic(residuals, lags=8)
print(f"Q={result[0]:.3f}, p-value={result[1]:.4f}")'''

EXAMPLES["dataviz.regression.helpers.jarque_bera_statistic"] = _SERIES_SETUP.format(
    func="jarque_bera_statistic") + '''
result = jarque_bera_statistic(residuals)
print(f"JB={result[0]:.3f}, p-value={result[1]:.4f}")'''

EXAMPLES["dataviz.regression.helpers.durbin_watson_statistic"] = (
    _SERIES_SETUP.format(func="durbin_watson_statistic") + '''
result = durbin_watson_statistic(residuals)
print(f"DW={result:.3f}")''')

_TRANSFORM_SETUP = '''import numpy as np
import pandas as pd
from dataviz.regression.helpers import {func}

rng = np.random.default_rng(42)
hospital_stay_days = pd.Series(rng.gamma(2.0, 2.5, 40) + 0.5,
                               name="length_of_stay_days")
lambdas = np.linspace(-2.0, 2.0, 25)
'''

EXAMPLES["dataviz.regression.helpers.box_cox_loglikelihood"] = (
    _TRANSFORM_SETUP.format(func="box_cox_loglikelihood") + '''
loglik = box_cox_loglikelihood(hospital_stay_days, lambdas)
best = lambdas[int(np.argmax(loglik))]
print(f"best lambda: {best:.2f}")''')

EXAMPLES["dataviz.regression.helpers.yeo_johnson_loglikelihood"] = (
    _TRANSFORM_SETUP.format(func="yeo_johnson_loglikelihood") + '''
centered = hospital_stay_days - hospital_stay_days.median()
loglik = yeo_johnson_loglikelihood(centered, lambdas)
best = lambdas[int(np.argmax(loglik))]
print(f"best lambda: {best:.2f}")''')

EXAMPLES["dataviz.regression.helpers.conformal_quantile"] = '''import numpy as np
import pandas as pd
from dataviz.regression.helpers import conformal_quantile

rng = np.random.default_rng(42)
calibration_residuals = pd.Series(rng.normal(0.0, 2.5, 30),
                                  name="calibration_residuals_ppm")
q90 = conformal_quantile(calibration_residuals, alpha=0.1)
print(f"90% conformal half-width: {q90:.3f} ppm")'''

EXAMPLES["dataviz.regression.helpers.jackknife_plus_intervals"] = '''import numpy as np
import pandas as pd
from dataviz.regression.helpers import jackknife_plus_intervals

rng = np.random.default_rng(42)
n_cal, n_test = 25, 6
y_calibration = pd.Series(rng.normal(70.0, 8.0, n_cal), name="yield_kg")
loo_predictions = (y_calibration.to_numpy()[:, None]
                   + rng.normal(0.0, 1.5, (n_cal, n_test)))
new_predictions = pd.Series(rng.normal(70.0, 2.0, n_test), name="plot_forecast")
lower, upper = jackknife_plus_intervals(loo_predictions, y_calibration,
                                        new_predictions, alpha=0.1)
print(pd.DataFrame({"lower": lower.round(2), "upper": upper.round(2)}))'''

# ---------------------------------------------------------------------------
# importance.py (4 members)
# ---------------------------------------------------------------------------

_IMP_SETUP = '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.importance import {func}

feature_names = ["ram_gb", "storage_gb", "screen_inches", "battery_mah",
                 "weight_g", "camera_mp", "age_months"]
importances = pd.Series([0.34, 0.22, 0.15, 0.11, 0.08, 0.06, 0.04],
                        index=feature_names, name="rf_importance")
'''

EXAMPLES["dataviz.regression.importance.feature_importance_regression_static"] = (
    _IMP_SETUP.format(func="feature_importance_regression_static") + '''
ax = feature_importance_regression_static(
    importances, feature_names=feature_names, top_n=6,
    title="Used Phone Price Model: Feature Importance",
    color="#1f77b4")
ax.set_xlabel("Gini importance")
plt.show()''')

EXAMPLES["dataviz.regression.importance.feature_importance_regression_interactive"] = (
    _IMP_SETUP.format(func="feature_importance_regression_interactive") + '''
fig = feature_importance_regression_interactive(
    importances, feature_names=feature_names, top_n=6,
    title="Used Phone Price Model: Feature Importance",
    template="plotly_white")
fig.show()''')

_PERM_SETUP = '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.importance import {func}

feature_names = ["dose_mg", "bmi", "age_years", "systolic_bp", "smoker"]
perm_mean = pd.Series([0.28, 0.19, 0.12, 0.07, 0.03], index=feature_names,
                      name="perm_importance_mean")
perm_std = pd.Series([0.04, 0.03, 0.03, 0.02, 0.01], index=feature_names,
                     name="perm_importance_std")
'''

EXAMPLES["dataviz.regression.importance.permutation_importance_regression_static"] = (
    _PERM_SETUP.format(func="permutation_importance_regression_static") + '''
ax = permutation_importance_regression_static(
    perm_mean, perm_std, feature_names=feature_names,
    title="Clinical Outcome Model: Permutation Importance (20 repeats)",
    color="#2ca02c", error_color="#444444")
ax.set_xlabel("Decrease in CV R-squared")
plt.show()''')

EXAMPLES["dataviz.regression.importance.permutation_importance_regression_interactive"] = (
    _PERM_SETUP.format(func="permutation_importance_regression_interactive") + '''
fig = permutation_importance_regression_interactive(
    perm_mean, perm_std, feature_names=feature_names,
    title="Clinical Outcome Model: Permutation Importance (20 repeats)",
    color="#2ca02c", template="plotly_white")
fig.show()''')

# ---------------------------------------------------------------------------
# influence.py (8 members)
# ---------------------------------------------------------------------------

_INFLUENCE_SETUP = '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.influence import {func}

rng = np.random.default_rng(42)
n = 28
ad_spend = rng.uniform(5.0, 60.0, n)
store_traffic = rng.uniform(100.0, 900.0, n)
X = pd.DataFrame({{"ad_spend_kusd": ad_spend,
                   "store_traffic_daily": store_traffic}})
X.loc[27, "ad_spend_kusd"] = 95.0  # an outlier campaign week
y = pd.Series(20.0 + 1.8 * ad_spend + 0.05 * store_traffic
              + rng.normal(0.0, 6.0, n), name="weekly_revenue_kusd")
y.iloc[27] = 260.0
beta = np.linalg.lstsq(np.column_stack([np.ones(n), X]), y, rcond=None)[0]
y_pred = np.column_stack([np.ones(n), X]) @ beta
'''

EXAMPLES["dataviz.regression.influence.leverage_plot_static"] = (
    _INFLUENCE_SETUP.format(func="leverage_plot_static") + '''
ax = leverage_plot_static(X, y, y_pred,
                          title="Marketing Mix Model: Leverage by Week",
                          threshold_multiplier=2.0, color="#1f77b4")
plt.show()''')

EXAMPLES["dataviz.regression.influence.leverage_plot_interactive"] = (
    _INFLUENCE_SETUP.format(func="leverage_plot_interactive") + '''
fig = leverage_plot_interactive(X, y, y_pred,
                                title="Marketing Mix Model: Leverage by Week",
                                template="plotly_white")
fig.show()''')

EXAMPLES["dataviz.regression.influence.cooks_distance_plot_static"] = (
    _INFLUENCE_SETUP.format(func="cooks_distance_plot_static") + '''
ax = cooks_distance_plot_static(X, y, y_pred,
                                title="Marketing Mix Model: Cook's Distance",
                                color="#d62728")
plt.show()''')

EXAMPLES["dataviz.regression.influence.cooks_distance_plot_interactive"] = (
    _INFLUENCE_SETUP.format(func="cooks_distance_plot_interactive") + '''
fig = cooks_distance_plot_interactive(
    X, y, y_pred, title="Marketing Mix Model: Cook's Distance",
    template="plotly_white")
fig.show()''')

EXAMPLES["dataviz.regression.influence.influence_bubble_plot_static"] = (
    _INFLUENCE_SETUP.format(func="influence_bubble_plot_static") + '''
ax = influence_bubble_plot_static(X, y, y_pred,
                                  title="Marketing Mix Model: Influence Bubble Plot",
                                  cmap="viridis", marker_min=30, marker_max=350)
plt.show()''')

EXAMPLES["dataviz.regression.influence.influence_bubble_plot_interactive"] = (
    _INFLUENCE_SETUP.format(func="influence_bubble_plot_interactive") + '''
fig = influence_bubble_plot_interactive(
    X, y, y_pred, title="Marketing Mix Model: Influence Bubble Plot",
    colorscale="Viridis", template="plotly_white")
fig.show()''')

EXAMPLES["dataviz.regression.influence.dfbetas_plot_static"] = (
    _INFLUENCE_SETUP.format(func="dfbetas_plot_static") + '''
ax = dfbetas_plot_static(X, y, y_pred, feature_names=list(X.columns),
                         title="Marketing Mix Model: DFBETAS Heatmap",
                         cmap="coolwarm")
plt.show()''')

EXAMPLES["dataviz.regression.influence.dfbetas_plot_interactive"] = (
    _INFLUENCE_SETUP.format(func="dfbetas_plot_interactive") + '''
fig = dfbetas_plot_interactive(X, y, y_pred, feature_names=list(X.columns),
                               title="Marketing Mix Model: DFBETAS Heatmap",
                               colorscale="RdBu", template="plotly_white")
fig.show()''')

# ---------------------------------------------------------------------------
# learning.py (2 members)
# ---------------------------------------------------------------------------

_LEARNING_SETUP = '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.learning import {func}

rng = np.random.default_rng(42)
train_sizes = np.array([20, 40, 60, 80, 100, 120, 150, 180])
train_scores = pd.Series(0.99 - 0.10 * np.sqrt(train_sizes / 180.0)
                         + rng.normal(0, 0.005, 8), name="train_r2")
val_scores = pd.Series(0.55 + 0.35 * (1.0 - np.exp(-train_sizes / 70.0))
                       + rng.normal(0, 0.01, 8), name="cv_r2")
'''

EXAMPLES["dataviz.regression.learning.learning_curve_static"] = (
    _LEARNING_SETUP.format(func="learning_curve_static") + '''
ax = learning_curve_static(train_sizes, train_scores, val_scores,
                           title="Concrete Strength Model: Learning Curve",
                           train_color="#1f77b4", val_color="#d62728",
                           marker_size=7)
ax.set_ylabel("R-squared")
plt.show()''')

EXAMPLES["dataviz.regression.learning.learning_curve_interactive"] = (
    _LEARNING_SETUP.format(func="learning_curve_interactive") + '''
fig = learning_curve_interactive(train_sizes, train_scores, val_scores,
                                 title="Concrete Strength Model: Learning Curve",
                                 train_color="#1f77b4", val_color="#d62728",
                                 template="plotly_white")
fig.show()''')

# ---------------------------------------------------------------------------
# metrics.py (8 members)
# ---------------------------------------------------------------------------

_METRICS_SETUP = '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.metrics import {func}
from dataviz.regression.helpers import compute_regression_metrics

rng = np.random.default_rng(42)
n = 30
sqft = rng.uniform(900.0, 3500.0, n)
y = pd.Series(60.0 + 0.16 * sqft + rng.normal(0.0, 12.0, n), name="price_kusd")
pred_ols = pd.Series(60.0 + 0.16 * sqft + rng.normal(0.0, 8.0, n),
                     name="ols_pred")
pred_ridge = pd.Series(62.0 + 0.15 * sqft + rng.normal(0.0, 10.0, n),
                       name="ridge_pred")
pred_gbm = pd.Series(61.0 + 0.16 * sqft + rng.normal(0.0, 6.0, n),
                     name="gbm_pred")
model_metrics = {{
    "OLS": compute_regression_metrics(y, pred_ols).as_dict(),
    "Ridge": compute_regression_metrics(y, pred_ridge).as_dict(),
    "GBM": compute_regression_metrics(y, pred_gbm).as_dict(),
}}
'''

EXAMPLES["dataviz.regression.metrics.regression_metrics_bar_static"] = (
    _METRICS_SETUP.format(func="regression_metrics_bar_static") + '''
ax = regression_metrics_bar_static(y, pred_gbm,
                                   metrics=("mae", "rmse", "medae", "r2"),
                                   title="Housing Price GBM: Test Metrics",
                                   color="#1f77b4")
plt.show()''')

EXAMPLES["dataviz.regression.metrics.regression_metrics_bar_interactive"] = (
    _METRICS_SETUP.format(func="regression_metrics_bar_interactive") + '''
fig = regression_metrics_bar_interactive(
    y, pred_gbm, metrics=("mae", "rmse", "medae", "r2"),
    title="Housing Price GBM: Test Metrics", template="plotly_white")
fig.show()''')

EXAMPLES["dataviz.regression.metrics.metric_comparison_bar_static"] = (
    _METRICS_SETUP.format(func="metric_comparison_bar_static") + '''
ax = metric_comparison_bar_static(model_metrics, metrics=("mae", "rmse", "r2"),
                                  title="Housing Price Models: Metric Comparison",
                                  cmap="tab10")
plt.show()''')

EXAMPLES["dataviz.regression.metrics.metric_comparison_bar_interactive"] = (
    _METRICS_SETUP.format(func="metric_comparison_bar_interactive") + '''
fig = metric_comparison_bar_interactive(
    model_metrics, metrics=("mae", "rmse", "r2"),
    title="Housing Price Models: Metric Comparison", template="plotly_white")
fig.show()''')

EXAMPLES["dataviz.regression.metrics.metric_radar_static"] = _METRICS_SETUP.format(
    func="metric_radar_static") + '''
ax = metric_radar_static(
    model_metrics, metrics=("mae", "rmse", "medae", "r2", "explained_variance"),
    title="Housing Price Models: Metric Radar", fill_alpha=0.20)
plt.show()'''

EXAMPLES["dataviz.regression.metrics.metric_radar_interactive"] = (
    _METRICS_SETUP.format(func="metric_radar_interactive") + '''
fig = metric_radar_interactive(
    model_metrics, metrics=("mae", "rmse", "medae", "r2", "explained_variance"),
    title="Housing Price Models: Metric Radar", template="plotly_white")
fig.show()''')

_SEGMENT_SETUP = '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.metrics import {func}

rng = np.random.default_rng(42)
n = 24
segments = pd.Series(np.repeat(["urban", "suburban", "rural"], 8),
                     name="store_region")
y = pd.Series(100.0 + rng.normal(0.0, 15.0, n), name="monthly_sales_kusd")
y_pred = y - rng.normal(0.0, 6.0, n) + np.where(segments == "rural", 8.0, 0.0)
'''

EXAMPLES["dataviz.regression.metrics.per_segment_metrics_heatmap_static"] = (
    _SEGMENT_SETUP.format(func="per_segment_metrics_heatmap_static") + '''
ax = per_segment_metrics_heatmap_static(
    y, y_pred, segments, metrics=("mae", "rmse", "r2"),
    title="Retail Sales Model: Metrics by Region", cmap="viridis")
plt.show()''')

EXAMPLES["dataviz.regression.metrics.per_segment_metrics_heatmap_interactive"] = (
    _SEGMENT_SETUP.format(func="per_segment_metrics_heatmap_interactive") + '''
fig = per_segment_metrics_heatmap_interactive(
    y, y_pred, segments, metrics=("mae", "rmse", "r2"),
    title="Retail Sales Model: Metrics by Region",
    colorscale="Viridis", template="plotly_white")
fig.show()''')
