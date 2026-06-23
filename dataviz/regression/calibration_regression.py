"""Regression calibration and predictive-uncertainty diagnostics."""

from __future__ import annotations

from typing import Optional

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from ..types import ArrayLike, FigureSize, MatplotlibAxes, PlotlyFigure
from ..utils import setup_plot, apply_theme
from .helpers import _as_array, prediction_intervals


# ---------------------------------------------------------------------------
# Calibration curve for regression (predicted vs observed quantiles)
# ---------------------------------------------------------------------------

def calibration_curve_regression_static(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    n_bins: int = 10,
    title: Optional[str] = None,
    figsize: FigureSize = (8, 8),
    color: str = "#4c78a8",
    line_color: str = "#e45756",
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Bin predictions into quantiles and plot mean predicted vs mean observed."""
    y_t = _as_array(y_true)
    y_p = _as_array(y_pred)
    if y_t.size != y_p.size:
        raise ValueError("y_true and y_pred must align.")
    edges = np.quantile(y_p, np.linspace(0, 1, n_bins + 1))
    edges[0] -= 1e-12
    bins = np.digitize(y_p, edges[1:-1])
    pred_mean = np.array([y_p[bins == k].mean() if np.any(bins == k) else np.nan
                          for k in range(n_bins)])
    obs_mean = np.array([y_t[bins == k].mean() if np.any(bins == k) else np.nan
                         for k in range(n_bins)])
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Regression Calibration",
                             xlabel="Predicted (bin mean)",
                             ylabel="Observed (bin mean)", figsize=figsize)
        fig.set_dpi(dpi)
        ax.scatter(pred_mean, obs_mean, color=color, s=70, alpha=0.85, **kwargs)
        ax.plot(pred_mean, obs_mean, color=color, linewidth=1.5)
        lo = float(np.nanmin([pred_mean.min(), obs_mean.min()]))
        hi = float(np.nanmax([pred_mean.max(), obs_mean.max()]))
        ax.plot([lo, hi], [lo, hi], color=line_color, linestyle="--", linewidth=2)
        if grid:
            ax.grid(True, alpha=grid_alpha)
        apply_theme(ax, theme)
    return ax


def calibration_curve_regression_interactive(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    n_bins: int = 10,
    title: Optional[str] = None,
    color: str = "#4c78a8",
    line_color: str = "#e45756",
    template: str = "plotly",
    height: int = 650,
    width: int = 650,
    **kwargs,
) -> PlotlyFigure:
    """Interactive regression calibration curve."""
    y_t = _as_array(y_true)
    y_p = _as_array(y_pred)
    edges = np.quantile(y_p, np.linspace(0, 1, n_bins + 1))
    edges[0] -= 1e-12
    bins = np.digitize(y_p, edges[1:-1])
    pred_mean = np.array([y_p[bins == k].mean() if np.any(bins == k) else np.nan
                          for k in range(n_bins)])
    obs_mean = np.array([y_t[bins == k].mean() if np.any(bins == k) else np.nan
                         for k in range(n_bins)])
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=pred_mean, y=obs_mean, mode="lines+markers",
                             marker=dict(color=color, size=10),
                             line=dict(color=color, width=2),
                             name="Calibration", **kwargs))
    lo = float(np.nanmin([np.nanmin(pred_mean), np.nanmin(obs_mean)]))
    hi = float(np.nanmax([np.nanmax(pred_mean), np.nanmax(obs_mean)]))
    fig.add_trace(go.Scatter(x=[lo, hi], y=[lo, hi], mode="lines",
                             line=dict(color=line_color, dash="dash", width=2),
                             name="y=x"))
    fig.update_layout(title=title or "Regression Calibration",
                      xaxis_title="Predicted (bin mean)",
                      yaxis_title="Observed (bin mean)",
                      template=template, height=height, width=width)
    return fig


# ---------------------------------------------------------------------------
# Prediction interval coverage
# ---------------------------------------------------------------------------

def prediction_interval_coverage_plot_static(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    levels: ArrayLike = (0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 0.99),
    method: str = "empirical",
    title: Optional[str] = None,
    figsize: FigureSize = (9, 6),
    coverage_color: str = "#4c78a8",
    ideal_color: str = "#e45756",
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Empirical coverage of prediction intervals at each nominal level."""
    y_t = _as_array(y_true)
    y_p = _as_array(y_pred)
    res = y_t - y_p
    levels_arr = np.asarray(levels, dtype=float)
    coverage = np.zeros_like(levels_arr)
    for i, lvl in enumerate(levels_arr):
        lo, hi = prediction_intervals(y_p, res, confidence=float(lvl), method=method)
        coverage[i] = float(((y_t >= lo) & (y_t <= hi)).mean())
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Prediction Interval Coverage",
                             xlabel="Nominal level",
                             ylabel="Empirical coverage", figsize=figsize)
        fig.set_dpi(dpi)
        ax.plot(levels_arr, coverage, color=coverage_color, marker="o",
                linewidth=2, label="Empirical", **kwargs)
        ax.plot([0, 1], [0, 1], color=ideal_color, linestyle="--", linewidth=2,
                label="Ideal")
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.legend()
        if grid:
            ax.grid(True, alpha=grid_alpha)
        apply_theme(ax, theme)
    return ax


