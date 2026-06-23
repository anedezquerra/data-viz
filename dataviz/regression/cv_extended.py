"""Extended cross-validation diagnostics."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from ..types import MatplotlibAxes, PlotlyFigure
from ..utils import setup_plot, apply_theme
from .helpers import _as_array


def learning_curve_with_band_static(train_sizes, mean_scores, std_scores, title=None,
                                    figsize=(10, 6), color="#4c78a8",
                                    band_color="#a8c5e0", metric_name="score",
                                    style="default", theme="default", dpi=100,
                                    **kwargs) -> MatplotlibAxes:
    """Learning curve with mean ± std band."""
    ts = _as_array(train_sizes); mu = _as_array(mean_scores); sd = _as_array(std_scores)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Learning Curve",
                             xlabel="train size", ylabel=metric_name, figsize=figsize)
        fig.set_dpi(dpi)
        ax.fill_between(ts, mu - sd, mu + sd, color=band_color, alpha=0.4)
        ax.plot(ts, mu, color=color, marker="o", **kwargs)
        ax.grid(True, alpha=0.3); apply_theme(ax, theme)
    return ax


def learning_curve_with_band_interactive(train_sizes, mean_scores, std_scores,
                                         title=None, color="#4c78a8",
                                         band_color="rgba(168,197,224,0.4)",
                                         metric_name="score", template="plotly",
                                         height=600, width=1000, **kwargs) -> PlotlyFigure:
    """Interactive learning curve with band."""
    ts = _as_array(train_sizes); mu = _as_array(mean_scores); sd = _as_array(std_scores)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=ts, y=mu + sd, mode="lines", line=dict(width=0), showlegend=False))
    fig.add_trace(go.Scatter(x=ts, y=mu - sd, mode="lines", line=dict(width=0),
                             fill="tonexty", fillcolor=band_color, name="±σ"))
    fig.add_trace(go.Scatter(x=ts, y=mu, mode="lines+markers",
                             line=dict(color=color), name="mean", **kwargs))
    fig.update_layout(title=title or "Learning Curve", template=template,
                      height=height, width=width,
                      xaxis_title="train size", yaxis_title=metric_name)
    return fig


def nested_cv_score_plot_static(outer_folds, scores, title=None, figsize=(10, 6),
                                color="#4c78a8", metric_name="score",
                                style="default", theme="default", dpi=100,
                                **kwargs) -> MatplotlibAxes:
    """Outer-fold scores from a nested CV."""
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Nested CV Scores",
                             xlabel="outer fold", ylabel=metric_name, figsize=figsize)
        fig.set_dpi(dpi)
        ax.bar(list(outer_folds), _as_array(scores), color=color, **kwargs)
        ax.grid(True, axis="y", alpha=0.3); apply_theme(ax, theme)
    return ax


def nested_cv_score_plot_interactive(outer_folds, scores, title=None, color="#4c78a8",
                                     metric_name="score", template="plotly",
                                     height=600, width=1000, **kwargs) -> PlotlyFigure:
    """Interactive nested-CV score bar."""
    fig = go.Figure([go.Bar(x=list(outer_folds), y=_as_array(scores),
                            marker_color=color, **kwargs)])
    fig.update_layout(title=title or "Nested CV Scores", template=template,
                      height=height, width=width, xaxis_title="outer fold",
                      yaxis_title=metric_name)
    return fig


def cv_residual_distribution_static(fold_labels, residuals_per_fold, title=None,
                                    figsize=(11, 6), color="#4c78a8",
                                    style="default", theme="default", dpi=100,
                                    **kwargs) -> MatplotlibAxes:
    """Boxplot of residuals per CV fold."""
    data = [list(r) for r in residuals_per_fold]
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "CV Residual Distribution",
                             xlabel="fold", ylabel="residual", figsize=figsize)
        fig.set_dpi(dpi)
        bp = ax.boxplot(data, labels=list(fold_labels), patch_artist=True, **kwargs)
        for patch in bp["boxes"]: patch.set_facecolor(color); patch.set_alpha(0.7)
        ax.axhline(0, color="#e45756", linestyle="--")
        ax.grid(True, alpha=0.3); apply_theme(ax, theme)
    return ax


def cv_residual_distribution_interactive(fold_labels, residuals_per_fold, title=None,
                                         color="#4c78a8", template="plotly",
                                         height=600, width=1100, **kwargs) -> PlotlyFigure:
    """Interactive CV residual boxplots."""
    fig = go.Figure()
    for lbl, r in zip(fold_labels, residuals_per_fold):
        fig.add_trace(go.Box(y=list(r), name=str(lbl), marker_color=color, **kwargs))
    fig.add_hline(y=0, line_dash="dash", line_color="#e45756")
    fig.update_layout(title=title or "CV Residual Distribution", template=template,
                      height=height, width=width, xaxis_title="fold", yaxis_title="residual")
    return fig


def repeated_kfold_violin_static(repeats, scores_per_repeat, title=None,
                                 figsize=(11, 6), color="#4c78a8",
                                 metric_name="score", style="default",
                                 theme="default", dpi=100, **kwargs) -> MatplotlibAxes:
    """Violin plot of scores per repeat in repeated K-fold."""
    data = [list(s) for s in scores_per_repeat]
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Repeated K-Fold Scores",
                             xlabel="repeat", ylabel=metric_name, figsize=figsize)
        fig.set_dpi(dpi)
        vp = ax.violinplot(data, showmeans=True, **kwargs)
        for body in vp["bodies"]: body.set_facecolor(color); body.set_alpha(0.5)
        ax.set_xticks(range(1, len(data) + 1)); ax.set_xticklabels(list(repeats))
        ax.grid(True, alpha=0.3); apply_theme(ax, theme)
    return ax


def repeated_kfold_violin_interactive(repeats, scores_per_repeat, title=None,
                                      color="#4c78a8", metric_name="score",
                                      template="plotly", height=600, width=1100,
                                      **kwargs) -> PlotlyFigure:
    """Interactive repeated K-fold violins."""
    fig = go.Figure()
    for rep, s in zip(repeats, scores_per_repeat):
        fig.add_trace(go.Violin(y=list(s), name=str(rep), line_color=color,
                                box_visible=True, meanline_visible=True, **kwargs))
    fig.update_layout(title=title or "Repeated K-Fold Scores", template=template,
                      height=height, width=width, xaxis_title="repeat",
                      yaxis_title=metric_name)
    return fig


def group_cv_score_strip_static(group_labels, scores, title=None, figsize=(10, 6),
                                color="#4c78a8", metric_name="score",
                                style="default", theme="default", dpi=100,
                                **kwargs) -> MatplotlibAxes:
    """Per-group CV score as a strip plot."""
    g = list(group_labels); s = _as_array(scores)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Group CV Scores",
                             xlabel="group", ylabel=metric_name, figsize=figsize)
        fig.set_dpi(dpi)
        jitter = (np.random.RandomState(0).rand(len(s)) - 0.5) * 0.15
        ax.scatter(np.arange(len(g)) + jitter, s, color=color, alpha=0.8, **kwargs)
        ax.set_xticks(range(len(g))); ax.set_xticklabels(g, rotation=45)
        ax.grid(True, alpha=0.3); apply_theme(ax, theme)
    return ax


def group_cv_score_strip_interactive(group_labels, scores, title=None, color="#4c78a8",
                                     metric_name="score", template="plotly",
                                     height=600, width=1000, **kwargs) -> PlotlyFigure:
    """Interactive group CV strip plot."""
    g = list(group_labels); s = _as_array(scores)
    fig = go.Figure([go.Scatter(x=g, y=s, mode="markers",
                                marker=dict(color=color, size=10), **kwargs)])
    fig.update_layout(title=title or "Group CV Scores", template=template,
                      height=height, width=width, xaxis_title="group",
                      yaxis_title=metric_name)
    return fig


learning_curve_with_band = learning_curve_with_band_static
nested_cv_score_plot = nested_cv_score_plot_static
cv_residual_distribution = cv_residual_distribution_static
repeated_kfold_violin = repeated_kfold_violin_static
group_cv_score_strip = group_cv_score_strip_static
