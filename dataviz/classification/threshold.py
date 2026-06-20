"""Threshold-based diagnostics: metric sweeps, KS, DET, cost, net-benefit."""

from __future__ import annotations

from typing import Optional, Sequence, Tuple

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from ..types import ArrayLike, FigureSize, MatplotlibAxes, PlotlyFigure
from ..utils import setup_plot, apply_theme


def _binary_counts(y_true: np.ndarray, y_prob: np.ndarray, thresholds: np.ndarray):
    y_true = y_true.astype(int)
    out = np.empty((len(thresholds), 4), dtype=float)  # tp, fp, tn, fn
    for i, t in enumerate(thresholds):
        pred = (y_prob >= t).astype(int)
        tp = float(((pred == 1) & (y_true == 1)).sum())
        fp = float(((pred == 1) & (y_true == 0)).sum())
        tn = float(((pred == 0) & (y_true == 0)).sum())
        fn = float(((pred == 0) & (y_true == 1)).sum())
        out[i] = [tp, fp, tn, fn]
    return out


def threshold_metric_curve_static(
    y_true: ArrayLike,
    y_prob: ArrayLike,
    metrics: Sequence[str] = ("precision", "recall", "f1", "accuracy"),
    n_thresholds: int = 100,
    title: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
) -> MatplotlibAxes:
    """Plot precision, recall, F1, accuracy as a function of decision threshold.

    Args:
        metrics: Any subset of ``{"precision", "recall", "f1", "accuracy",
            "specificity"}``.
    """
    y_true = np.asarray(y_true).astype(int)
    y_prob = np.asarray(y_prob, dtype=float)
    thresholds = np.linspace(0, 1, n_thresholds)
    counts = _binary_counts(y_true, y_prob, thresholds)
    tp, fp, tn, fn = counts.T
    out = {}
    out["precision"] = np.where(tp + fp > 0, tp / (tp + fp + 1e-12), 0.0)
    out["recall"] = np.where(tp + fn > 0, tp / (tp + fn + 1e-12), 0.0)
    out["f1"] = np.where((out["precision"] + out["recall"]) > 0,
                         2 * out["precision"] * out["recall"]
                         / (out["precision"] + out["recall"] + 1e-12), 0.0)
    out["accuracy"] = (tp + tn) / (tp + fp + tn + fn + 1e-12)
    out["specificity"] = np.where(tn + fp > 0, tn / (tn + fp + 1e-12), 0.0)

    title = title or "Metrics vs. decision threshold"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Threshold", ylabel="Score",
                             figsize=figsize)
        fig.set_dpi(dpi)
        for m in metrics:
            if m in out:
                ax.plot(thresholds, out[m], linewidth=2, label=m)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1.02)
        if grid:
            ax.grid(True, alpha=grid_alpha)
        ax.legend()
        apply_theme(ax, theme)
    return ax


def threshold_metric_curve_interactive(
    y_true: ArrayLike,
    y_prob: ArrayLike,
    metrics: Sequence[str] = ("precision", "recall", "f1", "accuracy"),
    n_thresholds: int = 100,
    title: Optional[str] = None,
    height: int = 600,
    width: int = 800,
    template: str = "plotly",
) -> PlotlyFigure:
    """Interactive threshold-metric sweep."""
    y_true = np.asarray(y_true).astype(int)
    y_prob = np.asarray(y_prob, dtype=float)
    thresholds = np.linspace(0, 1, n_thresholds)
    counts = _binary_counts(y_true, y_prob, thresholds)
    tp, fp, tn, fn = counts.T
    series = {
        "precision": np.where(tp + fp > 0, tp / (tp + fp + 1e-12), 0.0),
        "recall": np.where(tp + fn > 0, tp / (tp + fn + 1e-12), 0.0),
        "accuracy": (tp + tn) / (tp + fp + tn + fn + 1e-12),
        "specificity": np.where(tn + fp > 0, tn / (tn + fp + 1e-12), 0.0),
    }
    series["f1"] = np.where((series["precision"] + series["recall"]) > 0,
                            2 * series["precision"] * series["recall"]
                            / (series["precision"] + series["recall"] + 1e-12), 0.0)
    title = title or "Metrics vs. decision threshold"
    fig = go.Figure()
    for m in metrics:
        if m in series:
            fig.add_trace(go.Scatter(x=thresholds, y=series[m], mode="lines", name=m))
    fig.update_layout(title=title, xaxis_title="Threshold", yaxis_title="Score",
                      template=template, height=height, width=width,
                      xaxis=dict(range=[0, 1]), yaxis=dict(range=[0, 1.02]))
    return fig


