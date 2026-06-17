"""Univariate visualization charts, diagnostics, and statistical helpers."""

# Static (matplotlib) imports
from .advanced import (
    dot_plot_static,
    lollipop_chart_static,
    raincloud_plot_static,
    reference_band_histogram_static,
    ridgeline_plot_static,
    rug_plot_static,
    strip_plot_static,
)
from .accessors import UnivariateInput, infer_univariate_kind, numeric_or_none, resolve_univariate_data
from .box_plot import box_plot_static
from .categorical import category_counts, frequency_bar_static, pareto_chart_static
from .dashboard import univariate_analysis_dashboard_static
from .datetime import (
    as_datetime_series,
    event_counts,
    event_frequency_plot_static,
    interarrival_plot_static,
    interarrival_times,
)
from .density import density_static
from .diagnostics import (
    NormalityTestResult,
    normality_test,
    outlier_plot_static,
    percentile_plot_static,
    univariate_diagnostic_panel_static,
)
from .distribution import (
    cumulative_histogram_static,
    ecdf_plot_static,
    ecdf_values,
    pp_plot_static,
    qq_plot_static,
)
from .fitting import (
    DistributionFit,
    compare_distributions,
    fit_distribution,
    fitted_distribution_histogram_static,
    fitted_pdf_values,
)
from .histogram import histogram_static
from .inference import (
    BootstrapCI,
    bootstrap_ci,
    bootstrap_distribution,
    bootstrap_distribution_plot_static,
)
from .ordinal import (
    likert_summary,
    ordinal_bar_static,
    ordered_category_counts,
)
from .profile import UnivariateProfile, auto_profile, auto_profile_chart_interactive
from .quality import (
    DataQualitySummary,
    data_quality_summary,
    quality_bar_static,
    sentinel_rate,
    sentinel_value_counts,
)
from .robust import (
    RobustStats,
    mad_outliers,
    mad_zscores,
    robust_location_plot_static,
    robust_summary,
    trimmed_mean,
    winsorize_series,
)
from .stats import (
    UnivariateStats,
    as_numeric_series,
    iqr_outliers,
    percentile_table,
    recommended_bin_count,
    univariate_summary,
    zscore_outliers,
)
from .tail import (
    ConcentrationStats,
    concentration_summary,
    exceedance_table,
    lorenz_curve_static,
    lorenz_curve_values,
    survival_curve_static,
    survival_values,
)
from .text import (
    BooleanSummary,
    BooleanRateInterval,
    boolean_bar_static,
    boolean_summary,
    boolean_wilson_interval,
    string_length_summary,
    token_count_summary,
    top_terms,
    top_terms_bar_static,
)
from .treatment import (
    OutlierTreatmentResult,
    cap_outliers,
    flag_outliers,
    outlier_mask,
    outlier_treatment_comparison_static,
    remove_outliers,
)
from .transforms import (
    TransformResult,
    transform_series,
    transformation_comparison_static,
    transformation_summary,
)
from .violin_plot import violin_plot_static
from .weighted import (
    WeightedStats,
    resolve_weighted_series,
    weighted_ecdf_plot_static,
    weighted_ecdf_values,
    weighted_histogram_static,
    weighted_quantile,
    weighted_summary,
)

