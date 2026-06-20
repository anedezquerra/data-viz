"""Confidence / error diagnostics."""

from __future__ import annotations

from typing import Optional, Sequence

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from ..types import ArrayLike, FigureSize, MatplotlibAxes, PlotlyFigure
from ..utils import setup_plot, apply_theme
from .threshold import _binary_counts


def confidence_by_correctness_histogram_static(
    y_true: ArrayLike, y_prob: ArrayLike, threshold: float = 0.5,
    bins: int = 30, title: Optional[str] = None,
    figsize: FigureSize = (10, 6), alpha: float = 0.6,
    grid: bool = True, grid_alpha: float = 0.3, theme: str = "default",
    dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Histogram of model confidence ``|p - 0.5| * 2`` split by correctness."""
    y_true = np.asarray(y_true).astype(int)
    y_prob = np.asarray(y_prob, dtype=float)
    y_pred = (y_prob >= threshold).astype(int)
    confidence = np.abs(y_prob - 0.5) * 2
    correct = y_pred == y_true
    title = title or "Confidence split by correctness"
    edges = np.linspace(0, 1, bins + 1)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Confidence (|2p - 1|)",
                             ylabel="Count", figsize=figsize)
        fig.set_dpi(dpi)
        ax.hist(confidence[correct], bins=edges, alpha=alpha, color="tab:green",
                label=f"correct (n={int(correct.sum())})")
        ax.hist(confidence[~correct], bins=edges, alpha=alpha, color="tab:red",
                label=f"wrong (n={int((~correct).sum())})")
        if grid:
            ax.grid(True, alpha=grid_alpha)
        ax.legend()
        apply_theme(ax, theme)
    return ax


def confidence_by_correctness_histogram_interactive(
    y_true: ArrayLike, y_prob: ArrayLike, threshold: float = 0.5,
    bins: int = 30, title: Optional[str] = None,
    height: int = 600, width: int = 800, template: str = "plotly",
) -> PlotlyFigure:
    y_true = np.asarray(y_true).astype(int)
    y_prob = np.asarray(y_prob, dtype=float)
    y_pred = (y_prob >= threshold).astype(int)
    confidence = np.abs(y_prob - 0.5) * 2
    correct = y_pred == y_true
    fig = go.Figure()
    fig.add_trace(go.Histogram(x=confidence[correct], nbinsx=bins,
                               name="correct", opacity=0.6,
                               marker_color="green"))
    fig.add_trace(go.Histogram(x=confidence[~correct], nbinsx=bins,
                               name="wrong", opacity=0.6, marker_color="red"))
    fig.update_layout(title=title or "Confidence split by correctness",
                      barmode="overlay", xaxis_title="Confidence (|2p - 1|)",
                      yaxis_title="Count", template=template,
                      height=height, width=width)
    return fig


def discrimination_threshold_dashboard_static(
    y_true: ArrayLike, y_prob: ArrayLike, n_thresholds: int = 100,
    title: Optional[str] = None, figsize: FigureSize = (10, 6),
    grid: bool = True, grid_alpha: float = 0.3, theme: str = "default",
    dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Precision / recall / F1 / queue-rate vs. threshold (Yellowbrick-style)."""
    y_true = np.asarray(y_true).astype(int)
    y_prob = np.asarray(y_prob, dtype=float)
    thresholds = np.linspace(0, 1, n_thresholds)
    counts = _binary_counts(y_true, y_prob, thresholds)
    tp, fp, tn, fn = counts.T
    p = np.divide(tp, tp + fp, out=np.zeros_like(tp), where=tp + fp > 0)
    r = np.divide(tp, tp + fn, out=np.zeros_like(tp), where=tp + fn > 0)
    f1 = np.divide(2 * p * r, p + r, out=np.zeros_like(p), where=p + r > 0)
    queue = (tp + fp) / (tp + fp + tn + fn)
    title = title or "Discrimination threshold dashboard"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Threshold", ylabel="Score",
                             figsize=figsize)
        fig.set_dpi(dpi)
        ax.plot(thresholds, p, label="precision", linewidth=2)
        ax.plot(thresholds, r, label="recall", linewidth=2)
        ax.plot(thresholds, f1, label="F1", linewidth=2)
        ax.plot(thresholds, queue, label="queue rate", linewidth=2, linestyle="--")
        best = int(np.argmax(f1))
        ax.axvline(thresholds[best], color="red", linestyle=":",
                   label=f"max F1 @ t={thresholds[best]:.2f}")
        ax.set_xlim(0, 1); ax.set_ylim(0, 1.05)
        if grid:
            ax.grid(True, alpha=grid_alpha)
        ax.legend()
        apply_theme(ax, theme)
    return ax


