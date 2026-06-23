"""Autocorrelation, runs, and time-ordered residual diagnostics."""

from __future__ import annotations

from typing import Optional

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from ..types import ArrayLike, FigureSize, MatplotlibAxes, PlotlyFigure
from ..utils import setup_plot, apply_theme
from .helpers import (
    _as_array,
    _residuals,
    autocorrelation,
    partial_autocorrelation,
    runs_test_signs,
)


def _confidence_band(n: int, alpha: float = 0.05) -> float:
    # Bartlett's 1/sqrt(n) approximate band with z_{1-α/2} ≈ 1.96 at α=0.05.
    return 1.959963984540054 / max(np.sqrt(n), 1.0)


# ---------------------------------------------------------------------------
# Residual ACF
# ---------------------------------------------------------------------------

def residual_acf_static(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    max_lag: int = 20,
    title: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    color: str = "#4c78a8",
    band_color: str = "#e45756",
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Stem plot of residual autocorrelation up to ``max_lag`` with 95% band."""
    res = _residuals(y_true, y_pred)
    acf = autocorrelation(res, max_lag=max_lag)
    band = _confidence_band(res.size)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Residual ACF",
                             xlabel="Lag", ylabel="ACF", figsize=figsize)
        fig.set_dpi(dpi)
        lags = np.arange(acf.size)
        ax.vlines(lags, 0, acf, color=color, linewidth=2, **kwargs)
        ax.scatter(lags, acf, color=color, zorder=3)
        ax.axhline(0.0, color="#444", linewidth=1)
        ax.axhline(band, color=band_color, linestyle="--", linewidth=1)
        ax.axhline(-band, color=band_color, linestyle="--", linewidth=1)
        if grid:
            ax.grid(True, alpha=grid_alpha)
        apply_theme(ax, theme)
    return ax


def residual_acf_interactive(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    max_lag: int = 20,
    title: Optional[str] = None,
    color: str = "#4c78a8",
    band_color: str = "#e45756",
    template: str = "plotly",
    height: int = 600,
    width: int = 1000,
    **kwargs,
) -> PlotlyFigure:
    """Interactive residual ACF stem plot."""
    res = _residuals(y_true, y_pred)
    acf = autocorrelation(res, max_lag=max_lag)
    band = _confidence_band(res.size)
    lags = np.arange(acf.size)
    fig = go.Figure()
    for k, v in zip(lags, acf):
        fig.add_shape(type="line", x0=k, x1=k, y0=0, y1=v,
                      line=dict(color=color, width=2))
    fig.add_trace(go.Scatter(x=lags, y=acf, mode="markers",
                             marker=dict(color=color, size=8), name="ACF", **kwargs))
    fig.add_hline(y=band, line_dash="dash", line_color=band_color)
    fig.add_hline(y=-band, line_dash="dash", line_color=band_color)
    fig.add_hline(y=0.0, line_color="#444")
    fig.update_layout(title=title or "Residual ACF",
                      xaxis_title="Lag", yaxis_title="ACF",
                      template=template, height=height, width=width)
    return fig


# ---------------------------------------------------------------------------
# Residual PACF
# ---------------------------------------------------------------------------

def residual_pacf_static(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    max_lag: int = 20,
    title: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    color: str = "#4c78a8",
    band_color: str = "#e45756",
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Stem plot of residual partial autocorrelation."""
    res = _residuals(y_true, y_pred)
    pacf = partial_autocorrelation(res, max_lag=max_lag)
    band = _confidence_band(res.size)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Residual PACF",
                             xlabel="Lag", ylabel="PACF", figsize=figsize)
        fig.set_dpi(dpi)
        lags = np.arange(pacf.size)
        ax.vlines(lags, 0, pacf, color=color, linewidth=2, **kwargs)
        ax.scatter(lags, pacf, color=color, zorder=3)
        ax.axhline(0.0, color="#444", linewidth=1)
        ax.axhline(band, color=band_color, linestyle="--", linewidth=1)
        ax.axhline(-band, color=band_color, linestyle="--", linewidth=1)
        if grid:
            ax.grid(True, alpha=grid_alpha)
        apply_theme(ax, theme)
    return ax


