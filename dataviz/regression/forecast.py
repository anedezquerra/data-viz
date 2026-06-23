"""Forecasting and time-series regression charts."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from ..types import MatplotlibAxes, PlotlyFigure
from ..utils import setup_plot, apply_theme
from .helpers import _as_array


def forecast_vs_actual_static(time, y_true, y_pred, title=None, figsize=(11, 6),
                              true_color="#4c78a8", pred_color="#e45756",
                              style="default", theme="default", dpi=100,
                              **kwargs) -> MatplotlibAxes:
    """Overlay actual vs forecast time series."""
    t = _as_array(time)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Forecast vs Actual",
                             xlabel="time", ylabel="value", figsize=figsize)
        fig.set_dpi(dpi)
        ax.plot(t, _as_array(y_true), color=true_color, label="actual", **kwargs)
        ax.plot(t, _as_array(y_pred), color=pred_color, linestyle="--", label="forecast")
        ax.legend(); ax.grid(True, alpha=0.3); apply_theme(ax, theme)
    return ax


def forecast_vs_actual_interactive(time, y_true, y_pred, title=None,
                                   true_color="#4c78a8", pred_color="#e45756",
                                   template="plotly", height=600, width=1100,
                                   **kwargs) -> PlotlyFigure:
    """Interactive forecast/actual overlay."""
    t = _as_array(time)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=t, y=_as_array(y_true), mode="lines",
                             line=dict(color=true_color), name="actual", **kwargs))
    fig.add_trace(go.Scatter(x=t, y=_as_array(y_pred), mode="lines",
                             line=dict(color=pred_color, dash="dash"), name="forecast"))
    fig.update_layout(title=title or "Forecast vs Actual", template=template,
                      height=height, width=width, xaxis_title="time", yaxis_title="value")
    return fig


def forecast_error_over_horizon_static(horizons, errors, title=None, figsize=(10, 6),
                                       color="#4c78a8", style="default",
                                       theme="default", dpi=100, **kwargs) -> MatplotlibAxes:
    """Error metric (e.g., MAE/RMSE) as a function of forecast horizon."""
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Forecast Error by Horizon",
                             xlabel="horizon", ylabel="error", figsize=figsize)
        fig.set_dpi(dpi)
        ax.plot(_as_array(horizons), _as_array(errors), color=color, marker="o", **kwargs)
        ax.grid(True, alpha=0.3); apply_theme(ax, theme)
    return ax


def forecast_error_over_horizon_interactive(horizons, errors, title=None,
                                            color="#4c78a8", template="plotly",
                                            height=600, width=1000, **kwargs) -> PlotlyFigure:
    """Interactive forecast-error-by-horizon."""
    fig = go.Figure([go.Scatter(x=_as_array(horizons), y=_as_array(errors),
                                mode="lines+markers", line=dict(color=color), **kwargs)])
    fig.update_layout(title=title or "Forecast Error by Horizon", template=template,
                      height=height, width=width, xaxis_title="horizon",
                      yaxis_title="error")
    return fig


def rolling_forecast_origin_static(origins, scores, title=None, figsize=(10, 6),
                                   color="#4c78a8", style="default", theme="default",
                                   dpi=100, **kwargs) -> MatplotlibAxes:
    """Score across rolling forecast origins."""
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Rolling Forecast Origin",
                             xlabel="origin", ylabel="score", figsize=figsize)
        fig.set_dpi(dpi)
        ax.plot(_as_array(origins), _as_array(scores), color=color, marker="o", **kwargs)
        ax.grid(True, alpha=0.3); apply_theme(ax, theme)
    return ax


def rolling_forecast_origin_interactive(origins, scores, title=None, color="#4c78a8",
                                        template="plotly", height=600, width=1000,
                                        **kwargs) -> PlotlyFigure:
    """Interactive rolling-origin score curve."""
    fig = go.Figure([go.Scatter(x=_as_array(origins), y=_as_array(scores),
                                mode="lines+markers", line=dict(color=color), **kwargs)])
    fig.update_layout(title=title or "Rolling Forecast Origin", template=template,
                      height=height, width=width, xaxis_title="origin", yaxis_title="score")
    return fig


def backtest_error_distribution_static(errors, title=None, figsize=(10, 6),
                                       color="#4c78a8", bins=30, style="default",
                                       theme="default", dpi=100, **kwargs) -> MatplotlibAxes:
    """Histogram of backtest errors."""
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Backtest Error Distribution",
                             xlabel="error", ylabel="count", figsize=figsize)
        fig.set_dpi(dpi)
        ax.hist(_as_array(errors), bins=bins, color=color, edgecolor="white", **kwargs)
        ax.axvline(0, color="#e45756", linestyle="--")
        ax.grid(True, alpha=0.3); apply_theme(ax, theme)
    return ax


def backtest_error_distribution_interactive(errors, title=None, color="#4c78a8",
                                            nbins=30, template="plotly", height=600,
                                            width=1000, **kwargs) -> PlotlyFigure:
    """Interactive backtest-error histogram."""
    fig = go.Figure([go.Histogram(x=_as_array(errors), nbinsx=nbins,
                                  marker_color=color, **kwargs)])
    fig.add_vline(x=0, line_dash="dash", line_color="#e45756")
    fig.update_layout(title=title or "Backtest Error Distribution", template=template,
                      height=height, width=width, xaxis_title="error", yaxis_title="count")
    return fig


def expanding_window_metric_curve_static(window_sizes, metric_values, title=None,
                                         figsize=(10, 6), color="#4c78a8",
                                         metric_name="metric", style="default",
                                         theme="default", dpi=100, **kwargs) -> MatplotlibAxes:
    """Metric as the training window expands."""
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Expanding-Window Metric",
                             xlabel="window size", ylabel=metric_name, figsize=figsize)
        fig.set_dpi(dpi)
        ax.plot(_as_array(window_sizes), _as_array(metric_values),
                color=color, marker="o", **kwargs)
        ax.grid(True, alpha=0.3); apply_theme(ax, theme)
    return ax


def expanding_window_metric_curve_interactive(window_sizes, metric_values, title=None,
                                              color="#4c78a8", metric_name="metric",
                                              template="plotly", height=600, width=1000,
                                              **kwargs) -> PlotlyFigure:
    """Interactive expanding-window metric curve."""
    fig = go.Figure([go.Scatter(x=_as_array(window_sizes), y=_as_array(metric_values),
                                mode="lines+markers", line=dict(color=color), **kwargs)])
    fig.update_layout(title=title or "Expanding-Window Metric", template=template,
                      height=height, width=width, xaxis_title="window size",
                      yaxis_title=metric_name)
    return fig


def forecast_band_plot_static(time, y_true, y_pred, lower, upper, title=None,
                              figsize=(11, 6), pred_color="#4c78a8",
                              true_color="#222222", band_color="#a8c5e0",
                              style="default", theme="default", dpi=100,
                              **kwargs) -> MatplotlibAxes:
    """Forecast central path with prediction band and actual overlay."""
    t = _as_array(time)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Forecast Band", xlabel="time",
                             ylabel="value", figsize=figsize)
        fig.set_dpi(dpi)
        ax.fill_between(t, _as_array(lower), _as_array(upper), color=band_color,
                        alpha=0.4, label="band")
        ax.plot(t, _as_array(y_pred), color=pred_color, label="forecast", **kwargs)
        ax.plot(t, _as_array(y_true), color=true_color, linestyle="--", label="actual")
        ax.legend(); ax.grid(True, alpha=0.3); apply_theme(ax, theme)
    return ax


def forecast_band_plot_interactive(time, y_true, y_pred, lower, upper, title=None,
                                   pred_color="#4c78a8", true_color="#222222",
                                   band_color="rgba(168,197,224,0.4)",
                                   template="plotly", height=600, width=1100,
                                   **kwargs) -> PlotlyFigure:
    """Interactive forecast band."""
    t = _as_array(time)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=t, y=_as_array(upper), mode="lines",
                             line=dict(width=0), showlegend=False))
    fig.add_trace(go.Scatter(x=t, y=_as_array(lower), mode="lines", line=dict(width=0),
                             fill="tonexty", fillcolor=band_color, name="band"))
    fig.add_trace(go.Scatter(x=t, y=_as_array(y_pred), mode="lines",
                             line=dict(color=pred_color, width=2), name="forecast", **kwargs))
    fig.add_trace(go.Scatter(x=t, y=_as_array(y_true), mode="lines",
                             line=dict(color=true_color, dash="dash"), name="actual"))
    fig.update_layout(title=title or "Forecast Band", template=template,
                      height=height, width=width, xaxis_title="time", yaxis_title="value")
    return fig


forecast_vs_actual = forecast_vs_actual_static
forecast_error_over_horizon = forecast_error_over_horizon_static
rolling_forecast_origin = rolling_forecast_origin_static
backtest_error_distribution = backtest_error_distribution_static
expanding_window_metric_curve = expanding_window_metric_curve_static
forecast_band_plot = forecast_band_plot_static
