"""Regression analysis visualizations - static and interactive versions.

This sub-package collects a comprehensive toolbox of regression diagnostics.
All chart families ship with both a ``*_static`` (matplotlib) and a
``*_interactive`` (Plotly) implementation, plus a no-suffix alias that
defaults to the static variant. See the module README for usage examples.
"""

# ---------------------------------------------------------------------------
# Core (legacy entry points)
# ---------------------------------------------------------------------------
from .residual import residual_plot_static, residual_plot_interactive
from .prediction import prediction_plot_static, prediction_plot_interactive
from .learning import learning_curve_static, learning_curve_interactive

# ---------------------------------------------------------------------------
# Shared compute helpers
# ---------------------------------------------------------------------------
from .helpers import (
    RegressionMetrics,
    InfluenceStatistics,
    compute_regression_metrics,
    influence_statistics,
    prediction_intervals,
    coefficient_table,
    autocorrelation,
    partial_autocorrelation,
    runs_test_signs,
)

# ---------------------------------------------------------------------------
# Residual diagnostics (extended)
# ---------------------------------------------------------------------------
from .residual_extended import (
    residual_histogram_static, residual_histogram_interactive,
    residual_density_static, residual_density_interactive,
    residual_qq_static, residual_qq_interactive,
    residual_boxplot_by_group_static, residual_boxplot_by_group_interactive,
    standardized_residual_plot_static, standardized_residual_plot_interactive,
    scale_location_plot_static, scale_location_plot_interactive,
)

# ---------------------------------------------------------------------------
# Residual vs feature diagnostics
# ---------------------------------------------------------------------------
from .residual_features import (
    residual_vs_feature_static, residual_vs_feature_interactive,
    partial_residual_plot_static, partial_residual_plot_interactive,
    ccpr_plot_static, ccpr_plot_interactive,
    added_variable_plot_static, added_variable_plot_interactive,
)

# ---------------------------------------------------------------------------
# Autocorrelation and time-ordered diagnostics
# ---------------------------------------------------------------------------
from .autocorrelation import (
    residual_acf_static, residual_acf_interactive,
    residual_pacf_static, residual_pacf_interactive,
    residual_runs_plot_static, residual_runs_plot_interactive,
    residual_time_plot_static, residual_time_plot_interactive,
)

# ---------------------------------------------------------------------------
# Prediction diagnostics (extended)
# ---------------------------------------------------------------------------
from .prediction_extended import (
    pred_vs_actual_hexbin_static, pred_vs_actual_hexbin_interactive,
    pred_vs_actual_density_static, pred_vs_actual_density_interactive,
    prediction_error_histogram_static, prediction_error_histogram_interactive,
    prediction_interval_plot_static, prediction_interval_plot_interactive,
    error_by_magnitude_plot_static, error_by_magnitude_plot_interactive,
)

# ---------------------------------------------------------------------------
# Influence diagnostics
# ---------------------------------------------------------------------------
from .influence import (
    leverage_plot_static, leverage_plot_interactive,
    cooks_distance_plot_static, cooks_distance_plot_interactive,
    influence_bubble_plot_static, influence_bubble_plot_interactive,
    dfbetas_plot_static, dfbetas_plot_interactive,
)

# ---------------------------------------------------------------------------
# Coefficient visualizations
# ---------------------------------------------------------------------------
from .coefficients import (
    coefficient_plot_static, coefficient_plot_interactive,
    coefficient_forest_plot_static, coefficient_forest_plot_interactive,
    standardized_coefficient_plot_static, standardized_coefficient_plot_interactive,
    coefficient_path_plot_static, coefficient_path_plot_interactive,
)

# ---------------------------------------------------------------------------
# Feature importance
# ---------------------------------------------------------------------------
from .importance import (
    feature_importance_regression_static, feature_importance_regression_interactive,
    permutation_importance_regression_static, permutation_importance_regression_interactive,
)

# ---------------------------------------------------------------------------
# Regularization paths
# ---------------------------------------------------------------------------
from .regularization import (
    compute_regularization_path,
    lasso_path_static, lasso_path_interactive,
    ridge_path_static, ridge_path_interactive,
    regularization_validation_plot_static, regularization_validation_plot_interactive,
)

