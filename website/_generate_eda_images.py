"""Render four real EDA example images per chart family for the docs website.

Deterministic synthetic data (``numpy.random.default_rng``) drives every chart so
the output is reproducible. Images and a ``manifest.json`` (family -> image list
with captions) are written to ``website/assets/examples/eda``; the manifest is
consumed by ``_generate_function_docs.mjs`` to attach galleries to EDA pages.
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

OUT_DIR = Path(__file__).resolve().parent / "assets" / "examples" / "eda"
DPI = 110


def _figure_of(result):
    if isinstance(result, plt.Figure):
        return result
    if isinstance(result, (tuple, list)):
        return result[0].figure
    return result.figure


def _rng(seed: int) -> np.random.Generator:
    return np.random.default_rng(seed)


def _numeric_frame(seed, n=300):
    rng = _rng(seed)
    return pd.DataFrame(
        {
            "age": rng.normal(40.0, 12.0, n),
            "income": rng.normal(60000.0, 15000.0, n),
            "score": rng.normal(0.5, 0.2, n),
            "visits": rng.poisson(4.0, n),
        }
    )


def build_missing_data():
    n = 300

    complete = _numeric_frame(20, n)

    rng = _rng(21)
    scattered = _numeric_frame(21, n)
    for col, count in [("age", 20), ("income", 15), ("score", 25), ("visits", 10)]:
        scattered.loc[rng.choice(n, count, replace=False), col] = np.nan

    rng = _rng(22)
    structured = _numeric_frame(22, n)
    rows = rng.choice(n, 120, replace=False)
    structured.loc[rows, ["income", "score"]] = np.nan

    rng = _rng(23)
    heavy = _numeric_frame(23, n)
    heavy.loc[rng.choice(n, 210, replace=False), "income"] = np.nan
    heavy.loc[rng.choice(n, 60, replace=False), "age"] = np.nan

    scenarios = [
        (
            "Complete data — no missing values in any column.",
            complete,
        ),
        (
            "Scattered missingness — small random gaps across all columns.",
            scattered,
        ),
        (
            "Structured missingness — income and score are absent together.",
            structured,
        ),
        (
            "One heavy column — income is missing for most records.",
            heavy,
        ),
    ]
    return [(cap, dv.eda.missing_data_plot_static(df)) for cap, df in scenarios]


def build_distribution_summary():
    n = 400

    varied = pd.DataFrame(
        {
            "age": _rng(30).normal(40.0, 12.0, n),
            "income": _rng(31).gamma(2.0, 20000.0, n),
            "visits": _rng(32).poisson(4.0, n),
        }
    )

    rng = _rng(33)
    bimodal = pd.DataFrame(
        {
            "height": np.r_[rng.normal(160.0, 6.0, n // 2), rng.normal(178.0, 7.0, n - n // 2)],
            "weight": rng.normal(75.0, 12.0, n),
        }
    )

    rng = _rng(34)
    heavy_tailed = pd.DataFrame(
        {
            "returns": rng.standard_t(3, n) * 0.02,
            "volume": rng.lognormal(10.0, 0.8, n),
        }
    )

    rng = _rng(35)
    scaled = pd.DataFrame(
        {
            "temperature": rng.normal(22.0, 2.0, n),
            "pressure": rng.normal(1013.0, 8.0, n),
            "humidity": rng.uniform(20.0, 90.0, n),
        }
    )

    scenarios = [
        (
            "Mixed shapes — normal, skewed, and count columns side by side.",
            varied,
        ),
        (
            "Bimodal column — two overlapping groups in one variable.",
            bimodal,
        ),
        (
            "Heavy tails — extreme values stretch the axes.",
            heavy_tailed,
        ),
        (
            "Different scales — each column lives on its own range.",
            scaled,
        ),
    ]
    return [
        (cap, dv.eda.distribution_summary_static(df)) for cap, df in scenarios
    ]


def build_class_distribution():
    n = 500
    scenarios = [
        (
            "Balanced classes — each category appears about equally often.",
            pd.Series(
                _rng(40).choice(["a", "b", "c"], size=n, p=[1 / 3, 1 / 3, 1 / 3]),
                name="outcome",
            ),
        ),
        (
            "Imbalanced classes — one category dominates the sample.",
            pd.Series(
                _rng(41).choice(
                    ["approved", "review", "rejected"], size=n, p=[0.7, 0.2, 0.1]
                ),
                name="outcome",
            ),
        ),
        (
            "Rare class — the minority category is under 2% of records.",
            pd.Series(
                _rng(42).choice(["normal", "fraud"], size=n, p=[0.985, 0.015]),
                name="outcome",
            ),
        ),
        (
            "Many classes — a long tail of small categories.",
            pd.Series(
                _rng(43).choice(
                    ["alpha", "beta", "gamma", "delta", "epsilon", "zeta"],
                    size=n,
                    p=[0.4, 0.25, 0.15, 0.1, 0.07, 0.03],
                ),
                name="outcome",
            ),
        ),
    ]
    return [
        (cap, dv.eda.class_distribution_static(series)) for cap, series in scenarios
    ]


BUILDERS = {
    "missing_data_plot": build_missing_data,
    "distribution_summary": build_distribution_summary,
    "class_distribution": build_class_distribution,
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
            images.append({"src": f"assets/examples/eda/{name}", "caption": caption})
        manifest[family] = images
        print(f"{family}: {len(images)} images")

    (OUT_DIR / "manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )
    print(f"manifest: {OUT_DIR / 'manifest.json'}")


if __name__ == "__main__":
    main()
