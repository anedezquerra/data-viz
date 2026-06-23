"""Extended residual diagnostics: distributions, normality, and homoscedasticity."""

from __future__ import annotations

from typing import Optional, Sequence

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from ..types import ArrayLike, FigureSize, MatplotlibAxes, PlotlyFigure
from ..utils import setup_plot, apply_theme
from .helpers import _as_array, _residuals


# ---------------------------------------------------------------------------
# Residual histogram
# ---------------------------------------------------------------------------

def residual_histogram_static(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    bins: int = 30,
    title: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    color: str = "#4c78a8",
    edgecolor: str = "black",
    alpha: float = 0.8,
    show_normal_overlay: bool = True,
    overlay_color: str = "#e45756",
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Plot a histogram of residuals with an optional normal-density overlay."""
    res = _residuals(y_true, y_pred)
    with plt.style.context(style):
        fig, ax = setup_plot(
            title=title or "Residual Distribution",
            xlabel="Residual",
            ylabel="Density",
            figsize=figsize,
        )
        fig.set_dpi(dpi)
        ax.hist(res, bins=bins, density=True, color=color, edgecolor=edgecolor,
                alpha=alpha, **kwargs)
        if show_normal_overlay and res.size > 1:
            mu, sigma = float(np.mean(res)), float(np.std(res, ddof=1))
            xs = np.linspace(res.min(), res.max(), 200)
            ys = np.exp(-0.5 * ((xs - mu) / max(sigma, 1e-12)) ** 2) / (
                max(sigma, 1e-12) * np.sqrt(2 * np.pi)
            )
            ax.plot(xs, ys, color=overlay_color, linewidth=2, label="Normal fit")
            ax.legend()
        if grid:
            ax.grid(True, alpha=grid_alpha)
        apply_theme(ax, theme)
    return ax


def residual_histogram_interactive(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    bins: int = 30,
    title: Optional[str] = None,
    color: str = "#4c78a8",
    show_normal_overlay: bool = True,
    overlay_color: str = "#e45756",
    template: str = "plotly",
    height: int = 600,
    width: int = 1000,
    **kwargs,
) -> PlotlyFigure:
    """Interactive residual histogram with an optional normal-density overlay."""
    res = _residuals(y_true, y_pred)
    fig = go.Figure()
    fig.add_trace(go.Histogram(x=res, nbinsx=bins, histnorm="probability density",
                               marker_color=color, name="Residuals", **kwargs))
    if show_normal_overlay and res.size > 1:
        mu, sigma = float(np.mean(res)), float(np.std(res, ddof=1))
        xs = np.linspace(res.min(), res.max(), 200)
        ys = np.exp(-0.5 * ((xs - mu) / max(sigma, 1e-12)) ** 2) / (
            max(sigma, 1e-12) * np.sqrt(2 * np.pi)
        )
        fig.add_trace(go.Scatter(x=xs, y=ys, mode="lines",
                                 line=dict(color=overlay_color, width=2),
                                 name="Normal fit"))
    fig.update_layout(title=title or "Residual Distribution",
                      xaxis_title="Residual", yaxis_title="Density",
                      template=template, height=height, width=width)
    return fig


# ---------------------------------------------------------------------------
# Residual density (KDE)
# ---------------------------------------------------------------------------

def _gaussian_kde(values: np.ndarray, grid: np.ndarray, bandwidth: Optional[float] = None) -> np.ndarray:
    n = values.size
    if n == 0:
        return np.zeros_like(grid)
    if bandwidth is None:
        sigma = float(np.std(values, ddof=1)) if n > 1 else 1.0
        bandwidth = max(1.06 * sigma * n ** (-1 / 5), 1e-3)
    diffs = (grid[:, None] - values[None, :]) / bandwidth
    return float(1.0) / (n * bandwidth * np.sqrt(2 * np.pi)) * np.exp(-0.5 * diffs ** 2).sum(axis=1)


def residual_density_static(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    title: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    color: str = "#4c78a8",
    fill: bool = True,
    fill_alpha: float = 0.3,
    bandwidth: Optional[float] = None,
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Kernel-density estimate of residuals."""
    res = _residuals(y_true, y_pred)
    grid_x = np.linspace(res.min(), res.max(), 256)
    density = _gaussian_kde(res, grid_x, bandwidth)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Residual Density",
                             xlabel="Residual", ylabel="Density", figsize=figsize)
        fig.set_dpi(dpi)
        ax.plot(grid_x, density, color=color, linewidth=2, **kwargs)
        if fill:
            ax.fill_between(grid_x, density, color=color, alpha=fill_alpha)
        ax.axvline(0.0, color="#888", linestyle="--", linewidth=1)
        if grid:
            ax.grid(True, alpha=grid_alpha)
        apply_theme(ax, theme)
    return ax