def prediction_interval_coverage_plot_interactive(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    levels: ArrayLike = (0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 0.99),
    method: str = "empirical",
    title: Optional[str] = None,
    coverage_color: str = "#4c78a8",
    ideal_color: str = "#e45756",
    template: str = "plotly",
    height: int = 600,
    width: int = 700,
    **kwargs,
) -> PlotlyFigure:
    """Interactive prediction-interval coverage plot."""
    y_t = _as_array(y_true)
    y_p = _as_array(y_pred)
    res = y_t - y_p
    levels_arr = np.asarray(levels, dtype=float)
    coverage = np.zeros_like(levels_arr)
    for i, lvl in enumerate(levels_arr):
        lo, hi = prediction_intervals(y_p, res, confidence=float(lvl), method=method)
        coverage[i] = float(((y_t >= lo) & (y_t <= hi)).mean())
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=levels_arr, y=coverage, mode="lines+markers",
                             line=dict(color=coverage_color, width=2),
                             marker=dict(color=coverage_color),
                             name="Empirical", **kwargs))
    fig.add_trace(go.Scatter(x=[0, 1], y=[0, 1], mode="lines",
                             line=dict(color=ideal_color, dash="dash", width=2),
                             name="Ideal"))
    fig.update_layout(title=title or "Prediction Interval Coverage",
                      xaxis_title="Nominal level",
                      yaxis_title="Empirical coverage",
                      template=template, height=height, width=width,
                      xaxis=dict(range=[0, 1]), yaxis=dict(range=[0, 1]))
    return fig


# ---------------------------------------------------------------------------
# Uncertainty band (predicted mean ± user supplied std)
# ---------------------------------------------------------------------------

def uncertainty_band_plot_static(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    y_std: ArrayLike,
    z: float = 1.96,
    sort_by_prediction: bool = True,
    title: Optional[str] = None,
    figsize: FigureSize = (12, 6),
    point_color: str = "#4c78a8",
    line_color: str = "#e45756",
    band_color: str = "#a0c4e8",
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Plot mean prediction with a ±z·σ uncertainty band (e.g., Gaussian process)."""
    y_t = _as_array(y_true)
    y_p = _as_array(y_pred)
    sigma = _as_array(y_std)
    if y_t.shape != y_p.shape or y_t.shape != sigma.shape:
        raise ValueError("y_true, y_pred, and y_std must align.")
    idx = np.argsort(y_p) if sort_by_prediction else np.arange(y_p.size)
    x = np.arange(y_p.size)
    lo = y_p[idx] - z * sigma[idx]
    hi = y_p[idx] + z * sigma[idx]
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Predictive Uncertainty Band",
                             xlabel="Observation (sorted by prediction)",
                             ylabel="Value", figsize=figsize)
        fig.set_dpi(dpi)
        ax.fill_between(x, lo, hi, color=band_color, alpha=0.5,
                        label=f"±{z}·σ")
        ax.plot(x, y_p[idx], color=line_color, linewidth=2, label="Predicted")
        ax.scatter(x, y_t[idx], color=point_color, s=20, alpha=0.7,
                   label="Actual", **kwargs)
        ax.legend()
        if grid:
            ax.grid(True, alpha=grid_alpha)
        apply_theme(ax, theme)
    return ax


def uncertainty_band_plot_interactive(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    y_std: ArrayLike,
    z: float = 1.96,
    sort_by_prediction: bool = True,
    title: Optional[str] = None,
    point_color: str = "#4c78a8",
    line_color: str = "#e45756",
    band_color: str = "rgba(160,196,232,0.5)",
    template: str = "plotly",
    height: int = 600,
    width: int = 1100,
    **kwargs,
) -> PlotlyFigure:
    """Interactive ±z·σ predictive-uncertainty band."""
    y_t = _as_array(y_true)
    y_p = _as_array(y_pred)
    sigma = _as_array(y_std)
    idx = np.argsort(y_p) if sort_by_prediction else np.arange(y_p.size)
    x = np.arange(y_p.size)
    lo = y_p[idx] - z * sigma[idx]
    hi = y_p[idx] + z * sigma[idx]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=np.concatenate([x, x[::-1]]),
                             y=np.concatenate([hi, lo[::-1]]),
                             fill="toself", fillcolor=band_color,
                             line=dict(width=0), name=f"±{z}·σ"))
    fig.add_trace(go.Scatter(x=x, y=y_p[idx], mode="lines",
                             line=dict(color=line_color, width=2), name="Predicted"))
    fig.add_trace(go.Scatter(x=x, y=y_t[idx], mode="markers",
                             marker=dict(color=point_color, size=6),
                             name="Actual", **kwargs))
    fig.update_layout(title=title or "Predictive Uncertainty Band",
                      xaxis_title="Observation (sorted by prediction)",
                      yaxis_title="Value",
                      template=template, height=height, width=width)
    return fig


calibration_curve_regression = calibration_curve_regression_static
prediction_interval_coverage_plot = prediction_interval_coverage_plot_static
uncertainty_band_plot = uncertainty_band_plot_static
