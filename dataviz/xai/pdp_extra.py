"""Extended partial-dependence, ICE and ALE plots."""

from __future__ import annotations

from typing import Optional, Sequence

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from ..types import ArrayLike, FigureSize, MatplotlibAxes, MatrixLike, PlotlyFigure
from ..utils import setup_plot, apply_theme


def partial_dependence_2d_heatmap_static(
    x_grid: ArrayLike, y_grid: ArrayLike, pdp: MatrixLike,
    feature_x: str = "feature x", feature_y: str = "feature y",
    title: Optional[str] = None, figsize: FigureSize = (9, 7),
    cmap: str = "viridis", annot: bool = False, theme: str = "default",
    dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """2-D partial dependence (interaction) heatmap on a precomputed grid."""
    Z = np.asarray(pdp, dtype=float)
    title = title or f"Partial dependence: {feature_x} × {feature_y}"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel=feature_x, ylabel=feature_y,
                             figsize=figsize)
        fig.set_dpi(dpi)
        x = np.asarray(x_grid, dtype=float)
        y = np.asarray(y_grid, dtype=float)
        im = ax.imshow(Z, origin="lower", aspect="auto",
                       extent=[x.min(), x.max(), y.min(), y.max()], cmap=cmap)
        if annot:
            for i in range(Z.shape[0]):
                for j in range(Z.shape[1]):
                    ax.text(x[j], y[i], f"{Z[i, j]:.2f}", ha="center",
                            va="center", fontsize=7, color="white")
        cb = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
        cb.set_label("Partial dependence")
        apply_theme(ax, theme)
    return ax


def partial_dependence_2d_heatmap_interactive(
    x_grid: ArrayLike, y_grid: ArrayLike, pdp: MatrixLike,
    feature_x: str = "feature x", feature_y: str = "feature y",
    title: Optional[str] = None, height: int = 600, width: int = 700,
    template: str = "plotly", colorscale: str = "Viridis",
) -> PlotlyFigure:
    fig = go.Figure(go.Heatmap(z=np.asarray(pdp, dtype=float),
                               x=list(x_grid), y=list(y_grid),
                               colorscale=colorscale,
                               colorbar=dict(title="Partial dependence")))
    fig.update_layout(title=title or f"Partial dependence: {feature_x} × {feature_y}",
                      xaxis_title=feature_x, yaxis_title=feature_y,
                      template=template, height=height, width=width)
    return fig


