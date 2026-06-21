"""Local explanation charts: force plot, decision plot, LIME-style bars."""

from __future__ import annotations

from typing import Optional, Sequence

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from ..types import ArrayLike, FigureSize, MatplotlibAxes, MatrixLike, PlotlyFigure
from ..utils import setup_plot, apply_theme


def shap_force_plot_static(
    shap_values_instance: ArrayLike, feature_names: Sequence[str],
    base_value: float = 0.0, top_n: Optional[int] = None,
    title: Optional[str] = None, figsize: FigureSize = (12, 3),
    theme: str = "default", dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Horizontal force plot: positive (right) and negative (left) pushes from base."""
    s = np.asarray(shap_values_instance, dtype=float)
    order = np.argsort(np.abs(s))[::-1]
    if top_n:
        order = order[:top_n]
    names = [feature_names[i] for i in order]
    vals = s[order]
    final = float(base_value + s.sum())
    pos_vals = [(n, v) for n, v in zip(names, vals) if v > 0]
    neg_vals = [(n, v) for n, v in zip(names, vals) if v < 0]
    title = title or f"SHAP force (base={base_value:.2f}, f(x)={final:.2f})"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Score",
                             ylabel="", figsize=figsize)
        fig.set_dpi(dpi)
        cur = base_value
        for n, v in sorted(pos_vals, key=lambda kv: -kv[1]):
            ax.barh(0, v, left=cur, color="crimson", alpha=0.8,
                    edgecolor="white")
            ax.text(cur + v / 2, 0.3, f"{n}\n{v:+.2f}", ha="center",
                    fontsize=8)
            cur += v
        cur = base_value
        for n, v in sorted(neg_vals, key=lambda kv: kv[1]):
            ax.barh(0, v, left=cur, color="steelblue", alpha=0.8,
                    edgecolor="white")
            ax.text(cur + v / 2, -0.3, f"{n}\n{v:+.2f}", ha="center",
                    fontsize=8)
            cur += v
        ax.axvline(base_value, color="grey", linestyle="--",
                   label=f"base = {base_value:.2f}")
        ax.axvline(final, color="black", linestyle=":",
                   label=f"f(x) = {final:.2f}")
        ax.set_yticks([])
        ax.set_ylim(-1, 1)
        ax.legend(loc="upper right", fontsize=8)
        apply_theme(ax, theme)
    return ax


def shap_force_plot_interactive(
    shap_values_instance: ArrayLike, feature_names: Sequence[str],
    base_value: float = 0.0, top_n: Optional[int] = None,
    title: Optional[str] = None, height: int = 300, width: int = 1000,
    template: str = "plotly",
) -> PlotlyFigure:
    s = np.asarray(shap_values_instance, dtype=float)
    order = np.argsort(np.abs(s))[::-1]
    if top_n:
        order = order[:top_n]
    fig = go.Figure()
    cur_pos = base_value
    for i in order:
        if s[i] > 0:
            fig.add_trace(go.Bar(x=[s[i]], y=[0], base=cur_pos, orientation="h",
                                 marker_color="crimson",
                                 name=feature_names[i],
                                 text=f"{feature_names[i]} {s[i]:+.2f}",
                                 textposition="inside", showlegend=False))
            cur_pos += s[i]
    cur_neg = base_value
    for i in order:
        if s[i] < 0:
            fig.add_trace(go.Bar(x=[s[i]], y=[0], base=cur_neg, orientation="h",
                                 marker_color="steelblue",
                                 name=feature_names[i],
                                 text=f"{feature_names[i]} {s[i]:+.2f}",
                                 textposition="inside", showlegend=False))
            cur_neg += s[i]
    final = float(base_value + s.sum())
    fig.add_vline(x=base_value, line_dash="dash", line_color="grey",
                  annotation_text=f"base={base_value:.2f}")
    fig.add_vline(x=final, line_dash="dot", line_color="black",
                  annotation_text=f"f(x)={final:.2f}")
    fig.update_layout(title=title or "SHAP force", barmode="overlay",
                      template=template, height=height, width=width,
                      yaxis=dict(visible=False))
    return fig


def shap_decision_plot_static(
    shap_values: MatrixLike, feature_names: Sequence[str],
    base_value: float = 0.0, top_n: Optional[int] = None,
    title: Optional[str] = None, figsize: FigureSize = (10, 8),
    cmap: str = "coolwarm", grid: bool = True, grid_alpha: float = 0.3,
    theme: str = "default", dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Decision plot: cumulative SHAP path from base to f(x) for each instance.

    Features are ordered by global ``mean(|SHAP|)``.
    """
    S = np.asarray(shap_values, dtype=float)
    mabs = np.abs(S).mean(axis=0)
    order = np.argsort(mabs)
    if top_n:
        order = order[-top_n:]
    names = [feature_names[i] for i in order]
    n_inst = S.shape[0]
    title = title or "SHAP decision plot"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Model output",
                             ylabel="Feature", figsize=figsize)
        fig.set_dpi(dpi)
        finals = base_value + S.sum(axis=1)
        norm = (finals - finals.min()) / max(finals.max() - finals.min(), 1e-9)
        colormap = plt.colormaps.get_cmap(cmap)
        for k in range(n_inst):
            path = base_value + np.cumsum(S[k, order])
            xs = np.r_[base_value, path]
            ys = np.arange(len(order) + 1)
            ax.plot(xs, ys, color=colormap(norm[k]), alpha=0.45, linewidth=1.0)
        ax.axvline(base_value, color="grey", linestyle="--",
                   label=f"base = {base_value:.3f}")
        ax.set_yticks(range(1, len(names) + 1))
        ax.set_yticklabels(names)
        ax.set_ylim(-0.5, len(names) + 0.5)
        if grid:
            ax.grid(True, axis="x", alpha=grid_alpha)
        ax.legend(loc="lower right")
        apply_theme(ax, theme)
    return ax


