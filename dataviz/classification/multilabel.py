"""Multilabel diagnostics: per-label CM grid, co-occurrence, hamming/subset bars."""

from __future__ import annotations

from typing import Optional, Sequence

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from ..types import ArrayLike, FigureSize, MatplotlibAxes, PlotlyFigure
from ..utils import setup_plot, apply_theme


def multilabel_confusion_grid_static(
    Y_true: ArrayLike, Y_pred: ArrayLike, labels: Optional[Sequence] = None,
    title: Optional[str] = None, figsize: FigureSize = (12, 8),
    cmap: str = "Blues", theme: str = "default", dpi: int = 100,
    style: str = "default",
) -> "np.ndarray":
    """One 2x2 confusion matrix per label arranged in a small-multiples grid."""
    Y_true = np.asarray(Y_true).astype(int); Y_pred = np.asarray(Y_pred).astype(int)
    n_labels = Y_true.shape[1]
    if labels is None:
        labels = [f"L{i}" for i in range(n_labels)]
    cols = min(4, n_labels); rows = int(np.ceil(n_labels / cols))
    title = title or "Multilabel confusion matrices"
    with plt.style.context(style):
        fig, axes = plt.subplots(rows, cols, figsize=figsize, dpi=dpi,
                                 squeeze=False)
        fig.suptitle(title)
        for k in range(n_labels):
            ax = axes[k // cols, k % cols]
            yt = Y_true[:, k]; yp = Y_pred[:, k]
            tp = int(((yt == 1) & (yp == 1)).sum())
            fp = int(((yt == 0) & (yp == 1)).sum())
            tn = int(((yt == 0) & (yp == 0)).sum())
            fn = int(((yt == 1) & (yp == 0)).sum())
            cm = np.array([[tn, fp], [fn, tp]])
            im = ax.imshow(cm, cmap=cmap)
            for i in range(2):
                for j in range(2):
                    ax.text(j, i, str(cm[i, j]), ha="center", va="center",
                            fontsize=10,
                            color="white" if cm[i, j] > cm.max() / 2 else "black")
            ax.set_title(str(labels[k]), fontsize=10)
            ax.set_xticks([0, 1]); ax.set_xticklabels(["pred 0", "pred 1"], fontsize=8)
            ax.set_yticks([0, 1]); ax.set_yticklabels(["true 0", "true 1"], fontsize=8)
        for k in range(n_labels, rows * cols):
            axes[k // cols, k % cols].axis("off")
        fig.tight_layout()
    return axes


def multilabel_confusion_grid_interactive(
    Y_true: ArrayLike, Y_pred: ArrayLike, labels: Optional[Sequence] = None,
    title: Optional[str] = None, height: int = 700, width: int = 1000,
    template: str = "plotly", colorscale: str = "Blues",
) -> PlotlyFigure:
    Y_true = np.asarray(Y_true).astype(int); Y_pred = np.asarray(Y_pred).astype(int)
    n_labels = Y_true.shape[1]
    if labels is None:
        labels = [f"L{i}" for i in range(n_labels)]
    cols = min(4, n_labels); rows = int(np.ceil(n_labels / cols))
    fig = make_subplots(rows=rows, cols=cols, subplot_titles=[str(l) for l in labels])
    for k in range(n_labels):
        r, c = k // cols + 1, k % cols + 1
        yt = Y_true[:, k]; yp = Y_pred[:, k]
        tp = int(((yt == 1) & (yp == 1)).sum())
        fp = int(((yt == 0) & (yp == 1)).sum())
        tn = int(((yt == 0) & (yp == 0)).sum())
        fn = int(((yt == 1) & (yp == 0)).sum())
        cm = [[tn, fp], [fn, tp]]
        fig.add_trace(go.Heatmap(z=cm, x=["pred 0", "pred 1"],
                                 y=["true 0", "true 1"], colorscale=colorscale,
                                 showscale=False,
                                 text=[[str(v) for v in row] for row in cm],
                                 texttemplate="%{text}"),
                      row=r, col=c)
    fig.update_layout(title=title or "Multilabel confusion matrices",
                      template=template, height=height, width=width)
    return fig


def label_cooccurrence_heatmap_static(
    Y: ArrayLike, labels: Optional[Sequence] = None, normalize: bool = True,
    title: Optional[str] = None, figsize: FigureSize = (8, 7),
    cmap: str = "viridis", annot: bool = True, theme: str = "default",
    dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Heatmap of label co-occurrence counts (or Jaccard if normalized)."""
    Y = np.asarray(Y).astype(int)
    n_labels = Y.shape[1]
    if labels is None:
        labels = [f"L{i}" for i in range(n_labels)]
    co = (Y.T @ Y).astype(float)
    if normalize:
        denom = co + co.T - np.minimum(co, co.T)
        co = np.divide(co, denom + 1e-9)
    title = title or ("Label Jaccard co-occurrence" if normalize else "Label co-occurrence counts")
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="", ylabel="", figsize=figsize)
        fig.set_dpi(dpi)
        im = ax.imshow(co, cmap=cmap, vmin=0)
        ax.set_xticks(range(n_labels))
        ax.set_xticklabels([str(l) for l in labels], rotation=45, ha="right")
        ax.set_yticks(range(n_labels))
        ax.set_yticklabels([str(l) for l in labels])
        if annot:
            for i in range(n_labels):
                for j in range(n_labels):
                    fmt = ".2f" if normalize else ".0f"
                    ax.text(j, i, format(co[i, j], fmt), ha="center", va="center",
                            fontsize=8,
                            color="white" if co[i, j] > co.max() / 2 else "black")
        fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
        apply_theme(ax, theme)
    return ax


def label_cooccurrence_heatmap_interactive(
    Y: ArrayLike, labels: Optional[Sequence] = None, normalize: bool = True,
    title: Optional[str] = None, height: int = 600, width: int = 700,
    template: str = "plotly", colorscale: str = "Viridis",
) -> PlotlyFigure:
    Y = np.asarray(Y).astype(int); n_labels = Y.shape[1]
    if labels is None:
        labels = [f"L{i}" for i in range(n_labels)]
    co = (Y.T @ Y).astype(float)
    if normalize:
        denom = co + co.T - np.minimum(co, co.T)
        co = np.divide(co, denom + 1e-9)
    xs = [str(l) for l in labels]
    fmt = ".2f" if normalize else ".0f"
    fig = go.Figure(go.Heatmap(z=co, x=xs, y=xs, colorscale=colorscale,
                               text=[[format(v, fmt) for v in row] for row in co],
                               texttemplate="%{text}"))
    fig.update_layout(title=title or ("Label Jaccard" if normalize else "Label co-occurrence"),
                      template=template, height=height, width=width)
    return fig


def hamming_subset_accuracy_bar_static(
    Y_true: ArrayLike, Y_pred: ArrayLike, title: Optional[str] = None,
    figsize: FigureSize = (8, 5), theme: str = "default", dpi: int = 100,
    style: str = "default",
) -> MatplotlibAxes:
    """Bar chart of Hamming accuracy and exact-subset accuracy for multilabel."""
    Y_true = np.asarray(Y_true).astype(int); Y_pred = np.asarray(Y_pred).astype(int)
    hamming = float(1 - np.mean(np.abs(Y_true - Y_pred)))
    subset = float((Y_true == Y_pred).all(axis=1).mean())
    values = {"Hamming accuracy": hamming, "Subset (exact) accuracy": subset}
    title = title or "Multilabel accuracy summary"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="", ylabel="Accuracy",
                             figsize=figsize)
        fig.set_dpi(dpi)
        ax.bar(list(values.keys()), list(values.values()),
               color=["#1f77b4", "#ff7f0e"])
        ax.set_ylim(0, 1.05)
        for i, v in enumerate(values.values()):
            ax.text(i, v, f"{v:.3f}", ha="center", va="bottom", fontsize=10)
        apply_theme(ax, theme)
    return ax


def hamming_subset_accuracy_bar_interactive(
    Y_true: ArrayLike, Y_pred: ArrayLike, title: Optional[str] = None,
    height: int = 450, width: int = 600, template: str = "plotly",
) -> PlotlyFigure:
    Y_true = np.asarray(Y_true).astype(int); Y_pred = np.asarray(Y_pred).astype(int)
    hamming = float(1 - np.mean(np.abs(Y_true - Y_pred)))
    subset = float((Y_true == Y_pred).all(axis=1).mean())
    values = {"Hamming accuracy": hamming, "Subset (exact) accuracy": subset}
    fig = go.Figure(go.Bar(x=list(values.keys()), y=list(values.values()),
                           text=[f"{v:.3f}" for v in values.values()],
                           textposition="outside"))
    fig.update_layout(title=title or "Multilabel accuracy summary",
                      yaxis=dict(range=[0, 1.05], title="Accuracy"),
                      template=template, height=height, width=width)
    return fig
