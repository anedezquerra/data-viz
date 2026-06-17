window.DATAVIZ_MODULES = {
  univariate: {
    slug: "univariate",
    title: "Univariate",
    href: "module-univariate.html",
    status: "complete",
    summary: "One-variable analysis for numeric, categorical, ordinal, weighted, datetime, text, boolean, quality, tail, bootstrap, transformation, and profiling workflows.",
    staticCount: 43,
    interactiveCount: 42,
    helperCount: 89,
    capabilities: [
      { title: "Distribution views", text: "Histograms, density plots, ECDFs, cumulative histograms, QQ/PP plots, survival curves, reference bands, rainclouds, rugs, strips, and ridgelines." },
      { title: "Statistical summaries", text: "Classical, robust, weighted, bootstrap, tail, concentration, quality, text, boolean, and datetime summaries." },
      { title: "Automatic profiling", text: "Shared accessors and type inference select numeric, categorical, datetime, boolean, or text summaries and charts." },
      { title: "Data preparation", text: "Outlier masks, caps, removals, flags, sentinel checks, missingness profiles, transformations, and weighted quantiles." }
    ],
    groups: [
      { name: "Core charts", items: ["histogram", "density_plot", "box_plot", "violin_plot"], use: "Start with common distribution, spread, and shape views." },
      { name: "Advanced charts", items: ["ecdf_plot", "qq_plot", "pp_plot", "raincloud_plot", "ridgeline_plot", "rug_plot", "strip_plot"], use: "Inspect distribution shape, tails, individual points, and normality." },
      { name: "Categorical and ordinal", items: ["frequency_bar", "univariate_pareto_chart", "ordinal_bar", "likert_summary"], use: "Summarize ordered responses, Likert scales, and category frequencies." },
      { name: "Weighted and quality", items: ["weighted_summary", "weighted_histogram", "weighted_ecdf_plot", "data_quality_summary", "quality_bar"], use: "Analyze unequal sample weights and common data quality defects." },
      { name: "Inference and treatment", items: ["bootstrap_ci", "bootstrap_distribution_plot", "cap_outliers", "remove_outliers", "outlier_treatment_comparison"], use: "Quantify uncertainty and review outlier handling decisions." }
    ],
    example: "import dataviz as dv\n\nprofile = dv.auto_profile(\"sales\", data=df)\nfig = dv.auto_profile_chart_interactive(\"sales\", data=df)\n\nsummary = dv.weighted_summary(df[\"sales\"], df[\"sample_weight\"])\nci = dv.bootstrap_ci(df[\"sales\"], statistic=\"mean\", seed=42)\nax = dv.outlier_treatment_comparison(df[\"sales\"], treatment=\"cap\")",
    notes: "The univariate module is the most complete single-variable analysis surface in the package. Static functions default to matplotlib/seaborn outputs, interactive functions return Plotly figures, and helper functions return dataclasses, pandas Series, or pandas DataFrames for downstream workflows.",
    functions: [
      "histogram_static","density_static","box_plot_static","violin_plot_static","frequency_bar_static","pareto_chart_static","ecdf_plot_static","cumulative_histogram_static","qq_plot_static","pp_plot_static","outlier_plot_static","percentile_plot_static","univariate_diagnostic_panel_static","fitted_distribution_histogram_static","robust_location_plot_static","rug_plot_static","strip_plot_static","dot_plot_static","lollipop_chart_static","reference_band_histogram_static","raincloud_plot_static","ridgeline_plot_static","transformation_comparison_static","event_frequency_plot_static","interarrival_plot_static","univariate_analysis_dashboard_static","weighted_histogram_static","quality_bar_static","survival_curve_static","lorenz_curve_static","bootstrap_distribution_plot_static","boolean_bar_static","top_terms_bar_static","weighted_ecdf_plot_static","ordinal_bar_static","outlier_treatment_comparison_static",
      "histogram_interactive","density_interactive","box_plot_interactive","violin_plot_interactive","frequency_bar_interactive","pareto_chart_interactive","ecdf_plot_interactive","cumulative_histogram_interactive","qq_plot_interactive","pp_plot_interactive","outlier_plot_interactive","percentile_plot_interactive","univariate_diagnostic_panel_interactive","fitted_distribution_histogram_interactive","robust_location_plot_interactive","rug_plot_interactive","strip_plot_interactive","dot_plot_interactive","lollipop_chart_interactive","reference_band_histogram_interactive","raincloud_plot_interactive","ridgeline_plot_interactive","transformation_comparison_interactive","event_frequency_plot_interactive","interarrival_plot_interactive","univariate_analysis_dashboard_interactive","weighted_histogram_interactive","quality_bar_interactive","survival_curve_interactive","lorenz_curve_interactive","bootstrap_distribution_plot_interactive","boolean_bar_interactive","top_terms_bar_interactive","weighted_ecdf_plot_interactive","ordinal_bar_interactive","outlier_treatment_comparison_interactive","auto_profile_chart_interactive",
      "UnivariateInput","UnivariateStats","RobustStats","DistributionFit","TransformResult","NormalityTestResult","WeightedStats","DataQualitySummary","ConcentrationStats","BootstrapCI","BooleanSummary","BooleanRateInterval","OutlierTreatmentResult","UnivariateProfile","resolve_univariate_data","infer_univariate_kind","numeric_or_none","category_counts","ordered_category_counts","ecdf_values","survival_values","lorenz_curve_values","univariate_summary","robust_summary","weighted_summary","data_quality_summary","sentinel_value_counts","sentinel_rate","concentration_summary","normality_test","fit_distribution","compare_distributions","fitted_pdf_values","transform_series","transformation_summary","event_counts","interarrival_times","exceedance_table","bootstrap_distribution","bootstrap_ci","boolean_summary","boolean_wilson_interval","string_length_summary","token_count_summary","top_terms","likert_summary","auto_profile","weighted_quantile","weighted_ecdf_values","outlier_mask","cap_outliers","remove_outliers","flag_outliers","recommended_bin_count","percentile_table"
    ]
  },
  bivariate: {
    slug: "bivariate",
    title: "Bivariate",
    href: "module-bivariate.html",
    status: "complete",
    summary: "Two-variable visual analysis for relationships, grouped categories, trends, joint distributions, residual patterns, agreement, ranks, lags, and bivariate summary statistics.",
    staticCount: 24,
    interactiveCount: 24,
    helperCount: 26,
    capabilities: [
      { title: "Relationship charts", text: "Scatter, line, regression, density contour, hexbin, bubble, rank, lag, and residual relationship charts." },
      { title: "Categorical comparisons", text: "Grouped bars, category box/violin plots, crosstab heatmaps, conditional boxes, and binned means." },
      { title: "Paired diagnostics", text: "Bland-Altman, outlier scatter, quantile bins, area-between, error bars, and step plots." },
      { title: "Summary helpers", text: "BivariateStats and bivariate_summary provide numeric context for chart interpretation." }
    ],
    groups: [
      { name: "Relationship", items: ["scatter_plot", "line_plot", "regression_plot", "hexbin_plot", "density_contour"], use: "Show numeric-to-numeric association and trend structure." },
      { name: "Categorical", items: ["grouped_bar", "box_by_category", "violin_by_category", "crosstab_heatmap"], use: "Compare a measurement or count across category levels." },
      { name: "Diagnostics", items: ["outlier_scatter", "residual_relationship", "bland_altman", "lag_plot"], use: "Review assumptions, paired agreement, and temporal lag relationships." },
      { name: "Helpers", items: ["BivariateStats", "bivariate_summary"], use: "Return descriptive relationship metrics before plotting." }
    ],
    example: "import dataviz as dv\n\nstats = dv.bivariate_summary(df[\"height\"], df[\"weight\"])\nax = dv.regression_plot(df[\"height\"], df[\"weight\"])\nfig = dv.joint_scatter_hist_interactive(df[\"height\"], df[\"weight\"])",
    notes: "The bivariate module is designed for quickly moving from exploratory relationship plots to more diagnostic comparisons. Static aliases default to matplotlib; interactive functions mirror the same concepts in Plotly.",
    functions: ["scatter_plot_static","line_plot_static","correlation_heatmap_static","bubble_plot_static","hexbin_plot_static","regression_plot_static","density_contour_static","grouped_bar_static","box_by_category_static","violin_by_category_static","crosstab_heatmap_static","binned_mean_plot_static","errorbar_plot_static","area_between_static","step_plot_static","joint_scatter_hist_static","bivariate_histogram_static","outlier_scatter_static","residual_relationship_static","quantile_bin_plot_static","bland_altman_static","rank_scatter_static","lag_plot_static","conditional_box_static","scatter_plot_interactive","line_plot_interactive","correlation_heatmap_interactive","bubble_plot_interactive","hexbin_plot_interactive","regression_plot_interactive","density_contour_interactive","grouped_bar_interactive","box_by_category_interactive","violin_by_category_interactive","crosstab_heatmap_interactive","binned_mean_plot_interactive","errorbar_plot_interactive","area_between_interactive","step_plot_interactive","joint_scatter_hist_interactive","bivariate_histogram_interactive","outlier_scatter_interactive","residual_relationship_interactive","quantile_bin_plot_interactive","bland_altman_interactive","rank_scatter_interactive","lag_plot_interactive","conditional_box_interactive","BivariateStats","bivariate_summary","scatter_plot","line_plot","correlation_heatmap","bubble_plot","hexbin_plot","regression_plot","density_contour","grouped_bar","box_by_category","violin_by_category","crosstab_heatmap","binned_mean_plot","errorbar_plot","area_between","step_plot","joint_scatter_hist","bivariate_histogram","outlier_scatter","residual_relationship","quantile_bin_plot","bland_altman","rank_scatter","lag_plot","conditional_box"]
  },
  spc: {
    slug: "spc",
    title: "SPC",
    href: "module-spc.html",
    status: "complete",
    summary: "Statistical Process Control charts and process diagnostics for individuals data, subgroups, attributes, capability, rules, dashboards, and multivariate T² monitoring.",
    staticCount: 19,
    interactiveCount: 19,
    helperCount: 31,
    capabilities: [
      { title: "Variable charts", text: "Individuals, moving range, Xbar-R, Xbar-S, EWMA, and CUSUM views for continuous process monitoring." },
      { title: "Attribute charts", text: "p, np, c, and u charts for defect, defective, and rate monitoring." },
      { title: "Capability and diagnostics", text: "Capability histograms, run charts, rule violations, Pareto charts, process distributions, and zone charts." },
      { title: "Rules and constants", text: "Reusable control-limit calculations, SPC constants, rule-detection helpers, and Hotelling T² summaries." }
    ],
    groups: [
      { name: "Variable charts", items: ["control_chart", "moving_range_chart", "xbar_r_chart", "xbar_s_chart", "ewma_chart", "cusum_chart"], use: "Monitor continuous measurements and process shifts." },
      { name: "Attribute charts", items: ["p_chart", "np_chart", "c_chart", "u_chart"], use: "Monitor proportions, counts, and defect rates." },
      { name: "Capability", items: ["capability_summary", "capability_histogram"], use: "Evaluate process capability against specification limits." },
      { name: "Rules", items: ["detect_rule_violations", "individuals_limits", "moving_ranges", "get_spc_constants"], use: "Compute reusable SPC limits and rule annotations." }
    ],
    example: "import dataviz as dv\n\nlimits = dv.individuals_limits(values)\nviolations = dv.detect_rule_violations(values, limits)\nfig = dv.spc_dashboard_interactive(values)\ncapability = dv.capability_summary(values, lower_spec=9.5, upper_spec=10.5)",
    notes: "SPC functions are organized so calculations can be tested independently from charts. Most chart families have static and interactive variants plus aliases that default to static matplotlib output.",
    functions: ["control_chart_static","x_range_chart_static","moving_range_chart_static","xbar_r_chart_static","xbar_s_chart_static","ewma_chart_static","cusum_chart_static","p_chart_static","np_chart_static","c_chart_static","u_chart_static","capability_histogram_static","run_chart_static","rule_violation_chart_static","pareto_chart_static","process_distribution_static","zone_chart_static","hotelling_t2_chart_static","spc_dashboard_static","control_chart_interactive","x_range_chart_interactive","moving_range_chart_interactive","xbar_r_chart_interactive","xbar_s_chart_interactive","ewma_chart_interactive","cusum_chart_interactive","p_chart_interactive","np_chart_interactive","c_chart_interactive","u_chart_interactive","capability_histogram_interactive","run_chart_interactive","rule_violation_chart_interactive","pareto_chart_interactive","process_distribution_interactive","zone_chart_interactive","hotelling_t2_chart_interactive","spc_dashboard_interactive","ControlLimits","RuleViolation","SPCConstants","SPC_CONSTANTS","CapabilityStats","HotellingT2Result","capability_summary","hotelling_t2_summary","detect_rule_violations","individuals_limits","moving_ranges","get_spc_constants","control_chart","x_range_chart","moving_range_chart","xbar_r_chart","xbar_s_chart","ewma_chart","cusum_chart","p_chart","np_chart","c_chart","u_chart","capability_histogram","run_chart","rule_violation_chart","pareto_chart","process_distribution","zone_chart","hotelling_t2_chart","spc_dashboard"]
  },
  multivariate: {
    slug: "multivariate",
    title: "Multivariate",
    href: "module-multivariate.html",
    status: "complete",
    summary: "Multiple-variable visualization primitives for pairwise relationships, correlation heatmaps, and parallel coordinate profiles.",
    staticCount: 3,
    interactiveCount: 3,
    helperCount: 3,
    capabilities: [
      { title: "Matrix overview", text: "Pair plots and heatmaps reveal broad relationship structure across several numeric variables." },
      { title: "Profile comparison", text: "Parallel coordinate charts show row-wise multivariate profiles and contrast." },
      { title: "Static and interactive modes", text: "Each primary chart has a matplotlib/seaborn-style static function and a Plotly interactive companion." }
    ],
    groups: [
      { name: "Pairwise", items: ["pairplot", "pairplot_interactive"], use: "Compare all pairwise numeric relationships." },
      { name: "Correlation", items: ["heatmap", "heatmap_interactive"], use: "Summarize matrix-like associations." },
      { name: "Profiles", items: ["parallel_coordinates", "parallel_coordinates_interactive"], use: "Track multivariate row patterns." }
    ],
    example: "import dataviz as dv\n\nax = dv.multivariate.heatmap(df.corr())\nfig = dv.multivariate.parallel_coordinates_interactive(df)",
    notes: "This module provides the current multivariate visualization foundation and can later grow into PCA, clustering overlays, and dimensionality reduction dashboards.",
    functions: ["pairplot_static","heatmap_static","parallel_coordinates_static","pairplot_interactive","heatmap_interactive","parallel_coordinates_interactive","pairplot","heatmap","parallel_coordinates"]
  },
  eda: {
    slug: "eda",
    title: "EDA",
    href: "module-eda.html",
    status: "complete",
    summary: "Exploratory data analysis utilities for missingness, distribution summaries, and class balance inspection.",
    staticCount: 3,
    interactiveCount: 3,
    helperCount: 3,
    capabilities: [
      { title: "Missing data", text: "Visualize missingness patterns and missing-value scale quickly." },
      { title: "Distribution summaries", text: "Summarize distributions across dataframe columns during first-pass exploration." },
      { title: "Class balance", text: "Inspect target or label distributions before modeling." }
    ],
    groups: [
      { name: "Missingness", items: ["missing_data_plot", "missing_data_plot_interactive"], use: "Review completeness and missing-value patterns." },
      { name: "Distributions", items: ["distribution_summary", "distribution_summary_interactive"], use: "Compare variable distributions." },
      { name: "Classes", items: ["class_distribution", "class_distribution_interactive"], use: "Check target balance." }
    ],
    example: "import dataviz as dv\n\nax = dv.eda.missing_data_plot(df)\nfig = dv.eda.class_distribution_interactive(y)",
    notes: "EDA functions are intentionally compact and workflow-oriented. They complement the richer univariate and bivariate modules.",
    functions: ["missing_data_plot_static","distribution_summary_static","class_distribution_static","missing_data_plot_interactive","distribution_summary_interactive","class_distribution_interactive","missing_data_plot","distribution_summary","class_distribution"]
  },
  classification: {
    slug: "classification",
    title: "Classification",
    href: "module-classification.html",
    status: "complete",
    summary: "Classification model evaluation charts for confusion matrices, ROC curves, and precision-recall curves.",
    staticCount: 3,
    interactiveCount: 3,
    helperCount: 3,
    capabilities: [
      { title: "Confusion matrices", text: "Inspect class-level prediction outcomes and error structure." },
      { title: "ROC analysis", text: "Visualize true-positive and false-positive tradeoffs." },
      { title: "Precision-recall analysis", text: "Evaluate ranking quality under class imbalance." }
    ],
    groups: [
      { name: "Counts", items: ["confusion_matrix_plot", "confusion_matrix_plot_interactive"], use: "Show class prediction counts." },
      { name: "Ranking", items: ["roc_curve", "precision_recall_curve"], use: "Evaluate classifier score thresholds." }
    ],
    example: "import dataviz as dv\n\nax = dv.confusion_matrix_plot(cm, labels=[\"No\", \"Yes\"])\nfig = dv.precision_recall_curve_interactive(precision, recall, average_precision=0.82)",
    notes: "The module is focused on core supervised classification evaluation. It can later expand into calibration, lift, gain, and threshold-optimization pages.",
    functions: ["confusion_matrix_plot_static","roc_curve_static","precision_recall_curve_static","confusion_matrix_plot_interactive","roc_curve_interactive","precision_recall_curve_interactive","confusion_matrix_plot","roc_curve","precision_recall_curve"]
  },
  regression: {
    slug: "regression",
    title: "Regression",
    href: "module-regression.html",
    status: "complete",
    summary: "Regression diagnostic charts for residuals, prediction-vs-actual comparisons, and learning curves.",
    staticCount: 3,
    interactiveCount: 3,
    helperCount: 3,
    capabilities: [
      { title: "Residual diagnostics", text: "Spot heteroskedasticity, non-linearity, and systematic model error." },
      { title: "Prediction comparison", text: "Compare predicted and observed values." },
      { title: "Learning behavior", text: "Visualize training and validation curves across sample sizes." }
    ],
    groups: [
      { name: "Residuals", items: ["residual_plot", "residual_plot_interactive"], use: "Inspect model errors." },
      { name: "Predictions", items: ["prediction_plot", "prediction_plot_interactive"], use: "Compare y_true and y_pred." },
      { name: "Learning", items: ["learning_curve", "learning_curve_interactive"], use: "Review bias-variance behavior." }
    ],
    example: "import dataviz as dv\n\nax = dv.residual_plot(y_true, y_pred)\nfig = dv.learning_curve_interactive(train_sizes, train_scores, validation_scores)",
    notes: "Regression pages document model-diagnostic visuals and leave room for future influence, leverage, calibration, and interval diagnostics.",
    functions: ["residual_plot_static","prediction_plot_static","learning_curve_static","residual_plot_interactive","prediction_plot_interactive","learning_curve_interactive","residual_plot","prediction_plot","learning_curve"]
  },
  clustering: {
    slug: "clustering",
    title: "Clustering",
    href: "module-clustering.html",
    status: "complete",
    summary: "Clustering analysis visuals for cluster scatter views, dendrograms, and elbow diagnostics.",
    staticCount: 3,
    interactiveCount: 3,
    helperCount: 3,
    capabilities: [
      { title: "Cluster scatter", text: "Visualize cluster labels in two-dimensional embeddings or selected feature pairs." },
      { title: "Hierarchy", text: "Render dendrograms from linkage matrices." },
      { title: "Model selection", text: "Use elbow plots to inspect within-cluster variation across k values." }
    ],
    groups: [
      { name: "Clusters", items: ["scatter_clusters", "scatter_clusters_interactive"], use: "Show cluster assignments." },
      { name: "Hierarchy", items: ["dendrogram", "dendrogram_interactive"], use: "Display hierarchical clustering structure." },
      { name: "Selection", items: ["elbow_plot", "elbow_plot_interactive"], use: "Choose candidate k values." }
    ],
    example: "import dataviz as dv\n\nax = dv.clustering.scatter_clusters(X[:, 0], X[:, 1], labels)\nfig = dv.clustering.elbow_plot_interactive(k_values, inertias)",
    notes: "This module relies on SciPy for dendrogram rendering and provides both static and interactive chart families.",
    functions: ["scatter_clusters_static","dendrogram_static","elbow_plot_static","scatter_clusters_interactive","dendrogram_interactive","elbow_plot_interactive","scatter_clusters","dendrogram","elbow_plot"]
  },
  xai: {
    slug: "xai",
    title: "XAI",
    href: "module-xai.html",
    status: "complete",
    summary: "Explainable AI visualization helpers for feature importance, SHAP-style values, and partial dependence.",
    staticCount: 3,
    interactiveCount: 3,
    helperCount: 3,
    capabilities: [
      { title: "Feature importance", text: "Rank and compare model feature contributions." },
      { title: "SHAP views", text: "Visualize SHAP-like feature contribution arrays." },
      { title: "Partial dependence", text: "Inspect modeled response against feature values." }
    ],
    groups: [
      { name: "Importance", items: ["feature_importance", "feature_importance_interactive"], use: "Explain global feature rankings." },
      { name: "SHAP", items: ["shap_plot", "shap_plot_interactive"], use: "Inspect contribution-style explanations." },
      { name: "Dependence", items: ["partial_dependence", "partial_dependence_interactive"], use: "Show marginal response behavior." }
    ],
    example: "import dataviz as dv\n\nax = dv.xai.feature_importance(importances, feature_names=names)\nfig = dv.xai.partial_dependence_interactive(feature_values, pd_values)",
    notes: "The XAI module contains plotting helpers only; model-specific explanation computation stays outside the package.",
    functions: ["feature_importance_static","shap_plot_static","partial_dependence_static","feature_importance_interactive","shap_plot_interactive","partial_dependence_interactive","feature_importance","shap_plot","partial_dependence"]
  },
  utils: {
    slug: "utils",
    title: "Utils",
    href: "module-utils.html",
    status: "complete",
    summary: "Shared validation, plotting, reference-line, and dataframe-resolution helpers used across the package.",
    staticCount: 0,
    interactiveCount: 0,
    helperCount: 10,
    capabilities: [
      { title: "Plot setup", text: "Common matplotlib axes setup and theming helpers." },
      { title: "Validation", text: "Reusable alpha, positive integer, equal-length, and numeric dataframe validators." },
      { title: "Data resolution", text: "Resolve series, paired xy inputs, and numeric dataframe subsets consistently." }
    ],
    groups: [
      { name: "Plot helpers", items: ["setup_plot", "apply_theme"], use: "Create and style shared matplotlib plots." },
      { name: "Reference lines", items: ["add_reference_lines", "add_plotly_reference_lines"], use: "Add visual guides to charts." },
      { name: "Validation", items: ["validate_alpha", "validate_equal_length", "validate_positive_int"], use: "Keep chart functions consistent." }
    ],
    example: "from dataviz.utils import resolve_xy_data, validate_positive_int\n\nx, y = resolve_xy_data(\"height\", \"weight\", data=df, require_numeric=True)\nvalidate_positive_int(30, \"bins\")",
    notes: "Utility functions are public because they help users build custom extensions that behave like first-party chart functions.",
    functions: ["setup_plot","apply_theme","add_plotly_reference_lines","add_reference_lines","numeric_dataframe","resolve_series","resolve_xy_data","validate_alpha","validate_equal_length","validate_positive_int"]
  },
  "time-series": { slug: "time-series", title: "Time Series", href: "module-time-series.html", status: "planned", summary: "Reserved for future trend, seasonality, forecasting, anomaly, and calendar-aware visualization functions." },
  geospatial: { slug: "geospatial", title: "Geospatial", href: "module-geospatial.html", status: "planned", summary: "Reserved for future maps, choropleths, point layers, regions, and spatial diagnostics." },
  network: { slug: "network", title: "Network", href: "module-network.html", status: "planned", summary: "Reserved for future graph, node-link, adjacency, centrality, and community visualization functions." },
  dashboards: { slug: "dashboards", title: "Dashboards", href: "module-dashboards.html", status: "planned", summary: "Reserved for future layout-level report dashboards and multi-module composition helpers." },
  themes: { slug: "themes", title: "Themes", href: "module-themes.html", status: "planned", summary: "Reserved for future global styles, palettes, templates, and publication presets." },
  datasets: { slug: "datasets", title: "Datasets", href: "module-datasets.html", status: "planned", summary: "Reserved for future sample datasets and example data loaders." },
  io: { slug: "io", title: "I/O", href: "module-io.html", status: "planned", summary: "Reserved for future export, report, gallery, and file-writing helpers." },
  forecasting: { slug: "forecasting", title: "Forecasting", href: "module-forecasting.html", status: "planned", summary: "Reserved for future forecast interval, backtest, horizon, and error visualization functions." }
};
