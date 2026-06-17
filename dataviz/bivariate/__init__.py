"""Bivariate visualization charts - static and interactive versions."""

# Static (matplotlib) imports
from .scatter import scatter_plot_static
from .line import line_plot_static
from .correlation import correlation_heatmap_static
from .advanced import (
    bubble_plot_static,
    hexbin_plot_static,
    regression_plot_static,
    density_contour_static,
)
from .categorical import (
    grouped_bar_static,
    box_by_category_static,
    violin_by_category_static,
    crosstab_heatmap_static,
)
from .trends import (
    binned_mean_plot_static,
    errorbar_plot_static,
    area_between_static,
    step_plot_static,
)
from .joint import (
    joint_scatter_hist_static,
    bivariate_histogram_static,
)
from .stats import (
    BivariateStats,
    bivariate_summary,
    outlier_scatter_static,
    residual_relationship_static,
    quantile_bin_plot_static,
    bland_altman_static,
    rank_scatter_static,
    lag_plot_static,
    conditional_box_static,
)

# Interactive (plotly) imports
from .scatter import scatter_plot_interactive
from .line import line_plot_interactive
from .correlation import correlation_heatmap_interactive
from .advanced import (
    bubble_plot_interactive,
    hexbin_plot_interactive,
    regression_plot_interactive,
    density_contour_interactive,
)
from .categorical import (
    grouped_bar_interactive,
    box_by_category_interactive,
    violin_by_category_interactive,
    crosstab_heatmap_interactive,
)
from .trends import (
    binned_mean_plot_interactive,
    errorbar_plot_interactive,
    area_between_interactive,
    step_plot_interactive,
)
from .joint import (
    joint_scatter_hist_interactive,
    bivariate_histogram_interactive,
)
from .stats import (
    outlier_scatter_interactive,
    residual_relationship_interactive,
    quantile_bin_plot_interactive,
    bland_altman_interactive,
    rank_scatter_interactive,
    lag_plot_interactive,
    conditional_box_interactive,
)

# Convenience aliases
scatter_plot = scatter_plot_static
line_plot = line_plot_static
correlation_heatmap = correlation_heatmap_static
bubble_plot = bubble_plot_static
hexbin_plot = hexbin_plot_static
regression_plot = regression_plot_static
density_contour = density_contour_static
grouped_bar = grouped_bar_static
box_by_category = box_by_category_static
violin_by_category = violin_by_category_static
crosstab_heatmap = crosstab_heatmap_static
binned_mean_plot = binned_mean_plot_static
errorbar_plot = errorbar_plot_static
area_between = area_between_static
step_plot = step_plot_static
joint_scatter_hist = joint_scatter_hist_static
bivariate_histogram = bivariate_histogram_static
outlier_scatter = outlier_scatter_static
residual_relationship = residual_relationship_static
quantile_bin_plot = quantile_bin_plot_static
bland_altman = bland_altman_static
rank_scatter = rank_scatter_static
lag_plot = lag_plot_static
conditional_box = conditional_box_static

__all__ = [
    # Static versions
    "scatter_plot_static",
    "line_plot_static",
    "correlation_heatmap_static",
    "bubble_plot_static",
    "hexbin_plot_static",
    "regression_plot_static",
    "density_contour_static",
    "grouped_bar_static",
    "box_by_category_static",
    "violin_by_category_static",
    "crosstab_heatmap_static",
    "binned_mean_plot_static",
    "errorbar_plot_static",
    "area_between_static",
    "step_plot_static",
    "joint_scatter_hist_static",
    "bivariate_histogram_static",
    "outlier_scatter_static",
    "residual_relationship_static",
    "quantile_bin_plot_static",
    "bland_altman_static",
    "rank_scatter_static",
    "lag_plot_static",
    "conditional_box_static",
    # Interactive versions
    "scatter_plot_interactive",
    "line_plot_interactive",
    "correlation_heatmap_interactive",
    "bubble_plot_interactive",
    "hexbin_plot_interactive",
    "regression_plot_interactive",
    "density_contour_interactive",
    "grouped_bar_interactive",
    "box_by_category_interactive",
    "violin_by_category_interactive",
    "crosstab_heatmap_interactive",
    "binned_mean_plot_interactive",
    "errorbar_plot_interactive",
    "area_between_interactive",
    "step_plot_interactive",
    "joint_scatter_hist_interactive",
    "bivariate_histogram_interactive",
    "outlier_scatter_interactive",
    "residual_relationship_interactive",
    "quantile_bin_plot_interactive",
    "bland_altman_interactive",
    "rank_scatter_interactive",
    "lag_plot_interactive",
    "conditional_box_interactive",
    # Statistical helpers
    "BivariateStats",
    "bivariate_summary",
    # Aliases (default to static)
    "scatter_plot",
    "line_plot",
    "correlation_heatmap",
    "bubble_plot",
    "hexbin_plot",
    "regression_plot",
    "density_contour",
    "grouped_bar",
    "box_by_category",
    "violin_by_category",
    "crosstab_heatmap",
    "binned_mean_plot",
    "errorbar_plot",
    "area_between",
    "step_plot",
    "joint_scatter_hist",
    "bivariate_histogram",
    "outlier_scatter",
    "residual_relationship",
    "quantile_bin_plot",
    "bland_altman",
    "rank_scatter",
    "lag_plot",
    "conditional_box",
]
