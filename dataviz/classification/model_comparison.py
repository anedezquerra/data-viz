"""Model-comparison and monitoring charts: radar, Pareto, CD diagram, drift, PSI."""

from __future__ import annotations

from typing import Mapping, Optional, Sequence

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from ..types import ArrayLike, FigureSize, MatplotlibAxes, PlotlyFigure
from ..utils import setup_plot, apply_theme


def metrics_radar_chart_static(
    metrics: Mapping[str, Mapping[str, float]], title: Optional[str] = None,
    figsize: FigureSize = (8, 8), fill_alpha: float = 0.15,
    linewidth: float = 2.0, theme: str = "default", dpi: int = 100,
    style: str = "default",
) -> MatplotlibAxes:
    """Radar / spider chart of several models across the same metric set.

    Args:
        metrics: ``{model_name: {metric_name: value, ...}, ...}`` with all
            inner dicts sharing the same keys.
    """
    model_names = list(metrics.keys())
    if not model_names:
        raise ValueError("metrics is empty")
    metric_names = list(next(iter(metrics.values())).keys())
    n = len(metric_names)
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False).tolist()
    angles += angles[:1]
    title = title or "Model comparison (radar)"
    with plt.style.context(style):
        fig = plt.figure(figsize=figsize, dpi=dpi)
        ax = fig.add_subplot(111, polar=True)
        for name in model_names:
            vals = [metrics[name][m] for m in metric_names]
            vals += vals[:1]
            ax.plot(angles, vals, linewidth=linewidth, label=name)
            ax.fill(angles, vals, alpha=fill_alpha)
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(metric_names)
        ax.set_ylim(0, 1)
        ax.set_title(title)
        ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1), fontsize=9)
    return ax


def metrics_radar_chart_interactive(
    metrics: Mapping[str, Mapping[str, float]], title: Optional[str] = None,
    height: int = 600, width: int = 700, template: str = "plotly",
    fill: str = "toself",
) -> PlotlyFigure:
    """Interactive radar chart of multiple models."""
    metric_names = list(next(iter(metrics.values())).keys())
    fig = go.Figure()
    for name, ms in metrics.items():
        fig.add_trace(go.Scatterpolar(
            r=[ms[m] for m in metric_names] + [ms[metric_names[0]]],
            theta=metric_names + [metric_names[0]],
            fill=fill, name=name))
    fig.update_layout(title=title or "Model comparison (radar)",
                      polar=dict(radialaxis=dict(range=[0, 1])),
                      template=template, height=height, width=width)
    return fig


