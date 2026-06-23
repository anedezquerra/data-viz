"""Coefficient visualizations: bar, forest, standardized, and regularization paths."""

from __future__ import annotations

from typing import Optional, Sequence

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from ..types import ArrayLike, FigureSize, MatplotlibAxes, MatrixLike, PlotlyFigure
from ..utils import setup_plot, apply_theme
from .helpers import coefficient_table, _as_array, _as_matrix


# ---------------------------------------------------------------------------
# Coefficient plot
# ---------------------------------------------------------------------------

def coefficient_plot_static(
    coefficients: ArrayLike,
    feature_names: Optional[Sequence[str]] = None,
    title: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    positive_color: str = "#4c78a8",
    negative_color: str = "#e45756",
    sort: bool = True,
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Horizontal bar chart of coefficients colored by sign."""
    coefs = _as_array(coefficients)
    names = list(feature_names) if feature_names is not None else [f"x{i}" for i in range(coefs.size)]
    if len(names) != coefs.size:
        raise ValueError("feature_names length must match coefficients.")
    order = np.argsort(coefs) if sort else np.arange(coefs.size)
    sorted_coefs = coefs[order]
    sorted_names = np.array(names)[order]
    colors = [positive_color if c >= 0 else negative_color for c in sorted_coefs]
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Coefficients",
                             xlabel="Coefficient", ylabel="Feature", figsize=figsize)
        fig.set_dpi(dpi)
        ax.barh(sorted_names, sorted_coefs, color=colors, alpha=0.85, **kwargs)
        ax.axvline(0.0, color="#444", linewidth=1)
        if grid:
            ax.grid(True, alpha=grid_alpha, axis="x")
        apply_theme(ax, theme)
    return ax


def coefficient_plot_interactive(
    coefficients: ArrayLike,
    feature_names: Optional[Sequence[str]] = None,
    title: Optional[str] = None,
    positive_color: str = "#4c78a8",
    negative_color: str = "#e45756",
    sort: bool = True,
    template: str = "plotly",
    height: int = 600,
    width: int = 900,
    **kwargs,
) -> PlotlyFigure:
    """Interactive coefficient bar chart."""
    coefs = _as_array(coefficients)
    names = list(feature_names) if feature_names is not None else [f"x{i}" for i in range(coefs.size)]
    order = np.argsort(coefs) if sort else np.arange(coefs.size)
    sorted_coefs = coefs[order]
    sorted_names = np.array(names)[order]
    colors = [positive_color if c >= 0 else negative_color for c in sorted_coefs]
    fig = go.Figure()
    fig.add_trace(go.Bar(x=sorted_coefs, y=sorted_names, orientation="h",
                         marker_color=colors, name="Coefficient", **kwargs))
    fig.add_vline(x=0.0, line_color="#444")
    fig.update_layout(title=title or "Coefficients",
                      xaxis_title="Coefficient", yaxis_title="Feature",
                      template=template, height=height, width=width)
    return fig


# ---------------------------------------------------------------------------
# Coefficient forest plot (with CIs)
# ---------------------------------------------------------------------------

def coefficient_forest_plot_static(
    X: MatrixLike,
    y_true: ArrayLike,
    feature_names: Optional[Sequence[str]] = None,
    include_intercept: bool = True,
    title: Optional[str] = None,
    figsize: FigureSize = (10, 7),
    color: str = "#4c78a8",
    error_color: str = "#444",
    sort: bool = True,
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Forest plot: OLS coefficients with 95% confidence intervals."""
    table = coefficient_table(X, y_true, feature_names=feature_names,
                              include_intercept=include_intercept)
    if sort:
        table = table.sort_values("coef")
    ys = np.arange(len(table))
    errs = np.array([table["coef"] - table["ci_low"], table["ci_high"] - table["coef"]])
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Coefficient Forest (95% CI)",
                             xlabel="Coefficient", ylabel="Feature", figsize=figsize)
        fig.set_dpi(dpi)
        ax.errorbar(table["coef"], ys, xerr=errs, fmt="o", color=color,
                    ecolor=error_color, capsize=4, **kwargs)
        ax.set_yticks(ys)
        ax.set_yticklabels(table["feature"])
        ax.axvline(0.0, color="#444", linestyle="--", linewidth=1)
        if grid:
            ax.grid(True, alpha=grid_alpha, axis="x")
        apply_theme(ax, theme)
    return ax


