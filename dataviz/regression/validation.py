"""Validation / training-history visualizations."""

from __future__ import annotations

from typing import Mapping, Optional, Sequence

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from ..types import ArrayLike, FigureSize, MatplotlibAxes, MatrixLike, PlotlyFigure
from ..utils import setup_plot, apply_theme
from .helpers import _as_array


def _mean_band(values: np.ndarray):
    if values.ndim == 1:
        return values, None
    return values.mean(axis=1), values.std(axis=1)


# ---------------------------------------------------------------------------
# Validation curve
# ---------------------------------------------------------------------------

def validation_curve_static(
    param_values: ArrayLike,
    train_scores: MatrixLike,
    test_scores: MatrixLike,
    param_name: str = "param",
    score_name: str = "Score",
    log_x: bool = False,
    title: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    train_color: str = "#4c78a8",
    test_color: str = "#e45756",
    band_alpha: float = 0.2,
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Train/validation score curves vs a single hyperparameter."""
    x = _as_array(param_values)
    train = np.asarray(train_scores, dtype=float)
    test = np.asarray(test_scores, dtype=float)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Validation Curve",
                             xlabel=param_name, ylabel=score_name, figsize=figsize)
        fig.set_dpi(dpi)
        for arr, color, label in ((train, train_color, "Train"),
                                  (test, test_color, "Validation")):
            mean, std = _mean_band(arr)
            ax.plot(x, mean, color=color, marker="o", linewidth=2,
                    label=label, **kwargs)
            if std is not None:
                ax.fill_between(x, mean - std, mean + std, color=color,
                                alpha=band_alpha)
        if log_x:
            ax.set_xscale("log")
        ax.legend()
        if grid:
            ax.grid(True, alpha=grid_alpha)
        apply_theme(ax, theme)
    return ax


def validation_curve_interactive(
    param_values: ArrayLike,
    train_scores: MatrixLike,
    test_scores: MatrixLike,
    param_name: str = "param",
    score_name: str = "Score",
    log_x: bool = False,
    title: Optional[str] = None,
    train_color: str = "#4c78a8",
    test_color: str = "#e45756",
    template: str = "plotly",
    height: int = 600,
    width: int = 1000,
    **kwargs,
) -> PlotlyFigure:
    """Interactive validation curve."""
    x = _as_array(param_values)
    train = np.asarray(train_scores, dtype=float)
    test = np.asarray(test_scores, dtype=float)
    fig = go.Figure()
    for arr, color, label in ((train, train_color, "Train"),
                              (test, test_color, "Validation")):
        mean, std = _mean_band(arr)
        fig.add_trace(go.Scatter(x=x, y=mean, mode="lines+markers",
                                 line=dict(color=color, width=2),
                                 name=label, **kwargs))
        if std is not None:
            fig.add_trace(go.Scatter(
                x=np.concatenate([x, x[::-1]]),
                y=np.concatenate([mean + std, (mean - std)[::-1]]),
                fill="toself", fillcolor=color, opacity=0.18,
                line=dict(width=0), showlegend=False, name=f"{label} band",
            ))
    fig.update_layout(title=title or "Validation Curve",
                      xaxis_title=param_name, yaxis_title=score_name,
                      xaxis_type="log" if log_x else "linear",
                      template=template, height=height, width=width)
    return fig


# ---------------------------------------------------------------------------
# Training history
# ---------------------------------------------------------------------------

def training_history_static(
    history: Mapping[str, Sequence[float]],
    title: Optional[str] = None,
    figsize: FigureSize = (11, 6),
    cmap: str = "tab10",
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Plot training-history curves keyed by metric name (e.g. loss, val_loss)."""
    cmap_obj = plt.get_cmap(cmap)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Training History",
                             xlabel="Epoch", ylabel="Value", figsize=figsize)
        fig.set_dpi(dpi)
        for i, (key, vals) in enumerate(history.items()):
            arr = np.asarray(vals, dtype=float)
            ax.plot(np.arange(1, arr.size + 1), arr,
                    color=cmap_obj(i % cmap_obj.N),
                    linewidth=2, marker="o", label=key, **kwargs)
        ax.legend()
        if grid:
            ax.grid(True, alpha=grid_alpha)
        apply_theme(ax, theme)
    return ax


def training_history_interactive(
    history: Mapping[str, Sequence[float]],
    title: Optional[str] = None,
    template: str = "plotly",
    height: int = 600,
    width: int = 1100,
    **kwargs,
) -> PlotlyFigure:
    """Interactive training-history plot."""
    fig = go.Figure()
    for key, vals in history.items():
        arr = np.asarray(vals, dtype=float)
        fig.add_trace(go.Scatter(x=np.arange(1, arr.size + 1), y=arr,
                                 mode="lines+markers", name=key, **kwargs))
    fig.update_layout(title=title or "Training History",
                      xaxis_title="Epoch", yaxis_title="Value",
                      template=template, height=height, width=width)
    return fig


# ---------------------------------------------------------------------------
# Cross-validation score plot
# ---------------------------------------------------------------------------

