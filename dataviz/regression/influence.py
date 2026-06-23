"""Influence diagnostics: leverage, Cook's distance, DFFITS, DFBETAS."""

from __future__ import annotations

from typing import Optional, Sequence

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from ..types import ArrayLike, FigureSize, MatplotlibAxes, MatrixLike, PlotlyFigure
from ..utils import setup_plot, apply_theme
from .helpers import influence_statistics


# ---------------------------------------------------------------------------
# Leverage plot
# ---------------------------------------------------------------------------

def leverage_plot_static(
    X: MatrixLike,
    y_true: ArrayLike,
    y_pred: ArrayLike,
    title: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    color: str = "#4c78a8",
    threshold_color: str = "#e45756",
    threshold_multiplier: float = 2.0,
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Leverage (hat-matrix diagonal) per observation with a 2p/n threshold."""
    stats = influence_statistics(X, y_true, y_pred)
    n = stats.leverage.size
    p = stats.n_features + 1
    threshold = threshold_multiplier * p / n
    idx = np.arange(n)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Leverage",
                             xlabel="Observation index", ylabel="Leverage",
                             figsize=figsize)
        fig.set_dpi(dpi)
        ax.bar(idx, stats.leverage, color=color, alpha=0.85, **kwargs)
        ax.axhline(threshold, color=threshold_color, linestyle="--", linewidth=1,
                   label=f"{threshold_multiplier}·p/n")
        ax.legend()
        if grid:
            ax.grid(True, alpha=grid_alpha, axis="y")
        apply_theme(ax, theme)
    return ax


def leverage_plot_interactive(
    X: MatrixLike,
    y_true: ArrayLike,
    y_pred: ArrayLike,
    title: Optional[str] = None,
    color: str = "#4c78a8",
    threshold_color: str = "#e45756",
    threshold_multiplier: float = 2.0,
    template: str = "plotly",
    height: int = 600,
    width: int = 1100,
    **kwargs,
) -> PlotlyFigure:
    """Interactive leverage bar chart with a 2p/n threshold."""
    stats = influence_statistics(X, y_true, y_pred)
    n = stats.leverage.size
    p = stats.n_features + 1
    threshold = threshold_multiplier * p / n
    idx = np.arange(n)
    fig = go.Figure()
    fig.add_trace(go.Bar(x=idx, y=stats.leverage, marker_color=color,
                         name="Leverage", **kwargs))
    fig.add_hline(y=threshold, line_dash="dash", line_color=threshold_color)
    fig.update_layout(title=title or "Leverage",
                      xaxis_title="Observation index", yaxis_title="Leverage",
                      template=template, height=height, width=width)
    return fig


# ---------------------------------------------------------------------------
# Cook's distance plot
# ---------------------------------------------------------------------------

def cooks_distance_plot_static(
    X: MatrixLike,
    y_true: ArrayLike,
    y_pred: ArrayLike,
    title: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    color: str = "#4c78a8",
    threshold_color: str = "#e45756",
    threshold: Optional[float] = None,
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Cook's distance per observation with a 4/n threshold by default."""
    stats = influence_statistics(X, y_true, y_pred)
    n = stats.cooks_distance.size
    thr = threshold if threshold is not None else 4.0 / n
    idx = np.arange(n)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Cook's Distance",
                             xlabel="Observation index",
                             ylabel="Cook's distance", figsize=figsize)
        fig.set_dpi(dpi)
        ax.vlines(idx, 0, stats.cooks_distance, color=color, linewidth=2, **kwargs)
        ax.scatter(idx, stats.cooks_distance, color=color, zorder=3)
        ax.axhline(thr, color=threshold_color, linestyle="--", linewidth=1,
                   label=f"threshold={thr:.3g}")
        ax.legend()
        if grid:
            ax.grid(True, alpha=grid_alpha)
        apply_theme(ax, theme)
    return ax


def cooks_distance_plot_interactive(
    X: MatrixLike,
    y_true: ArrayLike,
    y_pred: ArrayLike,
    title: Optional[str] = None,
    color: str = "#4c78a8",
    threshold_color: str = "#e45756",
    threshold: Optional[float] = None,
    template: str = "plotly",
    height: int = 600,
    width: int = 1100,
    **kwargs,
) -> PlotlyFigure:
    """Interactive Cook's distance stem chart."""
    stats = influence_statistics(X, y_true, y_pred)
    n = stats.cooks_distance.size
    thr = threshold if threshold is not None else 4.0 / n
    idx = np.arange(n)
    fig = go.Figure()
    for i, v in zip(idx, stats.cooks_distance):
        fig.add_shape(type="line", x0=i, x1=i, y0=0, y1=v,
                      line=dict(color=color, width=2))
    fig.add_trace(go.Scatter(x=idx, y=stats.cooks_distance, mode="markers",
                             marker=dict(color=color), name="Cook's D", **kwargs))
    fig.add_hline(y=thr, line_dash="dash", line_color=threshold_color)
    fig.update_layout(title=title or "Cook's Distance",
                      xaxis_title="Observation index",
                      yaxis_title="Cook's distance",
                      template=template, height=height, width=width)
    return fig


# ---------------------------------------------------------------------------
# Influence bubble plot (leverage × residual × Cook's D)
# ---------------------------------------------------------------------------