# ---------------------------------------------------------------------------
# Metric visualizations
# ---------------------------------------------------------------------------
from .metrics import (
    regression_metrics_bar_static, regression_metrics_bar_interactive,
    metric_comparison_bar_static, metric_comparison_bar_interactive,
    metric_radar_static, metric_radar_interactive,
    per_segment_metrics_heatmap_static, per_segment_metrics_heatmap_interactive,
)

# ---------------------------------------------------------------------------
# Validation / training curves
# ---------------------------------------------------------------------------
from .validation import (
    validation_curve_static, validation_curve_interactive,
    training_history_static, training_history_interactive,
    cv_score_plot_static, cv_score_plot_interactive,
    bias_variance_plot_static, bias_variance_plot_interactive,
)

# ---------------------------------------------------------------------------
# Calibration / uncertainty
# ---------------------------------------------------------------------------
from .calibration_regression import (
    calibration_curve_regression_static, calibration_curve_regression_interactive,
    prediction_interval_coverage_plot_static, prediction_interval_coverage_plot_interactive,
    uncertainty_band_plot_static, uncertainty_band_plot_interactive,
)

# ---------------------------------------------------------------------------
# Composite diagnostic panels
# ---------------------------------------------------------------------------
from .diagnostics_panel import (
    regression_diagnostic_panel_static, regression_diagnostic_panel_interactive,
    regression_dashboard_static, regression_dashboard_interactive,
)

# ---------------------------------------------------------------------------
# Batch-2 helpers
# ---------------------------------------------------------------------------
from .helpers import (
    variance_inflation_factors,
    breusch_pagan_statistic,
    white_test_statistic,
    ljung_box_statistic,
    jarque_bera_statistic,
    durbin_watson_statistic,
    box_cox_loglikelihood,
    yeo_johnson_loglikelihood,
    conformal_quantile,
    jackknife_plus_intervals,
)

