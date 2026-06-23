"""Model selection charts (AIC/BIC, stepwise, best-subset)."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from ..types import MatplotlibAxes, PlotlyFigure
from ..utils import setup_plot, apply_theme
from .helpers import _as_array


def aic_bic_bar_static(model_names, aic, bic, title=None, figsize=(10, 6),
                       aic_color="#4c78a8", bic_color="#e45756", style="default",
                       theme="default", dpi=100, **kwargs) -> MatplotlibAxes:
    """Grouped AIC/BIC bar chart per candidate model."""
    names = list(model_names); a = _as_array(aic); b = _as_array(bic)
    pos = np.arange(len(names)); w = 0.4
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "AIC / BIC", xlabel="model",
                             ylabel="information criterion", figsize=figsize)
        fig.set_dpi(dpi)
        ax.bar(pos - w / 2, a, width=w, color=aic_color, label="AIC", **kwargs)
        ax.bar(pos + w / 2, b, width=w, color=bic_color, label="BIC")
        ax.set_xticks(pos); ax.set_xticklabels(names, rotation=45)
        ax.legend(); ax.grid(True, axis="y", alpha=0.3); apply_theme(ax, theme)
    return ax


def aic_bic_bar_interactive(model_names, aic, bic, title=None, aic_color="#4c78a8",
                            bic_color="#e45756", template="plotly", height=600,
                            width=1000, **kwargs) -> PlotlyFigure:
    """Interactive AIC/BIC bar chart."""
    fig = go.Figure([
        go.Bar(x=list(model_names), y=_as_array(aic), marker_color=aic_color, name="AIC", **kwargs),
        go.Bar(x=list(model_names), y=_as_array(bic), marker_color=bic_color, name="BIC"),
    ])
    fig.update_layout(title=title or "AIC / BIC", barmode="group", template=template,
                      height=height, width=width, xaxis_title="model",
                      yaxis_title="information criterion")
    return fig


def nested_model_comparison_plot_static(model_names, log_likelihoods,
                                        df_diff=None, title=None, figsize=(10, 6),
                                        color="#4c78a8", style="default",
                                        theme="default", dpi=100, **kwargs) -> MatplotlibAxes:
    """Nested model log-likelihood progression."""
    names = list(model_names); ll = _as_array(log_likelihoods)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Nested Model Log-Likelihood",
                             xlabel="model", ylabel="log L", figsize=figsize)
        fig.set_dpi(dpi)
        ax.plot(names, ll, color=color, marker="o", **kwargs)
        ax.tick_params(axis="x", rotation=45); ax.grid(True, alpha=0.3); apply_theme(ax, theme)
    return ax


def nested_model_comparison_plot_interactive(model_names, log_likelihoods,
                                             df_diff=None, title=None, color="#4c78a8",
                                             template="plotly", height=600, width=1000,
                                             **kwargs) -> PlotlyFigure:
    """Interactive nested-model comparison."""
    fig = go.Figure([go.Scatter(x=list(model_names), y=_as_array(log_likelihoods),
                                mode="lines+markers", line=dict(color=color), **kwargs)])
    fig.update_layout(title=title or "Nested Model Log-Likelihood", template=template,
                      height=height, width=width, xaxis_title="model", yaxis_title="log L")
    return fig


def stepwise_selection_path_static(step_labels, scores, title=None, figsize=(11, 6),
                                   color="#4c78a8", metric_name="score",
                                   style="default", theme="default", dpi=100,
                                   **kwargs) -> MatplotlibAxes:
    """Step-by-step stepwise (forward/backward) selection trajectory."""
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Stepwise Selection Path",
                             xlabel="step", ylabel=metric_name, figsize=figsize)
        fig.set_dpi(dpi)
        ax.plot(list(step_labels), _as_array(scores), color=color, marker="o", **kwargs)
        ax.tick_params(axis="x", rotation=45); ax.grid(True, alpha=0.3); apply_theme(ax, theme)
    return ax


def stepwise_selection_path_interactive(step_labels, scores, title=None,
                                        color="#4c78a8", metric_name="score",
                                        template="plotly", height=600, width=1100,
                                        **kwargs) -> PlotlyFigure:
    """Interactive stepwise selection path."""
    fig = go.Figure([go.Scatter(x=list(step_labels), y=_as_array(scores),
                                mode="lines+markers", line=dict(color=color), **kwargs)])
    fig.update_layout(title=title or "Stepwise Selection Path", template=template,
                      height=height, width=width, xaxis_title="step", yaxis_title=metric_name)
    return fig


def forward_selection_score_curve_static(num_features, scores, title=None,
                                         figsize=(10, 6), color="#4c78a8",
                                         metric_name="score", style="default",
                                         theme="default", dpi=100, **kwargs) -> MatplotlibAxes:
    """Score as additional features are added forward."""
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Forward Selection Score Curve",
                             xlabel="# features", ylabel=metric_name, figsize=figsize)
        fig.set_dpi(dpi)
        ax.plot(_as_array(num_features), _as_array(scores), color=color, marker="o", **kwargs)
        ax.grid(True, alpha=0.3); apply_theme(ax, theme)
    return ax


def forward_selection_score_curve_interactive(num_features, scores, title=None,
                                              color="#4c78a8", metric_name="score",
                                              template="plotly", height=600, width=1000,
                                              **kwargs) -> PlotlyFigure:
    """Interactive forward-selection score curve."""
    fig = go.Figure([go.Scatter(x=_as_array(num_features), y=_as_array(scores),
                                mode="lines+markers", line=dict(color=color), **kwargs)])
    fig.update_layout(title=title or "Forward Selection Score Curve", template=template,
                      height=height, width=width,
                      xaxis_title="# features", yaxis_title=metric_name)
    return fig


def best_subset_metric_bar_static(subset_labels, metric_values, title=None,
                                  figsize=(11, 6), color="#4c78a8",
                                  metric_name="metric", highlight_color="#e45756",
                                  style="default", theme="default", dpi=100,
                                  **kwargs) -> MatplotlibAxes:
    """Best-subset metric per candidate subset; minimum highlighted."""
    labels = list(subset_labels); m = _as_array(metric_values)
    best = int(np.argmin(m)) if m.size else -1
    colors = [highlight_color if i == best else color for i in range(len(m))]
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Best-Subset Metric", xlabel="subset",
                             ylabel=metric_name, figsize=figsize)
        fig.set_dpi(dpi)
        ax.bar(labels, m, color=colors, **kwargs)
        ax.tick_params(axis="x", rotation=45); ax.grid(True, axis="y", alpha=0.3)
        apply_theme(ax, theme)
    return ax


def best_subset_metric_bar_interactive(subset_labels, metric_values, title=None,
                                       color="#4c78a8", metric_name="metric",
                                       highlight_color="#e45756", template="plotly",
                                       height=600, width=1100, **kwargs) -> PlotlyFigure:
    """Interactive best-subset metric bar."""
    labels = list(subset_labels); m = _as_array(metric_values)
    best = int(np.argmin(m)) if m.size else -1
    colors = [highlight_color if i == best else color for i in range(len(m))]
    fig = go.Figure([go.Bar(x=labels, y=m, marker_color=colors, **kwargs)])
    fig.update_layout(title=title or "Best-Subset Metric", template=template,
                      height=height, width=width, xaxis_title="subset",
                      yaxis_title=metric_name)
    return fig


aic_bic_bar = aic_bic_bar_static
nested_model_comparison_plot = nested_model_comparison_plot_static
stepwise_selection_path = stepwise_selection_path_static
forward_selection_score_curve = forward_selection_score_curve_static
best_subset_metric_bar = best_subset_metric_bar_static
