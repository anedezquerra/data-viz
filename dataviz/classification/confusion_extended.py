"""Extended confusion-matrix views: normalized, diff, errors, error grid."""

from __future__ import annotations

from typing import Optional, Sequence

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from ..types import ArrayLike, FigureSize, Labels, MatrixLike, MatplotlibAxes, PlotlyFigure
from ..utils import setup_plot, apply_theme


def _as_cm(cm: MatrixLike) -> np.ndarray:
    arr = np.asarray(cm, dtype=float)
    if arr.ndim != 2 or arr.shape[0] != arr.shape[1]:
        raise ValueError("Confusion matrix must be 2-D and square.")
    return arr


def normalized_confusion_matrix_static(
    cm: MatrixLike,
    labels: Optional[Labels] = None,
    normalize: str = "true",
    title: Optional[str] = None,
    figsize: FigureSize = (8, 6),
    cmap: str = "Blues",
    annot: bool = True,
    fmt: str = ".2f",
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
) -> MatplotlibAxes:
    """Confusion matrix normalized by ``"true"``, ``"pred"`` or ``"all"``.

    Args:
        normalize: ``"true"`` divides by row totals (recall per class),
            ``"pred"`` by column totals (precision per class), ``"all"`` by the
            grand total.
    """
    M = _as_cm(cm)
    if normalize == "true":
        denom = M.sum(axis=1, keepdims=True)
    elif normalize == "pred":
        denom = M.sum(axis=0, keepdims=True)
    elif normalize == "all":
        denom = M.sum()
    else:
        raise ValueError("normalize must be 'true', 'pred' or 'all'")
    Mn = np.divide(M, denom, out=np.zeros_like(M), where=denom > 0)
    title = title or f"Confusion matrix (normalized: {normalize})"
    if labels is None:
        labels = list(range(M.shape[0]))
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Predicted", ylabel="True",
                             figsize=figsize)
        fig.set_dpi(dpi)
        im = ax.imshow(Mn, cmap=cmap, vmin=0, vmax=Mn.max())
        ax.set_xticks(range(len(labels)))
        ax.set_xticklabels([str(l) for l in labels])
        ax.set_yticks(range(len(labels)))
        ax.set_yticklabels([str(l) for l in labels])
        if annot:
            for i in range(Mn.shape[0]):
                for j in range(Mn.shape[1]):
                    ax.text(j, i, format(Mn[i, j], fmt), ha="center", va="center",
                            color="white" if Mn[i, j] > Mn.max() / 2 else "black",
                            fontsize=10)
        fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
        apply_theme(ax, theme)
    return ax


def normalized_confusion_matrix_interactive(
    cm: MatrixLike,
    labels: Optional[Labels] = None,
    normalize: str = "true",
    title: Optional[str] = None,
    height: int = 600,
    width: int = 700,
    template: str = "plotly",
    colorscale: str = "Blues",
) -> PlotlyFigure:
    """Interactive normalized confusion matrix."""
    M = _as_cm(cm)
    if normalize == "true":
        denom = M.sum(axis=1, keepdims=True)
    elif normalize == "pred":
        denom = M.sum(axis=0, keepdims=True)
    else:
        denom = M.sum()
    Mn = np.divide(M, denom, out=np.zeros_like(M), where=denom > 0)
    title = title or f"Confusion matrix (normalized: {normalize})"
    if labels is None:
        labels = list(range(M.shape[0]))
    xs = [str(l) for l in labels]
    fig = go.Figure(go.Heatmap(z=Mn, x=xs, y=xs, colorscale=colorscale,
                               text=[[f"{v:.2f}" for v in row] for row in Mn],
                               texttemplate="%{text}"))
    fig.update_layout(title=title, xaxis_title="Predicted", yaxis_title="True",
                      template=template, height=height, width=width,
                      yaxis=dict(autorange="reversed"))
    return fig


def confusion_matrix_diff_static(
    cm_a: MatrixLike,
    cm_b: MatrixLike,
    labels: Optional[Labels] = None,
    title: Optional[str] = None,
    figsize: FigureSize = (8, 6),
    cmap: str = "RdBu_r",
    annot: bool = True,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
) -> MatplotlibAxes:
    """Element-wise difference between two confusion matrices (``cm_a - cm_b``)."""
    A = _as_cm(cm_a)
    B = _as_cm(cm_b)
    if A.shape != B.shape:
        raise ValueError("Confusion matrices must have the same shape.")
    D = A - B
    title = title or "Confusion matrix difference (A - B)"
    if labels is None:
        labels = list(range(A.shape[0]))
    vmax = float(np.abs(D).max() or 1.0)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Predicted", ylabel="True",
                             figsize=figsize)
        fig.set_dpi(dpi)
        im = ax.imshow(D, cmap=cmap, vmin=-vmax, vmax=vmax)
        ax.set_xticks(range(len(labels)))
        ax.set_xticklabels([str(l) for l in labels])
        ax.set_yticks(range(len(labels)))
        ax.set_yticklabels([str(l) for l in labels])
        if annot:
            for i in range(D.shape[0]):
                for j in range(D.shape[1]):
                    ax.text(j, i, f"{D[i, j]:+.0f}", ha="center", va="center",
                            fontsize=10)
        fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
        apply_theme(ax, theme)
    return ax


