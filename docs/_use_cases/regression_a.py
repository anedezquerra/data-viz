"""Curated use cases for regression member pages."""

USE_CASES = {
    # autocorrelation
    "dataviz.regression.autocorrelation.residual_acf_static": (
        "Use to check whether regression residuals are autocorrelated across lags, "
        "which invalidates standard OLS inference for time-ordered data."
    ),
    "dataviz.regression.autocorrelation.residual_acf_interactive": (
        "Use to check whether regression residuals are autocorrelated across lags, "
        "which invalidates standard OLS inference for time-ordered data."
    ),
    "dataviz.regression.autocorrelation.residual_pacf_static": (
        "Use to identify the direct lag order of residual dependence when choosing an "
        "AR term or diagnosing model misspecification."
    ),
    "dataviz.regression.autocorrelation.residual_pacf_interactive": (
        "Use to identify the direct lag order of residual dependence when choosing an "
        "AR term or diagnosing model misspecification."
    ),
    "dataviz.regression.autocorrelation.residual_runs_plot_static": (
        "Use to spot non-random runs of positive or negative residuals, a quick check "
        "for structure the model failed to capture."
    ),
    "dataviz.regression.autocorrelation.residual_runs_plot_interactive": (
        "Use to spot non-random runs of positive or negative residuals, a quick check "
        "for structure the model failed to capture."
    ),
    "dataviz.regression.autocorrelation.residual_time_plot_static": (
        "Use to plot residuals over time or observation order to reveal drift, trends, "
        "or regime changes hidden by aggregate metrics."
    ),
    "dataviz.regression.autocorrelation.residual_time_plot_interactive": (
        "Use to plot residuals over time or observation order to reveal drift, trends, "
        "or regime changes hidden by aggregate metrics."
    ),
    # bayesian
    "dataviz.regression.bayesian.posterior_coefficient_density_static": (
        "Use to inspect the full posterior distribution of each coefficient from MCMC "
        "samples instead of relying on a single point estimate."
    ),
    "dataviz.regression.bayesian.posterior_coefficient_density_interactive": (
        "Use to inspect the full posterior distribution of each coefficient from MCMC "
        "samples instead of relying on a single point estimate."
    ),
    "dataviz.regression.bayesian.posterior_predictive_check_static": (
        "Use to compare posterior-predictive draws against observed y and confirm the "
        "fitted Bayesian model can reproduce the data it was trained on."
    ),
    "dataviz.regression.bayesian.posterior_predictive_check_interactive": (
        "Use to compare posterior-predictive draws against observed y and confirm the "
        "fitted Bayesian model can reproduce the data it was trained on."
    ),
    "dataviz.regression.bayesian.trace_plot_coefficients_static": (
        "Use to diagnose MCMC sampling health, checking chains for good mixing and "
        "stationarity before trusting posterior summaries."
    ),
    "dataviz.regression.bayesian.trace_plot_coefficients_interactive": (
        "Use to diagnose MCMC sampling health, checking chains for good mixing and "
        "stationarity before trusting posterior summaries."
    ),
    "dataviz.regression.bayesian.credible_interval_forest_static": (
        "Use to compare credible intervals across coefficients at a glance, seeing "
        "which effects are credibly different from zero."
    ),
    "dataviz.regression.bayesian.credible_interval_forest_interactive": (
        "Use to compare credible intervals across coefficients at a glance, seeing "
        "which effects are credibly different from zero."
    ),
    # calibration_regression
    "dataviz.regression.calibration_regression.calibration_curve_regression_static": (
        "Use when predicted values should match observed means in each bin; systematic "
        "deviation from the diagonal signals a miscalibrated regressor."
    ),
    "dataviz.regression.calibration_regression.calibration_curve_regression_interactive": (
        "Use when predicted values should match observed means in each bin; systematic "
        "deviation from the diagonal signals a miscalibrated regressor."
    ),
    "dataviz.regression.calibration_regression.prediction_interval_coverage_plot_static": (
        "Use to verify that nominal prediction intervals (e.g. 90%) actually cover the "
        "observed target at the advertised rate."
    ),
    "dataviz.regression.calibration_regression.prediction_interval_coverage_plot_interactive": (
        "Use to verify that nominal prediction intervals (e.g. 90%) actually cover the "
        "observed target at the advertised rate."
    ),
    "dataviz.regression.calibration_regression.uncertainty_band_plot_static": (
        "Use to visualize predictive mean with a plus/minus z-sigma band, e.g. for "
        "Gaussian process regression, to see where the model is uncertain."
    ),
    "dataviz.regression.calibration_regression.uncertainty_band_plot_interactive": (
        "Use to visualize predictive mean with a plus/minus z-sigma band, e.g. for "
        "Gaussian process regression, to see where the model is uncertain."
    ),
    # charts
    "dataviz.regression.charts.residual_plot": (
        "Use as a first-pass diagnostic: residual patterns versus fitted values expose "
        "nonlinearity and heteroscedasticity before trusting inference."
    ),
    "dataviz.regression.charts.prediction_plot": (
        "Use to compare observed versus predicted values; points off the diagonal "
        "reveal bias and where the model under- or over-predicts."
    ),
    "dataviz.regression.charts.learning_curve": (
        "Use to see how model performance scales with training-set size and decide "
        "whether more data or a different model will help."
    ),
    # coefficients
    "dataviz.regression.coefficients.coefficient_plot_static": (
        "Use for a quick read of coefficient magnitude and sign, colored by direction, "
        "when communicating which drivers push predictions up or down."
    ),
    "dataviz.regression.coefficients.coefficient_plot_interactive": (
        "Use for a quick read of coefficient magnitude and sign, colored by direction, "
        "when communicating which drivers push predictions up or down."
    ),
    "dataviz.regression.coefficients.coefficient_forest_plot_static": (
        "Use to show OLS coefficients with 95% confidence intervals so viewers can see "
        "which effects are statistically distinguishable from zero."
    ),
    "dataviz.regression.coefficients.coefficient_forest_plot_interactive": (
        "Use to show OLS coefficients with 95% confidence intervals so viewers can see "
        "which effects are statistically distinguishable from zero."
    ),
    "dataviz.regression.coefficients.standardized_coefficient_plot_static": (
        "Use to compare relative feature importance on a common scale via beta times "
        "sigma_x over sigma_y, when raw units are not comparable."
    ),
    "dataviz.regression.coefficients.standardized_coefficient_plot_interactive": (
        "Use to compare relative feature importance on a common scale via beta times "
        "sigma_x over sigma_y, when raw units are not comparable."
    ),
    "dataviz.regression.coefficients.coefficient_path_plot_static": (
        "Use to trace coefficient paths across a regularization parameter and see "
        "which features shrink out first in ridge or lasso fits."
    ),
    "dataviz.regression.coefficients.coefficient_path_plot_interactive": (
        "Use to trace coefficient paths across a regularization parameter and see "
        "which features shrink out first in ridge or lasso fits."
    ),
    # comparison
    "dataviz.regression.comparison.multi_model_pred_vs_actual_overlay_static": (
        "Use to overlay predicted-vs-actual scatters from several models and spot "
        "which one tracks the diagonal most tightly."
    ),
    "dataviz.regression.comparison.multi_model_pred_vs_actual_overlay_interactive": (
        "Use to overlay predicted-vs-actual scatters from several models and spot "
        "which one tracks the diagonal most tightly."
    ),
    "dataviz.regression.comparison.residual_density_overlay_multi_static": (
        "Use to compare residual distributions across models; tighter, zero-centered "
        "KDEs indicate better calibrated errors."
    ),
    "dataviz.regression.comparison.residual_density_overlay_multi_interactive": (
        "Use to compare residual distributions across models; tighter, zero-centered "
        "KDEs indicate better calibrated errors."
    ),
    "dataviz.regression.comparison.error_ecdf_overlay_static": (
        "Compare empirical CDFs of absolute error per model; the curve farthest up and "
        "left dominates on typical error magnitude."
    ),
    "dataviz.regression.comparison.error_ecdf_overlay_interactive": (
        "Compare empirical CDFs of absolute error per model; the curve farthest up and "
        "left dominates on typical error magnitude."
    ),
    "dataviz.regression.comparison.model_winner_heatmap_static": (
        "Use to summarize which model wins on each metric in one matrix, avoiding "
        "cherry-picking a single score when selecting a champion."
    ),
    "dataviz.regression.comparison.model_winner_heatmap_interactive": (
        "Use to summarize which model wins on each metric in one matrix, avoiding "
        "cherry-picking a single score when selecting a champion."
    ),
    # cv_extended
    "dataviz.regression.cv_extended.learning_curve_with_band_static": (
        "Use to show mean CV score versus training size with a plus/minus std band, "
        "revealing both bias and variance as data grows."
    ),
    "dataviz.regression.cv_extended.learning_curve_with_band_interactive": (
        "Use to show mean CV score versus training size with a plus/minus std band, "
        "revealing both bias and variance as data grows."
    ),
    "dataviz.regression.cv_extended.nested_cv_score_plot_static": (
        "Use to display outer-fold scores from nested CV, giving an unbiased estimate "
        "of performance after hyperparameter tuning."
    ),
    "dataviz.regression.cv_extended.nested_cv_score_plot_interactive": (
        "Use to display outer-fold scores from nested CV, giving an unbiased estimate "
        "of performance after hyperparameter tuning."
    ),
    "dataviz.regression.cv_extended.cv_residual_distribution_static": (
        "Use to compare residual boxplots across CV folds and check that errors are "
        "stable rather than driven by one lucky or unlucky split."
    ),
    "dataviz.regression.cv_extended.cv_residual_distribution_interactive": (
        "Use to compare residual boxplots across CV folds and check that errors are "
        "stable rather than driven by one lucky or unlucky split."
    ),
    "dataviz.regression.cv_extended.repeated_kfold_violin_static": (
        "Use to show the full score distribution per repeat in repeated K-fold, "
        "quantifying how much results vary with the random split."
    ),
    "dataviz.regression.cv_extended.repeated_kfold_violin_interactive": (
        "Use to show the full score distribution per repeat in repeated K-fold, "
        "quantifying how much results vary with the random split."
    ),
    "dataviz.regression.cv_extended.group_cv_score_strip_static": (
        "Use to plot CV scores per group in grouped cross-validation, exposing groups "
        "where the model generalizes poorly."
    ),
    "dataviz.regression.cv_extended.group_cv_score_strip_interactive": (
        "Use to plot CV scores per group in grouped cross-validation, exposing groups "
        "where the model generalizes poorly."
    ),
    # diagnostics_panel
    "dataviz.regression.diagnostics_panel.regression_diagnostic_panel_static": (
        "Use as a one-shot check of classic OLS assumptions: residuals-vs-fitted, QQ, "
        "scale-location, and leverage in four panels."
    ),
    "dataviz.regression.diagnostics_panel.regression_diagnostic_panel_interactive": (
        "Use as a one-shot check of classic OLS assumptions: residuals-vs-fitted, QQ, "
        "scale-location, and leverage in four panels."
    ),
    "dataviz.regression.diagnostics_panel.regression_dashboard_static": (
        "Use for a compact model overview combining predicted-vs-actual, residual "
        "scatter, error histogram, and summary metrics."
    ),
    "dataviz.regression.diagnostics_panel.regression_dashboard_interactive": (
        "Use for a compact model overview combining predicted-vs-actual, residual "
        "scatter, error histogram, and summary metrics."
    ),
    # domain
    "dataviz.regression.domain.price_elasticity_curve_static": (
        "Use in pricing analysis to plot quantity versus price with an elasticity fit, "
        "showing how demand responds to price changes."
    ),
    "dataviz.regression.domain.price_elasticity_curve_interactive": (
        "Use in pricing analysis to plot quantity versus price with an elasticity fit, "
        "showing how demand responds to price changes."
    ),
    "dataviz.regression.domain.dose_response_curve_static": (
        "Use in pharmacology or toxicology to plot response versus dose with an "
        "optional CI band and log-scaled dose axis."
    ),
    "dataviz.regression.domain.dose_response_curve_interactive": (
        "Use in pharmacology or toxicology to plot response versus dose with an "
        "optional CI band and log-scaled dose axis."
    ),
    "dataviz.regression.domain.demand_forecast_fan_chart_static": (
        "Use to present demand forecasts with nested quantile bands, communicating "
        "growing uncertainty the further out the horizon extends."
    ),
    "dataviz.regression.domain.demand_forecast_fan_chart_interactive": (
        "Use to present demand forecasts with nested quantile bands, communicating "
        "growing uncertainty the further out the horizon extends."
    ),
    "dataviz.regression.domain.yield_curve_fit_plot_static": (
        "Use in fixed-income work to compare observed bond yields against a fitted "
        "curve across maturities and spot mispriced points."
    ),
    "dataviz.regression.domain.yield_curve_fit_plot_interactive": (
        "Use in fixed-income work to compare observed bond yields against a fitted "
        "curve across maturities and spot mispriced points."
    ),
    # effects
    "dataviz.regression.effects.partial_dependence_regression_static": (
        "Use to show the marginal effect of one feature on the predicted target, "
        "averaged over all other features."
    ),
    "dataviz.regression.effects.partial_dependence_regression_interactive": (
        "Use to show the marginal effect of one feature on the predicted target, "
        "averaged over all other features."
    ),
    "dataviz.regression.effects.ice_plot_regression_static": (
        "Use to reveal heterogeneous feature effects hidden by PDP: per-observation "
        "ICE lines with the average overlaid."
    ),
    "dataviz.regression.effects.ice_plot_regression_interactive": (
        "Use to reveal heterogeneous feature effects hidden by PDP: per-observation "
        "ICE lines with the average overlaid."
    ),
    "dataviz.regression.effects.marginal_effects_plot_static": (
        "Use to report average marginal effect per feature with optional confidence "
        "intervals, e.g. for econometric model interpretation."
    ),
    "dataviz.regression.effects.marginal_effects_plot_interactive": (
        "Use to report average marginal effect per feature with optional confidence "
        "intervals, e.g. for econometric model interpretation."
    ),
    "dataviz.regression.effects.interaction_effect_plot_static": (
        "Use to show how the effect of one feature changes across levels of a second "
        "feature, exposing interactions."
    ),
    "dataviz.regression.effects.interaction_effect_plot_interactive": (
        "Use to show how the effect of one feature changes across levels of a second "
        "feature, exposing interactions."
    ),
    "dataviz.regression.effects.conditional_expectation_curve_static": (
        "Use to plot E[Y|x] with an optional confidence band when summarizing the "
        "expected outcome as a smooth function of one predictor."
    ),
    "dataviz.regression.effects.conditional_expectation_curve_interactive": (
        "Use to plot E[Y|x] with an optional confidence band when summarizing the "
        "expected outcome as a smooth function of one predictor."
    ),
    "dataviz.regression.effects.elasticity_plot_static": (
        "Use to plot elasticity, the percent change in prediction per percent change "
        "in a feature, when scale-free sensitivity matters."
    ),
    "dataviz.regression.effects.elasticity_plot_interactive": (
        "Use to plot elasticity, the percent change in prediction per percent change "
        "in a feature, when scale-free sensitivity matters."
    ),
    # errors_loss
    "dataviz.regression.errors_loss.loss_distribution_violin_static": (
        "Use to compare full per-observation loss distributions across models, "
        "catching heavy tails that mean error hides."
    ),
    "dataviz.regression.errors_loss.loss_distribution_violin_interactive": (
        "Use to compare full per-observation loss distributions across models, "
        "catching heavy tails that mean error hides."
    ),
    "dataviz.regression.errors_loss.ranked_error_plot_static": (
        "Use to see how quickly errors grow from typical to worst case by plotting "
        "errors sorted by magnitude."
    ),
    "dataviz.regression.errors_loss.ranked_error_plot_interactive": (
        "Use to see how quickly errors grow from typical to worst case by plotting "
        "errors sorted by magnitude."
    ),
    "dataviz.regression.errors_loss.worst_k_predictions_chart_static": (
        "Use to surface the k predictions with the largest absolute error for targeted "
        "inspection and debugging."
    ),
    "dataviz.regression.errors_loss.worst_k_predictions_chart_interactive": (
        "Use to surface the k predictions with the largest absolute error for targeted "
        "inspection and debugging."
    ),
    "dataviz.regression.errors_loss.error_decomposition_bar_static": (
        "Use to break total error into components such as bias squared, variance, and "
        "noise when explaining where error comes from."
    ),
    "dataviz.regression.errors_loss.error_decomposition_bar_interactive": (
        "Use to break total error into components such as bias squared, variance, and "
        "noise when explaining where error comes from."
    ),
}
