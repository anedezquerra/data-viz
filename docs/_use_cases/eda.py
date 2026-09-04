"""Curated use cases for eda member pages."""

USE_CASES = {
    # charts.py
    "dataviz.eda.charts.missing_data_plot": "Use when auditing a dataset for missing values before modeling to see which columns need imputation.",
    "dataviz.eda.charts.distribution_summary": "Use at the start of exploratory analysis to review the distribution of every dataframe column at once.",
    "dataviz.eda.charts.class_distribution": "Use to check target class balance before training a classifier and decide whether rebalancing is needed.",
    # class_dist.py
    "dataviz.eda.class_dist.class_distribution_static": "Use to check target class balance before training a classifier and decide whether rebalancing is needed.",
    "dataviz.eda.class_dist.class_distribution_interactive": "Use to check target class balance before training a classifier and decide whether rebalancing is needed.",
    # distribution.py
    "dataviz.eda.distribution.distribution_summary_static": "Use at the start of exploratory analysis to review the distribution of every dataframe column at once.",
    "dataviz.eda.distribution.distribution_summary_interactive": "Use at the start of exploratory analysis to review the distribution of every dataframe column at once.",
    # missing_data.py
    "dataviz.eda.missing_data.missing_data_plot_static": "Use when auditing a dataset for missing values before modeling to see which columns need imputation.",
    "dataviz.eda.missing_data.missing_data_plot_interactive": "Use when auditing a dataset for missing values before modeling to see which columns need imputation.",
}
