"""Per-class summary bars, top-K accuracy, confusion-flow Sankey."""

from __future__ import annotations

from typing import Mapping, Optional, Sequence

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from ..types import ArrayLike, FigureSize, MatplotlibAxes, PlotlyFigure
from ..utils import setup_plot, apply_theme
from .multiclass import _auc


def per_class_auc_bar_static(
    auc_per_class: Mapping[str, float], title: Optional[str] = None,
    figsize: FigureSize = (9, 5), color: str = "#1f77b4", grid: bool = True,
    grid_alpha: float = 0.3, theme: str = "default", dpi: int = 100,
    style: str = "default",
) -> MatplotlibAxes:
    """Bar chart of per-class one-vs-rest AUC values."""
    title = title or "Per-class ROC AUC"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Class", ylabel="AUC",
                             figsize=figsize)
        fig.set_dpi(dpi)
        names = list(auc_per_class.keys()); values = list(auc_per_class.values())
        ax.bar(names, values, color=color)
        ax.axhline(0.5, linestyle="--", color="grey", label="random")
        ax.set_ylim(0, 1.05)
        for i, v in enumerate(values):
            ax.text(i, v, f"{v:.3f}", ha="center", va="bottom", fontsize=9)
        if grid:
            ax.grid(True, axis="y", alpha=grid_alpha)
        ax.legend()
        apply_theme(ax, theme)
    return ax


def per_class_auc_bar_interactive(
    auc_per_class: Mapping[str, float], title: Optional[str] = None,
    height: int = 500, width: int = 700, template: str = "plotly",
) -> PlotlyFigure:
    title = title or "Per-class ROC AUC"
    names = list(auc_per_class.keys()); values = list(auc_per_class.values())
    fig = go.Figure(go.Bar(x=names, y=values,
                           text=[f"{v:.3f}" for v in values], textposition="outside"))
    fig.add_hline(y=0.5, line_dash="dash", annotation_text="random")
    fig.update_layout(title=title, xaxis_title="Class", yaxis_title="AUC",
                      template=template, height=height, width=width,
                      yaxis=dict(range=[0, 1.05]))
    return fig


def per_class_ap_bar_static(
    ap_per_class: Mapping[str, float], title: Optional[str] = None,
    figsize: FigureSize = (9, 5), color: str = "#2ca02c", grid: bool = True,
    grid_alpha: float = 0.3, theme: str = "default", dpi: int = 100,
    style: str = "default",
) -> MatplotlibAxes:
    """Bar chart of per-class Average Precision values."""
    title = title or "Per-class Average Precision"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Class",
                             ylabel="Average Precision", figsize=figsize)
        fig.set_dpi(dpi)
        names = list(ap_per_class.keys()); values = list(ap_per_class.values())
        ax.bar(names, values, color=color)
        ax.set_ylim(0, 1.05)
        for i, v in enumerate(values):
            ax.text(i, v, f"{v:.3f}", ha="center", va="bottom", fontsize=9)
        if grid:
            ax.grid(True, axis="y", alpha=grid_alpha)
        apply_theme(ax, theme)
    return ax


def per_class_ap_bar_interactive(
    ap_per_class: Mapping[str, float], title: Optional[str] = None,
    height: int = 500, width: int = 700, template: str = "plotly",
) -> PlotlyFigure:
    title = title or "Per-class Average Precision"
    names = list(ap_per_class.keys()); values = list(ap_per_class.values())
    fig = go.Figure(go.Bar(x=names, y=values,
                           text=[f"{v:.3f}" for v in values], textposition="outside"))
    fig.update_layout(title=title, xaxis_title="Class",
                      yaxis_title="Average Precision",
                      template=template, height=height, width=width,
                      yaxis=dict(range=[0, 1.05]))
    return fig


def top_k_accuracy_curve_static(
    y_true: ArrayLike, y_prob_matrix: ArrayLike, max_k: Optional[int] = None,
    title: Optional[str] = None, figsize: FigureSize = (9, 6), grid: bool = True,
    grid_alpha: float = 0.3, theme: str = "default", dpi: int = 100,
    style: str = "default",
) -> MatplotlibAxes:
    """Top-K accuracy vs K. Accuracy increases monotonically with K."""
    y_true = np.asarray(y_true).astype(int)
    P = np.asarray(y_prob_matrix, dtype=float)
    n_classes = P.shape[1]
    max_k = max_k or n_classes
    ranks = np.argsort(-P, axis=1)
    acc = []
    for k in range(1, max_k + 1):
        topk = ranks[:, :k]
        acc.append(float(np.mean([y in row for y, row in zip(y_true, topk)])))
    title = title or "Top-K accuracy"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="K", ylabel="Top-K accuracy",
                             figsize=figsize)
        fig.set_dpi(dpi)
        ks = list(range(1, max_k + 1))
        ax.plot(ks, acc, "o-", linewidth=2)
        ax.set_ylim(0, 1.02)
        for k, v in zip(ks, acc):
            ax.text(k, v, f"{v:.2f}", ha="center", va="bottom", fontsize=8)
        if grid:
            ax.grid(True, alpha=grid_alpha)
        apply_theme(ax, theme)
    return ax


