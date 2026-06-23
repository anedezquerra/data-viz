"""Quantile and robust-regression charts."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from ..types import ArrayLike, MatplotlibAxes, PlotlyFigure
from ..utils import setup_plot, apply_theme
from .helpers import _as_array


def quantile_regression_band_static(x, y, y_low, y_med, y_high, title=None,
                                    figsize=(10, 6), color="#4c78a8",
                                    band_color="#a8c5e0", theme="default",
                                    style="default", dpi=100, **kwargs) -> MatplotlibAxes:
    """Quantile-regression band: low/median/high prediction quantiles vs x."""
    x = _as_array(x); order = np.argsort(x)
    xs = x[order]
    yl, ym, yh = _as_array(y_low)[order], _as_array(y_med)[order], _as_array(y_high)[order]
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Quantile Regression Band",
                             xlabel="x", ylabel="y", figsize=figsize)
        fig.set_dpi(dpi)
        ax.scatter(x, y, color="#666", alpha=0.4, s=15)
        ax.fill_between(xs, yl, yh, color=band_color, alpha=0.5, label="quantile band")
        ax.plot(xs, ym, color=color, linewidth=2, label="median", **kwargs)
        ax.legend(); ax.grid(True, alpha=0.3); apply_theme(ax, theme)
    return ax


def quantile_regression_band_interactive(x, y, y_low, y_med, y_high, title=None,
                                         color="#4c78a8", band_color="rgba(168,197,224,0.5)",
                                         template="plotly", height=600, width=1000,
                                         **kwargs) -> PlotlyFigure:
    """Interactive quantile-regression band."""
    x = _as_array(x); order = np.argsort(x); xs = x[order]
    yl, ym, yh = _as_array(y_low)[order], _as_array(y_med)[order], _as_array(y_high)[order]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=xs, y=yh, mode="lines", line=dict(width=0), showlegend=False))
    fig.add_trace(go.Scatter(x=xs, y=yl, mode="lines", line=dict(width=0),
                             fill="tonexty", fillcolor=band_color, name="quantile band"))
    fig.add_trace(go.Scatter(x=x, y=y, mode="markers",
                             marker=dict(color="#666", size=4, opacity=0.5), name="obs"))
    fig.add_trace(go.Scatter(x=xs, y=ym, mode="lines",
                             line=dict(color=color, width=2), name="median", **kwargs))
    fig.update_layout(title=title or "Quantile Regression Band", template=template,
                      height=height, width=width, xaxis_title="x", yaxis_title="y")
    return fig


def quantile_loss_curve_static(quantiles, losses, title=None, figsize=(10, 6),
                               color="#4c78a8", style="default", theme="default",
                               dpi=100, **kwargs) -> MatplotlibAxes:
    """Plot pinball/quantile loss across τ values."""
    q = _as_array(quantiles); l = _as_array(losses)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Quantile Loss Curve",
                             xlabel="τ", ylabel="pinball loss", figsize=figsize)
        fig.set_dpi(dpi)
        ax.plot(q, l, color=color, marker="o", **kwargs)
        ax.grid(True, alpha=0.3); apply_theme(ax, theme)
    return ax


def quantile_loss_curve_interactive(quantiles, losses, title=None, color="#4c78a8",
                                    template="plotly", height=600, width=900,
                                    **kwargs) -> PlotlyFigure:
    """Interactive quantile-loss curve."""
    fig = go.Figure([go.Scatter(x=_as_array(quantiles), y=_as_array(losses),
                                mode="lines+markers", line=dict(color=color), **kwargs)])
    fig.update_layout(title=title or "Quantile Loss Curve", xaxis_title="τ",
                      yaxis_title="pinball loss", template=template,
                      height=height, width=width)
    return fig


def huber_vs_ols_overlay_static(x, y, y_ols, y_huber, title=None, figsize=(10, 6),
                                ols_color="#4c78a8", huber_color="#e45756",
                                style="default", theme="default", dpi=100,
                                **kwargs) -> MatplotlibAxes:
    """Overlay OLS and Huber fits over a scatter."""
    x = _as_array(x); order = np.argsort(x); xs = x[order]
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Huber vs OLS", xlabel="x",
                             ylabel="y", figsize=figsize)
        fig.set_dpi(dpi)
        ax.scatter(x, y, color="#666", alpha=0.5, s=18)
        ax.plot(xs, _as_array(y_ols)[order], color=ols_color, label="OLS", **kwargs)
        ax.plot(xs, _as_array(y_huber)[order], color=huber_color, label="Huber")
        ax.legend(); ax.grid(True, alpha=0.3); apply_theme(ax, theme)
    return ax


def huber_vs_ols_overlay_interactive(x, y, y_ols, y_huber, title=None,
                                     ols_color="#4c78a8", huber_color="#e45756",
                                     template="plotly", height=600, width=1000,
                                     **kwargs) -> PlotlyFigure:
    """Interactive Huber/OLS overlay."""
    x = _as_array(x); order = np.argsort(x); xs = x[order]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode="markers",
                             marker=dict(color="#666", size=5, opacity=0.5), name="obs"))
    fig.add_trace(go.Scatter(x=xs, y=_as_array(y_ols)[order], mode="lines",
                             line=dict(color=ols_color, width=2), name="OLS", **kwargs))
    fig.add_trace(go.Scatter(x=xs, y=_as_array(y_huber)[order], mode="lines",
                             line=dict(color=huber_color, width=2), name="Huber"))
    fig.update_layout(title=title or "Huber vs OLS", template=template,
                      height=height, width=width, xaxis_title="x", yaxis_title="y")
    return fig


def weighted_residual_plot_static(y_pred, residuals, weights, title=None,
                                  figsize=(10, 6), cmap="viridis", style="default",
                                  theme="default", dpi=100, **kwargs) -> MatplotlibAxes:
    """Residual scatter coloured by observation weight."""
    yp, r, w = _as_array(y_pred), _as_array(residuals), _as_array(weights)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Weighted Residuals",
                             xlabel="Predicted", ylabel="Residual", figsize=figsize)
        fig.set_dpi(dpi)
        sc = ax.scatter(yp, r, c=w, cmap=cmap, s=22, **kwargs)
        ax.axhline(0, color="#e45756", linestyle="--")
        fig.colorbar(sc, ax=ax, label="weight")
        ax.grid(True, alpha=0.3); apply_theme(ax, theme)
    return ax


def weighted_residual_plot_interactive(y_pred, residuals, weights, title=None,
                                       colorscale="Viridis", template="plotly",
                                       height=600, width=1000, **kwargs) -> PlotlyFigure:
    """Interactive weighted-residual plot."""
    yp, r, w = _as_array(y_pred), _as_array(residuals), _as_array(weights)
    fig = go.Figure([go.Scatter(x=yp, y=r, mode="markers",
                                marker=dict(color=w, colorscale=colorscale,
                                            showscale=True,
                                            colorbar=dict(title="weight")), **kwargs)])
    fig.add_hline(y=0, line_dash="dash", line_color="#e45756")
    fig.update_layout(title=title or "Weighted Residuals", template=template,
                      height=height, width=width,
                      xaxis_title="Predicted", yaxis_title="Residual")
    return fig


quantile_regression_band = quantile_regression_band_static
quantile_loss_curve = quantile_loss_curve_static
huber_vs_ols_overlay = huber_vs_ols_overlay_static
weighted_residual_plot = weighted_residual_plot_static