def residual_pacf_interactive(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    max_lag: int = 20,
    title: Optional[str] = None,
    color: str = "#4c78a8",
    band_color: str = "#e45756",
    template: str = "plotly",
    height: int = 600,
    width: int = 1000,
    **kwargs,
) -> PlotlyFigure:
    """Interactive residual PACF stem plot."""
    res = _residuals(y_true, y_pred)
    pacf = partial_autocorrelation(res, max_lag=max_lag)
    band = _confidence_band(res.size)
    lags = np.arange(pacf.size)
    fig = go.Figure()
    for k, v in zip(lags, pacf):
        fig.add_shape(type="line", x0=k, x1=k, y0=0, y1=v,
                      line=dict(color=color, width=2))
    fig.add_trace(go.Scatter(x=lags, y=pacf, mode="markers",
                             marker=dict(color=color, size=8), name="PACF", **kwargs))
    fig.add_hline(y=band, line_dash="dash", line_color=band_color)
    fig.add_hline(y=-band, line_dash="dash", line_color=band_color)
    fig.add_hline(y=0.0, line_color="#444")
    fig.update_layout(title=title or "Residual PACF",
                      xaxis_title="Lag", yaxis_title="PACF",
                      template=template, height=height, width=width)
    return fig


# ---------------------------------------------------------------------------
# Residual runs plot
# ---------------------------------------------------------------------------

def residual_runs_plot_static(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    title: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    positive_color: str = "#4c78a8",
    negative_color: str = "#e45756",
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Bar plot of residual signs over observation index with runs summary."""
    res = _residuals(y_true, y_pred)
    n_runs, n_pos, n_neg = runs_test_signs(res)
    idx = np.arange(res.size)
    colors = np.where(res >= 0, positive_color, negative_color)
    with plt.style.context(style):
        fig, ax = setup_plot(
            title=title or f"Residual Runs ({n_runs} runs, +{n_pos}, -{n_neg})",
            xlabel="Observation index", ylabel="Residual", figsize=figsize,
        )
        fig.set_dpi(dpi)
        ax.bar(idx, res, color=colors, **kwargs)
        ax.axhline(0.0, color="#444", linewidth=1)
        if grid:
            ax.grid(True, alpha=grid_alpha, axis="y")
        apply_theme(ax, theme)
    return ax


def residual_runs_plot_interactive(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    title: Optional[str] = None,
    positive_color: str = "#4c78a8",
    negative_color: str = "#e45756",
    template: str = "plotly",
    height: int = 600,
    width: int = 1000,
    **kwargs,
) -> PlotlyFigure:
    """Interactive residual-runs bar chart."""
    res = _residuals(y_true, y_pred)
    n_runs, n_pos, n_neg = runs_test_signs(res)
    idx = np.arange(res.size)
    colors = np.where(res >= 0, positive_color, negative_color)
    fig = go.Figure()
    fig.add_trace(go.Bar(x=idx, y=res, marker_color=colors, name="Residual", **kwargs))
    fig.add_hline(y=0.0, line_color="#444")
    fig.update_layout(
        title=title or f"Residual Runs ({n_runs} runs, +{n_pos}, -{n_neg})",
        xaxis_title="Observation index", yaxis_title="Residual",
        template=template, height=height, width=width,
    )
    return fig


# ---------------------------------------------------------------------------
# Residual time plot
# ---------------------------------------------------------------------------

def residual_time_plot_static(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    time: Optional[ArrayLike] = None,
    title: Optional[str] = None,
    figsize: FigureSize = (12, 5),
    color: str = "#4c78a8",
    marker: str = "o",
    line: bool = True,
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Residuals plotted against time (or observation index when omitted)."""
    res = _residuals(y_true, y_pred)
    t = _as_array(time) if time is not None else np.arange(res.size, dtype=float)
    if t.size != res.size:
        raise ValueError("time must align with y_true / y_pred.")
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Residuals Over Time",
                             xlabel="Time", ylabel="Residual", figsize=figsize)
        fig.set_dpi(dpi)
        if line:
            ax.plot(t, res, color=color, marker=marker, **kwargs)
        else:
            ax.scatter(t, res, color=color, **kwargs)
        ax.axhline(0.0, color="#444", linestyle="--", linewidth=1)
        if grid:
            ax.grid(True, alpha=grid_alpha)
        apply_theme(ax, theme)
    return ax


def residual_time_plot_interactive(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    time: Optional[ArrayLike] = None,
    title: Optional[str] = None,
    color: str = "#4c78a8",
    line: bool = True,
    template: str = "plotly",
    height: int = 500,
    width: int = 1100,
    **kwargs,
) -> PlotlyFigure:
    """Interactive residual time plot."""
    res = _residuals(y_true, y_pred)
    t = _as_array(time) if time is not None else np.arange(res.size, dtype=float)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=t, y=res,
                             mode="lines+markers" if line else "markers",
                             line=dict(color=color),
                             marker=dict(color=color), name="Residual", **kwargs))
    fig.add_hline(y=0.0, line_dash="dash", line_color="#444")
    fig.update_layout(title=title or "Residuals Over Time",
                      xaxis_title="Time", yaxis_title="Residual",
                      template=template, height=height, width=width)
    return fig


# Convenience aliases
residual_acf = residual_acf_static
residual_pacf = residual_pacf_static
residual_runs_plot = residual_runs_plot_static
residual_time_plot = residual_time_plot_static
