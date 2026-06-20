"""Calibration, probability distribution and Brier score visualizations."""

from __future__ import annotations

from typing import Mapping, Optional, Sequence

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from ..types import ArrayLike, FigureSize, MatplotlibAxes, PlotlyFigure
from ..utils import setup_plot, apply_theme


def _bin_calibration(
    y_true: np.ndarray, y_prob: np.ndarray, n_bins: int, strategy: str
):
    if strategy == "quantile":
        bins = np.quantile(y_prob, np.linspace(0, 1, n_bins + 1))
        bins[0], bins[-1] = 0.0, 1.0 + 1e-9
    else:
        bins = np.linspace(0, 1, n_bins + 1)
    idx = np.clip(np.digitize(y_prob, bins, right=False) - 1, 0, n_bins - 1)
    mean_pred, frac_pos, counts = [], [], []
    for b in range(n_bins):
        mask = idx == b
        if mask.any():
            mean_pred.append(float(y_prob[mask].mean()))
            frac_pos.append(float(y_true[mask].mean()))
            counts.append(int(mask.sum()))
    return np.array(mean_pred), np.array(frac_pos), np.array(counts)


def calibration_curve_static(
    y_true: ArrayLike,
    y_prob: ArrayLike,
    n_bins: int = 10,
    strategy: str = "uniform",
    title: Optional[str] = None,
    figsize: FigureSize = (8, 6),
    color: Optional[str] = None,
    linewidth: float = 2.0,
    marker: str = "o",
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
) -> MatplotlibAxes:
    """Reliability diagram comparing predicted probabilities to observed frequencies.

    Args:
        y_true: Binary ground-truth labels in ``{0, 1}``.
        y_prob: Predicted positive-class probabilities in ``[0, 1]``.
        n_bins: Number of probability bins.
        strategy: ``"uniform"`` for equal-width bins or ``"quantile"`` for equal-count bins.
    """
    y_true = np.asarray(y_true).astype(int)
    y_prob = np.asarray(y_prob, dtype=float)
    mean_pred, frac_pos, _ = _bin_calibration(y_true, y_prob, n_bins, strategy)
    title = title or "Calibration curve"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Mean predicted probability",
                             ylabel="Fraction of positives", figsize=figsize)
        fig.set_dpi(dpi)
        ax.plot([0, 1], [0, 1], color="grey", linestyle="--", label="perfect")
        ax.plot(mean_pred, frac_pos, marker=marker, color=color,
                linewidth=linewidth, label="model")
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        if grid:
            ax.grid(True, alpha=grid_alpha)
        ax.legend()
        apply_theme(ax, theme)
    return ax


def calibration_curve_interactive(
    y_true: ArrayLike,
    y_prob: ArrayLike,
    n_bins: int = 10,
    strategy: str = "uniform",
    title: Optional[str] = None,
    height: int = 600,
    width: int = 700,
    template: str = "plotly",
) -> PlotlyFigure:
    """Interactive reliability diagram."""
    y_true = np.asarray(y_true).astype(int)
    y_prob = np.asarray(y_prob, dtype=float)
    mean_pred, frac_pos, counts = _bin_calibration(y_true, y_prob, n_bins, strategy)
    title = title or "Calibration curve"
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[0, 1], y=[0, 1], mode="lines",
                             line=dict(color="grey", dash="dash"), name="perfect"))
    fig.add_trace(go.Scatter(x=mean_pred, y=frac_pos, mode="lines+markers",
                             name="model",
                             hovertext=[f"n={c}" for c in counts]))
    fig.update_layout(title=title, xaxis_title="Mean predicted probability",
                      yaxis_title="Fraction of positives",
                      template=template, height=height, width=width,
                      xaxis=dict(range=[0, 1]), yaxis=dict(range=[0, 1]))
    return fig


def probability_histogram_static(
    y_true: ArrayLike,
    y_prob: ArrayLike,
    bins: int = 30,
    title: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    alpha: float = 0.6,
    positive_label: str = "positive",
    negative_label: str = "negative",
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
) -> MatplotlibAxes:
    """Histogram of predicted probabilities split by true class.

    Useful to inspect class separability: well-separated peaks indicate a
    discriminative classifier.
    """
    y_true = np.asarray(y_true).astype(int)
    y_prob = np.asarray(y_prob, dtype=float)
    title = title or "Predicted probability by class"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Predicted probability",
                             ylabel="Count", figsize=figsize)
        fig.set_dpi(dpi)
        edges = np.linspace(0, 1, bins + 1)
        ax.hist(y_prob[y_true == 0], bins=edges, alpha=alpha,
                label=negative_label, color="tab:blue")
        ax.hist(y_prob[y_true == 1], bins=edges, alpha=alpha,
                label=positive_label, color="tab:orange")
        if grid:
            ax.grid(True, alpha=grid_alpha)
        ax.legend()
        apply_theme(ax, theme)
    return ax