def ice_plot_static(
    feature_values: ArrayLike, ice_curves: MatrixLike,
    feature_name: str = "feature", show_average: bool = True,
    title: Optional[str] = None, figsize: FigureSize = (10, 6),
    line_alpha: float = 0.2, grid: bool = True, grid_alpha: float = 0.3,
    theme: str = "default", dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Individual Conditional Expectation curves with optional PDP average.

    Args:
        ice_curves: Shape ``(n_instances, len(feature_values))`` matrix of
            predictions; row k is the response for instance k as the feature
            sweeps over ``feature_values``.
    """
    x = np.asarray(feature_values, dtype=float)
    Y = np.asarray(ice_curves, dtype=float)
    title = title or f"ICE plot: {feature_name}"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel=feature_name,
                             ylabel="Prediction", figsize=figsize)
        fig.set_dpi(dpi)
        for row in Y:
            ax.plot(x, row, color="steelblue", alpha=line_alpha, linewidth=0.8)
        if show_average:
            ax.plot(x, Y.mean(axis=0), color="black", linewidth=2.2,
                    label="average (PDP)")
            ax.legend()
        if grid:
            ax.grid(True, alpha=grid_alpha)
        apply_theme(ax, theme)
    return ax


def ice_plot_interactive(
    feature_values: ArrayLike, ice_curves: MatrixLike,
    feature_name: str = "feature", show_average: bool = True,
    title: Optional[str] = None, height: int = 600, width: int = 800,
    template: str = "plotly", line_alpha: float = 0.2,
) -> PlotlyFigure:
    x = np.asarray(feature_values, dtype=float)
    Y = np.asarray(ice_curves, dtype=float)
    fig = go.Figure()
    for k, row in enumerate(Y):
        fig.add_trace(go.Scatter(x=x, y=row, mode="lines", showlegend=False,
                                 line=dict(color=f"rgba(70,130,180,{line_alpha})",
                                            width=1),
                                 hoverinfo="skip"))
    if show_average:
        fig.add_trace(go.Scatter(x=x, y=Y.mean(axis=0), mode="lines",
                                 line=dict(color="black", width=3),
                                 name="average (PDP)"))
    fig.update_layout(title=title or f"ICE plot: {feature_name}",
                      xaxis_title=feature_name, yaxis_title="Prediction",
                      template=template, height=height, width=width)
    return fig


def centered_ice_plot_static(
    feature_values: ArrayLike, ice_curves: MatrixLike,
    feature_name: str = "feature", show_average: bool = True,
    title: Optional[str] = None, figsize: FigureSize = (10, 6),
    line_alpha: float = 0.2, grid: bool = True, grid_alpha: float = 0.3,
    theme: str = "default", dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Centered ICE (c-ICE) — anchors each curve to zero at the left endpoint."""
    Y = np.asarray(ice_curves, dtype=float)
    Yc = Y - Y[:, [0]]
    return ice_plot_static(feature_values, Yc, feature_name=feature_name,
                           show_average=show_average,
                           title=title or f"Centered ICE: {feature_name}",
                           figsize=figsize, line_alpha=line_alpha, grid=grid,
                           grid_alpha=grid_alpha, theme=theme, dpi=dpi,
                           style=style)


def centered_ice_plot_interactive(
    feature_values: ArrayLike, ice_curves: MatrixLike,
    feature_name: str = "feature", show_average: bool = True,
    title: Optional[str] = None, height: int = 600, width: int = 800,
    template: str = "plotly", line_alpha: float = 0.2,
) -> PlotlyFigure:
    Y = np.asarray(ice_curves, dtype=float)
    Yc = Y - Y[:, [0]]
    return ice_plot_interactive(feature_values, Yc, feature_name=feature_name,
                                show_average=show_average,
                                title=title or f"Centered ICE: {feature_name}",
                                height=height, width=width, template=template,
                                line_alpha=line_alpha)


def ale_plot_1d_static(
    bin_edges: ArrayLike, ale: ArrayLike, feature_name: str = "feature",
    title: Optional[str] = None, figsize: FigureSize = (10, 6),
    color: str = "tab:purple", grid: bool = True, grid_alpha: float = 0.3,
    theme: str = "default", dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """1-D Accumulated Local Effects on precomputed bins.

    Args:
        bin_edges: ``(n_bins + 1,)`` array of feature bin edges.
        ale: ``(n_bins,)`` array of ALE values (typically centered to 0).
    """
    e = np.asarray(bin_edges, dtype=float)
    a = np.asarray(ale, dtype=float)
    centers = (e[:-1] + e[1:]) / 2
    title = title or f"ALE: {feature_name}"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel=feature_name,
                             ylabel="ALE", figsize=figsize)
        fig.set_dpi(dpi)
        ax.plot(centers, a, color=color, linewidth=2.2, marker="o")
        ax.axhline(0, color="black", linewidth=0.6)
        for x in e:
            ax.axvline(x, color="grey", alpha=0.15, linewidth=0.6)
        if grid:
            ax.grid(True, alpha=grid_alpha)
        apply_theme(ax, theme)
    return ax


def ale_plot_1d_interactive(
    bin_edges: ArrayLike, ale: ArrayLike, feature_name: str = "feature",
    title: Optional[str] = None, height: int = 600, width: int = 800,
    template: str = "plotly", color: str = "purple",
) -> PlotlyFigure:
    e = np.asarray(bin_edges, dtype=float)
    centers = (e[:-1] + e[1:]) / 2
    fig = go.Figure(go.Scatter(x=centers, y=list(ale), mode="lines+markers",
                               line=dict(color=color, width=3)))
    fig.add_hline(y=0, line_color="black", line_width=1)
    fig.update_layout(title=title or f"ALE: {feature_name}",
                      xaxis_title=feature_name, yaxis_title="ALE",
                      template=template, height=height, width=width)
    return fig
