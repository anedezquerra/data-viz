"""Regularization-path helpers and plots (lasso / ridge / elastic-net)."""

from __future__ import annotations

from typing import Optional, Sequence, Tuple

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from ..types import ArrayLike, FigureSize, MatplotlibAxes, MatrixLike, PlotlyFigure
from ..utils import setup_plot, apply_theme
from .helpers import _as_array, _as_matrix


# ---------------------------------------------------------------------------
# Lightweight solvers used to compute paths without external dependencies.
# ---------------------------------------------------------------------------

def _standardize(X: np.ndarray, y: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, float]:
    mu_x = X.mean(axis=0)
    sigma_x = X.std(axis=0, ddof=0)
    sigma_x = np.where(sigma_x > 0, sigma_x, 1.0)
    mu_y = y.mean()
    return (X - mu_x) / sigma_x, y - mu_y, mu_x, sigma_x, mu_y


def _coordinate_descent(
    X: np.ndarray,
    y: np.ndarray,
    alpha: float,
    l1_ratio: float,
    max_iter: int = 500,
    tol: float = 1e-4,
) -> np.ndarray:
    n, p = X.shape
    beta = np.zeros(p)
    xtx_diag = (X ** 2).sum(axis=0)
    residual = y.copy()
    for _ in range(max_iter):
        max_change = 0.0
        for j in range(p):
            rho = float(X[:, j] @ residual + beta[j] * xtx_diag[j])
            denom = xtx_diag[j] + n * alpha * (1 - l1_ratio)
            soft = np.sign(rho) * max(abs(rho) - n * alpha * l1_ratio, 0.0)
            new_beta = soft / denom if denom > 0 else 0.0
            change = abs(new_beta - beta[j])
            if change > 0:
                residual -= (new_beta - beta[j]) * X[:, j]
                beta[j] = new_beta
            max_change = max(max_change, change)
        if max_change < tol:
            break
    return beta


def compute_regularization_path(
    X: MatrixLike,
    y: ArrayLike,
    alphas: Optional[Sequence[float]] = None,
    n_alphas: int = 50,
    eps: float = 1e-3,
    l1_ratio: float = 1.0,
) -> Tuple[np.ndarray, np.ndarray]:
    """Compute coefficient paths via coordinate descent on standardized data.

    ``l1_ratio=1.0`` corresponds to lasso, ``0.0`` to ridge, intermediate
    values to elastic net. Returns ``(alphas, coefficients)`` where
    ``coefficients`` has shape ``(n_alphas, n_features)`` on the original
    scale.
    """
    X_mat = _as_matrix(X)
    y_arr = _as_array(y)
    X_s, y_c, _, sigma_x, _ = _standardize(X_mat, y_arr)
    if alphas is None:
        max_corr = float(np.max(np.abs(X_s.T @ y_c))) / X_s.shape[0]
        alpha_max = max_corr / max(l1_ratio, 1e-3)
        alpha_min = max(alpha_max * eps, 1e-8)
        alphas = np.geomspace(alpha_max, alpha_min, n_alphas)
    alphas_arr = np.asarray(alphas, dtype=float)
    coefs_s = np.zeros((alphas_arr.size, X_mat.shape[1]))
    beta = np.zeros(X_mat.shape[1])
    for i, a in enumerate(alphas_arr):
        beta = _coordinate_descent(X_s, y_c, alpha=a, l1_ratio=l1_ratio,
                                   max_iter=300)
        coefs_s[i] = beta
    coefs = coefs_s / sigma_x
    return alphas_arr, coefs


# ---------------------------------------------------------------------------
# Lasso / ridge wrappers calling the shared plotting helpers
# ---------------------------------------------------------------------------

def _plot_path_static(alphas, coefs, names, title, figsize, theme, dpi, style,
                       grid, grid_alpha, cmap, **kwargs) -> MatplotlibAxes:
    cmap_obj = plt.get_cmap(cmap)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="α (log)",
                             ylabel="Coefficient", figsize=figsize)
        fig.set_dpi(dpi)
        for j in range(coefs.shape[1]):
            ax.plot(alphas, coefs[:, j], color=cmap_obj(j % cmap_obj.N),
                    linewidth=2, label=names[j], **kwargs)
        ax.set_xscale("log")
        ax.axhline(0.0, color="#444", linestyle="--", linewidth=1)
        ax.legend(loc="best", ncol=2, fontsize=8)
        if grid:
            ax.grid(True, alpha=grid_alpha)
        apply_theme(ax, theme)
    return ax


