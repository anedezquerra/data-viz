"""Core tests for univariate statistical helpers."""

from pathlib import Path

import numpy as np
import pandas as pd
import pytest

import dataviz.univariate as uv
from dataviz.univariate.accessors import infer_univariate_kind, resolve_univariate_data
from dataviz.univariate.categorical import category_counts
from dataviz.univariate.diagnostics import normality_test
from dataviz.univariate.distribution import ecdf_values
from dataviz.univariate.datetime import event_counts, interarrival_times
from dataviz.univariate.fitting import compare_distributions, fit_distribution, fitted_pdf_values
from dataviz.univariate.inference import bootstrap_ci, bootstrap_distribution
from dataviz.univariate.ordinal import likert_summary, ordered_category_counts
from dataviz.univariate.profile import auto_profile
from dataviz.univariate.quality import data_quality_summary
from dataviz.univariate.quality import sentinel_rate, sentinel_value_counts
from dataviz.univariate.robust import mad_outliers, robust_summary, trimmed_mean, winsorize_series
from dataviz.univariate.stats import (
    iqr_outliers,
    percentile_table,
    recommended_bin_count,
    univariate_summary,
    zscore_outliers,
)
from dataviz.univariate.tail import concentration_summary, exceedance_table, lorenz_curve_values, survival_values
from dataviz.univariate.text import boolean_summary, boolean_wilson_interval, string_length_summary, token_count_summary, top_terms
from dataviz.univariate.treatment import cap_outliers, flag_outliers, remove_outliers
from dataviz.univariate.transforms import transform_series, transformation_summary
from dataviz.univariate.weighted import weighted_ecdf_values, weighted_quantile, weighted_summary


def test_univariate_summary_reports_core_statistics() -> None:
    values = pd.Series([1, 2, 3, 4, 5, np.nan])

    summary = univariate_summary(values)

    assert summary.count == 5
    assert summary.missing == 1
    assert summary.mean == pytest.approx(3.0)
    assert summary.median == pytest.approx(3.0)
    assert summary.iqr == pytest.approx(2.0)


def test_iqr_outliers_flags_extreme_observation() -> None:
    mask = iqr_outliers([1, 2, 2, 3, 100])

    assert mask.tolist() == [False, False, False, False, True]


def test_zscore_outliers_handles_constant_series() -> None:
    mask = zscore_outliers([5, 5, 5, 5])

    assert mask.tolist() == [False, False, False, False]


def test_recommended_bin_count_validates_method() -> None:
    assert recommended_bin_count([1, 2, 3, 4], method="sqrt") == 2

    with pytest.raises(ValueError):
        recommended_bin_count([1, 2, 3], method="unknown")  # type: ignore[arg-type]


def test_percentile_table_includes_endpoints() -> None:
    table = percentile_table([1, 2, 3, 4], step=50)

    assert table["percentile"].tolist() == [0, 50, 100]
    assert table["value"].tolist() == pytest.approx([1, 2.5, 4])


def test_category_counts_supports_top_n_and_normalization() -> None:
    counts = category_counts(["A", "B", "A", "C", "A"], normalize=True, top_n=1)

    assert counts.index.tolist() == ["A"]
    assert counts.iloc[0] == pytest.approx(0.6)


def test_ecdf_values_are_sorted_and_ranked() -> None:
    x, y = ecdf_values([3, 1, 2])

    assert x.tolist() == [1, 2, 3]
    assert y.tolist() == pytest.approx([1 / 3, 2 / 3, 1.0])


def test_normality_test_validates_sample_size() -> None:
    with pytest.raises(ValueError):
        normality_test([1, 2], method="shapiro")


def test_robust_summary_reports_resistant_locations() -> None:
    summary = robust_summary([1, 2, 3, 4, 100], trim_proportion=0.2, winsor_limits=0.2)

    assert summary.count == 5
    assert summary.median == pytest.approx(3.0)
    assert summary.trimmed_mean == pytest.approx(3.0)
    assert summary.iqr == pytest.approx(2.0)


