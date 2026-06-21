"""Additional SHAP charts: beeswarm, instance heatmap, stacked force,
main vs interaction, monotonicity, temporal drift."""

from __future__ import annotations

from typing import Optional, Sequence

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from ..types import FigureSize, MatplotlibAxes, PlotlyFigure
from ..utils import setup_plot, apply_theme


def _order_by_mean_abs(shap_values: np.ndarray, features: Sequence[str]):
    mean_abs = np.abs(shap_values).mean(axis=0)
    order = np.argsort(mean_abs)
    return order, [features[i] for i in order]


def shap_beeswarm_plot_static(
    shap_values: np.ndarray, feature_values: np.ndarray,
    feature_names: Sequence[str], top_n: int = 15,
    title: Optional[str] = None, figsize: FigureSize = (10, 7),
    cmap: str = "coolwarm", point_size: int = 14,
    theme: str = "default", dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Density-jittered beeswarm of SHAP values colored by feature value."""
    order, names = _order_by_mean_abs(shap_values, list(feature_names))
    order = order[-top_n:]
    names = names[-top_n:]
    title = title or "SHAP beeswarm"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="SHAP value",
                             ylabel="Feature", figsize=figsize)
        fig.set_dpi(dpi)
        rng = np.random.default_rng(0)
        for row, idx in enumerate(order):
            sv = shap_values[:, idx]
            fv = feature_values[:, idx]
            fv_n = (fv - fv.min()) / (np.ptp(fv) + 1e-12)
            bins = np.linspace(sv.min(), sv.max(), 30)
            counts, _ = np.histogram(sv, bins=bins)
            density = np.interp(sv, (bins[:-1] + bins[1:]) / 2, counts)
            jitter = rng.uniform(-1, 1, size=sv.size) * (density / (counts.max() + 1)) * 0.35
            ax.scatter(sv, np.full_like(sv, row, dtype=float) + jitter,
                       c=fv_n, cmap=cmap, s=point_size, alpha=0.6,
                       edgecolors="none")
        ax.axvline(0, color="black", linewidth=0.6)
        ax.set_yticks(range(len(names)))
        ax.set_yticklabels(names)
        sm = plt.cm.ScalarMappable(cmap=cmap)
        sm.set_array([])
        fig.colorbar(sm, ax=ax, label="Feature value (low → high)")
        apply_theme(ax, theme)
    return ax


def shap_beeswarm_plot_interactive(
    shap_values: np.ndarray, feature_values: np.ndarray,
    feature_names: Sequence[str], top_n: int = 15,
    title: Optional[str] = None, figsize: FigureSize = (1000, 700),
    colorscale: str = "RdBu_r",
) -> PlotlyFigure:
    """Interactive SHAP beeswarm."""
    order, names = _order_by_mean_abs(shap_values, list(feature_names))
    order = order[-top_n:]
    names = names[-top_n:]
    fig = go.Figure()
    rng = np.random.default_rng(0)
    for row, idx in enumerate(order):
        sv = shap_values[:, idx]
        fv = feature_values[:, idx]
        fv_n = (fv - fv.min()) / (np.ptp(fv) + 1e-12)
        jitter = rng.uniform(-0.3, 0.3, size=sv.size)
        fig.add_trace(go.Scatter(
            x=sv, y=np.full_like(sv, row, dtype=float) + jitter,
            mode="markers", name=names[row],
            marker=dict(color=fv_n, colorscale=colorscale, size=6,
                        showscale=bool(row == len(order) - 1),
                        colorbar=dict(title="Feature value")),
            showlegend=False,
        ))
    fig.update_layout(title=title or "SHAP beeswarm",
                      xaxis_title="SHAP value", yaxis_title="Feature",
                      yaxis=dict(tickmode="array", tickvals=list(range(len(names))),
                                 ticktext=names),
                      width=figsize[0], height=figsize[1])
    return fig


def shap_heatmap_instances_static(
    shap_values: np.ndarray, feature_names: Sequence[str],
    top_n_features: int = 20, title: Optional[str] = None,
    figsize: FigureSize = (12, 7), cmap: str = "RdBu_r",
    theme: str = "default", dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Per-instance SHAP matrix sorted by similarity (nearest neighbor)."""
    order, names = _order_by_mean_abs(shap_values, list(feature_names))
    order = order[-top_n_features:]
    names = names[-top_n_features:]
    sv = shap_values[:, order]
    n = sv.shape[0]
    if n > 1:
        d = np.linalg.norm(sv[:, None, :] - sv[None, :, :], axis=-1)
        np.fill_diagonal(d, np.inf)
        seq = [0]
        rem = set(range(1, n))
        while rem:
            last = seq[-1]
            nxt = min(rem, key=lambda j: d[last, j])
            seq.append(nxt)
            rem.remove(nxt)
    else:
        seq = [0]
    sv_o = sv[seq].T
    vmax = np.abs(sv_o).max() or 1.0
    title = title or "SHAP per-instance heatmap"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Instance (sorted)",
                             ylabel="Feature", figsize=figsize)
        fig.set_dpi(dpi)
        im = ax.imshow(sv_o, cmap=cmap, aspect="auto", vmin=-vmax, vmax=vmax)
        ax.set_yticks(range(len(names)))
        ax.set_yticklabels(names)
        fig.colorbar(im, ax=ax, label="SHAP value")
        apply_theme(ax, theme)
    return ax


