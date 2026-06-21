"""Additional dependence / interaction charts: PDP+ICE, 2-D ALE, H-statistic, interaction network."""

from __future__ import annotations

from typing import Optional, Sequence, Tuple

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from ..types import FigureSize, MatplotlibAxes, PlotlyFigure
from ..utils import setup_plot, apply_theme


def pdp_with_ice_overlay_static(
    grid: np.ndarray, ice_curves: np.ndarray, pdp: np.ndarray,
    feature_name: str, rug: Optional[np.ndarray] = None,
    title: Optional[str] = None, figsize: FigureSize = (10, 6),
    ice_color: str = "steelblue", pdp_color: str = "darkorange",
    alpha_ice: float = 0.15, theme: str = "default",
    dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """1-D PDP curve overlaid on ICE spaghetti with optional rug."""
    title = title or f"PDP + ICE — {feature_name}"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel=feature_name,
                             ylabel="Prediction", figsize=figsize)
        fig.set_dpi(dpi)
        for c in ice_curves:
            ax.plot(grid, c, color=ice_color, alpha=alpha_ice, linewidth=0.8)
        ax.plot(grid, pdp, color=pdp_color, linewidth=2.5, label="PDP")
        if rug is not None:
            ymin = ax.get_ylim()[0]
            ax.plot(rug, np.full_like(rug, ymin), "|", color="black",
                    markersize=6, alpha=0.4)
        ax.legend()
        ax.grid(True, alpha=0.3)
        apply_theme(ax, theme)
    return ax


def pdp_with_ice_overlay_interactive(
    grid: np.ndarray, ice_curves: np.ndarray, pdp: np.ndarray,
    feature_name: str, title: Optional[str] = None,
    figsize: FigureSize = (1000, 600), ice_color: str = "steelblue",
    pdp_color: str = "darkorange", alpha_ice: float = 0.2,
) -> PlotlyFigure:
    """Interactive PDP + ICE overlay."""
    fig = go.Figure()
    for c in ice_curves:
        fig.add_trace(go.Scatter(x=grid, y=c, mode="lines",
                                 line=dict(color=ice_color, width=1),
                                 opacity=alpha_ice, showlegend=False,
                                 hoverinfo="skip"))
    fig.add_trace(go.Scatter(x=grid, y=pdp, mode="lines",
                             line=dict(color=pdp_color, width=3), name="PDP"))
    fig.update_layout(title=title or f"PDP + ICE — {feature_name}",
                      xaxis_title=feature_name, yaxis_title="Prediction",
                      width=figsize[0], height=figsize[1])
    return fig


def ale_plot_2d_static(
    ale_grid: np.ndarray, x_edges: np.ndarray, y_edges: np.ndarray,
    feature_x: str, feature_y: str, title: Optional[str] = None,
    figsize: FigureSize = (9, 7), cmap: str = "RdBu_r",
    theme: str = "default", dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """2-D ALE heatmap for a pair of features."""
    vmax = float(np.abs(ale_grid).max() or 1.0)
    title = title or f"2-D ALE — {feature_x} × {feature_y}"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel=feature_x,
                             ylabel=feature_y, figsize=figsize)
        fig.set_dpi(dpi)
        im = ax.pcolormesh(x_edges, y_edges, ale_grid.T, cmap=cmap,
                           vmin=-vmax, vmax=vmax, shading="auto")
        fig.colorbar(im, ax=ax, label="ALE")
        apply_theme(ax, theme)
    return ax


def ale_plot_2d_interactive(
    ale_grid: np.ndarray, x_edges: np.ndarray, y_edges: np.ndarray,
    feature_x: str, feature_y: str, title: Optional[str] = None,
    figsize: FigureSize = (900, 700), colorscale: str = "RdBu",
) -> PlotlyFigure:
    """Interactive 2-D ALE heatmap."""
    vmax = float(np.abs(ale_grid).max() or 1.0)
    xc = 0.5 * (x_edges[:-1] + x_edges[1:])
    yc = 0.5 * (y_edges[:-1] + y_edges[1:])
    fig = go.Figure(go.Heatmap(z=ale_grid.T, x=xc, y=yc,
                               colorscale=colorscale, zmin=-vmax, zmax=vmax,
                               colorbar=dict(title="ALE")))
    fig.update_layout(title=title or f"2-D ALE — {feature_x} × {feature_y}",
                      xaxis_title=feature_x, yaxis_title=feature_y,
                      width=figsize[0], height=figsize[1])
    return fig


