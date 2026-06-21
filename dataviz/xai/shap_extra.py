"""Extended SHAP-style global and per-feature charts."""

from __future__ import annotations

from typing import Optional, Sequence

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from ..types import ArrayLike, FigureSize, MatplotlibAxes, MatrixLike, PlotlyFigure
from ..utils import setup_plot, apply_theme


def _mean_abs_shap(shap_values: np.ndarray) -> np.ndarray:
    return np.abs(shap_values).mean(axis=0)


def shap_summary_dot_static(
    shap_values: MatrixLike, feature_values: MatrixLike,
    feature_names: Sequence[str], top_n: Optional[int] = None,
    title: Optional[str] = None, figsize: FigureSize = (10, 7),
    cmap: str = "coolwarm", point_size: int = 18,
    grid: bool = True, grid_alpha: float = 0.25, theme: str = "default",
    dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Bee-swarm SHAP summary: y = feature, x = SHAP value, color = feature value."""
    S = np.asarray(shap_values, dtype=float)
    X = np.asarray(feature_values, dtype=float)
    order = np.argsort(_mean_abs_shap(S))
    if top_n:
        order = order[-top_n:]
    names = [feature_names[i] for i in order]
    title = title or "SHAP summary (bee-swarm)"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="SHAP value",
                             ylabel="Feature", figsize=figsize)
        fig.set_dpi(dpi)
        for row, idx in enumerate(order):
            s = S[:, idx]; v = X[:, idx]
            vmin, vmax = float(v.min()), float(v.max())
            denom = (vmax - vmin) or 1.0
            norm = (v - vmin) / denom
            jitter = (np.random.default_rng(idx).random(s.size) - 0.5) * 0.35
            ax.scatter(s, np.full_like(s, row, dtype=float) + jitter,
                       c=norm, cmap=cmap, s=point_size, alpha=0.7,
                       edgecolor="none", vmin=0, vmax=1)
        ax.set_yticks(range(len(names)))
        ax.set_yticklabels(names)
        ax.axvline(0, color="black", linewidth=0.7)
        if grid:
            ax.grid(True, axis="x", alpha=grid_alpha)
        sm = plt.cm.ScalarMappable(cmap=cmap,
                                   norm=plt.Normalize(vmin=0, vmax=1))
        sm.set_array([])
        cb = fig.colorbar(sm, ax=ax, fraction=0.03, pad=0.02)
        cb.set_label("Feature value (low → high)")
        apply_theme(ax, theme)
    return ax


def shap_summary_dot_interactive(
    shap_values: MatrixLike, feature_values: MatrixLike,
    feature_names: Sequence[str], top_n: Optional[int] = None,
    title: Optional[str] = None, height: int = 700, width: int = 900,
    template: str = "plotly", colorscale: str = "RdBu_r",
) -> PlotlyFigure:
    S = np.asarray(shap_values, dtype=float)
    X = np.asarray(feature_values, dtype=float)
    order = np.argsort(_mean_abs_shap(S))
    if top_n:
        order = order[-top_n:]
    names = [feature_names[i] for i in order]
    fig = go.Figure()
    for row, idx in enumerate(order):
        s = S[:, idx]; v = X[:, idx]
        jitter = (np.random.default_rng(idx).random(s.size) - 0.5) * 0.35
        fig.add_trace(go.Scatter(
            x=s, y=np.full_like(s, row, dtype=float) + jitter,
            mode="markers",
            marker=dict(color=v, colorscale=colorscale, size=6,
                        showscale=bool(row == order[-1]),
                        colorbar=dict(title="feature value")),
            name=names[row], showlegend=False,
            hovertemplate=f"{names[row]}: %{{x:.3f}} (val=%{{marker.color:.3f}})"))
    fig.add_vline(x=0, line_color="black", line_width=1)
    fig.update_layout(title=title or "SHAP summary (bee-swarm)",
                      xaxis_title="SHAP value",
                      yaxis=dict(tickmode="array",
                                 tickvals=list(range(len(names))),
                                 ticktext=names, title="Feature"),
                      template=template, height=height, width=width)
    return fig


def shap_bar_global_static(
    shap_values: MatrixLike, feature_names: Sequence[str],
    top_n: Optional[int] = None, title: Optional[str] = None,
    figsize: FigureSize = (10, 6), color: str = "steelblue",
    grid: bool = True, grid_alpha: float = 0.3, theme: str = "default",
    dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    r"""Mean absolute SHAP per feature as a ranked horizontal bar chart."""
    S = np.asarray(shap_values, dtype=float)
    mabs = _mean_abs_shap(S)
    order = np.argsort(mabs)
    if top_n:
        order = order[-top_n:]
    names = [feature_names[i] for i in order]
    vals = mabs[order]
    title = title or "Global SHAP importance (mean |SHAP|)"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="mean(|SHAP|)",
                             ylabel="Feature", figsize=figsize)
        fig.set_dpi(dpi)
        ax.barh(names, vals, color=color, alpha=0.85, edgecolor="black")
        if grid:
            ax.grid(True, axis="x", alpha=grid_alpha)
        apply_theme(ax, theme)
    return ax


def shap_bar_global_interactive(
    shap_values: MatrixLike, feature_names: Sequence[str],
    top_n: Optional[int] = None, title: Optional[str] = None,
    height: int = 600, width: int = 800, template: str = "plotly",
) -> PlotlyFigure:
    S = np.asarray(shap_values, dtype=float)
    mabs = _mean_abs_shap(S)
    order = np.argsort(mabs)
    if top_n:
        order = order[-top_n:]
    fig = go.Figure(go.Bar(x=mabs[order], y=[feature_names[i] for i in order],
                           orientation="h", marker_color="steelblue"))
    fig.update_layout(title=title or "Global SHAP importance (mean |SHAP|)",
                      xaxis_title="mean(|SHAP|)", yaxis_title="Feature",
                      template=template, height=height, width=width)
    return fig


def shap_violin_static(
    shap_values: MatrixLike, feature_names: Sequence[str],
    top_n: Optional[int] = None, title: Optional[str] = None,
    figsize: FigureSize = (10, 7), grid: bool = True, grid_alpha: float = 0.25,
    theme: str = "default", dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Per-feature SHAP-value distribution as horizontal violins."""
    S = np.asarray(shap_values, dtype=float)
    order = np.argsort(_mean_abs_shap(S))
    if top_n:
        order = order[-top_n:]
    names = [feature_names[i] for i in order]
    data = [S[:, i] for i in order]
    title = title or "SHAP value distribution per feature"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="SHAP value",
                             ylabel="Feature", figsize=figsize)
        fig.set_dpi(dpi)
        parts = ax.violinplot(data, vert=False, showmedians=True,
                              positions=range(1, len(names) + 1))
        for pc in parts["bodies"]:
            pc.set_alpha(0.55); pc.set_facecolor("steelblue")
        ax.set_yticks(range(1, len(names) + 1))
        ax.set_yticklabels(names)
        ax.axvline(0, color="black", linewidth=0.7)
        if grid:
            ax.grid(True, axis="x", alpha=grid_alpha)
        apply_theme(ax, theme)
    return ax


