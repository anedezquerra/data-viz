"""Cohort / segment explainability charts."""

from __future__ import annotations

from typing import Mapping, Optional, Sequence

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from ..types import FigureSize, MatplotlibAxes, MatrixLike, PlotlyFigure
from ..utils import setup_plot, apply_theme


def importance_by_segment_heatmap_static(
    importances: Mapping[str, Mapping[str, float]],
    title: Optional[str] = None, figsize: FigureSize = (10, 7),
    cmap: str = "magma", annot: bool = True, theme: str = "default",
    dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Heatmap of per-segment feature importances.

    Args:
        importances: ``{segment_name: {feature: value, ...}, ...}`` with shared
            feature keys across segments.
    """
    segments = list(importances.keys())
    features = list(next(iter(importances.values())).keys())
    M = np.array([[importances[s][f] for f in features] for s in segments])
    title = title or "Feature importance by segment"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Feature", ylabel="Segment",
                             figsize=figsize)
        fig.set_dpi(dpi)
        im = ax.imshow(M, aspect="auto", cmap=cmap)
        ax.set_xticks(range(len(features)))
        ax.set_xticklabels(features, rotation=45, ha="right")
        ax.set_yticks(range(len(segments)))
        ax.set_yticklabels(segments)
        if annot:
            for i in range(len(segments)):
                for j in range(len(features)):
                    ax.text(j, i, f"{M[i, j]:.2f}", ha="center", va="center",
                            fontsize=8,
                            color="white" if M[i, j] > M.max() / 2 else "black")
        fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
        apply_theme(ax, theme)
    return ax


def importance_by_segment_heatmap_interactive(
    importances: Mapping[str, Mapping[str, float]],
    title: Optional[str] = None, height: int = 600, width: int = 900,
    template: str = "plotly", colorscale: str = "Magma",
) -> PlotlyFigure:
    segments = list(importances.keys())
    features = list(next(iter(importances.values())).keys())
    M = np.array([[importances[s][f] for f in features] for s in segments])
    fig = go.Figure(go.Heatmap(z=M, x=features, y=segments,
                               colorscale=colorscale,
                               text=np.round(M, 2), texttemplate="%{text}"))
    fig.update_layout(title=title or "Feature importance by segment",
                      xaxis_title="Feature", yaxis_title="Segment",
                      template=template, height=height, width=width)
    return fig


def shap_cluster_heatmap_static(
    shap_values: MatrixLike, feature_names: Sequence[str],
    n_clusters: int = 4, title: Optional[str] = None,
    figsize: FigureSize = (10, 8), cmap: str = "coolwarm",
    theme: str = "default", dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Heatmap of instances × features sorted by k-means clusters of SHAP signatures.

    Uses a small Lloyd-style k-means in pure NumPy (no sklearn dependency).
    """
    S = np.asarray(shap_values, dtype=float)
    n = S.shape[0]
    rng = np.random.default_rng(0)
    init = rng.choice(n, size=n_clusters, replace=False)
    centers = S[init].copy()
    labels = np.zeros(n, dtype=int)
    for _ in range(30):
        dists = np.linalg.norm(S[:, None, :] - centers[None, :, :], axis=2)
        new_labels = dists.argmin(axis=1)
        if np.array_equal(new_labels, labels):
            break
        labels = new_labels
        for k in range(n_clusters):
            members = S[labels == k]
            if members.size:
                centers[k] = members.mean(axis=0)
    order = np.argsort(labels)
    Sord = S[order]
    title = title or f"SHAP clusters (k={n_clusters})"
    vmax = float(np.abs(S).max())
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Feature", ylabel="Instance",
                             figsize=figsize)
        fig.set_dpi(dpi)
        im = ax.imshow(Sord, aspect="auto", cmap=cmap, vmin=-vmax, vmax=vmax)
        ax.set_xticks(range(len(feature_names)))
        ax.set_xticklabels(feature_names, rotation=45, ha="right")
        # Cluster boundaries
        sorted_labels = labels[order]
        boundaries = np.where(np.diff(sorted_labels) != 0)[0]
        for b in boundaries:
            ax.axhline(b + 0.5, color="black", linewidth=1.2)
        cb = fig.colorbar(im, ax=ax, fraction=0.04, pad=0.02)
        cb.set_label("SHAP value")
        apply_theme(ax, theme)
    return ax


def shap_cluster_heatmap_interactive(
    shap_values: MatrixLike, feature_names: Sequence[str],
    n_clusters: int = 4, title: Optional[str] = None,
    height: int = 700, width: int = 900, template: str = "plotly",
    colorscale: str = "RdBu_r",
) -> PlotlyFigure:
    S = np.asarray(shap_values, dtype=float)
    n = S.shape[0]
    rng = np.random.default_rng(0)
    init = rng.choice(n, size=n_clusters, replace=False)
    centers = S[init].copy()
    labels = np.zeros(n, dtype=int)
    for _ in range(30):
        dists = np.linalg.norm(S[:, None, :] - centers[None, :, :], axis=2)
        new_labels = dists.argmin(axis=1)
        if np.array_equal(new_labels, labels):
            break
        labels = new_labels
        for k in range(n_clusters):
            members = S[labels == k]
            if members.size:
                centers[k] = members.mean(axis=0)
    order = np.argsort(labels)
    Sord = S[order]
    vmax = float(np.abs(S).max())
    fig = go.Figure(go.Heatmap(z=Sord, x=list(feature_names),
                               colorscale=colorscale, zmin=-vmax, zmax=vmax,
                               colorbar=dict(title="SHAP value")))
    fig.update_layout(title=title or f"SHAP clusters (k={n_clusters})",
                      xaxis_title="Feature", yaxis_title="Instance",
                      template=template, height=height, width=width)
    return fig