def shap_decision_plot_interactive(
    shap_values: MatrixLike, feature_names: Sequence[str],
    base_value: float = 0.0, top_n: Optional[int] = None,
    title: Optional[str] = None, height: int = 700, width: int = 900,
    template: str = "plotly", colorscale: str = "RdBu_r",
) -> PlotlyFigure:
    S = np.asarray(shap_values, dtype=float)
    mabs = np.abs(S).mean(axis=0)
    order = np.argsort(mabs)
    if top_n:
        order = order[-top_n:]
    names = [feature_names[i] for i in order]
    finals = base_value + S.sum(axis=1)
    fig = go.Figure()
    for k in range(S.shape[0]):
        path = base_value + np.cumsum(S[k, order])
        fig.add_trace(go.Scatter(x=np.r_[base_value, path],
                                 y=np.arange(len(order) + 1),
                                 mode="lines",
                                 line=dict(width=1),
                                 marker=dict(color=finals[k],
                                             colorscale=colorscale,
                                             showscale=k == 0,
                                             colorbar=dict(title="f(x)")),
                                 showlegend=False,
                                 hovertemplate=f"f(x)={finals[k]:.3f}"))
    fig.add_vline(x=base_value, line_dash="dash", line_color="grey",
                  annotation_text=f"base={base_value:.3f}")
    fig.update_layout(title=title or "SHAP decision plot",
                      xaxis_title="Model output",
                      yaxis=dict(tickmode="array",
                                 tickvals=list(range(1, len(names) + 1)),
                                 ticktext=names, title="Feature"),
                      template=template, height=height, width=width)
    return fig


def lime_explanation_bar_static(
    contributions: Sequence[tuple], title: Optional[str] = None,
    figsize: FigureSize = (10, 6), grid: bool = True, grid_alpha: float = 0.3,
    theme: str = "default", dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """LIME-style signed bar of per-feature contributions for one instance.

    Args:
        contributions: Sequence of ``(label, value)`` tuples. Positive values
            push the prediction up, negatives push it down.
    """
    items = sorted(contributions, key=lambda kv: abs(kv[1]))
    names = [k for k, _ in items]
    vals = [v for _, v in items]
    title = title or "LIME explanation"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Contribution to prediction",
                             ylabel="Feature condition", figsize=figsize)
        fig.set_dpi(dpi)
        colors = ["tab:red" if v < 0 else "tab:green" for v in vals]
        ax.barh(names, vals, color=colors, alpha=0.85, edgecolor="black")
        ax.axvline(0, color="black", linewidth=0.7)
        if grid:
            ax.grid(True, axis="x", alpha=grid_alpha)
        apply_theme(ax, theme)
    return ax


def lime_explanation_bar_interactive(
    contributions: Sequence[tuple], title: Optional[str] = None,
    height: int = 600, width: int = 800, template: str = "plotly",
) -> PlotlyFigure:
    items = sorted(contributions, key=lambda kv: abs(kv[1]))
    names = [k for k, _ in items]; vals = [v for _, v in items]
    colors = ["red" if v < 0 else "green" for v in vals]
    fig = go.Figure(go.Bar(x=vals, y=names, orientation="h",
                           marker_color=colors))
    fig.add_vline(x=0, line_color="black", line_width=1)
    fig.update_layout(title=title or "LIME explanation",
                      xaxis_title="Contribution to prediction",
                      yaxis_title="Feature condition",
                      template=template, height=height, width=width)
    return fig
