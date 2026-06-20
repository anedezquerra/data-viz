"""Predicted-score distribution by true class (box / violin / strip)."""

from __future__ import annotations

from typing import Optional, Sequence

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from ..types import ArrayLike, FigureSize, MatplotlibAxes, PlotlyFigure
from ..utils import setup_plot, apply_theme


def score_distribution_by_class_static(
    y_true: ArrayLike,
    y_score: ArrayLike,
    labels: Optional[Sequence] = None,
    kind: str = "violin",
    title: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
) -> MatplotlibAxes:
    """Distribution of model scores grouped by true class.

    Args:
        kind: ``"violin"``, ``"box"`` or ``"strip"``.
    """
    y_true = np.asarray(y_true)
    y_score = np.asarray(y_score, dtype=float)
    if labels is None:
        labels = sorted(np.unique(y_true).tolist())
    groups = [y_score[y_true == l] for l in labels]
    title = title or "Score distribution by class"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="True class",
                             ylabel="Predicted score", figsize=figsize)
        fig.set_dpi(dpi)
        positions = np.arange(1, len(labels) + 1)
        if kind == "violin":
            parts = ax.violinplot(groups, positions=positions, showmedians=True)
            for pc in parts["bodies"]:
                pc.set_alpha(0.6)
        elif kind == "box":
            ax.boxplot(groups, positions=positions, widths=0.6)
        elif kind == "strip":
            for i, g in enumerate(groups):
                x = positions[i] + (np.random.default_rng(0).random(g.size) - 0.5) * 0.2
                ax.scatter(x, g, alpha=0.5, s=12)
        else:
            raise ValueError("kind must be 'violin', 'box' or 'strip'")
        ax.set_xticks(positions)
        ax.set_xticklabels([str(l) for l in labels])
        if grid:
            ax.grid(True, axis="y", alpha=grid_alpha)
        apply_theme(ax, theme)
    return ax


def score_distribution_by_class_interactive(
    y_true: ArrayLike,
    y_score: ArrayLike,
    labels: Optional[Sequence] = None,
    kind: str = "violin",
    title: Optional[str] = None,
    height: int = 600,
    width: int = 800,
    template: str = "plotly",
) -> PlotlyFigure:
    """Interactive distribution of model scores grouped by true class."""
    y_true = np.asarray(y_true)
    y_score = np.asarray(y_score, dtype=float)
    if labels is None:
        labels = sorted(np.unique(y_true).tolist())
    title = title or "Score distribution by class"
    fig = go.Figure()
    for l in labels:
        scores = y_score[y_true == l]
        if kind == "violin":
            fig.add_trace(go.Violin(y=scores, name=str(l), box_visible=True,
                                    meanline_visible=True))
        elif kind == "box":
            fig.add_trace(go.Box(y=scores, name=str(l)))
        elif kind == "strip":
            fig.add_trace(go.Box(y=scores, name=str(l), boxpoints="all",
                                 jitter=0.5, pointpos=0,
                                 fillcolor="rgba(0,0,0,0)",
                                 line=dict(color="rgba(0,0,0,0)")))
        else:
            raise ValueError("kind must be 'violin', 'box' or 'strip'")
    fig.update_layout(title=title, xaxis_title="True class",
                      yaxis_title="Predicted score", template=template,
                      height=height, width=width, showlegend=False)
    return fig