def ks_statistic_plot_static(
    y_true: ArrayLike,
    y_prob: ArrayLike,
    title: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
) -> MatplotlibAxes:
    """Kolmogorov-Smirnov plot of cumulative score distributions per class.

    The KS statistic is the maximum vertical gap between the two CDFs and is a
    common credit-scoring discrimination measure.
    """
    y_true = np.asarray(y_true).astype(int)
    y_prob = np.asarray(y_prob, dtype=float)
    pos = np.sort(y_prob[y_true == 1])
    neg = np.sort(y_prob[y_true == 0])
    grid_x = np.linspace(0, 1, 200)
    cdf_pos = np.searchsorted(pos, grid_x, side="right") / max(pos.size, 1)
    cdf_neg = np.searchsorted(neg, grid_x, side="right") / max(neg.size, 1)
    diff = np.abs(cdf_pos - cdf_neg)
    ks = float(diff.max())
    ks_x = grid_x[int(diff.argmax())]
    title = title or f"KS plot (KS = {ks:.3f})"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Score threshold",
                             ylabel="Cumulative proportion", figsize=figsize)
        fig.set_dpi(dpi)
        ax.plot(grid_x, cdf_pos, label="positives", color="tab:orange", linewidth=2)
        ax.plot(grid_x, cdf_neg, label="negatives", color="tab:blue", linewidth=2)
        ax.vlines(ks_x, cdf_pos[int(diff.argmax())], cdf_neg[int(diff.argmax())],
                  color="black", linestyle="--", label=f"KS @ {ks_x:.2f}")
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        if grid:
            ax.grid(True, alpha=grid_alpha)
        ax.legend()
        apply_theme(ax, theme)
    return ax


def ks_statistic_plot_interactive(
    y_true: ArrayLike,
    y_prob: ArrayLike,
    title: Optional[str] = None,
    height: int = 600,
    width: int = 800,
    template: str = "plotly",
) -> PlotlyFigure:
    """Interactive KS plot."""
    y_true = np.asarray(y_true).astype(int)
    y_prob = np.asarray(y_prob, dtype=float)
    pos = np.sort(y_prob[y_true == 1])
    neg = np.sort(y_prob[y_true == 0])
    grid_x = np.linspace(0, 1, 200)
    cdf_pos = np.searchsorted(pos, grid_x, side="right") / max(pos.size, 1)
    cdf_neg = np.searchsorted(neg, grid_x, side="right") / max(neg.size, 1)
    ks = float(np.abs(cdf_pos - cdf_neg).max())
    title = title or f"KS plot (KS = {ks:.3f})"
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=grid_x, y=cdf_pos, mode="lines", name="positives"))
    fig.add_trace(go.Scatter(x=grid_x, y=cdf_neg, mode="lines", name="negatives"))
    fig.update_layout(title=title, xaxis_title="Score threshold",
                      yaxis_title="Cumulative proportion", template=template,
                      height=height, width=width)
    return fig


