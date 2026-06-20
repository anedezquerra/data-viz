"""Per-class report, class balance and prediction-distribution charts."""

from __future__ import annotations

from typing import Mapping, Optional, Sequence

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from ..types import ArrayLike, FigureSize, MatplotlibAxes, PlotlyFigure
from ..utils import setup_plot, apply_theme


def _per_class_metrics(y_true: np.ndarray, y_pred: np.ndarray, labels: Sequence):
    out = {}
    for lab in labels:
        tp = int(((y_pred == lab) & (y_true == lab)).sum())
        fp = int(((y_pred == lab) & (y_true != lab)).sum())
        fn = int(((y_pred != lab) & (y_true == lab)).sum())
        prec = tp / (tp + fp) if tp + fp > 0 else 0.0
        rec = tp / (tp + fn) if tp + fn > 0 else 0.0
        f1 = 2 * prec * rec / (prec + rec) if prec + rec > 0 else 0.0
        support = int((y_true == lab).sum())
        out[lab] = dict(precision=prec, recall=rec, f1=f1, support=support)
    return out


def classification_report_heatmap_static(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    labels: Optional[Sequence] = None,
    title: Optional[str] = None,
    figsize: FigureSize = (8, 6),
    cmap: str = "YlGn",
    annot: bool = True,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
) -> MatplotlibAxes:
    """Heatmap of per-class precision / recall / F1 (rows = classes)."""
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    if labels is None:
        labels = sorted(set(np.unique(y_true).tolist() + np.unique(y_pred).tolist()))
    metrics = _per_class_metrics(y_true, y_pred, labels)
    cols = ["precision", "recall", "f1"]
    data = np.array([[metrics[l][c] for c in cols] for l in labels])
    title = title or "Per-class classification report"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="", ylabel="", figsize=figsize)
        fig.set_dpi(dpi)
        im = ax.imshow(data, cmap=cmap, vmin=0, vmax=1, aspect="auto")
        ax.set_xticks(range(len(cols)))
        ax.set_xticklabels(cols)
        ax.set_yticks(range(len(labels)))
        ax.set_yticklabels([str(l) for l in labels])
        if annot:
            for i in range(len(labels)):
                for j in range(len(cols)):
                    ax.text(j, i, f"{data[i, j]:.2f}", ha="center", va="center",
                            color="black", fontsize=10)
        fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
        apply_theme(ax, theme)
    return ax


def classification_report_heatmap_interactive(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    labels: Optional[Sequence] = None,
    title: Optional[str] = None,
    height: int = 500,
    width: int = 600,
    template: str = "plotly",
    colorscale: str = "YlGn",
) -> PlotlyFigure:
    """Interactive per-class classification report heatmap."""
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    if labels is None:
        labels = sorted(set(np.unique(y_true).tolist() + np.unique(y_pred).tolist()))
    metrics = _per_class_metrics(y_true, y_pred, labels)
    cols = ["precision", "recall", "f1"]
    data = [[metrics[l][c] for c in cols] for l in labels]
    title = title or "Per-class classification report"
    fig = go.Figure(go.Heatmap(z=data, x=cols, y=[str(l) for l in labels],
                               colorscale=colorscale, zmin=0, zmax=1,
                               text=[[f"{v:.2f}" for v in row] for row in data],
                               texttemplate="%{text}"))
    fig.update_layout(title=title, template=template, height=height, width=width)
    return fig


def per_class_metrics_bar_static(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    labels: Optional[Sequence] = None,
    title: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
) -> MatplotlibAxes:
    """Grouped bar chart of precision / recall / F1 per class."""
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    if labels is None:
        labels = sorted(set(np.unique(y_true).tolist() + np.unique(y_pred).tolist()))
    metrics = _per_class_metrics(y_true, y_pred, labels)
    cols = ["precision", "recall", "f1"]
    title = title or "Per-class precision / recall / F1"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Class", ylabel="Score",
                             figsize=figsize)
        fig.set_dpi(dpi)
        x = np.arange(len(labels))
        w = 0.27
        for i, c in enumerate(cols):
            vals = [metrics[l][c] for l in labels]
            ax.bar(x + (i - 1) * w, vals, w, label=c)
        ax.set_xticks(x)
        ax.set_xticklabels([str(l) for l in labels])
        ax.set_ylim(0, 1.05)
        if grid:
            ax.grid(True, axis="y", alpha=grid_alpha)
        ax.legend()
        apply_theme(ax, theme)
    return ax


def per_class_metrics_bar_interactive(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    labels: Optional[Sequence] = None,
    title: Optional[str] = None,
    height: int = 600,
    width: int = 800,
    template: str = "plotly",
) -> PlotlyFigure:
    """Interactive grouped bar of per-class precision/recall/F1."""
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    if labels is None:
        labels = sorted(set(np.unique(y_true).tolist() + np.unique(y_pred).tolist()))
    metrics = _per_class_metrics(y_true, y_pred, labels)
    cols = ["precision", "recall", "f1"]
    title = title or "Per-class precision / recall / F1"
    fig = go.Figure()
    for c in cols:
        fig.add_trace(go.Bar(name=c, x=[str(l) for l in labels],
                             y=[metrics[l][c] for l in labels]))
    fig.update_layout(barmode="group", title=title, xaxis_title="Class",
                      yaxis_title="Score", template=template,
                      height=height, width=width, yaxis=dict(range=[0, 1.05]))
    return fig


