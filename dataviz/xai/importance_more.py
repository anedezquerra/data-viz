"""Additional importance charts: gain, stability, correlation, clustering."""

from __future__ import annotations

from typing import Mapping, Optional, Sequence

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from ..types import FigureSize, MatplotlibAxes, PlotlyFigure
from ..utils import setup_plot, apply_theme


def gain_importance_bar_static(
    gain: Mapping[str, float], split_count: Optional[Mapping[str, float]] = None,
    top_n: Optional[int] = None, title: Optional[str] = None,
    figsize: FigureSize = (10, 6), color_gain: str = "steelblue",
    color_split: str = "darkorange", grid_alpha: float = 0.3,
    theme: str = "default", dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Tree-based gain importance with optional split-count dual axis."""
    items = sorted(gain.items(), key=lambda kv: kv[1])
    if top_n:
        items = items[-top_n:]
    names = [k for k, _ in items]
    g = np.array([v for _, v in items], dtype=float)
    title = title or "Gain importance"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Gain", ylabel="Feature",
                             figsize=figsize)
        fig.set_dpi(dpi)
        ax.barh(names, g, color=color_gain, alpha=0.85, edgecolor="black",
                label="Gain")
        ax.grid(True, axis="x", alpha=grid_alpha)
        if split_count is not None:
            s = np.array([split_count.get(k, 0) for k in names], dtype=float)
            ax2 = ax.twiny()
            ax2.plot(s, names, "o-", color=color_split, label="Split count")
            ax2.set_xlabel("Split count")
            ax2.legend(loc="lower right")
            ax.legend(loc="upper right")
        apply_theme(ax, theme)
    return ax


def gain_importance_bar_interactive(
    gain: Mapping[str, float], split_count: Optional[Mapping[str, float]] = None,
    top_n: Optional[int] = None, title: Optional[str] = None,
    figsize: FigureSize = (1000, 600), color_gain: str = "steelblue",
    color_split: str = "darkorange",
) -> PlotlyFigure:
    """Interactive gain importance dual-axis."""
    items = sorted(gain.items(), key=lambda kv: kv[1])
    if top_n:
        items = items[-top_n:]
    names = [k for k, _ in items]
    g = [v for _, v in items]
    fig = make_subplots(specs=[[{"secondary_y": False}]])
    fig.add_trace(go.Bar(x=g, y=names, orientation="h",
                         marker_color=color_gain, name="Gain"))
    if split_count is not None:
        s = [split_count.get(k, 0) for k in names]
        fig.add_trace(go.Scatter(x=s, y=names, mode="lines+markers",
                                 marker_color=color_split,
                                 name="Split count", xaxis="x2"))
        fig.update_layout(xaxis2=dict(overlaying="x", side="top",
                                      title="Split count"))
    fig.update_layout(title=title or "Gain importance",
                      xaxis_title="Gain", yaxis_title="Feature",
                      width=figsize[0], height=figsize[1])
    return fig


def importance_stability_plot_static(
    fold_importances: pd.DataFrame, top_n: Optional[int] = None,
    title: Optional[str] = None, figsize: FigureSize = (10, 6),
    color: str = "steelblue", grid_alpha: float = 0.3,
    theme: str = "default", dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Mean importance with CI bars across CV folds/seeds.

    ``fold_importances``: rows=folds, columns=features.
    """
    df = fold_importances
    mean = df.mean(axis=0)
    std = df.std(axis=0)
    order = mean.sort_values().index
    if top_n:
        order = order[-top_n:]
    title = title or "Importance stability (mean ± std)"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Importance", ylabel="Feature",
                             figsize=figsize)
        fig.set_dpi(dpi)
        ax.barh(order, mean.loc[order], xerr=std.loc[order],
                color=color, alpha=0.85, edgecolor="black", capsize=3)
        ax.grid(True, axis="x", alpha=grid_alpha)
        apply_theme(ax, theme)
    return ax


def importance_stability_plot_interactive(
    fold_importances: pd.DataFrame, top_n: Optional[int] = None,
    title: Optional[str] = None, figsize: FigureSize = (1000, 600),
    color: str = "steelblue",
) -> PlotlyFigure:
    """Interactive stability error-bar chart."""
    df = fold_importances
    mean = df.mean(axis=0)
    std = df.std(axis=0)
    order = mean.sort_values().index
    if top_n:
        order = order[-top_n:]
    fig = go.Figure(go.Bar(
        x=mean.loc[order], y=list(order), orientation="h",
        marker_color=color,
        error_x=dict(type="data", array=std.loc[order]),
    ))
    fig.update_layout(title=title or "Importance stability",
                      xaxis_title="Importance", yaxis_title="Feature",
                      width=figsize[0], height=figsize[1])
    return fig