def residual_density_interactive(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    title: Optional[str] = None,
    color: str = "#4c78a8",
    fill: bool = True,
    bandwidth: Optional[float] = None,
    template: str = "plotly",
    height: int = 600,
    width: int = 1000,
    **kwargs,
) -> PlotlyFigure:
    """Interactive residual KDE plot."""
    res = _residuals(y_true, y_pred)
    grid_x = np.linspace(res.min(), res.max(), 256)
    density = _gaussian_kde(res, grid_x, bandwidth)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=grid_x, y=density, mode="lines",
                             line=dict(color=color, width=2),
                             fill="tozeroy" if fill else None,
                             name="Density", **kwargs))
    fig.add_vline(x=0.0, line_dash="dash", line_color="#888")
    fig.update_layout(title=title or "Residual Density",
                      xaxis_title="Residual", yaxis_title="Density",
                      template=template, height=height, width=width)
    return fig


# ---------------------------------------------------------------------------
# Residual QQ plot
# ---------------------------------------------------------------------------

def _normal_quantiles(n: int) -> np.ndarray:
    from .helpers import prediction_intervals  # reuse ppf via residuals; trick avoided
    # Use a lightweight inverse-normal: rank-based Filliben plotting positions.
    ranks = np.arange(1, n + 1)
    p = (ranks - 3 / 8) / (n + 1 / 4)
    # Beasley-Springer-Moro approximation (inlined to avoid scipy dependency).
    a = [-3.969683028665376e1, 2.209460984245205e2, -2.759285104469687e2,
         1.383577518672690e2, -3.066479806614716e1, 2.506628277459239]
    b = [-5.447609879822406e1, 1.615858368580409e2, -1.556989798598866e2,
         6.680131188771972e1, -1.328068155288572e1]
    c = [-7.784894002430293e-3, -3.223964580411365e-1, -2.400758277161838,
         -2.549732539343734, 4.374664141464968, 2.938163982698783]
    d = [7.784695709041462e-3, 3.224671290700398e-1, 2.445134137142996,
         3.754408661907416]
    plow, phigh = 0.02425, 1 - 0.02425
    out = np.zeros_like(p)
    for i, pi in enumerate(p):
        if pi < plow:
            q = np.sqrt(-2 * np.log(pi))
            out[i] = (((((c[0]*q + c[1])*q + c[2])*q + c[3])*q + c[4])*q + c[5]) / \
                     ((((d[0]*q + d[1])*q + d[2])*q + d[3])*q + 1)
        elif pi <= phigh:
            q = pi - 0.5
            r = q * q
            out[i] = (((((a[0]*r + a[1])*r + a[2])*r + a[3])*r + a[4])*r + a[5])*q / \
                     (((((b[0]*r + b[1])*r + b[2])*r + b[3])*r + b[4])*r + 1)
        else:
            q = np.sqrt(-2 * np.log(1 - pi))
            out[i] = -(((((c[0]*q + c[1])*q + c[2])*q + c[3])*q + c[4])*q + c[5]) / \
                      ((((d[0]*q + d[1])*q + d[2])*q + d[3])*q + 1)
    return out


