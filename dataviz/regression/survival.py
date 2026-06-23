"""Survival-regression diagnostic charts."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from ..types import MatplotlibAxes, PlotlyFigure
from ..utils import setup_plot, apply_theme
from .helpers import _as_array


def km_predicted_vs_observed_static(times, km_observed, km_predicted, title=None,
                                    figsize=(10, 6), obs_color="#4c78a8",
                                    pred_color="#e45756", style="default",
                                    theme="default", dpi=100, **kwargs) -> MatplotlibAxes:
    """Observed vs predicted Kaplan–Meier survival curves."""
    t = _as_array(times)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "KM Predicted vs Observed",
                             xlabel="time", ylabel="S(t)", figsize=figsize)
        fig.set_dpi(dpi)
        ax.step(t, _as_array(km_observed), where="post", color=obs_color, label="observed", **kwargs)
        ax.step(t, _as_array(km_predicted), where="post", color=pred_color, label="predicted")
        ax.set_ylim(0, 1.02); ax.legend(); ax.grid(True, alpha=0.3); apply_theme(ax, theme)
    return ax


def km_predicted_vs_observed_interactive(times, km_observed, km_predicted, title=None,
                                         obs_color="#4c78a8", pred_color="#e45756",
                                         template="plotly", height=600, width=1000,
                                         **kwargs) -> PlotlyFigure:
    """Interactive KM observed/predicted overlay."""
    t = _as_array(times)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=t, y=_as_array(km_observed), mode="lines",
                             line=dict(color=obs_color, shape="hv"), name="observed", **kwargs))
    fig.add_trace(go.Scatter(x=t, y=_as_array(km_predicted), mode="lines",
                             line=dict(color=pred_color, shape="hv"), name="predicted"))
    fig.update_layout(title=title or "KM Predicted vs Observed", template=template,
                      height=height, width=width, xaxis_title="time", yaxis_title="S(t)",
                      yaxis=dict(range=[0, 1.02]))
    return fig


def cox_residual_plot_static(time, residuals, kind="martingale", title=None,
                             figsize=(10, 6), color="#4c78a8", style="default",
                             theme="default", dpi=100, **kwargs) -> MatplotlibAxes:
    """Cox model residuals (martingale/deviance/schoenfeld) vs time."""
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or f"Cox {kind.title()} Residuals",
                             xlabel="time", ylabel=f"{kind} residual", figsize=figsize)
        fig.set_dpi(dpi)
        ax.scatter(_as_array(time), _as_array(residuals), color=color, alpha=0.7, **kwargs)
        ax.axhline(0, color="#e45756", linestyle="--"); ax.grid(True, alpha=0.3); apply_theme(ax, theme)
    return ax


def cox_residual_plot_interactive(time, residuals, kind="martingale", title=None,
                                  color="#4c78a8", template="plotly", height=600,
                                  width=1000, **kwargs) -> PlotlyFigure:
    """Interactive Cox residuals."""
    fig = go.Figure([go.Scatter(x=_as_array(time), y=_as_array(residuals),
                                mode="markers", marker=dict(color=color), **kwargs)])
    fig.add_hline(y=0, line_dash="dash", line_color="#e45756")
    fig.update_layout(title=title or f"Cox {kind.title()} Residuals", template=template,
                      height=height, width=width, xaxis_title="time",
                      yaxis_title=f"{kind} residual")
    return fig


def proportional_hazards_test_plot_static(covariate_names, p_values, title=None,
                                          figsize=(10, 6), color="#4c78a8",
                                          alpha=0.05, style="default", theme="default",
                                          dpi=100, **kwargs) -> MatplotlibAxes:
    """Bar of Schoenfeld PH-assumption test p-values per covariate."""
    names = list(covariate_names); p = _as_array(p_values)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Proportional Hazards Test",
                             xlabel="covariate", ylabel="p-value", figsize=figsize)
        fig.set_dpi(dpi)
        ax.bar(names, p, color=color, **kwargs)
        ax.axhline(alpha, color="#e45756", linestyle="--", label=f"α={alpha}")
        ax.tick_params(axis="x", rotation=45); ax.legend(); ax.grid(True, axis="y", alpha=0.3)
        apply_theme(ax, theme)
    return ax


def proportional_hazards_test_plot_interactive(covariate_names, p_values, title=None,
                                               color="#4c78a8", alpha=0.05,
                                               template="plotly", height=600,
                                               width=1000, **kwargs) -> PlotlyFigure:
    """Interactive PH-test bar chart."""
    fig = go.Figure([go.Bar(x=list(covariate_names), y=_as_array(p_values),
                            marker_color=color, **kwargs)])
    fig.add_hline(y=alpha, line_dash="dash", line_color="#e45756",
                  annotation_text=f"α={alpha}")
    fig.update_layout(title=title or "Proportional Hazards Test", template=template,
                      height=height, width=width, xaxis_title="covariate",
                      yaxis_title="p-value")
    return fig


km_predicted_vs_observed = km_predicted_vs_observed_static
cox_residual_plot = cox_residual_plot_static
proportional_hazards_test_plot = proportional_hazards_test_plot_static