# ---------------------------------------------------------------------------
# Batch-2 chart modules
# ---------------------------------------------------------------------------
from .glm import (
    link_function_plot_static, link_function_plot_interactive,
    deviance_residual_plot_static, deviance_residual_plot_interactive,
    pearson_residual_plot_static, pearson_residual_plot_interactive,
    working_residual_plot_static, working_residual_plot_interactive,
    variance_function_plot_static, variance_function_plot_interactive,
    glm_diagnostic_panel_static, glm_diagnostic_panel_interactive,
)
from .quantile import (
    quantile_regression_band_static, quantile_regression_band_interactive,
    quantile_loss_curve_static, quantile_loss_curve_interactive,
    huber_vs_ols_overlay_static, huber_vs_ols_overlay_interactive,
    weighted_residual_plot_static, weighted_residual_plot_interactive,
)
from .survival import (
    km_predicted_vs_observed_static, km_predicted_vs_observed_interactive,
    cox_residual_plot_static, cox_residual_plot_interactive,
    proportional_hazards_test_plot_static, proportional_hazards_test_plot_interactive,
)
from .forecast import (
    forecast_vs_actual_static, forecast_vs_actual_interactive,
    forecast_error_over_horizon_static, forecast_error_over_horizon_interactive,
    rolling_forecast_origin_static, rolling_forecast_origin_interactive,
    backtest_error_distribution_static, backtest_error_distribution_interactive,
    expanding_window_metric_curve_static, expanding_window_metric_curve_interactive,
    forecast_band_plot_static, forecast_band_plot_interactive,
)
from .spatial import (
    spatial_residual_map_static, spatial_residual_map_interactive,
    moran_scatter_static, moran_scatter_interactive,
    panel_residual_heatmap_static, panel_residual_heatmap_interactive,
)
from .multicollinearity import (
    vif_bar_static, vif_bar_interactive,
    condition_index_plot_static, condition_index_plot_interactive,
    correlation_heatmap_with_clustering_static, correlation_heatmap_with_clustering_interactive,
    eigenvalue_scree_predictors_static, eigenvalue_scree_predictors_interactive,
    tolerance_bar_static, tolerance_bar_interactive,
)
from .effects import (
    partial_dependence_regression_static, partial_dependence_regression_interactive,
    ice_plot_regression_static, ice_plot_regression_interactive,
    marginal_effects_plot_static, marginal_effects_plot_interactive,
    interaction_effect_plot_static, interaction_effect_plot_interactive,
    conditional_expectation_curve_static, conditional_expectation_curve_interactive,
    elasticity_plot_static, elasticity_plot_interactive,
)
from .gof import (
    normality_test_panel_static, normality_test_panel_interactive,
    breusch_pagan_plot_static, breusch_pagan_plot_interactive,
    white_test_plot_static, white_test_plot_interactive,
    durbin_watson_gauge_static, durbin_watson_gauge_interactive,
    ljung_box_plot_static, ljung_box_plot_interactive,
    residual_dependence_test_panel_static, residual_dependence_test_panel_interactive,
)
from .selection import (
    aic_bic_bar_static, aic_bic_bar_interactive,
    nested_model_comparison_plot_static, nested_model_comparison_plot_interactive,
    stepwise_selection_path_static, stepwise_selection_path_interactive,
    forward_selection_score_curve_static, forward_selection_score_curve_interactive,
    best_subset_metric_bar_static, best_subset_metric_bar_interactive,
)
from .cv_extended import (
    learning_curve_with_band_static, learning_curve_with_band_interactive,
    nested_cv_score_plot_static, nested_cv_score_plot_interactive,
    cv_residual_distribution_static, cv_residual_distribution_interactive,
    repeated_kfold_violin_static, repeated_kfold_violin_interactive,
    group_cv_score_strip_static, group_cv_score_strip_interactive,
)
from .uncertainty import (
    conformal_interval_plot_static, conformal_interval_plot_interactive,
    jackknife_plus_band_static, jackknife_plus_band_interactive,
    quantile_calibration_plot_static, quantile_calibration_plot_interactive,
    sharpness_vs_coverage_plot_static, sharpness_vs_coverage_plot_interactive,
    coverage_by_segment_bar_static, coverage_by_segment_bar_interactive,
)
from .errors_loss import (
    loss_distribution_violin_static, loss_distribution_violin_interactive,
    ranked_error_plot_static, ranked_error_plot_interactive,
    worst_k_predictions_chart_static, worst_k_predictions_chart_interactive,
    error_decomposition_bar_static, error_decomposition_bar_interactive,
)
from .mixed_effects import (
    random_effect_caterpillar_static, random_effect_caterpillar_interactive,
    random_intercept_slope_scatter_static, random_intercept_slope_scatter_interactive,
    group_means_vs_predicted_static, group_means_vs_predicted_interactive,
)
from .transforms import (
    boxcox_likelihood_curve_static, boxcox_likelihood_curve_interactive,
    yeojohnson_lambda_search_static, yeojohnson_lambda_search_interactive,
    log_log_diagnostic_static, log_log_diagnostic_interactive,
    power_transform_residual_panel_static, power_transform_residual_panel_interactive,
)
from .var_engineering import (
    target_vs_feature_smooth_grid_static, target_vs_feature_smooth_grid_interactive,
    feature_target_correlation_bar_static, feature_target_correlation_bar_interactive,
    target_encoding_curve_static, target_encoding_curve_interactive,
)
from .bayesian import (
    posterior_coefficient_density_static, posterior_coefficient_density_interactive,
    posterior_predictive_check_static, posterior_predictive_check_interactive,
    trace_plot_coefficients_static, trace_plot_coefficients_interactive,
    credible_interval_forest_static, credible_interval_forest_interactive,
)
from .comparison import (
    multi_model_pred_vs_actual_overlay_static, multi_model_pred_vs_actual_overlay_interactive,
    residual_density_overlay_multi_static, residual_density_overlay_multi_interactive,
    error_ecdf_overlay_static, error_ecdf_overlay_interactive,
    model_winner_heatmap_static, model_winner_heatmap_interactive,
)
from .domain import (
    price_elasticity_curve_static, price_elasticity_curve_interactive,
    dose_response_curve_static, dose_response_curve_interactive,
    demand_forecast_fan_chart_static, demand_forecast_fan_chart_interactive,
    yield_curve_fit_plot_static, yield_curve_fit_plot_interactive,
)


