"""Smoke tests for univariate chart constructors."""

from typing import Any, Dict, Tuple

import pandas as pd
import pytest

import dataviz.univariate as uv


NUMERIC = pd.Series([1.0, 2.0, 2.5, 3.0, 8.0], name="value")
CATEGORY = pd.Series(["Low", "Medium", "High", "Medium", "High"], name="rating")
TEXT = pd.Series(["red blue", "red green", "blue"], name="tags")
DATES = pd.to_datetime(["2026-01-01", "2026-01-02", "2026-01-04"])
WEIGHTS = pd.Series([1.0, 1.0, 2.0, 1.0, 3.0], name="weight")
FRAME = pd.DataFrame({"a": [1, 2, 3, 4], "b": [2, 3, 4, 5]})
VIOLIN_FRAME = pd.DataFrame({"group": ["A", "A", "B", "B"], "value": [1, 2, 3, 4]})


CHART_CALLS = [
    ("histogram_static", (NUMERIC,), {}),
    ("density_static", (NUMERIC,), {}),
    ("box_plot_static", (FRAME,), {}),
    ("violin_plot_static", (VIOLIN_FRAME,), {"x": "group", "y": "value"}),
    ("frequency_bar_static", (CATEGORY,), {}),
    ("pareto_chart_static", (CATEGORY,), {}),
    ("ecdf_plot_static", (NUMERIC,), {}),
    ("cumulative_histogram_static", (NUMERIC,), {}),
    ("qq_plot_static", (NUMERIC,), {}),
    ("pp_plot_static", (NUMERIC,), {}),
    ("outlier_plot_static", (NUMERIC,), {}),
    ("percentile_plot_static", (NUMERIC,), {}),
    ("univariate_diagnostic_panel_static", (NUMERIC,), {}),
    ("fitted_distribution_histogram_static", (NUMERIC,), {}),
    ("robust_location_plot_static", (NUMERIC,), {}),
    ("rug_plot_static", (NUMERIC,), {}),
    ("strip_plot_static", (NUMERIC,), {}),
    ("dot_plot_static", (CATEGORY,), {}),
    ("lollipop_chart_static", (CATEGORY,), {}),
    ("reference_band_histogram_static", (NUMERIC,), {}),
    ("raincloud_plot_static", (NUMERIC,), {}),
    ("ridgeline_plot_static", (FRAME,), {}),
    ("transformation_comparison_static", (NUMERIC,), {}),
    ("event_frequency_plot_static", (DATES,), {}),
    ("interarrival_plot_static", (DATES,), {}),
    ("univariate_analysis_dashboard_static", (NUMERIC,), {}),
    ("weighted_histogram_static", (NUMERIC, WEIGHTS), {}),
    ("quality_bar_static", (NUMERIC,), {}),
    ("survival_curve_static", (NUMERIC,), {}),
    ("lorenz_curve_static", (NUMERIC,), {}),
    ("bootstrap_distribution_plot_static", (NUMERIC,), {"n_resamples": 20, "seed": 1}),
    ("boolean_bar_static", ([True, False, True],), {}),
    ("top_terms_bar_static", (TEXT,), {"top_n": 3}),
    ("weighted_ecdf_plot_static", (NUMERIC, WEIGHTS), {}),
    ("ordinal_bar_static", (CATEGORY,), {"order": ["Low", "Medium", "High"]}),
    ("outlier_treatment_comparison_static", (NUMERIC,), {}),
    ("histogram_interactive", (NUMERIC,), {}),
    ("density_interactive", (NUMERIC,), {}),
    ("box_plot_interactive", (FRAME,), {}),
    ("violin_plot_interactive", (VIOLIN_FRAME,), {"x": "group", "y": "value"}),
    ("frequency_bar_interactive", (CATEGORY,), {}),
    ("pareto_chart_interactive", (CATEGORY,), {}),
    ("ecdf_plot_interactive", (NUMERIC,), {}),
    ("cumulative_histogram_interactive", (NUMERIC,), {}),
    ("qq_plot_interactive", (NUMERIC,), {}),
    ("pp_plot_interactive", (NUMERIC,), {}),
    ("outlier_plot_interactive", (NUMERIC,), {}),
    ("percentile_plot_interactive", (NUMERIC,), {}),
    ("univariate_diagnostic_panel_interactive", (NUMERIC,), {}),
    ("fitted_distribution_histogram_interactive", (NUMERIC,), {}),
    ("robust_location_plot_interactive", (NUMERIC,), {}),
    ("rug_plot_interactive", (NUMERIC,), {}),
    ("strip_plot_interactive", (NUMERIC,), {}),
    ("dot_plot_interactive", (CATEGORY,), {}),
    ("lollipop_chart_interactive", (CATEGORY,), {}),
    ("reference_band_histogram_interactive", (NUMERIC,), {}),
    ("raincloud_plot_interactive", (NUMERIC,), {}),
    ("ridgeline_plot_interactive", (FRAME,), {}),
    ("transformation_comparison_interactive", (NUMERIC,), {}),
    ("event_frequency_plot_interactive", (DATES,), {}),
    ("interarrival_plot_interactive", (DATES,), {}),
    ("univariate_analysis_dashboard_interactive", (NUMERIC,), {}),
    ("weighted_histogram_interactive", (NUMERIC, WEIGHTS), {}),
    ("quality_bar_interactive", (NUMERIC,), {}),
    ("survival_curve_interactive", (NUMERIC,), {}),
    ("lorenz_curve_interactive", (NUMERIC,), {}),
    ("bootstrap_distribution_plot_interactive", (NUMERIC,), {"n_resamples": 20, "seed": 1}),
    ("boolean_bar_interactive", ([True, False, True],), {}),
    ("top_terms_bar_interactive", (TEXT,), {"top_n": 3}),
    ("weighted_ecdf_plot_interactive", (NUMERIC, WEIGHTS), {}),
    ("ordinal_bar_interactive", (CATEGORY,), {"order": ["Low", "Medium", "High"]}),
    ("outlier_treatment_comparison_interactive", (NUMERIC,), {}),
    ("auto_profile_chart_interactive", (NUMERIC,), {}),
]


@pytest.mark.parametrize(("name", "args", "kwargs"), CHART_CALLS)
def test_univariate_chart_constructors_smoke(name: str, args: Tuple[Any, ...], kwargs: Dict[str, Any]) -> None:
    constructor = getattr(uv, name)

    result = constructor(*args, **kwargs)

    assert result is not None
