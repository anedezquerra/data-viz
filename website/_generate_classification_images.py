"""Render four real classification example images per chart family.

Deterministic synthetic data (``numpy.random.default_rng``) drives every chart
so the output is reproducible. Images and a ``manifest.json`` (family -> image
list with captions) are written to ``website/assets/examples/classification``;
the manifest is consumed by ``_generate_function_docs.mjs`` to attach galleries
to classification pages.
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import dataviz as dv  # noqa: E402

OUT_DIR = Path(__file__).resolve().parent / "assets" / "examples" / "classification"
DPI = 110

LABELS_3 = ["Setosa", "Versicolor", "Virginica"]


def _figure_of(result):
    if isinstance(result, plt.Figure):
        return result
    if isinstance(result, (tuple, list)):
        return result[0].figure
    return result.figure


def _rng(seed: int) -> np.random.Generator:
    return np.random.default_rng(seed)


def _cm_scenarios():
    strong = np.array([[48, 2, 0], [3, 44, 3], [0, 4, 46]])
    weak = np.array([[30, 12, 8], [10, 28, 12], [8, 14, 28]])
    imbalanced = np.array([[185, 10, 5], [25, 18, 7], [12, 8, 6]])
    confused = np.array([[46, 3, 1], [2, 25, 23], [1, 20, 29]])
    return [
        (
            "Strong classifier — nearly all predictions land on the diagonal.",
            strong,
        ),
        (
            "Weak classifier — predictions scatter well off the diagonal.",
            weak,
        ),
        (
            "Imbalanced classes — the majority class dominates the counts.",
            imbalanced,
        ),
        (
            "Systematic confusion — Versicolor and Virginica blur together.",
            confused,
        ),
    ]


def build_confusion_matrix():
    return [
        (
            cap,
            dv.classification.confusion_matrix_plot_static(
                cm, labels=LABELS_3, title=cap.split(" — ")[0]
            ),
        )
        for cap, cm in _cm_scenarios()
    ]


def _roc_scenarios():
    fpr = np.linspace(0.0, 1.0, 50)
    curves = [
        (
            "Excellent separation — the curve hugs the top-left corner.",
            fpr**0.12,
        ),
        (
            "Good separation — solid lift over the chance diagonal.",
            fpr**0.35,
        ),
        (
            "Weak separation — only a modest bow above chance.",
            fpr**0.7,
        ),
        (
            "Near chance — the curve collapses onto the diagonal.",
            fpr + 0.04 * np.sin(3 * np.pi * fpr) * fpr * (1 - fpr) * 8,
        ),
    ]
    out = []
    for cap, tpr in curves:
        tpr = np.clip(np.maximum.accumulate(tpr), 0.0, 1.0)
        auc = float(np.trapezoid(tpr, fpr))
        out.append((cap, tpr, auc))
    return fpr, out


def build_roc():
    fpr, scenarios = _roc_scenarios()
    return [
        (
            cap,
            dv.classification.roc_curve_static(
                fpr, tpr, auc=auc, title=cap.split(" — ")[0]
            ),
        )
        for cap, tpr, auc in scenarios
    ]


def _pr_scenarios():
    recall = np.linspace(0.0, 1.0, 50)
    curves = [
        (
            "Strong on balanced data — precision stays high to the end.",
            1.0 - 0.12 * recall**6,
        ),
        (
            "Imbalanced but strong — precision holds until high recall.",
            0.98 - 0.5 * recall**12,
        ),
        (
            "Moderate model — precision erodes steadily with recall.",
            0.95 - 0.4 * recall**2,
        ),
        (
            "Weak on imbalanced data — precision collapses early.",
            0.7 - 0.5 * recall**1.5,
        ),
    ]
    out = []
    for cap, precision in curves:
        precision = np.clip(precision, 0.0, 1.0)
        ap = float(np.trapezoid(precision, recall))
        out.append((cap, precision, ap))
    return recall, out


def build_precision_recall():
    recall, scenarios = _pr_scenarios()
    return [
        (
            cap,
            dv.classification.precision_recall_curve_static(
                precision, recall, ap=ap, title=cap.split(" — ")[0]
            ),
        )
        for cap, precision, ap in scenarios
    ]


BUILDERS = {
    "confusion_matrix_plot": build_confusion_matrix,
    "roc_curve": build_roc,
    "precision_recall_curve": build_precision_recall,
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
                    "src": f"assets/examples/classification/{name}",
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