def _plot_path_interactive(alphas, coefs, names, title, template, height, width,
                            **kwargs) -> PlotlyFigure:
    fig = go.Figure()
    for j in range(coefs.shape[1]):
        fig.add_trace(go.Scatter(x=alphas, y=coefs[:, j], mode="lines",
                                 name=names[j], **kwargs))
    fig.add_hline(y=0.0, line_dash="dash", line_color="#444")
    fig.update_layout(title=title, xaxis_title="α", yaxis_title="Coefficient",
                      xaxis_type="log", template=template, height=height, width=width)
    return fig


def lasso_path_static(
    X: MatrixLike,
    y_true: ArrayLike,
    feature_names: Optional[Sequence[str]] = None,
    alphas: Optional[Sequence[float]] = None,
    n_alphas: int = 50,
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
    """Lasso coefficient path computed with internal coordinate descent."""
    a, C = compute_regularization_path(X, y_true, alphas=alphas, n_alphas=n_alphas,
                                       l1_ratio=1.0)
    names = list(feature_names) if feature_names is not None else [f"x{i}" for i in range(C.shape[1])]
    return _plot_path_static(a, C, names, title or "Lasso Path", figsize,
                              theme, dpi, style, grid, grid_alpha, cmap, **kwargs)


def lasso_path_interactive(
    X: MatrixLike,
    y_true: ArrayLike,
    feature_names: Optional[Sequence[str]] = None,
    alphas: Optional[Sequence[float]] = None,
    n_alphas: int = 50,
    title: Optional[str] = None,
    template: str = "plotly",
    height: int = 600,
    width: int = 1100,
    **kwargs,
) -> PlotlyFigure:
    """Interactive lasso path."""
    a, C = compute_regularization_path(X, y_true, alphas=alphas, n_alphas=n_alphas,
                                       l1_ratio=1.0)
    names = list(feature_names) if feature_names is not None else [f"x{i}" for i in range(C.shape[1])]
    return _plot_path_interactive(a, C, names, title or "Lasso Path",
                                   template, height, width, **kwargs)


def ridge_path_static(
    X: MatrixLike,
    y_true: ArrayLike,
    feature_names: Optional[Sequence[str]] = None,
    alphas: Optional[Sequence[float]] = None,
    n_alphas: int = 50,
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
    """Ridge coefficient path using closed-form ``(XᵀX + αI)⁻¹Xᵀy`` solutions."""
    X_mat = _as_matrix(X)
    y_arr = _as_array(y_true)
    X_s, y_c, _, sigma_x, _ = _standardize(X_mat, y_arr)
    if alphas is None:
        alpha_max = float(np.max(np.abs(X_s.T @ y_c))) / X_s.shape[0]
        alphas = np.geomspace(max(alpha_max * 1e-3, 1e-6), alpha_max * 10, n_alphas)
    alphas_arr = np.asarray(alphas, dtype=float)
    XtX = X_s.T @ X_s
    Xty = X_s.T @ y_c
    coefs = np.zeros((alphas_arr.size, X_mat.shape[1]))
    eye = np.eye(X_mat.shape[1])
    for i, a in enumerate(alphas_arr):
        coefs[i] = np.linalg.solve(XtX + X_s.shape[0] * a * eye, Xty)
    coefs = coefs / sigma_x
    names = list(feature_names) if feature_names is not None else [f"x{i}" for i in range(X_mat.shape[1])]
    return _plot_path_static(alphas_arr, coefs, names, title or "Ridge Path",
                              figsize, theme, dpi, style, grid, grid_alpha, cmap,
                              **kwargs)


def ridge_path_interactive(
    X: MatrixLike,
    y_true: ArrayLike,
    feature_names: Optional[Sequence[str]] = None,
    alphas: Optional[Sequence[float]] = None,
    n_alphas: int = 50,
    title: Optional[str] = None,
    template: str = "plotly",
    height: int = 600,
    width: int = 1100,
    **kwargs,
) -> PlotlyFigure:
    """Interactive ridge path."""
    X_mat = _as_matrix(X)
    y_arr = _as_array(y_true)
    X_s, y_c, _, sigma_x, _ = _standardize(X_mat, y_arr)
    if alphas is None:
        alpha_max = float(np.max(np.abs(X_s.T @ y_c))) / X_s.shape[0]
        alphas = np.geomspace(max(alpha_max * 1e-3, 1e-6), alpha_max * 10, n_alphas)
    alphas_arr = np.asarray(alphas, dtype=float)
    XtX = X_s.T @ X_s
    Xty = X_s.T @ y_c
    coefs = np.zeros((alphas_arr.size, X_mat.shape[1]))
    eye = np.eye(X_mat.shape[1])
    for i, a in enumerate(alphas_arr):
        coefs[i] = np.linalg.solve(XtX + X_s.shape[0] * a * eye, Xty)
    coefs = coefs / sigma_x
    names = list(feature_names) if feature_names is not None else [f"x{i}" for i in range(X_mat.shape[1])]
    return _plot_path_interactive(alphas_arr, coefs, names, title or "Ridge Path",
                                   template, height, width, **kwargs)


# ---------------------------------------------------------------------------
# Regularization validation curve (train/test score vs alpha)
# ---------------------------------------------------------------------------

def regularization_validation_plot_static(
    alphas: ArrayLike,
    train_scores: ArrayLike,
    test_scores: ArrayLike,
    score_name: str = "Score",
    log_x: bool = True,
    title: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    train_color: str = "#4c78a8",
    test_color: str = "#e45756",
    band_alpha: float = 0.2,
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Train/test score curves vs regularization strength.

    ``train_scores`` and ``test_scores`` may be 1-D (single value per α) or
    2-D ``(n_alphas, n_folds)``; the latter renders a ±1 std band.
    """
    a = _as_array(alphas)
    train = np.asarray(train_scores, dtype=float)
    test = np.asarray(test_scores, dtype=float)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Regularization Validation",
                             xlabel="α", ylabel=score_name, figsize=figsize)
        fig.set_dpi(dpi)
        for arr, color, label in ((train, train_color, "Train"),
                                  (test, test_color, "Validation")):
            mean = arr.mean(axis=1) if arr.ndim == 2 else arr
            ax.plot(a, mean, color=color, linewidth=2, marker="o",
                    label=label, **kwargs)
            if arr.ndim == 2:
                std = arr.std(axis=1)
                ax.fill_between(a, mean - std, mean + std, color=color,
                                alpha=band_alpha)
        if log_x:
            ax.set_xscale("log")
        ax.legend()
        if grid:
            ax.grid(True, alpha=grid_alpha)
        apply_theme(ax, theme)
    return ax


def regularization_validation_plot_interactive(
    alphas: ArrayLike,
    train_scores: ArrayLike,
    test_scores: ArrayLike,
    score_name: str = "Score",
    log_x: bool = True,
    title: Optional[str] = None,
    train_color: str = "#4c78a8",
    test_color: str = "#e45756",
    template: str = "plotly",
    height: int = 600,
    width: int = 1000,
    **kwargs,
) -> PlotlyFigure:
    """Interactive regularization train/test validation curve."""
    a = _as_array(alphas)
    train = np.asarray(train_scores, dtype=float)
    test = np.asarray(test_scores, dtype=float)
    fig = go.Figure()
    for arr, color, label in ((train, train_color, "Train"),
                              (test, test_color, "Validation")):
        mean = arr.mean(axis=1) if arr.ndim == 2 else arr
        fig.add_trace(go.Scatter(x=a, y=mean, mode="lines+markers",
                                 line=dict(color=color, width=2),
                                 name=label, **kwargs))
        if arr.ndim == 2:
            std = arr.std(axis=1)
            fig.add_trace(go.Scatter(
                x=np.concatenate([a, a[::-1]]),
                y=np.concatenate([mean + std, (mean - std)[::-1]]),
                fill="toself", fillcolor=color, opacity=0.18,
                line=dict(width=0), showlegend=False, name=f"{label} band",
            ))
    fig.update_layout(title=title or "Regularization Validation",
                      xaxis_title="α", yaxis_title=score_name,
                      xaxis_type="log" if log_x else "linear",
                      template=template, height=height, width=width)
    return fig


lasso_path = lasso_path_static
ridge_path = ridge_path_static
regularization_validation_plot = regularization_validation_plot_static
