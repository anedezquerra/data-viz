"""Fairness / subgroup diagnostics."""

from __future__ import annotations

from typing import Mapping, Optional, Sequence

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from ..types import ArrayLike, FigureSize, MatplotlibAxes, PlotlyFigure
from ..utils import setup_plot, apply_theme
from .calibration import _bin_calibration


def _segment_metrics(y_true, y_pred, groups, metric):
    out = {}
    for g in np.unique(groups):
        mask = groups == g
        yt = y_true[mask]; yp = y_pred[mask]
        if metric == "accuracy":
            out[g] = float((yt == yp).mean())
        elif metric == "tpr":
            denom = (yt == 1).sum()
            out[g] = float(((yt == 1) & (yp == 1)).sum() / denom) if denom else 0.0
        elif metric == "fpr":
            denom = (yt == 0).sum()
            out[g] = float(((yt == 0) & (yp == 1)).sum() / denom) if denom else 0.0
        elif metric == "precision":
            denom = (yp == 1).sum()
            out[g] = float(((yt == 1) & (yp == 1)).sum() / denom) if denom else 0.0
        elif metric == "f1":
            tp = int(((yt == 1) & (yp == 1)).sum())
            fp = int(((yt == 0) & (yp == 1)).sum())
            fn = int(((yt == 1) & (yp == 0)).sum())
            p = tp / (tp + fp) if tp + fp else 0.0
            r = tp / (tp + fn) if tp + fn else 0.0
            out[g] = float(2 * p * r / (p + r)) if p + r else 0.0
        elif metric == "selection_rate":
            out[g] = float((yp == 1).mean())
        else:
            raise ValueError(f"unknown metric {metric}")
    return out