def shap_heatmap_instances_interactive(
    shap_values: np.ndarray, feature_names: Sequence[str],
    top_n_features: int = 20, title: Optional[str] = None,
    figsize: FigureSize = (1100, 700), colorscale: str = "RdBu",
) -> PlotlyFigure:
    """Interactive SHAP instance heatmap."""
    order, names = _order_by_mean_abs(shap_values, list(feature_names))
    order = order[-top_n_features:]
    names = names[-top_n_features:]
    sv = shap_values[:, order]
    vmax = float(np.abs(sv).max() or 1.0)
    fig = go.Figure(go.Heatmap(z=sv.T, y=names, colorscale=colorscale,
                               zmin=-vmax, zmax=vmax,
                               colorbar=dict(title="SHAP")))
    fig.update_layout(title=title or "SHAP per-instance heatmap",
                      xaxis_title="Instance", yaxis_title="Feature",
                      width=figsize[0], height=figsize[1])
    return fig


def shap_force_stacked_static(
    shap_values: np.ndarray, base_value: float,
    feature_names: Sequence[str], top_n: int = 8,
    title: Optional[str] = None, figsize: FigureSize = (12, 6),
    cmap: str = "tab10", theme: str = "default",
    dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Stacked force plot across many instances (cumulative contribution)."""
    mean_abs = np.abs(shap_values).mean(axis=0)
    order = np.argsort(mean_abs)[-top_n:]
    sv = shap_values[:, order]
    names = [feature_names[i] for i in order]
    n_inst = sv.shape[0]
    x = np.arange(n_inst)
    pos = np.clip(sv, 0, None)
    neg = np.clip(sv, None, 0)
    title = title or "Stacked SHAP forces"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Instance",
                             ylabel="Contribution", figsize=figsize)
        fig.set_dpi(dpi)
        colors = plt.get_cmap(cmap)(np.linspace(0, 1, len(names)))
        bottom_p = np.full(n_inst, base_value, dtype=float)
        bottom_n = np.full(n_inst, base_value, dtype=float)
        for k, name in enumerate(names):
            ax.bar(x, pos[:, k], bottom=bottom_p, color=colors[k],
                   width=1.0, label=name)
            bottom_p += pos[:, k]
            ax.bar(x, neg[:, k], bottom=bottom_n, color=colors[k],
                   width=1.0, alpha=0.6)
            bottom_n += neg[:, k]
        ax.axhline(base_value, color="black", linewidth=0.8,
                   label="Base value")
        ax.legend(loc="upper right", fontsize=8, ncol=2)
        apply_theme(ax, theme)
    return ax


def shap_force_stacked_interactive(
    shap_values: np.ndarray, base_value: float,
    feature_names: Sequence[str], top_n: int = 8,
    title: Optional[str] = None, figsize: FigureSize = (1100, 600),
) -> PlotlyFigure:
    """Interactive stacked SHAP force plot."""
    mean_abs = np.abs(shap_values).mean(axis=0)
    order = np.argsort(mean_abs)[-top_n:]
    sv = shap_values[:, order]
    names = [feature_names[i] for i in order]
    n_inst = sv.shape[0]
    x = list(range(n_inst))
    fig = go.Figure()
    for k, name in enumerate(names):
        fig.add_trace(go.Bar(x=x, y=sv[:, k], name=name))
    fig.add_hline(y=base_value, line=dict(color="black"),
                  annotation_text="base")
    fig.update_layout(barmode="relative", title=title or "Stacked SHAP forces",
                      xaxis_title="Instance", yaxis_title="Contribution",
                      width=figsize[0], height=figsize[1])
    return fig


def shap_main_vs_interaction_bar_static(
    main_effects: np.ndarray, interaction_effects: np.ndarray,
    feature_names: Sequence[str], top_n: Optional[int] = None,
    title: Optional[str] = None, figsize: FigureSize = (10, 6),
    color_main: str = "steelblue", color_inter: str = "indianred",
    theme: str = "default", dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Stacked bar of mean|main| vs mean|interaction| per feature."""
    main = np.abs(main_effects).mean(axis=0)
    inter = np.abs(interaction_effects).mean(axis=0)
    total = main + inter
    order = np.argsort(total)
    if top_n:
        order = order[-top_n:]
    names = [feature_names[i] for i in order]
    m = main[order]
    n = inter[order]
    title = title or "SHAP main vs interaction"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="mean |contribution|",
                             ylabel="Feature", figsize=figsize)
        fig.set_dpi(dpi)
        ax.barh(names, m, color=color_main, label="Main")
        ax.barh(names, n, left=m, color=color_inter, label="Interaction")
        ax.legend()
        apply_theme(ax, theme)
    return ax


