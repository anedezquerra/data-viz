"""Curated use cases for univariate member pages."""

USE_CASES = {
    # accessors
    "dataviz.univariate.accessors.UnivariateInput": "Immutable resolved input carrying the cleaned Series, display name, inferred kind, and missing count; consumed by wrappers that normalize univariate inputs.",
    "dataviz.univariate.accessors.resolve_univariate_data": "Use to resolve a column name or series-like into a validated UnivariateInput, applying missing-value policy and optional numeric coercion before plotting.",
    "dataviz.univariate.accessors.infer_univariate_kind": "Use to classify a column as numeric, categorical, datetime, boolean, or text so downstream code can pick the right chart.",
    "dataviz.univariate.accessors.numeric_or_none": "Use in permissive profiling code to attempt numeric coercion, returning None instead of raising when no usable numeric values remain.",
    # advanced
    "dataviz.univariate.advanced.rug_plot_static": "Use to show every individual observation as ticks along an axis, revealing clustering and gaps that bins can hide.",
    "dataviz.univariate.advanced.rug_plot_interactive": "Use to show every individual observation as ticks along an axis, revealing clustering and gaps that bins can hide.",
    "dataviz.univariate.advanced.strip_plot_static": "Use to display each observation as a jittered point, ideal for small samples where exact values and density matter.",
    "dataviz.univariate.advanced.strip_plot_interactive": "Use to display each observation as a jittered point, ideal for small samples where exact values and density matter.",
    "dataviz.univariate.advanced.dot_plot_static": "Use as a Cleveland dot plot to compare category counts with less ink than bars, emphasizing position over length.",
    "dataviz.univariate.advanced.dot_plot_interactive": "Use as a Cleveland dot plot to compare category counts with less ink than bars, emphasizing position over length.",
    "dataviz.univariate.advanced.lollipop_chart_static": "Use to compare category counts with stems and markers when bars feel too heavy for a slim ranking view.",
    "dataviz.univariate.advanced.lollipop_chart_interactive": "Use to compare category counts with stems and markers when bars feel too heavy for a slim ranking view.",
    "dataviz.univariate.advanced.reference_band_histogram_static": "Use when you need a histogram annotated with mean and standard-deviation bands to judge spread against typical reference ranges.",
    "dataviz.univariate.advanced.reference_band_histogram_interactive": "Use when you need a histogram annotated with mean and standard-deviation bands to judge spread against typical reference ranges.",
    "dataviz.univariate.advanced.raincloud_plot_static": "Use to combine density, box plot, and raw points in one raincloud view showing shape, quartiles, and observations together.",
    "dataviz.univariate.advanced.raincloud_plot_interactive": "Use to combine density, box plot, and raw points in one raincloud view showing shape, quartiles, and observations together.",
    "dataviz.univariate.advanced.ridgeline_plot_static": "Use to stack density curves for several numeric dataframe columns to compare distribution shapes across variables at a glance.",
    "dataviz.univariate.advanced.ridgeline_plot_interactive": "Use to stack density curves for several numeric dataframe columns to compare distribution shapes across variables at a glance.",
    # box_plot
    "dataviz.univariate.box_plot.box_plot_static": "Use to summarize quartiles, spread, and outliers of a numeric variable, with an optional notch for median comparison.",
    "dataviz.univariate.box_plot.box_plot_interactive": "Use to summarize quartiles, spread, and outliers of a numeric variable with hover detail; DataFrame input draws one box per column.",
    # categorical
    "dataviz.univariate.categorical.category_counts": "Use to compute sorted category counts or proportions, optionally limited to the top N, as input for categorical charts.",
    "dataviz.univariate.categorical.frequency_bar_static": "Use to show how often each category occurs, with normalize=True when proportions matter more than raw counts.",
    "dataviz.univariate.categorical.frequency_bar_interactive": "Use to show how often each category occurs with hover labels, with normalize=True when proportions matter more than raw counts.",
    "dataviz.univariate.categorical.pareto_chart_static": "Use to rank categories by frequency with a cumulative percentage line, highlighting the vital few that drive most cases.",
    "dataviz.univariate.categorical.pareto_chart_interactive": "Use to rank categories by frequency with a cumulative percentage line, highlighting the vital few that drive most cases.",
    # charts
    "dataviz.univariate.charts.histogram": "Use when profiling a numeric column for the first time to see shape, spread, and outliers at a glance.",
    "dataviz.univariate.charts.density_plot": "Use to view a smooth kernel density estimate of a numeric variable when bin edges of a histogram would distract.",
    "dataviz.univariate.charts.box_plot": "Use to summarize quartiles, spread, and outliers of a numeric variable in a compact box plot.",
    "dataviz.univariate.charts.violin_plot": "Use to see the full distribution shape of a numeric variable, including multimodality that a box plot hides.",
    # dashboard
    "dataviz.univariate.dashboard.univariate_analysis_dashboard_static": "Use to get a multi-panel overview of one variable combining several univariate views in a single figure.",
    "dataviz.univariate.dashboard.univariate_analysis_dashboard_interactive": "Use to get a multi-panel interactive overview of one variable combining several univariate views in a single figure.",
    # datetime
    "dataviz.univariate.datetime.as_datetime_series": "Use to convert series-like values into a clean datetime Series before event counting or interarrival analysis.",
    "dataviz.univariate.datetime.event_counts": "Use to aggregate datetime observations into counts per calendar frequency such as day, week, or month.",
    "dataviz.univariate.datetime.event_frequency_plot_static": "Use to chart how event counts evolve over time from raw datetime observations at a chosen frequency.",
    "dataviz.univariate.datetime.event_frequency_plot_interactive": "Use to chart how event counts evolve over time from raw datetime observations at a chosen frequency.",
    "dataviz.univariate.datetime.interarrival_times": "Use to compute elapsed time between consecutive events, e.g. gaps between orders or failures, in a chosen unit.",
    "dataviz.univariate.datetime.interarrival_plot_static": "Use to histogram the gaps between consecutive events to spot burstiness or regularity in timing.",
    "dataviz.univariate.datetime.interarrival_plot_interactive": "Use to histogram the gaps between consecutive events to spot burstiness or regularity in timing.",
    # density
    "dataviz.univariate.density.density_static": "Use to estimate the smooth probability density of a numeric variable without committing to histogram bins.",
    "dataviz.univariate.density.density_interactive": "Use to estimate the smooth probability density of a numeric variable with hover inspection of the curve.",
    # diagnostics
    "dataviz.univariate.diagnostics.NormalityTestResult": "Result of a normality test carrying the statistic, p-value, and verdict; consumed when deciding if a variable is plausibly normal.",
    "dataviz.univariate.diagnostics.normality_test": "Use to formally test whether a numeric variable departs from normality before applying methods that assume it.",
    "dataviz.univariate.diagnostics.outlier_plot_static": "Use an index plot that flags univariate outliers to locate which observations sit outside expected bounds.",
    "dataviz.univariate.diagnostics.outlier_plot_interactive": "Use an index plot that flags univariate outliers to locate which observations sit outside expected bounds.",
    "dataviz.univariate.diagnostics.percentile_plot_static": "Use to profile a variable across its percentiles, revealing tail behavior and skew beyond mean and standard deviation.",
    "dataviz.univariate.diagnostics.percentile_plot_interactive": "Use to profile a variable across its percentiles, revealing tail behavior and skew beyond mean and standard deviation.",
    "dataviz.univariate.diagnostics.univariate_diagnostic_panel_static": "Use to run a four-panel diagnostic figure when you want a quick, broad health check of one variable in a single view.",
    "dataviz.univariate.diagnostics.univariate_diagnostic_panel_interactive": "Use to run a four-panel diagnostic figure when you want a quick, broad health check of one variable in a single view.",
    # distribution
    "dataviz.univariate.distribution.ecdf_values": "Use to compute sorted values and cumulative probabilities for an empirical CDF when you need the arrays, not the chart.",
    "dataviz.univariate.distribution.ecdf_plot_static": "Use to plot the empirical cumulative distribution, reading off medians and quantiles directly without binning.",
    "dataviz.univariate.distribution.ecdf_plot_interactive": "Use to plot the empirical cumulative distribution, reading off medians and quantiles directly without binning.",
    "dataviz.univariate.distribution.cumulative_histogram_static": "Use to show cumulative counts across bins when the running total of observations matters more than per-bin frequency.",
    "dataviz.univariate.distribution.cumulative_histogram_interactive": "Use to show cumulative counts across bins when the running total of observations matters more than per-bin frequency.",
    "dataviz.univariate.distribution.qq_plot_static": "Use to compare sample quantiles against a theoretical distribution to assess fit, especially in the tails.",
    "dataviz.univariate.distribution.qq_plot_interactive": "Use to compare sample quantiles against a theoretical distribution to assess fit, especially in the tails.",
    "dataviz.univariate.distribution.pp_plot_static": "Use to compare cumulative probabilities between data and a theoretical distribution to check fit near the center.",
    "dataviz.univariate.distribution.pp_plot_interactive": "Use to compare cumulative probabilities between data and a theoretical distribution to check fit near the center.",
    # fitting
    "dataviz.univariate.fitting.DistributionFit": "Fitted SciPy distribution summary carrying the distribution name, parameters, and fit quality; consumed by ranking and overlay helpers.",
    "dataviz.univariate.fitting.fit_distribution": "Use to fit a named SciPy continuous distribution to a numeric variable and recover its estimated parameters.",
    "dataviz.univariate.fitting.compare_distributions": "Use to fit and rank several candidate distributions to find which family best describes a numeric variable.",
    "dataviz.univariate.fitting.fitted_pdf_values": "Use to compute x and density values of a fitted distribution when you need the curve arrays rather than a chart.",
    "dataviz.univariate.fitting.fitted_distribution_histogram_static": "Use to overlay a fitted probability density on a histogram to visually judge how well the chosen distribution fits.",
    "dataviz.univariate.fitting.fitted_distribution_histogram_interactive": "Use to overlay a fitted probability density on a histogram to visually judge how well the chosen distribution fits.",
    # histogram
    "dataviz.univariate.histogram.histogram_static": "Use when profiling a numeric column for the first time to see shape, spread, and outliers at a glance.",
    "dataviz.univariate.histogram.histogram_interactive": "Use when profiling a numeric column for the first time with hoverable bin counts and zoomable ranges.",
}