def residual_qq_static(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    title: Optional[str] = None,
    figsize: FigureSize = (8, 8),
    marker_color: str = "#4c78a8",
    line_color: str = "#e45756",
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Normal Q-Q plot of residuals with a reference line through the IQR."""
    res = _residuals(y_true, y_pred)
    sample = np.sort(res)
    theoretical = _normal_quantiles(sample.size)
    q25, q75 = np.percentile(sample, [25, 75])
    t25, t75 = np.percentile(theoretical, [25, 75])
    slope = (q75 - q25) / max(t75 - t25, 1e-12)
    intercept = q25 - slope * t25
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Residual Q-Q Plot",
                             xlabel="Theoretical quantile",
                             ylabel="Sample residual quantile", figsize=figsize)
        fig.set_dpi(dpi)
        ax.scatter(theoretical, sample, color=marker_color, **kwargs)
        xs = np.array([theoretical.min(), theoretical.max()])
        ax.plot(xs, slope * xs + intercept, color=line_color, linewidth=2)
        if grid:
            ax.grid(True, alpha=grid_alpha)
        apply_theme(ax, theme)
    return ax


def residual_qq_interactive(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    title: Optional[str] = None,
    marker_color: str = "#4c78a8",
    line_color: str = "#e45756",
    template: str = "plotly",
    height: int = 700,
    width: int = 700,
    **kwargs,
) -> PlotlyFigure:
    """Interactive normal Q-Q plot of residuals."""
    res = _residuals(y_true, y_pred)
    sample = np.sort(res)
    theoretical = _normal_quantiles(sample.size)
    q25, q75 = np.percentile(sample, [25, 75])
    t25, t75 = np.percentile(theoretical, [25, 75])
    slope = (q75 - q25) / max(t75 - t25, 1e-12)
    intercept = q25 - slope * t25
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=theoretical, y=sample, mode="markers",
                             marker=dict(color=marker_color), name="Residuals", **kwargs))
    xs = np.array([theoretical.min(), theoretical.max()])
    fig.add_trace(go.Scatter(x=xs, y=slope * xs + intercept, mode="lines",
                             line=dict(color=line_color, width=2), name="Reference"))
    fig.update_layout(title=title or "Residual Q-Q Plot",
                      xaxis_title="Theoretical quantile",
                      yaxis_title="Sample residual quantile",
                      template=template, height=height, width=width)
    return fig


# ---------------------------------------------------------------------------
# Residual boxplot by group
# ---------------------------------------------------------------------------

def residual_boxplot_by_group_static(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    groups: ArrayLike,
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
    """Box plot of residuals partitioned by a categorical group."""
    res = _residuals(y_true, y_pred)
    g = pd.Series(np.asarray(groups))
    if g.size != res.size:
        raise ValueError("groups must align with y_true / y_pred.")
    df = pd.DataFrame({"residual": res, "group": g})
    levels = list(df["group"].astype(str).unique())
    data = [df.loc[df["group"].astype(str) == lvl, "residual"].to_numpy() for lvl in levels]
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Residuals by Group",
                             xlabel="Group", ylabel="Residual", figsize=figsize)
        fig.set_dpi(dpi)
        bp = ax.boxplot(data, labels=levels, patch_artist=True, **kwargs)
        for patch in bp["boxes"]:
            patch.set_facecolor(color)
            patch.set_alpha(0.7)
        ax.axhline(0.0, color="#e45756", linestyle="--", linewidth=1)
        if grid:
            ax.grid(True, alpha=grid_alpha, axis="y")
        apply_theme(ax, theme)
    return ax


def residual_boxplot_by_group_interactive(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    groups: ArrayLike,
    title: Optional[str] = None,
    color: str = "#4c78a8",
    template: str = "plotly",
    height: int = 600,
    width: int = 1000,
    **kwargs,
) -> PlotlyFigure:
    """Interactive residual box plot per group."""
    res = _residuals(y_true, y_pred)
    g = np.asarray(groups).astype(str)
    if g.size != res.size:
        raise ValueError("groups must align with y_true / y_pred.")
    fig = go.Figure()
    fig.add_trace(go.Box(y=res, x=g, marker_color=color, **kwargs))
    fig.add_hline(y=0.0, line_dash="dash", line_color="#e45756")
    fig.update_layout(title=title or "Residuals by Group",
                      xaxis_title="Group", yaxis_title="Residual",
                      template=template, height=height, width=width)
    return fig


# ---------------------------------------------------------------------------
# Standardized residual plot
# ---------------------------------------------------------------------------

def standardized_residual_plot_static(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    title: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    color: str = "#4c78a8",
    grid: bool = True,
    grid_alpha: float = 0.3,
    bound: float = 2.0,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Standardized residuals (residual / σ̂) vs predicted values."""
    res = _residuals(y_true, y_pred)
    sigma = float(np.std(res, ddof=1)) if res.size > 1 else 1.0
    std_res = res / max(sigma, 1e-12)
    y_p = _as_array(y_pred)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Standardized Residuals",
                             xlabel="Predicted", ylabel="Standardized residual",
                             figsize=figsize)
        fig.set_dpi(dpi)
        ax.scatter(y_p, std_res, color=color, alpha=0.7, **kwargs)
        ax.axhline(0.0, color="#444", linestyle="--", linewidth=1)
        ax.axhline(bound, color="#e45756", linestyle=":", linewidth=1)
        ax.axhline(-bound, color="#e45756", linestyle=":", linewidth=1)
        if grid:
            ax.grid(True, alpha=grid_alpha)
        apply_theme(ax, theme)
    return ax


