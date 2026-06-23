"""Variable / feature engineering charts for regression."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from ..types import MatplotlibAxes, PlotlyFigure
from ..utils import setup_plot, apply_theme
from .helpers import _as_array, _as_matrix


def _smooth(x, y, bins=20):
    x = _as_array(x); y = _as_array(y)
    if x.size == 0: return np.array([]), np.array([])
    edges = np.linspace(x.min(), x.max(), bins + 1)
    centers = 0.5 * (edges[1:] + edges[:-1])
    means = np.full(bins, np.nan)
    for i in range(bins):
        mask = (x >= edges[i]) & (x < edges[i + 1])
        if mask.any(): means[i] = float(np.mean(y[mask]))
    valid = ~np.isnan(means)
    return centers[valid], means[valid]


def target_vs_feature_smooth_grid_static(X, y, feature_names=None, bins=20, title=None,
                                         figsize=(12, 8), color="#4c78a8",
                                         style="default", theme="default", dpi=100,
                                         ncols=3, **kwargs) -> MatplotlibAxes:
    """Grid of smoothed E[y|x_j] curves across features."""
    Xm = _as_matrix(X); ya = _as_array(y)
    n_feat = Xm.shape[1]
    names = list(feature_names) if feature_names is not None else [f"x{i}" for i in range(n_feat)]
    nrows = int(np.ceil(n_feat / ncols))
    with plt.style.context(style):
        fig, axes = plt.subplots(nrows, ncols, figsize=figsize, dpi=dpi)
        if title: fig.suptitle(title, fontsize=14)
        axes = np.atleast_2d(axes).ravel()
        for j in range(n_feat):
            cx, cy = _smooth(Xm[:, j], ya, bins=bins)
            axes[j].plot(cx, cy, color=color, marker="o", **kwargs)
            axes[j].set_title(names[j]); axes[j].grid(True, alpha=0.3); apply_theme(axes[j], theme)
        for k in range(n_feat, len(axes)): axes[k].axis("off")
        fig.tight_layout()
    return axes[0]


def target_vs_feature_smooth_grid_interactive(X, y, feature_names=None, bins=20,
                                              title=None, color="#4c78a8",
                                              template="plotly", height=800, width=1200,
                                              ncols=3, **kwargs) -> PlotlyFigure:
    """Interactive grid of E[y|x_j] curves."""
    from plotly.subplots import make_subplots
    Xm = _as_matrix(X); ya = _as_array(y); n_feat = Xm.shape[1]
    names = list(feature_names) if feature_names is not None else [f"x{i}" for i in range(n_feat)]
    nrows = int(np.ceil(n_feat / ncols))
    fig = make_subplots(rows=nrows, cols=ncols, subplot_titles=names)
    for j in range(n_feat):
        cx, cy = _smooth(Xm[:, j], ya, bins=bins)
        r, c = j // ncols + 1, j % ncols + 1
        fig.add_trace(go.Scatter(x=cx, y=cy, mode="lines+markers",
                                 line=dict(color=color), showlegend=False, **kwargs),
                      row=r, col=c)
    fig.update_layout(title=title or "Target vs Feature (smoothed)",
                      template=template, height=height, width=width)
    return fig


def feature_target_correlation_bar_static(X, y, feature_names=None, title=None,
                                          figsize=(10, 6), color="#4c78a8",
                                          style="default", theme="default", dpi=100,
                                          **kwargs) -> MatplotlibAxes:
    """Per-feature Pearson correlation with the target, sorted by magnitude."""
    Xm = _as_matrix(X); ya = _as_array(y)
    corr = np.array([np.corrcoef(Xm[:, j], ya)[0, 1] for j in range(Xm.shape[1])])
    names = list(feature_names) if feature_names is not None else [f"x{i}" for i in range(Xm.shape[1])]
    order = np.argsort(-np.abs(corr))
    corr_s = corr[order]; names_s = [names[i] for i in order]
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Feature–Target Correlation",
                             xlabel="feature", ylabel="ρ", figsize=figsize)
        fig.set_dpi(dpi)
        ax.bar(names_s, corr_s, color=color, **kwargs)
        ax.axhline(0, color="#888", linestyle="--")
        ax.tick_params(axis="x", rotation=45); ax.grid(True, axis="y", alpha=0.3)
        apply_theme(ax, theme)
    return ax


def feature_target_correlation_bar_interactive(X, y, feature_names=None, title=None,
                                               color="#4c78a8", template="plotly",
                                               height=600, width=1100,
                                               **kwargs) -> PlotlyFigure:
    """Interactive feature/target correlation bar."""
    Xm = _as_matrix(X); ya = _as_array(y)
    corr = np.array([np.corrcoef(Xm[:, j], ya)[0, 1] for j in range(Xm.shape[1])])
    names = list(feature_names) if feature_names is not None else [f"x{i}" for i in range(Xm.shape[1])]
    order = np.argsort(-np.abs(corr))
    corr_s = corr[order]; names_s = [names[i] for i in order]
    fig = go.Figure([go.Bar(x=names_s, y=corr_s, marker_color=color, **kwargs)])
    fig.add_hline(y=0, line_dash="dash", line_color="#888")
    fig.update_layout(title=title or "Feature–Target Correlation", template=template,
                      height=height, width=width, xaxis_title="feature", yaxis_title="ρ")
    return fig


def target_encoding_curve_static(category_means, sample_sizes, prior=None, title=None,
                                 figsize=(10, 6), color="#4c78a8",
                                 line_color="#e45756", style="default",
                                 theme="default", dpi=100, **kwargs) -> MatplotlibAxes:
    """Target-encoded category mean vs sample size with optional prior."""
    cm = _as_array(category_means); n = _as_array(sample_sizes)
    order = np.argsort(n)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Target Encoding (mean vs n)",
                             xlabel="sample size", ylabel="mean target", figsize=figsize)
        fig.set_dpi(dpi)
        ax.scatter(n[order], cm[order], color=color, **kwargs)
        if prior is not None:
            ax.axhline(float(prior), color=line_color, linestyle="--", label=f"prior={prior}")
            ax.legend()
        ax.grid(True, alpha=0.3); apply_theme(ax, theme)
    return ax


def target_encoding_curve_interactive(category_means, sample_sizes, prior=None,
                                      title=None, color="#4c78a8",
                                      line_color="#e45756", template="plotly",
                                      height=600, width=1000, **kwargs) -> PlotlyFigure:
    """Interactive target-encoding curve."""
    cm = _as_array(category_means); n = _as_array(sample_sizes)
    order = np.argsort(n)
    fig = go.Figure([go.Scatter(x=n[order], y=cm[order], mode="markers",
                                marker=dict(color=color), **kwargs)])
    if prior is not None:
        fig.add_hline(y=float(prior), line_dash="dash", line_color=line_color,
                      annotation_text=f"prior={prior}")
    fig.update_layout(title=title or "Target Encoding (mean vs n)", template=template,
                      height=height, width=width,
                      xaxis_title="sample size", yaxis_title="mean target")
    return fig


target_vs_feature_smooth_grid = target_vs_feature_smooth_grid_static
feature_target_correlation_bar = feature_target_correlation_bar_static
target_encoding_curve = target_encoding_curve_static
