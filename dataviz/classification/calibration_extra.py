"""Extra calibration / probability views."""

from __future__ import annotations

from typing import Mapping, Optional, Sequence, Tuple

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from ..types import ArrayLike, FigureSize, MatplotlibAxes, PlotlyFigure
from ..utils import setup_plot, apply_theme
from .calibration import _bin_calibration


def multiclass_calibration_curve_static(
    y_true: ArrayLike, y_prob_matrix: ArrayLike,
    labels: Optional[Sequence] = None, n_bins: int = 10,
    strategy: str = "uniform", title: Optional[str] = None,
    figsize: FigureSize = (12, 8), theme: str = "default",
    dpi: int = 100, style: str = "default",
) -> "np.ndarray":
    """One reliability panel per class (small multiples).

    Args:
        y_true: Integer class labels of shape ``(n,)``.
        y_prob_matrix: Predicted probabilities of shape ``(n, n_classes)``.
    """
    y_true = np.asarray(y_true).astype(int)
    P = np.asarray(y_prob_matrix, dtype=float)
    n_classes = P.shape[1]
    if labels is None:
        labels = list(range(n_classes))
    cols = min(3, n_classes); rows = int(np.ceil(n_classes / cols))
    title = title or "Multiclass calibration (one-vs-rest)"
    with plt.style.context(style):
        fig, axes = plt.subplots(rows, cols, figsize=figsize, dpi=dpi,
                                 squeeze=False)
        fig.suptitle(title)
        for k in range(n_classes):
            ax = axes[k // cols, k % cols]
            y_bin = (y_true == k).astype(int)
            mp, fp, _ = _bin_calibration(y_bin, P[:, k], n_bins, strategy)
            ax.plot([0, 1], [0, 1], "--", color="grey")
            ax.plot(mp, fp, "o-", linewidth=2)
            ax.set_title(f"class {labels[k]}")
            ax.set_xlim(0, 1); ax.set_ylim(0, 1)
            ax.set_xlabel("predicted"); ax.set_ylabel("observed")
            apply_theme(ax, theme)
        for k in range(n_classes, rows * cols):
            axes[k // cols, k % cols].axis("off")
        fig.tight_layout()
    return axes


def multiclass_calibration_curve_interactive(
    y_true: ArrayLike, y_prob_matrix: ArrayLike,
    labels: Optional[Sequence] = None, n_bins: int = 10,
    strategy: str = "uniform", title: Optional[str] = None,
    height: int = 700, width: int = 900, template: str = "plotly",
) -> PlotlyFigure:
    """Interactive multiclass reliability small-multiples."""
    y_true = np.asarray(y_true).astype(int)
    P = np.asarray(y_prob_matrix, dtype=float)
    n_classes = P.shape[1]
    if labels is None:
        labels = list(range(n_classes))
    cols = min(3, n_classes); rows = int(np.ceil(n_classes / cols))
    fig = make_subplots(rows=rows, cols=cols,
                        subplot_titles=[f"class {l}" for l in labels])
    for k in range(n_classes):
        r, c = k // cols + 1, k % cols + 1
        y_bin = (y_true == k).astype(int)
        mp, fp, _ = _bin_calibration(y_bin, P[:, k], n_bins, strategy)
        fig.add_trace(go.Scatter(x=[0, 1], y=[0, 1], mode="lines",
                                 line=dict(color="grey", dash="dash"),
                                 showlegend=False), row=r, col=c)
        fig.add_trace(go.Scatter(x=mp, y=fp, mode="lines+markers",
                                 showlegend=False), row=r, col=c)
    fig.update_layout(title=title or "Multiclass calibration", template=template,
                      height=height, width=width)
    return fig


def calibration_with_confidence_static(
    y_true: ArrayLike, y_prob: ArrayLike, n_bins: int = 10,
    strategy: str = "uniform", n_bootstrap: int = 500, ci: float = 0.95,
    title: Optional[str] = None, figsize: FigureSize = (9, 6),
    grid: bool = True, grid_alpha: float = 0.3, theme: str = "default",
    dpi: int = 100, style: str = "default", random_state: int = 0,
) -> MatplotlibAxes:
    """Reliability curve with bootstrap confidence bands on the observed fraction."""
    rng = np.random.default_rng(random_state)
    y_true = np.asarray(y_true).astype(int)
    y_prob = np.asarray(y_prob, dtype=float)
    n = y_true.size
    mp_obs, fp_obs, _ = _bin_calibration(y_true, y_prob, n_bins, strategy)
    boots = np.full((n_bootstrap, mp_obs.size), np.nan)
    for b in range(n_bootstrap):
        idx = rng.integers(0, n, n)
        _, fp_b, _ = _bin_calibration(y_true[idx], y_prob[idx], n_bins, strategy)
        if fp_b.size == mp_obs.size:
            boots[b] = fp_b
    alpha = (1 - ci) / 2
    lo = np.nanquantile(boots, alpha, axis=0)
    hi = np.nanquantile(boots, 1 - alpha, axis=0)
    title = title or f"Calibration with {int(ci*100)}% CI"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Mean predicted probability",
                             ylabel="Fraction of positives", figsize=figsize)
        fig.set_dpi(dpi)
        ax.plot([0, 1], [0, 1], "--", color="grey", label="perfect")
        ax.fill_between(mp_obs, lo, hi, alpha=0.25, label=f"{int(ci*100)}% CI")
        ax.plot(mp_obs, fp_obs, "o-", linewidth=2, label="model")
        ax.set_xlim(0, 1); ax.set_ylim(0, 1)
        if grid:
            ax.grid(True, alpha=grid_alpha)
        ax.legend()
        apply_theme(ax, theme)
    return ax


def calibration_with_confidence_interactive(
    y_true: ArrayLike, y_prob: ArrayLike, n_bins: int = 10,
    strategy: str = "uniform", n_bootstrap: int = 500, ci: float = 0.95,
    title: Optional[str] = None, height: int = 600, width: int = 700,
    template: str = "plotly", random_state: int = 0,
) -> PlotlyFigure:
    rng = np.random.default_rng(random_state)
    y_true = np.asarray(y_true).astype(int)
    y_prob = np.asarray(y_prob, dtype=float)
    n = y_true.size
    mp_obs, fp_obs, _ = _bin_calibration(y_true, y_prob, n_bins, strategy)
    boots = np.full((n_bootstrap, mp_obs.size), np.nan)
    for b in range(n_bootstrap):
        idx = rng.integers(0, n, n)
        _, fp_b, _ = _bin_calibration(y_true[idx], y_prob[idx], n_bins, strategy)
        if fp_b.size == mp_obs.size:
            boots[b] = fp_b
    alpha = (1 - ci) / 2
    lo = np.nanquantile(boots, alpha, axis=0)
    hi = np.nanquantile(boots, 1 - alpha, axis=0)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[0, 1], y=[0, 1], mode="lines",
                             line=dict(color="grey", dash="dash"), name="perfect"))
    fig.add_trace(go.Scatter(x=np.concatenate([mp_obs, mp_obs[::-1]]),
                             y=np.concatenate([hi, lo[::-1]]),
                             fill="toself", fillcolor="rgba(0,100,200,0.2)",
                             line=dict(width=0), name=f"{int(ci*100)}% CI"))
    fig.add_trace(go.Scatter(x=mp_obs, y=fp_obs, mode="lines+markers", name="model"))
    fig.update_layout(title=title or "Calibration with CI", template=template,
                      height=height, width=width,
                      xaxis=dict(range=[0, 1], title="Mean predicted probability"),
                      yaxis=dict(range=[0, 1], title="Fraction of positives"))
    return fig


