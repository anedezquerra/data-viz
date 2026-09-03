"""Render four real multivariate example images per chart family.

Deterministic synthetic data (``numpy.random.default_rng``) drives every chart so
the output is reproducible. Images and a ``manifest.json`` (family -> image list
with captions) are written to ``website/assets/examples/multivariate``; the
manifest is consumed by ``_generate_function_docs.mjs`` to attach galleries to
multivariate pages.
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

OUT_DIR = Path(__file__).resolve().parent / "assets" / "examples" / "multivariate"
DPI = 110


def _figure_of(result):
    if isinstance(result, plt.Figure):
        return result
    if isinstance(result, (tuple, list)):
        return result[0].figure
    return result.figure


def _rng(seed: int) -> np.random.Generator:
    return np.random.default_rng(seed)


def build_pairplot():
    n = 200

    rng = _rng(0)
    x1 = rng.normal(0.0, 1.0, n)
    correlated = pd.DataFrame(
        {
            "length": x1,
            "weight": 0.8 * x1 + rng.normal(0.0, 0.4, n),
            "age": rng.normal(5.0, 1.5, n),
        }
    )

    rng = _rng(1)
    uncorrelated = pd.DataFrame(
        {
            "length": rng.normal(0.0, 1.0, n),
            "weight": rng.normal(10.0, 2.0, n),
            "age": rng.normal(5.0, 1.5, n),
        }
    )

    rng = _rng(2)
    half = n // 2
    clustered = pd.DataFrame(
        {
            "length": np.r_[rng.normal(-1.5, 0.4, half), rng.normal(1.5, 0.4, half)],
            "weight": np.r_[rng.normal(8.0, 0.5, half), rng.normal(12.0, 0.5, half)],
            "age": rng.normal(5.0, 1.5, n),
        }
    )

    rng = _rng(3)
    x = rng.uniform(-3.0, 3.0, n)
    nonlinear = pd.DataFrame(
        {
            "x": x,
            "y": x**2 + rng.normal(0.0, 0.8, n),
            "z": rng.normal(0.0, 1.0, n),
        }
    )

    scenarios = [
        (
            "Correlated pair — length and weight rise together.",
            correlated,
        ),
        (
            "Uncorrelated features — scatter clouds show no structure.",
            uncorrelated,
        ),
        (
            "Two clusters — distinct groups separate in every panel.",
            clustered,
        ),
        (
            "Non-linear link — a curved relationship appears in one panel.",
            nonlinear,
        ),
    ]
    return [
        (cap, dv.multivariate.pairplot_static(df)) for cap, df in scenarios
    ]


def _corr_frame(seed, spec, n=300):
    """Build a dataframe from (base_index, coef, noise) column specs."""
    rng = _rng(seed)
    base = [rng.normal(0.0, 1.0, n) for _ in range(3)]
    data = {}
    for name, (bi, coef, noise) in spec.items():
        data[name] = coef * base[bi] + rng.normal(0.0, noise, n)
    return pd.DataFrame(data)


def build_heatmap():
    strong = _corr_frame(
        5,
        {
            "length": (0, 1.0, 0.1),
            "weight": (0, 0.9, 0.3),
            "age": (1, 1.0, 0.1),
            "price": (0, -0.6, 0.8),
        },
    ).corr()
    weak = _corr_frame(
        6,
        {
            "a": (0, 1.0, 1.2),
            "b": (1, 1.0, 1.2),
            "c": (2, 1.0, 1.2),
            "d": (0, 0.15, 1.2),
        },
    ).corr()
    anticorr = _corr_frame(
        7,
        {
            "load": (0, 1.0, 0.2),
            "speed": (0, -0.85, 0.4),
            "temp": (0, 0.8, 0.4),
            "wear": (0, 0.7, 0.5),
        },
    ).corr()
    blocks = _corr_frame(
        8,
        {
            "x1": (0, 1.0, 0.2),
            "x2": (0, 0.9, 0.3),
            "y1": (1, 1.0, 0.2),
            "y2": (1, 0.9, 0.3),
        },
    ).corr()
    scenarios = [
        (
            "Mixed correlations — strong positive and negative links.",
            strong,
        ),
        (
            "No structure — near-zero correlations across the board.",
            weak,
        ),
        (
            "Trade-off — one driver pushes variables in opposite directions.",
            anticorr,
        ),
        (
            "Two blocks — variable pairs cluster into independent groups.",
            blocks,
        ),
    ]
    return [
        (cap, dv.multivariate.heatmap_static(corr)) for cap, corr in scenarios
    ]


def build_parallel_coordinates():
    n = 60
    cols = ["speed", "power", "weight", "range"]

    rng = _rng(9)
    uniform = pd.DataFrame(
        {
            "speed": rng.normal(50.0, 8.0, n),
            "power": rng.normal(120.0, 15.0, n),
            "weight": rng.normal(900.0, 80.0, n),
            "range": rng.normal(300.0, 40.0, n),
        }
    )

    rng = _rng(10)
    third = n // 3
    clustered = pd.DataFrame(
        {
            "speed": np.r_[
                rng.normal(35.0, 3.0, third),
                rng.normal(55.0, 3.0, third),
                rng.normal(75.0, 3.0, n - 2 * third),
            ],
            "power": np.r_[
                rng.normal(90.0, 5.0, third),
                rng.normal(120.0, 5.0, third),
                rng.normal(160.0, 5.0, n - 2 * third),
            ],
            "weight": np.r_[
                rng.normal(1100.0, 40.0, third),
                rng.normal(900.0, 40.0, third),
                rng.normal(700.0, 40.0, n - 2 * third),
            ],
            "range": np.r_[
                rng.normal(220.0, 15.0, third),
                rng.normal(300.0, 15.0, third),
                rng.normal(380.0, 15.0, n - 2 * third),
            ],
        }
    )

    outlier = uniform.copy()
    outlier.loc[5, "speed"] = 95.0
    outlier.loc[5, "power"] = 40.0
    outlier.loc[5, "weight"] = 400.0
    outlier.loc[5, "range"] = 500.0

    rng = _rng(11)
    t = np.linspace(0.0, 1.0, n)
    graduated = pd.DataFrame(
        {
            "speed": 30.0 + 50.0 * t + rng.normal(0.0, 3.0, n),
            "power": 80.0 + 90.0 * t + rng.normal(0.0, 6.0, n),
            "weight": 1100.0 - 400.0 * t + rng.normal(0.0, 40.0, n),
            "range": 200.0 + 200.0 * t + rng.normal(0.0, 20.0, n),
        }
    )

    scenarios = [
        (
            "Uniform profiles — records overlap with no clear grouping.",
            uniform,
        ),
        (
            "Three profiles — lines bundle into distinct tiers.",
            clustered,
        ),
        (
            "Outlier — one record breaks away from the pack.",
            outlier,
        ),
        (
            "Graduated order — profiles form a smooth low-to-high ladder.",
            graduated,
        ),
    ]
    return [
        (cap, dv.multivariate.parallel_coordinates_static(df[cols]))
        for cap, df in scenarios
    ]


BUILDERS = {
    "pairplot": build_pairplot,
    "heatmap": build_heatmap,
    "parallel_coordinates": build_parallel_coordinates,
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
                {
                    "src": f"assets/examples/multivariate/{name}",
                    "caption": caption,
                }
            )
        manifest[family] = images
        print(f"{family}: {len(images)} images")

    (OUT_DIR / "manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )
    print(f"manifest: {OUT_DIR / 'manifest.json'}")


if __name__ == "__main__":
    main()
