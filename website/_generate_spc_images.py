"""Render four real SPC example images per chart family for the docs website.

Deterministic synthetic data (``numpy.random.default_rng``) drives every chart so
the output is reproducible. Images and a ``manifest.json`` (family -> image list
with captions) are written to ``website/assets/examples/spc``; the manifest is
consumed by ``_generate_function_docs.mjs`` to attach galleries to SPC pages.
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

OUT_DIR = Path(__file__).resolve().parent / "assets" / "examples" / "spc"
DPI = 110


def _figure_of(result):
    if isinstance(result, plt.Figure):
        return result
    if isinstance(result, (tuple, list)):
        return result[0].figure
    return result.figure


def _rng(seed: int) -> np.random.Generator:
    return np.random.default_rng(seed)


def _individual_scenarios():
    """Four individual-value series: stable, mean shift, drift, outliers."""
    n = 40
    stable = _rng(0).normal(10.0, 0.5, n)

    shift = _rng(1).normal(10.0, 0.5, n)
    shift[n // 2 :] += 1.2

    drift = _rng(2).normal(10.0, 0.4, n) + np.linspace(0.0, 2.2, n)

    spikes = _rng(3).normal(10.0, 0.5, n)
    spikes[[9, 24, 33]] += np.array([2.6, -2.4, 3.0])

    return [
        ("Stable process — points vary randomly inside the control limits.", stable),
        ("Mean shift — the average jumps midway through the run.", shift),
        ("Gradual drift — a slow upward trend walks toward the upper limit.", drift),
        ("Special-cause spikes — isolated points break the control limits.", spikes),
    ]


def build_control():
    return [
        (cap, dv.spc.control_chart_static(pd.Series(v, name="Value")))
        for cap, v in _individual_scenarios()
    ]


def build_moving_range():
    return [
        (cap, dv.spc.moving_range_chart_static(pd.Series(v, name="Value")))
        for cap, v in _individual_scenarios()
    ]


def build_run():
    return [
        (cap, dv.spc.run_chart_static(pd.Series(v, name="Value")))
        for cap, v in _individual_scenarios()
    ]


def build_zone():
    return [
        (cap, dv.spc.zone_chart_static(pd.Series(v, name="Value")))
        for cap, v in _individual_scenarios()
    ]


def build_rule_violation():
    return [
        (cap, dv.spc.rule_violation_chart_static(pd.Series(v, name="Value")))
        for cap, v in _individual_scenarios()
    ]


def build_ewma():
    out = []
    for cap, v in _individual_scenarios():
        out.append((cap, dv.spc.ewma_chart_static(pd.Series(v, name="Value"))))
    return out


def build_cusum():
    out = []
    for cap, v in _individual_scenarios():
        out.append(
            (cap, dv.spc.cusum_chart_static(pd.Series(v, name="Value"), target=10.0))
        )
    return out


def build_spc_dashboard():
    return [
        (cap, dv.spc.spc_dashboard_static(pd.Series(v, name="Value")))
        for cap, v in _individual_scenarios()
    ]


def _subgroups(seed, shift_at=None, shift=0.0, spread=0.5, k=25, n=5):
    rng = _rng(seed)
    data = rng.normal(10.0, spread, (k, n))
    if shift_at is not None:
        data[shift_at:] += shift
    return data


def build_xbar_r():
    scenarios = [
        (
            "Stable subgroups — subgroup means and ranges stay in control.",
            _subgroups(10),
        ),
        (
            "Mean shift — subgroup averages climb after the 15th sample.",
            _subgroups(11, 15, 1.0),
        ),
        (
            "Widening spread — larger within-subgroup variation inflates the range chart.",
            _subgroups(12, spread=0.9),
        ),
        (
            "Out-of-control subgroup — one subgroup mean exceeds the limit.",
            _subgroups(13, 20, 1.6),
        ),
    ]
    return [(cap, dv.spc.xbar_r_chart_static(d)) for cap, d in scenarios]


def build_xbar_s():
    scenarios = [
        (
            "Stable subgroups — mean and standard-deviation charts are in control.",
            _subgroups(14, n=8),
        ),
        (
            "Mean shift — subgroup averages step up partway through.",
            _subgroups(15, 14, 1.0, n=8),
        ),
        (
            "Increased variation — subgroup spread grows and the S chart reacts.",
            _subgroups(16, spread=1.0, n=8),
        ),
        (
            "Special cause — a single subgroup drives an out-of-control signal.",
            _subgroups(17, 18, 1.8, n=8),
        ),
    ]
    return [(cap, dv.spc.xbar_s_chart_static(d)) for cap, d in scenarios]


def build_x_range():
    rng = _rng(20)
    stable = pd.Series(rng.normal(10.0, 0.5, 150), name="Value")
    shift = pd.Series(_rng(21).normal(10.0, 0.5, 150), name="Value")
    shift[75:] += 1.0
    drift = pd.Series(
        _rng(22).normal(10.0, 0.4, 150) + np.linspace(0, 2, 150), name="Value"
    )
    wide = pd.Series(_rng(23).normal(10.0, 0.9, 150), name="Value")
    scenarios = [
        ("Stable process — 30 subgroups of five stay in control.", stable),
        ("Mean shift — the process centre moves up after subgroup 15.", shift),
        ("Drift — a steady trend pushes subgroup means upward.", drift),
        ("High variation — a wider spread stresses the range portion.", wide),
    ]
    return [
        (cap, dv.spc.x_range_chart_static(v, subgroup_size=5)) for cap, v in scenarios
    ]


def build_p_chart():
    n = 20
    sizes = pd.Series([100] * n)
    stable = pd.Series(_rng(30).binomial(100, 0.04, n))
    shift = pd.Series(
        np.r_[
            _rng(31).binomial(100, 0.03, n // 2), _rng(32).binomial(100, 0.09, n // 2)
        ]
    )
    varying_sizes = pd.Series(_rng(33).integers(80, 140, n))
    varying = pd.Series(
        [_rng(34 + i).binomial(int(s), 0.05) for i, s in enumerate(varying_sizes)]
    )
    spike = pd.Series(_rng(35).binomial(100, 0.04, n))
    spike[[7, 15]] = [18, 20]
    scenarios = [
        ("Stable proportion defective — points scatter around p-bar.", stable, sizes),
        (
            "Process deterioration — the defect rate rises in the second half.",
            shift,
            sizes,
        ),
        (
            "Varying sample sizes — control limits widen for smaller samples.",
            varying,
            varying_sizes,
        ),
        ("Out-of-control points — two samples exceed the upper limit.", spike, sizes),
    ]
    return [(cap, dv.spc.p_chart_static(d, s)) for cap, d, s in scenarios]


def build_np_chart():
    n = 20
    stable = pd.Series(_rng(40).binomial(100, 0.04, n))
    shift = pd.Series(
        np.r_[
            _rng(41).binomial(100, 0.03, n // 2), _rng(42).binomial(100, 0.09, n // 2)
        ]
    )
    drift = pd.Series(
        np.clip(
            (_rng(43).binomial(100, 0.04, n) + np.arange(n) * 0.3).astype(int), 0, 100
        )
    )
    spike = pd.Series(_rng(44).binomial(100, 0.04, n))
    spike[[6, 14]] = [17, 19]
    scenarios = [
        ("Stable defective count — constant sample size of 100.", stable),
        ("Upward shift — nonconforming units increase midway.", shift),
        ("Slow drift — the defective count trends upward over time.", drift),
        ("Special cause — isolated high counts break the limit.", spike),
    ]
    return [(cap, dv.spc.np_chart_static(d, 100)) for cap, d in scenarios]


def build_c_chart():
    n = 25
    stable = pd.Series(_rng(50).poisson(4.0, n))
    shift = pd.Series(
        np.r_[_rng(51).poisson(3.0, n // 2), _rng(52).poisson(7.0, n - n // 2)]
    )
    drift = pd.Series((_rng(53).poisson(4.0, n) + np.arange(n) * 0.2).astype(int))
    spike = pd.Series(_rng(54).poisson(4.0, n))
    spike[[8, 18]] = [14, 15]
    scenarios = [
        ("Stable defect count — a constant inspection area.", stable),
        ("Increased defects — the average count rises partway through.", shift),
        ("Drifting count — defects trend upward over time.", drift),
        ("Special cause — two inspections show excessive defects.", spike),
    ]
    return [(cap, dv.spc.c_chart_static(d)) for cap, d in scenarios]


def build_u_chart():
    n = 20
    units = pd.Series(_rng(60).integers(40, 60, n))
    stable = pd.Series([_rng(61 + i).poisson(0.1 * u) for i, u in enumerate(units)])
    shift_u = pd.Series(
        [
            _rng(70 + i).poisson((0.08 if i < n // 2 else 0.18) * u)
            for i, u in enumerate(units)
        ]
    )
    equal_units = pd.Series([50] * n)
    equal = pd.Series(_rng(80).poisson(5.0, n))
    spike = pd.Series([_rng(90 + i).poisson(0.1 * u) for i, u in enumerate(units)])
    spike[[5, 13]] = [16, 18]
    scenarios = [
        (
            "Stable defects per unit — inspection sizes vary sample to sample.",
            stable,
            units,
        ),
        ("Rate increase — defects per unit climb in the second half.", shift_u, units),
        ("Equal inspection sizes — straight control limits.", equal, equal_units),
        ("Special cause — two samples exceed the upper limit.", spike, units),
    ]
    return [(cap, dv.spc.u_chart_static(d, u)) for cap, d, u in scenarios]


def build_pareto():
    cats = ["Scratch", "Dent", "Misalign", "Color", "Crack", "Other"]
    scenarios = [
        (
            "Classic 80/20 — a few categories dominate the defects.",
            [140, 90, 40, 20, 8, 4],
        ),
        (
            "Single dominant cause — one category drives most defects.",
            [220, 30, 20, 12, 8, 5],
        ),
        ("Even spread — no single vital few stands out.", [60, 55, 50, 45, 40, 35]),
        (
            "Long tail — many small contributors after the leaders.",
            [120, 70, 25, 22, 18, 15],
        ),
    ]
    return [(cap, dv.spc.pareto_chart_static(cats, c)) for cap, c in scenarios]


def build_capability():
    lsl, usl = 8.5, 11.5
    scenarios = [
        (
            "Capable and centred — the spread fits comfortably in spec.",
            _rng(100).normal(10.0, 0.4, 300),
            lsl,
            usl,
        ),
        (
            "Off-centre — the mean drifts toward the upper spec limit.",
            _rng(101).normal(10.8, 0.4, 300),
            lsl,
            usl,
        ),
        (
            "Too much spread — the distribution overflows both limits.",
            _rng(102).normal(10.0, 0.9, 300),
            lsl,
            usl,
        ),
        (
            "Skewed process — a non-normal tail crosses the lower limit.",
            _rng(103).gamma(2.0, 0.6, 300) + 7.5,
            lsl,
            usl,
        ),
    ]
    return [
        (
            cap,
            dv.spc.capability_histogram_static(
                pd.Series(v, name="Value"), lsl=lo, usl=hi
            ),
        )
        for cap, v, lo, hi in scenarios
    ]


def build_process_distribution():
    scenarios = [
        (
            "Normal process — a symmetric, bell-shaped distribution.",
            _rng(110).normal(10.0, 0.6, 400),
        ),
        (
            "Right-skewed — a long upper tail from occasional large values.",
            _rng(111).gamma(2.0, 0.7, 400) + 7.0,
        ),
        (
            "Bimodal — two overlapping modes suggest mixed streams.",
            np.r_[_rng(112).normal(9.0, 0.4, 200), _rng(113).normal(11.5, 0.4, 200)],
        ),
        (
            "Heavy-tailed — extra dispersion from rare extreme values.",
            _rng(114).standard_t(3, 400) * 0.8 + 10.0,
        ),
    ]
    return [
        (cap, dv.spc.process_distribution_static(pd.Series(v, name="Value")))
        for cap, v in scenarios
    ]


def build_hotelling():
    def frame(seed, shift_at=None, shift=(0.0, 0.0), corr=0.0, outlier=None):
        rng = _rng(seed)
        n = 40
        x1 = rng.normal(10.0, 0.5, n)
        x2 = corr * (x1 - 10.0) + rng.normal(20.0, 0.5, n)
        if shift_at is not None:
            x1[shift_at:] += shift[0]
            x2[shift_at:] += shift[1]
        if outlier is not None:
            x1[outlier] += 2.5
            x2[outlier] -= 2.2
        return pd.DataFrame({"x1": x1, "x2": x2})

    scenarios = [
        (
            "In control — two correlated variables stay within the T² limit.",
            frame(120, corr=0.6),
        ),
        (
            "Joint shift — both variables move together after sample 20.",
            frame(121, 20, (1.0, 1.0), corr=0.6),
        ),
        (
            "Counter-move — a single variable breaks the usual correlation.",
            frame(122, corr=0.6, outlier=15),
        ),
        (
            "Multivariate outlier — one point is far in the T² metric.",
            frame(123, corr=0.6, outlier=30),
        ),
    ]
    return [(cap, dv.spc.hotelling_t2_chart_static(d)) for cap, d in scenarios]


BUILDERS = {
    "control_chart": build_control,
    "x_range_chart": build_x_range,
    "moving_range_chart": build_moving_range,
    "xbar_r_chart": build_xbar_r,
    "xbar_s_chart": build_xbar_s,
    "ewma_chart": build_ewma,
    "cusum_chart": build_cusum,
    "p_chart": build_p_chart,
    "np_chart": build_np_chart,
    "c_chart": build_c_chart,
    "u_chart": build_u_chart,
    "capability_histogram": build_capability,
    "run_chart": build_run,
    "rule_violation_chart": build_rule_violation,
    "pareto_chart": build_pareto,
    "process_distribution": build_process_distribution,
    "zone_chart": build_zone,
    "hotelling_t2_chart": build_hotelling,
    "spc_dashboard": build_spc_dashboard,
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
            images.append({"src": f"assets/examples/spc/{name}", "caption": caption})
        manifest[family] = images
        print(f"{family}: {len(images)} images")

    (OUT_DIR / "manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )
    print(f"manifest: {OUT_DIR / 'manifest.json'}")


if __name__ == "__main__":
    main()