def coefficient_forest_plot_interactive(
    X: MatrixLike,
    y_true: ArrayLike,
    feature_names: Optional[Sequence[str]] = None,
    include_intercept: bool = True,
    title: Optional[str] = None,
    color: str = "#4c78a8",
    error_color: str = "#444",
    sort: bool = True,
    template: str = "plotly",
    height: int = 650,
    width: int = 900,
    **kwargs,
) -> PlotlyFigure:
    """Interactive coefficient forest plot with 95% CI bars."""
    table = coefficient_table(X, y_true, feature_names=feature_names,
                              include_intercept=include_intercept)
    if sort:
        table = table.sort_values("coef")
    err_plus = (table["ci_high"] - table["coef"]).to_numpy()
    err_minus = (table["coef"] - table["ci_low"]).to_numpy()
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=table["coef"], y=table["feature"], mode="markers",
        marker=dict(color=color, size=10),
        error_x=dict(type="data", array=err_plus, arrayminus=err_minus,
                     color=error_color, thickness=2),
        name="Coefficient", **kwargs,
    ))
    fig.add_vline(x=0.0, line_dash="dash", line_color="#444")
    fig.update_layout(title=title or "Coefficient Forest (95% CI)",
                      xaxis_title="Coefficient", yaxis_title="Feature",
                      template=template, height=height, width=width)
    return fig


# ---------------------------------------------------------------------------
# Standardized coefficient plot
# ---------------------------------------------------------------------------

def standardized_coefficient_plot_static(
    X: MatrixLike,
    y_true: ArrayLike,
    feature_names: Optional[Sequence[str]] = None,
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
    """Bar chart of standardized OLS coefficients (β · σ_x / σ_y)."""
    X_mat = _as_matrix(X)
    y_t = _as_array(y_true)
    names = list(feature_names) if feature_names is not None else [f"x{i}" for i in range(X_mat.shape[1])]
    sigma_x = np.std(X_mat, axis=0, ddof=1)
    sigma_y = float(np.std(y_t, ddof=1)) if y_t.size > 1 else 1.0
    X_aug = np.column_stack([np.ones(X_mat.shape[0]), X_mat])
    beta = np.linalg.pinv(X_aug.T @ X_aug) @ X_aug.T @ y_t
    std_beta = beta[1:] * sigma_x / max(sigma_y, 1e-12)
    order = np.argsort(std_beta)
    colors = [positive_color if v >= 0 else negative_color for v in std_beta[order]]
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Standardized Coefficients",
                             xlabel="β (standardized)", ylabel="Feature",
                             figsize=figsize)
        fig.set_dpi(dpi)
        ax.barh(np.array(names)[order], std_beta[order], color=colors,
                alpha=0.85, **kwargs)
        ax.axvline(0.0, color="#444", linewidth=1)
        if grid:
            ax.grid(True, alpha=grid_alpha, axis="x")
        apply_theme(ax, theme)
    return ax