def shap_violin_interactive(
    shap_values: MatrixLike, feature_names: Sequence[str],
    top_n: Optional[int] = None, title: Optional[str] = None,
    height: int = 700, width: int = 800, template: str = "plotly",
) -> PlotlyFigure:
    S = np.asarray(shap_values, dtype=float)
    order = np.argsort(_mean_abs_shap(S))
    if top_n:
        order = order[-top_n:]
    fig = go.Figure()
    for i in order:
        fig.add_trace(go.Violin(x=S[:, i], name=feature_names[i],
                                orientation="h", box_visible=True,
                                meanline_visible=True))
    fig.add_vline(x=0, line_color="black", line_width=1)
    fig.update_layout(title=title or "SHAP value distribution per feature",
                      xaxis_title="SHAP value", template=template,
                      height=height, width=width, showlegend=False)
    return fig


def shap_dependence_plot_static(
    shap_values_feature: ArrayLike, feature_values: ArrayLike,
    interaction_values: Optional[ArrayLike] = None,
    feature_name: str = "feature", interaction_name: str = "interaction",
    title: Optional[str] = None, figsize: FigureSize = (10, 6),
    cmap: str = "coolwarm", grid: bool = True, grid_alpha: float = 0.3,
    theme: str = "default", dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """SHAP value vs. feature value (optionally colored by an interaction feature)."""
    s = np.asarray(shap_values_feature, dtype=float)
    x = np.asarray(feature_values, dtype=float)
    title = title or f"SHAP dependence: {feature_name}"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel=feature_name,
                             ylabel=f"SHAP value ({feature_name})",
                             figsize=figsize)
        fig.set_dpi(dpi)
        if interaction_values is not None:
            iv = np.asarray(interaction_values, dtype=float)
            sc = ax.scatter(x, s, c=iv, cmap=cmap, s=18, alpha=0.75,
                            edgecolor="none")
            cb = fig.colorbar(sc, ax=ax, fraction=0.03, pad=0.02)
            cb.set_label(interaction_name)
        else:
            ax.scatter(x, s, s=18, alpha=0.7, color="steelblue",
                       edgecolor="none")
        ax.axhline(0, color="black", linewidth=0.6)
        if grid:
            ax.grid(True, alpha=grid_alpha)
        apply_theme(ax, theme)
    return ax