def standardized_residual_plot_interactive(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    title: Optional[str] = None,
    color: str = "#4c78a8",
    bound: float = 2.0,
    template: str = "plotly",
    height: int = 600,
    width: int = 1000,
    **kwargs,
) -> PlotlyFigure:
    """Interactive standardized residuals vs predicted values."""
    res = _residuals(y_true, y_pred)
    sigma = float(np.std(res, ddof=1)) if res.size > 1 else 1.0
    std_res = res / max(sigma, 1e-12)
    y_p = _as_array(y_pred)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=y_p, y=std_res, mode="markers",
                             marker=dict(color=color), name="Residual", **kwargs))
    fig.add_hline(y=0.0, line_dash="dash", line_color="#444")
    fig.add_hline(y=bound, line_dash="dot", line_color="#e45756")
    fig.add_hline(y=-bound, line_dash="dot", line_color="#e45756")
    fig.update_layout(title=title or "Standardized Residuals",
                      xaxis_title="Predicted", yaxis_title="Standardized residual",
                      template=template, height=height, width=width)
    return fig


# ---------------------------------------------------------------------------
# Scale-location (spread vs predicted)
# ---------------------------------------------------------------------------

def scale_location_plot_static(
    y_true: ArrayLike,
    y_pred: ArrayLike,
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
    """Sqrt(\\|standardized residual\\|) vs predicted — homoscedasticity check."""
    res = _residuals(y_true, y_pred)
    sigma = float(np.std(res, ddof=1)) if res.size > 1 else 1.0
    sqrt_abs = np.sqrt(np.abs(res / max(sigma, 1e-12)))
    y_p = _as_array(y_pred)
    order = np.argsort(y_p)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Scale-Location",
                             xlabel="Predicted",
                             ylabel="√|Standardized residual|", figsize=figsize)
        fig.set_dpi(dpi)
        ax.scatter(y_p, sqrt_abs, color=color, alpha=0.7, **kwargs)
        if trend and y_p.size >= 5:
            window = max(5, y_p.size // 20)
            roll = pd.Series(sqrt_abs[order]).rolling(window, min_periods=1, center=True).mean()
            ax.plot(y_p[order], roll, color=trend_color, linewidth=2)
        if grid:
            ax.grid(True, alpha=grid_alpha)
        apply_theme(ax, theme)
    return ax


def scale_location_plot_interactive(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    title: Optional[str] = None,
    color: str = "#4c78a8",
    trend: bool = True,
    trend_color: str = "#e45756",
    template: str = "plotly",
    height: int = 600,
    width: int = 1000,
    **kwargs,
) -> PlotlyFigure:
    """Interactive scale-location plot."""
    res = _residuals(y_true, y_pred)
    sigma = float(np.std(res, ddof=1)) if res.size > 1 else 1.0
    sqrt_abs = np.sqrt(np.abs(res / max(sigma, 1e-12)))
    y_p = _as_array(y_pred)
    order = np.argsort(y_p)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=y_p, y=sqrt_abs, mode="markers",
                             marker=dict(color=color), name="Residual", **kwargs))
    if trend and y_p.size >= 5:
        window = max(5, y_p.size // 20)
        roll = pd.Series(sqrt_abs[order]).rolling(window, min_periods=1, center=True).mean()
        fig.add_trace(go.Scatter(x=y_p[order], y=roll, mode="lines",
                                 line=dict(color=trend_color, width=2),
                                 name="Smoothed trend"))
    fig.update_layout(title=title or "Scale-Location",
                      xaxis_title="Predicted",
                      yaxis_title="√|Standardized residual|",
                      template=template, height=height, width=width)
    return fig


# Convenience aliases
residual_histogram = residual_histogram_static
residual_density = residual_density_static
residual_qq = residual_qq_static
residual_boxplot_by_group = residual_boxplot_by_group_static
standardized_residual_plot = standardized_residual_plot_static
scale_location_plot = scale_location_plot_static
