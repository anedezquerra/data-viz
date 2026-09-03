"""Render four real regression example images per chart family.

Deterministic synthetic data (``numpy.random.default_rng``) drives every chart
so the output is reproducible. Images and a ``manifest.json`` (family -> image
list with captions) are written to ``website/assets/examples/regression``; the
manifest is consumed by ``_generate_function_docs.mjs`` to attach galleries to
regression pages.
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import dataviz as dv  # noqa: E402

OUT_DIR = Path(__file__).resolve().parent / "assets" / "examples" / "regression"
DPI = 110


def _figure_of(result):
    if isinstance(result, plt.Figure):
        return result
    if isinstance(result, (tuple, list)):
        return result[0].figure
    return result.figure


def _rng(seed: int) -> np.random.Generator:
    return np.random.default_rng(seed)


def _residual_scenarios():
    n = 120
    y_true = _rng(0).uniform(10.0, 50.0, n)
    homo = y_true + _rng(1).normal(0.0, 3.0, n)
    hetero = y_true + _rng(2).normal(0.0, 1.0, n) * (y_true - 10.0) / 8.0
    curved = y_true + 12.0 * np.sin((y_true - 10.0) / 40.0 * np.pi) + _rng(3).normal(
        0.0, 1.5, n
    )
    outliers = y_true + _rng(4).normal(0.0, 2.5, n)
    outliers[[15, 60, 95]] += np.array([18.0, -20.0, 16.0])
    return [
        (
            "Well specified — residuals form a shapeless cloud around zero.",
            y_true,
            homo,
        ),
        (
            "Heteroscedastic — the residual spread fans out with the fit.",
            y_true,
            hetero,
        ),
        (
            "Nonlinear misfit — a curved pattern the model failed to capture.",
            y_true,
            curved,
        ),
        (
            "Outliers — a few extreme residuals stand apart from the rest.",
            y_true,
            outliers,
        ),
    ]


def build_residual():
    return [
        (
            cap,
            dv.regression.residual_plot_static(
                yt, yp, title=cap.split(" — ")[0]
            ),
        )
        for cap, yt, yp in _residual_scenarios()
    ]


def _prediction_scenarios():
    n = 120
    y_true = _rng(10).uniform(10.0, 50.0, n)
    accurate = y_true + _rng(11).normal(0.0, 2.5, n)
    biased = 0.85 * y_true + 3.0 + _rng(12).normal(0.0, 2.0, n)
    noisy = y_true + _rng(13).normal(0.0, 7.0, n)
    saturating = 45.0 - 45.0 * np.exp(-y_true / 15.0) + _rng(14).normal(0.0, 1.5, n)
    return [
        (
            "Accurate model — points hug the 45-degree identity line.",
            y_true,
            accurate,
        ),
        (
            "Biased model — predictions drift off the line at high values.",
            y_true,
            biased,
        ),
        (
            "Noisy model — wide scatter around the identity line.",
            y_true,
            noisy,
        ),
        (
            "Saturating model — predictions plateau for large targets.",
            y_true,
            saturating,
        ),
    ]


def build_prediction():
    return [
        (
            cap,
            dv.regression.prediction_plot_static(
                yt, yp, title=cap.split(" — ")[0]
            ),
        )
        for cap, yt, yp in _prediction_scenarios()
    ]


def _learning_curve_scenarios():
    sizes = np.linspace(0.1, 1.0, 8)
    good_train = np.array([0.96, 0.93, 0.91, 0.90, 0.89, 0.88, 0.88, 0.87])
    good_val = np.array([0.74, 0.79, 0.82, 0.84, 0.85, 0.86, 0.86, 0.86])
    over_train = np.array([0.99, 0.99, 0.98, 0.98, 0.98, 0.97, 0.97, 0.97])
    over_val = np.array([0.65, 0.68, 0.70, 0.71, 0.72, 0.72, 0.73, 0.73])
    under_train = np.array([0.68, 0.67, 0.66, 0.66, 0.65, 0.65, 0.65, 0.65])
    under_val = np.array([0.62, 0.63, 0.64, 0.64, 0.64, 0.64, 0.64, 0.64])
    more_train = np.array([0.97, 0.94, 0.92, 0.90, 0.89, 0.88, 0.87, 0.86])
    more_val = np.array([0.68, 0.73, 0.76, 0.79, 0.81, 0.82, 0.83, 0.84])
    return [
        (
            "Good fit — training and validation scores converge.",
            good_train,
            good_val,
        ),
        (
            "Overfit — a wide, persistent gap between the two curves.",
            over_train,
            over_val,
        ),
        (
            "Underfit — both curves plateau at a low score.",
            under_train,
            under_val,
        ),
        (
            "More data helps — the validation score is still climbing.",
            more_train,
            more_val,
        ),
    ]


def build_learning_curve():
    return [
        (
            cap,
            dv.regression.learning_curve_static(
                np.linspace(0.1, 1.0, 8), tr, va, title=cap.split(" — ")[0]
            ),
        )
        for cap, tr, va in _learning_curve_scenarios()
    ]


BUILDERS = {
    "residual_plot": build_residual,
    "prediction_plot": build_prediction,
    "learning_curve": build_learning_curve,
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
                    "src": f"assets/examples/regression/{name}",
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