# Interactive (plotly) imports
from .advanced import (
    dot_plot_interactive,
    lollipop_chart_interactive,
    raincloud_plot_interactive,
    reference_band_histogram_interactive,
    ridgeline_plot_interactive,
    rug_plot_interactive,
    strip_plot_interactive,
)
from .box_plot import box_plot_interactive
from .categorical import frequency_bar_interactive, pareto_chart_interactive
from .dashboard import univariate_analysis_dashboard_interactive
from .datetime import event_frequency_plot_interactive, interarrival_plot_interactive
from .density import density_interactive
from .diagnostics import (
    outlier_plot_interactive,
    percentile_plot_interactive,
    univariate_diagnostic_panel_interactive,
)
from .distribution import (
    cumulative_histogram_interactive,
    ecdf_plot_interactive,
    pp_plot_interactive,
    qq_plot_interactive,
)
from .fitting import fitted_distribution_histogram_interactive
from .histogram import histogram_interactive
from .inference import bootstrap_distribution_plot_interactive
from .quality import quality_bar_interactive
from .robust import robust_location_plot_interactive
from .transforms import transformation_comparison_interactive
from .violin_plot import violin_plot_interactive
from .tail import lorenz_curve_interactive, survival_curve_interactive
from .text import boolean_bar_interactive, top_terms_bar_interactive
from .weighted import weighted_histogram_interactive
from .ordinal import ordinal_bar_interactive
from .treatment import outlier_treatment_comparison_interactive
from .weighted import weighted_ecdf_plot_interactive

# Convenience aliases
histogram = histogram_static
density_plot = density_static
box_plot = box_plot_static
violin_plot = violin_plot_static
frequency_bar = frequency_bar_static
univariate_pareto_chart = pareto_chart_static
ecdf_plot = ecdf_plot_static
cumulative_histogram = cumulative_histogram_static
qq_plot = qq_plot_static
pp_plot = pp_plot_static
outlier_plot = outlier_plot_static
percentile_plot = percentile_plot_static
univariate_diagnostic_panel = univariate_diagnostic_panel_static
fitted_distribution_histogram = fitted_distribution_histogram_static
robust_location_plot = robust_location_plot_static
rug_plot = rug_plot_static
strip_plot = strip_plot_static
dot_plot = dot_plot_static
lollipop_chart = lollipop_chart_static
reference_band_histogram = reference_band_histogram_static
raincloud_plot = raincloud_plot_static
ridgeline_plot = ridgeline_plot_static
transformation_comparison = transformation_comparison_static
event_frequency_plot = event_frequency_plot_static
interarrival_plot = interarrival_plot_static
univariate_analysis_dashboard = univariate_analysis_dashboard_static
weighted_histogram = weighted_histogram_static
quality_bar = quality_bar_static
survival_curve = survival_curve_static
lorenz_curve = lorenz_curve_static
bootstrap_distribution_plot = bootstrap_distribution_plot_static
boolean_bar = boolean_bar_static
top_terms_bar = top_terms_bar_static
weighted_ecdf_plot = weighted_ecdf_plot_static
ordinal_bar = ordinal_bar_static
outlier_treatment_comparison = outlier_treatment_comparison_static
auto_profile_chart = auto_profile_chart_interactive

