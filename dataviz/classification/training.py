"""Training diagnostics: validation curve, CV boxplot, training history."""

from __future__ import annotations

from typing import Mapping, Optional, Sequence

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from ..types import ArrayLike, FigureSize, MatplotlibAxes, PlotlyFigure
from ..utils import setup_plot, apply_theme


def validation_curve_static(
    param_values: ArrayLike, train_scores: ArrayLike, val_scores: ArrayLike,
    param_name: str = "param", title: Optional[str] = None,
    figsize: FigureSize = (10, 6), grid: bool = True, grid_alpha: float = 0.3,
    theme: str = "default", dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Train / validation score vs. hyperparameter sweep, with std bands.

    Args:
        train_scores, val_scores: Arrays of shape ``(len(param_values), n_folds)``
            or 1-D arrays of the per-value mean.
    """
    x = np.asarray(param_values)
    tr = np.asarray(train_scores, dtype=float); va = np.asarray(val_scores, dtype=float)
    if tr.ndim == 1:
        tr_mean, tr_std = tr, np.zeros_like(tr)
        va_mean, va_std = va, np.zeros_like(va)
    else:
        tr_mean, tr_std = tr.mean(axis=1), tr.std(axis=1)
        va_mean, va_std = va.mean(axis=1), va.std(axis=1)
    title = title or f"Validation curve over {param_name}"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel=param_name, ylabel="Score",
                             figsize=figsize)
        fig.set_dpi(dpi)
        ax.fill_between(x, tr_mean - tr_std, tr_mean + tr_std, alpha=0.2,
                        color="tab:blue")
        ax.plot(x, tr_mean, "o-", color="tab:blue", linewidth=2, label="train")
        ax.fill_between(x, va_mean - va_std, va_mean + va_std, alpha=0.2,
                        color="tab:orange")
        ax.plot(x, va_mean, "o-", color="tab:orange", linewidth=2, label="validation")
        if grid:
            ax.grid(True, alpha=grid_alpha)
        ax.legend()
        apply_theme(ax, theme)
    return ax


def validation_curve_interactive(
    param_values: ArrayLike, train_scores: ArrayLike, val_scores: ArrayLike,
    param_name: str = "param", title: Optional[str] = None,
    height: int = 600, width: int = 800, template: str = "plotly",
) -> PlotlyFigure:
    x = np.asarray(param_values)
    tr = np.asarray(train_scores, dtype=float); va = np.asarray(val_scores, dtype=float)
    if tr.ndim == 1:
        tr_mean, tr_std = tr, np.zeros_like(tr)
        va_mean, va_std = va, np.zeros_like(va)
    else:
        tr_mean, tr_std = tr.mean(axis=1), tr.std(axis=1)
        va_mean, va_std = va.mean(axis=1), va.std(axis=1)
    title = title or f"Validation curve over {param_name}"
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=np.concatenate([x, x[::-1]]),
        y=np.concatenate([tr_mean + tr_std, (tr_mean - tr_std)[::-1]]),
        fill="toself", fillcolor="rgba(31,119,180,0.2)", line=dict(width=0),
        showlegend=False, name="train band"))
    fig.add_trace(go.Scatter(x=x, y=tr_mean, mode="lines+markers", name="train"))
    fig.add_trace(go.Scatter(
        x=np.concatenate([x, x[::-1]]),
        y=np.concatenate([va_mean + va_std, (va_mean - va_std)[::-1]]),
        fill="toself", fillcolor="rgba(255,127,14,0.2)", line=dict(width=0),
        showlegend=False, name="val band"))
    fig.add_trace(go.Scatter(x=x, y=va_mean, mode="lines+markers", name="validation"))
    fig.update_layout(title=title, xaxis_title=param_name, yaxis_title="Score",
                      template=template, height=height, width=width)
    return fig


def cv_score_boxplot_static(
    cv_scores: Mapping[str, Sequence[float]], title: Optional[str] = None,
    figsize: FigureSize = (10, 6), grid: bool = True, grid_alpha: float = 0.3,
    theme: str = "default", dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Box plot of per-fold CV scores for several models."""
    title = title or "Cross-validation score per model"
    names = list(cv_scores.keys())
    data = [list(cv_scores[n]) for n in names]
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Model", ylabel="CV score",
                             figsize=figsize)
        fig.set_dpi(dpi)
        try:
            ax.boxplot(data, tick_labels=names, widths=0.55)
        except TypeError:
            ax.boxplot(data, labels=names, widths=0.55)
        for i, vals in enumerate(data, start=1):
            ax.scatter(np.full(len(vals), i)
                       + (np.random.default_rng(0).random(len(vals)) - 0.5) * 0.1,
                       vals, alpha=0.5, s=18, color="tab:blue")
        if grid:
            ax.grid(True, axis="y", alpha=grid_alpha)
        apply_theme(ax, theme)
    return ax


def cv_score_boxplot_interactive(
    cv_scores: Mapping[str, Sequence[float]], title: Optional[str] = None,
    height: int = 600, width: int = 800, template: str = "plotly",
) -> PlotlyFigure:
    title = title or "Cross-validation score per model"
    fig = go.Figure()
    for name, scores in cv_scores.items():
        fig.add_trace(go.Box(y=list(scores), name=name, boxpoints="all", jitter=0.4))
    fig.update_layout(title=title, yaxis_title="CV score", template=template,
                      height=height, width=width)
    return fig


def training_history_curve_static(
    history: Mapping[str, Sequence[float]], title: Optional[str] = None,
    figsize: FigureSize = (10, 6), grid: bool = True, grid_alpha: float = 0.3,
    theme: str = "default", dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Plot training curves (loss / accuracy / ...) over epochs.

    Args:
        history: Mapping ``metric_name -> per-epoch values``. Series with
            ``"val_"`` prefix or ``"validation"`` substring are styled dashed.
    """
    title = title or "Training history"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Epoch", ylabel="Value",
                             figsize=figsize)
        fig.set_dpi(dpi)
        for name, vals in history.items():
            ls = "--" if name.startswith("val_") or "validation" in name else "-"
            ax.plot(range(1, len(vals) + 1), vals, ls, linewidth=2, label=name)
        if grid:
            ax.grid(True, alpha=grid_alpha)
        ax.legend()
        apply_theme(ax, theme)
    return ax


def training_history_curve_interactive(
    history: Mapping[str, Sequence[float]], title: Optional[str] = None,
    height: int = 600, width: int = 800, template: str = "plotly",
) -> PlotlyFigure:
    title = title or "Training history"
    fig = go.Figure()
    for name, vals in history.items():
        dash = "dash" if name.startswith("val_") or "validation" in name else "solid"
        fig.add_trace(go.Scatter(x=list(range(1, len(vals) + 1)), y=list(vals),
                                 mode="lines+markers", name=name,
                                 line=dict(dash=dash)))
    fig.update_layout(title=title, xaxis_title="Epoch", yaxis_title="Value",
                      template=template, height=height, width=width)
    return fig