def pareto_tradeoff_bubble_static(
    models: Mapping[str, Mapping[str, float]],
    x_metric: str = "precision", y_metric: str = "recall",
    size_metric: str = "auc", title: Optional[str] = None,
    figsize: FigureSize = (9, 6), grid: bool = True, grid_alpha: float = 0.3,
    theme: str = "default", dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Bubble plot of model trade-offs with the Pareto frontier highlighted."""
    names = list(models.keys())
    xs = np.array([models[n][x_metric] for n in names])
    ys = np.array([models[n][y_metric] for n in names])
    sizes = np.array([models[n][size_metric] for n in names])
    # Pareto front (maximize both x and y)
    order = np.argsort(-xs)
    pareto = []
    best_y = -np.inf
    for i in order:
        if ys[i] > best_y:
            pareto.append(i); best_y = ys[i]
    pareto = sorted(pareto, key=lambda k: xs[k])
    title = title or f"Pareto trade-off ({x_metric} vs {y_metric})"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel=x_metric, ylabel=y_metric,
                             figsize=figsize)
        fig.set_dpi(dpi)
        ax.scatter(xs, ys, s=80 + 600 * (sizes - sizes.min())
                           / (sizes.max() - sizes.min() + 1e-9),
                   alpha=0.6, edgecolor="black")
        for x, y, n in zip(xs, ys, names):
            ax.text(x, y, " " + n, fontsize=9, va="center")
        if len(pareto) > 1:
            ax.plot(xs[pareto], ys[pareto], "--", color="red",
                    label="Pareto frontier")
            ax.legend()
        if grid:
            ax.grid(True, alpha=grid_alpha)
        apply_theme(ax, theme)
    return ax


def pareto_tradeoff_bubble_interactive(
    models: Mapping[str, Mapping[str, float]],
    x_metric: str = "precision", y_metric: str = "recall",
    size_metric: str = "auc", title: Optional[str] = None,
    height: int = 600, width: int = 800, template: str = "plotly",
) -> PlotlyFigure:
    names = list(models.keys())
    xs = [models[n][x_metric] for n in names]
    ys = [models[n][y_metric] for n in names]
    sizes = [models[n][size_metric] for n in names]
    fig = go.Figure(go.Scatter(x=xs, y=ys, mode="markers+text", text=names,
                               textposition="top center",
                               marker=dict(size=[10 + 40 * (s - min(sizes))
                                                  / (max(sizes) - min(sizes) + 1e-9)
                                                 for s in sizes],
                                            opacity=0.7,
                                            line=dict(width=1, color="black"))))
    fig.update_layout(title=title or f"Pareto trade-off ({x_metric} vs {y_metric})",
                      xaxis_title=x_metric, yaxis_title=y_metric,
                      template=template, height=height, width=width)
    return fig


def critical_difference_diagram_static(
    rank_table: Mapping[str, Sequence[float]], cd: Optional[float] = None,
    title: Optional[str] = None, figsize: FigureSize = (10, 4),
    theme: str = "default", dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Critical-difference diagram (Demsar) from per-dataset ranks.

    Args:
        rank_table: ``{model_name: [rank_on_dataset_1, ...]}``. Lower rank = better.
        cd: Optional critical-difference threshold (Nemenyi). When provided,
            models within ``cd`` of each other are joined by a horizontal bar.
    """
    model_names = list(rank_table.keys())
    avg_ranks = {n: float(np.mean(rank_table[n])) for n in model_names}
    order = sorted(model_names, key=lambda n: avg_ranks[n])
    ranks_sorted = [avg_ranks[n] for n in order]
    n_models = len(order)
    title = title or "Critical-difference diagram"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Average rank (lower is better)",
                             ylabel="", figsize=figsize)
        fig.set_dpi(dpi)
        ax.set_xlim(1, n_models)
        ax.set_ylim(-1, 1)
        ax.hlines(0, 1, n_models, color="black", linewidth=1.5)
        for i in range(1, n_models + 1):
            ax.vlines(i, -0.05, 0.05, color="black")
            ax.text(i, -0.15, str(i), ha="center", va="top", fontsize=9)
        for i, n in enumerate(order):
            ax.plot(ranks_sorted[i], 0, "o", markersize=8, color="tab:blue")
            yoff = 0.4 if i % 2 == 0 else 0.7
            ax.annotate(n, (ranks_sorted[i], 0),
                        xytext=(ranks_sorted[i], yoff),
                        arrowprops=dict(arrowstyle="-", color="grey"),
                        ha="center", fontsize=9)
        if cd:
            ax.hlines(-0.6, 1, 1 + cd, color="red", linewidth=2)
            ax.text(1 + cd / 2, -0.7, f"CD={cd:.2f}", ha="center", color="red",
                    fontsize=9)
        ax.set_yticks([])
        for sp in ["left", "right", "top"]:
            ax.spines[sp].set_visible(False)
        apply_theme(ax, theme)
    return ax


def critical_difference_diagram_interactive(
    rank_table: Mapping[str, Sequence[float]], cd: Optional[float] = None,
    title: Optional[str] = None, height: int = 350, width: int = 900,
    template: str = "plotly",
) -> PlotlyFigure:
    """Interactive critical-difference / mean-rank chart."""
    model_names = list(rank_table.keys())
    avg_ranks = {n: float(np.mean(rank_table[n])) for n in model_names}
    order = sorted(model_names, key=lambda n: avg_ranks[n])
    ranks = [avg_ranks[n] for n in order]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=ranks, y=[0] * len(ranks), mode="markers+text",
                             text=order, textposition="top center",
                             marker=dict(size=12)))
    if cd:
        fig.add_shape(type="line", x0=1, x1=1 + cd, y0=-0.5, y1=-0.5,
                      line=dict(color="red", width=3))
        fig.add_annotation(x=1 + cd / 2, y=-0.7, text=f"CD={cd:.2f}",
                           showarrow=False, font=dict(color="red"))
    fig.update_layout(title=title or "Critical-difference diagram",
                      xaxis=dict(title="Average rank (lower is better)",
                                 range=[1, len(order)]),
                      yaxis=dict(visible=False, range=[-1, 1]),
                      template=template, height=height, width=width)
    return fig


