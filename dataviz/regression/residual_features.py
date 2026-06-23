"""Residual vs feature diagnostics: feature plots, partial residuals, AVP."""

from __future__ import annotations

from typing import Optional, Sequence

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from ..types import ArrayLike, FigureSize, MatplotlibAxes, MatrixLike, PlotlyFigure
from ..utils import setup_plot, apply_theme
from .helpers import _as_array, _as_matrix, _residuals


def _ols_fit(X: np.ndarray, y: np.ndarray) -> np.ndarray:
    return np.linalg.pinv(X.T @ X) @ X.T @ y


# ---------------------------------------------------------------------------
# Residual vs feature
# ---------------------------------------------------------------------------

def residual_vs_feature_static(
    feature: ArrayLike,
    y_true: ArrayLike,
    y_pred: ArrayLike,
    feature_name: str = "feature",
    title: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    color: str = "#4c78a8",
    trend: bool = True,
    trend_color: str = "#e45756",
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Scatter of residuals against a single feature with optional smooth trend."""
    res = _residuals(y_true, y_pred)
    x = _as_array(feature)
    if x.size != res.size:
        raise ValueError("feature must align with y_true / y_pred.")
    order = np.argsort(x)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or f"Residual vs {feature_name}",
                             xlabel=feature_name, ylabel="Residual", figsize=figsize)
        fig.set_dpi(dpi)
        ax.scatter(x, res, color=color, alpha=0.7, **kwargs)
        ax.axhline(0.0, color="#444", linestyle="--", linewidth=1)
        if trend and x.size >= 5:
            window = max(5, x.size // 20)
            roll = pd.Series(res[order]).rolling(window, min_periods=1, center=True).mean()
            ax.plot(x[order], roll, color=trend_color, linewidth=2)
        if grid:
            ax.grid(True, alpha=grid_alpha)
        apply_theme(ax, theme)
    return ax


def residual_vs_feature_interactive(
    feature: ArrayLike,
    y_true: ArrayLike,
    y_pred: ArrayLike,
    feature_name: str = "feature",
    title: Optional[str] = None,
    color: str = "#4c78a8",
    trend: bool = True,
    trend_color: str = "#e45756",
    template: str = "plotly",
    height: int = 600,
    width: int = 1000,
    **kwargs,
) -> PlotlyFigure:
    """Interactive scatter of residuals vs a single feature."""
    res = _residuals(y_true, y_pred)
    x = _as_array(feature)
    order = np.argsort(x)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=res, mode="markers",
                             marker=dict(color=color), name="Residual", **kwargs))
    fig.add_hline(y=0.0, line_dash="dash", line_color="#444")
    if trend and x.size >= 5:
        window = max(5, x.size // 20)
        roll = pd.Series(res[order]).rolling(window, min_periods=1, center=True).mean()
        fig.add_trace(go.Scatter(x=x[order], y=roll, mode="lines",
                                 line=dict(color=trend_color, width=2),
                                 name="Smoothed trend"))
    fig.update_layout(title=title or f"Residual vs {feature_name}",
                      xaxis_title=feature_name, yaxis_title="Residual",
                      template=template, height=height, width=width)
    return fig


# ---------------------------------------------------------------------------
# Partial residual plot
# ---------------------------------------------------------------------------

def partial_residual_plot_static(
    X: MatrixLike,
    y_true: ArrayLike,
    feature_index: int,
    feature_name: Optional[str] = None,
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
    """Partial residual plot for the chosen feature in an OLS fit.

    The partial residual is ``e + β_j · X_j``; it shows the marginal effect of
    feature ``j`` while accounting for the other predictors.
    """
    X_mat = _as_matrix(X)
    y_t = _as_array(y_true)
    if feature_index < 0 or feature_index >= X_mat.shape[1]:
        raise IndexError("feature_index out of range.")
    X_aug = np.column_stack([np.ones(X_mat.shape[0]), X_mat])
    beta = _ols_fit(X_aug, y_t)
    fitted = X_aug @ beta
    resid = y_t - fitted
    bj = beta[feature_index + 1]
    xj = X_mat[:, feature_index]
    partial = resid + bj * xj
    name = feature_name or f"x{feature_index}"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or f"Partial Residual ({name})",
                             xlabel=name, ylabel="Partial residual", figsize=figsize)
        fig.set_dpi(dpi)
        ax.scatter(xj, partial, color=color, alpha=0.7, **kwargs)
        xs = np.array([xj.min(), xj.max()])
        ax.plot(xs, bj * xs + np.mean(partial - bj * xj), color=line_color, linewidth=2)
        if grid:
            ax.grid(True, alpha=grid_alpha)
        apply_theme(ax, theme)
    return ax


def partial_residual_plot_interactive(
    X: MatrixLike,
    y_true: ArrayLike,
    feature_index: int,
    feature_name: Optional[str] = None,
    title: Optional[str] = None,
    color: str = "#4c78a8",
    line_color: str = "#e45756",
    template: str = "plotly",
    height: int = 600,
    width: int = 1000,
    **kwargs,
) -> PlotlyFigure:
    """Interactive partial residual plot for OLS."""
    X_mat = _as_matrix(X)
    y_t = _as_array(y_true)
    X_aug = np.column_stack([np.ones(X_mat.shape[0]), X_mat])
    beta = _ols_fit(X_aug, y_t)
    fitted = X_aug @ beta
    resid = y_t - fitted
    bj = beta[feature_index + 1]
    xj = X_mat[:, feature_index]
    partial = resid + bj * xj
    name = feature_name or f"x{feature_index}"
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=xj, y=partial, mode="markers",
                             marker=dict(color=color), name="Partial residual", **kwargs))
    xs = np.array([xj.min(), xj.max()])
    fig.add_trace(go.Scatter(x=xs, y=bj * xs + np.mean(partial - bj * xj),
                             mode="lines", line=dict(color=line_color, width=2),
                             name=f"Slope β={bj:.3g}"))
    fig.update_layout(title=title or f"Partial Residual ({name})",
                      xaxis_title=name, yaxis_title="Partial residual",
                      template=template, height=height, width=width)
    return fig


# ---------------------------------------------------------------------------
# CCPR (component + component plus residual)
# ---------------------------------------------------------------------------

def ccpr_plot_static(
    X: MatrixLike,
    y_true: ArrayLike,
    feature_index: int,
    feature_name: Optional[str] = None,
    title: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    component_color: str = "#4c78a8",
    residual_color: str = "#bbbbbb",
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """CCPR plot: linear fit component plus residuals as a scatter overlay."""
    X_mat = _as_matrix(X)
    y_t = _as_array(y_true)
    X_aug = np.column_stack([np.ones(X_mat.shape[0]), X_mat])
    beta = _ols_fit(X_aug, y_t)
    resid = y_t - X_aug @ beta
    bj = beta[feature_index + 1]
    xj = X_mat[:, feature_index]
    component = bj * xj
    name = feature_name or f"x{feature_index}"
    order = np.argsort(xj)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or f"CCPR ({name})",
                             xlabel=name, ylabel="Component + residual",
                             figsize=figsize)
        fig.set_dpi(dpi)
        ax.scatter(xj, component + resid, color=residual_color, alpha=0.6, **kwargs)
        ax.plot(xj[order], component[order], color=component_color, linewidth=2,
                label=f"β·{name}")
        ax.legend()
        if grid:
            ax.grid(True, alpha=grid_alpha)
        apply_theme(ax, theme)
    return ax


def ccpr_plot_interactive(
    X: MatrixLike,
    y_true: ArrayLike,
    feature_index: int,
    feature_name: Optional[str] = None,
    title: Optional[str] = None,
    component_color: str = "#4c78a8",
    residual_color: str = "#bbbbbb",
    template: str = "plotly",
    height: int = 600,
    width: int = 1000,
    **kwargs,
) -> PlotlyFigure:
    """Interactive CCPR plot."""
    X_mat = _as_matrix(X)
    y_t = _as_array(y_true)
    X_aug = np.column_stack([np.ones(X_mat.shape[0]), X_mat])
    beta = _ols_fit(X_aug, y_t)
    resid = y_t - X_aug @ beta
    bj = beta[feature_index + 1]
    xj = X_mat[:, feature_index]
    component = bj * xj
    name = feature_name or f"x{feature_index}"
    order = np.argsort(xj)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=xj, y=component + resid, mode="markers",
                             marker=dict(color=residual_color),
                             name="Component + residual", **kwargs))
    fig.add_trace(go.Scatter(x=xj[order], y=component[order], mode="lines",
                             line=dict(color=component_color, width=2),
                             name=f"β·{name}"))
    fig.update_layout(title=title or f"CCPR ({name})",
                      xaxis_title=name, yaxis_title="Component + residual",
                      template=template, height=height, width=width)
    return fig


# ---------------------------------------------------------------------------
# Added variable plot (partial regression)
# ---------------------------------------------------------------------------

def added_variable_plot_static(
    X: MatrixLike,
    y_true: ArrayLike,
    feature_index: int,
    feature_name: Optional[str] = None,
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
    """Added-variable (partial regression) plot for feature ``feature_index``."""
    X_mat = _as_matrix(X)
    y_t = _as_array(y_true)
    if feature_index < 0 or feature_index >= X_mat.shape[1]:
        raise IndexError("feature_index out of range.")
    others = np.delete(X_mat, feature_index, axis=1)
    Z = np.column_stack([np.ones(X_mat.shape[0]), others])
    beta_y = _ols_fit(Z, y_t)
    e_y = y_t - Z @ beta_y
    xj = X_mat[:, feature_index]
    beta_x = _ols_fit(Z, xj)
    e_x = xj - Z @ beta_x
    slope = float(np.dot(e_x, e_y) / max(np.dot(e_x, e_x), 1e-12))
    name = feature_name or f"x{feature_index}"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or f"Added Variable ({name})",
                             xlabel=f"e({name} | others)",
                             ylabel="e(y | others)", figsize=figsize)
        fig.set_dpi(dpi)
        ax.scatter(e_x, e_y, color=color, alpha=0.7, **kwargs)
        xs = np.array([e_x.min(), e_x.max()])
        ax.plot(xs, slope * xs, color=line_color, linewidth=2, label=f"β={slope:.3g}")
        ax.legend()
        if grid:
            ax.grid(True, alpha=grid_alpha)
        apply_theme(ax, theme)
    return ax


def added_variable_plot_interactive(
    X: MatrixLike,
    y_true: ArrayLike,
    feature_index: int,
    feature_name: Optional[str] = None,
    title: Optional[str] = None,
    color: str = "#4c78a8",
    line_color: str = "#e45756",
    template: str = "plotly",
    height: int = 600,
    width: int = 1000,
    **kwargs,
) -> PlotlyFigure:
    """Interactive added-variable plot."""
    X_mat = _as_matrix(X)
    y_t = _as_array(y_true)
    others = np.delete(X_mat, feature_index, axis=1)
    Z = np.column_stack([np.ones(X_mat.shape[0]), others])
    e_y = y_t - Z @ _ols_fit(Z, y_t)
    xj = X_mat[:, feature_index]
    e_x = xj - Z @ _ols_fit(Z, xj)
    slope = float(np.dot(e_x, e_y) / max(np.dot(e_x, e_x), 1e-12))
    name = feature_name or f"x{feature_index}"
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=e_x, y=e_y, mode="markers",
                             marker=dict(color=color),
                             name="Partial residual", **kwargs))
    xs = np.array([e_x.min(), e_x.max()])
    fig.add_trace(go.Scatter(x=xs, y=slope * xs, mode="lines",
                             line=dict(color=line_color, width=2),
                             name=f"β={slope:.3g}"))
    fig.update_layout(title=title or f"Added Variable ({name})",
                      xaxis_title=f"e({name} | others)",
                      yaxis_title="e(y | others)",
                      template=template, height=height, width=width)
    return fig


# Convenience aliases
residual_vs_feature = residual_vs_feature_static
partial_residual_plot = partial_residual_plot_static
ccpr_plot = ccpr_plot_static
added_variable_plot = added_variable_plot_static