def top_k_accuracy_curve_interactive(
    y_true: ArrayLike, y_prob_matrix: ArrayLike, max_k: Optional[int] = None,
    title: Optional[str] = None, height: int = 500, width: int = 700,
    template: str = "plotly",
) -> PlotlyFigure:
    y_true = np.asarray(y_true).astype(int)
    P = np.asarray(y_prob_matrix, dtype=float)
    n_classes = P.shape[1]; max_k = max_k or n_classes
    ranks = np.argsort(-P, axis=1)
    acc = [float(np.mean([y in row for y, row in zip(y_true, ranks[:, :k])]))
           for k in range(1, max_k + 1)]
    title = title or "Top-K accuracy"
    fig = go.Figure(go.Scatter(x=list(range(1, max_k + 1)), y=acc,
                               mode="lines+markers"))
    fig.update_layout(title=title, xaxis_title="K", yaxis_title="Top-K accuracy",
                      template=template, height=height, width=width,
                      yaxis=dict(range=[0, 1.02]))
    return fig


def confusion_sankey_static(
    y_true: ArrayLike, y_pred: ArrayLike, labels: Optional[Sequence] = None,
    title: Optional[str] = None, figsize: FigureSize = (10, 7),
    cmap: str = "tab10", theme: str = "default", dpi: int = 100,
    style: str = "default",
) -> MatplotlibAxes:
    """Static 'Sankey-like' visualisation of true→predicted class flows.

    Renders parallel columns of nodes connected by quadrilaterals whose width
    encodes the flow magnitude. For an interactive Sankey use the plotly
    counterpart.
    """
    y_true = np.asarray(y_true); y_pred = np.asarray(y_pred)
    if labels is None:
        labels = sorted(set(np.unique(y_true).tolist() + np.unique(y_pred).tolist()))
    n = len(labels)
    M = np.zeros((n, n), dtype=float)
    for i, t in enumerate(labels):
        for j, p in enumerate(labels):
            M[i, j] = int(((y_true == t) & (y_pred == p)).sum())
    title = title or "Confusion flow"
    colors = plt.get_cmap(cmap)(np.linspace(0, 1, n))
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="", ylabel="", figsize=figsize)
        fig.set_dpi(dpi)
        total = max(M.sum(), 1)
        left_y = np.cumsum(np.concatenate([[0], M.sum(axis=1)])) / total
        right_y = np.cumsum(np.concatenate([[0], M.sum(axis=0)])) / total
        for i in range(n):
            ax.add_patch(plt.Rectangle((0.0, left_y[i]), 0.05,
                                       left_y[i + 1] - left_y[i],
                                       color=colors[i]))
            ax.text(-0.02, (left_y[i] + left_y[i + 1]) / 2, str(labels[i]),
                    ha="right", va="center", fontsize=9)
            ax.add_patch(plt.Rectangle((0.95, right_y[i]), 0.05,
                                       right_y[i + 1] - right_y[i],
                                       color=colors[i]))
            ax.text(1.02, (right_y[i] + right_y[i + 1]) / 2, str(labels[i]),
                    ha="left", va="center", fontsize=9)
        cum_l = left_y.copy(); cum_r = right_y.copy()
        for i in range(n):
            for j in range(n):
                w = M[i, j] / total
                if w <= 0:
                    continue
                ax.fill([0.05, 0.95, 0.95, 0.05],
                        [cum_l[i], cum_r[j], cum_r[j] + w, cum_l[i] + w],
                        color=colors[i], alpha=0.25, linewidth=0)
                cum_l[i] += w; cum_r[j] += w
        ax.set_xlim(-0.2, 1.2); ax.set_ylim(-0.02, 1.02)
        ax.set_xticks([]); ax.set_yticks([])
        for sp in ax.spines.values():
            sp.set_visible(False)
        apply_theme(ax, theme)
    return ax


def confusion_sankey_interactive(
    y_true: ArrayLike, y_pred: ArrayLike, labels: Optional[Sequence] = None,
    title: Optional[str] = None, height: int = 600, width: int = 800,
    template: str = "plotly",
) -> PlotlyFigure:
    """Interactive Sankey of true → predicted class flow."""
    y_true = np.asarray(y_true); y_pred = np.asarray(y_pred)
    if labels is None:
        labels = sorted(set(np.unique(y_true).tolist() + np.unique(y_pred).tolist()))
    n = len(labels)
    node_labels = [f"T:{l}" for l in labels] + [f"P:{l}" for l in labels]
    sources, targets, values = [], [], []
    for i, t in enumerate(labels):
        for j, p in enumerate(labels):
            v = int(((y_true == t) & (y_pred == p)).sum())
            if v > 0:
                sources.append(i); targets.append(n + j); values.append(v)
    fig = go.Figure(go.Sankey(
        node=dict(label=node_labels, pad=12, thickness=15),
        link=dict(source=sources, target=targets, value=values),
    ))
    fig.update_layout(title=title or "Confusion flow (true → predicted)",
                      template=template, height=height, width=width)
    return fig
