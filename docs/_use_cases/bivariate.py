"""Curated use cases for bivariate member pages."""

USE_CASES = {
    # advanced.py
    "dataviz.bivariate.advanced.bubble_plot_static": "Use when you need to show a third numeric dimension on a scatter plot by encoding it as point size.",
    "dataviz.bivariate.advanced.bubble_plot_interactive": "Use when you need to show a third numeric dimension on a scatter plot by encoding it as point size.",
    "dataviz.bivariate.advanced.hexbin_plot_static": "Use when a scatter plot of a large dataset overplots, to see point density as hexagonal bins.",
    "dataviz.bivariate.advanced.hexbin_plot_interactive": "Use when a scatter plot of a large dataset overplots, to see point density as hexagonal bins.",
    "dataviz.bivariate.advanced.regression_plot_static": "Use to overlay a polynomial trend line on a scatter plot when assessing whether a simple curve fits the relationship.",
    "dataviz.bivariate.advanced.regression_plot_interactive": "Use to overlay a polynomial trend line on a scatter plot when assessing whether a simple curve fits the relationship.",
    "dataviz.bivariate.advanced.density_contour_static": "Use to visualize the joint density of two variables as contour lines when individual points are too dense to read.",
    "dataviz.bivariate.advanced.density_contour_interactive": "Use to visualize the joint density of two variables as contour lines when individual points are too dense to read.",
    # categorical.py
    "dataviz.bivariate.categorical.grouped_bar_static": "Use to compare an aggregated numeric value, such as a mean or sum, across the levels of a categorical variable.",
    "dataviz.bivariate.categorical.grouped_bar_interactive": "Use to compare an aggregated numeric value, such as a mean or sum, across the levels of a categorical variable.",
    "dataviz.bivariate.categorical.box_by_category_static": "Use to compare the spread, median, and outliers of a numeric variable across categories.",
    "dataviz.bivariate.categorical.box_by_category_interactive": "Use to compare the spread, median, and outliers of a numeric variable across categories.",
    "dataviz.bivariate.categorical.violin_by_category_static": "Use when box plots hide bimodal or skewed shapes and you need the full distribution per category.",
    "dataviz.bivariate.categorical.violin_by_category_interactive": "Use when box plots hide bimodal or skewed shapes and you need the full distribution per category.",
    "dataviz.bivariate.categorical.crosstab_heatmap_static": "Use to spot associations between two categorical variables by mapping their contingency table to color intensity.",
    "dataviz.bivariate.categorical.crosstab_heatmap_interactive": "Use to spot associations between two categorical variables by mapping their contingency table to color intensity.",
    # charts.py
    "dataviz.bivariate.charts.scatter_plot": "Use as a first look at the relationship between two numeric variables before choosing a more specialized view.",
    "dataviz.bivariate.charts.line_plot": "Use to show how a numeric variable changes across an ordered axis such as time or sequence index.",
    "dataviz.bivariate.charts.correlation_heatmap": "Use to scan pairwise correlations among dataframe columns and quickly find strongly related variable pairs.",
    # correlation.py
    "dataviz.bivariate.correlation.correlation_heatmap_static": "Use to scan pairwise correlations among dataframe columns and quickly find strongly related variable pairs.",
    "dataviz.bivariate.correlation.correlation_heatmap_interactive": "Use to scan pairwise correlations among dataframe columns and quickly find strongly related variable pairs.",
    # joint.py
    "dataviz.bivariate.joint.joint_scatter_hist_static": "Use to see a two-variable relationship and each marginal distribution in one figure during exploratory analysis.",
    "dataviz.bivariate.joint.joint_scatter_hist_interactive": "Use to see a two-variable relationship and each marginal distribution in one figure during exploratory analysis.",
    "dataviz.bivariate.joint.bivariate_histogram_static": "Use to summarize the joint distribution of two variables as rectangular bins when points overplot.",
    "dataviz.bivariate.joint.bivariate_histogram_interactive": "Use to summarize the joint distribution of two variables as rectangular bins when points overplot.",
    # line.py
    "dataviz.bivariate.line.line_plot_static": "Use to show how a numeric variable changes across an ordered axis such as time or sequence index.",
    "dataviz.bivariate.line.line_plot_interactive": "Use to show how a numeric variable changes across an ordered axis such as time or sequence index.",
    # scatter.py
    "dataviz.bivariate.scatter.scatter_plot_static": "Use as a first look at the relationship between two numeric variables before choosing a more specialized view.",
    "dataviz.bivariate.scatter.scatter_plot_interactive": "Use as a first look at the relationship between two numeric variables before choosing a more specialized view.",
    # stats.py
    "dataviz.bivariate.stats.BivariateStats": "Returned by bivariate_summary; carries correlations, covariance, fit coefficients, and descriptive statistics for downstream reporting.",
    "dataviz.bivariate.stats.bivariate_summary": "Use when you need numeric evidence of association, such as Pearson or Spearman correlation, rather than a chart.",
    "dataviz.bivariate.stats.outlier_scatter_static": "Use to flag unusual points in a two-variable relationship using z-score or IQR rules before fitting models.",
    "dataviz.bivariate.stats.outlier_scatter_interactive": "Use to flag unusual points in a two-variable relationship using z-score or IQR rules before fitting models.",
    "dataviz.bivariate.stats.residual_relationship_static": "Use to check whether a polynomial fit leaves structure in the residuals, signaling a poor model choice.",
    "dataviz.bivariate.stats.residual_relationship_interactive": "Use to check whether a polynomial fit leaves structure in the residuals, signaling a poor model choice.",
    "dataviz.bivariate.stats.quantile_bin_plot_static": "Use to summarize how a y statistic, mean or median, varies across quantile bins of x for a robust trend view.",
    "dataviz.bivariate.stats.quantile_bin_plot_interactive": "Use to summarize how a y statistic, mean or median, varies across quantile bins of x for a robust trend view.",
    "dataviz.bivariate.stats.bland_altman_static": "Use when comparing two measurement methods to assess their agreement and bias rather than their correlation.",
    "dataviz.bivariate.stats.bland_altman_interactive": "Use when comparing two measurement methods to assess their agreement and bias rather than their correlation.",
    "dataviz.bivariate.stats.rank_scatter_static": "Use to compare the rank ordering of two variables when monotonic association matters more than raw values.",
    "dataviz.bivariate.stats.rank_scatter_interactive": "Use to compare the rank ordering of two variables when monotonic association matters more than raw values.",
    "dataviz.bivariate.stats.lag_plot_static": "Use to check for delayed or leading-lag relationships between two ordered series, such as time-shifted signals.",
    "dataviz.bivariate.stats.lag_plot_interactive": "Use to check for delayed or leading-lag relationships between two ordered series, such as time-shifted signals.",
    "dataviz.bivariate.stats.conditional_box_static": "Use to see how the full distribution of y changes as a numeric conditioning variable x increases across bins.",
    "dataviz.bivariate.stats.conditional_box_interactive": "Use to see how the full distribution of y changes as a numeric conditioning variable x increases across bins.",
    # trends.py
    "dataviz.bivariate.trends.binned_mean_plot_static": "Use to smooth noisy scatter data into mean y values per x bin and reveal the underlying trend.",
    "dataviz.bivariate.trends.binned_mean_plot_interactive": "Use to smooth noisy scatter data into mean y values per x bin and reveal the underlying trend.",
    "dataviz.bivariate.trends.errorbar_plot_static": "Use to compare group means with uncertainty intervals along an ordered or categorical x axis.",
    "dataviz.bivariate.trends.errorbar_plot_interactive": "Use to compare group means with uncertainty intervals along an ordered or categorical x axis.",
    "dataviz.bivariate.trends.area_between_static": "Use to highlight the gap between two y-series over a shared x axis, such as forecast bounds or tolerance bands.",
    "dataviz.bivariate.trends.area_between_interactive": "Use to highlight the gap between two y-series over a shared x axis, such as forecast bounds or tolerance bands.",
    "dataviz.bivariate.trends.step_plot_static": "Use for values that change discretely at known points, such as cumulative counts or rate changes over time.",
    "dataviz.bivariate.trends.step_plot_interactive": "Use for values that change discretely at known points, such as cumulative counts or rate changes over time.",
}