def cv_score_plot_static(
    fold_scores: ArrayLike,
    model_name: Optional[str] = None,
    title: Optional[str] = None,
    figsize: FigureSize = (10, 5),
    color: str = "#4c78a8",
    mean_color: str = "#e45756",
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Bar chart of per-fold cross-validation scores with mean reference line."""
    scores = _as_array(fold_scores)
    folds = np.arange(1, scores.size + 1)
    mean = float(scores.mean())
    label = model_name or "Model"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or f"CV Scores ({label})",
                             xlabel="Fold", ylabel="Score", figsize=figsize)
        fig.set_dpi(dpi)
        ax.bar(folds, scores, color=color, alpha=0.85, **kwargs)
        ax.axhline(mean, color=mean_color, linestyle="--", linewidth=2,
                   label=f"Mean={mean:.3g}")
        ax.legend()
        if grid:
            ax.grid(True, alpha=grid_alpha, axis="y")
        apply_theme(ax, theme)
    return ax


def cv_score_plot_interactive(
    fold_scores: ArrayLike,
    model_name: Optional[str] = None,
    title: Optional[str] = None,
    color: str = "#4c78a8",
    mean_color: str = "#e45756",
    template: str = "plotly",
    height: int = 500,
    width: int = 900,
    **kwargs,
) -> PlotlyFigure:
    """Interactive cross-validation per-fold score chart."""
    scores = _as_array(fold_scores)
    folds = np.arange(1, scores.size + 1)
    mean = float(scores.mean())
    label = model_name or "Model"
    fig = go.Figure()
    fig.add_trace(go.Bar(x=folds, y=scores, marker_color=color,
                         name="Fold score", **kwargs))
    fig.add_hline(y=mean, line_dash="dash", line_color=mean_color,
                  annotation_text=f"Mean={mean:.3g}")
    fig.update_layout(title=title or f"CV Scores ({label})",
                      xaxis_title="Fold", yaxis_title="Score",
                      template=template, height=height, width=width)
    return fig


# ---------------------------------------------------------------------------
# Bias-variance decomposition plot
# ---------------------------------------------------------------------------

def bias_variance_plot_static(
    complexity: ArrayLike,
    bias_squared: ArrayLike,
    variance: ArrayLike,
    noise: Optional[ArrayLike] = None,
    title: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    bias_color: str = "#4c78a8",
    variance_color: str = "#e45756",
    noise_color: str = "#54a24b",
    total_color: str = "#444",
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Plot bias², variance, optional noise, and total error vs model complexity."""
    x = _as_array(complexity)
    b = _as_array(bias_squared)
    v = _as_array(variance)
    n = _as_array(noise) if noise is not None else np.zeros_like(x)
    total = b + v + n
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Bias-Variance Decomposition",
                             xlabel="Model complexity", ylabel="Error",
                             figsize=figsize)
        fig.set_dpi(dpi)
        ax.plot(x, b, color=bias_color, linewidth=2, label="Bias²", **kwargs)
        ax.plot(x, v, color=variance_color, linewidth=2, label="Variance")
        if noise is not None:
            ax.plot(x, n, color=noise_color, linewidth=2, label="Noise")
        ax.plot(x, total, color=total_color, linewidth=2, linestyle="--",
                label="Total")
        ax.legend()
        if grid:
            ax.grid(True, alpha=grid_alpha)
        apply_theme(ax, theme)
    return ax


def bias_variance_plot_interactive(
    complexity: ArrayLike,
    bias_squared: ArrayLike,
    variance: ArrayLike,
    noise: Optional[ArrayLike] = None,
    title: Optional[str] = None,
    bias_color: str = "#4c78a8",
    variance_color: str = "#e45756",
    noise_color: str = "#54a24b",
    total_color: str = "#444",
    template: str = "plotly",
    height: int = 600,
    width: int = 1000,
    **kwargs,
) -> PlotlyFigure:
    """Interactive bias-variance decomposition plot."""
    x = _as_array(complexity)
    b = _as_array(bias_squared)
    v = _as_array(variance)
    n = _as_array(noise) if noise is not None else np.zeros_like(x)
    total = b + v + n
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=b, mode="lines",
                             line=dict(color=bias_color, width=2),
                             name="Bias²", **kwargs))
    fig.add_trace(go.Scatter(x=x, y=v, mode="lines",
                             line=dict(color=variance_color, width=2),
                             name="Variance"))
    if noise is not None:
        fig.add_trace(go.Scatter(x=x, y=n, mode="lines",
                                 line=dict(color=noise_color, width=2),
                                 name="Noise"))
    fig.add_trace(go.Scatter(x=x, y=total, mode="lines",
                             line=dict(color=total_color, width=2, dash="dash"),
                             name="Total"))
    fig.update_layout(title=title or "Bias-Variance Decomposition",
                      xaxis_title="Model complexity", yaxis_title="Error",
                      template=template, height=height, width=width)
    return fig


validation_curve = validation_curve_static
training_history = training_history_static
cv_score_plot = cv_score_plot_static
bias_variance_plot = bias_variance_plot_static
