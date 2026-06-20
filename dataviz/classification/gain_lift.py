"""Gain, lift and cumulative-accuracy-profile (CAP) charts."""

from __future__ import annotations

from typing import Optional

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from ..types import ArrayLike, FigureSize, MatplotlibAxes, PlotlyFigure
from ..utils import setup_plot, apply_theme


def _gain_arrays(y_true: np.ndarray, y_prob: np.ndarray):
    order = np.argsort(-y_prob)
    y_sorted = y_true[order].astype(int)
    n = y_sorted.size
    cum_positive = np.cumsum(y_sorted)
    total_positive = max(int(y_sorted.sum()), 1)
    pct_population = np.arange(1, n + 1) / n
    pct_positive_captured = cum_positive / total_positive
    return pct_population, pct_positive_captured


def gain_chart_static(
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
    """Cumulative gains chart: fraction of positives captured vs sample fraction.

    The diagonal represents a random model; the curve close to the top-left
    indicates an effective classifier.
    """
    y_true = np.asarray(y_true).astype(int)
    y_prob = np.asarray(y_prob, dtype=float)
    pct_pop, pct_pos = _gain_arrays(y_true, y_prob)
    title = title or "Cumulative gains chart"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Fraction of population",
                             ylabel="Fraction of positives captured",
                             figsize=figsize)
        fig.set_dpi(dpi)
        ax.plot(pct_pop, pct_pos, linewidth=2, label="model")
        ax.plot([0, 1], [0, 1], color="grey", linestyle="--", label="random")
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1.02)
        if grid:
            ax.grid(True, alpha=grid_alpha)
        ax.legend(loc="lower right")
        apply_theme(ax, theme)
    return ax


def gain_chart_interactive(
    y_true: ArrayLike,
    y_prob: ArrayLike,
    title: Optional[str] = None,
    height: int = 600,
    width: int = 700,
    template: str = "plotly",
) -> PlotlyFigure:
    """Interactive cumulative gains chart."""
    y_true = np.asarray(y_true).astype(int)
    y_prob = np.asarray(y_prob, dtype=float)
    pct_pop, pct_pos = _gain_arrays(y_true, y_prob)
    title = title or "Cumulative gains chart"
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=pct_pop, y=pct_pos, mode="lines", name="model"))
    fig.add_trace(go.Scatter(x=[0, 1], y=[0, 1], mode="lines",
                             line=dict(color="grey", dash="dash"), name="random"))
    fig.update_layout(title=title, xaxis_title="Fraction of population",
                      yaxis_title="Fraction of positives captured",
                      template=template, height=height, width=width,
                      xaxis=dict(range=[0, 1]), yaxis=dict(range=[0, 1.02]))
    return fig


def lift_chart_static(
    y_true: ArrayLike,
    y_prob: ArrayLike,
    n_bins: int = 10,
    title: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    color: Optional[str] = None,
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
) -> MatplotlibAxes:
    """Decile lift chart: model precision per decile divided by base rate."""
    y_true = np.asarray(y_true).astype(int)
    y_prob = np.asarray(y_prob, dtype=float)
    order = np.argsort(-y_prob)
    y_sorted = y_true[order]
    base = max(y_true.mean(), 1e-12)
    splits = np.array_split(y_sorted, n_bins)
    deciles = np.arange(1, n_bins + 1)
    lift = np.array([s.mean() / base if s.size else 0.0 for s in splits])
    title = title or "Decile lift chart"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Decile (1 = top scores)",
                             ylabel="Lift over baseline", figsize=figsize)
        fig.set_dpi(dpi)
        ax.bar(deciles, lift, color=color if color else "#1f77b4")
        ax.axhline(1.0, color="grey", linestyle="--")
        for i, v in enumerate(lift):
            ax.text(deciles[i], v, f"{v:.2f}", ha="center", va="bottom", fontsize=9)
        if grid:
            ax.grid(True, axis="y", alpha=grid_alpha)
        apply_theme(ax, theme)
    return ax


