"""
DataViz - A comprehensive data visualization package.

This package provides easy-to-use tools for creating beautiful visualizations
organized by chart type and analysis category. Each chart has both static
(matplotlib/seaborn) and interactive (plotly) versions.

Usage Examples
--------------

Static (default, matplotlib-based):
    >>> import dataviz as dv
    >>> dv.histogram(data)  # Uses histogram_static
    >>> dv.scatter_plot(x, y)  # Uses scatter_plot_static

Interactive (plotly-based):
    >>> dv.histogram_interactive(data)
    >>> dv.scatter_plot_interactive(x, y)

Or access via submodules:
    >>> dv.univariate.histogram_static(data)
    >>> dv.univariate.histogram_interactive(data)
"""

__version__ = "0.1.0"
__author__ = "PhD Aned Esquerra-Arguelles"
__email__ = "aned.ezquerra@gmail.com"

# Import submodules
from . import spc
from . import univariate
from . import bivariate
from . import multivariate
from . import eda
from . import xai
from . import regression
from . import classification
from . import clustering
from . import utils
from . import types

# Convenience imports - Static versions (default)
from .univariate import (
    histogram_static as histogram,
    density_static as density_plot,
    box_plot_static as box_plot,
    violin_plot_static as violin_plot,
)
from .bivariate import (
    scatter_plot_static as scatter_plot,
    line_plot_static as line_plot,
    correlation_heatmap_static as correlation_heatmap,
    bubble_plot_static as bubble_plot,
    hexbin_plot_static as hexbin_plot,
    regression_plot_static as regression_plot,
    density_contour_static as density_contour,
    grouped_bar_static as grouped_bar,
    box_by_category_static as box_by_category,
    violin_by_category_static as violin_by_category,
    crosstab_heatmap_static as crosstab_heatmap,
    binned_mean_plot_static as binned_mean_plot,
    errorbar_plot_static as errorbar_plot,
    area_between_static as area_between,
    step_plot_static as step_plot,
    joint_scatter_hist_static as joint_scatter_hist,
    bivariate_histogram_static as bivariate_histogram,
    BivariateStats,
    bivariate_summary,
    outlier_scatter_static as outlier_scatter,
    residual_relationship_static as residual_relationship,
    quantile_bin_plot_static as quantile_bin_plot,
    bland_altman_static as bland_altman,
    rank_scatter_static as rank_scatter,
    lag_plot_static as lag_plot,
    conditional_box_static as conditional_box,
)
from .eda import (
    missing_data_plot_static as missing_data_plot,
    distribution_summary_static as distribution_summary,
    class_distribution_static as class_distribution,
)
from .regression import (
    residual_plot_static as residual_plot,
    prediction_plot_static as prediction_plot,
    learning_curve_static as learning_curve,
)
from .classification import (
    confusion_matrix_plot_static as confusion_matrix_plot,
    roc_curve_static as roc_curve,
    precision_recall_curve_static as precision_recall_curve,
)

# Interactive versions imports
from .univariate import (
    histogram_interactive,
    density_interactive,
    box_plot_interactive,
    violin_plot_interactive,
)
from .bivariate import (
    scatter_plot_interactive,
    line_plot_interactive,
    correlation_heatmap_interactive,
    bubble_plot_interactive,
    hexbin_plot_interactive,
    regression_plot_interactive,
    density_contour_interactive,
    grouped_bar_interactive,
    box_by_category_interactive,
    violin_by_category_interactive,
    crosstab_heatmap_interactive,
    binned_mean_plot_interactive,
    errorbar_plot_interactive,
    area_between_interactive,
    step_plot_interactive,
    joint_scatter_hist_interactive,
    bivariate_histogram_interactive,
    outlier_scatter_interactive,
    residual_relationship_interactive,
    quantile_bin_plot_interactive,
    bland_altman_interactive,
    rank_scatter_interactive,
    lag_plot_interactive,
    conditional_box_interactive,
)
from .eda import (
    missing_data_plot_interactive,
    distribution_summary_interactive,
    class_distribution_interactive,
)
from .regression import (
    residual_plot_interactive,
    prediction_plot_interactive,
    learning_curve_interactive,
)
from .classification import (
    confusion_matrix_plot_interactive,
    roc_curve_interactive,
    precision_recall_curve_interactive,
)

__all__ = [
    # Submodules
    "spc",
    "univariate",
    "bivariate",
    "multivariate",
    "eda",
    "xai",
    "regression",
    "classification",
    "clustering",
    "utils",
    "types",
    # Univariate - static
    "histogram",
    "density_plot",
    "box_plot",
    "violin_plot",
    # Univariate - interactive
    "histogram_interactive",
    "density_interactive",
    "box_plot_interactive",
    "violin_plot_interactive",
    # Bivariate - static
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
    "BivariateStats",
    "bivariate_summary",
    "outlier_scatter",
    "residual_relationship",
    "quantile_bin_plot",
    "bland_altman",
    "rank_scatter",
    "lag_plot",
    "conditional_box",
    # Bivariate - interactive
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
    # EDA - static
    "missing_data_plot",
    "distribution_summary",
    "class_distribution",
    # EDA - interactive
    "missing_data_plot_interactive",
    "distribution_summary_interactive",
    "class_distribution_interactive",
    # Regression - static
    "residual_plot",
    "prediction_plot",
    "learning_curve",
    # Regression - interactive
    "residual_plot_interactive",
    "prediction_plot_interactive",
    "learning_curve_interactive",
    # Classification - static
    "confusion_matrix_plot",
    "roc_curve",
    "precision_recall_curve",
    # Classification - interactive
    "confusion_matrix_plot_interactive",
    "roc_curve_interactive",
    "precision_recall_curve_interactive",
]