# Convenience aliases (default to static implementations).
residual_plot = residual_plot_static
prediction_plot = prediction_plot_static
learning_curve = learning_curve_static
residual_histogram = residual_histogram_static
residual_density = residual_density_static
residual_qq = residual_qq_static
residual_boxplot_by_group = residual_boxplot_by_group_static
standardized_residual_plot = standardized_residual_plot_static
scale_location_plot = scale_location_plot_static
residual_vs_feature = residual_vs_feature_static
partial_residual_plot = partial_residual_plot_static
ccpr_plot = ccpr_plot_static
added_variable_plot = added_variable_plot_static
residual_acf = residual_acf_static
residual_pacf = residual_pacf_static
residual_runs_plot = residual_runs_plot_static
residual_time_plot = residual_time_plot_static
pred_vs_actual_hexbin = pred_vs_actual_hexbin_static
pred_vs_actual_density = pred_vs_actual_density_static
prediction_error_histogram = prediction_error_histogram_static
prediction_interval_plot = prediction_interval_plot_static
error_by_magnitude_plot = error_by_magnitude_plot_static
leverage_plot = leverage_plot_static
cooks_distance_plot = cooks_distance_plot_static
influence_bubble_plot = influence_bubble_plot_static
dfbetas_plot = dfbetas_plot_static
coefficient_plot = coefficient_plot_static
coefficient_forest_plot = coefficient_forest_plot_static
standardized_coefficient_plot = standardized_coefficient_plot_static
coefficient_path_plot = coefficient_path_plot_static
feature_importance_regression = feature_importance_regression_static
permutation_importance_regression = permutation_importance_regression_static
lasso_path = lasso_path_static
ridge_path = ridge_path_static
regularization_validation_plot = regularization_validation_plot_static
regression_metrics_bar = regression_metrics_bar_static
metric_comparison_bar = metric_comparison_bar_static
metric_radar = metric_radar_static
per_segment_metrics_heatmap = per_segment_metrics_heatmap_static
validation_curve = validation_curve_static
training_history = training_history_static
cv_score_plot = cv_score_plot_static
bias_variance_plot = bias_variance_plot_static
calibration_curve_regression = calibration_curve_regression_static
prediction_interval_coverage_plot = prediction_interval_coverage_plot_static
uncertainty_band_plot = uncertainty_band_plot_static
regression_diagnostic_panel = regression_diagnostic_panel_static
regression_dashboard = regression_dashboard_static

