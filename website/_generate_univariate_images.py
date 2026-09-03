"""Render four real univariate example images per chart family for the docs website.

Deterministic synthetic data (``numpy.random.default_rng``) drives every chart so
the output is reproducible. Images and a ``manifest.json`` (family -> image list
with captions) are written to ``website/assets/examples/univariate``; the manifest
is consumed by ``_generate_function_docs.mjs`` to attach galleries to univariate
pages.
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

import dataviz as dv  # noqa: E402

OUT_DIR = Path(__file__).resolve().parent / "assets" / "examples" / "univariate"
DPI = 110


def _figure_of(result):
    if isinstance(result, plt.Figure):
        return result
    if isinstance(result, (tuple, list)):
        return result[0].figure
    return result.figure


def _rng(seed: int) -> np.random.Generator:
    return np.random.default_rng(seed)


def _spiked(seed=4, n=500):
    values = _rng(seed).normal(170, 6, n)
    values[[40, 200, 380]] += np.array([35.0, -30.0, 40.0])
    return values


def _continuous_scenarios():
    return [
        (
            "Roughly normal — a symmetric spread around the centre.",
            _rng(0).normal(170, 10, 500),
        ),
        (
            "Right-skewed — a long upper tail of occasional large values.",
            _rng(1).gamma(2.0, 2.5, 500) + 150,
        ),
        (
            "Bimodal — two overlapping subgroups form distinct humps.",
            np.r_[_rng(2).normal(160, 5, 250), _rng(3).normal(180, 5, 250)],
        ),
        (
            "Heavy-tailed with spikes — extreme values stretch the scale.",
            _spiked(),
        ),
    ]


def _categorical_series(seed, counts):
    categories = ["Scratch", "Dent", "Misalign", "Color", "Crack", "Other"]
    labels = np.repeat(categories, counts)
    return pd.Series(_rng(seed).permutation(labels))


def _categorical_scenarios():
    return [
        (
            "Vital few — two categories account for most records.",
            _categorical_series(7, [140, 90, 40, 20, 8, 4]),
        ),
        (
            "Even spread — no single category dominates.",
            _categorical_series(8, [60, 55, 50, 45, 40, 35]),
        ),
        (
            "Single dominant cause — one category dwarfs the rest.",
            _categorical_series(9, [220, 30, 20, 12, 8, 5]),
        ),
        (
            "Long tail — many small contributors trail the leaders.",
            _categorical_series(10, [120, 70, 25, 22, 18, 15]),
        ),
    ]


def _group_frames():
    def frame(seed, shifts=(0.0, 0.0, 0.0), spreads=(0.5, 0.5, 0.5), outliers=False):
        rng = _rng(seed)
        data = pd.DataFrame(
            {
                name: rng.normal(10.0 + shifts[i], spreads[i], 100)
                for i, name in enumerate(["Line A", "Line B", "Line C"])
            }
        )
        if outliers:
            data.loc[data.index[:6], "Line C"] += 4.0
        return data

    return [
        ("Aligned groups — all three lines share centre and spread.", frame(50)),
        (
            "Shifted group — Line B runs consistently high.",
            frame(51, shifts=(0.0, 1.2, 0.0)),
        ),
        (
            "Unequal spread — Line C varies far more than the others.",
            frame(52, spreads=(0.5, 0.5, 1.4)),
        ),
        (
            "Contaminated group — a handful of extremes inflate Line C.",
            frame(53, outliers=True),
        ),
    ]


def _times(gaps_hours, start="2024-01-01"):
    gaps = np.asarray(gaps_hours, dtype=float)
    stamps = pd.Timestamp(start) + pd.to_timedelta(gaps.cumsum(), unit="h")
    return pd.Series(stamps)


def build_histogram():
    return [
        (cap, dv.univariate.histogram_static(pd.Series(v, name="Value"), bins=30))
        for cap, v in _continuous_scenarios()
    ]


def build_density():
    return [
        (cap, dv.univariate.density_static(pd.Series(v, name="Value")))
        for cap, v in _continuous_scenarios()
    ]


def build_box_plot():
    return [
        (cap, dv.univariate.box_plot_static(df, ylabel="Measurement"))
        for cap, df in _group_frames()
    ]


def build_violin_plot():
    return [
        (cap, dv.univariate.violin_plot_static(df, ylabel="Measurement"))
        for cap, df in _group_frames()
    ]


def build_frequency_bar():
    return [
        (cap, dv.univariate.frequency_bar_static(s)) for cap, s in _categorical_scenarios()
    ]


def build_pareto_chart():
    return [
        (cap, dv.univariate.pareto_chart_static(s)) for cap, s in _categorical_scenarios()
    ]


def build_ecdf_plot():
    return [
        (cap, dv.univariate.ecdf_plot_static(pd.Series(v, name="Value")))
        for cap, v in _continuous_scenarios()
    ]


def build_cumulative_histogram():
    return [
        (
            cap,
            dv.univariate.cumulative_histogram_static(pd.Series(v, name="Value"), bins=30),
        )
        for cap, v in _continuous_scenarios()
    ]


def _fit_scenarios():
    return [
        ("Normal data — points hug the reference line.", _rng(5).normal(0, 1, 300)),
        (
            "Right-skewed — the points bend upward at the high end.",
            _rng(6).gamma(2.0, 1.0, 300),
        ),
        ("Heavy tails — both ends pull away from the line.", _rng(7).standard_t(3, 300)),
        (
            "Light tails — bounded data flatten at the extremes.",
            _rng(8).uniform(-2, 2, 300),
        ),
    ]


def build_qq_plot():
    return [
        (cap, dv.univariate.qq_plot_static(pd.Series(v, name="Value")))
        for cap, v in _fit_scenarios()
    ]


def build_pp_plot():
    captions = [
        "Normal data — cumulative probabilities track the diagonal.",
        "Right-skewed — the centre sags below the diagonal.",
        "Heavy tails — the curve bows in an S around the diagonal.",
        "Light tails — the centre overshoots the diagonal.",
    ]
    return [
        (cap, dv.univariate.pp_plot_static(pd.Series(v, name="Value")))
        for cap, (_, v) in zip(captions, _fit_scenarios())
    ]


def build_outlier_plot():
    clean = _rng(9).normal(10.0, 0.5, 200)
    spikes = _rng(10).normal(10.0, 0.5, 200)
    spikes[[25, 90, 150]] += np.array([3.0, -2.8, 3.4])
    cluster = _rng(11).normal(10.0, 0.5, 200)
    cluster[80:90] += 1.8
    skewed = _rng(12).gamma(2.0, 0.5, 200) + 9.0
    scenarios = [
        ("Clean data — no points flagged by the IQR rule.", clean),
        ("Isolated spikes — three points break the fences.", spikes),
        ("Outlier cluster — a run of high values is flagged.", cluster),
        ("Skewed data — the natural tail trips the rule.", skewed),
    ]
    return [
        (cap, dv.univariate.outlier_plot_static(pd.Series(v, name="Value")))
        for cap, v in scenarios
    ]


def build_percentile_plot():
    return [
        (cap, dv.univariate.percentile_plot_static(pd.Series(v, name="Value")))
        for cap, v in _continuous_scenarios()
    ]


def build_univariate_diagnostic_panel():
    return [
        (cap, dv.univariate.univariate_diagnostic_panel_static(pd.Series(v, name="Value")))
        for cap, v in _continuous_scenarios()
    ]


def build_fitted_distribution_histogram():
    scenarios = [
        (
            "Normal fit — the curve tracks the bars closely.",
            _rng(60).normal(10.0, 1.0, 400),
            "norm",
        ),
        (
            "Lognormal fit — the model follows the skewed tail.",
            _rng(61).lognormal(2.0, 0.4, 400),
            "lognorm",
        ),
        (
            "Gamma fit — a flexible match for positive skew.",
            _rng(62).gamma(3.0, 1.0, 400),
            "gamma",
        ),
        (
            "Exponential fit — decay modelled from the origin.",
            _rng(63).exponential(2.0, 400),
            "expon",
        ),
    ]
    return [
        (
            cap,
            dv.univariate.fitted_distribution_histogram_static(
                pd.Series(v, name="Value"), distribution=dist
            ),
        )
        for cap, v, dist in scenarios
    ]


def build_robust_location_plot():
    clean = _rng(64).normal(10.0, 0.5, 200)
    contaminated = _rng(65).normal(10.0, 0.5, 200)
    contaminated[:5] += 6.0
    skewed = _rng(66).gamma(2.0, 0.5, 200) + 9.0
    heavy = _rng(67).standard_t(3, 200) * 0.5 + 10.0
    scenarios = [
        ("Clean data — every location estimate agrees.", clean),
        ("Contaminated — the mean is pulled; robust estimates resist.", contaminated),
        ("Skewed data — the mean sits above the median.", skewed),
        ("Heavy tails — trimmed and winsorised means stay centred.", heavy),
    ]
    return [
        (cap, dv.univariate.robust_location_plot_static(pd.Series(v, name="Value")))
        for cap, v in scenarios
    ]


def _small_samples():
    clustered = np.r_[_rng(70).normal(160, 3, 40), _rng(71).normal(180, 3, 40)]
    skewed = _rng(72).gamma(2.0, 2.0, 80) + 150
    sparse = _rng(73).normal(170, 10, 25)
    return [
        ("Even spread — observations fill the range uniformly.", _rng(74).normal(170, 10, 80)),
        ("Two clusters — a clear gap separates the subgroups.", clustered),
        ("Skewed sample — points pile up at the low end.", skewed),
        ("Small sample — every one of 25 observations is visible.", sparse),
    ]


def build_rug_plot():
    return [
        (cap, dv.univariate.rug_plot_static(pd.Series(v, name="Value")))
        for cap, v in _small_samples()
    ]


def build_strip_plot():
    return [
        (cap, dv.univariate.strip_plot_static(pd.Series(v, name="Value")))
        for cap, v in _small_samples()
    ]


def build_dot_plot():
    return [
        (cap, dv.univariate.dot_plot_static(s)) for cap, s in _categorical_scenarios()
    ]


def build_lollipop_chart():
    return [
        (cap, dv.univariate.lollipop_chart_static(s)) for cap, s in _categorical_scenarios()
    ]


def build_reference_band_histogram():
    return [
        (
            cap,
            dv.univariate.reference_band_histogram_static(pd.Series(v, name="Value"), bins=30),
        )
        for cap, v in _continuous_scenarios()
    ]


def build_raincloud_plot():
    scenarios = [
        ("Symmetric sample — cloud, box, and points agree.", _rng(75).normal(170, 10, 120)),
        (
            "Right-skewed — the rain stretches into the upper tail.",
            _rng(76).gamma(2.0, 2.5, 120) + 150,
        ),
        (
            "Bimodal — two humps the box plot alone would hide.",
            np.r_[_rng(77).normal(160, 4, 60), _rng(78).normal(180, 4, 60)],
        ),
        ("Small sample — 40 observations, all visible.", _rng(79).normal(170, 10, 40)),
    ]
    return [
        (cap, dv.univariate.raincloud_plot_static(pd.Series(v, name="Value")))
        for cap, v in scenarios
    ]


def build_ridgeline_plot():
    def frame(seed, shifts, spreads=(0.5,) * 4):
        rng = _rng(seed)
        return pd.DataFrame(
            {
                f"Week {i + 1}": rng.normal(10.0 + shifts[i], spreads[i], 120)
                for i in range(4)
            }
        )

    scenarios = [
        (
            "Drifting centre — the distribution walks upward week by week.",
            frame(80, (0.0, 0.3, 0.6, 0.9)),
        ),
        (
            "Stable process — four weeks stack on the same centre.",
            frame(81, (0.0, 0.0, 0.0, 0.0)),
        ),
        (
            "Widening spread — later weeks grow more variable.",
            frame(82, (0.0,) * 4, (0.3, 0.5, 0.8, 1.1)),
        ),
        (
            "Emerging subgroup — week 4 splits toward a second mode.",
            pd.DataFrame(
                {
                    "Week 1": _rng(83).normal(10.0, 0.5, 120),
                    "Week 2": _rng(84).normal(10.0, 0.5, 120),
                    "Week 3": _rng(85).normal(10.0, 0.5, 120),
                    "Week 4": np.r_[_rng(86).normal(10.0, 0.4, 60), _rng(87).normal(11.5, 0.4, 60)],
                }
            ),
        ),
    ]
    return [(cap, dv.univariate.ridgeline_plot_static(df)) for cap, df in scenarios]


def build_transformation_comparison():
    scenarios = [
        (
            "Strong skew — the log transform restores symmetry.",
            _rng(88).lognormal(0.0, 0.8, 500),
        ),
        (
            "Gamma data — transforms pull in the long right tail.",
            _rng(89).gamma(2.0, 1.0, 500),
        ),
        (
            "Moderate skew — a milder transform suffices.",
            _rng(90).gamma(6.0, 1.0, 500),
        ),
        (
            "Near-symmetric — transforms change little.",
            _rng(91).normal(20.0, 3.0, 500),
        ),
    ]
    return [
        (cap, dv.univariate.transformation_comparison_static(pd.Series(v, name="Value")))
        for cap, v in scenarios
    ]


def _event_scenarios():
    steady = _times(_rng(92).exponential(12.0, 300))
    surge = _times(np.r_[_rng(93).exponential(12.0, 150), _rng(94).exponential(4.0, 150)])
    growing = _times(_rng(95).exponential(12.0, 300) * np.linspace(2.0, 0.4, 300))
    gapped_gaps = _rng(96).exponential(12.0, 300)
    gapped_gaps[150] += 60 * 24
    gapped = _times(gapped_gaps)
    return [
        ("Steady stream — weekly counts hover around a constant rate.", steady),
        ("Sudden surge — event volume jumps in the second half.", surge),
        ("Accelerating demand — intervals shrink as activity grows.", growing),
        ("Quiet gap — a two-month lull splits the timeline.", gapped),
    ]


def build_event_frequency_plot():
    return [
        (cap, dv.univariate.event_frequency_plot_static(t, freq="W"))
        for cap, t in _event_scenarios()
    ]


def build_interarrival_plot():
    poisson = _times(_rng(97).exponential(24.0, 300))
    bursty = _times(
        np.where(_rng(98).random(300) < 0.7, _rng(99).exponential(2.0, 300), _rng(100).exponential(120.0, 300))
    )
    regular = _times(_rng(101).normal(24.0, 2.0, 300))
    bimodal = _times(
        np.r_[_rng(102).exponential(6.0, 150), _rng(103).exponential(96.0, 150)]
    )
    scenarios = [
        ("Poisson process — gaps follow the exponential shape.", poisson),
        ("Bursty arrivals — many short waits mixed with long silences.", bursty),
        ("Clockwork-regular — gaps cluster tightly around one day.", regular),
        ("Two regimes — fast and slow phases form a bimodal gap mix.", bimodal),
    ]
    return [(cap, dv.univariate.interarrival_plot_static(t, unit="D")) for cap, t in scenarios]


def build_univariate_analysis_dashboard():
    return [
        (cap, dv.univariate.univariate_analysis_dashboard_static(pd.Series(v, name="Value")))
        for cap, v in _continuous_scenarios()
    ]


def _weighted_scenarios():
    values = _rng(104).normal(50.0, 10.0, 500)
    tail_weights = np.where(values > 55, 4.0, 1.0)
    survey_values = np.r_[_rng(105).normal(45.0, 8.0, 300), _rng(106).normal(60.0, 8.0, 200)]
    survey_weights = np.r_[np.ones(300), np.full(200, 0.5)]
    skewed = _rng(107).gamma(2.0, 5.0, 500)
    amount_weights = skewed / skewed.mean()
    return [
        (
            "Uniform weights — the weighted view matches the raw sample.",
            values,
            np.ones(500),
        ),
        (
            "Tail emphasis — large values count four times as much.",
            values,
            tail_weights,
        ),
        (
            "Survey weights — an oversampled segment is weighted down.",
            survey_values,
            survey_weights,
        ),
        (
            "Amount-weighted — weighting by size shifts the mass rightward.",
            skewed,
            amount_weights,
        ),
    ]


def build_weighted_histogram():
    return [
        (
            cap,
            dv.univariate.weighted_histogram_static(
                pd.Series(v, name="Value"), pd.Series(w), bins=30
            ),
        )
        for cap, v, w in _weighted_scenarios()
    ]


def build_weighted_ecdf_plot():
    return [
        (cap, dv.univariate.weighted_ecdf_plot_static(pd.Series(v, name="Value"), pd.Series(w)))
        for cap, v, w in _weighted_scenarios()
    ]


def build_quality_bar():
    clean = pd.Series(_rng(108).normal(10.0, 1.0, 300))
    clean.iloc[:3] = np.nan
    messy = pd.Series(_rng(109).normal(10.0, 1.0, 300))
    messy.iloc[:15] = np.nan
    messy.iloc[15:30] = 0.0
    messy.iloc[30:50] = messy.iloc[50:70].to_numpy()
    zero_inflated = pd.Series(np.where(_rng(110).random(300) < 0.4, 0.0, _rng(111).poisson(3.0, 300)))
    signed = pd.Series(_rng(112).normal(0.0, 5.0, 300))
    scenarios = [
        ("Mostly clean — only a sliver of missing values.", clean),
        ("Messy column — missing, zeros, and duplicates all present.", messy),
        ("Zero-inflated — two in five observations are exactly zero.", zero_inflated),
        ("Signed values — about half the column is negative by design.", signed),
    ]
    return [(cap, dv.univariate.quality_bar_static(s)) for cap, s in scenarios]


def build_survival_curve():
    scenarios = [
        (
            "Constant hazard — exponential lifetimes decay steadily.",
            _rng(113).exponential(365.0, 400),
        ),
        (
            "Ageing population — Weibull wear-out accelerates over time.",
            _rng(114).weibull(2.5, 400) * 365,
        ),
        (
            "Long-lived tail — a few units survive far beyond the rest.",
            _rng(115).lognormal(5.5, 0.5, 400),
        ),
        (
            "Two subgroups — an early-failure cohort drops the curve fast.",
            np.r_[_rng(116).exponential(120.0, 100), _rng(117).weibull(3.0, 300) * 500],
        ),
    ]
    return [
        (cap, dv.univariate.survival_curve_static(pd.Series(v, name="Days")))
        for cap, v in scenarios
    ]


def build_lorenz_curve():
    scenarios = [
        (
            "Near-equal — the curve hugs the line of perfect equality.",
            _rng(118).uniform(40_000, 60_000, 1000),
        ),
        (
            "Typical inequality — a moderate bow away from equality.",
            _rng(119).lognormal(10.5, 0.6, 1000),
        ),
        (
            "High concentration — the top share holds most of the total.",
            (_rng(120).pareto(1.5, 1000) + 1.0) * 10_000,
        ),
        (
            "Extreme dominance — a handful of observations own almost everything.",
            np.r_[_rng(121).lognormal(10.0, 0.4, 990), _rng(122).lognormal(13.5, 0.3, 10)],
        ),
    ]
    return [
        (cap, dv.univariate.lorenz_curve_static(pd.Series(v, name="Income")))
        for cap, v in scenarios
    ]


def build_bootstrap_distribution_plot():
    scenarios = [
        (
            "Mean of normal data — a symmetric, narrow sampling distribution.",
            _rng(123).normal(170, 10, 200),
            "mean",
        ),
        (
            "Median of skewed data — the bootstrap stays well behaved.",
            _rng(124).gamma(2.0, 2.5, 200) + 150,
            "median",
        ),
        (
            "Standard deviation — wider and slightly right-skewed.",
            _rng(125).normal(170, 10, 200),
            "std",
        ),
        (
            "Small sample — n=30 leaves visible resampling noise.",
            _rng(126).normal(170, 10, 30),
            "mean",
        ),
    ]
    return [
        (
            cap,
            dv.univariate.bootstrap_distribution_plot_static(
                pd.Series(v, name="Value"), statistic=stat, n_resamples=1000, seed=0
            ),
        )
        for cap, v, stat in scenarios
    ]


def build_boolean_bar():
    scenarios = [
        ("Balanced — true and false are nearly even.", 0.5),
        ("Imbalanced — true cases outnumber false four to one.", 0.8),
        ("Rare positives — only five percent of flags are true.", 0.05),
        ("Near-unanimous — almost every record is true.", 0.97),
    ]
    return [
        (cap, dv.univariate.boolean_bar_static(pd.Series(_rng(130 + i).random(300) < p)))
        for i, (cap, p) in enumerate(scenarios)
    ]


def build_top_terms_bar():
    def words(seed, terms, probs, n=500):
        return pd.Series(_rng(seed).choice(terms, size=n, p=probs))

    tickets = ["delivery", "quality", "price", "support", "packaging", "refund", "shipping"]
    scenarios = [
        (
            "Support tickets — delivery and quality dominate the queue.",
            words(134, tickets, [0.30, 0.22, 0.16, 0.12, 0.09, 0.06, 0.05]),
        ),
        (
            "Product reviews — one term towers over the rest.",
            words(135, tickets, [0.55, 0.12, 0.10, 0.08, 0.06, 0.05, 0.04]),
        ),
        (
            "Search queries — a flat vocabulary with no clear leader.",
            words(136, tickets, [0.16, 0.15, 0.15, 0.14, 0.14, 0.13, 0.13]),
        ),
        (
            "Error logs — a long tail of rare messages.",
            words(137, tickets, [0.40, 0.25, 0.15, 0.10, 0.05, 0.03, 0.02]),
        ),
    ]
    return [(cap, dv.univariate.top_terms_bar_static(s, top_n=10)) for cap, s in scenarios]


def build_ordinal_bar():
    scale = ["Poor", "Fair", "Good", "Very good", "Excellent"]
    scenarios = [
        (
            "Positive skew — most ratings land at the top end.",
            [0.05, 0.15, 0.35, 0.30, 0.15],
        ),
        (
            "Negative skew — dissatisfaction piles up at the low end.",
            [0.40, 0.30, 0.15, 0.10, 0.05],
        ),
        ("Uniform — every rating is chosen about equally.", [0.20] * 5),
        (
            "Polarised — opinions split between the two extremes.",
            [0.35, 0.05, 0.10, 0.10, 0.40],
        ),
    ]
    return [
        (
            cap,
            dv.univariate.ordinal_bar_static(
                pd.Series(_rng(140 + i).choice(scale, size=400, p=probs)), order=scale
            ),
        )
        for i, (cap, probs) in enumerate(scenarios)
    ]


def build_outlier_treatment_comparison():
    def spiked_values(seed):
        values = _rng(seed).normal(10.0, 0.5, 300)
        values[[10, 120, 250]] += np.array([4.0, -3.5, 4.5])
        return pd.Series(values, name="Value")

    scenarios = [
        (
            "IQR capping — fences pull the spikes back to the whiskers.",
            spiked_values(144),
            "iqr",
            "cap",
        ),
        (
            "IQR removal — flagged points are dropped entirely.",
            spiked_values(145),
            "iqr",
            "remove",
        ),
        (
            "Z-score capping — a stricter 3σ rule trims the extremes.",
            spiked_values(146),
            "zscore",
            "cap",
        ),
        (
            "MAD capping — the robust rule resists masking.",
            spiked_values(147),
            "mad",
            "cap",
        ),
    ]
    return [
        (
            cap,
            dv.univariate.outlier_treatment_comparison_static(
                v, rule=rule, treatment=treatment
            ),
        )
        for cap, v, rule, treatment in scenarios
    ]


BUILDERS = {
    "histogram": build_histogram,
    "density": build_density,
    "box_plot": build_box_plot,
    "violin_plot": build_violin_plot,
    "frequency_bar": build_frequency_bar,
    "pareto_chart": build_pareto_chart,
    "ecdf_plot": build_ecdf_plot,
    "cumulative_histogram": build_cumulative_histogram,
    "qq_plot": build_qq_plot,
    "pp_plot": build_pp_plot,
    "outlier_plot": build_outlier_plot,
    "percentile_plot": build_percentile_plot,
    "univariate_diagnostic_panel": build_univariate_diagnostic_panel,
    "fitted_distribution_histogram": build_fitted_distribution_histogram,
    "robust_location_plot": build_robust_location_plot,
    "rug_plot": build_rug_plot,
    "strip_plot": build_strip_plot,
    "dot_plot": build_dot_plot,
    "lollipop_chart": build_lollipop_chart,
    "reference_band_histogram": build_reference_band_histogram,
    "raincloud_plot": build_raincloud_plot,
    "ridgeline_plot": build_ridgeline_plot,
    "transformation_comparison": build_transformation_comparison,
    "event_frequency_plot": build_event_frequency_plot,
    "interarrival_plot": build_interarrival_plot,
    "univariate_analysis_dashboard": build_univariate_analysis_dashboard,
    "weighted_histogram": build_weighted_histogram,
    "quality_bar": build_quality_bar,
    "survival_curve": build_survival_curve,
    "lorenz_curve": build_lorenz_curve,
    "bootstrap_distribution_plot": build_bootstrap_distribution_plot,
    "boolean_bar": build_boolean_bar,
    "top_terms_bar": build_top_terms_bar,
    "weighted_ecdf_plot": build_weighted_ecdf_plot,
    "ordinal_bar": build_ordinal_bar,
    "outlier_treatment_comparison": build_outlier_treatment_comparison,
}


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    manifest: dict[str, list[dict[str, str]]] = {}

    for family, builder in BUILDERS.items():
        entries = builder()
        images = []
        for index, (caption, result) in enumerate(entries, start=1):
            fig = _figure_of(result)
            name = f"{family}_{index}.png"
            fig.savefig(OUT_DIR / name, dpi=DPI, bbox_inches="tight")
            plt.close(fig)
            images.append(
                {"src": f"assets/examples/univariate/{name}", "caption": caption}
            )
        manifest[family] = images
        print(f"{family}: {len(images)} images")

    (OUT_DIR / "manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )
    print(f"manifest: {OUT_DIR / 'manifest.json'}")


if __name__ == "__main__":
    main()
