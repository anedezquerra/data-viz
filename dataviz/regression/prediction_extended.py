"""Extended prediction-vs-actual diagnostics and prediction-interval plots."""

from __future__ import annotations

from typing import Optional

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from ..types import ArrayLike, FigureSize, MatplotlibAxes, PlotlyFigure
from ..utils import setup_plot, apply_theme
from .helpers import _as_array, _residuals, prediction_intervals


# ---------------------------------------------------------------------------
# Hexbin pred vs actual
# ---------------------------------------------------------------------------

def pred_vs_actual_hexbin_static(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    gridsize: int = 30,
    title: Optional[str] = None,
    figsize: FigureSize = (8, 8),
    cmap: str = "viridis",
    line_color: str = "#e45756",
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Hexbin density of predicted vs actual values."""
    y_t = _as_array(y_true)
    y_p = _as_array(y_pred)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Predicted vs Actual",
                             xlabel="Actual", ylabel="Predicted", figsize=figsize)
        fig.set_dpi(dpi)
        hb = ax.hexbin(y_t, y_p, gridsize=gridsize, cmap=cmap, mincnt=1, **kwargs)
        fig.colorbar(hb, ax=ax, label="Count")
        lo = min(y_t.min(), y_p.min())
        hi = max(y_t.max(), y_p.max())
        ax.plot([lo, hi], [lo, hi], color=line_color, linewidth=2)
        if grid:
            ax.grid(True, alpha=grid_alpha)
        apply_theme(ax, theme)
    return ax


def pred_vs_actual_hexbin_interactive(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    nbins: int = 30,
    title: Optional[str] = None,
    colorscale: str = "Viridis",
    line_color: str = "#e45756",
    template: str = "plotly",
    height: int = 700,
    width: int = 700,
    **kwargs,
) -> PlotlyFigure:
    """Interactive 2-D histogram (hexbin-like) of predicted vs actual values."""
    y_t = _as_array(y_true)
    y_p = _as_array(y_pred)
    fig = go.Figure()
    fig.add_trace(go.Histogram2d(x=y_t, y=y_p, nbinsx=nbins, nbinsy=nbins,
                                 colorscale=colorscale, name="Density", **kwargs))
    lo = float(min(y_t.min(), y_p.min()))
    hi = float(max(y_t.max(), y_p.max()))
    fig.add_trace(go.Scatter(x=[lo, hi], y=[lo, hi], mode="lines",
                             line=dict(color=line_color, width=2), name="y=x"))
    fig.update_layout(title=title or "Predicted vs Actual",
                      xaxis_title="Actual", yaxis_title="Predicted",
                      template=template, height=height, width=width)
    return fig


# ---------------------------------------------------------------------------
# Density pred vs actual
# ---------------------------------------------------------------------------

def pred_vs_actual_density_static(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    bins: int = 60,
    title: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    actual_color: str = "#4c78a8",
    predicted_color: str = "#e45756",
    alpha: float = 0.4,
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Overlay the marginal distributions of actual and predicted values."""
    y_t = _as_array(y_true)
    y_p = _as_array(y_pred)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Actual vs Predicted Density",
                             xlabel="Value", ylabel="Density", figsize=figsize)
        fig.set_dpi(dpi)
        ax.hist(y_t, bins=bins, density=True, color=actual_color, alpha=alpha,
                label="Actual", **kwargs)
        ax.hist(y_p, bins=bins, density=True, color=predicted_color, alpha=alpha,
                label="Predicted")
        ax.legend()
        if grid:
            ax.grid(True, alpha=grid_alpha)
        apply_theme(ax, theme)
    return ax


def pred_vs_actual_density_interactive(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    bins: int = 60,
    title: Optional[str] = None,
    actual_color: str = "#4c78a8",
    predicted_color: str = "#e45756",
    template: str = "plotly",
    height: int = 600,
    width: int = 1000,
    **kwargs,
) -> PlotlyFigure:
    """Interactive overlay of actual and predicted marginal distributions."""
    y_t = _as_array(y_true)
    y_p = _as_array(y_pred)
    fig = go.Figure()
    fig.add_trace(go.Histogram(x=y_t, nbinsx=bins, histnorm="probability density",
                               marker_color=actual_color, opacity=0.55,
                               name="Actual", **kwargs))
    fig.add_trace(go.Histogram(x=y_p, nbinsx=bins, histnorm="probability density",
                               marker_color=predicted_color, opacity=0.55,
                               name="Predicted"))
    fig.update_layout(title=title or "Actual vs Predicted Density",
                      xaxis_title="Value", yaxis_title="Density",
                      barmode="overlay", template=template,
                      height=height, width=width)
    return fig