# Batch-2 aliases
link_function_plot = link_function_plot_static
deviance_residual_plot = deviance_residual_plot_static
pearson_residual_plot = pearson_residual_plot_static
working_residual_plot = working_residual_plot_static
variance_function_plot = variance_function_plot_static
glm_diagnostic_panel = glm_diagnostic_panel_static
quantile_regression_band = quantile_regression_band_static
quantile_loss_curve = quantile_loss_curve_static
huber_vs_ols_overlay = huber_vs_ols_overlay_static
weighted_residual_plot = weighted_residual_plot_static
km_predicted_vs_observed = km_predicted_vs_observed_static
cox_residual_plot = cox_residual_plot_static
proportional_hazards_test_plot = proportional_hazards_test_plot_static
forecast_vs_actual = forecast_vs_actual_static
forecast_error_over_horizon = forecast_error_over_horizon_static
rolling_forecast_origin = rolling_forecast_origin_static
backtest_error_distribution = backtest_error_distribution_static
expanding_window_metric_curve = expanding_window_metric_curve_static
forecast_band_plot = forecast_band_plot_static
spatial_residual_map = spatial_residual_map_static
moran_scatter = moran_scatter_static
panel_residual_heatmap = panel_residual_heatmap_static
vif_bar = vif_bar_static
condition_index_plot = condition_index_plot_static
correlation_heatmap_with_clustering = correlation_heatmap_with_clustering_static
eigenvalue_scree_predictors = eigenvalue_scree_predictors_static
tolerance_bar = tolerance_bar_static
partial_dependence_regression = partial_dependence_regression_static
ice_plot_regression = ice_plot_regression_static
marginal_effects_plot = marginal_effects_plot_static
interaction_effect_plot = interaction_effect_plot_static
conditional_expectation_curve = conditional_expectation_curve_static
elasticity_plot = elasticity_plot_static
normality_test_panel = normality_test_panel_static
breusch_pagan_plot = breusch_pagan_plot_static
white_test_plot = white_test_plot_static
durbin_watson_gauge = durbin_watson_gauge_static
ljung_box_plot = ljung_box_plot_static
residual_dependence_test_panel = residual_dependence_test_panel_static
aic_bic_bar = aic_bic_bar_static
nested_model_comparison_plot = nested_model_comparison_plot_static
stepwise_selection_path = stepwise_selection_path_static
forward_selection_score_curve = forward_selection_score_curve_static
best_subset_metric_bar = best_subset_metric_bar_static
learning_curve_with_band = learning_curve_with_band_static
nested_cv_score_plot = nested_cv_score_plot_static
cv_residual_distribution = cv_residual_distribution_static
repeated_kfold_violin = repeated_kfold_violin_static
group_cv_score_strip = group_cv_score_strip_static
conformal_interval_plot = conformal_interval_plot_static
jackknife_plus_band = jackknife_plus_band_static
quantile_calibration_plot = quantile_calibration_plot_static
sharpness_vs_coverage_plot = sharpness_vs_coverage_plot_static
coverage_by_segment_bar = coverage_by_segment_bar_static
loss_distribution_violin = loss_distribution_violin_static
ranked_error_plot = ranked_error_plot_static
worst_k_predictions_chart = worst_k_predictions_chart_static
error_decomposition_bar = error_decomposition_bar_static
random_effect_caterpillar = random_effect_caterpillar_static
random_intercept_slope_scatter = random_intercept_slope_scatter_static
group_means_vs_predicted = group_means_vs_predicted_static
boxcox_likelihood_curve = boxcox_likelihood_curve_static
yeojohnson_lambda_search = yeojohnson_lambda_search_static
log_log_diagnostic = log_log_diagnostic_static
power_transform_residual_panel = power_transform_residual_panel_static
target_vs_feature_smooth_grid = target_vs_feature_smooth_grid_static
feature_target_correlation_bar = feature_target_correlation_bar_static
target_encoding_curve = target_encoding_curve_static
posterior_coefficient_density = posterior_coefficient_density_static
posterior_predictive_check = posterior_predictive_check_static
trace_plot_coefficients = trace_plot_coefficients_static
credible_interval_forest = credible_interval_forest_static
multi_model_pred_vs_actual_overlay = multi_model_pred_vs_actual_overlay_static
residual_density_overlay_multi = residual_density_overlay_multi_static
error_ecdf_overlay = error_ecdf_overlay_static
model_winner_heatmap = model_winner_heatmap_static
price_elasticity_curve = price_elasticity_curve_static
dose_response_curve = dose_response_curve_static
demand_forecast_fan_chart = demand_forecast_fan_chart_static
yield_curve_fit_plot = yield_curve_fit_plot_static