def shap_dependence_plot_interactive(
    shap_values_feature: ArrayLike, feature_values: ArrayLike,
    interaction_values: Optional[ArrayLike] = None,
    feature_name: str = "feature", interaction_name: str = "interaction",
    title: Optional[str] = None, height: int = 600, width: int = 800,
    template: str = "plotly", colorscale: str = "RdBu_r",
) -> PlotlyFigure:
    s = np.asarray(shap_values_feature, dtype=float)
    x = np.asarray(feature_values, dtype=float)
    marker = dict(size=6, opacity=0.75)
    if interaction_values is not None:
        marker.update(color=np.asarray(interaction_values, dtype=float),
                      colorscale=colorscale, showscale=True,
                      colorbar=dict(title=interaction_name))
    fig = go.Figure(go.Scatter(x=x, y=s, mode="markers", marker=marker))
    fig.add_hline(y=0, line_color="black", line_width=1)
    fig.update_layout(title=title or f"SHAP dependence: {feature_name}",
                      xaxis_title=feature_name,
                      yaxis_title=f"SHAP value ({feature_name})",
                      template=template, height=height, width=width)
    return fig


def shap_interaction_heatmap_static(
    interaction_matrix: MatrixLike, feature_names: Sequence[str],
    top_n: Optional[int] = None, title: Optional[str] = None,
    figsize: FigureSize = (9, 8), cmap: str = "viridis",
    annot: bool = True, theme: str = "default", dpi: int = 100,
    style: str = "default",
) -> MatplotlibAxes:
    r"""Heatmap of mean absolute SHAP interaction values between feature pairs."""
    M = np.asarray(interaction_matrix, dtype=float)
    if top_n and top_n < M.shape[0]:
        ranking = np.argsort(M.sum(axis=1))[::-1][:top_n]
        M = M[np.ix_(ranking, ranking)]
        feature_names = [feature_names[i] for i in ranking]
    title = title or "Mean |SHAP interaction|"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="", ylabel="", figsize=figsize)
        fig.set_dpi(dpi)
        im = ax.imshow(M, cmap=cmap, aspect="auto")
        ax.set_xticks(range(len(feature_names)))
        ax.set_xticklabels(feature_names, rotation=45, ha="right")
        ax.set_yticks(range(len(feature_names)))
        ax.set_yticklabels(feature_names)
        if annot:
            for i in range(len(feature_names)):
                for j in range(len(feature_names)):
                    ax.text(j, i, f"{M[i, j]:.2f}", ha="center", va="center",
                            color="white" if M[i, j] > M.max() / 2 else "black",
                            fontsize=7)
        fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
        apply_theme(ax, theme)
    return ax