def h_statistic_heatmap_static(
    h_matrix: pd.DataFrame, title: Optional[str] = None,
    figsize: FigureSize = (8, 7), cmap: str = "magma",
    annot: bool = True, theme: str = "default",
    dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Friedman's H-statistic heatmap for pairwise feature interactions."""
    title = title or "Friedman H-statistic"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Feature",
                             ylabel="Feature", figsize=figsize)
        fig.set_dpi(dpi)
        im = ax.imshow(h_matrix.values, cmap=cmap, vmin=0,
                       vmax=float(h_matrix.values.max() or 1.0))
        ax.set_xticks(range(len(h_matrix.columns)))
        ax.set_xticklabels(h_matrix.columns, rotation=45, ha="right")
        ax.set_yticks(range(len(h_matrix.index)))
        ax.set_yticklabels(h_matrix.index)
        if annot:
            for i in range(h_matrix.shape[0]):
                for j in range(h_matrix.shape[1]):
                    ax.text(j, i, f"{h_matrix.values[i, j]:.2f}",
                            ha="center", va="center", fontsize=8,
                            color="white" if h_matrix.values[i, j] > 0.4 else "black")
        fig.colorbar(im, ax=ax, label="H")
        apply_theme(ax, theme)
    return ax


def h_statistic_heatmap_interactive(
    h_matrix: pd.DataFrame, title: Optional[str] = None,
    figsize: FigureSize = (800, 700), colorscale: str = "Magma",
) -> PlotlyFigure:
    """Interactive H-statistic heatmap."""
    fig = go.Figure(go.Heatmap(
        z=h_matrix.values, x=list(h_matrix.columns), y=list(h_matrix.index),
        colorscale=colorscale, text=np.round(h_matrix.values, 2),
        texttemplate="%{text}", colorbar=dict(title="H"),
    ))
    fig.update_layout(title=title or "Friedman H-statistic",
                      width=figsize[0], height=figsize[1])
    return fig


def interaction_network_static(
    interaction_matrix: pd.DataFrame, threshold: float = 0.1,
    title: Optional[str] = None, figsize: FigureSize = (9, 9),
    node_color: str = "steelblue", edge_cmap: str = "Reds",
    theme: str = "default", dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Network of strong feature interactions on a circular layout."""
    feats = list(interaction_matrix.index)
    n = len(feats)
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False)
    xs = np.cos(angles)
    ys = np.sin(angles)
    M = interaction_matrix.values
    vmax = float(M.max() or 1.0)
    cmap = plt.get_cmap(edge_cmap)
    title = title or "Interaction network"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="", ylabel="",
                             figsize=figsize)
        fig.set_dpi(dpi)
        for i in range(n):
            for j in range(i + 1, n):
                w = M[i, j]
                if w >= threshold:
                    ax.plot([xs[i], xs[j]], [ys[i], ys[j]],
                            color=cmap(w / vmax),
                            linewidth=0.5 + 4.0 * w / vmax,
                            alpha=0.85)
        ax.scatter(xs, ys, s=400, color=node_color,
                   edgecolors="black", zorder=3)
        for x, y, name in zip(xs, ys, feats):
            ax.text(1.1 * x, 1.1 * y, name, ha="center", va="center",
                    fontsize=9)
        ax.set_xlim(-1.4, 1.4)
        ax.set_ylim(-1.4, 1.4)
        ax.set_aspect("equal")
        ax.axis("off")
        apply_theme(ax, theme)
    return ax


def interaction_network_interactive(
    interaction_matrix: pd.DataFrame, threshold: float = 0.1,
    title: Optional[str] = None, figsize: FigureSize = (900, 800),
    node_color: str = "steelblue", edge_color: str = "indianred",
) -> PlotlyFigure:
    """Interactive interaction network on a circular layout."""
    feats = list(interaction_matrix.index)
    n = len(feats)
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False)
    xs = np.cos(angles)
    ys = np.sin(angles)
    M = interaction_matrix.values
    vmax = float(M.max() or 1.0)
    fig = go.Figure()
    for i in range(n):
        for j in range(i + 1, n):
            w = M[i, j]
            if w >= threshold:
                fig.add_trace(go.Scatter(
                    x=[xs[i], xs[j]], y=[ys[i], ys[j]], mode="lines",
                    line=dict(color=edge_color, width=1 + 6 * w / vmax),
                    opacity=0.8, hoverinfo="text",
                    text=f"{feats[i]} × {feats[j]}: {w:.2f}",
                    showlegend=False,
                ))
    fig.add_trace(go.Scatter(x=xs, y=ys, mode="markers+text",
                             marker=dict(size=22, color=node_color,
                                         line=dict(color="black", width=1)),
                             text=feats, textposition="top center",
                             showlegend=False))
    fig.update_layout(title=title or "Interaction network",
                      xaxis=dict(visible=False), yaxis=dict(visible=False,
                                                            scaleanchor="x"),
                      width=figsize[0], height=figsize[1])
    return fig