def probability_histogram_interactive(
    y_true: ArrayLike,
    y_prob: ArrayLike,
    bins: int = 30,
    title: Optional[str] = None,
    height: int = 600,
    width: int = 800,
    template: str = "plotly",
) -> PlotlyFigure:
    """Interactive histogram of predicted probabilities split by true class."""
    y_true = np.asarray(y_true).astype(int)
    y_prob = np.asarray(y_prob, dtype=float)
    title = title or "Predicted probability by class"
    fig = go.Figure()
    fig.add_trace(go.Histogram(x=y_prob[y_true == 0], nbinsx=bins, name="negative",
                               opacity=0.6))
    fig.add_trace(go.Histogram(x=y_prob[y_true == 1], nbinsx=bins, name="positive",
                               opacity=0.6))
    fig.update_layout(title=title, barmode="overlay",
                      xaxis_title="Predicted probability", yaxis_title="Count",
                      template=template, height=height, width=width)
    return fig


def probability_density_static(
    y_true: ArrayLike,
    y_prob: ArrayLike,
    title: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    bandwidth: Optional[float] = None,
    grid_size: int = 200,
    fill: bool = True,
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
) -> MatplotlibAxes:
    """Per-class kernel density estimate of predicted probabilities."""
    y_true = np.asarray(y_true).astype(int)
    y_prob = np.asarray(y_prob, dtype=float)
    title = title or "Predicted probability density by class"
    grid_x = np.linspace(0, 1, grid_size)

    def _kde(x):
        if x.size < 2:
            return np.zeros_like(grid_x)
        bw = bandwidth or 1.06 * x.std(ddof=1) * (x.size ** (-1 / 5))
        bw = max(bw, 1e-3)
        diff = (grid_x[:, None] - x[None, :]) / bw
        return np.exp(-0.5 * diff ** 2).sum(axis=1) / (x.size * bw * np.sqrt(2 * np.pi))

    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Predicted probability",
                             ylabel="Density", figsize=figsize)
        fig.set_dpi(dpi)
        for label, color, name in [(0, "tab:blue", "negative"),
                                   (1, "tab:orange", "positive")]:
            y = _kde(y_prob[y_true == label])
            ax.plot(grid_x, y, color=color, linewidth=2, label=name)
            if fill:
                ax.fill_between(grid_x, y, color=color, alpha=0.2)
        if grid:
            ax.grid(True, alpha=grid_alpha)
        ax.legend()
        apply_theme(ax, theme)
    return ax


def probability_density_interactive(
    y_true: ArrayLike,
    y_prob: ArrayLike,
    title: Optional[str] = None,
    bandwidth: Optional[float] = None,
    grid_size: int = 200,
    height: int = 600,
    width: int = 800,
    template: str = "plotly",
) -> PlotlyFigure:
    """Interactive per-class KDE of predicted probabilities."""
    y_true = np.asarray(y_true).astype(int)
    y_prob = np.asarray(y_prob, dtype=float)
    title = title or "Predicted probability density by class"
    grid_x = np.linspace(0, 1, grid_size)
    fig = go.Figure()
    for label, color, name in [(0, "blue", "negative"), (1, "orange", "positive")]:
        x = y_prob[y_true == label]
        if x.size < 2:
            continue
        bw = bandwidth or 1.06 * x.std(ddof=1) * (x.size ** (-1 / 5))
        bw = max(bw, 1e-3)
        diff = (grid_x[:, None] - x[None, :]) / bw
        y = np.exp(-0.5 * diff ** 2).sum(axis=1) / (x.size * bw * np.sqrt(2 * np.pi))
        fig.add_trace(go.Scatter(x=grid_x, y=y, mode="lines", name=name,
                                 fill="tozeroy", line=dict(color=color)))
    fig.update_layout(title=title, xaxis_title="Predicted probability",
                      yaxis_title="Density", template=template,
                      height=height, width=width)
    return fig


def brier_score_bar_static(
    scores: Mapping[str, float],
    title: Optional[str] = None,
    figsize: FigureSize = (8, 5),
    color: Optional[str] = None,
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
) -> MatplotlibAxes:
    """Bar chart of Brier scores per model or per class. Lower is better."""
    title = title or "Brier score (lower is better)"
    names = list(scores.keys())
    values = list(scores.values())
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="", ylabel="Brier score",
                             figsize=figsize)
        fig.set_dpi(dpi)
        ax.bar(names, values, color=color or "tab:purple")
        for i, v in enumerate(values):
            ax.text(i, v, f"{v:.3f}", ha="center", va="bottom", fontsize=9)
        if grid:
            ax.grid(True, axis="y", alpha=grid_alpha)
        apply_theme(ax, theme)
    return ax


def brier_score_bar_interactive(
    scores: Mapping[str, float],
    title: Optional[str] = None,
    height: int = 500,
    width: int = 700,
    template: str = "plotly",
) -> PlotlyFigure:
    """Interactive bar chart of Brier scores."""
    title = title or "Brier score (lower is better)"
    fig = go.Figure(go.Bar(x=list(scores.keys()), y=list(scores.values()),
                           text=[f"{v:.3f}" for v in scores.values()],
                           textposition="outside"))
    fig.update_layout(title=title, yaxis_title="Brier score",
                      template=template, height=height, width=width)
    return fig
