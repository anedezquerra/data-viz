"""Curated rich examples for regression member pages."""

EXAMPLES = {
    # ------------------------------------------------------------------
    # mixed_effects
    # ------------------------------------------------------------------
    "dataviz.regression.mixed_effects.random_effect_caterpillar_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.mixed_effects import random_effect_caterpillar_static

rng = np.random.default_rng(42)
clinics = pd.Series([f"Clinic {c:02d}" for c in range(1, 16)], name="clinic")
random_effects = pd.Series(rng.normal(0.0, 1.2, size=15), name="intercept_shift")
std_errors = pd.Series(rng.uniform(0.25, 0.6, size=15), name="se")

ax = random_effect_caterpillar_static(
    clinics, random_effects, std_errors=std_errors,
    title="Clinical trial: random intercepts by site",
    color="#2a6f97", theme="minimal",
)
ax.set_xlabel("Treatment effect shift (mmHg)")
plt.show()''',
    "dataviz.regression.mixed_effects.random_effect_caterpillar_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.mixed_effects import random_effect_caterpillar_interactive

rng = np.random.default_rng(42)
clinics = pd.Series([f"Clinic {c:02d}" for c in range(1, 16)], name="clinic")
random_effects = pd.Series(rng.normal(0.0, 1.2, size=15), name="intercept_shift")
std_errors = pd.Series(rng.uniform(0.25, 0.6, size=15), name="se")

fig = random_effect_caterpillar_interactive(
    clinics, random_effects, std_errors=std_errors,
    title="Clinical trial: random intercepts by site",
    color="#2a6f97", template="plotly_white", height=700,
)
fig.show()''',
    "dataviz.regression.mixed_effects.random_intercept_slope_scatter_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.mixed_effects import random_intercept_slope_scatter_static

rng = np.random.default_rng(42)
schools = pd.Series([f"School {s:02d}" for s in range(1, 21)], name="school")
random_intercepts = pd.Series(rng.normal(0.0, 2.5, size=20), name="intercept")
random_slopes = pd.Series(
    -0.4 * random_intercepts + rng.normal(0.0, 0.6, size=20), name="slope"
)

ax = random_intercept_slope_scatter_static(
    random_intercepts, random_slopes,
    title="Education study: intercept vs slope per school",
    color="#6a4c93", theme="minimal",
)
ax.set_xlabel("Random intercept (baseline score)")
ax.set_ylabel("Random slope (gain per week)")
plt.show()''',
    "dataviz.regression.mixed_effects.random_intercept_slope_scatter_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.mixed_effects import random_intercept_slope_scatter_interactive

rng = np.random.default_rng(42)
schools = pd.Series([f"School {s:02d}" for s in range(1, 21)], name="school")
random_intercepts = pd.Series(rng.normal(0.0, 2.5, size=20), name="intercept")
random_slopes = pd.Series(
    -0.4 * random_intercepts + rng.normal(0.0, 0.6, size=20), name="slope"
)

fig = random_intercept_slope_scatter_interactive(
    random_intercepts, random_slopes,
    title="Education study: intercept vs slope per school",
    color="#6a4c93", template="plotly_white",
)
fig.show()''',
    "dataviz.regression.mixed_effects.group_means_vs_predicted_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.mixed_effects import group_means_vs_predicted_static

rng = np.random.default_rng(42)
lines = pd.Series([f"Line {c}" for c in "ABCDEFGHIJ"], name="line")
observed = pd.Series(rng.normal(92.0, 4.0, size=10).round(2), name="observed_yield")
predicted = pd.Series(observed + rng.normal(0.0, 1.5, size=10), name="predicted_yield")

ax = group_means_vs_predicted_static(
    lines, observed, predicted,
    title="Manufacturing yield: observed vs mixed-model predicted",
    obs_color="#1b9e77", pred_color="#d95f02", theme="minimal",
)
ax.set_ylabel("Mean yield (%)")
plt.show()''',
    "dataviz.regression.mixed_effects.group_means_vs_predicted_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.mixed_effects import group_means_vs_predicted_interactive

rng = np.random.default_rng(42)
lines = pd.Series([f"Line {c}" for c in "ABCDEFGHIJ"], name="line")
observed = pd.Series(rng.normal(92.0, 4.0, size=10).round(2), name="observed_yield")
predicted = pd.Series(observed + rng.normal(0.0, 1.5, size=10), name="predicted_yield")

fig = group_means_vs_predicted_interactive(
    lines, observed, predicted,
    title="Manufacturing yield: observed vs mixed-model predicted",
    obs_color="#1b9e77", pred_color="#d95f02", template="plotly_white",
)
fig.show()''',
    # ------------------------------------------------------------------
    # multicollinearity
    # ------------------------------------------------------------------
    "dataviz.regression.multicollinearity.vif_bar_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.multicollinearity import vif_bar_static

rng = np.random.default_rng(42)
n = 36
living_area = rng.normal(1800, 400, n)
housing = pd.DataFrame({
    "living_area_sqft": living_area,
    "bedrooms": np.clip(living_area / 450 + rng.normal(0, 0.4, n), 1, 6),
    "bathrooms": np.clip(living_area / 700 + rng.normal(0, 0.3, n), 1, 4),
    "lot_size_sqft": rng.normal(6000, 1500, n),
    "age_years": rng.uniform(0, 60, n),
})

ax = vif_bar_static(
    housing, feature_names=list(housing.columns),
    title="Housing price model: variance inflation factors",
    threshold=5.0, color="#4878d0", theme="minimal",
)
ax.set_ylabel("VIF")
plt.show()''',
    "dataviz.regression.multicollinearity.vif_bar_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.multicollinearity import vif_bar_interactive

rng = np.random.default_rng(42)
n = 36
living_area = rng.normal(1800, 400, n)
housing = pd.DataFrame({
    "living_area_sqft": living_area,
    "bedrooms": np.clip(living_area / 450 + rng.normal(0, 0.4, n), 1, 6),
    "bathrooms": np.clip(living_area / 700 + rng.normal(0, 0.3, n), 1, 4),
    "lot_size_sqft": rng.normal(6000, 1500, n),
    "age_years": rng.uniform(0, 60, n),
})

fig = vif_bar_interactive(
    housing, feature_names=list(housing.columns),
    title="Housing price model: variance inflation factors",
    threshold=5.0, color="#4878d0", template="plotly_white",
)
fig.show()''',
    "dataviz.regression.multicollinearity.condition_index_plot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.multicollinearity import condition_index_plot_static

rng = np.random.default_rng(42)
n = 36
engine_size = rng.normal(2.4, 0.6, n)
vehicles = pd.DataFrame({
    "engine_l": engine_size,
    "horsepower": 95 * engine_size + rng.normal(0, 12, n),
    "weight_kg": 620 * engine_size + rng.normal(0, 90, n),
    "wheelbase_in": rng.normal(104, 6, n),
})

ax = condition_index_plot_static(
    vehicles, title="Fuel-efficiency model: condition indices",
    threshold=30.0, color="#ee854a", theme="minimal",
)
ax.set_ylabel("Condition index")
plt.show()''',
    "dataviz.regression.multicollinearity.condition_index_plot_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.multicollinearity import condition_index_plot_interactive

rng = np.random.default_rng(42)
n = 36
engine_size = rng.normal(2.4, 0.6, n)
vehicles = pd.DataFrame({
    "engine_l": engine_size,
    "horsepower": 95 * engine_size + rng.normal(0, 12, n),
    "weight_kg": 620 * engine_size + rng.normal(0, 90, n),
    "wheelbase_in": rng.normal(104, 6, n),
})

fig = condition_index_plot_interactive(
    vehicles, title="Fuel-efficiency model: condition indices",
    threshold=30.0, color="#ee854a", template="plotly_white",
)
fig.show()''',
    "dataviz.regression.multicollinearity.correlation_heatmap_with_clustering_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.multicollinearity import correlation_heatmap_with_clustering_static

rng = np.random.default_rng(42)
n = 48
ad_spend = rng.normal(50, 12, n)
marketing = pd.DataFrame({
    "tv_spend_k": ad_spend + rng.normal(0, 4, n),
    "radio_spend_k": 0.6 * ad_spend + rng.normal(0, 6, n),
    "social_spend_k": rng.normal(20, 6, n),
    "email_campaigns": rng.integers(1, 9, n).astype(float),
    "web_traffic_k": 1.4 * ad_spend + rng.normal(0, 10, n),
})

ax = correlation_heatmap_with_clustering_static(
    marketing, feature_names=list(marketing.columns),
    title="Marketing mix model: clustered predictor correlations",
    cmap="RdBu_r", theme="minimal",
)
plt.show()''',
    "dataviz.regression.multicollinearity.correlation_heatmap_with_clustering_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.multicollinearity import correlation_heatmap_with_clustering_interactive

rng = np.random.default_rng(42)
n = 48
ad_spend = rng.normal(50, 12, n)
marketing = pd.DataFrame({
    "tv_spend_k": ad_spend + rng.normal(0, 4, n),
    "radio_spend_k": 0.6 * ad_spend + rng.normal(0, 6, n),
    "social_spend_k": rng.normal(20, 6, n),
    "email_campaigns": rng.integers(1, 9, n).astype(float),
    "web_traffic_k": 1.4 * ad_spend + rng.normal(0, 10, n),
})

fig = correlation_heatmap_with_clustering_interactive(
    marketing, feature_names=list(marketing.columns),
    title="Marketing mix model: clustered predictor correlations",
    colorscale="RdBu", template="plotly_white",
)
fig.show()''',
    "dataviz.regression.multicollinearity.eigenvalue_scree_predictors_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.multicollinearity import eigenvalue_scree_predictors_static

rng = np.random.default_rng(42)
n = 40
size = rng.normal(2000, 500, n)
homes = pd.DataFrame({
    "sqft": size,
    "bedrooms": size / 480 + rng.normal(0, 0.4, n),
    "bathrooms": size / 750 + rng.normal(0, 0.3, n),
    "garage_cars": np.clip(size / 900 + rng.normal(0, 0.3, n), 0, 4),
    "lot_sqft": rng.normal(7000, 1800, n),
})

ax = eigenvalue_scree_predictors_static(
    homes, title="Home appraisal model: predictor eigenvalue scree",
    color="#6acc64", theme="minimal",
)
ax.set_ylabel("Eigenvalue")
plt.show()''',
    "dataviz.regression.multicollinearity.eigenvalue_scree_predictors_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.multicollinearity import eigenvalue_scree_predictors_interactive

rng = np.random.default_rng(42)
n = 40
size = rng.normal(2000, 500, n)
homes = pd.DataFrame({
    "sqft": size,
    "bedrooms": size / 480 + rng.normal(0, 0.4, n),
    "bathrooms": size / 750 + rng.normal(0, 0.3, n),
    "garage_cars": np.clip(size / 900 + rng.normal(0, 0.3, n), 0, 4),
    "lot_sqft": rng.normal(7000, 1800, n),
})

fig = eigenvalue_scree_predictors_interactive(
    homes, title="Home appraisal model: predictor eigenvalue scree",
    color="#6acc64", template="plotly_white",
)
fig.show()''',
    "dataviz.regression.multicollinearity.tolerance_bar_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.multicollinearity import tolerance_bar_static

rng = np.random.default_rng(42)
n = 36
load = rng.normal(320, 60, n)
plant = pd.DataFrame({
    "throughput_tph": load,
    "conveyor_speed": 0.9 * load / 60 + rng.normal(0, 0.15, n),
    "motor_current_a": 0.45 * load + rng.normal(0, 8, n),
    "ambient_temp_c": rng.normal(24, 3, n),
    "operator_experience_yr": rng.uniform(0.5, 20, n),
})

ax = tolerance_bar_static(
    plant, feature_names=list(plant.columns),
    title="Plant throughput model: predictor tolerance",
    threshold=0.2, color="#d65f5f", theme="minimal",
)
ax.set_ylabel("Tolerance (1/VIF)")
plt.show()''',
    "dataviz.regression.multicollinearity.tolerance_bar_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.multicollinearity import tolerance_bar_interactive

rng = np.random.default_rng(42)
n = 36
load = rng.normal(320, 60, n)
plant = pd.DataFrame({
    "throughput_tph": load,
    "conveyor_speed": 0.9 * load / 60 + rng.normal(0, 0.15, n),
    "motor_current_a": 0.45 * load + rng.normal(0, 8, n),
    "ambient_temp_c": rng.normal(24, 3, n),
    "operator_experience_yr": rng.uniform(0.5, 20, n),
})

fig = tolerance_bar_interactive(
    plant, feature_names=list(plant.columns),
    title="Plant throughput model: predictor tolerance",
    threshold=0.2, color="#d65f5f", template="plotly_white",
)
fig.show()''',
    # ------------------------------------------------------------------
    # prediction
    # ------------------------------------------------------------------
    "dataviz.regression.prediction.prediction_plot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.prediction import prediction_plot_static

rng = np.random.default_rng(42)
days = pd.date_range("2025-01-05", periods=24, freq="W")
actual_demand = pd.Series(
    420 + 3.5 * np.arange(24) + rng.normal(0, 25, 24),
    index=days, name="actual_mwh",
)
predicted_demand = pd.Series(
    actual_demand + rng.normal(0, 18, 24), index=days, name="forecast_mwh"
)

ax = prediction_plot_static(
    actual_demand, predicted_demand,
    title="Weekly energy demand: forecast vs actual",
    color="#2a6f97", marker_size=60, alpha=0.75,
    line_color="#d62728", theme="minimal",
)
ax.set_xlabel("Actual demand (MWh)")
ax.set_ylabel("Forecast demand (MWh)")
plt.show()''',
    "dataviz.regression.prediction.prediction_plot_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.prediction import prediction_plot_interactive

rng = np.random.default_rng(42)
days = pd.date_range("2025-01-05", periods=24, freq="W")
actual_demand = pd.Series(
    420 + 3.5 * np.arange(24) + rng.normal(0, 25, 24),
    index=days, name="actual_mwh",
)
predicted_demand = pd.Series(
    actual_demand + rng.normal(0, 18, 24), index=days, name="forecast_mwh"
)

fig = prediction_plot_interactive(
    actual_demand, predicted_demand,
    title="Weekly energy demand: forecast vs actual",
    marker_color="#2a6f97", marker_size=9,
    line_color="#d62728", template="plotly_white",
)
fig.show()''',
    # ------------------------------------------------------------------
    # prediction_extended
    # ------------------------------------------------------------------
    "dataviz.regression.prediction_extended.pred_vs_actual_hexbin_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.prediction_extended import pred_vs_actual_hexbin_static

rng = np.random.default_rng(42)
batches = pd.Series(np.arange(1, 121), name="batch")
actual_yield = pd.Series(
    rng.gamma(shape=9.0, scale=4.0, size=120), name="actual_yield_kg"
)
predicted_yield = pd.Series(
    0.85 * actual_yield + 5.0 + rng.normal(0, 3.5, 120), name="predicted_yield_kg"
)

ax = pred_vs_actual_hexbin_static(
    actual_yield, predicted_yield, gridsize=18,
    title="Chemical batch yield: predicted vs actual density",
    cmap="cividis", theme="minimal",
)
ax.set_xlabel("Actual yield (kg)")
ax.set_ylabel("Predicted yield (kg)")
plt.show()''',
    "dataviz.regression.prediction_extended.pred_vs_actual_hexbin_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.prediction_extended import pred_vs_actual_hexbin_interactive

rng = np.random.default_rng(42)
batches = pd.Series(np.arange(1, 121), name="batch")
actual_yield = pd.Series(
    rng.gamma(shape=9.0, scale=4.0, size=120), name="actual_yield_kg"
)
predicted_yield = pd.Series(
    0.85 * actual_yield + 5.0 + rng.normal(0, 3.5, 120), name="predicted_yield_kg"
)

fig = pred_vs_actual_hexbin_interactive(
    actual_yield, predicted_yield, nbins=18,
    title="Chemical batch yield: predicted vs actual density",
    colorscale="Cividis", template="plotly_white",
)
fig.show()''',
    "dataviz.regression.prediction_extended.pred_vs_actual_density_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.prediction_extended import pred_vs_actual_density_static

rng = np.random.default_rng(42)
rides = pd.Series(np.arange(1, 61), name="ride")
actual_fare = pd.Series(rng.lognormal(2.8, 0.45, 60), name="actual_fare_usd")
predicted_fare = pd.Series(
    0.9 * actual_fare + 1.5 + rng.normal(0, 1.8, 60), name="predicted_fare_usd"
)

ax = pred_vs_actual_density_static(
    actual_fare, predicted_fare, bins=24,
    title="Ride-hailing fares: actual vs predicted distributions",
    actual_color="#4878d0", predicted_color="#ee854a",
    alpha=0.45, theme="minimal",
)
ax.set_xlabel("Fare (USD)")
plt.show()''',
    "dataviz.regression.prediction_extended.pred_vs_actual_density_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.prediction_extended import pred_vs_actual_density_interactive

rng = np.random.default_rng(42)
rides = pd.Series(np.arange(1, 61), name="ride")
actual_fare = pd.Series(rng.lognormal(2.8, 0.45, 60), name="actual_fare_usd")
predicted_fare = pd.Series(
    0.9 * actual_fare + 1.5 + rng.normal(0, 1.8, 60), name="predicted_fare_usd"
)

fig = pred_vs_actual_density_interactive(
    actual_fare, predicted_fare, bins=24,
    title="Ride-hailing fares: actual vs predicted distributions",
    actual_color="#4878d0", predicted_color="#ee854a",
    template="plotly_white",
)
fig.show()''',
    "dataviz.regression.prediction_extended.prediction_error_histogram_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.prediction_extended import prediction_error_histogram_static

rng = np.random.default_rng(42)
months = pd.date_range("2023-01-01", periods=30, freq="MS")
actual_sales = pd.Series(
    980 + 12 * np.sin(np.arange(30) / 4.8) + rng.normal(0, 40, 30),
    index=months, name="actual_units",
)
forecast_sales = pd.Series(
    actual_sales + rng.normal(6, 28, 30), index=months, name="forecast_units"
)

ax = prediction_error_histogram_static(
    actual_sales, forecast_sales, bins=14,
    title="Retail sales forecast error distribution",
    color="#4878d0", edgecolor="white", theme="minimal",
)
ax.set_xlabel("Error: actual minus forecast (units)")
plt.show()''',
    "dataviz.regression.prediction_extended.prediction_error_histogram_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.prediction_extended import prediction_error_histogram_interactive

rng = np.random.default_rng(42)
months = pd.date_range("2023-01-01", periods=30, freq="MS")
actual_sales = pd.Series(
    980 + 12 * np.sin(np.arange(30) / 4.8) + rng.normal(0, 40, 30),
    index=months, name="actual_units",
)
forecast_sales = pd.Series(
    actual_sales + rng.normal(6, 28, 30), index=months, name="forecast_units"
)

fig = prediction_error_histogram_interactive(
    actual_sales, forecast_sales, bins=14,
    title="Retail sales forecast error distribution",
    color="#4878d0", template="plotly_white",
)
fig.show()''',
    "dataviz.regression.prediction_extended.prediction_interval_plot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.prediction_extended import prediction_interval_plot_static

rng = np.random.default_rng(42)
patients = pd.Series(np.arange(1, 31), name="patient")
actual_charge = pd.Series(
    rng.uniform(8, 60, 30).round(1), name="actual_charge_kusd"
).sort_values().reset_index(drop=True)
predicted_charge = pd.Series(
    actual_charge + rng.normal(0, 4.5, 30), name="predicted_charge_kusd"
)

ax = prediction_interval_plot_static(
    actual_charge, predicted_charge, confidence=0.90, method="empirical",
    title="Hospital charge model: 90% prediction intervals",
    point_color="#2a6f97", band_color="#a8d5e5", line_color="#d62728",
    theme="minimal",
)
ax.set_ylabel("Charge (thousand USD)")
plt.show()''',
    "dataviz.regression.prediction_extended.prediction_interval_plot_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.prediction_extended import prediction_interval_plot_interactive

rng = np.random.default_rng(42)
patients = pd.Series(np.arange(1, 31), name="patient")
actual_charge = pd.Series(
    rng.uniform(8, 60, 30).round(1), name="actual_charge_kusd"
).sort_values().reset_index(drop=True)
predicted_charge = pd.Series(
    actual_charge + rng.normal(0, 4.5, 30), name="predicted_charge_kusd"
)

fig = prediction_interval_plot_interactive(
    actual_charge, predicted_charge, confidence=0.90, method="empirical",
    title="Hospital charge model: 90% prediction intervals",
    point_color="#2a6f97", band_color="rgba(168,213,229,0.5)",
    line_color="#d62728", template="plotly_white",
)
fig.show()''',
    "dataviz.regression.prediction_extended.error_by_magnitude_plot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.prediction_extended import error_by_magnitude_plot_static

rng = np.random.default_rng(42)
stores = pd.Series([f"Store {s:02d}" for s in range(1, 41)], name="store")
actual_revenue = pd.Series(
    rng.uniform(50, 900, 40).round(0), name="actual_revenue_kusd"
)
predicted_revenue = pd.Series(
    actual_revenue * rng.normal(1.0, 0.08, 40) + rng.normal(0, 15, 40),
    name="predicted_revenue_kusd",
)

ax = error_by_magnitude_plot_static(
    actual_revenue, predicted_revenue, n_bins=8,
    title="Store revenue model: MAE by revenue magnitude",
    color="#4878d0", line_color="#d62728", theme="minimal",
)
ax.set_xlabel("Actual revenue midpoint (kUSD)")
plt.show()''',
    "dataviz.regression.prediction_extended.error_by_magnitude_plot_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.prediction_extended import error_by_magnitude_plot_interactive

rng = np.random.default_rng(42)
stores = pd.Series([f"Store {s:02d}" for s in range(1, 41)], name="store")
actual_revenue = pd.Series(
    rng.uniform(50, 900, 40).round(0), name="actual_revenue_kusd"
)
predicted_revenue = pd.Series(
    actual_revenue * rng.normal(1.0, 0.08, 40) + rng.normal(0, 15, 40),
    name="predicted_revenue_kusd",
)

fig = error_by_magnitude_plot_interactive(
    actual_revenue, predicted_revenue, n_bins=8,
    title="Store revenue model: MAE by revenue magnitude",
    color="#4878d0", line_color="#d62728", template="plotly_white",
)
fig.show()''',
    # ------------------------------------------------------------------
    # quantile
    # ------------------------------------------------------------------
    "dataviz.regression.quantile.quantile_regression_band_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.quantile import quantile_regression_band_static

rng = np.random.default_rng(42)
distance_km = pd.Series(rng.uniform(2, 60, 25).round(1), name="distance_km")
delivery_min = pd.Series(
    8 + 1.6 * distance_km + rng.gamma(2.0, 3.0, 25), name="delivery_min"
)
q10 = 6 + 1.45 * distance_km
q50 = 8 + 1.60 * distance_km
q90 = 11 + 1.85 * distance_km

ax = quantile_regression_band_static(
    distance_km, delivery_min, q10, q50, q90,
    title="Courier delivery time: 10/50/90% quantile band",
    color="#2a6f97", band_color="#a8d5e5", theme="minimal",
)
ax.set_xlabel("Distance (km)")
ax.set_ylabel("Delivery time (min)")
plt.show()''',
    "dataviz.regression.quantile.quantile_regression_band_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.quantile import quantile_regression_band_interactive

rng = np.random.default_rng(42)
distance_km = pd.Series(rng.uniform(2, 60, 25).round(1), name="distance_km")
delivery_min = pd.Series(
    8 + 1.6 * distance_km + rng.gamma(2.0, 3.0, 25), name="delivery_min"
)
q10 = 6 + 1.45 * distance_km
q50 = 8 + 1.60 * distance_km
q90 = 11 + 1.85 * distance_km

fig = quantile_regression_band_interactive(
    distance_km, delivery_min, q10, q50, q90,
    title="Courier delivery time: 10/50/90% quantile band",
    color="#2a6f97", band_color="rgba(168,213,229,0.5)",
    template="plotly_white",
)
fig.show()''',
    "dataviz.regression.quantile.quantile_loss_curve_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.quantile import quantile_loss_curve_static

rng = np.random.default_rng(42)
quantiles = pd.Series(np.round(np.arange(0.05, 0.96, 0.05), 2), name="tau")
residual_sample = rng.normal(0, 2.5, 400)
losses = pd.Series(
    [np.mean(np.maximum(t * residual_sample, (t - 1) * residual_sample))
     for t in quantiles],
    name="pinball_loss",
)

ax = quantile_loss_curve_static(
    quantiles, losses,
    title="Demand forecasting: pinball loss by quantile level",
    color="#6a4c93", theme="minimal",
)
ax.set_xlabel("Quantile level (tau)")
plt.show()''',
    "dataviz.regression.quantile.quantile_loss_curve_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.quantile import quantile_loss_curve_interactive

rng = np.random.default_rng(42)
quantiles = pd.Series(np.round(np.arange(0.05, 0.96, 0.05), 2), name="tau")
residual_sample = rng.normal(0, 2.5, 400)
losses = pd.Series(
    [np.mean(np.maximum(t * residual_sample, (t - 1) * residual_sample))
     for t in quantiles],
    name="pinball_loss",
)

fig = quantile_loss_curve_interactive(
    quantiles, losses,
    title="Demand forecasting: pinball loss by quantile level",
    color="#6a4c93", template="plotly_white",
)
fig.show()''',
    "dataviz.regression.quantile.huber_vs_ols_overlay_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.quantile import huber_vs_ols_overlay_static

rng = np.random.default_rng(42)
experience_yr = pd.Series(rng.uniform(0, 25, 24).round(1), name="experience_yr")
salary_kusd = pd.Series(
    45 + 3.2 * experience_yr + rng.normal(0, 6, 24), name="salary_kusd"
)
salary_kusd.iloc[[3, 11]] += 55  # executive outliers
ols_coef = np.polyfit(experience_yr, salary_kusd, 1)
y_ols = pd.Series(np.polyval(ols_coef, experience_yr), name="ols_fit")
weights = np.ones(24)
for _ in range(8):
    resid = salary_kusd.to_numpy() - np.polyval(ols_coef, experience_yr)
    scale = max(1.345 * np.median(np.abs(resid)) / 0.6745, 1e-6)
    weights = np.minimum(1.0, scale / np.maximum(np.abs(resid), 1e-9))
    w_fit = np.polyfit(experience_yr, salary_kusd, 1, w=weights)
    ols_coef_huber = w_fit
y_huber = pd.Series(np.polyval(ols_coef_huber, experience_yr), name="huber_fit")

ax = huber_vs_ols_overlay_static(
    experience_yr, salary_kusd, y_ols, y_huber,
    title="Compensation study: Huber vs OLS with outliers",
    ols_color="#4878d0", huber_color="#d62728", theme="minimal",
)
ax.set_xlabel("Experience (years)")
ax.set_ylabel("Salary (kUSD)")
plt.show()''',
    "dataviz.regression.quantile.huber_vs_ols_overlay_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.quantile import huber_vs_ols_overlay_interactive

rng = np.random.default_rng(42)
experience_yr = pd.Series(rng.uniform(0, 25, 24).round(1), name="experience_yr")
salary_kusd = pd.Series(
    45 + 3.2 * experience_yr + rng.normal(0, 6, 24), name="salary_kusd"
)
salary_kusd.iloc[[3, 11]] += 55  # executive outliers
ols_coef = np.polyfit(experience_yr, salary_kusd, 1)
y_ols = pd.Series(np.polyval(ols_coef, experience_yr), name="ols_fit")
weights = np.ones(24)
for _ in range(8):
    resid = salary_kusd.to_numpy() - np.polyval(ols_coef, experience_yr)
    scale = max(1.345 * np.median(np.abs(resid)) / 0.6745, 1e-6)
    weights = np.minimum(1.0, scale / np.maximum(np.abs(resid), 1e-9))
    w_fit = np.polyfit(experience_yr, salary_kusd, 1, w=weights)
    ols_coef_huber = w_fit
y_huber = pd.Series(np.polyval(ols_coef_huber, experience_yr), name="huber_fit")

fig = huber_vs_ols_overlay_interactive(
    experience_yr, salary_kusd, y_ols, y_huber,
    title="Compensation study: Huber vs OLS with outliers",
    ols_color="#4878d0", huber_color="#d62728", template="plotly_white",
)
fig.show()''',
    "dataviz.regression.quantile.weighted_residual_plot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.quantile import weighted_residual_plot_static

rng = np.random.default_rng(42)
towns = pd.Series(np.arange(1, 26), name="town")
predicted_cases = pd.Series(rng.uniform(20, 220, 25).round(1), name="predicted")
residuals = pd.Series(rng.normal(0, 14, 25).round(2), name="residual")
sample_size = pd.Series(rng.integers(120, 4000, 25), name="survey_n")
weights = sample_size / sample_size.max()

ax = weighted_residual_plot_static(
    predicted_cases, residuals, weights,
    title="Epidemiology survey: residuals weighted by sample size",
    cmap="plasma", theme="minimal",
)
ax.set_xlabel("Predicted weekly cases")
plt.show()''',
    "dataviz.regression.quantile.weighted_residual_plot_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.quantile import weighted_residual_plot_interactive

rng = np.random.default_rng(42)
towns = pd.Series(np.arange(1, 26), name="town")
predicted_cases = pd.Series(rng.uniform(20, 220, 25).round(1), name="predicted")
residuals = pd.Series(rng.normal(0, 14, 25).round(2), name="residual")
sample_size = pd.Series(rng.integers(120, 4000, 25), name="survey_n")
weights = sample_size / sample_size.max()

fig = weighted_residual_plot_interactive(
    predicted_cases, residuals, weights,
    title="Epidemiology survey: residuals weighted by sample size",
    colorscale="Plasma", template="plotly_white",
)
fig.show()''',
    # ------------------------------------------------------------------
    # regularization
    # ------------------------------------------------------------------
    "dataviz.regression.regularization.compute_regularization_path": '''import numpy as np
import pandas as pd
from dataviz.regression.regularization import compute_regularization_path

rng = np.random.default_rng(42)
n = 30
promo = rng.uniform(0, 10, n)
stores = pd.DataFrame({
    "price_index": rng.normal(100, 8, n),
    "promo_depth_pct": promo,
    "shelf_share_pct": 30 + 2 * promo + rng.normal(0, 3, n),
    "competitor_dist_km": rng.uniform(0.2, 12, n),
    "foot_traffic_k": rng.normal(4.5, 1.2, n),
    "online_ads_k": rng.normal(1.8, 0.7, n),
})
weekly_sales = pd.Series(
    120 - 1.1 * stores["price_index"] + 6.0 * promo
    + 2.5 * stores["foot_traffic_k"] + rng.normal(0, 9, n),
    name="weekly_sales_k",
)

alphas, coefs = compute_regularization_path(
    stores, weekly_sales, n_alphas=40, l1_ratio=1.0
)
result = {"alphas": np.round(alphas, 4), "coef_shape": coefs.shape}
print(result)''',
    "dataviz.regression.regularization.lasso_path_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.regularization import lasso_path_static

rng = np.random.default_rng(42)
n = 30
promo = rng.uniform(0, 10, n)
stores = pd.DataFrame({
    "price_index": rng.normal(100, 8, n),
    "promo_depth_pct": promo,
    "shelf_share_pct": 30 + 2 * promo + rng.normal(0, 3, n),
    "competitor_dist_km": rng.uniform(0.2, 12, n),
    "foot_traffic_k": rng.normal(4.5, 1.2, n),
    "online_ads_k": rng.normal(1.8, 0.7, n),
})
weekly_sales = pd.Series(
    120 - 1.1 * stores["price_index"] + 6.0 * promo
    + 2.5 * stores["foot_traffic_k"] + rng.normal(0, 9, n),
    name="weekly_sales_k",
)

ax = lasso_path_static(
    stores, weekly_sales, feature_names=list(stores.columns), n_alphas=40,
    title="Retail sales drivers: lasso coefficient path",
    cmap="tab10", theme="minimal",
)
ax.set_ylabel("Coefficient (kUSD per unit)")
plt.show()''',
    "dataviz.regression.regularization.lasso_path_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.regularization import lasso_path_interactive

rng = np.random.default_rng(42)
n = 30
promo = rng.uniform(0, 10, n)
stores = pd.DataFrame({
    "price_index": rng.normal(100, 8, n),
    "promo_depth_pct": promo,
    "shelf_share_pct": 30 + 2 * promo + rng.normal(0, 3, n),
    "competitor_dist_km": rng.uniform(0.2, 12, n),
    "foot_traffic_k": rng.normal(4.5, 1.2, n),
    "online_ads_k": rng.normal(1.8, 0.7, n),
})
weekly_sales = pd.Series(
    120 - 1.1 * stores["price_index"] + 6.0 * promo
    + 2.5 * stores["foot_traffic_k"] + rng.normal(0, 9, n),
    name="weekly_sales_k",
)

fig = lasso_path_interactive(
    stores, weekly_sales, feature_names=list(stores.columns), n_alphas=40,
    title="Retail sales drivers: lasso coefficient path",
    template="plotly_white",
)
fig.show()''',
    "dataviz.regression.regularization.ridge_path_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.regularization import ridge_path_static

rng = np.random.default_rng(42)
n = 32
load = rng.normal(300, 55, n)
sensors = pd.DataFrame({
    "bearing_temp_c": 55 + 0.09 * load + rng.normal(0, 1.5, n),
    "vibration_mms": 1.2 + 0.012 * load + rng.normal(0, 0.3, n),
    "oil_pressure_kpa": 420 - 0.35 * load + rng.normal(0, 9, n),
    "rpm": 1200 + 2.1 * load + rng.normal(0, 25, n),
    "ambient_c": rng.normal(22, 2.5, n),
})
energy_kwh = pd.Series(
    40 + 0.55 * sensors["bearing_temp_c"]
    + 6.0 * sensors["vibration_mms"] + rng.normal(0, 3, n),
    name="energy_kwh",
)

ax = ridge_path_static(
    sensors, energy_kwh, feature_names=list(sensors.columns), n_alphas=40,
    title="Turbine energy model: ridge coefficient path",
    cmap="tab10", theme="minimal",
)
plt.show()''',
    "dataviz.regression.regularization.ridge_path_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.regularization import ridge_path_interactive

rng = np.random.default_rng(42)
n = 32
load = rng.normal(300, 55, n)
sensors = pd.DataFrame({
    "bearing_temp_c": 55 + 0.09 * load + rng.normal(0, 1.5, n),
    "vibration_mms": 1.2 + 0.012 * load + rng.normal(0, 0.3, n),
    "oil_pressure_kpa": 420 - 0.35 * load + rng.normal(0, 9, n),
    "rpm": 1200 + 2.1 * load + rng.normal(0, 25, n),
    "ambient_c": rng.normal(22, 2.5, n),
})
energy_kwh = pd.Series(
    40 + 0.55 * sensors["bearing_temp_c"]
    + 6.0 * sensors["vibration_mms"] + rng.normal(0, 3, n),
    name="energy_kwh",
)

fig = ridge_path_interactive(
    sensors, energy_kwh, feature_names=list(sensors.columns), n_alphas=40,
    title="Turbine energy model: ridge coefficient path",
    template="plotly_white",
)
fig.show()''',
    "dataviz.regression.regularization.regularization_validation_plot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.regularization import regularization_validation_plot_static

rng = np.random.default_rng(42)
alphas = pd.Series(np.geomspace(1e-4, 10.0, 16), name="alpha")
fold_scores = []
for a in alphas:
    bias = 0.06 * np.log10(a / 1e-4) ** 2
    variance = 0.10 / (1 + 25 * a)
    fold_scores.append(0.92 - bias - variance + rng.normal(0, 0.015, 5))
test_scores = np.array(fold_scores)
train_scores = test_scores + 0.04 + rng.normal(0, 0.005, test_scores.shape)

ax = regularization_validation_plot_static(
    alphas, train_scores, test_scores, score_name="R-squared",
    title="Pricing model: ridge validation curve (5-fold CV)",
    train_color="#4878d0", test_color="#d62728", theme="minimal",
)
plt.show()''',
    "dataviz.regression.regularization.regularization_validation_plot_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.regularization import regularization_validation_plot_interactive

rng = np.random.default_rng(42)
alphas = pd.Series(np.geomspace(1e-4, 10.0, 16), name="alpha")
fold_scores = []
for a in alphas:
    bias = 0.06 * np.log10(a / 1e-4) ** 2
    variance = 0.10 / (1 + 25 * a)
    fold_scores.append(0.92 - bias - variance + rng.normal(0, 0.015, 5))
test_scores = np.array(fold_scores)
train_scores = test_scores + 0.04 + rng.normal(0, 0.005, test_scores.shape)

fig = regularization_validation_plot_interactive(
    alphas, train_scores, test_scores, score_name="R-squared",
    title="Pricing model: ridge validation curve (5-fold CV)",
    train_color="#4878d0", test_color="#d62728", template="plotly_white",
)
fig.show()''',
    # ------------------------------------------------------------------
    # residual
    # ------------------------------------------------------------------
    "dataviz.regression.residual.residual_plot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.residual import residual_plot_static

rng = np.random.default_rng(42)
homes = pd.Series(np.arange(1, 23), name="listing")
actual_price = pd.Series(
    rng.uniform(180, 850, 22).round(0), name="actual_price_kusd"
)
predicted_price = pd.Series(
    actual_price + rng.normal(0, 32, 22) + 0.05 * (actual_price - 500),
    name="predicted_price_kusd",
)

ax = residual_plot_static(
    actual_price, predicted_price,
    title="Home appraisal model: residual diagnostics",
    color="#2a6f97", marker_size=70, alpha=0.8,
    line_color="#d62728", theme="minimal",
)
ax.set_xlabel("Predicted price (kUSD)")
ax.set_ylabel("Residual (kUSD)")
plt.show()''',
    "dataviz.regression.residual.residual_plot_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.residual import residual_plot_interactive

rng = np.random.default_rng(42)
homes = pd.Series(np.arange(1, 23), name="listing")
actual_price = pd.Series(
    rng.uniform(180, 850, 22).round(0), name="actual_price_kusd"
)
predicted_price = pd.Series(
    actual_price + rng.normal(0, 32, 22) + 0.05 * (actual_price - 500),
    name="predicted_price_kusd",
)

fig = residual_plot_interactive(
    actual_price, predicted_price,
    title="Home appraisal model: residual diagnostics",
    marker_color="#2a6f97", marker_size=10,
    line_color="#d62728", template="plotly_white",
)
fig.show()''',
    # ------------------------------------------------------------------
    # residual_extended
    # ------------------------------------------------------------------
    "dataviz.regression.residual_extended.residual_histogram_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.residual_extended import residual_histogram_static

rng = np.random.default_rng(42)
patients = pd.Series(np.arange(1, 41), name="patient")
actual_bp = pd.Series(rng.normal(128, 14, 40).round(1), name="actual_sbp")
predicted_bp = pd.Series(
    actual_bp + rng.normal(0, 6.5, 40), name="predicted_sbp"
)

ax = residual_histogram_static(
    actual_bp, predicted_bp, bins=12,
    title="Blood-pressure model: residual distribution",
    color="#4878d0", edgecolor="white", overlay_color="#d62728",
    theme="minimal",
)
ax.set_xlabel("Residual (mmHg)")
plt.show()''',
    "dataviz.regression.residual_extended.residual_histogram_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.residual_extended import residual_histogram_interactive

rng = np.random.default_rng(42)
patients = pd.Series(np.arange(1, 41), name="patient")
actual_bp = pd.Series(rng.normal(128, 14, 40).round(1), name="actual_sbp")
predicted_bp = pd.Series(
    actual_bp + rng.normal(0, 6.5, 40), name="predicted_sbp"
)

fig = residual_histogram_interactive(
    actual_bp, predicted_bp, bins=12,
    title="Blood-pressure model: residual distribution",
    color="#4878d0", overlay_color="#d62728", template="plotly_white",
)
fig.show()''',
    "dataviz.regression.residual_extended.residual_density_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.residual_extended import residual_density_static

rng = np.random.default_rng(42)
flights = pd.Series(np.arange(1, 51), name="flight")
actual_delay = pd.Series(rng.normal(12, 18, 50).round(1), name="actual_delay_min")
predicted_delay = pd.Series(
    actual_delay + rng.laplace(0, 6, 50), name="predicted_delay_min"
)

ax = residual_density_static(
    actual_delay, predicted_delay, bandwidth=4.0,
    title="Flight delay model: residual kernel density",
    color="#6a4c93", fill_alpha=0.35, theme="minimal",
)
ax.set_xlabel("Residual (min)")
plt.show()''',
    "dataviz.regression.residual_extended.residual_density_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.residual_extended import residual_density_interactive

rng = np.random.default_rng(42)
flights = pd.Series(np.arange(1, 51), name="flight")
actual_delay = pd.Series(rng.normal(12, 18, 50).round(1), name="actual_delay_min")
predicted_delay = pd.Series(
    actual_delay + rng.laplace(0, 6, 50), name="predicted_delay_min"
)

fig = residual_density_interactive(
    actual_delay, predicted_delay, bandwidth=4.0,
    title="Flight delay model: residual kernel density",
    color="#6a4c93", template="plotly_white",
)
fig.show()''',
    "dataviz.regression.residual_extended.residual_qq_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.residual_extended import residual_qq_static

rng = np.random.default_rng(42)
wells = pd.Series(np.arange(1, 31), name="well")
actual_flow = pd.Series(rng.normal(540, 80, 30).round(1), name="actual_bpd")
predicted_flow = pd.Series(
    actual_flow + rng.normal(0, 35, 30), name="predicted_bpd"
)

ax = residual_qq_static(
    actual_flow, predicted_flow,
    title="Oil well flow model: normal Q-Q of residuals",
    marker_color="#1b9e77", line_color="#d62728", theme="minimal",
)
plt.show()''',
    "dataviz.regression.residual_extended.residual_qq_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.residual_extended import residual_qq_interactive

rng = np.random.default_rng(42)
wells = pd.Series(np.arange(1, 31), name="well")
actual_flow = pd.Series(rng.normal(540, 80, 30).round(1), name="actual_bpd")
predicted_flow = pd.Series(
    actual_flow + rng.normal(0, 35, 30), name="predicted_bpd"
)

fig = residual_qq_interactive(
    actual_flow, predicted_flow,
    title="Oil well flow model: normal Q-Q of residuals",
    marker_color="#1b9e77", line_color="#d62728", template="plotly_white",
)
fig.show()''',
    "dataviz.regression.residual_extended.residual_boxplot_by_group_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.residual_extended import residual_boxplot_by_group_static

rng = np.random.default_rng(42)
n = 36
shifts = pd.Series(np.repeat(["Day", "Swing", "Night"], 12), name="shift")
actual_output = pd.Series(rng.normal(480, 45, n).round(0), name="actual_units")
shift_bias = shifts.map({"Day": 4.0, "Swing": -2.0, "Night": -9.0})
predicted_output = pd.Series(
    actual_output + shift_bias + rng.normal(0, 18, n), name="predicted_units"
)

ax = residual_boxplot_by_group_static(
    actual_output, predicted_output, shifts,
    title="Factory output model: residuals by shift",
    color="#4878d0", theme="minimal",
)
plt.show()''',
    "dataviz.regression.residual_extended.residual_boxplot_by_group_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.residual_extended import residual_boxplot_by_group_interactive

rng = np.random.default_rng(42)
n = 36
shifts = pd.Series(np.repeat(["Day", "Swing", "Night"], 12), name="shift")
actual_output = pd.Series(rng.normal(480, 45, n).round(0), name="actual_units")
shift_bias = shifts.map({"Day": 4.0, "Swing": -2.0, "Night": -9.0})
predicted_output = pd.Series(
    actual_output + shift_bias + rng.normal(0, 18, n), name="predicted_units"
)

fig = residual_boxplot_by_group_interactive(
    actual_output, predicted_output, shifts,
    title="Factory output model: residuals by shift",
    color="#4878d0", template="plotly_white",
)
fig.show()''',
    "dataviz.regression.residual_extended.standardized_residual_plot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.residual_extended import standardized_residual_plot_static

rng = np.random.default_rng(42)
claims = pd.Series(np.arange(1, 33), name="claim")
actual_payout = pd.Series(
    rng.uniform(2, 95, 32).round(1), name="actual_payout_kusd"
)
predicted_payout = pd.Series(
    actual_payout + rng.normal(0, 5, 32), name="predicted_payout_kusd"
)
predicted_payout.iloc[7] -= 28  # flagged outlier claim

ax = standardized_residual_plot_static(
    actual_payout, predicted_payout, bound=2.0,
    title="Insurance payout model: standardized residuals",
    color="#ee854a", theme="minimal",
)
ax.set_xlabel("Predicted payout (kUSD)")
plt.show()''',
    "dataviz.regression.residual_extended.standardized_residual_plot_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.residual_extended import standardized_residual_plot_interactive

rng = np.random.default_rng(42)
claims = pd.Series(np.arange(1, 33), name="claim")
actual_payout = pd.Series(
    rng.uniform(2, 95, 32).round(1), name="actual_payout_kusd"
)
predicted_payout = pd.Series(
    actual_payout + rng.normal(0, 5, 32), name="predicted_payout_kusd"
)
predicted_payout.iloc[7] -= 28  # flagged outlier claim

fig = standardized_residual_plot_interactive(
    actual_payout, predicted_payout, bound=2.0,
    title="Insurance payout model: standardized residuals",
    color="#ee854a", template="plotly_white",
)
fig.show()''',
    "dataviz.regression.residual_extended.scale_location_plot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.regression.residual_extended import scale_location_plot_static

rng = np.random.default_rng(42)
orders = pd.Series(np.arange(1, 46), name="order")
actual_cost = pd.Series(
    rng.uniform(20, 400, 45).round(1), name="actual_cost_usd"
)
hetero_noise = rng.normal(0, 1, 45) * (4 + 0.05 * actual_cost)
predicted_cost = pd.Series(actual_cost + hetero_noise, name="predicted_cost_usd")

ax = scale_location_plot_static(
    actual_cost, predicted_cost,
    title="Shipping cost model: scale-location check",
    color="#4878d0", trend_color="#d62728", theme="minimal",
)
ax.set_xlabel("Predicted cost (USD)")
plt.show()''',
    "dataviz.regression.residual_extended.scale_location_plot_interactive": '''import numpy as np
import pandas as pd
from dataviz.regression.residual_extended import scale_location_plot_interactive

rng = np.random.default_rng(42)
orders = pd.Series(np.arange(1, 46), name="order")
actual_cost = pd.Series(
    rng.uniform(20, 400, 45).round(1), name="actual_cost_usd"
)
hetero_noise = rng.normal(0, 1, 45) * (4 + 0.05 * actual_cost)
predicted_cost = pd.Series(actual_cost + hetero_noise, name="predicted_cost_usd")

fig = scale_location_plot_interactive(
    actual_cost, predicted_cost,
    title="Shipping cost model: scale-location check",
    color="#4878d0", trend_color="#d62728", template="plotly_white",
)
fig.show()''',
}
