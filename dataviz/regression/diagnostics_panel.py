"""Composite regression diagnostic panels."""

from __future__ import annotations

from typing import Optional, Sequence

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from ..types import ArrayLike, FigureSize, MatplotlibFigure, MatrixLike, PlotlyFigure
from ..utils import setup_plot, apply_theme
from .helpers import _as_array, _as_matrix, _residuals, compute_regression_metrics
from .influence import influence_statistics


def _smooth(x: np.ndarray, y: np.ndarray, window: Optional[int] = None) -> tuple[np.ndarray, np.ndarray]:
    order = np.argsort(x)
    w = window if window is not None else max(5, x.size // 20)
    import pandas as pd
    roll = pd.Series(y[order]).rolling(w, min_periods=1, center=True).mean().to_numpy()
    return x[order], roll


# ---------------------------------------------------------------------------
# Regression diagnostic panel — the canonical 4-up plot
# ---------------------------------------------------------------------------

def regression_diagnostic_panel_static(
    X: MatrixLike,
    y_true: ArrayLike,
    y_pred: ArrayLike,
    title: Optional[str] = None,
    figsize: FigureSize = (12, 10),
    color: str = "#4c78a8",
    line_color: str = "#e45756",
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
) -> MatplotlibFigure:
    """Four-panel diagnostic: residuals-vs-fitted, QQ, scale-location, leverage."""
    y_t = _as_array(y_true)
    y_p = _as_array(y_pred)
    res = _residuals(y_t, y_p)
    sigma = float(np.std(res, ddof=1)) if res.size > 1 else 1.0
    std_res = res / max(sigma, 1e-12)
    stats = influence_statistics(X, y_t, y_p)
    sample = np.sort(res)
    from .residual_extended import _normal_quantiles
    theoretical = _normal_quantiles(sample.size)
    sqrt_abs = np.sqrt(np.abs(std_res))

    with plt.style.context(style):
        fig, axes = plt.subplots(2, 2, figsize=figsize, dpi=dpi)
        ((ax_rf, ax_qq), (ax_sl, ax_lv)) = axes
        if title:
            fig.suptitle(title, fontsize=14)

        ax_rf.scatter(y_p, res, color=color, alpha=0.7)
        ax_rf.axhline(0.0, color=line_color, linestyle="--", linewidth=2)
        xs, smooth = _smooth(y_p, res)
        ax_rf.plot(xs, smooth, color=line_color, linewidth=2)
        ax_rf.set_title("Residuals vs Fitted")
        ax_rf.set_xlabel("Fitted")
        ax_rf.set_ylabel("Residual")
        ax_rf.grid(True, alpha=0.3)

        q25, q75 = np.percentile(sample, [25, 75])
        t25, t75 = np.percentile(theoretical, [25, 75])
        slope = (q75 - q25) / max(t75 - t25, 1e-12)
        intercept = q25 - slope * t25
        ax_qq.scatter(theoretical, sample, color=color, alpha=0.7)
        xs = np.array([theoretical.min(), theoretical.max()])
        ax_qq.plot(xs, slope * xs + intercept, color=line_color, linewidth=2)
        ax_qq.set_title("Normal Q-Q")
        ax_qq.set_xlabel("Theoretical quantile")
        ax_qq.set_ylabel("Sample residual")
        ax_qq.grid(True, alpha=0.3)

        ax_sl.scatter(y_p, sqrt_abs, color=color, alpha=0.7)
        xs, smooth = _smooth(y_p, sqrt_abs)
        ax_sl.plot(xs, smooth, color=line_color, linewidth=2)
        ax_sl.set_title("Scale-Location")
        ax_sl.set_xlabel("Fitted")
        ax_sl.set_ylabel("√|Std. residual|")
        ax_sl.grid(True, alpha=0.3)

        ax_lv.scatter(stats.leverage, stats.standardized_residuals,
                      color=color, alpha=0.7, s=30 + 200 * stats.cooks_distance / max(stats.cooks_distance.max(), 1e-12))
        ax_lv.axhline(0.0, color=line_color, linestyle="--", linewidth=1)
        ax_lv.set_title("Residual vs Leverage")
        ax_lv.set_xlabel("Leverage")
        ax_lv.set_ylabel("Std. residual")
        ax_lv.grid(True, alpha=0.3)

        for ax in axes.ravel():
            apply_theme(ax, theme)
        fig.tight_layout()
    return fig


def regression_diagnostic_panel_interactive(
    X: MatrixLike,
    y_true: ArrayLike,
    y_pred: ArrayLike,
    title: Optional[str] = None,
    color: str = "#4c78a8",
    line_color: str = "#e45756",
    template: str = "plotly",
    height: int = 900,
    width: int = 1100,
) -> PlotlyFigure:
    """Interactive four-panel regression diagnostic dashboard."""
    y_t = _as_array(y_true)
    y_p = _as_array(y_pred)
    res = _residuals(y_t, y_p)
    sigma = float(np.std(res, ddof=1)) if res.size > 1 else 1.0
    std_res = res / max(sigma, 1e-12)
    stats = influence_statistics(X, y_t, y_p)
    sample = np.sort(res)
    from .residual_extended import _normal_quantiles
    theoretical = _normal_quantiles(sample.size)
    sqrt_abs = np.sqrt(np.abs(std_res))
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=("Residuals vs Fitted", "Normal Q-Q",
                        "Scale-Location", "Residual vs Leverage"),
    )
    fig.add_trace(go.Scatter(x=y_p, y=res, mode="markers",
                             marker=dict(color=color), name="Resid"),
                  row=1, col=1)
    xs, smooth = _smooth(y_p, res)
    fig.add_trace(go.Scatter(x=xs, y=smooth, mode="lines",
                             line=dict(color=line_color, width=2),
                             name="Smooth", showlegend=False),
                  row=1, col=1)
    q25, q75 = np.percentile(sample, [25, 75])
    t25, t75 = np.percentile(theoretical, [25, 75])
    slope = (q75 - q25) / max(t75 - t25, 1e-12)
    intercept = q25 - slope * t25
    fig.add_trace(go.Scatter(x=theoretical, y=sample, mode="markers",
                             marker=dict(color=color), name="Q-Q",
                             showlegend=False), row=1, col=2)
    fig.add_trace(go.Scatter(x=[theoretical.min(), theoretical.max()],
                             y=[slope * theoretical.min() + intercept,
                                slope * theoretical.max() + intercept],
                             mode="lines",
                             line=dict(color=line_color, width=2),
                             showlegend=False), row=1, col=2)
    fig.add_trace(go.Scatter(x=y_p, y=sqrt_abs, mode="markers",
                             marker=dict(color=color), showlegend=False),
                  row=2, col=1)
    xs, smooth = _smooth(y_p, sqrt_abs)
    fig.add_trace(go.Scatter(x=xs, y=smooth, mode="lines",
                             line=dict(color=line_color, width=2),
                             showlegend=False), row=2, col=1)
    size = 6 + 25 * stats.cooks_distance / max(stats.cooks_distance.max(), 1e-12)
    fig.add_trace(go.Scatter(x=stats.leverage, y=stats.standardized_residuals,
                             mode="markers",
                             marker=dict(color=color, size=size),
                             showlegend=False), row=2, col=2)
    fig.update_layout(title=title or "Regression Diagnostics",
                      template=template, height=height, width=width)
    return fig