def discrimination_threshold_dashboard_interactive(
    y_true: ArrayLike, y_prob: ArrayLike, n_thresholds: int = 100,
    title: Optional[str] = None, height: int = 600, width: int = 800,
    template: str = "plotly",
) -> PlotlyFigure:
    y_true = np.asarray(y_true).astype(int)
    y_prob = np.asarray(y_prob, dtype=float)
    thresholds = np.linspace(0, 1, n_thresholds)
    counts = _binary_counts(y_true, y_prob, thresholds)
    tp, fp, tn, fn = counts.T
    p = np.divide(tp, tp + fp, out=np.zeros_like(tp), where=tp + fp > 0)
    r = np.divide(tp, tp + fn, out=np.zeros_like(tp), where=tp + fn > 0)
    f1 = np.divide(2 * p * r, p + r, out=np.zeros_like(p), where=p + r > 0)
    queue = (tp + fp) / (tp + fp + tn + fn)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=thresholds, y=p, mode="lines", name="precision"))
    fig.add_trace(go.Scatter(x=thresholds, y=r, mode="lines", name="recall"))
    fig.add_trace(go.Scatter(x=thresholds, y=f1, mode="lines", name="F1"))
    fig.add_trace(go.Scatter(x=thresholds, y=queue, mode="lines",
                             line=dict(dash="dash"), name="queue rate"))
    best = int(np.argmax(f1))
    fig.add_vline(x=float(thresholds[best]), line_dash="dot", line_color="red",
                  annotation_text=f"max F1 @ {thresholds[best]:.2f}")
    fig.update_layout(title=title or "Discrimination threshold dashboard",
                      xaxis_title="Threshold", yaxis_title="Score",
                      template=template, height=height, width=width,
                      xaxis=dict(range=[0, 1]), yaxis=dict(range=[0, 1.05]))
    return fig