def importance_correlation_heatmap_static(
    importances_by_model: pd.DataFrame, title: Optional[str] = None,
    figsize: FigureSize = (8, 7), cmap: str = "RdBu_r",
    annot: bool = True, theme: str = "default",
    dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Pearson correlation of importance vectors across models.

    Rows=features, columns=models.
    """
    corr = importances_by_model.corr()
    title = title or "Importance correlation across models"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="", ylabel="", figsize=figsize)
        fig.set_dpi(dpi)
        im = ax.imshow(corr.values, cmap=cmap, vmin=-1, vmax=1, aspect="auto")
        ax.set_xticks(range(len(corr.columns)))
        ax.set_xticklabels(corr.columns, rotation=45, ha="right")
        ax.set_yticks(range(len(corr.index)))
        ax.set_yticklabels(corr.index)
        if annot:
            for i in range(corr.shape[0]):
                for j in range(corr.shape[1]):
                    ax.text(j, i, f"{corr.values[i, j]:.2f}",
                            ha="center", va="center", fontsize=8,
                            color="black" if abs(corr.values[i, j]) < 0.6 else "white")
        fig.colorbar(im, ax=ax, label="r")
        apply_theme(ax, theme)
    return ax


def importance_correlation_heatmap_interactive(
    importances_by_model: pd.DataFrame, title: Optional[str] = None,
    figsize: FigureSize = (800, 700), colorscale: str = "RdBu",
) -> PlotlyFigure:
    """Interactive importance-correlation heatmap."""
    corr = importances_by_model.corr()
    fig = go.Figure(go.Heatmap(
        z=corr.values, x=list(corr.columns), y=list(corr.index),
        colorscale=colorscale, zmin=-1, zmax=1,
        text=np.round(corr.values, 2), texttemplate="%{text}",
    ))
    fig.update_layout(title=title or "Importance correlation across models",
                      width=figsize[0], height=figsize[1])
    return fig


def feature_clustermap_static(
    importance_matrix: pd.DataFrame, title: Optional[str] = None,
    figsize: FigureSize = (10, 8), cmap: str = "viridis",
    theme: str = "default", dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Hierarchical clustering of features by importance signature.

    Rows=features, columns=models/folds. Reorders rows by 1-D correlation
    distance via greedy nearest-neighbor (no scipy dependency).
    """
    df = importance_matrix
    vals = df.values
    n = vals.shape[0]
    if n > 1:
        dist = 1.0 - np.corrcoef(vals)
        np.fill_diagonal(dist, np.inf)
        order = [0]
        remaining = set(range(1, n))
        while remaining:
            last = order[-1]
            nxt = min(remaining, key=lambda j: dist[last, j])
            order.append(nxt)
            remaining.remove(nxt)
    else:
        order = list(range(n))
    df_ord = df.iloc[order]
    title = title or "Feature clustermap"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Model/Fold",
                             ylabel="Feature", figsize=figsize)
        fig.set_dpi(dpi)
        im = ax.imshow(df_ord.values, cmap=cmap, aspect="auto")
        ax.set_xticks(range(len(df_ord.columns)))
        ax.set_xticklabels(df_ord.columns, rotation=45, ha="right")
        ax.set_yticks(range(len(df_ord.index)))
        ax.set_yticklabels(df_ord.index)
        fig.colorbar(im, ax=ax, label="Importance")
        apply_theme(ax, theme)
    return ax


def feature_clustermap_interactive(
    importance_matrix: pd.DataFrame, title: Optional[str] = None,
    figsize: FigureSize = (1000, 800), colorscale: str = "Viridis",
) -> PlotlyFigure:
    """Interactive feature clustermap."""
    df = importance_matrix
    vals = df.values
    n = vals.shape[0]
    if n > 1:
        dist = 1.0 - np.corrcoef(vals)
        np.fill_diagonal(dist, np.inf)
        order = [0]
        remaining = set(range(1, n))
        while remaining:
            last = order[-1]
            nxt = min(remaining, key=lambda j: dist[last, j])
            order.append(nxt)
            remaining.remove(nxt)
    else:
        order = list(range(n))
    df_ord = df.iloc[order]
    fig = go.Figure(go.Heatmap(
        z=df_ord.values, x=list(df_ord.columns), y=list(df_ord.index),
        colorscale=colorscale,
    ))
    fig.update_layout(title=title or "Feature clustermap",
                      xaxis_title="Model/Fold", yaxis_title="Feature",
                      width=figsize[0], height=figsize[1])
    return fig
