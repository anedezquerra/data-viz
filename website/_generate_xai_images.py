"""Render four real XAI example images per chart family for the docs website.

Deterministic synthetic data (``numpy.random.default_rng``) drives every chart so
the output is reproducible. Images and a ``manifest.json`` (family -> image list
with captions) are written to ``website/assets/examples/xai``; the manifest is
consumed by ``_generate_function_docs.mjs`` to attach galleries to XAI pages.
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

OUT_DIR = Path(__file__).resolve().parent / "assets" / "examples" / "xai"
DPI = 110

FEATURES = ["Age", "Income", "Tenure", "Region", "Device", "Channel"]


def _figure_of(result):
    if isinstance(result, plt.Figure):
        return result
    if isinstance(result, (tuple, list)):
        return result[0].figure
    return result.figure


def _rng(seed: int) -> np.random.Generator:
    return np.random.default_rng(seed)


def build_feature_importance():
    scenarios = [
        (
            "Dominant driver — one feature carries most of the signal.",
            [0.46, 0.14, 0.11, 0.08, 0.06, 0.04],
        ),
        (
            "Even spread — contributions are shared across features.",
            [0.19, 0.18, 0.17, 0.16, 0.15, 0.14],
        ),
        (
            "Long tail — two leaders ahead of many weak contributors.",
            [0.32, 0.25, 0.09, 0.07, 0.05, 0.03],
        ),
        (
            "Weak model — all importances hover near zero.",
            [0.03, 0.02, 0.02, 0.01, 0.01, 0.01],
        ),
    ]
    return [
        (
            cap,
            dv.xai.feature_importance_static(pd.Series(vals, index=FEATURES)),
        )
        for cap, vals in scenarios
    ]


def build_shap_plot():
    n = 200
    dominant = np.column_stack(
        [
            _rng(0).normal(0.0, 1.0, n),
            _rng(1).normal(0.0, 0.3, n),
            _rng(2).normal(0.0, 0.15, n),
            _rng(3).normal(0.0, 0.05, n),
        ]
    )
    opposing = np.column_stack(
        [
            _rng(4).normal(0.8, 0.3, n),
            _rng(5).normal(-0.8, 0.3, n),
            _rng(6).normal(0.0, 0.1, n),
            _rng(7).normal(0.0, 0.05, n),
        ]
    )
    uniform = np.column_stack(
        [_rng(8 + i).normal(0.0, 0.25, n) for i in range(4)]
    )
    mixed = np.column_stack(
        [
            _rng(12).normal(0.0, 0.7, n),
            _rng(13).normal(0.0, 0.6, n),
            _rng(14).normal(0.0, 0.5, n),
            _rng(15).normal(0.0, 0.4, n),
        ]
    )
    scenarios = [
        (
            "Single driver — one feature dominates the average impact.",
            dominant,
        ),
        (
            "Opposing effects — two features push predictions in opposite directions.",
            opposing,
        ),
        (
            "Uniform impact — all features contribute small, similar effects.",
            uniform,
        ),
        (
            "Graded impacts — contributions taper smoothly across features.",
            mixed,
        ),
    ]
    names = ["Age", "Income", "Tenure", "Region"]
    return [
        (cap, dv.xai.shap_plot_static(vals, names)) for cap, vals in scenarios
    ]


def build_partial_dependence():
    grid = np.linspace(0.0, 10.0, 30)
    scenarios = [
        (
            "Linear effect — the prediction rises steadily with the feature.",
            grid,
            1.0 + 0.5 * grid,
        ),
        (
            "Saturating effect — gains flatten out at higher values.",
            grid,
            2.0 + 1.5 * np.log1p(grid),
        ),
        (
            "Non-monotonic effect — the response peaks in the mid-range.",
            grid,
            3.0 - 0.15 * (grid - 5.0) ** 2,
        ),
        (
            "No effect — the feature barely changes the prediction.",
            grid,
            2.5 + _rng(20).normal(0.0, 0.03, grid.size),
        ),
    ]
    return [
        (
            cap,
            dv.xai.partial_dependence_static(g, p, feature_name="Income"),
        )
        for cap, g, p in scenarios
    ]


BUILDERS = {
    "feature_importance": build_feature_importance,
    "shap_plot": build_shap_plot,
    "partial_dependence": build_partial_dependence,
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
            images.append({"src": f"assets/examples/xai/{name}", "caption": caption})
        manifest[family] = images
        print(f"{family}: {len(images)} images")

    (OUT_DIR / "manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )
    print(f"manifest: {OUT_DIR / 'manifest.json'}")


if __name__ == "__main__":
    main()