__all__ = [
    # Helpers and result types
    "RegressionMetrics",
    "InfluenceStatistics",
    "compute_regression_metrics",
    "influence_statistics",
    "prediction_intervals",
    "coefficient_table",
    "autocorrelation",
    "partial_autocorrelation",
    "runs_test_signs",
    "compute_regularization_path",
    # Core static
    "residual_plot_static", "prediction_plot_static", "learning_curve_static",
    # Core interactive
    "residual_plot_interactive", "prediction_plot_interactive", "learning_curve_interactive",
    # Residual extended
    "residual_histogram_static", "residual_histogram_interactive",
    "residual_density_static", "residual_density_interactive",
    "residual_qq_static", "residual_qq_interactive",
    "residual_boxplot_by_group_static", "residual_boxplot_by_group_interactive",
    "standardized_residual_plot_static", "standardized_residual_plot_interactive",
    "scale_location_plot_static", "scale_location_plot_interactive",
    # Residual vs feature
    "residual_vs_feature_static", "residual_vs_feature_interactive",
    "partial_residual_plot_static", "partial_residual_plot_interactive",
    "ccpr_plot_static", "ccpr_plot_interactive",
    "added_variable_plot_static", "added_variable_plot_interactive",
    # Autocorrelation
    "residual_acf_static", "residual_acf_interactive",
    "residual_pacf_static", "residual_pacf_interactive",
    "residual_runs_plot_static", "residual_runs_plot_interactive",
    "residual_time_plot_static", "residual_time_plot_interactive",
    # Prediction extended
    "pred_vs_actual_hexbin_static", "pred_vs_actual_hexbin_interactive",
    "pred_vs_actual_density_static", "pred_vs_actual_density_interactive",
    "prediction_error_histogram_static", "prediction_error_histogram_interactive",
    "prediction_interval_plot_static", "prediction_interval_plot_interactive",
    "error_by_magnitude_plot_static", "error_by_magnitude_plot_interactive",
    # Influence
    "leverage_plot_static", "leverage_plot_interactive",
    "cooks_distance_plot_static", "cooks_distance_plot_interactive",
    "influence_bubble_plot_static", "influence_bubble_plot_interactive",
    "dfbetas_plot_static", "dfbetas_plot_interactive",
    # Coefficients
    "coefficient_plot_static", "coefficient_plot_interactive",
    "coefficient_forest_plot_static", "coefficient_forest_plot_interactive",
    "standardized_coefficient_plot_static", "standardized_coefficient_plot_interactive",
    "coefficient_path_plot_static", "coefficient_path_plot_interactive",
    # Importance
    "feature_importance_regression_static", "feature_importance_regression_interactive",
    "permutation_importance_regression_static", "permutation_importance_regression_interactive",
    # Regularization
    "lasso_path_static", "lasso_path_interactive",
    "ridge_path_static", "ridge_path_interactive",
    "regularization_validation_plot_static", "regularization_validation_plot_interactive",
    # Metrics
    "regression_metrics_bar_static", "regression_metrics_bar_interactive",
    "metric_comparison_bar_static", "metric_comparison_bar_interactive",
    "metric_radar_static", "metric_radar_interactive",
    "per_segment_metrics_heatmap_static", "per_segment_metrics_heatmap_interactive",
    # Validation
    "validation_curve_static", "validation_curve_interactive",
    "training_history_static", "training_history_interactive",
    "cv_score_plot_static", "cv_score_plot_interactive",
    "bias_variance_plot_static", "bias_variance_plot_interactive",
    # Calibration / uncertainty
    "calibration_curve_regression_static", "calibration_curve_regression_interactive",
    "prediction_interval_coverage_plot_static", "prediction_interval_coverage_plot_interactive",
    "uncertainty_band_plot_static", "uncertainty_band_plot_interactive",
    # Panels
    "regression_diagnostic_panel_static", "regression_diagnostic_panel_interactive",
    "regression_dashboard_static", "regression_dashboard_interactive",
    # Aliases
    "residual_plot", "prediction_plot", "learning_curve",
    "residual_histogram", "residual_density", "residual_qq",
    "residual_boxplot_by_group", "standardized_residual_plot",
    "scale_location_plot", "residual_vs_feature", "partial_residual_plot",
    "ccpr_plot", "added_variable_plot", "residual_acf", "residual_pacf",
    "residual_runs_plot", "residual_time_plot", "pred_vs_actual_hexbin",
    "pred_vs_actual_density", "prediction_error_histogram",
    "prediction_interval_plot", "error_by_magnitude_plot", "leverage_plot",
    "cooks_distance_plot", "influence_bubble_plot", "dfbetas_plot",
    "coefficient_plot", "coefficient_forest_plot",
    "standardized_coefficient_plot", "coefficient_path_plot",
    "feature_importance_regression", "permutation_importance_regression",
    "lasso_path", "ridge_path", "regularization_validation_plot",
    "regression_metrics_bar", "metric_comparison_bar", "metric_radar",
    "per_segment_metrics_heatmap", "validation_curve", "training_history",
    "cv_score_plot", "bias_variance_plot", "calibration_curve_regression",
    "prediction_interval_coverage_plot", "uncertainty_band_plot",
    "regression_diagnostic_panel", "regression_dashboard",
    # Batch-2 helpers
    "variance_inflation_factors", "breusch_pagan_statistic", "white_test_statistic",
    "ljung_box_statistic", "jarque_bera_statistic", "durbin_watson_statistic",
    "box_cox_loglikelihood", "yeo_johnson_loglikelihood", "conformal_quantile",
    "jackknife_plus_intervals",
    # GLM
    "link_function_plot_static", "link_function_plot_interactive",
    "deviance_residual_plot_static", "deviance_residual_plot_interactive",
    "pearson_residual_plot_static", "pearson_residual_plot_interactive",
    "working_residual_plot_static", "working_residual_plot_interactive",
    "variance_function_plot_static", "variance_function_plot_interactive",
    "glm_diagnostic_panel_static", "glm_diagnostic_panel_interactive",
    # Quantile / robust
    "quantile_regression_band_static", "quantile_regression_band_interactive",
    "quantile_loss_curve_static", "quantile_loss_curve_interactive",
    "huber_vs_ols_overlay_static", "huber_vs_ols_overlay_interactive",
    "weighted_residual_plot_static", "weighted_residual_plot_interactive",
    # Survival
    "km_predicted_vs_observed_static", "km_predicted_vs_observed_interactive",
    "cox_residual_plot_static", "cox_residual_plot_interactive",
    "proportional_hazards_test_plot_static", "proportional_hazards_test_plot_interactive",
    # Forecast
    "forecast_vs_actual_static", "forecast_vs_actual_interactive",
    "forecast_error_over_horizon_static", "forecast_error_over_horizon_interactive",
    "rolling_forecast_origin_static", "rolling_forecast_origin_interactive",
    "backtest_error_distribution_static", "backtest_error_distribution_interactive",
    "expanding_window_metric_curve_static", "expanding_window_metric_curve_interactive",
    "forecast_band_plot_static", "forecast_band_plot_interactive",
    # Spatial
    "spatial_residual_map_static", "spatial_residual_map_interactive",
    "moran_scatter_static", "moran_scatter_interactive",
    "panel_residual_heatmap_static", "panel_residual_heatmap_interactive",
    # Multicollinearity
    "vif_bar_static", "vif_bar_interactive",
    "condition_index_plot_static", "condition_index_plot_interactive",
    "correlation_heatmap_with_clustering_static", "correlation_heatmap_with_clustering_interactive",
    "eigenvalue_scree_predictors_static", "eigenvalue_scree_predictors_interactive",
    "tolerance_bar_static", "tolerance_bar_interactive",
    # Effects
    "partial_dependence_regression_static", "partial_dependence_regression_interactive",
    "ice_plot_regression_static", "ice_plot_regression_interactive",
    "marginal_effects_plot_static", "marginal_effects_plot_interactive",
    "interaction_effect_plot_static", "interaction_effect_plot_interactive",
    "conditional_expectation_curve_static", "conditional_expectation_curve_interactive",
    "elasticity_plot_static", "elasticity_plot_interactive",
    # GOF
    "normality_test_panel_static", "normality_test_panel_interactive",
    "breusch_pagan_plot_static", "breusch_pagan_plot_interactive",
    "white_test_plot_static", "white_test_plot_interactive",
    "durbin_watson_gauge_static", "durbin_watson_gauge_interactive",
    "ljung_box_plot_static", "ljung_box_plot_interactive",
    "residual_dependence_test_panel_static", "residual_dependence_test_panel_interactive",
    # Selection
    "aic_bic_bar_static", "aic_bic_bar_interactive",
    "nested_model_comparison_plot_static", "nested_model_comparison_plot_interactive",
    "stepwise_selection_path_static", "stepwise_selection_path_interactive",
    "forward_selection_score_curve_static", "forward_selection_score_curve_interactive",
    "best_subset_metric_bar_static", "best_subset_metric_bar_interactive",
    # CV extended
    "learning_curve_with_band_static", "learning_curve_with_band_interactive",
    "nested_cv_score_plot_static", "nested_cv_score_plot_interactive",
    "cv_residual_distribution_static", "cv_residual_distribution_interactive",
    "repeated_kfold_violin_static", "repeated_kfold_violin_interactive",
    "group_cv_score_strip_static", "group_cv_score_strip_interactive",
    # Uncertainty
    "conformal_interval_plot_static", "conformal_interval_plot_interactive",
    "jackknife_plus_band_static", "jackknife_plus_band_interactive",
    "quantile_calibration_plot_static", "quantile_calibration_plot_interactive",
    "sharpness_vs_coverage_plot_static", "sharpness_vs_coverage_plot_interactive",
    "coverage_by_segment_bar_static", "coverage_by_segment_bar_interactive",
    # Errors / loss
    "loss_distribution_violin_static", "loss_distribution_violin_interactive",
    "ranked_error_plot_static", "ranked_error_plot_interactive",
    "worst_k_predictions_chart_static", "worst_k_predictions_chart_interactive",
    "error_decomposition_bar_static", "error_decomposition_bar_interactive",
    # Mixed effects
    "random_effect_caterpillar_static", "random_effect_caterpillar_interactive",
    "random_intercept_slope_scatter_static", "random_intercept_slope_scatter_interactive",
    "group_means_vs_predicted_static", "group_means_vs_predicted_interactive",
    # Transforms
    "boxcox_likelihood_curve_static", "boxcox_likelihood_curve_interactive",
    "yeojohnson_lambda_search_static", "yeojohnson_lambda_search_interactive",
    "log_log_diagnostic_static", "log_log_diagnostic_interactive",
    "power_transform_residual_panel_static", "power_transform_residual_panel_interactive",
    # Var engineering
    "target_vs_feature_smooth_grid_static", "target_vs_feature_smooth_grid_interactive",
    "feature_target_correlation_bar_static", "feature_target_correlation_bar_interactive",
    "target_encoding_curve_static", "target_encoding_curve_interactive",
    # Bayesian
    "posterior_coefficient_density_static", "posterior_coefficient_density_interactive",
    "posterior_predictive_check_static", "posterior_predictive_check_interactive",
    "trace_plot_coefficients_static", "trace_plot_coefficients_interactive",
    "credible_interval_forest_static", "credible_interval_forest_interactive",
    # Comparison
    "multi_model_pred_vs_actual_overlay_static", "multi_model_pred_vs_actual_overlay_interactive",
    "residual_density_overlay_multi_static", "residual_density_overlay_multi_interactive",
    "error_ecdf_overlay_static", "error_ecdf_overlay_interactive",
    "model_winner_heatmap_static", "model_winner_heatmap_interactive",
    # Domain
    "price_elasticity_curve_static", "price_elasticity_curve_interactive",
    "dose_response_curve_static", "dose_response_curve_interactive",
    "demand_forecast_fan_chart_static", "demand_forecast_fan_chart_interactive",
    "yield_curve_fit_plot_static", "yield_curve_fit_plot_interactive",
    # Batch-2 aliases
    "link_function_plot", "deviance_residual_plot", "pearson_residual_plot",
    "working_residual_plot", "variance_function_plot", "glm_diagnostic_panel",
    "quantile_regression_band", "quantile_loss_curve", "huber_vs_ols_overlay",
    "weighted_residual_plot", "km_predicted_vs_observed", "cox_residual_plot",
    "proportional_hazards_test_plot", "forecast_vs_actual",
    "forecast_error_over_horizon", "rolling_forecast_origin",
    "backtest_error_distribution", "expanding_window_metric_curve",
    "forecast_band_plot", "spatial_residual_map", "moran_scatter",
    "panel_residual_heatmap", "vif_bar", "condition_index_plot",
    "correlation_heatmap_with_clustering", "eigenvalue_scree_predictors",
    "tolerance_bar", "partial_dependence_regression", "ice_plot_regression",
    "marginal_effects_plot", "interaction_effect_plot",
    "conditional_expectation_curve", "elasticity_plot", "normality_test_panel",
    "breusch_pagan_plot", "white_test_plot", "durbin_watson_gauge",
    "ljung_box_plot", "residual_dependence_test_panel", "aic_bic_bar",
    "nested_model_comparison_plot", "stepwise_selection_path",
    "forward_selection_score_curve", "best_subset_metric_bar",
    "learning_curve_with_band", "nested_cv_score_plot",
    "cv_residual_distribution", "repeated_kfold_violin", "group_cv_score_strip",
    "conformal_interval_plot", "jackknife_plus_band", "quantile_calibration_plot",
    "sharpness_vs_coverage_plot", "coverage_by_segment_bar",
    "loss_distribution_violin", "ranked_error_plot", "worst_k_predictions_chart",
    "error_decomposition_bar", "random_effect_caterpillar",
    "random_intercept_slope_scatter", "group_means_vs_predicted",
    "boxcox_likelihood_curve", "yeojohnson_lambda_search", "log_log_diagnostic",
    "power_transform_residual_panel", "target_vs_feature_smooth_grid",
    "feature_target_correlation_bar", "target_encoding_curve",
    "posterior_coefficient_density", "posterior_predictive_check",
    "trace_plot_coefficients", "credible_interval_forest",
    "multi_model_pred_vs_actual_overlay", "residual_density_overlay_multi",
    "error_ecdf_overlay", "model_winner_heatmap", "price_elasticity_curve",
    "dose_response_curve", "demand_forecast_fan_chart", "yield_curve_fit_plot",
]