def influence_bubble_plot_static(
    X: MatrixLike,
    y_true: ArrayLike,
    y_pred: ArrayLike,
    title: Optional[str] = None,
    figsize: FigureSize = (10, 7),
    cmap: str = "viridis",
    marker_min: int = 20,
    marker_max: int = 400,
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Leverage vs studentized residual, bubble size encoding Cook's distance."""
    stats = influence_statistics(X, y_true, y_pred)
    cooks = stats.cooks_distance
    rng = cooks.max() - cooks.min()
    if rng <= 0:
        sizes = np.full_like(cooks, (marker_min + marker_max) / 2)
    else:
        sizes = marker_min + (cooks - cooks.min()) / rng * (marker_max - marker_min)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Influence Plot",
                             xlabel="Leverage",
                             ylabel="Studentized residual", figsize=figsize)
        fig.set_dpi(dpi)
        sc = ax.scatter(stats.leverage, stats.studentized_residuals,
                        s=sizes, c=cooks, cmap=cmap, alpha=0.7,
                        edgecolors="black", linewidth=0.5, **kwargs)
        fig.colorbar(sc, ax=ax, label="Cook's distance")
        ax.axhline(0.0, color="#444", linestyle="--", linewidth=1)
        if grid:
            ax.grid(True, alpha=grid_alpha)
        apply_theme(ax, theme)
    return ax


def influence_bubble_plot_interactive(
    X: MatrixLike,
    y_true: ArrayLike,
    y_pred: ArrayLike,
    title: Optional[str] = None,
    colorscale: str = "Viridis",
    marker_min: int = 5,
    marker_max: int = 30,
    template: str = "plotly",
    height: int = 650,
    width: int = 950,
    **kwargs,
) -> PlotlyFigure:
    """Interactive influence bubble plot."""
    stats = influence_statistics(X, y_true, y_pred)
    cooks = stats.cooks_distance
    rng = cooks.max() - cooks.min()
    if rng <= 0:
        sizes = np.full_like(cooks, (marker_min + marker_max) / 2)
    else:
        sizes = marker_min + (cooks - cooks.min()) / rng * (marker_max - marker_min)
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=stats.leverage, y=stats.studentized_residuals, mode="markers",
        marker=dict(size=sizes, color=cooks, colorscale=colorscale,
                    showscale=True, colorbar=dict(title="Cook's D"),
                    line=dict(color="black", width=0.5)),
        name="Observation", **kwargs,
    ))
    fig.add_hline(y=0.0, line_dash="dash", line_color="#444")
    fig.update_layout(title=title or "Influence Plot",
                      xaxis_title="Leverage",
                      yaxis_title="Studentized residual",
                      template=template, height=height, width=width)
    return fig


# ---------------------------------------------------------------------------
# DFBETAS plot
# ---------------------------------------------------------------------------

def dfbetas_plot_static(
    X: MatrixLike,
    y_true: ArrayLike,
    y_pred: ArrayLike,
    feature_names: Optional[Sequence[str]] = None,
    title: Optional[str] = None,
    figsize: FigureSize = (12, 6),
    cmap: str = "coolwarm",
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Heatmap of DFBETAS values (observations × coefficients)."""
    stats = influence_statistics(X, y_true, y_pred)
    dfb = stats.dfbetas
    n, p = dfb.shape
    cols: list[str]
    if feature_names is None:
        cols = ["intercept"] + [f"x{i}" for i in range(p - 1)]
    else:
        cols = ["intercept", *feature_names]
        if len(cols) != p:
            raise ValueError("feature_names length must match coefficients.")
    vmax = float(np.max(np.abs(dfb))) if dfb.size else 1.0
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "DFBETAS",
                             xlabel="Coefficient",
                             ylabel="Observation index", figsize=figsize)
        fig.set_dpi(dpi)
        im = ax.imshow(dfb, aspect="auto", cmap=cmap, vmin=-vmax, vmax=vmax, **kwargs)
        ax.set_xticks(np.arange(p))
        ax.set_xticklabels(cols, rotation=45, ha="right")
        fig.colorbar(im, ax=ax, label="DFBETAS")
        if grid:
            ax.grid(False)
        apply_theme(ax, theme)
    return ax


def dfbetas_plot_interactive(
    X: MatrixLike,
    y_true: ArrayLike,
    y_pred: ArrayLike,
    feature_names: Optional[Sequence[str]] = None,
    title: Optional[str] = None,
    colorscale: str = "RdBu",
    template: str = "plotly",
    height: int = 700,
    width: int = 1100,
    **kwargs,
) -> PlotlyFigure:
    """Interactive DFBETAS heatmap."""
    stats = influence_statistics(X, y_true, y_pred)
    dfb = stats.dfbetas
    n, p = dfb.shape
    cols: list[str]
    if feature_names is None:
        cols = ["intercept"] + [f"x{i}" for i in range(p - 1)]
    else:
        cols = ["intercept", *feature_names]
    vmax = float(np.max(np.abs(dfb))) if dfb.size else 1.0
    fig = go.Figure()
    fig.add_trace(go.Heatmap(z=dfb, x=cols, y=np.arange(n),
                             colorscale=colorscale, zmin=-vmax, zmax=vmax,
                             colorbar=dict(title="DFBETAS"), **kwargs))
    fig.update_layout(title=title or "DFBETAS",
                      xaxis_title="Coefficient",
                      yaxis_title="Observation index",
                      template=template, height=height, width=width)
    return fig


# Convenience aliases
leverage_plot = leverage_plot_static
cooks_distance_plot = cooks_distance_plot_static
influence_bubble_plot = influence_bubble_plot_static
dfbetas_plot = dfbetas_plot_static
