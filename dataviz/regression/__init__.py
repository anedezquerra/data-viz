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
]