def test_mad_outliers_flags_large_extreme() -> None:
    mask = mad_outliers([1, 2, 3, 4, 100], threshold=3.0)

    assert mask.tolist() == [False, False, False, False, True]


def test_trimmed_and_winsorized_helpers_validate_proportions() -> None:
    assert trimmed_mean([1, 2, 3, 100], proportion=0.25) == pytest.approx(2.5)
    assert winsorize_series([1, 2, 3, 100], limits=0.25).tolist() == pytest.approx([1.75, 2, 3, 27.25])

    with pytest.raises(ValueError):
        trimmed_mean([1, 2, 3], proportion=0.5)


def test_fit_distribution_returns_reproducible_metrics() -> None:
    fit = fit_distribution([1, 2, 3, 4, 5], distribution="norm")

    assert fit.distribution == "norm"
    assert len(fit.parameters) == 2
    assert fit.aic > 0
    assert fit.bic > 0


def test_compare_distributions_sorts_by_aic() -> None:
    table = compare_distributions([1, 2, 3, 4, 5], distributions=["norm", "expon"])

    assert table["aic"].tolist() == sorted(table["aic"].tolist())
    assert set(table["distribution"]) == {"norm", "expon"}


def test_fitted_pdf_values_returns_curve_and_fit() -> None:
    x_values, y_values, fit = fitted_pdf_values([1, 2, 3, 4, 5], distribution="norm", points=10)

    assert len(x_values) == 10
    assert len(y_values) == 10
    assert fit.distribution == "norm"


def test_transform_series_handles_boxcox_constraints() -> None:
    result = transform_series([1, 2, 3, 4], method="boxcox")

    assert result.method == "boxcox"
    assert result.parameter is not None

    with pytest.raises(ValueError):
        transform_series([0, 1, 2], method="boxcox")


def test_transformation_summary_skips_invalid_methods() -> None:
    table = transformation_summary([-2, -1, 0, 1, 2])

    assert "yeojohnson" in table["method"].tolist()
    assert "boxcox" not in table["method"].tolist()


def test_event_counts_and_interarrival_times() -> None:
    timestamps = ["2026-01-01", "2026-01-01", "2026-01-03"]

    counts = event_counts(timestamps, freq="D")
    gaps = interarrival_times(timestamps, unit="D")

    assert counts.tolist() == [2, 0, 1]
    assert gaps.tolist() == pytest.approx([0.0, 2.0])


def test_weighted_summary_and_quantile() -> None:
    values = [1, 2, 3]
    weights = [1, 1, 4]

    summary = weighted_summary(values, weights)

    assert summary.weight_sum == pytest.approx(6.0)
    assert summary.mean == pytest.approx(15 / 6)
    assert weighted_quantile(values, weights, 0.5) == pytest.approx(3.0)


def test_data_quality_summary_reports_rates() -> None:
    summary = data_quality_summary([1, 1, 0, -2, None])

    assert summary.count == 5
    assert summary.missing_rate == pytest.approx(0.2)
    assert summary.duplicate_rate == pytest.approx(0.25)
    assert summary.zero_rate == pytest.approx(0.25)
    assert summary.negative_rate == pytest.approx(0.25)


def test_tail_helpers_report_survival_exceedance_and_concentration() -> None:
    x_values, survival = survival_values([1, 2, 3])
    table = exceedance_table([1, 2, 3], [1, 2])
    population, share = lorenz_curve_values([1, 1, 2])
    concentration = concentration_summary([1, 1, 2])

    assert x_values.tolist() == [1, 2, 3]
    assert survival.tolist() == pytest.approx([2 / 3, 1 / 3, 0.0])
    assert table["count"].tolist() == [2, 1]
    assert population[[0, -1]].tolist() == pytest.approx([0.0, 1.0])
    assert share[[0, -1]].tolist() == pytest.approx([0.0, 1.0])
    assert concentration.gini == pytest.approx(1 / 6)