def standardized_coefficient_plot_interactive(
    X: MatrixLike,
    y_true: ArrayLike,
    feature_names: Optional[Sequence[str]] = None,
    title: Optional[str] = None,
    positive_color: str = "#4c78a8",
    negative_color: str = "#e45756",
    template: str = "plotly",
    height: int = 600,
    width: int = 900,
    **kwargs,
) -> PlotlyFigure:
    """Interactive standardized-coefficient chart."""
    X_mat = _as_matrix(X)
    y_t = _as_array(y_true)
    names = list(feature_names) if feature_names is not None else [f"x{i}" for i in range(X_mat.shape[1])]
    sigma_x = np.std(X_mat, axis=0, ddof=1)
    sigma_y = float(np.std(y_t, ddof=1)) if y_t.size > 1 else 1.0
    X_aug = np.column_stack([np.ones(X_mat.shape[0]), X_mat])
    beta = np.linalg.pinv(X_aug.T @ X_aug) @ X_aug.T @ y_t
    std_beta = beta[1:] * sigma_x / max(sigma_y, 1e-12)
    order = np.argsort(std_beta)
    colors = [positive_color if v >= 0 else negative_color for v in std_beta[order]]
    fig = go.Figure()
    fig.add_trace(go.Bar(x=std_beta[order], y=np.array(names)[order],
                         orientation="h", marker_color=colors,
                         name="Std. coefficient", **kwargs))
    fig.add_vline(x=0.0, line_color="#444")
    fig.update_layout(title=title or "Standardized Coefficients",
                      xaxis_title="β (standardized)", yaxis_title="Feature",
                      template=template, height=height, width=width)
    return fig


# ---------------------------------------------------------------------------
# Coefficient path plot (for precomputed paths)
# ---------------------------------------------------------------------------

def coefficient_path_plot_static(
    alphas: ArrayLike,
    coefficients: MatrixLike,
    feature_names: Optional[Sequence[str]] = None,
    log_x: bool = True,
    title: Optional[str] = None,
    figsize: FigureSize = (11, 6),
    cmap: str = "tab20",
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Plot coefficient paths vs a regularization parameter.

    ``coefficients`` is shaped ``(n_alphas, n_features)``. Use this with
    pre-computed lasso / ridge / elastic-net paths from any solver.
    """
    a = _as_array(alphas)
    C = _as_matrix(coefficients)
    if C.shape[0] != a.size:
        raise ValueError("coefficients first dimension must match alphas.")
    names = list(feature_names) if feature_names is not None else [f"x{i}" for i in range(C.shape[1])]
    cmap_obj = plt.get_cmap(cmap)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Coefficient Path",
                             xlabel="α (log scale)" if log_x else "α",
                             ylabel="Coefficient", figsize=figsize)
        fig.set_dpi(dpi)
        for j in range(C.shape[1]):
            ax.plot(a, C[:, j], color=cmap_obj(j % cmap_obj.N),
                    linewidth=2, label=names[j], **kwargs)
        if log_x:
            ax.set_xscale("log")
        ax.axhline(0.0, color="#444", linestyle="--", linewidth=1)
        ax.legend(loc="best", ncol=2, fontsize=8)
        if grid:
            ax.grid(True, alpha=grid_alpha)
        apply_theme(ax, theme)
    return ax


def coefficient_path_plot_interactive(
    alphas: ArrayLike,
    coefficients: MatrixLike,
    feature_names: Optional[Sequence[str]] = None,
    log_x: bool = True,
    title: Optional[str] = None,
    template: str = "plotly",
    height: int = 600,
    width: int = 1100,
    **kwargs,
) -> PlotlyFigure:
    """Interactive coefficient path plot."""
    a = _as_array(alphas)
    C = _as_matrix(coefficients)
    names = list(feature_names) if feature_names is not None else [f"x{i}" for i in range(C.shape[1])]
    fig = go.Figure()
    for j in range(C.shape[1]):
        fig.add_trace(go.Scatter(x=a, y=C[:, j], mode="lines",
                                 name=names[j], **kwargs))
    fig.add_hline(y=0.0, line_dash="dash", line_color="#444")
    fig.update_layout(
        title=title or "Coefficient Path",
        xaxis_title="α (log)" if log_x else "α",
        yaxis_title="Coefficient",
        xaxis_type="log" if log_x else "linear",
        template=template, height=height, width=width,
    )
    return fig


# Convenience aliases
coefficient_plot = coefficient_plot_static
coefficient_forest_plot = coefficient_forest_plot_static
standardized_coefficient_plot = standardized_coefficient_plot_static
coefficient_path_plot = coefficient_path_plot_static