# ---------------------------------------------------------------------------
# Regression dashboard — prediction vs actual + residuals + metrics
# ---------------------------------------------------------------------------

def regression_dashboard_static(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    n_features: Optional[int] = None,
    title: Optional[str] = None,
    figsize: FigureSize = (14, 8),
    color: str = "#4c78a8",
    line_color: str = "#e45756",
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
) -> MatplotlibFigure:
    """Dashboard with predicted-vs-actual, residual scatter, error histogram, metrics."""
    y_t = _as_array(y_true)
    y_p = _as_array(y_pred)
    res = _residuals(y_t, y_p)
    metrics = compute_regression_metrics(y_t, y_p, n_features=n_features).as_dict()
    keys = ["mae", "rmse", "medae", "r2"]
    if metrics.get("adj_r2") is not None:
        keys.append("adj_r2")
    with plt.style.context(style):
        fig, axes = plt.subplots(2, 2, figsize=figsize, dpi=dpi)
        ((ax_pa, ax_rs), (ax_hist, ax_met)) = axes
        if title:
            fig.suptitle(title, fontsize=14)
        lo, hi = float(min(y_t.min(), y_p.min())), float(max(y_t.max(), y_p.max()))
        ax_pa.scatter(y_t, y_p, color=color, alpha=0.7)
        ax_pa.plot([lo, hi], [lo, hi], color=line_color, linewidth=2)
        ax_pa.set_title("Predicted vs Actual")
        ax_pa.set_xlabel("Actual")
        ax_pa.set_ylabel("Predicted")
        ax_pa.grid(True, alpha=0.3)
        ax_rs.scatter(y_p, res, color=color, alpha=0.7)
        ax_rs.axhline(0.0, color=line_color, linestyle="--", linewidth=2)
        ax_rs.set_title("Residuals")
        ax_rs.set_xlabel("Predicted")
        ax_rs.set_ylabel("Residual")
        ax_rs.grid(True, alpha=0.3)
        ax_hist.hist(res, bins=30, density=True, color=color, alpha=0.8,
                     edgecolor="black")
        ax_hist.axvline(0.0, color=line_color, linestyle="--", linewidth=2)
        ax_hist.set_title("Residual distribution")
        ax_hist.set_xlabel("Residual")
        ax_hist.grid(True, alpha=0.3)
        ax_met.axis("off")
        rows = [[k, f"{metrics[k]:.4g}"] for k in keys]
        table = ax_met.table(cellText=rows, colLabels=["Metric", "Value"],
                             loc="center", cellLoc="center", colWidths=[0.4, 0.4])
        table.auto_set_font_size(False)
        table.set_fontsize(11)
        table.scale(1, 1.6)
        ax_met.set_title("Metrics")
        for ax in axes.ravel():
            apply_theme(ax, theme)
        fig.tight_layout()
    return fig


