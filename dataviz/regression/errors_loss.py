"""Loss / error distribution charts."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from ..types import MatplotlibAxes, PlotlyFigure
from ..utils import setup_plot, apply_theme
from .helpers import _as_array


def loss_distribution_violin_static(model_labels, losses_per_model, title=None,
                                    figsize=(11, 6), color="#4c78a8",
                                    metric_name="loss", style="default",
                                    theme="default", dpi=100, **kwargs) -> MatplotlibAxes:
    """Violin plot of per-observation losses across models."""
    data = [list(l) for l in losses_per_model]
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Loss Distribution", xlabel="model",
                             ylabel=metric_name, figsize=figsize)
        fig.set_dpi(dpi)
        vp = ax.violinplot(data, showmeans=True, **kwargs)
        for body in vp["bodies"]: body.set_facecolor(color); body.set_alpha(0.5)
        ax.set_xticks(range(1, len(data) + 1)); ax.set_xticklabels(list(model_labels))
        ax.grid(True, alpha=0.3); apply_theme(ax, theme)
    return ax


def loss_distribution_violin_interactive(model_labels, losses_per_model, title=None,
                                         color="#4c78a8", metric_name="loss",
                                         template="plotly", height=600, width=1100,
                                         **kwargs) -> PlotlyFigure:
    """Interactive loss distribution violins."""
    fig = go.Figure()
    for lbl, l in zip(model_labels, losses_per_model):
        fig.add_trace(go.Violin(y=list(l), name=str(lbl), line_color=color,
                                box_visible=True, meanline_visible=True, **kwargs))
    fig.update_layout(title=title or "Loss Distribution", template=template,
                      height=height, width=width, xaxis_title="model",
                      yaxis_title=metric_name)
    return fig


def ranked_error_plot_static(errors, title=None, figsize=(10, 6), color="#4c78a8",
                             style="default", theme="default", dpi=100,
                             **kwargs) -> MatplotlibAxes:
    """Errors sorted by magnitude."""
    e = np.sort(_as_array(errors))
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Ranked Errors", xlabel="rank",
                             ylabel="error", figsize=figsize)
        fig.set_dpi(dpi)
        ax.plot(np.arange(len(e)), e, color=color, **kwargs)
        ax.axhline(0, color="#e45756", linestyle="--")
        ax.grid(True, alpha=0.3); apply_theme(ax, theme)
    return ax


def ranked_error_plot_interactive(errors, title=None, color="#4c78a8",
                                  template="plotly", height=600, width=1000,
                                  **kwargs) -> PlotlyFigure:
    """Interactive ranked-error plot."""
    e = np.sort(_as_array(errors))
    fig = go.Figure([go.Scatter(x=np.arange(len(e)), y=e, mode="lines",
                                line=dict(color=color), **kwargs)])
    fig.add_hline(y=0, line_dash="dash", line_color="#e45756")
    fig.update_layout(title=title or "Ranked Errors", template=template,
                      height=height, width=width, xaxis_title="rank", yaxis_title="error")
    return fig


def worst_k_predictions_chart_static(y_true, y_pred, k=10, title=None,
                                     figsize=(10, 6), color="#4c78a8",
                                     style="default", theme="default", dpi=100,
                                     **kwargs) -> MatplotlibAxes:
    """Top-k worst predictions by absolute error."""
    yt, yp = _as_array(y_true), _as_array(y_pred)
    err = np.abs(yt - yp); idx = np.argsort(-err)[:k]
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or f"Worst {k} Predictions",
                             xlabel="observation index", ylabel="|error|", figsize=figsize)
        fig.set_dpi(dpi)
        ax.bar([str(i) for i in idx], err[idx], color=color, **kwargs)
        ax.tick_params(axis="x", rotation=45); ax.grid(True, axis="y", alpha=0.3)
        apply_theme(ax, theme)
    return ax


def worst_k_predictions_chart_interactive(y_true, y_pred, k=10, title=None,
                                          color="#4c78a8", template="plotly",
                                          height=600, width=1000, **kwargs) -> PlotlyFigure:
    """Interactive worst-k predictions."""
    yt, yp = _as_array(y_true), _as_array(y_pred)
    err = np.abs(yt - yp); idx = np.argsort(-err)[:k]
    fig = go.Figure([go.Bar(x=[str(i) for i in idx], y=err[idx],
                            marker_color=color, **kwargs)])
    fig.update_layout(title=title or f"Worst {k} Predictions", template=template,
                      height=height, width=width,
                      xaxis_title="observation index", yaxis_title="|error|")
    return fig


def error_decomposition_bar_static(components, values, title=None, figsize=(10, 6),
                                   color="#4c78a8", style="default",
                                   theme="default", dpi=100, **kwargs) -> MatplotlibAxes:
    """Bar of error components (e.g., bias², variance, noise)."""
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Error Decomposition",
                             xlabel="component", ylabel="value", figsize=figsize)
        fig.set_dpi(dpi)
        ax.bar(list(components), _as_array(values), color=color, **kwargs)
        ax.grid(True, axis="y", alpha=0.3); apply_theme(ax, theme)
    return ax


def error_decomposition_bar_interactive(components, values, title=None,
                                        color="#4c78a8", template="plotly",
                                        height=600, width=1000, **kwargs) -> PlotlyFigure:
    """Interactive error-decomposition bar."""
    fig = go.Figure([go.Bar(x=list(components), y=_as_array(values),
                            marker_color=color, **kwargs)])
    fig.update_layout(title=title or "Error Decomposition", template=template,
                      height=height, width=width,
                      xaxis_title="component", yaxis_title="value")
    return fig


loss_distribution_violin = loss_distribution_violin_static
ranked_error_plot = ranked_error_plot_static
worst_k_predictions_chart = worst_k_predictions_chart_static
error_decomposition_bar = error_decomposition_bar_static