# ---------------------------------------------------------------------------
# Prediction error histogram
# ---------------------------------------------------------------------------

def prediction_error_histogram_static(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    bins: int = 30,
    title: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    color: str = "#4c78a8",
    edgecolor: str = "black",
    cumulative: bool = False,
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Histogram of prediction errors (y_true − y_pred), optionally cumulative."""
    res = _residuals(y_true, y_pred)
    with plt.style.context(style):
        fig, ax = setup_plot(
            title=title or ("Cumulative Error" if cumulative else "Prediction Error"),
            xlabel="Error", ylabel="Density", figsize=figsize,
        )
        fig.set_dpi(dpi)
        ax.hist(res, bins=bins, density=True, cumulative=cumulative,
                color=color, edgecolor=edgecolor, alpha=0.8, **kwargs)
        ax.axvline(0.0, color="#e45756", linestyle="--", linewidth=1)
        if grid:
            ax.grid(True, alpha=grid_alpha)
        apply_theme(ax, theme)
    return ax


def prediction_error_histogram_interactive(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    bins: int = 30,
    title: Optional[str] = None,
    color: str = "#4c78a8",
    cumulative: bool = False,
    template: str = "plotly",
    height: int = 600,
    width: int = 1000,
    **kwargs,
) -> PlotlyFigure:
    """Interactive prediction-error histogram."""
    res = _residuals(y_true, y_pred)
    fig = go.Figure()
    fig.add_trace(go.Histogram(x=res, nbinsx=bins,
                               histnorm="probability density",
                               cumulative_enabled=cumulative,
                               marker_color=color, name="Error", **kwargs))
    fig.add_vline(x=0.0, line_dash="dash", line_color="#e45756")
    fig.update_layout(
        title=title or ("Cumulative Error" if cumulative else "Prediction Error"),
        xaxis_title="Error", yaxis_title="Density",
        template=template, height=height, width=width,
    )
    return fig


# ---------------------------------------------------------------------------
# Prediction interval plot
# ---------------------------------------------------------------------------

def prediction_interval_plot_static(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    confidence: float = 0.95,
    method: str = "empirical",
    sort_by_prediction: bool = True,
    title: Optional[str] = None,
    figsize: FigureSize = (12, 6),
    point_color: str = "#4c78a8",
    band_color: str = "#a0c4e8",
    line_color: str = "#e45756",
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Plot predictions with empirical or Gaussian prediction-interval band."""
    y_t = _as_array(y_true)
    y_p = _as_array(y_pred)
    res = y_t - y_p
    lo, hi = prediction_intervals(y_p, res, confidence=confidence, method=method)
    idx = np.argsort(y_p) if sort_by_prediction else np.arange(y_p.size)
    x = np.arange(y_p.size)
    with plt.style.context(style):
        fig, ax = setup_plot(
            title=title or f"Predictions with {int(confidence * 100)}% Interval",
            xlabel="Observation (sorted by prediction)",
            ylabel="Value", figsize=figsize,
        )
        fig.set_dpi(dpi)
        ax.fill_between(x, lo[idx], hi[idx], color=band_color, alpha=0.5,
                        label=f"{int(confidence * 100)}% PI")
        ax.plot(x, y_p[idx], color=line_color, linewidth=2, label="Predicted")
        ax.scatter(x, y_t[idx], color=point_color, s=20, alpha=0.7,
                   label="Actual", **kwargs)
        ax.legend()
        if grid:
            ax.grid(True, alpha=grid_alpha)
        apply_theme(ax, theme)
    return ax


def prediction_interval_plot_interactive(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    confidence: float = 0.95,
    method: str = "empirical",
    sort_by_prediction: bool = True,
    title: Optional[str] = None,
    point_color: str = "#4c78a8",
    band_color: str = "rgba(160,196,232,0.5)",
    line_color: str = "#e45756",
    template: str = "plotly",
    height: int = 600,
    width: int = 1100,
    **kwargs,
) -> PlotlyFigure:
    """Interactive predictions with a shaded prediction-interval band."""
    y_t = _as_array(y_true)
    y_p = _as_array(y_pred)
    res = y_t - y_p
    lo, hi = prediction_intervals(y_p, res, confidence=confidence, method=method)
    idx = np.argsort(y_p) if sort_by_prediction else np.arange(y_p.size)
    x = np.arange(y_p.size)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=np.concatenate([x, x[::-1]]),
                             y=np.concatenate([hi[idx], lo[idx][::-1]]),
                             fill="toself", fillcolor=band_color,
                             line=dict(width=0), name=f"{int(confidence*100)}% PI"))
    fig.add_trace(go.Scatter(x=x, y=y_p[idx], mode="lines",
                             line=dict(color=line_color, width=2), name="Predicted"))
    fig.add_trace(go.Scatter(x=x, y=y_t[idx], mode="markers",
                             marker=dict(color=point_color, size=6),
                             name="Actual", **kwargs))
    fig.update_layout(
        title=title or f"Predictions with {int(confidence * 100)}% Interval",
        xaxis_title="Observation (sorted by prediction)",
        yaxis_title="Value", template=template, height=height, width=width,
    )
    return fig


