"""Render four real clustering example images per chart family.

Deterministic synthetic data (``numpy.random.default_rng``) drives every chart
so the output is reproducible. Images and a ``manifest.json`` (family -> image
list with captions) are written to ``website/assets/examples/clustering``; the
manifest is consumed by ``_generate_function_docs.mjs`` to attach galleries to
clustering pages.
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import dataviz as dv  # noqa: E402

OUT_DIR = Path(__file__).resolve().parent / "assets" / "examples" / "clustering"
DPI = 110


def _figure_of(result):
    if isinstance(result, plt.Figure):
        return result
    if isinstance(result, (tuple, list)):
        return result[0].figure
    return result.figure


def _rng(seed: int) -> np.random.Generator:
    return np.random.default_rng(seed)


def _blobs(seed, centres, spread=0.4, n=40):
    rng = _rng(seed)
    xs, ys, ls = [], [], []
    for i, (cx, cy) in enumerate(centres):
        xs.append(rng.normal(cx, spread, n))
        ys.append(rng.normal(cy, spread, n))
        ls.append(np.full(n, i))
    return np.concatenate(xs), np.concatenate(ys), np.concatenate(ls)


def _scatter_scenarios():
    x1, y1, l1 = _blobs(0, [(0.0, 0.0), (3.0, 3.0), (1.5, 5.0)])
    x2, y2, l2 = _blobs(1, [(0.0, 0.0), (1.2, 1.0), (0.6, 2.0)], spread=0.7)
    rng = _rng(2)
    t = rng.uniform(0.0, 2 * np.pi, 120)
    r = np.where(t < np.pi, 1.0, 2.2) + rng.normal(0.0, 0.15, 120)
    x3, y3 = r * np.cos(t), r * np.sin(t)
    l3 = (t >= np.pi).astype(int)
    x4, y4, l4 = _blobs(3, [(0.0, 0.0), (4.0, 0.5), (2.0, 4.0)])
    return [
        (
            "Well separated — three compact clusters with clear gaps.",
            x1,
            y1,
            l1,
            False,
        ),
        (
            "Overlapping clusters — boundaries blur between groups.",
            x2,
            y2,
            l2,
            False,
        ),
        (
            "Non-spherical structure — ring shapes defeat distance-based splits.",
            x3,
            y3,
            l3,
            False,
        ),
        (
            "With centroids — markers locate each cluster centre.",
            x4,
            y4,
            l4,
            True,
        ),
    ]


def build_scatter():
    return [
        (
            cap,
            dv.clustering.scatter_clusters_static(
                x, y, labels, show_centroids=cent, title=cap.split(" — ")[0]
            ),
        )
        for cap, x, y, labels, cent in _scatter_scenarios()
    ]


def _linkage_scenarios():
    clear3 = np.array(
        [
            [0.0, 1.0, 0.15, 2.0],
            [2.0, 3.0, 0.22, 2.0],
            [4.0, 5.0, 0.18, 2.0],
            [6.0, 7.0, 0.55, 4.0],
            [8.0, 9.0, 1.10, 6.0],
        ]
    )
    chained = np.array(
        [
            [0.0, 1.0, 0.10, 2.0],
            [6.0, 2.0, 0.16, 3.0],
            [7.0, 3.0, 0.24, 4.0],
            [8.0, 4.0, 0.33, 5.0],
            [9.0, 5.0, 0.42, 6.0],
        ]
    )
    two_groups = np.array(
        [
            [0.0, 1.0, 0.12, 2.0],
            [2.0, 6.0, 0.20, 3.0],
            [3.0, 4.0, 0.14, 2.0],
            [5.0, 8.0, 0.22, 3.0],
            [7.0, 9.0, 1.30, 6.0],
        ]
    )
    cut = np.array(
        [
            [0.0, 1.0, 0.15, 2.0],
            [2.0, 3.0, 0.25, 2.0],
            [4.0, 5.0, 0.20, 2.0],
            [6.0, 7.0, 0.60, 4.0],
            [8.0, 9.0, 1.05, 6.0],
        ]
    )
    labels = ["S1", "S2", "S3", "S4", "S5", "S6"]
    return [
        (
            "Clear structure — long final gaps mark three natural clusters.",
            clear3,
            labels,
            None,
        ),
        (
            "Chained merges — no gap suggests a clean place to cut.",
            chained,
            labels,
            None,
        ),
        (
            "Two dominant groups — one large merge splits the tree in half.",
            two_groups,
            labels,
            None,
        ),
        (
            "Cut by threshold — colouring marks clusters below the line.",
            cut,
            labels,
            0.8,
        ),
    ]


def build_dendrogram():
    out = []
    for cap, z, labels, threshold in _linkage_scenarios():
        kwargs = {"title": cap.split(" — ")[0], "labels": labels}
        if threshold is not None:
            kwargs["color_threshold"] = threshold
        out.append((cap, dv.clustering.dendrogram_static(z, **kwargs)))
    return out


def _elbow_scenarios():
    ks = np.arange(1, 11)
    clear3 = np.array(
        [900.0, 420.0, 260.0, 190.0, 160.0, 140.0, 128.0, 120.0, 115.0, 110.0]
    )
    smooth = 900.0 * np.exp(-0.35 * (ks - 1)) + 80.0
    clear4 = np.array(
        [950.0, 520.0, 330.0, 210.0, 180.0, 165.0, 155.0, 148.0, 143.0, 140.0]
    )
    steep2 = np.array(
        [900.0, 250.0, 200.0, 175.0, 160.0, 150.0, 143.0, 138.0, 134.0, 130.0]
    )
    return [
        (
            "Clear elbow — the curve bends sharply at three clusters.",
            ks,
            clear3,
            2,
        ),
        (
            "No elbow — a smooth decline offers no obvious choice.",
            ks,
            smooth,
            None,
        ),
        (
            "Elbow at four — the bend arrives one cluster later.",
            ks,
            clear4,
            3,
        ),
        (
            "Steep drop, quick plateau — two clusters capture most structure.",
            ks,
            steep2,
            1,
        ),
    ]


def build_elbow():
    out = []
    for cap, ks, inertias, idx in _elbow_scenarios():
        kwargs = {"title": cap.split(" — ")[0]}
        if idx is not None:
            kwargs["elbow_idx"] = idx
        out.append((cap, dv.clustering.elbow_plot_static(ks, inertias, **kwargs)))
    return out


BUILDERS = {
    "scatter_clusters": build_scatter,
    "dendrogram": build_dendrogram,
    "elbow_plot": build_elbow,
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
                    "src": f"assets/examples/clustering/{name}",
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
