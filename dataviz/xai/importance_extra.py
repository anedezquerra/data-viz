"""Extended feature-importance charts: permutation, group comparison, distributions."""

from __future__ import annotations

from typing import Mapping, Optional, Sequence

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from ..types import ArrayLike, FigureSize, MatplotlibAxes, PlotlyFigure
from ..utils import setup_plot, apply_theme


def permutation_importance_bar_static(
    importances: Mapping[str, float], std: Optional[Mapping[str, float]] = None,
    top_n: Optional[int] = None, title: Optional[str] = None,
    figsize: FigureSize = (10, 6), color: str = "steelblue",
    grid: bool = True, grid_alpha: float = 0.3, theme: str = "default",
    dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Horizontal permutation-importance bar with optional error bars."""
    items = sorted(importances.items(), key=lambda kv: kv[1])
    if top_n:
        items = items[-top_n:]
    names = [k for k, _ in items]
    vals = np.array([v for _, v in items])
    errs = np.array([std[k] for k in names]) if std else None
    title = title or "Permutation importance"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Decrease in score",
                             ylabel="Feature", figsize=figsize)
        fig.set_dpi(dpi)
        ax.barh(names, vals, color=color, alpha=0.85, edgecolor="black",
                xerr=errs, capsize=3)
        if grid:
            ax.grid(True, axis="x", alpha=grid_alpha)
        apply_theme(ax, theme)
    return ax


def permutation_importance_bar_interactive(
    importances: Mapping[str, float], std: Optional[Mapping[str, float]] = None,
    top_n: Optional[int] = None, title: Optional[str] = None,
    height: int = 600, width: int = 800, template: str = "plotly",
) -> PlotlyFigure:
    items = sorted(importances.items(), key=lambda kv: kv[1])
    if top_n:
        items = items[-top_n:]
    names = [k for k, _ in items]
    vals = [v for _, v in items]
    errs = [std[k] for k in names] if std else None
    fig = go.Figure(go.Bar(x=vals, y=names, orientation="h",
                           error_x=dict(type="data", array=errs) if errs else None,
                           marker_color="steelblue"))
    fig.update_layout(title=title or "Permutation importance",
                      xaxis_title="Decrease in score", yaxis_title="Feature",
                      template=template, height=height, width=width)
    return fig


def feature_importance_grouped_bar_static(
    importances: Mapping[str, Mapping[str, float]], top_n: Optional[int] = None,
    title: Optional[str] = None, figsize: FigureSize = (12, 7),
    grid: bool = True, grid_alpha: float = 0.3, theme: str = "default",
    dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Grouped horizontal bars comparing importances across multiple models.

    Args:
        importances: ``{model_name: {feature: value, ...}, ...}`` with shared
            feature keys across models.
    """
    model_names = list(importances.keys())
    feature_names = list(next(iter(importances.values())).keys())
    if top_n:
        agg = {f: np.mean([importances[m][f] for m in model_names])
               for f in feature_names}
        feature_names = [f for f, _ in sorted(agg.items(),
                                              key=lambda kv: -kv[1])[:top_n]]
    n_models = len(model_names)
    bar_h = 0.8 / n_models
    y = np.arange(len(feature_names))[::-1]
    title = title or "Feature importance across models"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Importance",
                             ylabel="Feature", figsize=figsize)
        fig.set_dpi(dpi)
        for i, m in enumerate(model_names):
            vals = [importances[m][f] for f in feature_names]
            ax.barh(y + (i - (n_models - 1) / 2) * bar_h, vals,
                    height=bar_h, label=m, alpha=0.85, edgecolor="black")
        ax.set_yticks(y); ax.set_yticklabels(feature_names)
        if grid:
            ax.grid(True, axis="x", alpha=grid_alpha)
        ax.legend()
        apply_theme(ax, theme)
    return ax


def feature_importance_grouped_bar_interactive(
    importances: Mapping[str, Mapping[str, float]], top_n: Optional[int] = None,
    title: Optional[str] = None, height: int = 700, width: int = 900,
    template: str = "plotly",
) -> PlotlyFigure:
    model_names = list(importances.keys())
    feature_names = list(next(iter(importances.values())).keys())
    if top_n:
        agg = {f: np.mean([importances[m][f] for m in model_names])
               for f in feature_names}
        feature_names = [f for f, _ in sorted(agg.items(),
                                              key=lambda kv: -kv[1])[:top_n]]
    fig = go.Figure()
    for m in model_names:
        fig.add_trace(go.Bar(y=feature_names,
                             x=[importances[m][f] for f in feature_names],
                             orientation="h", name=m))
    fig.update_layout(title=title or "Feature importance across models",
                      barmode="group", xaxis_title="Importance",
                      yaxis_title="Feature", template=template,
                      height=height, width=width)
    return fig