def shap_interaction_heatmap_interactive(
    interaction_matrix: MatrixLike, feature_names: Sequence[str],
    top_n: Optional[int] = None, title: Optional[str] = None,
    height: int = 700, width: int = 800, template: str = "plotly",
    colorscale: str = "Viridis",
) -> PlotlyFigure:
    M = np.asarray(interaction_matrix, dtype=float)
    if top_n and top_n < M.shape[0]:
        ranking = np.argsort(M.sum(axis=1))[::-1][:top_n]
        M = M[np.ix_(ranking, ranking)]
        feature_names = [feature_names[i] for i in ranking]
    fig = go.Figure(go.Heatmap(z=M, x=list(feature_names), y=list(feature_names),
                               colorscale=colorscale, text=np.round(M, 2),
                               texttemplate="%{text}"))
    fig.update_layout(title=title or "Mean |SHAP interaction|",
                      template=template, height=height, width=width)
    return fig


def shap_waterfall_plot_static(
    shap_values_instance: ArrayLike, feature_names: Sequence[str],
    base_value: float = 0.0, top_n: Optional[int] = None,
    title: Optional[str] = None, figsize: FigureSize = (10, 7),
    grid: bool = True, grid_alpha: float = 0.3, theme: str = "default",
    dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Per-instance waterfall of feature contributions from base value to prediction."""
    s = np.asarray(shap_values_instance, dtype=float)
    order = np.argsort(np.abs(s))[::-1]
    if top_n:
        head = order[:top_n]
        rest = order[top_n:]
        other = float(s[rest].sum()) if rest.size else 0.0
        names = [feature_names[i] for i in head] + (["other"] if rest.size else [])
        vals = list(s[head]) + ([other] if rest.size else [])
    else:
        names = [feature_names[i] for i in order]
        vals = list(s[order])
    # Build waterfall positions
    cum = base_value
    bars = []
    for n, v in zip(names, vals):
        bars.append((n, cum, v))
        cum += v
    final = cum
    title = title or f"SHAP waterfall (f(x) = {final:.3f})"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Contribution",
                             ylabel="Feature", figsize=figsize)
        fig.set_dpi(dpi)
        for i, (n, left, v) in enumerate(reversed(bars)):
            ax.barh(i, v, left=left,
                    color="tab:blue" if v < 0 else "tab:red",
                    alpha=0.85, edgecolor="black")
            ax.text(left + v, i, f" {v:+.3f}", va="center", fontsize=8)
        ax.set_yticks(range(len(bars)))
        ax.set_yticklabels([n for n, _, _ in reversed(bars)])
        ax.axvline(base_value, color="grey", linestyle="--",
                   label=f"base = {base_value:.3f}")
        ax.axvline(final, color="black", linestyle=":",
                   label=f"f(x) = {final:.3f}")
        if grid:
            ax.grid(True, axis="x", alpha=grid_alpha)
        ax.legend()
        apply_theme(ax, theme)
    return ax


def shap_waterfall_plot_interactive(
    shap_values_instance: ArrayLike, feature_names: Sequence[str],
    base_value: float = 0.0, top_n: Optional[int] = None,
    title: Optional[str] = None, height: int = 600, width: int = 900,
    template: str = "plotly",
) -> PlotlyFigure:
    s = np.asarray(shap_values_instance, dtype=float)
    order = np.argsort(np.abs(s))[::-1]
    if top_n:
        head = order[:top_n]; rest = order[top_n:]
        other = float(s[rest].sum()) if rest.size else 0.0
        names = [feature_names[i] for i in head] + (["other"] if rest.size else [])
        vals = list(s[head]) + ([other] if rest.size else [])
    else:
        names = [feature_names[i] for i in order]
        vals = list(s[order])
    measures = ["relative"] * len(vals) + ["total"]
    x = names + ["f(x)"]
    y = vals + [None]
    fig = go.Figure(go.Waterfall(orientation="v", measure=measures, x=x, y=y,
                                 base=base_value,
                                 increasing=dict(marker_color="crimson"),
                                 decreasing=dict(marker_color="steelblue"),
                                 totals=dict(marker_color="black")))
    fig.update_layout(title=title or "SHAP waterfall", template=template,
                      height=height, width=width, showlegend=False)
    return fig
