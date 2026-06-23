"""Multicollinearity diagnostic charts."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from ..types import MatplotlibAxes, PlotlyFigure
from ..utils import setup_plot, apply_theme
from .helpers import _as_array, _as_matrix, variance_inflation_factors


def vif_bar_static(X, feature_names=None, title=None, figsize=(10, 6),
                   color="#4c78a8", threshold=5.0, style="default", theme="default",
                   dpi=100, **kwargs) -> MatplotlibAxes:
    """Variance Inflation Factor per predictor."""
    Xm = _as_matrix(X); vifs = variance_inflation_factors(Xm)
    names = list(feature_names) if feature_names is not None else [f"x{i}" for i in range(Xm.shape[1])]
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "VIF", xlabel="feature",
                             ylabel="VIF", figsize=figsize)
        fig.set_dpi(dpi)
        ax.bar(names, vifs, color=color, **kwargs)
        ax.axhline(threshold, color="#e45756", linestyle="--", label=f"τ={threshold}")
        ax.tick_params(axis="x", rotation=45); ax.legend()
        ax.grid(True, axis="y", alpha=0.3); apply_theme(ax, theme)
    return ax


def vif_bar_interactive(X, feature_names=None, title=None, color="#4c78a8",
                        threshold=5.0, template="plotly", height=600, width=1000,
                        **kwargs) -> PlotlyFigure:
    """Interactive VIF bar."""
    Xm = _as_matrix(X); vifs = variance_inflation_factors(Xm)
    names = list(feature_names) if feature_names is not None else [f"x{i}" for i in range(Xm.shape[1])]
    fig = go.Figure([go.Bar(x=names, y=vifs, marker_color=color, **kwargs)])
    fig.add_hline(y=threshold, line_dash="dash", line_color="#e45756",
                  annotation_text=f"τ={threshold}")
    fig.update_layout(title=title or "VIF", template=template, height=height, width=width,
                      xaxis_title="feature", yaxis_title="VIF")
    return fig


def condition_index_plot_static(X, title=None, figsize=(10, 6), color="#4c78a8",
                                threshold=30.0, style="default", theme="default",
                                dpi=100, **kwargs) -> MatplotlibAxes:
    """Condition indices (κ_k = √(λ_max/λ_k)) of the predictor design."""
    Xm = _as_matrix(X); Xc = Xm - Xm.mean(axis=0)
    s = np.linalg.svd(Xc, compute_uv=False)
    s2 = s ** 2
    ci = np.sqrt(s2.max() / np.where(s2 > 0, s2, 1e-12))
    idx = np.arange(1, len(ci) + 1)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Condition Index", xlabel="component",
                             ylabel="κ", figsize=figsize)
        fig.set_dpi(dpi)
        ax.bar(idx, ci, color=color, **kwargs)
        ax.axhline(threshold, color="#e45756", linestyle="--", label=f"τ={threshold}")
        ax.legend(); ax.grid(True, axis="y", alpha=0.3); apply_theme(ax, theme)
    return ax


def condition_index_plot_interactive(X, title=None, color="#4c78a8", threshold=30.0,
                                     template="plotly", height=600, width=1000,
                                     **kwargs) -> PlotlyFigure:
    """Interactive condition-index bar."""
    Xm = _as_matrix(X); Xc = Xm - Xm.mean(axis=0)
    s = np.linalg.svd(Xc, compute_uv=False); s2 = s ** 2
    ci = np.sqrt(s2.max() / np.where(s2 > 0, s2, 1e-12))
    fig = go.Figure([go.Bar(x=list(range(1, len(ci) + 1)), y=ci,
                            marker_color=color, **kwargs)])
    fig.add_hline(y=threshold, line_dash="dash", line_color="#e45756")
    fig.update_layout(title=title or "Condition Index", template=template,
                      height=height, width=width,
                      xaxis_title="component", yaxis_title="κ")
    return fig


def correlation_heatmap_with_clustering_static(X, feature_names=None, title=None,
                                               figsize=(8, 7), cmap="coolwarm",
                                               style="default", theme="default",
                                               dpi=100, **kwargs) -> MatplotlibAxes:
    """Correlation heatmap with simple hierarchical row/col ordering."""
    Xm = _as_matrix(X)
    corr = np.corrcoef(Xm, rowvar=False)
    # Simple ordering: by mean absolute correlation desc
    score = np.mean(np.abs(corr), axis=1)
    order = np.argsort(-score)
    corr = corr[order][:, order]
    names = list(feature_names) if feature_names is not None else [f"x{i}" for i in range(Xm.shape[1])]
    names = [names[i] for i in order]
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Correlation (clustered)",
                             xlabel="", ylabel="", figsize=figsize)
        fig.set_dpi(dpi)
        im = ax.imshow(corr, cmap=cmap, vmin=-1, vmax=1, **kwargs)
        ax.set_xticks(range(len(names))); ax.set_xticklabels(names, rotation=45, ha="right")
        ax.set_yticks(range(len(names))); ax.set_yticklabels(names)
        fig.colorbar(im, ax=ax, label="ρ"); apply_theme(ax, theme)
    return ax


def correlation_heatmap_with_clustering_interactive(X, feature_names=None, title=None,
                                                    colorscale="RdBu", template="plotly",
                                                    height=700, width=800,
                                                    **kwargs) -> PlotlyFigure:
    """Interactive clustered correlation heatmap."""
    Xm = _as_matrix(X); corr = np.corrcoef(Xm, rowvar=False)
    score = np.mean(np.abs(corr), axis=1); order = np.argsort(-score)
    corr = corr[order][:, order]
    names = list(feature_names) if feature_names is not None else [f"x{i}" for i in range(Xm.shape[1])]
    names = [names[i] for i in order]
    fig = go.Figure([go.Heatmap(z=corr, x=names, y=names, zmin=-1, zmax=1,
                                colorscale=colorscale, colorbar=dict(title="ρ"), **kwargs)])
    fig.update_layout(title=title or "Correlation (clustered)", template=template,
                      height=height, width=width)
    return fig


def eigenvalue_scree_predictors_static(X, title=None, figsize=(10, 6), color="#4c78a8",
                                       style="default", theme="default", dpi=100,
                                       **kwargs) -> MatplotlibAxes:
    """Eigenvalue scree plot of the centred predictor covariance."""
    Xm = _as_matrix(X); Xc = Xm - Xm.mean(axis=0)
    cov = (Xc.T @ Xc) / max(Xc.shape[0] - 1, 1)
    eigs = np.sort(np.linalg.eigvalsh(cov))[::-1]
    idx = np.arange(1, len(eigs) + 1)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Eigenvalue Scree (predictors)",
                             xlabel="component", ylabel="eigenvalue", figsize=figsize)
        fig.set_dpi(dpi)
        ax.plot(idx, eigs, color=color, marker="o", **kwargs)
        ax.grid(True, alpha=0.3); apply_theme(ax, theme)
    return ax


def eigenvalue_scree_predictors_interactive(X, title=None, color="#4c78a8",
                                            template="plotly", height=600, width=1000,
                                            **kwargs) -> PlotlyFigure:
    """Interactive scree plot of predictors."""
    Xm = _as_matrix(X); Xc = Xm - Xm.mean(axis=0)
    cov = (Xc.T @ Xc) / max(Xc.shape[0] - 1, 1)
    eigs = np.sort(np.linalg.eigvalsh(cov))[::-1]
    fig = go.Figure([go.Scatter(x=list(range(1, len(eigs) + 1)), y=eigs,
                                mode="lines+markers", line=dict(color=color), **kwargs)])
    fig.update_layout(title=title or "Eigenvalue Scree (predictors)", template=template,
                      height=height, width=width,
                      xaxis_title="component", yaxis_title="eigenvalue")
    return fig


def tolerance_bar_static(X, feature_names=None, title=None, figsize=(10, 6),
                         color="#4c78a8", threshold=0.2, style="default",
                         theme="default", dpi=100, **kwargs) -> MatplotlibAxes:
    """Tolerance (1/VIF) per predictor."""
    Xm = _as_matrix(X); tol = 1.0 / variance_inflation_factors(Xm)
    names = list(feature_names) if feature_names is not None else [f"x{i}" for i in range(Xm.shape[1])]
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Tolerance", xlabel="feature",
                             ylabel="1/VIF", figsize=figsize)
        fig.set_dpi(dpi)
        ax.bar(names, tol, color=color, **kwargs)
        ax.axhline(threshold, color="#e45756", linestyle="--", label=f"τ={threshold}")
        ax.tick_params(axis="x", rotation=45); ax.legend()
        ax.grid(True, axis="y", alpha=0.3); apply_theme(ax, theme)
    return ax


def tolerance_bar_interactive(X, feature_names=None, title=None, color="#4c78a8",
                              threshold=0.2, template="plotly", height=600, width=1000,
                              **kwargs) -> PlotlyFigure:
    """Interactive tolerance bar."""
    Xm = _as_matrix(X); tol = 1.0 / variance_inflation_factors(Xm)
    names = list(feature_names) if feature_names is not None else [f"x{i}" for i in range(Xm.shape[1])]
    fig = go.Figure([go.Bar(x=names, y=tol, marker_color=color, **kwargs)])
    fig.add_hline(y=threshold, line_dash="dash", line_color="#e45756")
    fig.update_layout(title=title or "Tolerance", template=template, height=height,
                      width=width, xaxis_title="feature", yaxis_title="1/VIF")
    return fig


vif_bar = vif_bar_static
condition_index_plot = condition_index_plot_static
correlation_heatmap_with_clustering = correlation_heatmap_with_clustering_static
eigenvalue_scree_predictors = eigenvalue_scree_predictors_static
tolerance_bar = tolerance_bar_static