def score_distribution_drift_static(
    scores_reference: ArrayLike, scores_current: ArrayLike,
    bins: int = 40, title: Optional[str] = None,
    figsize: FigureSize = (10, 6), grid: bool = True, grid_alpha: float = 0.3,
    theme: str = "default", dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Overlay of score distributions from a reference and a current window."""
    ref = np.asarray(scores_reference, dtype=float)
    cur = np.asarray(scores_current, dtype=float)
    edges = np.linspace(min(ref.min(), cur.min()),
                        max(ref.max(), cur.max()), bins + 1)
    title = title or "Score distribution drift"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Score", ylabel="Density",
                             figsize=figsize)
        fig.set_dpi(dpi)
        ax.hist(ref, bins=edges, density=True, alpha=0.5, color="tab:blue",
                label=f"reference (n={ref.size})")
        ax.hist(cur, bins=edges, density=True, alpha=0.5, color="tab:orange",
                label=f"current (n={cur.size})")
        if grid:
            ax.grid(True, alpha=grid_alpha)
        ax.legend()
        apply_theme(ax, theme)
    return ax


def score_distribution_drift_interactive(
    scores_reference: ArrayLike, scores_current: ArrayLike,
    bins: int = 40, title: Optional[str] = None,
    height: int = 600, width: int = 800, template: str = "plotly",
) -> PlotlyFigure:
    ref = np.asarray(scores_reference, dtype=float)
    cur = np.asarray(scores_current, dtype=float)
    fig = go.Figure()
    fig.add_trace(go.Histogram(x=ref, nbinsx=bins, histnorm="probability density",
                               name="reference", opacity=0.5))
    fig.add_trace(go.Histogram(x=cur, nbinsx=bins, histnorm="probability density",
                               name="current", opacity=0.5))
    fig.update_layout(title=title or "Score distribution drift", barmode="overlay",
                      xaxis_title="Score", yaxis_title="Density",
                      template=template, height=height, width=width)
    return fig


def _psi(reference, current, n_bins):
    ref = np.asarray(reference, dtype=float)
    cur = np.asarray(current, dtype=float)
    edges = np.quantile(ref, np.linspace(0, 1, n_bins + 1))
    edges[0] = -np.inf; edges[-1] = np.inf
    ref_hist, _ = np.histogram(ref, bins=edges)
    cur_hist, _ = np.histogram(cur, bins=edges)
    ref_p = np.clip(ref_hist / max(ref.size, 1), 1e-6, None)
    cur_p = np.clip(cur_hist / max(cur.size, 1), 1e-6, None)
    contributions = (cur_p - ref_p) * np.log(cur_p / ref_p)
    return edges, ref_p, cur_p, contributions, float(contributions.sum())


def psi_bar_static(
    scores_reference: ArrayLike, scores_current: ArrayLike, n_bins: int = 10,
    title: Optional[str] = None, figsize: FigureSize = (10, 6),
    grid: bool = True, grid_alpha: float = 0.3, theme: str = "default",
    dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Population Stability Index per bin and overall PSI.

    PSI < 0.1 = stable, 0.1-0.25 = moderate shift, > 0.25 = major shift.
    """
    edges, ref_p, cur_p, contrib, total = _psi(scores_reference, scores_current, n_bins)
    title = title or f"PSI by bin (total={total:.3f})"
    centers = (edges[:-1] + edges[1:]) / 2
    centers[0] = edges[1]; centers[-1] = edges[-2]
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Bin",
                             ylabel="PSI contribution", figsize=figsize)
        fig.set_dpi(dpi)
        ax.bar(range(n_bins), contrib,
               color=["tab:red" if c > 0 else "tab:blue" for c in contrib])
        ax.set_xticks(range(n_bins))
        ax.set_xticklabels([f"b{i}" for i in range(n_bins)])
        ax.axhline(0, color="black", linewidth=0.6)
        for tier, label in [(0.1, "stable<0.1"), (0.25, "moderate<0.25")]:
            ax.axhline(tier, linestyle=":", color="grey")
        if grid:
            ax.grid(True, axis="y", alpha=grid_alpha)
        apply_theme(ax, theme)
    return ax


def psi_bar_interactive(
    scores_reference: ArrayLike, scores_current: ArrayLike, n_bins: int = 10,
    title: Optional[str] = None, height: int = 500, width: int = 800,
    template: str = "plotly",
) -> PlotlyFigure:
    _, _, _, contrib, total = _psi(scores_reference, scores_current, n_bins)
    fig = go.Figure(go.Bar(x=[f"b{i}" for i in range(n_bins)], y=contrib,
                           marker_color=["red" if c > 0 else "blue" for c in contrib],
                           text=[f"{c:.3f}" for c in contrib],
                           textposition="outside"))
    fig.update_layout(title=title or f"PSI by bin (total={total:.3f})",
                      xaxis_title="Bin", yaxis_title="PSI contribution",
                      template=template, height=height, width=width)
    return fig
