"""Surrogate-model and counterfactual explanation charts."""

from __future__ import annotations

from typing import Mapping, Optional, Sequence

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from ..types import FigureSize, MatplotlibAxes, PlotlyFigure
from ..utils import setup_plot, apply_theme


def surrogate_tree_plot_static(
    rules: Sequence[Mapping], title: Optional[str] = None,
    figsize: FigureSize = (12, 7), node_color: str = "#a6c8ff",
    text_color: str = "black", theme: str = "default", dpi: int = 100,
    style: str = "default",
) -> MatplotlibAxes:
    """Render a shallow surrogate tree from a structured rule list.

    Args:
        rules: Sequence of dicts with keys ``depth`` (int >= 0),
            ``condition`` (str), and optional ``prediction`` (str) for leaves.
            The function lays out nodes top-down by depth.
    """
    rows = list(rules)
    by_depth: dict[int, list[int]] = {}
    for i, r in enumerate(rows):
        by_depth.setdefault(int(r.get("depth", 0)), []).append(i)
    max_depth = max(by_depth)
    title = title or "Surrogate decision tree"
    positions: dict[int, tuple[float, float]] = {}
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="", ylabel="",
                             figsize=figsize)
        fig.set_dpi(dpi)
        for d, idxs in by_depth.items():
            n = len(idxs)
            for j, i in enumerate(idxs):
                x = (j + 1) / (n + 1)
                y = 1 - d / max(max_depth, 1)
                positions[i] = (x, y)
                text = rows[i].get("condition", "")
                if rows[i].get("prediction") is not None:
                    text += f"\n→ {rows[i]['prediction']}"
                ax.add_patch(plt.Rectangle((x - 0.10, y - 0.06), 0.20, 0.12,
                                           facecolor=node_color,
                                           edgecolor="black", linewidth=1))
                ax.text(x, y, text, ha="center", va="center", fontsize=8,
                        color=text_color)
        # Connect nodes by parent index if provided.
        for i, r in enumerate(rows):
            p = r.get("parent")
            if p is not None and p in positions:
                x0, y0 = positions[p]
                x1, y1 = positions[i]
                ax.plot([x0, x1], [y0 - 0.06, y1 + 0.06], color="black",
                        linewidth=1)
        ax.set_xlim(0, 1); ax.set_ylim(-0.1, 1.1)
        ax.set_xticks([]); ax.set_yticks([])
        for sp in ["left", "right", "top", "bottom"]:
            ax.spines[sp].set_visible(False)
        apply_theme(ax, theme)
    return ax


def surrogate_tree_plot_interactive(
    rules: Sequence[Mapping], title: Optional[str] = None,
    height: int = 600, width: int = 1000, template: str = "plotly",
) -> PlotlyFigure:
    rows = list(rules)
    by_depth: dict[int, list[int]] = {}
    for i, r in enumerate(rows):
        by_depth.setdefault(int(r.get("depth", 0)), []).append(i)
    max_depth = max(by_depth)
    positions: dict[int, tuple[float, float]] = {}
    edges_x: list[float] = []; edges_y: list[float] = []
    for d, idxs in by_depth.items():
        n = len(idxs)
        for j, i in enumerate(idxs):
            positions[i] = ((j + 1) / (n + 1),
                             1 - d / max(max_depth, 1))
    for i, r in enumerate(rows):
        p = r.get("parent")
        if p is not None and p in positions:
            x0, y0 = positions[p]; x1, y1 = positions[i]
            edges_x += [x0, x1, None]; edges_y += [y0, y1, None]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=edges_x, y=edges_y, mode="lines",
                             line=dict(color="black"), hoverinfo="skip",
                             showlegend=False))
    xs = [positions[i][0] for i in range(len(rows))]
    ys = [positions[i][1] for i in range(len(rows))]
    texts = []
    for r in rows:
        t = r.get("condition", "")
        if r.get("prediction") is not None:
            t += f"<br>→ {r['prediction']}"
        texts.append(t)
    fig.add_trace(go.Scatter(x=xs, y=ys, mode="markers+text", text=texts,
                             textposition="middle center",
                             marker=dict(size=60, color="#a6c8ff",
                                          line=dict(width=1, color="black")),
                             hoverinfo="text", showlegend=False))
    fig.update_layout(title=title or "Surrogate decision tree",
                      xaxis=dict(visible=False, range=[0, 1]),
                      yaxis=dict(visible=False, range=[-0.1, 1.1]),
                      template=template, height=height, width=width)
    return fig


def counterfactual_change_bar_static(
    original: Mapping[str, float], counterfactual: Mapping[str, float],
    top_n: Optional[int] = None, title: Optional[str] = None,
    figsize: FigureSize = (10, 6), grid: bool = True, grid_alpha: float = 0.3,
    theme: str = "default", dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Per-feature deltas required to flip a prediction (counterfactual recipe)."""
    keys = list(original.keys())
    deltas = {k: counterfactual.get(k, 0.0) - original[k] for k in keys}
    items = sorted(deltas.items(), key=lambda kv: abs(kv[1]))
    if top_n:
        items = items[-top_n:]
    names = [k for k, _ in items]; vals = [v for _, v in items]
    title = title or "Counterfactual feature changes"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Δ feature value",
                             ylabel="Feature", figsize=figsize)
        fig.set_dpi(dpi)
        colors = ["tab:red" if v < 0 else "tab:green" for v in vals]
        ax.barh(names, vals, color=colors, alpha=0.85, edgecolor="black")
        for n, v in zip(names, vals):
            orig = original[n]; cf = counterfactual.get(n, orig)
            ax.text(v, n, f"  {orig:.2f} → {cf:.2f}", va="center", fontsize=8)
        ax.axvline(0, color="black", linewidth=0.7)
        if grid:
            ax.grid(True, axis="x", alpha=grid_alpha)
        apply_theme(ax, theme)
    return ax


def counterfactual_change_bar_interactive(
    original: Mapping[str, float], counterfactual: Mapping[str, float],
    top_n: Optional[int] = None, title: Optional[str] = None,
    height: int = 600, width: int = 900, template: str = "plotly",
) -> PlotlyFigure:
    keys = list(original.keys())
    deltas = {k: counterfactual.get(k, 0.0) - original[k] for k in keys}
    items = sorted(deltas.items(), key=lambda kv: abs(kv[1]))
    if top_n:
        items = items[-top_n:]
    names = [k for k, _ in items]; vals = [v for _, v in items]
    colors = ["red" if v < 0 else "green" for v in vals]
    text = [f"{original[n]:.2f} → {counterfactual.get(n, original[n]):.2f}"
            for n in names]
    fig = go.Figure(go.Bar(x=vals, y=names, orientation="h",
                           marker_color=colors, text=text,
                           textposition="outside"))
    fig.add_vline(x=0, line_color="black", line_width=1)
    fig.update_layout(title=title or "Counterfactual feature changes",
                      xaxis_title="Δ feature value", yaxis_title="Feature",
                      template=template, height=height, width=width)
    return fig