def misclassification_cluster_heatmap_static(
    y_true: ArrayLike, y_prob: ArrayLike, n_score_bins: int = 10,
    threshold: float = 0.5, title: Optional[str] = None,
    figsize: FigureSize = (9, 5), cmap: str = "Reds",
    theme: str = "default", dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Error rate per score bin, with the bin-bias direction.

    Rows: true label, Cols: score decile. Cell = mistake rate.
    """
    y_true = np.asarray(y_true).astype(int)
    y_prob = np.asarray(y_prob, dtype=float)
    y_pred = (y_prob >= threshold).astype(int)
    edges = np.linspace(0, 1, n_score_bins + 1)
    idx = np.clip(np.digitize(y_prob, edges) - 1, 0, n_score_bins - 1)
    data = np.zeros((2, n_score_bins))
    for c in (0, 1):
        for b in range(n_score_bins):
            mask = (y_true == c) & (idx == b)
            if mask.sum() > 0:
                data[c, b] = float((y_pred[mask] != y_true[mask]).mean())
    title = title or "Mistake rate by true class and score bin"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Score bin",
                             ylabel="True class", figsize=figsize)
        fig.set_dpi(dpi)
        im = ax.imshow(data, cmap=cmap, vmin=0, vmax=1, aspect="auto")
        ax.set_xticks(range(n_score_bins))
        ax.set_xticklabels([f"{edges[i]:.1f}-{edges[i+1]:.1f}"
                             for i in range(n_score_bins)], rotation=45, ha="right")
        ax.set_yticks([0, 1]); ax.set_yticklabels(["0", "1"])
        for i in range(2):
            for j in range(n_score_bins):
                ax.text(j, i, f"{data[i, j]:.2f}", ha="center", va="center",
                        fontsize=8,
                        color="white" if data[i, j] > 0.5 else "black")
        fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
        apply_theme(ax, theme)
    return ax


def misclassification_cluster_heatmap_interactive(
    y_true: ArrayLike, y_prob: ArrayLike, n_score_bins: int = 10,
    threshold: float = 0.5, title: Optional[str] = None,
    height: int = 450, width: int = 800, template: str = "plotly",
    colorscale: str = "Reds",
) -> PlotlyFigure:
    y_true = np.asarray(y_true).astype(int)
    y_prob = np.asarray(y_prob, dtype=float)
    y_pred = (y_prob >= threshold).astype(int)
    edges = np.linspace(0, 1, n_score_bins + 1)
    idx = np.clip(np.digitize(y_prob, edges) - 1, 0, n_score_bins - 1)
    data = np.zeros((2, n_score_bins))
    for c in (0, 1):
        for b in range(n_score_bins):
            mask = (y_true == c) & (idx == b)
            if mask.sum() > 0:
                data[c, b] = float((y_pred[mask] != y_true[mask]).mean())
    fig = go.Figure(go.Heatmap(
        z=data, x=[f"{edges[i]:.1f}-{edges[i+1]:.1f}" for i in range(n_score_bins)],
        y=["0", "1"], colorscale=colorscale, zmin=0, zmax=1,
        text=[[f"{v:.2f}" for v in row] for row in data], texttemplate="%{text}"))
    fig.update_layout(title=title or "Mistake rate by true class and score bin",
                      xaxis_title="Score bin", yaxis_title="True class",
                      template=template, height=height, width=width)
    return fig


def loss_distribution_plot_static(
    y_true: ArrayLike, y_prob: ArrayLike, bins: int = 40,
    eps: float = 1e-9, title: Optional[str] = None,
    figsize: FigureSize = (10, 6), grid: bool = True, grid_alpha: float = 0.3,
    theme: str = "default", dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Per-sample log-loss distribution to surface high-loss outliers."""
    y_true = np.asarray(y_true).astype(int)
    y_prob = np.clip(np.asarray(y_prob, dtype=float), eps, 1 - eps)
    loss = -(y_true * np.log(y_prob) + (1 - y_true) * np.log(1 - y_prob))
    mean_loss = float(loss.mean())
    title = title or f"Per-sample log loss (mean={mean_loss:.3f})"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Log loss",
                             ylabel="Count", figsize=figsize)
        fig.set_dpi(dpi)
        ax.hist(loss[y_true == 0], bins=bins, alpha=0.6, color="tab:blue",
                label="negatives")
        ax.hist(loss[y_true == 1], bins=bins, alpha=0.6, color="tab:orange",
                label="positives")
        ax.axvline(mean_loss, color="red", linestyle="--",
                   label=f"mean = {mean_loss:.3f}")
        if grid:
            ax.grid(True, alpha=grid_alpha)
        ax.legend()
        apply_theme(ax, theme)
    return ax


def loss_distribution_plot_interactive(
    y_true: ArrayLike, y_prob: ArrayLike, bins: int = 40,
    eps: float = 1e-9, title: Optional[str] = None,
    height: int = 600, width: int = 800, template: str = "plotly",
) -> PlotlyFigure:
    y_true = np.asarray(y_true).astype(int)
    y_prob = np.clip(np.asarray(y_prob, dtype=float), eps, 1 - eps)
    loss = -(y_true * np.log(y_prob) + (1 - y_true) * np.log(1 - y_prob))
    mean_loss = float(loss.mean())
    fig = go.Figure()
    fig.add_trace(go.Histogram(x=loss[y_true == 0], nbinsx=bins, opacity=0.6,
                               name="negatives"))
    fig.add_trace(go.Histogram(x=loss[y_true == 1], nbinsx=bins, opacity=0.6,
                               name="positives"))
    fig.add_vline(x=mean_loss, line_dash="dash", line_color="red",
                  annotation_text=f"mean={mean_loss:.3f}")
    fig.update_layout(title=title or f"Per-sample log loss (mean={mean_loss:.3f})",
                      barmode="overlay", xaxis_title="Log loss", yaxis_title="Count",
                      template=template, height=height, width=width)
    return fig