def test_bootstrap_helpers_are_reproducible_with_seed() -> None:
    distribution = bootstrap_distribution([1, 2, 3, 4], statistic="mean", n_resamples=20, seed=42)
    ci = bootstrap_ci([1, 2, 3, 4], statistic="mean", n_resamples=20, seed=42)

    assert len(distribution) == 20
    assert ci.estimate == pytest.approx(2.5)
    assert ci.lower <= ci.estimate <= ci.upper


def test_text_and_boolean_helpers() -> None:
    boolean = boolean_summary([True, False, True, None])
    lengths = string_length_summary(["alpha", "bb"])
    tokens = token_count_summary(["hello world", "solo"])
    terms = top_terms(["Red blue", "red"], top_n=1)

    assert boolean.true_count == 2
    assert boolean.true_rate == pytest.approx(2 / 3)
    assert lengths.tolist() == [5, 2]
    assert tokens.tolist() == [2, 1]
    assert terms.index.tolist() == ["red"]
    assert terms.iloc[0] == 2


def test_resolve_univariate_data_supports_column_names() -> None:
    df = pd.DataFrame({"sales": [1, 2, None, 4]})

    resolved = resolve_univariate_data("sales", data=df, require_numeric=True)

    assert resolved.name == "sales"
    assert resolved.values.tolist() == [1, 2, 4]
    assert resolved.missing_count == 1
    assert resolved.kind == "numeric"


def test_infer_univariate_kind_detects_common_types() -> None:
    assert infer_univariate_kind([True, False]) == "boolean"
    assert infer_univariate_kind(pd.to_datetime(["2026-01-01", "2026-01-02"])) == "datetime"
    assert infer_univariate_kind(["red", "blue", "red"]) == "categorical"


def test_auto_profile_returns_type_specific_payload() -> None:
    profile = auto_profile([1, 2, 3], name="score")

    assert profile.name == "score"
    assert profile.kind == "numeric"
    assert "stats" in profile.summary


def test_ordinal_and_likert_helpers_preserve_order() -> None:
    values = ["High", "Low", "High"]
    counts = ordered_category_counts(values, order=["Low", "Medium", "High"])
    table = likert_summary(["Agree", "Neutral", "Agree"])

    assert counts.index.tolist() == ["Low", "Medium", "High"]
    assert counts.tolist() == [1, 0, 2]
    assert table["count"].sum() == 3


def test_sentinel_helpers_count_placeholder_values() -> None:
    counts = sentinel_value_counts([1, -999, -999, None], [-999])

    assert counts.loc[-999] == 2
    assert sentinel_rate([1, -999, -999, None], [-999]) == pytest.approx(0.5)


def test_boolean_wilson_interval_bounds_rate() -> None:
    interval = boolean_wilson_interval([True, False, True, True])

    assert interval.lower <= interval.true_rate <= interval.upper
    assert interval.confidence_level == pytest.approx(0.95)


def test_weighted_ecdf_values_use_weight_mass() -> None:
    x_values, probabilities = weighted_ecdf_values([1, 2, 3], [1, 1, 2])

    assert x_values.tolist() == [1, 2, 3]
    assert probabilities.tolist() == pytest.approx([0.25, 0.5, 1.0])


def test_outlier_treatment_helpers_cap_remove_and_flag() -> None:
    values = [1, 2, 2, 3, 100]
    capped = cap_outliers(values)
    removed = remove_outliers(values)
    flagged = flag_outliers(values)

    assert capped.treated.iloc[-1] == pytest.approx(3)
    assert removed.treated.tolist() == [1, 2, 2, 3]
    assert flagged["is_outlier"].tolist() == [False, False, False, False, True]


def test_univariate_export_parity() -> None:
    missing = [name for name in uv.__all__ if not hasattr(uv, name)]

    assert missing == []


def test_dependency_metadata_contains_runtime_requirements() -> None:
    pyproject = Path("pyproject.toml").read_text()
    requirements = Path("requirements.txt").read_text()

    for dependency in ["matplotlib", "numpy", "pandas", "plotly", "scipy", "seaborn"]:
        assert dependency in pyproject
        assert dependency in requirements
