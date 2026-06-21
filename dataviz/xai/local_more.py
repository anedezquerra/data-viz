"""Additional local explanations: anchors, k-NN, prototype/criticism, contrastive."""

from __future__ import annotations

from typing import Mapping, Optional, Sequence

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from ..types import FigureSize, MatplotlibAxes, PlotlyFigure
from ..utils import setup_plot, apply_theme


def anchor_explanation_plot_static(
    rules: Sequence[str], precision: Sequence[float],
    coverage: Sequence[float], title: Optional[str] = None,
    figsize: FigureSize = (10, 6), color_p: str = "steelblue",
    color_c: str = "darkorange", theme: str = "default",
    dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Anchor rules with precision and coverage as grouped bars."""
    y = np.arange(len(rules))
    h = 0.4
    title = title or "Anchor explanation"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Score", ylabel="Rule",
                             figsize=figsize)
        fig.set_dpi(dpi)
        ax.barh(y - h / 2, precision, height=h, color=color_p, label="Precision")
        ax.barh(y + h / 2, coverage, height=h, color=color_c, label="Coverage")
        ax.set_yticks(y)
        ax.set_yticklabels(rules)
        ax.set_xlim(0, 1.0)
        ax.legend()
        apply_theme(ax, theme)
    return ax


def anchor_explanation_plot_interactive(
    rules: Sequence[str], precision: Sequence[float],
    coverage: Sequence[float], title: Optional[str] = None,
    figsize: FigureSize = (1000, 600),
    color_p: str = "steelblue", color_c: str = "darkorange",
) -> PlotlyFigure:
    """Interactive anchor explanation bars."""
    fig = go.Figure()
    fig.add_trace(go.Bar(y=list(rules), x=list(precision), orientation="h",
                         name="Precision", marker_color=color_p))
    fig.add_trace(go.Bar(y=list(rules), x=list(coverage), orientation="h",
                         name="Coverage", marker_color=color_c))
    fig.update_layout(barmode="group",
                      title=title or "Anchor explanation",
                      xaxis_title="Score", yaxis_title="Rule",
                      width=figsize[0], height=figsize[1])
    return fig


def nearest_neighbor_explanation_static(
    query: Mapping[str, float], neighbors: pd.DataFrame,
    target: Optional[Sequence] = None, title: Optional[str] = None,
    figsize: FigureSize = (10, 6), cmap: str = "RdBu_r",
    theme: str = "default", dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """k-NN explanation: query vs neighbor feature heatmap."""
    cols = list(query.keys())
    rows = ["query"] + [f"nbr {i}" for i in range(len(neighbors))]
    mat = np.vstack([
        np.array([query[c] for c in cols]),
        neighbors[cols].to_numpy(),
    ])
    title = title or "k-NN explanation"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Feature", ylabel="",
                             figsize=figsize)
        fig.set_dpi(dpi)
        im = ax.imshow(mat, cmap=cmap, aspect="auto")
        ax.set_xticks(range(len(cols)))
        ax.set_xticklabels(cols, rotation=45, ha="right")
        ax.set_yticks(range(len(rows)))
        ax.set_yticklabels(rows)
        if target is not None:
            for i, t in enumerate(["?"] + list(map(str, target))):
                ax.text(len(cols) - 0.4, i, f"y={t}", va="center", fontsize=8)
        fig.colorbar(im, ax=ax)
        apply_theme(ax, theme)
    return ax


def nearest_neighbor_explanation_interactive(
    query: Mapping[str, float], neighbors: pd.DataFrame,
    target: Optional[Sequence] = None, title: Optional[str] = None,
    figsize: FigureSize = (1000, 600), colorscale: str = "RdBu",
) -> PlotlyFigure:
    """Interactive k-NN explanation heatmap."""
    cols = list(query.keys())
    rows = ["query"] + [f"nbr {i}" for i in range(len(neighbors))]
    mat = np.vstack([
        np.array([query[c] for c in cols]),
        neighbors[cols].to_numpy(),
    ])
    fig = go.Figure(go.Heatmap(z=mat, x=cols, y=rows, colorscale=colorscale))
    if target is not None:
        labels = ["?"] + list(map(str, target))
        for i, t in enumerate(labels):
            fig.add_annotation(x=len(cols) - 0.5, y=i, text=f"y={t}",
                               showarrow=False, xanchor="left")
    fig.update_layout(title=title or "k-NN explanation",
                      width=figsize[0], height=figsize[1])
    return fig


def prototype_criticism_grid_static(
    prototypes: pd.DataFrame, criticisms: pd.DataFrame,
    title: Optional[str] = None, figsize: FigureSize = (12, 6),
    cmap: str = "viridis", theme: str = "default",
    dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Side-by-side heatmap of prototypes (typical) and criticisms (outliers)."""
    cols = list(prototypes.columns)
    n_p = len(prototypes)
    n_c = len(criticisms)
    title = title or "Prototypes vs Criticisms"
    with plt.style.context(style):
        fig, axes = plt.subplots(1, 2, figsize=figsize, dpi=dpi,
                                 gridspec_kw={"width_ratios": [n_p, n_c]})
        for ax, df, label in [(axes[0], prototypes, "Prototypes"),
                               (axes[1], criticisms, "Criticisms")]:
            im = ax.imshow(df.to_numpy().T, cmap=cmap, aspect="auto")
            ax.set_title(label)
            ax.set_yticks(range(len(cols)))
            ax.set_yticklabels(cols)
            ax.set_xticks(range(len(df)))
            ax.set_xticklabels([f"#{i}" for i in range(len(df))])
            fig.colorbar(im, ax=ax)
            apply_theme(ax, theme)
        fig.suptitle(title)
        fig.tight_layout()
    return axes[0]


def prototype_criticism_grid_interactive(
    prototypes: pd.DataFrame, criticisms: pd.DataFrame,
    title: Optional[str] = None, figsize: FigureSize = (1100, 600),
    colorscale: str = "Viridis",
) -> PlotlyFigure:
    """Interactive prototypes/criticisms heatmap pair."""
    cols = list(prototypes.columns)
    fig = make_subplots(rows=1, cols=2, subplot_titles=("Prototypes", "Criticisms"),
                        horizontal_spacing=0.08,
                        column_widths=[max(len(prototypes), 1),
                                       max(len(criticisms), 1)])
    fig.add_trace(go.Heatmap(z=prototypes.to_numpy().T, y=cols,
                             colorscale=colorscale, showscale=False),
                  row=1, col=1)
    fig.add_trace(go.Heatmap(z=criticisms.to_numpy().T, y=cols,
                             colorscale=colorscale, showscale=True),
                  row=1, col=2)
    fig.update_layout(title=title or "Prototypes vs Criticisms",
                      width=figsize[0], height=figsize[1])
    return fig


def contrastive_explanation_bar_static(
    pertinent_positives: Mapping[str, float],
    pertinent_negatives: Mapping[str, float],
    title: Optional[str] = None, figsize: FigureSize = (10, 6),
    color_pp: str = "#2ca02c", color_pn: str = "#d62728",
    theme: str = "default", dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Contrastive explanation: pertinent positives vs negatives diverging bars."""
    feats = sorted(set(pertinent_positives) | set(pertinent_negatives),
                   key=lambda k: (pertinent_positives.get(k, 0)
                                  - pertinent_negatives.get(k, 0)))
    pp = [pertinent_positives.get(k, 0.0) for k in feats]
    pn = [-pertinent_negatives.get(k, 0.0) for k in feats]
    title = title or "Contrastive explanation"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Contribution",
                             ylabel="Feature", figsize=figsize)
        fig.set_dpi(dpi)
        ax.barh(feats, pp, color=color_pp, label="Pertinent positives")
        ax.barh(feats, pn, color=color_pn, label="Pertinent negatives")
        ax.axvline(0, color="black", linewidth=0.7)
        ax.legend()
        apply_theme(ax, theme)
    return ax


def contrastive_explanation_bar_interactive(
    pertinent_positives: Mapping[str, float],
    pertinent_negatives: Mapping[str, float],
    title: Optional[str] = None, figsize: FigureSize = (1000, 600),
    color_pp: str = "#2ca02c", color_pn: str = "#d62728",
) -> PlotlyFigure:
    """Interactive contrastive explanation bars."""
    feats = sorted(set(pertinent_positives) | set(pertinent_negatives),
                   key=lambda k: (pertinent_positives.get(k, 0)
                                  - pertinent_negatives.get(k, 0)))
    pp = [pertinent_positives.get(k, 0.0) for k in feats]
    pn = [-pertinent_negatives.get(k, 0.0) for k in feats]
    fig = go.Figure()
    fig.add_trace(go.Bar(y=feats, x=pp, orientation="h",
                         name="Pertinent positives", marker_color=color_pp))
    fig.add_trace(go.Bar(y=feats, x=pn, orientation="h",
                         name="Pertinent negatives", marker_color=color_pn))
    fig.update_layout(barmode="overlay",
                      title=title or "Contrastive explanation",
                      xaxis_title="Contribution", yaxis_title="Feature",
                      width=figsize[0], height=figsize[1])
    return fig