def platt_isotonic_overlay_static(
    y_true: ArrayLike, y_prob: ArrayLike, n_bins: int = 15,
    title: Optional[str] = None, figsize: FigureSize = (9, 6),
    grid: bool = True, grid_alpha: float = 0.3, theme: str = "default",
    dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Overlay raw, Platt-scaled (logistic) and isotonic-regressed calibration mappings."""
    y_true = np.asarray(y_true).astype(int)
    y_prob = np.clip(np.asarray(y_prob, dtype=float), 1e-6, 1 - 1e-6)
    # Platt: logistic fit p = 1/(1+exp(-(a*logit+b))) via Newton-Raphson
    x = np.log(y_prob / (1 - y_prob))
    a, b = 1.0, 0.0
    for _ in range(50):
        z = a * x + b; p = 1.0 / (1.0 + np.exp(-z))
        g_a = ((p - y_true) * x).sum(); g_b = (p - y_true).sum()
        w = p * (1 - p) + 1e-9
        H = np.array([[(w * x * x).sum(), (w * x).sum()],
                      [(w * x).sum(), w.sum()]])
        try:
            step = np.linalg.solve(H, np.array([g_a, g_b]))
        except np.linalg.LinAlgError:
            break
        a -= step[0]; b -= step[1]
    grid_x = np.linspace(0.001, 0.999, 200)
    gx_logit = np.log(grid_x / (1 - grid_x))
    platt = 1.0 / (1.0 + np.exp(-(a * gx_logit + b)))
    # Isotonic via PAV
    order = np.argsort(y_prob); xs = y_prob[order]; ys = y_true[order].astype(float)
    iso = ys.copy(); w_iso = np.ones_like(iso)
    i = 0
    while i < iso.size - 1:
        if iso[i] > iso[i + 1]:
            new_w = w_iso[i] + w_iso[i + 1]
            new_v = (iso[i] * w_iso[i] + iso[i + 1] * w_iso[i + 1]) / new_w
            iso[i] = new_v; w_iso[i] = new_w
            iso = np.delete(iso, i + 1); w_iso = np.delete(w_iso, i + 1)
            xs = np.delete(xs, i + 1)
            if i > 0:
                i -= 1
        else:
            i += 1
    iso_curve = np.interp(grid_x, xs, iso)
    mp_obs, fp_obs, _ = _bin_calibration(y_true, y_prob, n_bins, "uniform")
    title = title or "Calibration mapping overlay"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Predicted probability",
                             ylabel="Calibrated probability", figsize=figsize)
        fig.set_dpi(dpi)
        ax.plot([0, 1], [0, 1], "--", color="grey", label="perfect")
        ax.plot(grid_x, platt, linewidth=2, label="Platt (logistic)")
        ax.plot(grid_x, iso_curve, linewidth=2, label="Isotonic")
        ax.scatter(mp_obs, fp_obs, s=30, color="black", label="binned observed")
        ax.set_xlim(0, 1); ax.set_ylim(0, 1)
        if grid:
            ax.grid(True, alpha=grid_alpha)
        ax.legend()
        apply_theme(ax, theme)
    return ax


def platt_isotonic_overlay_interactive(
    y_true: ArrayLike, y_prob: ArrayLike, n_bins: int = 15,
    title: Optional[str] = None, height: int = 600, width: int = 800,
    template: str = "plotly",
) -> PlotlyFigure:
    import matplotlib
    matplotlib.use("Agg")
    ax = platt_isotonic_overlay_static(y_true, y_prob, n_bins=n_bins)
    lines = ax.get_lines()
    title = title or "Calibration mapping overlay"
    fig = go.Figure()
    for ln in lines:
        fig.add_trace(go.Scatter(x=ln.get_xdata(), y=ln.get_ydata(), mode="lines",
                                 name=ln.get_label()))
    plt.close(ax.figure)
    fig.update_layout(title=title, template=template, height=height, width=width,
                      xaxis=dict(title="Predicted probability", range=[0, 1]),
                      yaxis=dict(title="Calibrated probability", range=[0, 1]))
    return fig


def sharpness_resolution_decomposition_static(
    y_true: ArrayLike, y_prob: ArrayLike, n_bins: int = 10,
    title: Optional[str] = None, figsize: FigureSize = (8, 5),
    theme: str = "default", dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Murphy decomposition of the Brier score into reliability, resolution, uncertainty.

    Brier = reliability - resolution + uncertainty.
    """
    y_true = np.asarray(y_true).astype(int)
    y_prob = np.asarray(y_prob, dtype=float)
    mp, fp, counts = _bin_calibration(y_true, y_prob, n_bins, "uniform")
    n = y_true.size
    o_bar = y_true.mean()
    reliability = float((counts * (mp - fp) ** 2).sum() / n)
    resolution = float((counts * (fp - o_bar) ** 2).sum() / n)
    uncertainty = float(o_bar * (1 - o_bar))
    brier = float(((y_prob - y_true) ** 2).mean())
    parts = {"Brier": brier, "Reliability": reliability,
             "Resolution": resolution, "Uncertainty": uncertainty}
    title = title or f"Brier decomposition (Brier={brier:.3f})"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="", ylabel="Score",
                             figsize=figsize)
        fig.set_dpi(dpi)
        colors = ["#444", "#d62728", "#2ca02c", "#1f77b4"]
        ax.bar(list(parts.keys()), list(parts.values()), color=colors)
        for i, v in enumerate(parts.values()):
            ax.text(i, v, f"{v:.3f}", ha="center", va="bottom", fontsize=9)
        apply_theme(ax, theme)
    return ax