__all__ = [
    # Static versions
    "histogram_static",
    "density_static",
    "box_plot_static",
    "violin_plot_static",
    "frequency_bar_static",
    "pareto_chart_static",
    "ecdf_plot_static",
    "cumulative_histogram_static",
    "qq_plot_static",
    "pp_plot_static",
    "outlier_plot_static",
    "percentile_plot_static",
    "univariate_diagnostic_panel_static",
    "fitted_distribution_histogram_static",
    "robust_location_plot_static",
    "rug_plot_static",
    "strip_plot_static",
    "dot_plot_static",
    "lollipop_chart_static",
    "reference_band_histogram_static",
    "raincloud_plot_static",
    "ridgeline_plot_static",
    "transformation_comparison_static",
    "event_frequency_plot_static",
    "interarrival_plot_static",
    "univariate_analysis_dashboard_static",
    "weighted_histogram_static",
    "quality_bar_static",
    "survival_curve_static",
    "lorenz_curve_static",
    "bootstrap_distribution_plot_static",
    "boolean_bar_static",
    "top_terms_bar_static",
    "weighted_ecdf_plot_static",
    "ordinal_bar_static",
    "outlier_treatment_comparison_static",
    # Interactive versions
    "histogram_interactive",
    "density_interactive",
    "box_plot_interactive",
    "violin_plot_interactive",
    "frequency_bar_interactive",
    "pareto_chart_interactive",
    "ecdf_plot_interactive",
    "cumulative_histogram_interactive",
    "qq_plot_interactive",
    "pp_plot_interactive",
    "outlier_plot_interactive",
    "percentile_plot_interactive",
    "univariate_diagnostic_panel_interactive",
    "fitted_distribution_histogram_interactive",
    "robust_location_plot_interactive",
    "rug_plot_interactive",
    "strip_plot_interactive",
    "dot_plot_interactive",
    "lollipop_chart_interactive",
    "reference_band_histogram_interactive",
    "raincloud_plot_interactive",
    "ridgeline_plot_interactive",
    "transformation_comparison_interactive",
    "event_frequency_plot_interactive",
    "interarrival_plot_interactive",
    "univariate_analysis_dashboard_interactive",
    "weighted_histogram_interactive",
    "quality_bar_interactive",
    "survival_curve_interactive",
    "lorenz_curve_interactive",
    "bootstrap_distribution_plot_interactive",
    "boolean_bar_interactive",
    "top_terms_bar_interactive",
    "weighted_ecdf_plot_interactive",
    "ordinal_bar_interactive",
    "outlier_treatment_comparison_interactive",
    "auto_profile_chart_interactive",
    # Statistical helpers
    "UnivariateInput",
    "UnivariateStats",
    "RobustStats",
    "DistributionFit",
    "TransformResult",
    "NormalityTestResult",
    "WeightedStats",
    "DataQualitySummary",
    "ConcentrationStats",
    "BootstrapCI",
    "BooleanSummary",
    "BooleanRateInterval",
    "OutlierTreatmentResult",
    "UnivariateProfile",
    "as_numeric_series",
    "as_datetime_series",
    "resolve_weighted_series",
    "resolve_univariate_data",
    "infer_univariate_kind",
    "numeric_or_none",
    "category_counts",
    "ordered_category_counts",
    "ecdf_values",
    "survival_values",
    "lorenz_curve_values",
    "univariate_summary",
    "robust_summary",
    "weighted_summary",
    "data_quality_summary",
    "sentinel_value_counts",
    "sentinel_rate",
    "concentration_summary",
    "normality_test",
    "fit_distribution",
    "compare_distributions",
    "fitted_pdf_values",
    "transform_series",
    "transformation_summary",
    "event_counts",
    "interarrival_times",
    "exceedance_table",
    "bootstrap_distribution",
    "bootstrap_ci",
    "boolean_summary",
    "boolean_wilson_interval",
    "string_length_summary",
    "token_count_summary",
    "top_terms",
    "likert_summary",
    "auto_profile",
    "weighted_quantile",
    "weighted_ecdf_values",
    "outlier_mask",
    "cap_outliers",
    "remove_outliers",
    "flag_outliers",
    "iqr_outliers",
    "zscore_outliers",
    "mad_outliers",
    "mad_zscores",
    "trimmed_mean",
    "winsorize_series",
    "recommended_bin_count",
    "percentile_table",
    # Aliases (default to static)
    "histogram",
    "density_plot",
    "box_plot",
    "violin_plot",
    "frequency_bar",
    "univariate_pareto_chart",
    "ecdf_plot",
    "cumulative_histogram",
    "qq_plot",
    "pp_plot",
    "outlier_plot",
    "percentile_plot",
    "univariate_diagnostic_panel",
    "fitted_distribution_histogram",
    "robust_location_plot",
    "rug_plot",
    "strip_plot",
    "dot_plot",
    "lollipop_chart",
    "reference_band_histogram",
    "raincloud_plot",
    "ridgeline_plot",
    "transformation_comparison",
    "event_frequency_plot",
    "interarrival_plot",
    "univariate_analysis_dashboard",
    "weighted_histogram",
    "quality_bar",
    "survival_curve",
    "lorenz_curve",
    "bootstrap_distribution_plot",
    "boolean_bar",
    "top_terms_bar",
    "weighted_ecdf_plot",
    "ordinal_bar",
    "outlier_treatment_comparison",
    "auto_profile_chart",
]