# ---------------------------------------------------------------------------
# Error by magnitude
# ---------------------------------------------------------------------------

def error_by_magnitude_plot_static(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    n_bins: int = 10,
    title: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    color: str = "#4c78a8",
    line_color: str = "#e45756",
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Mean absolute error grouped into quantile bins of actual magnitude."""
    y_t = _as_array(y_true)
    y_p = _as_array(y_pred)
    if y_t.size != y_p.size:
        raise ValueError("y_true and y_pred must align.")
    edges = np.quantile(y_t, np.linspace(0, 1, n_bins + 1))
    edges[0] -= 1e-12
    bins = np.digitize(y_t, edges[1:-1])
    err = np.abs(y_t - y_p)
    centers = 0.5 * (edges[:-1] + edges[1:])
    mae_per_bin = np.array([err[bins == k].mean() if np.any(bins == k) else np.nan
                            for k in range(n_bins)])
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Error by Magnitude",
                             xlabel="Actual (quantile midpoint)",
                             ylabel="MAE", figsize=figsize)
        fig.set_dpi(dpi)
        ax.bar(centers, mae_per_bin, width=(edges[1:] - edges[:-1]) * 0.9,
               color=color, alpha=0.8, **kwargs)
        ax.plot(centers, mae_per_bin, color=line_color, marker="o", linewidth=2)
        if grid:
            ax.grid(True, alpha=grid_alpha, axis="y")
        apply_theme(ax, theme)
    return ax


def error_by_magnitude_plot_interactive(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    n_bins: int = 10,
    title: Optional[str] = None,
    color: str = "#4c78a8",
    line_color: str = "#e45756",
    template: str = "plotly",
    height: int = 600,
    width: int = 1000,
    **kwargs,
) -> PlotlyFigure:
    """Interactive error-by-magnitude chart."""
    y_t = _as_array(y_true)
    y_p = _as_array(y_pred)
    edges = np.quantile(y_t, np.linspace(0, 1, n_bins + 1))
    edges[0] -= 1e-12
    bins = np.digitize(y_t, edges[1:-1])
    err = np.abs(y_t - y_p)
    centers = 0.5 * (edges[:-1] + edges[1:])
    mae = np.array([err[bins == k].mean() if np.any(bins == k) else np.nan
                    for k in range(n_bins)])
    fig = go.Figure()
    fig.add_trace(go.Bar(x=centers, y=mae, marker_color=color, name="MAE", **kwargs))
    fig.add_trace(go.Scatter(x=centers, y=mae, mode="lines+markers",
                             line=dict(color=line_color, width=2),
                             marker=dict(color=line_color), name="Trend"))
    fig.update_layout(title=title or "Error by Magnitude",
                      xaxis_title="Actual (quantile midpoint)",
                      yaxis_title="MAE", template=template,
                      height=height, width=width)
    return fig


# Convenience aliases
pred_vs_actual_hexbin = pred_vs_actual_hexbin_static
pred_vs_actual_density = pred_vs_actual_density_static
prediction_error_histogram = prediction_error_histogram_static
prediction_interval_plot = prediction_interval_plot_static
error_by_magnitude_plot = error_by_magnitude_plot_static