def det_curve_static(
    y_true: ArrayLike,
    y_prob: ArrayLike,
    title: Optional[str] = None,
    figsize: FigureSize = (8, 6),
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
) -> MatplotlibAxes:
    """Detection-error tradeoff: false negative rate vs. false positive rate.

    Plotted on a probit (Gaussian-quantile) scale, DET curves spread out the
    operating region used in detection / biometric problems.
    """
    from math import erf, sqrt
    y_true = np.asarray(y_true).astype(int)
    y_prob = np.asarray(y_prob, dtype=float)
    thresholds = np.unique(np.concatenate([[0.0, 1.0], np.linspace(0, 1, 200)]))
    counts = _binary_counts(y_true, y_prob, thresholds)
    tp, fp, tn, fn = counts.T
    fpr = np.where(fp + tn > 0, fp / (fp + tn + 1e-12), 0.0)
    fnr = np.where(tp + fn > 0, fn / (tp + fn + 1e-12), 0.0)
    fpr = np.clip(fpr, 1e-4, 1 - 1e-4)
    fnr = np.clip(fnr, 1e-4, 1 - 1e-4)

    def probit(p):
        return np.sqrt(2) * np.array([_inv_erf(2 * pp - 1) for pp in p])

    title = title or "Detection-error tradeoff (DET)"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="False Positive Rate",
                             ylabel="False Negative Rate", figsize=figsize)
        fig.set_dpi(dpi)
        ax.plot(probit(fpr), probit(fnr), linewidth=2)
        tick_p = np.array([0.001, 0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.4])
        tick_locs = probit(tick_p)
        ax.set_xticks(tick_locs)
        ax.set_xticklabels([f"{p:g}" for p in tick_p])
        ax.set_yticks(tick_locs)
        ax.set_yticklabels([f"{p:g}" for p in tick_p])
        if grid:
            ax.grid(True, alpha=grid_alpha)
        apply_theme(ax, theme)
    return ax


def _inv_erf(x: float) -> float:
    from math import log, sqrt
    a = 0.147
    sign = 1 if x >= 0 else -1
    x = min(max(x, -0.999999), 0.999999)
    ln = log(1 - x * x)
    term = 2 / (np.pi * a) + ln / 2
    return sign * np.sqrt(np.sqrt(term * term - ln / a) - term)


def det_curve_interactive(
    y_true: ArrayLike,
    y_prob: ArrayLike,
    title: Optional[str] = None,
    height: int = 600,
    width: int = 700,
    template: str = "plotly",
) -> PlotlyFigure:
    """Interactive DET curve on a linear scale (FNR vs FPR)."""
    y_true = np.asarray(y_true).astype(int)
    y_prob = np.asarray(y_prob, dtype=float)
    thresholds = np.linspace(0, 1, 200)
    counts = _binary_counts(y_true, y_prob, thresholds)
    tp, fp, tn, fn = counts.T
    fpr = np.where(fp + tn > 0, fp / (fp + tn + 1e-12), 0.0)
    fnr = np.where(tp + fn > 0, fn / (tp + fn + 1e-12), 0.0)
    title = title or "Detection-error tradeoff (DET)"
    fig = go.Figure(go.Scatter(x=fpr, y=fnr, mode="lines",
                               hovertext=[f"t={t:.2f}" for t in thresholds],
                               name="DET"))
    fig.update_layout(title=title, xaxis_title="False Positive Rate",
                      yaxis_title="False Negative Rate", template=template,
                      height=height, width=width,
                      xaxis=dict(type="log"), yaxis=dict(type="log"))
    return fig


def cost_curve_static(
    y_true: ArrayLike,
    y_prob: ArrayLike,
    cost_fp: float = 1.0,
    cost_fn: float = 1.0,
    n_thresholds: int = 200,
    title: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
) -> MatplotlibAxes:
    """Total misclassification cost vs. decision threshold.

    Marks the cost-minimising operating point.
    """
    y_true = np.asarray(y_true).astype(int)
    y_prob = np.asarray(y_prob, dtype=float)
    thresholds = np.linspace(0, 1, n_thresholds)
    counts = _binary_counts(y_true, y_prob, thresholds)
    _, fp, _, fn = counts.T
    cost = cost_fp * fp + cost_fn * fn
    best_idx = int(np.argmin(cost))
    title = title or f"Cost curve (best t = {thresholds[best_idx]:.2f})"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Threshold",
                             ylabel="Total cost", figsize=figsize)
        fig.set_dpi(dpi)
        ax.plot(thresholds, cost, linewidth=2)
        ax.axvline(thresholds[best_idx], color="red", linestyle="--",
                   label=f"argmin t={thresholds[best_idx]:.2f}")
        if grid:
            ax.grid(True, alpha=grid_alpha)
        ax.legend()
        apply_theme(ax, theme)
    return ax