def class_balance_bar_static(
    y_true: ArrayLike,
    y_pred: Optional[ArrayLike] = None,
    labels: Optional[Sequence] = None,
    title: Optional[str] = None,
    figsize: FigureSize = (8, 5),
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
) -> MatplotlibAxes:
    """Class counts in ground truth and (optionally) predictions side by side."""
    y_true = np.asarray(y_true)
    if labels is None:
        labels = sorted(np.unique(y_true).tolist())
    true_counts = [int((y_true == l).sum()) for l in labels]
    title = title or "Class balance"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Class", ylabel="Count",
                             figsize=figsize)
        fig.set_dpi(dpi)
        x = np.arange(len(labels))
        if y_pred is not None:
            y_pred = np.asarray(y_pred)
            pred_counts = [int((y_pred == l).sum()) for l in labels]
            ax.bar(x - 0.2, true_counts, 0.4, label="true")
            ax.bar(x + 0.2, pred_counts, 0.4, label="pred")
            ax.legend()
        else:
            ax.bar(x, true_counts, color="tab:blue")
        ax.set_xticks(x)
        ax.set_xticklabels([str(l) for l in labels])
        if grid:
            ax.grid(True, axis="y", alpha=grid_alpha)
        apply_theme(ax, theme)
    return ax


def class_balance_bar_interactive(
    y_true: ArrayLike,
    y_pred: Optional[ArrayLike] = None,
    labels: Optional[Sequence] = None,
    title: Optional[str] = None,
    height: int = 500,
    width: int = 700,
    template: str = "plotly",
) -> PlotlyFigure:
    """Interactive class balance bar chart."""
    y_true = np.asarray(y_true)
    if labels is None:
        labels = sorted(np.unique(y_true).tolist())
    true_counts = [int((y_true == l).sum()) for l in labels]
    title = title or "Class balance"
    fig = go.Figure()
    fig.add_trace(go.Bar(x=[str(l) for l in labels], y=true_counts, name="true"))
    if y_pred is not None:
        y_pred = np.asarray(y_pred)
        pred_counts = [int((y_pred == l).sum()) for l in labels]
        fig.add_trace(go.Bar(x=[str(l) for l in labels], y=pred_counts, name="pred"))
        fig.update_layout(barmode="group")
    fig.update_layout(title=title, xaxis_title="Class", yaxis_title="Count",
                      template=template, height=height, width=width)
    return fig


def prediction_distribution_static(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    labels: Optional[Sequence] = None,
    normalize: bool = True,
    title: Optional[str] = None,
    figsize: FigureSize = (9, 6),
    cmap: str = "tab10",
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
) -> MatplotlibAxes:
    """Stacked bar of predicted-class shares for each true class."""
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    if labels is None:
        labels = sorted(set(np.unique(y_true).tolist() + np.unique(y_pred).tolist()))
    n = len(labels)
    M = np.zeros((n, n), dtype=float)
    for i, t in enumerate(labels):
        for j, p in enumerate(labels):
            M[i, j] = int(((y_true == t) & (y_pred == p)).sum())
    if normalize:
        row_sum = M.sum(axis=1, keepdims=True)
        M = np.divide(M, row_sum, out=np.zeros_like(M), where=row_sum > 0)
    title = title or "Predicted class distribution per true class"
    colors = plt.get_cmap(cmap)(np.linspace(0, 1, n))
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="True class",
                             ylabel="Share" if normalize else "Count",
                             figsize=figsize)
        fig.set_dpi(dpi)
        x = np.arange(n)
        bottom = np.zeros(n)
        for j, p in enumerate(labels):
            ax.bar(x, M[:, j], bottom=bottom, color=colors[j],
                   label=f"pred={p}")
            bottom += M[:, j]
        ax.set_xticks(x)
        ax.set_xticklabels([str(l) for l in labels])
        ax.legend(loc="center left", bbox_to_anchor=(1.02, 0.5))
        apply_theme(ax, theme)
    return ax


def prediction_distribution_interactive(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    labels: Optional[Sequence] = None,
    normalize: bool = True,
    title: Optional[str] = None,
    height: int = 600,
    width: int = 800,
    template: str = "plotly",
) -> PlotlyFigure:
    """Interactive stacked-bar of predicted-class distribution per true class."""
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    if labels is None:
        labels = sorted(set(np.unique(y_true).tolist() + np.unique(y_pred).tolist()))
    n = len(labels)
    M = np.zeros((n, n), dtype=float)
    for i, t in enumerate(labels):
        for j, p in enumerate(labels):
            M[i, j] = int(((y_true == t) & (y_pred == p)).sum())
    if normalize:
        row_sum = M.sum(axis=1, keepdims=True)
        M = np.divide(M, row_sum, out=np.zeros_like(M), where=row_sum > 0)
    title = title or "Predicted class distribution per true class"
    fig = go.Figure()
    xlabs = [str(l) for l in labels]
    for j, p in enumerate(labels):
        fig.add_trace(go.Bar(name=f"pred={p}", x=xlabs, y=M[:, j]))
    fig.update_layout(barmode="stack", title=title, xaxis_title="True class",
                      yaxis_title="Share" if normalize else "Count",
                      template=template, height=height, width=width)
    return fig