def feature_importance_boxplot_static(
    per_fold: Mapping[str, Sequence[float]], top_n: Optional[int] = None,
    title: Optional[str] = None, figsize: FigureSize = (10, 7),
    grid: bool = True, grid_alpha: float = 0.3, theme: str = "default",
    dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Boxplot of per-fold (or per-repeat) importances per feature."""
    items = sorted(per_fold.items(),
                   key=lambda kv: float(np.median(list(kv[1]))))
    if top_n:
        items = items[-top_n:]
    names = [k for k, _ in items]
    data = [list(v) for _, v in items]
    title = title or "Permutation importance distribution"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Importance",
                             ylabel="Feature", figsize=figsize)
        fig.set_dpi(dpi)
        ax.boxplot(data, vert=False, widths=0.55)
        ax.set_yticks(range(1, len(names) + 1))
        ax.set_yticklabels(names)
        if grid:
            ax.grid(True, axis="x", alpha=grid_alpha)
        apply_theme(ax, theme)
    return ax


def feature_importance_boxplot_interactive(
    per_fold: Mapping[str, Sequence[float]], top_n: Optional[int] = None,
    title: Optional[str] = None, height: int = 700, width: int = 800,
    template: str = "plotly",
) -> PlotlyFigure:
    items = sorted(per_fold.items(),
                   key=lambda kv: float(np.median(list(kv[1]))))
    if top_n:
        items = items[-top_n:]
    fig = go.Figure()
    for name, vals in items:
        fig.add_trace(go.Box(x=list(vals), name=name, orientation="h",
                             boxpoints="outliers"))
    fig.update_layout(title=title or "Permutation importance distribution",
                      xaxis_title="Importance", template=template,
                      height=height, width=width, showlegend=False)
    return fig


def drop_column_importance_bar_static(
    deltas: Mapping[str, float], top_n: Optional[int] = None,
    title: Optional[str] = None, figsize: FigureSize = (10, 7),
    grid: bool = True, grid_alpha: float = 0.3, theme: str = "default",
    dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Signed drop-column importance (positive = column matters)."""
    items = sorted(deltas.items(), key=lambda kv: kv[1])
    if top_n:
        items = items[-top_n:]
    names = [k for k, _ in items]
    vals = [v for _, v in items]
    title = title or "Drop-column importance"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Score drop when removed",
                             ylabel="Feature", figsize=figsize)
        fig.set_dpi(dpi)
        colors = ["tab:red" if v < 0 else "tab:blue" for v in vals]
        ax.barh(names, vals, color=colors, alpha=0.85, edgecolor="black")
        ax.axvline(0, color="black", linewidth=0.7)
        if grid:
            ax.grid(True, axis="x", alpha=grid_alpha)
        apply_theme(ax, theme)
    return ax


def drop_column_importance_bar_interactive(
    deltas: Mapping[str, float], top_n: Optional[int] = None,
    title: Optional[str] = None, height: int = 700, width: int = 800,
    template: str = "plotly",
) -> PlotlyFigure:
    items = sorted(deltas.items(), key=lambda kv: kv[1])
    if top_n:
        items = items[-top_n:]
    names = [k for k, _ in items]
    vals = [v for _, v in items]
    colors = ["red" if v < 0 else "steelblue" for v in vals]
    fig = go.Figure(go.Bar(x=vals, y=names, orientation="h",
                           marker_color=colors))
    fig.add_vline(x=0, line_color="black", line_width=1)
    fig.update_layout(title=title or "Drop-column importance",
                      xaxis_title="Score drop when removed",
                      yaxis_title="Feature", template=template,
                      height=height, width=width)
    return fig


def importance_method_scatter_static(
    a: Mapping[str, float], b: Mapping[str, float],
    a_name: str = "method A", b_name: str = "method B",
    title: Optional[str] = None, figsize: FigureSize = (8, 8),
    grid: bool = True, grid_alpha: float = 0.3, theme: str = "default",
    dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Scatter of two importance rankings to assess method agreement."""
    keys = sorted(set(a) & set(b))
    xs = np.array([a[k] for k in keys])
    ys = np.array([b[k] for k in keys])
    title = title or f"{a_name} vs {b_name}"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel=a_name, ylabel=b_name,
                             figsize=figsize)
        fig.set_dpi(dpi)
        ax.scatter(xs, ys, s=60, alpha=0.7, edgecolor="black")
        for k, x, y in zip(keys, xs, ys):
            ax.annotate(k, (x, y), fontsize=8, alpha=0.7)
        lo = float(min(xs.min(), ys.min())); hi = float(max(xs.max(), ys.max()))
        ax.plot([lo, hi], [lo, hi], "--", color="grey", label="y = x")
        if grid:
            ax.grid(True, alpha=grid_alpha)
        ax.legend()
        apply_theme(ax, theme)
    return ax


def importance_method_scatter_interactive(
    a: Mapping[str, float], b: Mapping[str, float],
    a_name: str = "method A", b_name: str = "method B",
    title: Optional[str] = None, height: int = 600, width: int = 700,
    template: str = "plotly",
) -> PlotlyFigure:
    keys = sorted(set(a) & set(b))
    xs = [a[k] for k in keys]; ys = [b[k] for k in keys]
    lo = min(min(xs), min(ys)); hi = max(max(xs), max(ys))
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=xs, y=ys, mode="markers+text", text=keys,
                             textposition="top center",
                             marker=dict(size=12, opacity=0.7,
                                          line=dict(width=1, color="black"))))
    fig.add_trace(go.Scatter(x=[lo, hi], y=[lo, hi], mode="lines",
                             line=dict(dash="dash", color="grey"), name="y = x"))
    fig.update_layout(title=title or f"{a_name} vs {b_name}",
                      xaxis_title=a_name, yaxis_title=b_name,
                      template=template, height=height, width=width)
    return fig