def cost_curve_interactive(
    y_true: ArrayLike,
    y_prob: ArrayLike,
    cost_fp: float = 1.0,
    cost_fn: float = 1.0,
    n_thresholds: int = 200,
    title: Optional[str] = None,
    height: int = 600,
    width: int = 800,
    template: str = "plotly",
) -> PlotlyFigure:
    """Interactive cost curve."""
    y_true = np.asarray(y_true).astype(int)
    y_prob = np.asarray(y_prob, dtype=float)
    thresholds = np.linspace(0, 1, n_thresholds)
    counts = _binary_counts(y_true, y_prob, thresholds)
    _, fp, _, fn = counts.T
    cost = cost_fp * fp + cost_fn * fn
    title = title or "Cost curve"
    fig = go.Figure(go.Scatter(x=thresholds, y=cost, mode="lines", name="cost"))
    best = float(thresholds[int(np.argmin(cost))])
    fig.add_vline(x=best, line_dash="dash", line_color="red",
                  annotation_text=f"argmin={best:.2f}")
    fig.update_layout(title=title, xaxis_title="Threshold", yaxis_title="Total cost",
                      template=template, height=height, width=width)
    return fig


def net_benefit_curve_static(
    y_true: ArrayLike,
    y_prob: ArrayLike,
    n_thresholds: int = 100,
    title: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
) -> MatplotlibAxes:
    """Decision-curve analysis (net benefit vs threshold probability).

    Overlays the strategies *treat all*, *treat none* and the model.
    """
    y_true = np.asarray(y_true).astype(int)
    y_prob = np.asarray(y_prob, dtype=float)
    n = y_true.size
    thresholds = np.linspace(0.01, 0.99, n_thresholds)
    counts = _binary_counts(y_true, y_prob, thresholds)
    tp, fp, _, _ = counts.T
    nb_model = (tp - fp * (thresholds / (1 - thresholds))) / n
    prevalence = y_true.mean()
    nb_all = prevalence - (1 - prevalence) * (thresholds / (1 - thresholds))
    title = title or "Decision-curve analysis (net benefit)"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Threshold probability",
                             ylabel="Net benefit", figsize=figsize)
        fig.set_dpi(dpi)
        ax.plot(thresholds, nb_model, linewidth=2, label="model")
        ax.plot(thresholds, nb_all, linewidth=1.5, linestyle="--", label="treat all")
        ax.axhline(0, linewidth=1.5, linestyle=":", color="grey", label="treat none")
        ax.set_xlim(0, 1)
        if grid:
            ax.grid(True, alpha=grid_alpha)
        ax.legend()
        apply_theme(ax, theme)
    return ax


def net_benefit_curve_interactive(
    y_true: ArrayLike,
    y_prob: ArrayLike,
    n_thresholds: int = 100,
    title: Optional[str] = None,
    height: int = 600,
    width: int = 800,
    template: str = "plotly",
) -> PlotlyFigure:
    """Interactive decision-curve analysis."""
    y_true = np.asarray(y_true).astype(int)
    y_prob = np.asarray(y_prob, dtype=float)
    n = y_true.size
    thresholds = np.linspace(0.01, 0.99, n_thresholds)
    counts = _binary_counts(y_true, y_prob, thresholds)
    tp, fp, _, _ = counts.T
    nb_model = (tp - fp * (thresholds / (1 - thresholds))) / n
    prevalence = y_true.mean()
    nb_all = prevalence - (1 - prevalence) * (thresholds / (1 - thresholds))
    title = title or "Decision-curve analysis (net benefit)"
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=thresholds, y=nb_model, mode="lines", name="model"))
    fig.add_trace(go.Scatter(x=thresholds, y=nb_all, mode="lines",
                             line=dict(dash="dash"), name="treat all"))
    fig.add_hline(y=0, line_dash="dot", annotation_text="treat none")
    fig.update_layout(title=title, xaxis_title="Threshold probability",
                      yaxis_title="Net benefit", template=template,
                      height=height, width=width)
    return fig
