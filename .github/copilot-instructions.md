# DataViz Project Instructions

This is a Python data visualization package project with modular organization and dual rendering modes.

## Project Overview

- **Type**: Python Package
- **Purpose**: Comprehensive data visualization library organized by chart type with static and interactive versions
- **Main Dependencies**: matplotlib, seaborn, numpy, pandas, plotly
- **Python Version**: >=3.8

## Project Structure

The `dataviz/` package is organized into specialized modules, with each chart type in a separate file:

- **spc/** - Statistical Process Control charts
  - `control.py` - control_chart_static, control_chart_interactive
  - `x_range.py` - x_range_chart_static, x_range_chart_interactive
- **univariate/** - Single variable visualizations
  - `histogram.py` - histogram_static, histogram_interactive
  - `density.py` - density_static, density_interactive
  - `box_plot.py` - box_plot_static, box_plot_interactive
  - `violin_plot.py` - violin_plot_static, violin_plot_interactive
- **bivariate/** - Two variable relationships
  - `scatter.py` - scatter_plot_static, scatter_plot_interactive
  - `line.py` - line_plot_static, line_plot_interactive
  - `correlation.py` - correlation_heatmap_static, correlation_heatmap_interactive
- **multivariate/** - Multiple variable analysis
  - `pairplot.py` - pairplot_static, pairplot_interactive
  - `heatmap.py` - heatmap_static, heatmap_interactive
  - `parallel.py` - parallel_coordinates_static, parallel_coordinates_interactive
- **eda/** - Exploratory Data Analysis visualizations
  - `missing_data.py` - missing_data_plot_static, missing_data_plot_interactive
  - `distribution.py` - distribution_summary_static, distribution_summary_interactive
  - `class_dist.py` - class_distribution_static, class_distribution_interactive
- **xai/** - Explainable AI & feature importance charts
  - `feature_imp.py` - feature_importance_static, feature_importance_interactive
  - `shap.py` - shap_plot_static, shap_plot_interactive
  - `partial_dep.py` - partial_dependence_static, partial_dependence_interactive
- **regression/** - Regression model diagnostic plots
  - `residual.py` - residual_plot_static, residual_plot_interactive
  - `prediction.py` - prediction_plot_static, prediction_plot_interactive
  - `learning.py` - learning_curve_static, learning_curve_interactive
- **classification/** - Classification model evaluation
  - `confusion_matrix.py` - confusion_matrix_plot_static, confusion_matrix_plot_interactive
  - `roc.py` - roc_curve_static, roc_curve_interactive
  - `pr_curve.py` - precision_recall_curve_static, precision_recall_curve_interactive
- **clustering/** - Clustering analyses
  - `scatter_clusters.py` - scatter_clusters_static, scatter_clusters_interactive
  - `elbow.py` - elbow_plot_static, elbow_plot_interactive
  - `dendrogram.py` - dendrogram_static, dendrogram_interactive
- **utils/** - Helper functions and utility modules
  - `helpers.py` - setup_plot, apply_theme

## Key Features

- **Dual Versioning**: Every chart has static (matplotlib/seaborn) and interactive (plotly) versions
- **Naming Convention**: 
  - Static: `function_static` (e.g., `histogram_static`)
  - Interactive: `function_interactive` (e.g., `histogram_interactive`)
  - Default alias: `function` defaults to static version (e.g., `histogram`)
- **Modular Files**: Each chart type is in its own `.py` file for maintainability
- **Consistent API**: Both versions share the same parameters and interface

## Adding New Chart Types

1. Create new function in appropriate module file:
   ```python
   def chart_name_static(...) -> plt.Axes:
       # matplotlib/seaborn implementation
       pass
   
   def chart_name_interactive(...) -> go.Figure:
       # plotly implementation
       pass
   ```

2. Export both versions in module `__init__.py`
3. Add convenience alias for static version (default)
4. Add tests for both static and interactive versions
5. Update main `dataviz/__init__.py` if adding top-level convenience imports

## Dependencies

- **Required**: matplotlib, seaborn, numpy, pandas, plotly
- **Optional**: scipy (for hierarchical clustering), kaleido (for plotly image export)

## Development Commands

- Install: `pip install -e ".[dev]"`
- Test: `pytest`
- Format: `black dataviz tests`
- Lint: `flake8 dataviz tests`
- Type check: `mypy dataviz`

## Usage Examples

```python
import dataviz as dv

# Static (default)
ax = dv.histogram(data)

# Interactive
fig = dv.histogram_interactive(data)

# Via submodule
ax = dv.univariate.histogram_static(data)
fig = dv.univariate.histogram_interactive(data)
```