def sharpness_resolution_decomposition_interactive(
    y_true: ArrayLike, y_prob: ArrayLike, n_bins: int = 10,
    title: Optional[str] = None, height: int = 500, width: int = 700,
    template: str = "plotly",
) -> PlotlyFigure:
    y_true = np.asarray(y_true).astype(int)
    y_prob = np.asarray(y_prob, dtype=float)
    mp, fp, counts = _bin_calibration(y_true, y_prob, n_bins, "uniform")
    n = y_true.size; o_bar = y_true.mean()
    reliability = float((counts * (mp - fp) ** 2).sum() / n)
    resolution = float((counts * (fp - o_bar) ** 2).sum() / n)
    uncertainty = float(o_bar * (1 - o_bar))
    brier = float(((y_prob - y_true) ** 2).mean())
    parts = {"Brier": brier, "Reliability": reliability,
             "Resolution": resolution, "Uncertainty": uncertainty}
    fig = go.Figure(go.Bar(x=list(parts.keys()), y=list(parts.values()),
                           text=[f"{v:.3f}" for v in parts.values()],
                           textposition="outside"))
    fig.update_layout(title=title or f"Brier decomposition (Brier={brier:.3f})",
                      template=template, height=height, width=width)
    return fig


def score_ecdf_by_class_static(
    y_true: ArrayLike, y_score: ArrayLike,
    labels: Optional[Sequence] = None, title: Optional[str] = None,
    figsize: FigureSize = (10, 6), grid: bool = True, grid_alpha: float = 0.3,
    theme: str = "default", dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Empirical CDF of model scores grouped by true class."""
    y_true = np.asarray(y_true); y_score = np.asarray(y_score, dtype=float)
    if labels is None:
        labels = sorted(np.unique(y_true).tolist())
    title = title or "Score ECDF by class"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Score",
                             ylabel="Cumulative proportion", figsize=figsize)
        fig.set_dpi(dpi)
        for l in labels:
            s = np.sort(y_score[y_true == l])
            if s.size == 0:
                continue
            ax.step(np.concatenate([[s.min()], s]),
                    np.concatenate([[0.0], np.arange(1, s.size + 1) / s.size]),
                    label=str(l), linewidth=2)
        ax.set_ylim(0, 1)
        if grid:
            ax.grid(True, alpha=grid_alpha)
        ax.legend()
        apply_theme(ax, theme)
    return ax


def score_ecdf_by_class_interactive(
    y_true: ArrayLike, y_score: ArrayLike,
    labels: Optional[Sequence] = None, title: Optional[str] = None,
    height: int = 600, width: int = 800, template: str = "plotly",
) -> PlotlyFigure:
    y_true = np.asarray(y_true); y_score = np.asarray(y_score, dtype=float)
    if labels is None:
        labels = sorted(np.unique(y_true).tolist())
    fig = go.Figure()
    for l in labels:
        s = np.sort(y_score[y_true == l])
        if s.size == 0:
            continue
        fig.add_trace(go.Scatter(x=s, y=np.arange(1, s.size + 1) / s.size,
                                 mode="lines", line_shape="hv", name=str(l)))
    fig.update_layout(title=title or "Score ECDF by class", xaxis_title="Score",
                      yaxis_title="Cumulative proportion", template=template,
                      height=height, width=width, yaxis=dict(range=[0, 1]))
    return fig


def score_qq_by_class_static(
    y_true: ArrayLike, y_score: ArrayLike,
    labels: Optional[Sequence] = None, n_quantiles: int = 50,
    title: Optional[str] = None, figsize: FigureSize = (8, 6),
    grid: bool = True, grid_alpha: float = 0.3, theme: str = "default",
    dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Q-Q plot of model scores: each class vs. a uniform reference distribution."""
    y_true = np.asarray(y_true); y_score = np.asarray(y_score, dtype=float)
    if labels is None:
        labels = sorted(np.unique(y_true).tolist())
    qs = np.linspace(0.01, 0.99, n_quantiles)
    title = title or "Score Q-Q vs. uniform per class"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Uniform quantile",
                             ylabel="Score quantile", figsize=figsize)
        fig.set_dpi(dpi)
        ax.plot([0, 1], [0, 1], "--", color="grey", label="reference")
        for l in labels:
            s = y_score[y_true == l]
            if s.size == 0:
                continue
            ax.plot(qs, np.quantile(s, qs), "o-", label=str(l))
        ax.set_xlim(0, 1)
        if grid:
            ax.grid(True, alpha=grid_alpha)
        ax.legend()
        apply_theme(ax, theme)
    return ax


def score_qq_by_class_interactive(
    y_true: ArrayLike, y_score: ArrayLike,
    labels: Optional[Sequence] = None, n_quantiles: int = 50,
    title: Optional[str] = None, height: int = 600, width: int = 700,
    template: str = "plotly",
) -> PlotlyFigure:
    y_true = np.asarray(y_true); y_score = np.asarray(y_score, dtype=float)
    if labels is None:
        labels = sorted(np.unique(y_true).tolist())
    qs = np.linspace(0.01, 0.99, n_quantiles)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[0, 1], y=[0, 1], mode="lines",
                             line=dict(color="grey", dash="dash"), name="reference"))
    for l in labels:
        s = y_score[y_true == l]
        if s.size == 0:
            continue
        fig.add_trace(go.Scatter(x=qs, y=np.quantile(s, qs), mode="lines+markers",
                                 name=str(l)))
    fig.update_layout(title=title or "Score Q-Q vs. uniform per class",
                      xaxis_title="Uniform quantile", yaxis_title="Score quantile",
                      template=template, height=height, width=width)
    return fig