def shap_main_vs_interaction_bar_interactive(
    main_effects: np.ndarray, interaction_effects: np.ndarray,
    feature_names: Sequence[str], top_n: Optional[int] = None,
    title: Optional[str] = None, figsize: FigureSize = (1000, 600),
    color_main: str = "steelblue", color_inter: str = "indianred",
) -> PlotlyFigure:
    """Interactive main vs interaction stacked bar."""
    main = np.abs(main_effects).mean(axis=0)
    inter = np.abs(interaction_effects).mean(axis=0)
    total = main + inter
    order = np.argsort(total)
    if top_n:
        order = order[-top_n:]
    names = [feature_names[i] for i in order]
    fig = go.Figure()
    fig.add_trace(go.Bar(y=names, x=main[order], orientation="h",
                         name="Main", marker_color=color_main))
    fig.add_trace(go.Bar(y=names, x=inter[order], orientation="h",
                         name="Interaction", marker_color=color_inter))
    fig.update_layout(barmode="stack",
                      title=title or "SHAP main vs interaction",
                      xaxis_title="mean |contribution|", yaxis_title="Feature",
                      width=figsize[0], height=figsize[1])
    return fig


def shap_monotonicity_plot_static(
    feature_values: np.ndarray, shap_values: np.ndarray,
    feature_name: str, title: Optional[str] = None,
    figsize: FigureSize = (10, 6), color: str = "steelblue",
    line_color: str = "darkorange", theme: str = "default",
    dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """SHAP vs feature value with monotonic isotonic overlay (pool-adjacent)."""
    order = np.argsort(feature_values)
    x = feature_values[order]
    y = shap_values[order]
    iso = _isotonic(y)
    title = title or f"SHAP monotonicity — {feature_name}"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel=feature_name,
                             ylabel="SHAP value", figsize=figsize)
        fig.set_dpi(dpi)
        ax.scatter(x, y, color=color, alpha=0.4, s=14)
        ax.plot(x, iso, color=line_color, linewidth=2.0,
                label="Isotonic (non-decreasing)")
        ax.axhline(0, color="black", linewidth=0.6)
        ax.legend()
        apply_theme(ax, theme)
    return ax


