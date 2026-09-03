"""Render four real bivariate example images per chart family for the docs site.

Deterministic synthetic data (``numpy.random.default_rng``) drives every chart
so the output is reproducible. Images and a ``manifest.json`` (family -> image
list with captions) are written to ``website/assets/examples/bivariate``; the
manifest is consumed by ``_generate_function_docs.mjs`` to attach galleries to
bivariate pages.
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

OUT_DIR = Path(__file__).resolve().parent / "assets" / "examples" / "bivariate"
DPI = 110


def _figure_of(result):
    if isinstance(result, plt.Figure):
        return result
    if isinstance(result, (tuple, list)):
        return result[0].figure
    return result.figure


def _rng(seed: int) -> np.random.Generator:
    return np.random.default_rng(seed)


def _xy_scenarios(n=200):
    """Four (x, y) pairs: linear, nonlinear, uncorrelated, outlier-driven."""
    x1 = _rng(0).normal(50, 10, n)
    linear = (x1, 2.0 * x1 + _rng(1).normal(0, 15, n))

    x2 = _rng(2).uniform(0, 10, n)
    nonlinear = (x2, (x2 - 5) ** 2 + _rng(3).normal(0, 3, n))

    none = (_rng(4).normal(50, 10, n), _rng(5).normal(100, 15, n))

    x4 = _rng(6).normal(50, 10, n)
    y4 = 1.5 * x4 + _rng(7).normal(0, 8, n)
    x4 = np.r_[x4, [95, 10, 90]]
    y4 = np.r_[y4, [20, 160, 25]]
    return [
        ("Strong linear trend — y rises steadily with x.", linear),
        ("Curved relationship — a parabola the eye catches at once.", nonlinear),
        ("No correlation — the cloud is round and directionless.", none),
        ("Outlier-driven — three stray points dominate the picture.", (x4, y4)),
    ]


def build_scatter_plot():
    return [(cap, dv.bivariate.scatter_plot_static(x, y)) for cap, (x, y) in
            _xy_scenarios()]


def build_line_plot():
    n = 60
    x = pd.Series(np.arange(n), name="Day")
    trend = 100 + np.arange(n) * 0.4 + _rng(10).normal(0, 3, n)
    seasonal = 50 + 10 * np.sin(np.arange(n) / 5.0) + _rng(11).normal(0, 2, n)
    flat = _rng(12).normal(75, 4, n)
    drop = 100 - np.arange(n) * 0.5 + _rng(13).normal(0, 2, n)
    drop[35:] -= 12
    scenarios = [
        ("Upward trend — throughput climbs steadily over the period.", trend),
        ("Seasonal cycle — a repeating wave rides on the noise.", seasonal),
        ("Flat series — no trend, only point-to-point variation.", flat),
        ("Step change — the level drops abruptly midway through.", drop),
    ]
    return [(cap, dv.bivariate.line_plot_static(x, pd.Series(v, name="Value")))
            for cap, v in scenarios]


def _corr_frame(cols, make):
    rng = _rng(30)
    base = rng.normal(0, 1, 200)
    data = {}
    for name, coef in make.items():
        data[name] = coef * base + rng.normal(0, max(1e-9, (1 - abs(coef)) ** 0.5), 200)
    return pd.DataFrame(data, columns=cols)


def build_correlation_heatmap():
    cols = ["a", "b", "c", "d"]
    scenarios = [
        (
            "Strong blocks — high positive and negative correlations stand out.",
            _corr_frame(cols, {"a": 0.9, "b": 0.85, "c": -0.7, "d": 0.2}),
        ),
        (
            "Weak correlations — no meaningful structure between variables.",
            _corr_frame(cols, {"a": 0.9, "b": 0.1, "c": -0.15, "d": 0.05}),
        ),
        (
            "Mixed signs — positive and negative associations side by side.",
            _corr_frame(cols, {"a": 0.8, "b": 0.75, "c": -0.8, "d": -0.6}),
        ),
        (
            "One dominant pair — a single strong link among independents.",
            _corr_frame(cols, {"a": 0.9, "b": 0.95, "c": 0.05, "d": -0.05}),
        ),
    ]
    return [(cap, dv.bivariate.correlation_heatmap_static(df))
            for cap, df in scenarios]


def build_bubble_plot():
    def make(seed, size_fn, color_fn):
        rng = _rng(40 + seed)
        x = rng.normal(50, 12, 60)
        y = 0.7 * x + rng.normal(0, 8, 60)
        return x, y, size_fn(x, rng), color_fn(x, rng)

    scenarios = [
        (
            "Size tracks x — larger bubbles cluster to the right.",
            make(0, lambda x, r: np.clip(x, 5, None) * 6, lambda x, r: x),
        ),
        (
            "Unrelated size — bubble area carries no signal.",
            make(1, lambda x, r: r.uniform(50, 500, len(x)), lambda x, r: x),
        ),
        (
            "Colour gradient — a fourth variable encoded as colour.",
            make(2, lambda x, r: r.uniform(80, 400, len(x)),
                 lambda x, r: r.uniform(0, 1, len(x))),
        ),
        (
            "Few large players — a handful of bubbles dominate the field.",
            make(3, lambda x, r: np.where(r.random(len(x)) > 0.9, 900, 120),
                 lambda x, r: x),
        ),
    ]
    return [(cap, dv.bivariate.bubble_plot_static(x, y, s, c))
            for cap, (x, y, s, c) in scenarios]


def _dense_scenarios(n=5000):
    r1 = _rng(50)
    corr = (r1.normal(0, 1, n), 0.6 * r1.normal(0, 1, n))
    corr = (corr[0], 0.6 * corr[0] + _rng(51).normal(0, 0.8, n))

    r2 = _rng(52)
    two = (
        np.r_[r2.normal(-2, 0.6, n // 2), _rng(53).normal(2, 0.6, n // 2)],
        np.r_[_rng(54).normal(-2, 0.6, n // 2), _rng(55).normal(2, 0.6, n // 2)],
    )

    uniform = (_rng(56).uniform(-3, 3, n), _rng(57).uniform(-3, 3, n))

    skewed = (_rng(58).gamma(2.0, 1.0, n), _rng(59).gamma(2.0, 1.0, n) * 0.5)
    return [
        ("Correlated mass — density stretches along the diagonal.", corr),
        ("Two clusters — the bins reveal two distinct groups.", two),
        ("Uniform spread — no concentration anywhere in the plane.", uniform),
        ("Skewed density — mass piles up near the origin.", skewed),
    ]


def build_hexbin_plot():
    return [(cap, dv.bivariate.hexbin_plot_static(x, y, gridsize=25))
            for cap, (x, y) in _dense_scenarios()]


def build_regression_plot():
    x1 = _rng(60).uniform(0, 10, 150)
    linear = (x1, 3 + 2 * x1 + _rng(61).normal(0, 3, 150))
    x2 = _rng(62).uniform(0, 10, 150)
    quad = (x2, 2 + 0.6 * x2**2 + _rng(63).normal(0, 4, 150))
    x3 = _rng(64).uniform(0, 10, 150)
    weak = (x3, 10 + 0.2 * x3 + _rng(65).normal(0, 8, 150))
    x4 = _rng(66).uniform(0, 10, 150)
    y4 = 3 + 2 * x4 + _rng(67).normal(0, 2, 150)
    y4[[10, 60, 110]] += np.array([25, -22, 28])
    scenarios = [
        ("Linear fit — the degree-1 line tracks the data well.", linear, 1),
        ("Curved trend — degree 2 follows the acceleration.", quad, 2),
        ("Weak slope — the fit is nearly flat against the noise.", weak, 1),
        ("Outliers pull — a few points bend the fitted line.", (x4, y4), 1),
    ]
    return [(cap, dv.bivariate.regression_plot_static(x, y, degree=d))
            for cap, (x, y), d in scenarios]


def build_density_contour():
    return [(cap, dv.bivariate.density_contour_static(x, y, levels=8))
            for cap, (x, y) in _dense_scenarios(1500)]


def _categorical_scenarios(n=400):
    cats = ["A", "B", "C", "D"]
    r = _rng(70)
    shift_cat = pd.Series(r.choice(cats, n))
    shift = pd.Series(r.normal(100, 15, n)
                      + shift_cat.map({"A": 0, "B": 12, "C": -8, "D": 20}))

    r = _rng(71)
    even_cat = pd.Series(r.choice(cats, n))
    even = pd.Series(r.normal(50, 10, n))

    r = _rng(72)
    dom_cat = pd.Series(r.choice(cats, n, p=[0.7, 0.1, 0.1, 0.1]))
    dom = pd.Series(r.normal(80, 12, n))

    r = _rng(73)
    neg_cat = pd.Series(r.choice(cats, n))
    neg = pd.Series(r.normal(0, 10, n)
                    + neg_cat.map({"A": -15, "B": 5, "C": -5, "D": 10}))
    return [
        ("Shifted levels — group means differ clearly.", shift_cat, shift, "mean"),
        ("No group effect — all categories average the same.", even_cat, even, "mean"),
        ("One dominant group — totals driven by category A.", dom_cat, dom, "sum"),
        ("Mixed signs — some groups average below zero.", neg_cat, neg, "mean"),
    ]


def build_grouped_bar():
    return [(cap, dv.bivariate.grouped_bar_static(c, v, aggfunc=a))
            for cap, c, v, a in _categorical_scenarios()]


def build_box_by_category():
    out = []
    for cap, c, v, _ in _categorical_scenarios():
        out.append((cap, dv.bivariate.box_by_category_static(c, v)))
    return out


def build_violin_by_category():
    n = 450
    r = _rng(80)
    normal_cat = pd.Series(r.choice(["A", "B", "C"], n))
    normal = pd.Series(r.normal(50, 6, n)
                       + normal_cat.map({"A": 0, "B": 8, "C": -6}))

    bimodal_cat = pd.Series(["A"] * n)
    bimodal = pd.Series(np.r_[_rng(81).normal(40, 4, n // 2),
                              _rng(82).normal(60, 4, n - n // 2)])
    r = _rng(83)
    bimodal_cat = pd.Series(r.choice(["A", "B"], n))
    bimodal = pd.Series(np.where(bimodal_cat == "A", bimodal[:n],
                                 r.normal(50, 6, n)))

    skew_cat = pd.Series(_rng(84).choice(["A", "B", "C"], n))
    skew = pd.Series(_rng(85).gamma(2.0, 8, n))

    wide_cat = pd.Series(_rng(86).choice(["A", "B", "C"], n))
    wide = pd.Series(_rng(87).normal(50, 1, n)
                     * wide_cat.map({"A": 3, "B": 8, "C": 15}) + 40)
    scenarios = [
        ("Location shifts — violins sit at different heights.", normal_cat, normal),
        ("Bimodal group — category A shows two humps.", bimodal_cat, bimodal),
        ("Right-skewed — long upper tails in every group.", skew_cat, skew),
        ("Growing spread — violins widen from A to C.", wide_cat, wide),
    ]
    return [(cap, dv.bivariate.violin_by_category_static(c, v))
            for cap, c, v in scenarios]


def build_crosstab_heatmap():
    n = 500
    r = _rng(90)
    indep = (
        pd.Series(r.choice(["North", "South", "East"], n)),
        pd.Series(_rng(91).choice(["Pass", "Rework", "Scrap"], n)),
    )
    r = _rng(92)
    row = pd.Series(r.choice(["North", "South", "East"], n))
    assoc = (
        row,
        pd.Series([_rng(93 + i).choice(["Pass", "Rework", "Scrap"],
                                       p={"North": [0.8, 0.15, 0.05],
                                          "South": [0.4, 0.4, 0.2],
                                          "East": [0.2, 0.3, 0.5]}[v])
                   for i, v in enumerate(row)]),
    )
    norm = (
        pd.Series(_rng(94).choice(["Small", "Medium", "Large"], n, p=[0.6, 0.3, 0.1])),
        pd.Series(_rng(95).choice(["Low", "High"], n)),
    )
    rare = (
        pd.Series(_rng(96).choice(["X", "Y", "Z", "W"], n)),
        pd.Series(_rng(97).choice(["Red", "Green", "Blue"], n, p=[0.8, 0.15, 0.05])),
    )
    scenarios = [
        ("Independent factors — shares spread evenly across cells.", indep, "all"),
        ("Strong association — each region favours a different outcome.",
         assoc, "all"),
        ("Row-normalised — rates comparable despite unequal group sizes.",
         norm, "index"),
        ("Rare combinations — some cells barely occur at all.", rare, "all"),
    ]
    return [
        (cap, dv.bivariate.crosstab_heatmap_static(rc, cc, normalize=nm))
        for cap, (rc, cc), nm in scenarios
    ]


def build_binned_mean_plot():
    n = 2000
    x1 = _rng(100).uniform(0, 10, n)
    linear = (x1, 2 * x1 + _rng(101).normal(0, 5, n))
    x2 = _rng(102).uniform(0, 10, n)
    curve = (x2, 10 * np.sin(x2) + _rng(103).normal(0, 2, n))
    x3 = _rng(104).uniform(0, 10, n)
    flat = (x3, _rng(105).normal(20, 6, n))
    x4 = _rng(106).uniform(0, 10, n)
    hetero = (x4, 2 * x4 + _rng(107).normal(0, 1, n) * (1 + x4))
    scenarios = [
        ("Linear trend — binned means climb steadily.", linear),
        ("Nonlinear wave — binning reveals a sinusoid under the noise.", curve),
        ("No relationship — the binned means stay flat.", flat),
        ("Stable mean, growing noise — trend holds while spread widens.", hetero),
    ]
    return [(cap, dv.bivariate.binned_mean_plot_static(x, y, bins=12))
            for cap, (x, y) in scenarios]


def build_errorbar_plot():
    x = np.arange(1, 9)
    const = (x, 10 + 2 * x + _rng(110).normal(0, 0.5, 8),
             np.full(8, 1.5), None)
    growing = (x, 10 + 2 * x + _rng(111).normal(0, 0.5, 8),
               np.linspace(0.4, 3.5, 8), None)
    both = (x, 5 + 3 * x + _rng(112).normal(0, 0.5, 8),
            _rng(113).uniform(0.5, 1.5, 8), _rng(114).uniform(0.2, 0.6, 8))
    small_n = (x, 12 + 1.5 * x + _rng(115).normal(0, 0.5, 8),
               _rng(116).uniform(2.5, 4.5, 8), None)
    scenarios = [
        ("Constant uncertainty — every estimate is equally precise.", *const),
        ("Growing uncertainty — later measurements are noisier.", *growing),
        ("Two-dimensional error — both x and y carry uncertainty.", *both),
        ("Small samples — wide intervals warn against over-reading.", *small_n),
    ]
    return [(cap, dv.bivariate.errorbar_plot_static(x, y, yerr=ye, xerr=xe))
            for cap, x, y, ye, xe in scenarios]


def build_area_between():
    x = np.linspace(0, 10, 100)
    mid = np.sin(x)
    scenarios = [
        ("Constant band — a fixed tolerance around the nominal curve.",
         x, mid - 0.3, mid + 0.3),
        ("Widening band — uncertainty grows away from the origin.",
         x, 0.2 * x - 0.05 * x**2, 0.2 * x + 0.05 * x**2 + 0.6),
        ("Confidence envelope — interval balloons at the edges.",
         x, 0.1 * x**2 - 0.8 - 0.04 * (x - 5) ** 2,
         0.1 * x**2 + 0.8 + 0.04 * (x - 5) ** 2),
        ("Seasonal envelope — the band breathes with the cycle.",
         x, mid - 0.2 - 0.2 * np.abs(np.sin(x / 2)),
         mid + 0.2 + 0.2 * np.abs(np.sin(x / 2))),
    ]
    return [(cap, dv.bivariate.area_between_static(x, lo, hi))
            for cap, x, lo, hi in scenarios]


def build_step_plot():
    n = 20
    x = np.arange(n)
    r = _rng(120)
    tiers = (x, np.cumsum(r.choice([-1, 0, 1, 2], n, p=[0.2, 0.3, 0.3, 0.2])) + 20)
    setpoint = (x, np.where(x < 7, 65, np.where(x < 14, 72, 68)).astype(float)
                + _rng(121).normal(0, 0.1, n))
    countdown = (x, np.sort(_rng(122).integers(0, 10, n))[::-1].astype(float))
    inventory = (x, np.maximum(0, 50 - np.cumsum(_rng(123).integers(0, 6, n))))
    scenarios = [
        ("Random walk steps — level drifts up in discrete jumps.", tiers, "post"),
        ("Setpoint changes — the target holds between adjustments.",
         setpoint, "post"),
        ("Countdown — a quantity decrements to zero.", countdown, "pre"),
        ("Depletion — inventory falls in discrete withdrawals.", inventory, "mid"),
    ]
    return [(cap, dv.bivariate.step_plot_static(x, y, where=w))
            for cap, (x, y), w in scenarios]


def build_joint_scatter_hist():
    n = 500
    r = _rng(130)
    corr = (r.normal(0, 1, n), 0.6 * r.normal(0, 1, n))
    corr = (corr[0], 0.6 * corr[0] + _rng(131).normal(0, 0.8, n))
    indep = (_rng(132).normal(0, 1, n), _rng(133).normal(0, 1, n))
    skewed = (_rng(134).gamma(2.0, 1.0, n), _rng(135).gamma(3.0, 0.8, n))
    bimodal = (
        _rng(136).normal(0, 1, n),
        np.r_[_rng(137).normal(-2, 0.7, n // 2), _rng(138).normal(2, 0.7, n - n // 2)],
    )
    scenarios = [
        ("Correlated pair — marginals are both bell-shaped.", corr),
        ("Independent normals — no joint or marginal surprises.", indep),
        ("Skewed marginals — both histograms lean right.", skewed),
        ("Bimodal y — the side histogram exposes two groups.", bimodal),
    ]
    return [(cap, dv.bivariate.joint_scatter_hist_static(x, y))
            for cap, (x, y) in scenarios]


def build_bivariate_histogram():
    return [(cap, dv.bivariate.bivariate_histogram_static(x, y, bins=25))
            for cap, (x, y) in _dense_scenarios(3000)]


def build_outlier_scatter():
    n = 300
    r = _rng(140)
    x1 = r.normal(50, 8, n)
    iqr = (np.r_[x1, [95, 15, 100]], np.r_[0.8 * x1 + _rng(141).normal(0, 6, n),
                                           [20, 95, 25]])
    x2 = _rng(142).normal(50, 8, n)
    zsc = (np.r_[x2, [85, 20]], np.r_[0.5 * x2 + _rng(143).normal(0, 6, n), [90, 15]])
    x3 = _rng(144).normal(50, 8, n)
    tight = (x3, 0.8 * x3 + _rng(145).normal(0, 6, n))
    x4 = _rng(146).normal(50, 8, n)
    clean = (x4, 0.8 * x4 + _rng(147).normal(0, 6, n))
    scenarios = [
        ("IQR fences — three points fall outside the whiskers.", iqr, "iqr", 1.5),
        ("Z-score rule — extreme standardised values flagged.", zsc, "zscore", 3.0),
        ("Tight fence — a strict threshold flags borderline points.",
         tight, "iqr", 1.0),
        ("Clean data — nothing exceeds the fences.", clean, "iqr", 1.5),
    ]
    return [(cap, dv.bivariate.outlier_scatter_static(x, y, method=m, threshold=t))
            for cap, (x, y), m, t in scenarios]


def build_residual_relationship():
    n = 200
    x1 = _rng(150).uniform(0, 10, n)
    ok = (x1, 3 + 2 * x1 + _rng(151).normal(0, 2, n))
    x2 = _rng(152).uniform(0, 10, n)
    curved = (x2, 2 * x2 + 0.4 * x2**2 + _rng(153).normal(0, 2, n))
    x3 = _rng(154).uniform(0, 10, n)
    hetero = (x3, 3 + 2 * x3 + _rng(155).normal(0, 1, n) * (0.3 + x3))
    x4 = _rng(156).uniform(0, 10, n)
    y4 = 3 + 2 * x4 + _rng(157).normal(0, 1.5, n)
    y4[n // 2] += 30
    scenarios = [
        ("Adequate fit — residuals scatter randomly around zero.", ok),
        ("Missed curvature — residuals arc because the fit is too simple.", curved),
        ("Heteroscedasticity — the residual spread fans out with x.", hetero),
        ("Influential outlier — one point dominates the residual scale.", (x4, y4)),
    ]
    return [(cap, dv.bivariate.residual_relationship_static(x, y, degree=1))
            for cap, (x, y) in scenarios]


def build_quantile_bin_plot():
    n = 1500
    x1 = _rng(160).uniform(0, 10, n)
    linear = (x1, 5 + 2 * x1 + _rng(161).normal(0, 2, n), "mean")
    x2 = _rng(162).gamma(2.0, 1.5, n)
    logged = (x2, 5 + 3 * np.log1p(x2) + _rng(163).normal(0, 1.5, n), "mean")
    x3 = _rng(164).uniform(0, 10, n)
    flat = (x3, _rng(165).normal(10, 3, n), "mean")
    x4 = _rng(166).uniform(0, 10, n)
    y4 = 2 * x4 + _rng(167).normal(0, 1, n) * (1 + x4)
    y4[:40] += 40
    scenarios = [
        ("Linear rise — each decile of x adds the same amount.", *linear),
        ("Diminishing returns — the curve flattens at high x.", *logged),
        ("No effect — every quantile bin averages the same.", *flat),
        ("Median robustness — the median ignores the injected outliers.",
         x4, y4, "median"),
    ]
    return [(cap, dv.bivariate.quantile_bin_plot_static(x, y, q=10, statistic=s))
            for cap, x, y, s in scenarios]


def build_bland_altman():
    n = 150
    a1 = _rng(170).normal(100, 15, n)
    good = (a1, a1 + _rng(171).normal(0, 3, n))
    a2 = _rng(172).normal(100, 15, n)
    bias = (a2, a2 + 6 + _rng(173).normal(0, 3, n))
    a3 = _rng(174).normal(100, 15, n)
    prop = (a3, a3 * (1.0 + 0.001 * (a3 - 100)) + 0.12 * (a3 - 100)
            + _rng(175).normal(0, 2, n))
    a4 = _rng(176).normal(100, 15, n)
    loose = (a4, a4 + _rng(177).normal(0, 9, n))
    scenarios = [
        ("Good agreement — differences hug zero inside narrow limits.", good),
        ("Constant bias — method B reads six units high throughout.", bias),
        ("Proportional bias — the gap widens as magnitude grows.", prop),
        ("Poor agreement — wide limits of agreement reject interchangeability.",
         loose),
    ]
    return [(cap, dv.bivariate.bland_altman_static(x, y))
            for cap, (x, y) in scenarios]


def build_rank_scatter():
    n = 200
    x1 = _rng(180).uniform(0, 100, n)
    linear = (x1, 0.8 * x1 + _rng(181).normal(0, 8, n))
    x2 = _rng(182).uniform(0, 100, n)
    mono = (x2, np.sqrt(x2) * 10 + _rng(183).normal(0, 5, n))
    x3 = _rng(184).uniform(0, 100, n)
    weak = (x3, 0.1 * x3 + _rng(185).normal(0, 30, n))
    x4 = _rng(186).uniform(0, 10, n)
    ushape = (x4, (x4 - 5) ** 2 + _rng(187).normal(0, 1, n))
    scenarios = [
        ("Monotone linear — ranks fall neatly along the diagonal.", linear),
        ("Monotone but curved — ranking straightens the square-root shape.", mono),
        ("Weak association — ranks scatter broadly.", weak),
        ("U-shaped — ranks reveal the reversal of direction.", ushape),
    ]
    return [(cap, dv.bivariate.rank_scatter_static(x, y))
            for cap, (x, y) in scenarios]


def build_lag_plot():
    n = 300
    noise = pd.Series(_rng(190).normal(0, 1, n))
    ar_noise = _rng(191).normal(0, 1, n)
    ar = pd.Series(np.convolve(ar_noise, [0.8, 0.2], mode="same"))
    t = np.arange(n)
    seasonal = pd.Series(np.sin(t / 3.0) + _rng(192).normal(0, 0.2, n))
    trend = pd.Series(0.05 * t + _rng(193).normal(0, 0.5, n))
    scenarios = [
        ("White noise — no structure, consecutive values independent.", noise, 1),
        ("Autocorrelated — the diagonal band shows lag-1 dependence.", ar, 1),
        ("Seasonal series — lag 12 exposes the repeating cycle.", seasonal, 12),
        ("Trending series — the tight diagonal reflects the drift.", trend, 1),
    ]
    return [(cap, dv.bivariate.lag_plot_static(s, s, lag=k))
            for cap, s, k in scenarios]


def build_conditional_box():
    n = 800
    x1 = _rng(200).uniform(0, 10, n)
    linear = (x1, 3 * x1 + _rng(201).normal(0, 2, n))
    x2 = _rng(202).uniform(0, 10, n)
    curve = (x2, 20 * np.sin(x2 / 1.5) + 30 + _rng(203).normal(0, 2, n))
    x3 = _rng(204).uniform(0, 10, n)
    hetero = (x3, 3 * x3 + _rng(205).normal(0, 1, n) * (1 + 0.4 * x3))
    x4 = _rng(206).uniform(0, 10, n)
    none = (x4, _rng(207).normal(25, 5, n))
    scenarios = [
        ("Linear shift — box medians march upward across bins.", linear),
        ("Nonlinear — medians rise then fall with x.", curve),
        ("Widening spread — boxes grow taller toward high x.", hetero),
        ("No relationship — every bin looks the same.", none),
    ]
    return [(cap, dv.bivariate.conditional_box_static(x, y, bins=8))
            for cap, (x, y) in scenarios]


BUILDERS = {
    "scatter_plot": build_scatter_plot,
    "line_plot": build_line_plot,
    "correlation_heatmap": build_correlation_heatmap,
    "bubble_plot": build_bubble_plot,
    "hexbin_plot": build_hexbin_plot,
    "regression_plot": build_regression_plot,
    "density_contour": build_density_contour,
    "grouped_bar": build_grouped_bar,
    "box_by_category": build_box_by_category,
    "violin_by_category": build_violin_by_category,
    "crosstab_heatmap": build_crosstab_heatmap,
    "binned_mean_plot": build_binned_mean_plot,
    "errorbar_plot": build_errorbar_plot,
    "area_between": build_area_between,
    "step_plot": build_step_plot,
    "joint_scatter_hist": build_joint_scatter_hist,
    "bivariate_histogram": build_bivariate_histogram,
    "outlier_scatter": build_outlier_scatter,
    "residual_relationship": build_residual_relationship,
    "quantile_bin_plot": build_quantile_bin_plot,
    "bland_altman": build_bland_altman,
    "rank_scatter": build_rank_scatter,
    "lag_plot": build_lag_plot,
    "conditional_box": build_conditional_box,
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
                {"src": f"assets/examples/bivariate/{name}", "caption": caption}
            )
        manifest[family] = images
        print(f"{family}: {len(images)} images")

    (OUT_DIR / "manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )
    print(f"manifest: {OUT_DIR / 'manifest.json'}")


if __name__ == "__main__":
    main()