def confusion_matrix_diff_interactive(
    cm_a: MatrixLike,
    cm_b: MatrixLike,
    labels: Optional[Labels] = None,
    title: Optional[str] = None,
    height: int = 600,
    width: int = 700,
    template: str = "plotly",
    colorscale: str = "RdBu",
) -> PlotlyFigure:
    """Interactive confusion-matrix diff (model comparison)."""
    A = _as_cm(cm_a)
    B = _as_cm(cm_b)
    D = A - B
    title = title or "Confusion matrix difference (A - B)"
    if labels is None:
        labels = list(range(A.shape[0]))
    xs = [str(l) for l in labels]
    vmax = float(np.abs(D).max() or 1.0)
    fig = go.Figure(go.Heatmap(z=D, x=xs, y=xs, colorscale=colorscale,
                               zmin=-vmax, zmax=vmax,
                               text=[[f"{v:+.0f}" for v in row] for row in D],
                               texttemplate="%{text}"))
    fig.update_layout(title=title, xaxis_title="Predicted", yaxis_title="True",
                      template=template, height=height, width=width,
                      yaxis=dict(autorange="reversed"))
    return fig


def error_analysis_grid_static(
    cm: MatrixLike,
    labels: Optional[Labels] = None,
    title: Optional[str] = None,
    figsize: FigureSize = (8, 6),
    cmap: str = "Reds",
    annot: bool = True,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
) -> MatplotlibAxes:
    """Off-diagonal error-rate grid: only mis-classification entries are shown.

    Each cell ``(i, j)`` with ``i != j`` is divided by the row total to give
    the *probability of mistaking class i for class j*.
    """
    M = _as_cm(cm)
    row_sum = M.sum(axis=1, keepdims=True)
    Mn = np.divide(M, row_sum, out=np.zeros_like(M), where=row_sum > 0)
    np.fill_diagonal(Mn, 0.0)
    title = title or "Error analysis grid (off-diagonal mistake rate)"
    if labels is None:
        labels = list(range(M.shape[0]))
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Predicted", ylabel="True",
                             figsize=figsize)
        fig.set_dpi(dpi)
        im = ax.imshow(Mn, cmap=cmap, vmin=0, vmax=max(Mn.max(), 1e-6))
        ax.set_xticks(range(len(labels)))
        ax.set_xticklabels([str(l) for l in labels])
        ax.set_yticks(range(len(labels)))
        ax.set_yticklabels([str(l) for l in labels])
        if annot:
            for i in range(Mn.shape[0]):
                for j in range(Mn.shape[1]):
                    if i != j and Mn[i, j] > 0:
                        ax.text(j, i, f"{Mn[i, j]:.2f}", ha="center", va="center",
                                fontsize=10,
                                color="white" if Mn[i, j] > Mn.max() / 2 else "black")
        fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
        apply_theme(ax, theme)
    return ax


def error_analysis_grid_interactive(
    cm: MatrixLike,
    labels: Optional[Labels] = None,
    title: Optional[str] = None,
    height: int = 600,
    width: int = 700,
    template: str = "plotly",
    colorscale: str = "Reds",
) -> PlotlyFigure:
    """Interactive off-diagonal mistake-rate grid."""
    M = _as_cm(cm)
    row_sum = M.sum(axis=1, keepdims=True)
    Mn = np.divide(M, row_sum, out=np.zeros_like(M), where=row_sum > 0)
    np.fill_diagonal(Mn, 0.0)
    title = title or "Error analysis grid (off-diagonal mistake rate)"
    if labels is None:
        labels = list(range(M.shape[0]))
    xs = [str(l) for l in labels]
    fig = go.Figure(go.Heatmap(z=Mn, x=xs, y=xs, colorscale=colorscale, zmin=0,
                               text=[[f"{v:.2f}" if v > 0 else "" for v in row]
                                     for row in Mn],
                               texttemplate="%{text}"))
    fig.update_layout(title=title, xaxis_title="Predicted", yaxis_title="True",
                      template=template, height=height, width=width,
                      yaxis=dict(autorange="reversed"))
    return fig