def regression_dashboard_interactive(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    n_features: Optional[int] = None,
    title: Optional[str] = None,
    color: str = "#4c78a8",
    line_color: str = "#e45756",
    template: str = "plotly",
    height: int = 800,
    width: int = 1200,
) -> PlotlyFigure:
    """Interactive regression dashboard."""
    y_t = _as_array(y_true)
    y_p = _as_array(y_pred)
    res = _residuals(y_t, y_p)
    metrics = compute_regression_metrics(y_t, y_p, n_features=n_features).as_dict()
    keys = ["mae", "rmse", "medae", "r2"]
    if metrics.get("adj_r2") is not None:
        keys.append("adj_r2")
    fig = make_subplots(
        rows=2, cols=2,
        specs=[[{}, {}], [{}, {"type": "table"}]],
        subplot_titles=("Predicted vs Actual", "Residuals",
                        "Residual distribution", "Metrics"),
    )
    lo, hi = float(min(y_t.min(), y_p.min())), float(max(y_t.max(), y_p.max()))
    fig.add_trace(go.Scatter(x=y_t, y=y_p, mode="markers",
                             marker=dict(color=color), name="Pred"),
                  row=1, col=1)
    fig.add_trace(go.Scatter(x=[lo, hi], y=[lo, hi], mode="lines",
                             line=dict(color=line_color, width=2),
                             showlegend=False), row=1, col=1)
    fig.add_trace(go.Scatter(x=y_p, y=res, mode="markers",
                             marker=dict(color=color), showlegend=False),
                  row=1, col=2)
    fig.add_hline(y=0.0, line_dash="dash", line_color=line_color,
                  row=1, col=2)
    fig.add_trace(go.Histogram(x=res, marker_color=color, showlegend=False,
                               histnorm="probability density"),
                  row=2, col=1)
    fig.add_trace(go.Table(header=dict(values=["Metric", "Value"]),
                           cells=dict(values=[keys, [f"{metrics[k]:.4g}" for k in keys]])),
                  row=2, col=2)
    fig.update_layout(title=title or "Regression Dashboard",
                      template=template, height=height, width=width)
    return fig


regression_diagnostic_panel = regression_diagnostic_panel_static
regression_dashboard = regression_dashboard_static
