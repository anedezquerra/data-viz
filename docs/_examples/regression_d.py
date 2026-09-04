"""Curated rich examples for regression member pages."""

EXAMPLES = {
    # ------------------------------------------------------------------
    # residual_features
    # ------------------------------------------------------------------
    "dataviz.regression.residual_features.residual_vs_feature_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.residual_features import residual_vs_feature_static

rng = np.random.default_rng(42)
n = 40
listings = pd.DataFrame({
    "sqft": rng.uniform(800, 3600, n),
})
noise = rng.normal(0, 18, n)
price = 60 + 0.22 * listings["sqft"] + 0.00003 * listings["sqft"] ** 2 + noise
y_pred = 70 + 0.26 * listings["sqft"]  # linear model misses curvature

ax = residual_vs_feature_static(
    listings["sqft"], price, y_pred,
    feature_name="Living area (sqft)",
    title="Home pricing model: residuals vs living area",
    trend_color="#e45756",
)
ax.set_xlabel("Living area (sqft)")
plt.show()''',
    "dataviz.regression.residual_features.residual_vs_feature_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.residual_features import residual_vs_feature_interactive

rng = np.random.default_rng(42)
n = 40
listings = pd.DataFrame({
    "sqft": rng.uniform(800, 3600, n),
})
noise = rng.normal(0, 18, n)
price = 60 + 0.22 * listings["sqft"] + 0.00003 * listings["sqft"] ** 2 + noise
y_pred = 70 + 0.26 * listings["sqft"]  # linear model misses curvature

fig = residual_vs_feature_interactive(
    listings["sqft"], price, y_pred,
    feature_name="Living area (sqft)",
    title="Home pricing model: residuals vs living area",
    trend_color="#e45756",
)
fig.show()''',
    "dataviz.regression.residual_features.partial_residual_plot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.residual_features import partial_residual_plot_static

rng = np.random.default_rng(42)
n = 35
cars = pd.DataFrame({
    "horsepower": rng.uniform(90, 320, n),
    "weight_kg": rng.uniform(900, 2100, n),
    "age_years": rng.uniform(0, 12, n),
})
mpg = (52 - 0.045 * cars["horsepower"] - 0.008 * cars["weight_kg"]
       - 0.6 * cars["age_years"] + rng.normal(0, 1.5, n))

ax = partial_residual_plot_static(
    cars, mpg, feature_index=0, feature_name="horsepower",
    title="Fuel economy study: partial residual for horsepower",
)
plt.show()''',
    "dataviz.regression.residual_features.partial_residual_plot_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.residual_features import partial_residual_plot_interactive

rng = np.random.default_rng(42)
n = 35
cars = pd.DataFrame({
    "horsepower": rng.uniform(90, 320, n),
    "weight_kg": rng.uniform(900, 2100, n),
    "age_years": rng.uniform(0, 12, n),
})
mpg = (52 - 0.045 * cars["horsepower"] - 0.008 * cars["weight_kg"]
       - 0.6 * cars["age_years"] + rng.normal(0, 1.5, n))

fig = partial_residual_plot_interactive(
    cars, mpg, feature_index=0, feature_name="horsepower",
    title="Fuel economy study: partial residual for horsepower",
)
fig.show()''',
    "dataviz.regression.residual_features.ccpr_plot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.residual_features import ccpr_plot_static

rng = np.random.default_rng(42)
n = 35
cars = pd.DataFrame({
    "horsepower": rng.uniform(90, 320, n),
    "weight_kg": rng.uniform(900, 2100, n),
    "age_years": rng.uniform(0, 12, n),
})
mpg = (52 - 0.045 * cars["horsepower"] - 0.008 * cars["weight_kg"]
       - 0.6 * cars["age_years"] + rng.normal(0, 1.5, n))

ax = ccpr_plot_static(
    cars, mpg, feature_index=1, feature_name="weight_kg",
    title="Fuel economy study: CCPR for vehicle weight",
)
ax.set_ylabel("Component + residual (mpg)")
plt.show()''',
    "dataviz.regression.residual_features.ccpr_plot_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.residual_features import ccpr_plot_interactive

rng = np.random.default_rng(42)
n = 35
cars = pd.DataFrame({
    "horsepower": rng.uniform(90, 320, n),
    "weight_kg": rng.uniform(900, 2100, n),
    "age_years": rng.uniform(0, 12, n),
})
mpg = (52 - 0.045 * cars["horsepower"] - 0.008 * cars["weight_kg"]
       - 0.6 * cars["age_years"] + rng.normal(0, 1.5, n))

fig = ccpr_plot_interactive(
    cars, mpg, feature_index=1, feature_name="weight_kg",
    title="Fuel economy study: CCPR for vehicle weight",
)
fig.show()''',
    "dataviz.regression.residual_features.added_variable_plot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.residual_features import added_variable_plot_static

rng = np.random.default_rng(42)
n = 35
cars = pd.DataFrame({
    "horsepower": rng.uniform(90, 320, n),
    "weight_kg": rng.uniform(900, 2100, n),
    "age_years": rng.uniform(0, 12, n),
})
mpg = (52 - 0.045 * cars["horsepower"] - 0.008 * cars["weight_kg"]
       - 0.6 * cars["age_years"] + rng.normal(0, 1.5, n))

ax = added_variable_plot_static(
    cars, mpg, feature_index=2, feature_name="age_years",
    title="Fuel economy study: added-variable plot for car age",
)
plt.show()''',
    "dataviz.regression.residual_features.added_variable_plot_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.residual_features import added_variable_plot_interactive

rng = np.random.default_rng(42)
n = 35
cars = pd.DataFrame({
    "horsepower": rng.uniform(90, 320, n),
    "weight_kg": rng.uniform(900, 2100, n),
    "age_years": rng.uniform(0, 12, n),
})
mpg = (52 - 0.045 * cars["horsepower"] - 0.008 * cars["weight_kg"]
       - 0.6 * cars["age_years"] + rng.normal(0, 1.5, n))

fig = added_variable_plot_interactive(
    cars, mpg, feature_index=2, feature_name="age_years",
    title="Fuel economy study: added-variable plot for car age",
)
fig.show()''',

    # ------------------------------------------------------------------
    # selection
    # ------------------------------------------------------------------
    "dataviz.regression.selection.aic_bic_bar_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.selection import aic_bic_bar_static

models = ["Linear", "Quadratic", "Cubic", "Log terms", "Full kitchen-sink"]
aic = np.array([412.3, 388.1, 390.6, 381.4, 397.9])
bic = aic + np.array([6.2, 6.2, 9.4, 9.4, 15.7])

ax = aic_bic_bar_static(
    models, aic, bic,
    title="Yield-curve regressors: AIC vs BIC per candidate model",
)
plt.show()''',
    "dataviz.regression.selection.aic_bic_bar_interactive": '''import numpy as np
from dataviz.regression.selection import aic_bic_bar_interactive

models = ["Linear", "Quadratic", "Cubic", "Log terms", "Full kitchen-sink"]
aic = np.array([412.3, 388.1, 390.6, 381.4, 397.9])
bic = aic + np.array([6.2, 6.2, 9.4, 9.4, 15.7])

fig = aic_bic_bar_interactive(
    models, aic, bic,
    title="Yield-curve regressors: AIC vs BIC per candidate model",
)
fig.show()''',
    "dataviz.regression.selection.nested_model_comparison_plot_static": '''import matplotlib.pyplot as plt
from dataviz.regression.selection import nested_model_comparison_plot_static

models = ["Intercept", "+ temp", "+ pressure", "+ catalyst", "+ temp:pressure"]
log_lik = [-128.4, -102.7, -88.9, -80.2, -79.6]
df_diff = [1, 1, 1, 1, 1]

ax = nested_model_comparison_plot_static(
    models, log_lik, df_diff=df_diff,
    title="Chemical reactor study: nested model log-likelihoods",
)
ax.axhline(-80.2, color="#888", linestyle=":", linewidth=1)
plt.show()''',
    "dataviz.regression.selection.nested_model_comparison_plot_interactive": '''from dataviz.regression.selection import nested_model_comparison_plot_interactive

models = ["Intercept", "+ temp", "+ pressure", "+ catalyst", "+ temp:pressure"]
log_lik = [-128.4, -102.7, -88.9, -80.2, -79.6]
df_diff = [1, 1, 1, 1, 1]

fig = nested_model_comparison_plot_interactive(
    models, log_lik, df_diff=df_diff,
    title="Chemical reactor study: nested model log-likelihoods",
)
fig.show()''',
    "dataviz.regression.selection.stepwise_selection_path_static": '''import matplotlib.pyplot as plt
from dataviz.regression.selection import stepwise_selection_path_static

steps = ["start", "+ sqft", "+ bedrooms", "+ age", "+ garage",
         "+ baths", "- bedrooms", "+ lot_size"]
cv_rmse = [95.2, 61.8, 55.4, 49.7, 47.3, 46.9, 45.8, 45.6]

ax = stepwise_selection_path_static(
    steps, cv_rmse, metric_name="CV RMSE (k$)",
    title="Housing price model: stepwise selection path",
)
plt.show()''',
    "dataviz.regression.selection.stepwise_selection_path_interactive": '''from dataviz.regression.selection import stepwise_selection_path_interactive

steps = ["start", "+ sqft", "+ bedrooms", "+ age", "+ garage",
         "+ baths", "- bedrooms", "+ lot_size"]
cv_rmse = [95.2, 61.8, 55.4, 49.7, 47.3, 46.9, 45.8, 45.6]

fig = stepwise_selection_path_interactive(
    steps, cv_rmse, metric_name="CV RMSE (k$)",
    title="Housing price model: stepwise selection path",
)
fig.show()''',
    "dataviz.regression.selection.forward_selection_score_curve_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.selection import forward_selection_score_curve_static

num_features = np.arange(1, 9)
adj_r2 = [0.42, 0.61, 0.70, 0.75, 0.78, 0.80, 0.807, 0.809]

ax = forward_selection_score_curve_static(
    num_features, adj_r2, metric_name="Adjusted R-squared",
    title="Bike-share demand: forward selection score curve",
)
plt.show()''',
    "dataviz.regression.selection.forward_selection_score_curve_interactive": '''import numpy as np
from dataviz.regression.selection import forward_selection_score_curve_interactive

num_features = np.arange(1, 9)
adj_r2 = [0.42, 0.61, 0.70, 0.75, 0.78, 0.80, 0.807, 0.809]

fig = forward_selection_score_curve_interactive(
    num_features, adj_r2, metric_name="Adjusted R-squared",
    title="Bike-share demand: forward selection score curve",
)
fig.show()''',
    "dataviz.regression.selection.best_subset_metric_bar_static": '''import matplotlib.pyplot as plt
from dataviz.regression.selection import best_subset_metric_bar_static

subsets = ["{temp}", "{temp, press}", "{temp, cat}", "{press, cat}",
           "{temp, press, cat}", "{all 5}"]
mallows_cp = [38.2, 12.5, 9.8, 21.4, 4.1, 6.0]

ax = best_subset_metric_bar_static(
    subsets, mallows_cp, metric_name="Mallows Cp",
    title="Reactor yield: best-subset search by Mallows Cp",
)
plt.show()''',
    "dataviz.regression.selection.best_subset_metric_bar_interactive": '''from dataviz.regression.selection import best_subset_metric_bar_interactive

subsets = ["{temp}", "{temp, press}", "{temp, cat}", "{press, cat}",
           "{temp, press, cat}", "{all 5}"]
mallows_cp = [38.2, 12.5, 9.8, 21.4, 4.1, 6.0]

fig = best_subset_metric_bar_interactive(
    subsets, mallows_cp, metric_name="Mallows Cp",
    title="Reactor yield: best-subset search by Mallows Cp",
)
fig.show()''',

    # ------------------------------------------------------------------
    # spatial
    # ------------------------------------------------------------------
    "dataviz.regression.spatial.spatial_residual_map_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.spatial import spatial_residual_map_static

rng = np.random.default_rng(42)
n = 45
lon = -104.99 + rng.uniform(-0.25, 0.25, n)   # Denver metro
lat = 39.74 + rng.uniform(-0.20, 0.20, n)
true_price = 320 + 180 * (lat - 39.74) + rng.normal(0, 25, n)
pred_price = 320 + 90 * (lat - 39.74)          # underfits the north-south gradient
residuals = true_price - pred_price

ax = spatial_residual_map_static(
    lon, lat, residuals, cmap="coolwarm",
    title="Denver housing model: geographic residual map (k$)",
)
plt.show()''',
    "dataviz.regression.spatial.spatial_residual_map_interactive": '''import numpy as np
from dataviz.regression.spatial import spatial_residual_map_interactive

rng = np.random.default_rng(42)
n = 45
lon = -104.99 + rng.uniform(-0.25, 0.25, n)   # Denver metro
lat = 39.74 + rng.uniform(-0.20, 0.20, n)
true_price = 320 + 180 * (lat - 39.74) + rng.normal(0, 25, n)
pred_price = 320 + 90 * (lat - 39.74)          # underfits the north-south gradient
residuals = true_price - pred_price

fig = spatial_residual_map_interactive(
    lon, lat, residuals, colorscale="RdBu",
    title="Denver housing model: geographic residual map (k$)",
)
fig.show()''',
    "dataviz.regression.spatial.moran_scatter_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.spatial import moran_scatter_static

rng = np.random.default_rng(42)
n = 48  # continental US states
base = rng.normal(0, 1, n)
unemployment = 4.5 + 1.2 * base + rng.normal(0, 0.4, n)
spatial_lag = 4.5 + 1.2 * (0.6 * base + 0.4 * rng.normal(0, 1, n))

ax = moran_scatter_static(
    unemployment, spatial_lag,
    title="State unemployment: Moran scatter of spatial autocorrelation",
)
plt.show()''',
    "dataviz.regression.spatial.moran_scatter_interactive": '''import numpy as np
from dataviz.regression.spatial import moran_scatter_interactive

rng = np.random.default_rng(42)
n = 48  # continental US states
base = rng.normal(0, 1, n)
unemployment = 4.5 + 1.2 * base + rng.normal(0, 0.4, n)
spatial_lag = 4.5 + 1.2 * (0.6 * base + 0.4 * rng.normal(0, 1, n))

fig = moran_scatter_interactive(
    unemployment, spatial_lag,
    title="State unemployment: Moran scatter of spatial autocorrelation",
)
fig.show()''',
    "dataviz.regression.spatial.panel_residual_heatmap_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.spatial import panel_residual_heatmap_static

rng = np.random.default_rng(42)
plants = ["Austin", "Boise", "Fresno", "Reno", "Tucson", "Tulsa"]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
resid = rng.normal(0, 1, (len(plants), len(months)))
resid[2, 6:9] += 3.0   # Fresno summer overheating episodes
resid[0, 0:2] -= 2.0   # Austin winter start-up issues

ax = panel_residual_heatmap_static(
    resid, unit_labels=plants, time_labels=months,
    title="Manufacturing line OEE model: panel residuals by plant and month",
)
plt.show()''',
    "dataviz.regression.spatial.panel_residual_heatmap_interactive": '''import numpy as np
from dataviz.regression.spatial import panel_residual_heatmap_interactive

rng = np.random.default_rng(42)
plants = ["Austin", "Boise", "Fresno", "Reno", "Tucson", "Tulsa"]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
resid = rng.normal(0, 1, (len(plants), len(months)))
resid[2, 6:9] += 3.0   # Fresno summer overheating episodes
resid[0, 0:2] -= 2.0   # Austin winter start-up issues

fig = panel_residual_heatmap_interactive(
    resid, unit_labels=plants, time_labels=months,
    title="Manufacturing line OEE model: panel residuals by plant and month",
)
fig.show()''',

    # ------------------------------------------------------------------
    # survival
    # ------------------------------------------------------------------
    "dataviz.regression.survival.km_predicted_vs_observed_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.survival import km_predicted_vs_observed_static

months = np.arange(0, 37, 3)
observed = np.array([1.00, 0.97, 0.93, 0.88, 0.82, 0.75, 0.68,
                     0.60, 0.53, 0.46, 0.39, 0.33, 0.27])
predicted = np.array([1.00, 0.96, 0.91, 0.85, 0.79, 0.72, 0.65,
                      0.58, 0.51, 0.44, 0.38, 0.32, 0.26])

ax = km_predicted_vs_observed_static(
    months, observed, predicted,
    title="Phase II oncology trial: KM observed vs Cox-predicted survival",
)
ax.set_xlabel("Months since randomization")
plt.show()''',
    "dataviz.regression.survival.km_predicted_vs_observed_interactive": '''import numpy as np
from dataviz.regression.survival import km_predicted_vs_observed_interactive

months = np.arange(0, 37, 3)
observed = np.array([1.00, 0.97, 0.93, 0.88, 0.82, 0.75, 0.68,
                     0.60, 0.53, 0.46, 0.39, 0.33, 0.27])
predicted = np.array([1.00, 0.96, 0.91, 0.85, 0.79, 0.72, 0.65,
                      0.58, 0.51, 0.44, 0.38, 0.32, 0.26])

fig = km_predicted_vs_observed_interactive(
    months, observed, predicted,
    title="Phase II oncology trial: KM observed vs Cox-predicted survival",
)
fig.show()''',
    "dataviz.regression.survival.cox_residual_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.survival import cox_residual_plot_static

rng = np.random.default_rng(42)
n = 40
follow_up = np.sort(rng.uniform(2, 60, n))  # months
martingale = rng.normal(0, 0.45, n).clip(-1.0, 1.0)
martingale[follow_up > 45] += 0.15          # mild lack of fit at long times

ax = cox_residual_plot_static(
    follow_up, martingale, kind="martingale",
    title="Cardiology cohort: Cox martingale residuals vs follow-up time",
)
plt.show()''',
    "dataviz.regression.survival.cox_residual_plot_interactive": '''import numpy as np
from dataviz.regression.survival import cox_residual_plot_interactive

rng = np.random.default_rng(42)
n = 40
follow_up = np.sort(rng.uniform(2, 60, n))  # months
martingale = rng.normal(0, 0.45, n).clip(-1.0, 1.0)
martingale[follow_up > 45] += 0.15          # mild lack of fit at long times

fig = cox_residual_plot_interactive(
    follow_up, martingale, kind="martingale",
    title="Cardiology cohort: Cox martingale residuals vs follow-up time",
)
fig.show()''',
    "dataviz.regression.survival.proportional_hazards_test_plot_static": '''import matplotlib.pyplot as plt
from dataviz.regression.survival import proportional_hazards_test_plot_static

covariates = ["age", "bmi", "smoker", "stage", "treatment", "sex"]
p_values = [0.62, 0.31, 0.08, 0.012, 0.44, 0.71]

ax = proportional_hazards_test_plot_static(
    covariates, p_values, alpha=0.05,
    title="Schoenfeld test of the proportional-hazards assumption",
)
plt.show()''',
    "dataviz.regression.survival.proportional_hazards_test_plot_interactive": '''from dataviz.regression.survival import proportional_hazards_test_plot_interactive

covariates = ["age", "bmi", "smoker", "stage", "treatment", "sex"]
p_values = [0.62, 0.31, 0.08, 0.012, 0.44, 0.71]

fig = proportional_hazards_test_plot_interactive(
    covariates, p_values, alpha=0.05,
    title="Schoenfeld test of the proportional-hazards assumption",
)
fig.show()''',

    # ------------------------------------------------------------------
    # transforms
    # ------------------------------------------------------------------
    "dataviz.regression.transforms.boxcox_likelihood_curve_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.transforms import boxcox_likelihood_curve_static

rng = np.random.default_rng(42)
claim_amount = rng.gamma(shape=2.0, scale=1800.0, size=60)  # right-skewed, > 0

ax = boxcox_likelihood_curve_static(
    claim_amount, lambdas=np.linspace(-1.5, 1.5, 91),
    title="Auto insurance claims: Box-Cox profile log-likelihood",
)
plt.show()''',
    "dataviz.regression.transforms.boxcox_likelihood_curve_interactive": '''import numpy as np
from dataviz.regression.transforms import boxcox_likelihood_curve_interactive

rng = np.random.default_rng(42)
claim_amount = rng.gamma(shape=2.0, scale=1800.0, size=60)  # right-skewed, > 0

fig = boxcox_likelihood_curve_interactive(
    claim_amount, lambdas=np.linspace(-1.5, 1.5, 91),
    title="Auto insurance claims: Box-Cox profile log-likelihood",
)
fig.show()''',
    "dataviz.regression.transforms.yeojohnson_lambda_search_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.transforms import yeojohnson_lambda_search_static

rng = np.random.default_rng(42)
profit_margin = rng.normal(4.0, 9.0, 55) - rng.gamma(1.5, 4.0, 55)  # mixed signs

ax = yeojohnson_lambda_search_static(
    profit_margin, lambdas=np.linspace(-2, 2, 121),
    title="Store profit margins: Yeo-Johnson lambda search",
)
plt.show()''',
    "dataviz.regression.transforms.yeojohnson_lambda_search_interactive": '''import numpy as np
from dataviz.regression.transforms import yeojohnson_lambda_search_interactive

rng = np.random.default_rng(42)
profit_margin = rng.normal(4.0, 9.0, 55) - rng.gamma(1.5, 4.0, 55)  # mixed signs

fig = yeojohnson_lambda_search_interactive(
    profit_margin, lambdas=np.linspace(-2, 2, 121),
    title="Store profit margins: Yeo-Johnson lambda search",
)
fig.show()''',
    "dataviz.regression.transforms.log_log_diagnostic_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.transforms import log_log_diagnostic_static

rng = np.random.default_rng(42)
n = 38
city_area = rng.uniform(20, 900, n)                    # km^2
population = 4200 * city_area ** 0.85 * np.exp(rng.normal(0, 0.18, n))

ax = log_log_diagnostic_static(
    city_area, population,
    title="Urban scaling study: log-log check of area vs population",
)
plt.show()''',
    "dataviz.regression.transforms.log_log_diagnostic_interactive": '''import numpy as np
from dataviz.regression.transforms import log_log_diagnostic_interactive

rng = np.random.default_rng(42)
n = 38
city_area = rng.uniform(20, 900, n)                    # km^2
population = 4200 * city_area ** 0.85 * np.exp(rng.normal(0, 0.18, n))

fig = log_log_diagnostic_interactive(
    city_area, population,
    title="Urban scaling study: log-log check of area vs population",
)
fig.show()''',
    "dataviz.regression.transforms.power_transform_residual_panel_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.transforms import power_transform_residual_panel_static

rng = np.random.default_rng(42)
n = 36
y_pred = np.sort(rng.uniform(20, 400, n))              # fitted claim cost (k$)
spread = 0.04 * y_pred                                 # heteroscedastic noise
resid_orig = rng.normal(0, 1, n) * spread
resid_log = rng.normal(0, 0.06, n)
resid_sqrt = rng.normal(0, 0.35, n)

fig = power_transform_residual_panel_static(
    y_pred, resid_orig, resid_log, resid_sqrt,
    title="Claim cost model: residual panel across power transforms",
)
plt.show()''',
    "dataviz.regression.transforms.power_transform_residual_panel_interactive": '''import numpy as np
from dataviz.regression.transforms import power_transform_residual_panel_interactive

rng = np.random.default_rng(42)
n = 36
y_pred = np.sort(rng.uniform(20, 400, n))              # fitted claim cost (k$)
spread = 0.04 * y_pred                                 # heteroscedastic noise
resid_orig = rng.normal(0, 1, n) * spread
resid_log = rng.normal(0, 0.06, n)
resid_sqrt = rng.normal(0, 0.35, n)

fig = power_transform_residual_panel_interactive(
    y_pred, resid_orig, resid_log, resid_sqrt,
    title="Claim cost model: residual panel across power transforms",
)
fig.show()''',

    # ------------------------------------------------------------------
    # uncertainty
    # ------------------------------------------------------------------
    "dataviz.regression.uncertainty.conformal_interval_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.uncertainty import conformal_interval_plot_static

rng = np.random.default_rng(42)
n = 30
load_mw = 450 + 120 * np.sin(np.linspace(0, 2 * np.pi, n)) + rng.normal(0, 18, n)
pred_mw = 450 + 120 * np.sin(np.linspace(0, 2 * np.pi, n))
half_width = 25 + 8 * np.abs(np.sin(np.linspace(0, np.pi, n)))
lower, upper = pred_mw - half_width, pred_mw + half_width

ax = conformal_interval_plot_static(
    load_mw, pred_mw, lower, upper,
    title="Grid load forecast: split-conformal 90% prediction intervals",
)
plt.show()''',
    "dataviz.regression.uncertainty.conformal_interval_plot_interactive": '''import numpy as np
from dataviz.regression.uncertainty import conformal_interval_plot_interactive

rng = np.random.default_rng(42)
n = 30
load_mw = 450 + 120 * np.sin(np.linspace(0, 2 * np.pi, n)) + rng.normal(0, 18, n)
pred_mw = 450 + 120 * np.sin(np.linspace(0, 2 * np.pi, n))
half_width = 25 + 8 * np.abs(np.sin(np.linspace(0, np.pi, n)))
lower, upper = pred_mw - half_width, pred_mw + half_width

fig = conformal_interval_plot_interactive(
    load_mw, pred_mw, lower, upper,
    title="Grid load forecast: split-conformal 90% prediction intervals",
)
fig.show()''',
    "dataviz.regression.uncertainty.jackknife_plus_band_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.uncertainty import jackknife_plus_band_static

rng = np.random.default_rng(42)
n = 30
load_mw = 450 + 120 * np.sin(np.linspace(0, 2 * np.pi, n)) + rng.normal(0, 18, n)
pred_mw = 450 + 120 * np.sin(np.linspace(0, 2 * np.pi, n))
half_width = 25 + 8 * np.abs(np.sin(np.linspace(0, np.pi, n)))
lower, upper = pred_mw - half_width, pred_mw + half_width

ax = jackknife_plus_band_static(
    load_mw, pred_mw, lower, upper,
    title="Grid load forecast: jackknife+ 90% predictive band",
)
plt.show()''',
    "dataviz.regression.uncertainty.jackknife_plus_band_interactive": '''import numpy as np
from dataviz.regression.uncertainty import jackknife_plus_band_interactive

rng = np.random.default_rng(42)
n = 30
load_mw = 450 + 120 * np.sin(np.linspace(0, 2 * np.pi, n)) + rng.normal(0, 18, n)
pred_mw = 450 + 120 * np.sin(np.linspace(0, 2 * np.pi, n))
half_width = 25 + 8 * np.abs(np.sin(np.linspace(0, np.pi, n)))
lower, upper = pred_mw - half_width, pred_mw + half_width

fig = jackknife_plus_band_interactive(
    load_mw, pred_mw, lower, upper,
    title="Grid load forecast: jackknife+ 90% predictive band",
)
fig.show()''',
    "dataviz.regression.uncertainty.quantile_calibration_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.uncertainty import quantile_calibration_plot_static

nominal = np.linspace(0.05, 0.95, 19)
empirical = nominal + 0.04 * np.sin(2 * np.pi * nominal) - 0.015

ax = quantile_calibration_plot_static(
    nominal, empirical,
    title="Rainfall quantile regression: nominal vs empirical coverage",
)
plt.show()''',
    "dataviz.regression.uncertainty.quantile_calibration_plot_interactive": '''import numpy as np
from dataviz.regression.uncertainty import quantile_calibration_plot_interactive

nominal = np.linspace(0.05, 0.95, 19)
empirical = nominal + 0.04 * np.sin(2 * np.pi * nominal) - 0.015

fig = quantile_calibration_plot_interactive(
    nominal, empirical,
    title="Rainfall quantile regression: nominal vs empirical coverage",
)
fig.show()''',
    "dataviz.regression.uncertainty.sharpness_vs_coverage_plot_static": '''import matplotlib.pyplot as plt
from dataviz.regression.uncertainty import sharpness_vs_coverage_plot_static

models = ["Linear+conformal", "Quantile RF", "Bayesian ridge", "NGBoost"]
sharpness = [58.2, 44.7, 49.5, 41.3]   # average interval width (k$)
coverage = [0.901, 0.912, 0.887, 0.928]

ax = sharpness_vs_coverage_plot_static(
    sharpness, coverage, model_labels=models,
    title="House price intervals: sharpness vs empirical coverage",
)
ax.axhline(0.90, color="#e45756", linestyle=":", linewidth=1)
plt.show()''',
    "dataviz.regression.uncertainty.sharpness_vs_coverage_plot_interactive": '''from dataviz.regression.uncertainty import sharpness_vs_coverage_plot_interactive

models = ["Linear+conformal", "Quantile RF", "Bayesian ridge", "NGBoost"]
sharpness = [58.2, 44.7, 49.5, 41.3]   # average interval width (k$)
coverage = [0.901, 0.912, 0.887, 0.928]

fig = sharpness_vs_coverage_plot_interactive(
    sharpness, coverage, model_labels=models,
    title="House price intervals: sharpness vs empirical coverage",
)
fig.show()''',
    "dataviz.regression.uncertainty.coverage_by_segment_bar_static": '''import matplotlib.pyplot as plt
from dataviz.regression.uncertainty import coverage_by_segment_bar_static

segments = ["Urban", "Suburban", "Rural", "Coastal", "Mountain"]
coverage = [0.93, 0.91, 0.84, 0.88, 0.79]

ax = coverage_by_segment_bar_static(
    segments, coverage, nominal=0.9,
    title="Property value model: conformal coverage by market segment",
)
plt.show()''',
    "dataviz.regression.uncertainty.coverage_by_segment_bar_interactive": '''from dataviz.regression.uncertainty import coverage_by_segment_bar_interactive

segments = ["Urban", "Suburban", "Rural", "Coastal", "Mountain"]
coverage = [0.93, 0.91, 0.84, 0.88, 0.79]

fig = coverage_by_segment_bar_interactive(
    segments, coverage, nominal=0.9,
    title="Property value model: conformal coverage by market segment",
)
fig.show()''',

    # ------------------------------------------------------------------
    # validation
    # ------------------------------------------------------------------
    "dataviz.regression.validation.validation_curve_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.validation import validation_curve_static

rng = np.random.default_rng(42)
alphas = np.logspace(-3, 2, 12)
base_train = 0.55 + 0.40 * (1 - np.exp(-alphas))
base_test = 0.88 - 0.0011 * (np.log10(alphas) + 1.2) ** 4
train_scores = base_train[:, None] + rng.normal(0, 0.012, (12, 5))
test_scores = base_test[:, None] + rng.normal(0, 0.020, (12, 5))

ax = validation_curve_static(
    alphas, train_scores, test_scores,
    param_name="Ridge alpha", score_name="R-squared", log_x=True,
    title="Ridge regression on concrete strength: validation curve",
)
plt.show()''',
    "dataviz.regression.validation.validation_curve_interactive": '''import numpy as np
from dataviz.regression.validation import validation_curve_interactive

rng = np.random.default_rng(42)
alphas = np.logspace(-3, 2, 12)
base_train = 0.55 + 0.40 * (1 - np.exp(-alphas))
base_test = 0.88 - 0.0011 * (np.log10(alphas) + 1.2) ** 4
train_scores = base_train[:, None] + rng.normal(0, 0.012, (12, 5))
test_scores = base_test[:, None] + rng.normal(0, 0.020, (12, 5))

fig = validation_curve_interactive(
    alphas, train_scores, test_scores,
    param_name="Ridge alpha", score_name="R-squared", log_x=True,
    title="Ridge regression on concrete strength: validation curve",
)
fig.show()''',
    "dataviz.regression.validation.training_history_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.validation import training_history_static

rng = np.random.default_rng(42)
epochs = np.arange(1, 21)
train_rmse = 42 * np.exp(-epochs / 6.0) + 8.5 + rng.normal(0, 0.25, 20)
val_rmse = 42 * np.exp(-epochs / 6.5) + 10.8 + rng.normal(0, 0.35, 20)
val_rmse[14:] += np.linspace(0, 1.8, 6)  # onset of overfitting
history = {"train_rmse": train_rmse, "val_rmse": val_rmse}

ax = training_history_static(
    history,
    title="Demand forecasting MLP: training history (RMSE, k units)",
)
plt.show()''',
    "dataviz.regression.validation.training_history_interactive": '''import numpy as np
from dataviz.regression.validation import training_history_interactive

rng = np.random.default_rng(42)
epochs = np.arange(1, 21)
train_rmse = 42 * np.exp(-epochs / 6.0) + 8.5 + rng.normal(0, 0.25, 20)
val_rmse = 42 * np.exp(-epochs / 6.5) + 10.8 + rng.normal(0, 0.35, 20)
val_rmse[14:] += np.linspace(0, 1.8, 6)  # onset of overfitting
history = {"train_rmse": train_rmse, "val_rmse": val_rmse}

fig = training_history_interactive(
    history,
    title="Demand forecasting MLP: training history (RMSE, k units)",
)
fig.show()''',
    "dataviz.regression.validation.cv_score_plot_static": '''import matplotlib.pyplot as plt
from dataviz.regression.validation import cv_score_plot_static

fold_r2 = [0.812, 0.795, 0.834, 0.807, 0.851, 0.788, 0.822, 0.815]

ax = cv_score_plot_static(
    fold_r2, model_name="Gradient boosting (wine quality)",
    title="8-fold cross-validation R-squared",
)
plt.show()''',
    "dataviz.regression.validation.cv_score_plot_interactive": '''from dataviz.regression.validation import cv_score_plot_interactive

fold_r2 = [0.812, 0.795, 0.834, 0.807, 0.851, 0.788, 0.822, 0.815]

fig = cv_score_plot_interactive(
    fold_r2, model_name="Gradient boosting (wine quality)",
    title="8-fold cross-validation R-squared",
)
fig.show()''',
    "dataviz.regression.validation.bias_variance_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.validation import bias_variance_plot_static

degree = np.arange(1, 11)
bias_sq = 14.0 / degree ** 1.6
variance = 0.35 * degree ** 1.8
noise = np.full_like(degree, 4.0, dtype=float)

ax = bias_variance_plot_static(
    degree, bias_sq, variance, noise=noise,
    title="Polynomial fit of compressor efficiency: bias-variance trade-off",
)
plt.show()''',
    "dataviz.regression.validation.bias_variance_plot_interactive": '''import numpy as np
from dataviz.regression.validation import bias_variance_plot_interactive

degree = np.arange(1, 11)
bias_sq = 14.0 / degree ** 1.6
variance = 0.35 * degree ** 1.8
noise = np.full_like(degree, 4.0, dtype=float)

fig = bias_variance_plot_interactive(
    degree, bias_sq, variance, noise=noise,
    title="Polynomial fit of compressor efficiency: bias-variance trade-off",
)
fig.show()''',

    # ------------------------------------------------------------------
    # var_engineering
    # ------------------------------------------------------------------
    "dataviz.regression.var_engineering.target_vs_feature_smooth_grid_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.var_engineering import target_vs_feature_smooth_grid_static

rng = np.random.default_rng(42)
n = 60
X = pd.DataFrame({
    "temperature": rng.uniform(15, 35, n),
    "humidity": rng.uniform(20, 95, n),
    "wind_speed": rng.uniform(0, 40, n),
    "hour": rng.uniform(0, 24, n),
})
rentals = (30 + 4.2 * X["temperature"] - 0.9 * X["humidity"]
           + 18 * np.sin(X["hour"] / 24 * 2 * np.pi)
           + rng.normal(0, 12, n))

ax = target_vs_feature_smooth_grid_static(
    X, rentals, feature_names=list(X.columns), bins=15, ncols=2,
    title="Bike-share demand: smoothed target vs each feature",
)
plt.show()''',
    "dataviz.regression.var_engineering.target_vs_feature_smooth_grid_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.var_engineering import target_vs_feature_smooth_grid_interactive

rng = np.random.default_rng(42)
n = 60
X = pd.DataFrame({
    "temperature": rng.uniform(15, 35, n),
    "humidity": rng.uniform(20, 95, n),
    "wind_speed": rng.uniform(0, 40, n),
    "hour": rng.uniform(0, 24, n),
})
rentals = (30 + 4.2 * X["temperature"] - 0.9 * X["humidity"]
           + 18 * np.sin(X["hour"] / 24 * 2 * np.pi)
           + rng.normal(0, 12, n))

fig = target_vs_feature_smooth_grid_interactive(
    X, rentals, feature_names=list(X.columns), bins=15, ncols=2,
    title="Bike-share demand: smoothed target vs each feature",
)
fig.show()''',
    "dataviz.regression.var_engineering.feature_target_correlation_bar_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.var_engineering import feature_target_correlation_bar_static

rng = np.random.default_rng(42)
n = 50
temp = rng.uniform(15, 35, n)
humidity = rng.uniform(20, 95, n)
wind = rng.uniform(0, 40, n)
pressure = rng.uniform(1005, 1025, n)
rentals = 30 + 4.2 * temp - 0.9 * humidity + rng.normal(0, 12, n)
X = pd.DataFrame({
    "temperature": temp, "humidity": humidity,
    "wind_speed": wind, "pressure": pressure,
})

ax = feature_target_correlation_bar_static(
    X, rentals, feature_names=list(X.columns),
    title="Bike-share demand: feature-target Pearson correlations",
)
plt.show()''',
    "dataviz.regression.var_engineering.feature_target_correlation_bar_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.var_engineering import feature_target_correlation_bar_interactive

rng = np.random.default_rng(42)
n = 50
temp = rng.uniform(15, 35, n)
humidity = rng.uniform(20, 95, n)
wind = rng.uniform(0, 40, n)
pressure = rng.uniform(1005, 1025, n)
rentals = 30 + 4.2 * temp - 0.9 * humidity + rng.normal(0, 12, n)
X = pd.DataFrame({
    "temperature": temp, "humidity": humidity,
    "wind_speed": wind, "pressure": pressure,
})

fig = feature_target_correlation_bar_interactive(
    X, rentals, feature_names=list(X.columns),
    title="Bike-share demand: feature-target Pearson correlations",
)
fig.show()''',
    "dataviz.regression.var_engineering.target_encoding_curve_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.regression.var_engineering import target_encoding_curve_static

zip_means = [385, 402, 291, 450, 318, 512, 366, 277, 429, 341, 470, 305, 398, 260, 445]
zip_counts = [210, 95, 640, 38, 480, 22, 150, 720, 61, 390, 45, 540, 120, 810, 88]
prior = np.average(zip_means, weights=zip_counts)

ax = target_encoding_curve_static(
    zip_means, zip_counts, prior=round(float(prior), 1),
    title="Home prices by ZIP: target-encoded mean vs sample size (k$)",
)
plt.show()''',
    "dataviz.regression.var_engineering.target_encoding_curve_interactive": '''import numpy as np
from dataviz.regression.var_engineering import target_encoding_curve_interactive

zip_means = [385, 402, 291, 450, 318, 512, 366, 277, 429, 341, 470, 305, 398, 260, 445]
zip_counts = [210, 95, 640, 38, 480, 22, 150, 720, 61, 390, 45, 540, 120, 810, 88]
prior = np.average(zip_means, weights=zip_counts)

fig = target_encoding_curve_interactive(
    zip_means, zip_counts, prior=round(float(prior), 1),
    title="Home prices by ZIP: target-encoded mean vs sample size (k$)",
)
fig.show()''',
}
