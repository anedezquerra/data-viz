"""Feature importance visualizations for regression models."""

from __future__ import annotations

from typing import Optional, Sequence

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from ..types import ArrayLike, FigureSize, MatplotlibAxes, PlotlyFigure
from ..utils import setup_plot, apply_theme
from .helpers import _as_array


def feature_importance_regression_static(
    importances: ArrayLike,
    feature_names: Optional[Sequence[str]] = None,
    top_n: Optional[int] = None,
    title: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    color: str = "#4c78a8",
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Horizontal bar chart of model feature importances (descending)."""
    imp = _as_array(importances)
    names = list(feature_names) if feature_names is not None else [f"x{i}" for i in range(imp.size)]
    if len(names) != imp.size:
        raise ValueError("feature_names length must match importances.")
    order = np.argsort(imp)[::-1]
    if top_n is not None:
        order = order[:top_n]
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Feature Importance",
                             xlabel="Importance", ylabel="Feature", figsize=figsize)
        fig.set_dpi(dpi)
        ax.barh(np.array(names)[order][::-1], imp[order][::-1], color=color,
                alpha=0.85, **kwargs)
        if grid:
            ax.grid(True, alpha=grid_alpha, axis="x")
        apply_theme(ax, theme)
    return ax


def feature_importance_regression_interactive(
    importances: ArrayLike,
    feature_names: Optional[Sequence[str]] = None,
    top_n: Optional[int] = None,
    title: Optional[str] = None,
    color: str = "#4c78a8",
    template: str = "plotly",
    height: int = 600,
    width: int = 900,
    **kwargs,
) -> PlotlyFigure:
    """Interactive feature-importance bar chart."""
    imp = _as_array(importances)
    names = list(feature_names) if feature_names is not None else [f"x{i}" for i in range(imp.size)]
    order = np.argsort(imp)[::-1]
    if top_n is not None:
        order = order[:top_n]
    fig = go.Figure()
    fig.add_trace(go.Bar(x=imp[order][::-1], y=np.array(names)[order][::-1],
                         orientation="h", marker_color=color,
                         name="Importance", **kwargs))
    fig.update_layout(title=title or "Feature Importance",
                      xaxis_title="Importance", yaxis_title="Feature",
                      template=template, height=height, width=width)
    return fig


def permutation_importance_regression_static(
    importances_mean: ArrayLike,
    importances_std: ArrayLike,
    feature_names: Optional[Sequence[str]] = None,
    top_n: Optional[int] = None,
    title: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    color: str = "#4c78a8",
    error_color: str = "#444",
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Permutation-importance plot with mean ± standard deviation error bars."""
    means = _as_array(importances_mean)
    stds = _as_array(importances_std)
    if means.shape != stds.shape:
        raise ValueError("means and stds must have the same shape.")
    names = list(feature_names) if feature_names is not None else [f"x{i}" for i in range(means.size)]
    order = np.argsort(means)[::-1]
    if top_n is not None:
        order = order[:top_n]
    sorted_names = np.array(names)[order][::-1]
    sorted_means = means[order][::-1]
    sorted_stds = stds[order][::-1]
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Permutation Importance",
                             xlabel="Importance (mean)", ylabel="Feature",
                             figsize=figsize)
        fig.set_dpi(dpi)
        ax.barh(sorted_names, sorted_means, xerr=sorted_stds, color=color,
                ecolor=error_color, alpha=0.85, capsize=4, **kwargs)
        if grid:
            ax.grid(True, alpha=grid_alpha, axis="x")
        apply_theme(ax, theme)
    return ax


def permutation_importance_regression_interactive(
    importances_mean: ArrayLike,
    importances_std: ArrayLike,
    feature_names: Optional[Sequence[str]] = None,
    top_n: Optional[int] = None,
    title: Optional[str] = None,
    color: str = "#4c78a8",
    error_color: str = "#444",
    template: str = "plotly",
    height: int = 600,
    width: int = 950,
    **kwargs,
) -> PlotlyFigure:
    """Interactive permutation-importance chart."""
    means = _as_array(importances_mean)
    stds = _as_array(importances_std)
    names = list(feature_names) if feature_names is not None else [f"x{i}" for i in range(means.size)]
    order = np.argsort(means)[::-1]
    if top_n is not None:
        order = order[:top_n]
    sorted_names = np.array(names)[order][::-1]
    sorted_means = means[order][::-1]
    sorted_stds = stds[order][::-1]
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=sorted_means, y=sorted_names, orientation="h", marker_color=color,
        error_x=dict(type="data", array=sorted_stds, color=error_color, thickness=2),
        name="Importance", **kwargs,
    ))
    fig.update_layout(title=title or "Permutation Importance",
                      xaxis_title="Importance (mean)", yaxis_title="Feature",
                      template=template, height=height, width=width)
    return fig


feature_importance_regression = feature_importance_regression_static
permutation_importance_regression = permutation_importance_regression_static
