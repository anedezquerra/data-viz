# Univariate Module Guide

The univariate module provides static matplotlib charts, interactive Plotly charts, and calculation helpers for one-variable analysis.

## Numeric Data

- `univariate_summary`: classical descriptive statistics.
- `robust_summary`: median, MAD, trimmed mean, winsorized mean, and IQR fences.
- `histogram`, `density_plot`, `box_plot`, `violin_plot`: core distribution views.
- `ecdf_plot`, `survival_curve`, `qq_plot`, `pp_plot`: distribution diagnostics.
- `fitted_distribution_histogram`: histogram with fitted SciPy distribution overlay.
- `univariate_analysis_dashboard`: broad numeric profile dashboard.

```python
import dataviz as dv

summary = dv.univariate_summary(values)
fig = dv.univariate_analysis_dashboard_interactive(values)
```

## Categorical, Ordinal, And Boolean Data

- `category_counts`, `frequency_bar`, `univariate_pareto_chart`: category frequency analysis.
- `ordered_category_counts`, `ordinal_bar`, `likert_summary`: ordered and Likert-style variables.
- `boolean_summary`, `boolean_wilson_interval`, `boolean_bar`: binary indicators and rate intervals.

```python
counts = dv.ordered_category_counts(ratings, order=["Low", "Medium", "High"])
interval = dv.boolean_wilson_interval(flags)
```

## Weighted Data

- `weighted_summary`: weighted mean, variance, standard deviation, and quartiles.
- `weighted_quantile`: weighted quantile helper.
- `weighted_histogram`, `weighted_ecdf_plot`: weighted distribution views.

```python
weighted = dv.weighted_summary(values, weights)
fig = dv.weighted_ecdf_plot_interactive(values, weights)
```

## Data Quality And Outliers

- `data_quality_summary`, `quality_bar`: missing, duplicate, zero, and negative rates.
- `sentinel_value_counts`, `sentinel_rate`: placeholder values such as `-999` or `"N/A"`.
- `outlier_mask`, `flag_outliers`, `cap_outliers`, `remove_outliers`: treatment helpers.
- `outlier_treatment_comparison`: before-after treatment review.

```python
quality = dv.data_quality_summary(values)
treated = dv.cap_outliers(values, rule="iqr")
```

## Tail And Concentration Analysis

- `exceedance_table`: counts and rates above thresholds.
- `concentration_summary`: Gini and top-share metrics.
- `lorenz_curve`, `survival_curve`: concentration and upper-tail visuals.

```python
concentration = dv.concentration_summary(revenue)
fig = dv.lorenz_curve_interactive(revenue)
```

## Text And Datetime Data

- `string_length_summary`, `token_count_summary`, `top_terms`: lightweight text profiling.
- `top_terms_bar`: term count chart.
- `event_counts`, `interarrival_times`: datetime event-stream summaries.
- `event_frequency_plot`, `interarrival_plot`: event timing charts.

```python
terms = dv.top_terms(messages, top_n=10)
events = dv.event_counts(timestamps, freq="W")
```

## Automatic Profiling

- `resolve_univariate_data`: shared column-name and missing-value handling.
- `infer_univariate_kind`: infer numeric, categorical, datetime, boolean, or text.
- `auto_profile`: type-aware summary payload.
- `auto_profile_chart_interactive`: type-aware interactive chart selection.

```python
profile = dv.auto_profile("sales", data=df)
fig = dv.auto_profile_chart_interactive("sales", data=df)
```