def lift_chart_interactive(
    y_true: ArrayLike,
    y_prob: ArrayLike,
    n_bins: int = 10,
    title: Optional[str] = None,
    height: int = 600,
    width: int = 800,
    template: str = "plotly",
) -> PlotlyFigure:
    """Interactive decile lift chart."""
    y_true = np.asarray(y_true).astype(int)
    y_prob = np.asarray(y_prob, dtype=float)
    order = np.argsort(-y_prob)
    y_sorted = y_true[order]
    base = max(y_true.mean(), 1e-12)
    splits = np.array_split(y_sorted, n_bins)
    lift = [s.mean() / base if s.size else 0.0 for s in splits]
    title = title or "Decile lift chart"
    fig = go.Figure(go.Bar(x=list(range(1, n_bins + 1)), y=lift,
                           text=[f"{v:.2f}" for v in lift], textposition="outside"))
    fig.add_hline(y=1.0, line_dash="dash")
    fig.update_layout(title=title, xaxis_title="Decile (1 = top scores)",
                      yaxis_title="Lift over baseline", template=template,
                      height=height, width=width)
    return fig


def cumulative_accuracy_profile_static(
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
    """Cumulative accuracy profile (CAP) and the accuracy ratio (AR).

    AR = (area between model and random) / (area between perfect and random).
    """
    y_true = np.asarray(y_true).astype(int)
    y_prob = np.asarray(y_prob, dtype=float)
    pct_pop, pct_pos = _gain_arrays(y_true, y_prob)
    prevalence = float(y_true.mean())
    perfect_x = np.array([0.0, prevalence, 1.0])
    perfect_y = np.array([0.0, 1.0, 1.0])
    area_model = float(np.trapezoid(pct_pos, pct_pop))
    area_perfect = float(np.trapezoid(perfect_y, perfect_x))
    accuracy_ratio = (area_model - 0.5) / (area_perfect - 0.5 + 1e-12)
    title = title or f"CAP (AR = {accuracy_ratio:.3f})"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Fraction of population",
                             ylabel="Fraction of positives captured",
                             figsize=figsize)
        fig.set_dpi(dpi)
        ax.plot(pct_pop, pct_pos, linewidth=2, label="model")
        ax.plot(perfect_x, perfect_y, color="green", linestyle="--", label="perfect")
        ax.plot([0, 1], [0, 1], color="grey", linestyle=":", label="random")
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1.02)
        if grid:
            ax.grid(True, alpha=grid_alpha)
        ax.legend(loc="lower right")
        apply_theme(ax, theme)
    return ax


def cumulative_accuracy_profile_interactive(
    y_true: ArrayLike,
    y_prob: ArrayLike,
    title: Optional[str] = None,
    height: int = 600,
    width: int = 700,
    template: str = "plotly",
) -> PlotlyFigure:
    """Interactive CAP curve."""
    y_true = np.asarray(y_true).astype(int)
    y_prob = np.asarray(y_prob, dtype=float)
    pct_pop, pct_pos = _gain_arrays(y_true, y_prob)
    prevalence = float(y_true.mean())
    perfect_x = [0.0, prevalence, 1.0]
    perfect_y = [0.0, 1.0, 1.0]
    title = title or "Cumulative accuracy profile"
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=pct_pop, y=pct_pos, mode="lines", name="model"))
    fig.add_trace(go.Scatter(x=perfect_x, y=perfect_y, mode="lines",
                             line=dict(color="green", dash="dash"), name="perfect"))
    fig.add_trace(go.Scatter(x=[0, 1], y=[0, 1], mode="lines",
                             line=dict(color="grey", dash="dot"), name="random"))
    fig.update_layout(title=title, xaxis_title="Fraction of population",
                      yaxis_title="Fraction of positives captured",
                      template=template, height=height, width=width,
                      xaxis=dict(range=[0, 1]), yaxis=dict(range=[0, 1.02]))
    return fig