def shap_monotonicity_plot_interactive(
    feature_values: np.ndarray, shap_values: np.ndarray,
    feature_name: str, title: Optional[str] = None,
    figsize: FigureSize = (1000, 600), color: str = "steelblue",
    line_color: str = "darkorange",
) -> PlotlyFigure:
    """Interactive SHAP monotonicity plot."""
    order = np.argsort(feature_values)
    x = feature_values[order]
    y = shap_values[order]
    iso = _isotonic(y)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode="markers",
                             marker=dict(color=color, opacity=0.5),
                             name="SHAP"))
    fig.add_trace(go.Scatter(x=x, y=iso, mode="lines",
                             line=dict(color=line_color, width=3),
                             name="Isotonic"))
    fig.update_layout(title=title or f"SHAP monotonicity — {feature_name}",
                      xaxis_title=feature_name, yaxis_title="SHAP value",
                      width=figsize[0], height=figsize[1])
    return fig


def _isotonic(y: np.ndarray) -> np.ndarray:
    """Pool-adjacent-violators for non-decreasing fit (stack-based, no sklearn)."""
    y = y.astype(float)
    n = y.size
    vals = []
    weights = []
    starts = []
    for i in range(n):
        vals.append(float(y[i]))
        weights.append(1.0)
        starts.append(i)
        while len(vals) >= 2 and vals[-2] > vals[-1]:
            v2 = vals.pop()
            w2 = weights.pop()
            s2 = starts.pop()
            v1 = vals.pop()
            w1 = weights.pop()
            s1 = starts.pop()
            w = w1 + w2
            vals.append((v1 * w1 + v2 * w2) / w)
            weights.append(w)
            starts.append(s1)
    out = np.empty(n, dtype=float)
    starts.append(n)
    for k, v in enumerate(vals):
        out[starts[k]:starts[k + 1]] = v
    return out


def shap_temporal_drift_static(
    timestamps: pd.Series, shap_values: np.ndarray,
    feature_names: Sequence[str], freq: str = "W",
    top_n: int = 5, title: Optional[str] = None,
    figsize: FigureSize = (12, 6), cmap: str = "tab10",
    theme: str = "default", dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Mean absolute SHAP per feature over time windows."""
    df = pd.DataFrame(np.abs(shap_values), columns=list(feature_names))
    df["__ts__"] = pd.to_datetime(timestamps).values
    agg = df.groupby(pd.Grouper(key="__ts__", freq=freq)).mean()
    means = agg.mean(axis=0).sort_values(ascending=False)
    cols = means.index[:top_n]
    title = title or "SHAP temporal drift"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Time",
                             ylabel="mean |SHAP|", figsize=figsize)
        fig.set_dpi(dpi)
        colors = plt.get_cmap(cmap)(np.linspace(0, 1, len(cols)))
        for c, col in zip(colors, cols):
            ax.plot(agg.index, agg[col], label=col, color=c, marker="o")
        ax.legend()
        ax.grid(True, alpha=0.3)
        apply_theme(ax, theme)
    return ax


def shap_temporal_drift_interactive(
    timestamps: pd.Series, shap_values: np.ndarray,
    feature_names: Sequence[str], freq: str = "W",
    top_n: int = 5, title: Optional[str] = None,
    figsize: FigureSize = (1100, 600),
) -> PlotlyFigure:
    """Interactive SHAP temporal drift."""
    df = pd.DataFrame(np.abs(shap_values), columns=list(feature_names))
    df["__ts__"] = pd.to_datetime(timestamps).values
    agg = df.groupby(pd.Grouper(key="__ts__", freq=freq)).mean()
    means = agg.mean(axis=0).sort_values(ascending=False)
    cols = means.index[:top_n]
    fig = go.Figure()
    for col in cols:
        fig.add_trace(go.Scatter(x=agg.index, y=agg[col], mode="lines+markers",
                                 name=col))
    fig.update_layout(title=title or "SHAP temporal drift",
                      xaxis_title="Time", yaxis_title="mean |SHAP|",
                      width=figsize[0], height=figsize[1])
    return fig