def per_segment_metric_bar_static(
    y_true: ArrayLike, y_pred: ArrayLike, groups: ArrayLike,
    metrics: Sequence[str] = ("accuracy", "f1", "tpr", "fpr"),
    title: Optional[str] = None, figsize: FigureSize = (10, 6),
    grid: bool = True, grid_alpha: float = 0.3, theme: str = "default",
    dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Grouped bar chart of metrics per demographic / segment group."""
    y_true = np.asarray(y_true).astype(int)
    y_pred = np.asarray(y_pred).astype(int)
    groups = np.asarray(groups)
    group_names = sorted(np.unique(groups).tolist())
    title = title or "Metrics per segment"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Segment", ylabel="Score",
                             figsize=figsize)
        fig.set_dpi(dpi)
        x = np.arange(len(group_names))
        w = 0.8 / len(metrics)
        for i, m in enumerate(metrics):
            ms = _segment_metrics(y_true, y_pred, groups, m)
            vals = [ms[g] for g in group_names]
            ax.bar(x + (i - (len(metrics) - 1) / 2) * w, vals, w, label=m)
        ax.set_xticks(x); ax.set_xticklabels([str(g) for g in group_names])
        ax.set_ylim(0, 1.05)
        if grid:
            ax.grid(True, axis="y", alpha=grid_alpha)
        ax.legend()
        apply_theme(ax, theme)
    return ax


def per_segment_metric_bar_interactive(
    y_true: ArrayLike, y_pred: ArrayLike, groups: ArrayLike,
    metrics: Sequence[str] = ("accuracy", "f1", "tpr", "fpr"),
    title: Optional[str] = None, height: int = 600, width: int = 900,
    template: str = "plotly",
) -> PlotlyFigure:
    y_true = np.asarray(y_true).astype(int)
    y_pred = np.asarray(y_pred).astype(int)
    groups = np.asarray(groups)
    group_names = sorted(np.unique(groups).tolist())
    title = title or "Metrics per segment"
    fig = go.Figure()
    for m in metrics:
        ms = _segment_metrics(y_true, y_pred, groups, m)
        fig.add_trace(go.Bar(name=m, x=[str(g) for g in group_names],
                             y=[ms[g] for g in group_names]))
    fig.update_layout(barmode="group", title=title, xaxis_title="Segment",
                      yaxis_title="Score", template=template,
                      height=height, width=width, yaxis=dict(range=[0, 1.05]))
    return fig


def fairness_disparity_heatmap_static(
    y_true: ArrayLike, y_pred: ArrayLike, groups: ArrayLike,
    metrics: Sequence[str] = ("tpr", "fpr", "precision", "selection_rate"),
    title: Optional[str] = None, figsize: FigureSize = (9, 5),
    cmap: str = "RdBu_r", theme: str = "default", dpi: int = 100,
    style: str = "default",
) -> MatplotlibAxes:
    """Heatmap of metric values per group, centered on the cross-group mean.

    Cells coloured by deviation from the population mean (red = above, blue = below).
    """
    y_true = np.asarray(y_true).astype(int)
    y_pred = np.asarray(y_pred).astype(int)
    groups = np.asarray(groups)
    group_names = sorted(np.unique(groups).tolist())
    data = np.zeros((len(metrics), len(group_names)))
    for i, m in enumerate(metrics):
        ms = _segment_metrics(y_true, y_pred, groups, m)
        row = np.array([ms[g] for g in group_names])
        data[i] = row - row.mean()
    vmax = float(np.abs(data).max() or 1e-3)
    title = title or "Fairness disparity (deviation from population mean)"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Segment", ylabel="Metric",
                             figsize=figsize)
        fig.set_dpi(dpi)
        im = ax.imshow(data, cmap=cmap, vmin=-vmax, vmax=vmax, aspect="auto")
        ax.set_xticks(range(len(group_names)))
        ax.set_xticklabels([str(g) for g in group_names])
        ax.set_yticks(range(len(metrics)))
        ax.set_yticklabels(list(metrics))
        for i in range(len(metrics)):
            for j in range(len(group_names)):
                ax.text(j, i, f"{data[i, j]:+.2f}", ha="center", va="center",
                        fontsize=9)
        fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
        apply_theme(ax, theme)
    return ax


def fairness_disparity_heatmap_interactive(
    y_true: ArrayLike, y_pred: ArrayLike, groups: ArrayLike,
    metrics: Sequence[str] = ("tpr", "fpr", "precision", "selection_rate"),
    title: Optional[str] = None, height: int = 500, width: int = 800,
    template: str = "plotly", colorscale: str = "RdBu",
) -> PlotlyFigure:
    y_true = np.asarray(y_true).astype(int)
    y_pred = np.asarray(y_pred).astype(int)
    groups = np.asarray(groups)
    group_names = sorted(np.unique(groups).tolist())
    data = np.zeros((len(metrics), len(group_names)))
    for i, m in enumerate(metrics):
        ms = _segment_metrics(y_true, y_pred, groups, m)
        row = np.array([ms[g] for g in group_names])
        data[i] = row - row.mean()
    vmax = float(np.abs(data).max() or 1e-3)
    fig = go.Figure(go.Heatmap(z=data, x=[str(g) for g in group_names],
                               y=list(metrics), colorscale=colorscale,
                               zmin=-vmax, zmax=vmax,
                               text=[[f"{v:+.2f}" for v in row] for row in data],
                               texttemplate="%{text}"))
    fig.update_layout(title=title or "Fairness disparity",
                      template=template, height=height, width=width)
    return fig


def _binary_roc(y_true: np.ndarray, y_score: np.ndarray):
    order = np.argsort(-y_score)
    yt = y_true[order]
    tps = np.cumsum(yt == 1); fps = np.cumsum(yt == 0)
    P = max(int((y_true == 1).sum()), 1); N = max(int((y_true == 0).sum()), 1)
    return np.concatenate([[0], fps / N, [1]]), np.concatenate([[0], tps / P, [1]])


def segment_roc_overlay_static(
    y_true: ArrayLike, y_score: ArrayLike, groups: ArrayLike,
    title: Optional[str] = None, figsize: FigureSize = (9, 6),
    grid: bool = True, grid_alpha: float = 0.3, theme: str = "default",
    dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """ROC curves overlaid per subgroup to expose performance disparity."""
    y_true = np.asarray(y_true).astype(int)
    y_score = np.asarray(y_score, dtype=float)
    groups = np.asarray(groups)
    group_names = sorted(np.unique(groups).tolist())
    title = title or "ROC per segment"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="False Positive Rate",
                             ylabel="True Positive Rate", figsize=figsize)
        fig.set_dpi(dpi)
        for g in group_names:
            mask = groups == g
            fpr, tpr = _binary_roc(y_true[mask], y_score[mask])
            ax.plot(fpr, tpr, linewidth=2, label=str(g))
        ax.plot([0, 1], [0, 1], color="grey", linestyle="--")
        ax.set_xlim(0, 1); ax.set_ylim(0, 1.02)
        if grid:
            ax.grid(True, alpha=grid_alpha)
        ax.legend()
        apply_theme(ax, theme)
    return ax


def segment_roc_overlay_interactive(
    y_true: ArrayLike, y_score: ArrayLike, groups: ArrayLike,
    title: Optional[str] = None, height: int = 600, width: int = 700,
    template: str = "plotly",
) -> PlotlyFigure:
    y_true = np.asarray(y_true).astype(int)
    y_score = np.asarray(y_score, dtype=float)
    groups = np.asarray(groups)
    group_names = sorted(np.unique(groups).tolist())
    fig = go.Figure()
    for g in group_names:
        mask = groups == g
        fpr, tpr = _binary_roc(y_true[mask], y_score[mask])
        fig.add_trace(go.Scatter(x=fpr, y=tpr, mode="lines", name=str(g)))
    fig.add_trace(go.Scatter(x=[0, 1], y=[0, 1], mode="lines",
                             line=dict(color="grey", dash="dash"),
                             showlegend=False))
    fig.update_layout(title=title or "ROC per segment", template=template,
                      height=height, width=width,
                      xaxis=dict(title="FPR", range=[0, 1]),
                      yaxis=dict(title="TPR", range=[0, 1.02]))
    return fig


def segment_calibration_overlay_static(
    y_true: ArrayLike, y_prob: ArrayLike, groups: ArrayLike, n_bins: int = 10,
    strategy: str = "uniform", title: Optional[str] = None,
    figsize: FigureSize = (9, 6), grid: bool = True, grid_alpha: float = 0.3,
    theme: str = "default", dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Reliability diagrams overlaid per subgroup."""
    y_true = np.asarray(y_true).astype(int)
    y_prob = np.asarray(y_prob, dtype=float)
    groups = np.asarray(groups)
    group_names = sorted(np.unique(groups).tolist())
    title = title or "Calibration per segment"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Mean predicted probability",
                             ylabel="Fraction of positives", figsize=figsize)
        fig.set_dpi(dpi)
        ax.plot([0, 1], [0, 1], "--", color="grey", label="perfect")
        for g in group_names:
            mask = groups == g
            mp, fp, _ = _bin_calibration(y_true[mask], y_prob[mask], n_bins, strategy)
            ax.plot(mp, fp, "o-", linewidth=2, label=str(g))
        ax.set_xlim(0, 1); ax.set_ylim(0, 1)
        if grid:
            ax.grid(True, alpha=grid_alpha)
        ax.legend()
        apply_theme(ax, theme)
    return ax


def segment_calibration_overlay_interactive(
    y_true: ArrayLike, y_prob: ArrayLike, groups: ArrayLike, n_bins: int = 10,
    strategy: str = "uniform", title: Optional[str] = None, height: int = 600,
    width: int = 700, template: str = "plotly",
) -> PlotlyFigure:
    y_true = np.asarray(y_true).astype(int)
    y_prob = np.asarray(y_prob, dtype=float)
    groups = np.asarray(groups)
    group_names = sorted(np.unique(groups).tolist())
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[0, 1], y=[0, 1], mode="lines",
                             line=dict(color="grey", dash="dash"), name="perfect"))
    for g in group_names:
        mask = groups == g
        mp, fp, _ = _bin_calibration(y_true[mask], y_prob[mask], n_bins, strategy)
        fig.add_trace(go.Scatter(x=mp, y=fp, mode="lines+markers", name=str(g)))
    fig.update_layout(title=title or "Calibration per segment", template=template,
                      height=height, width=width,
                      xaxis=dict(range=[0, 1]), yaxis=dict(range=[0, 1]))
    return fig
