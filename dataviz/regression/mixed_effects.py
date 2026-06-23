"""Mixed-effects / hierarchical regression charts."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from ..types import MatplotlibAxes, PlotlyFigure
from ..utils import setup_plot, apply_theme
from .helpers import _as_array


def random_effect_caterpillar_static(group_labels, effects, std_errors=None, title=None,
                                     figsize=(8, 8), color="#4c78a8", style="default",
                                     theme="default", dpi=100, **kwargs) -> MatplotlibAxes:
    """Caterpillar plot of random effects (sorted) with ±SE bars."""
    g = list(group_labels); e = _as_array(effects)
    order = np.argsort(e); e_sorted = e[order]
    labels_sorted = [g[i] for i in order]
    pos = np.arange(len(e))
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Random Effects (caterpillar)",
                             xlabel="effect", ylabel="group", figsize=figsize)
        fig.set_dpi(dpi)
        if std_errors is not None:
            se = _as_array(std_errors)[order]
            ax.errorbar(e_sorted, pos, xerr=1.96 * se, fmt="o", color=color, **kwargs)
        else:
            ax.scatter(e_sorted, pos, color=color, **kwargs)
        ax.axvline(0, color="#888", linestyle="--")
        ax.set_yticks(pos); ax.set_yticklabels(labels_sorted, fontsize=8)
        ax.grid(True, axis="x", alpha=0.3); apply_theme(ax, theme)
    return ax


def random_effect_caterpillar_interactive(group_labels, effects, std_errors=None,
                                          title=None, color="#4c78a8",
                                          template="plotly", height=800, width=800,
                                          **kwargs) -> PlotlyFigure:
    """Interactive random-effect caterpillar."""
    g = list(group_labels); e = _as_array(effects)
    order = np.argsort(e); e_sorted = e[order]
    labels_sorted = [g[i] for i in order]
    err = None
    if std_errors is not None:
        se = _as_array(std_errors)[order]
        err = dict(type="data", array=1.96 * se)
    fig = go.Figure([go.Scatter(x=e_sorted, y=labels_sorted, mode="markers",
                                marker=dict(color=color, size=8),
                                error_x=err, **kwargs)])
    fig.add_vline(x=0, line_dash="dash", line_color="#888")
    fig.update_layout(title=title or "Random Effects (caterpillar)", template=template,
                      height=height, width=width,
                      xaxis_title="effect", yaxis_title="group")
    return fig


def random_intercept_slope_scatter_static(intercepts, slopes, title=None,
                                          figsize=(8, 8), color="#4c78a8",
                                          style="default", theme="default", dpi=100,
                                          **kwargs) -> MatplotlibAxes:
    """Per-group random intercept vs random slope."""
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Random Intercept vs Slope",
                             xlabel="intercept", ylabel="slope", figsize=figsize)
        fig.set_dpi(dpi)
        ax.scatter(_as_array(intercepts), _as_array(slopes), color=color, alpha=0.7, **kwargs)
        ax.axhline(0, color="#888", linestyle="--"); ax.axvline(0, color="#888", linestyle="--")
        ax.grid(True, alpha=0.3); apply_theme(ax, theme)
    return ax


def random_intercept_slope_scatter_interactive(intercepts, slopes, title=None,
                                               color="#4c78a8", template="plotly",
                                               height=650, width=750,
                                               **kwargs) -> PlotlyFigure:
    """Interactive random intercept/slope scatter."""
    fig = go.Figure([go.Scatter(x=_as_array(intercepts), y=_as_array(slopes),
                                mode="markers", marker=dict(color=color), **kwargs)])
    fig.add_hline(y=0, line_dash="dash", line_color="#888")
    fig.add_vline(x=0, line_dash="dash", line_color="#888")
    fig.update_layout(title=title or "Random Intercept vs Slope", template=template,
                      height=height, width=width, xaxis_title="intercept", yaxis_title="slope")
    return fig


def group_means_vs_predicted_static(group_labels, group_observed_means,
                                    group_predicted_means, title=None, figsize=(10, 6),
                                    obs_color="#4c78a8", pred_color="#e45756",
                                    style="default", theme="default", dpi=100,
                                    **kwargs) -> MatplotlibAxes:
    """Observed vs model-predicted group means."""
    g = list(group_labels)
    obs = _as_array(group_observed_means); pred = _as_array(group_predicted_means)
    pos = np.arange(len(g)); w = 0.4
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Group Means: Observed vs Predicted",
                             xlabel="group", ylabel="mean", figsize=figsize)
        fig.set_dpi(dpi)
        ax.bar(pos - w / 2, obs, width=w, color=obs_color, label="observed", **kwargs)
        ax.bar(pos + w / 2, pred, width=w, color=pred_color, label="predicted")
        ax.set_xticks(pos); ax.set_xticklabels(g, rotation=45)
        ax.legend(); ax.grid(True, axis="y", alpha=0.3); apply_theme(ax, theme)
    return ax


def group_means_vs_predicted_interactive(group_labels, group_observed_means,
                                         group_predicted_means, title=None,
                                         obs_color="#4c78a8", pred_color="#e45756",
                                         template="plotly", height=600, width=1100,
                                         **kwargs) -> PlotlyFigure:
    """Interactive observed vs predicted group means."""
    g = list(group_labels)
    fig = go.Figure([
        go.Bar(x=g, y=_as_array(group_observed_means), marker_color=obs_color,
               name="observed", **kwargs),
        go.Bar(x=g, y=_as_array(group_predicted_means), marker_color=pred_color,
               name="predicted"),
    ])
    fig.update_layout(title=title or "Group Means: Observed vs Predicted",
                      barmode="group", template=template, height=height, width=width,
                      xaxis_title="group", yaxis_title="mean")
    return fig


random_effect_caterpillar = random_effect_caterpillar_static
random_intercept_slope_scatter = random_intercept_slope_scatter_static
group_means_vs_predicted = group_means_vs_predicted_static
