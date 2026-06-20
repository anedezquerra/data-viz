"""2-D decision-boundary visualization for classifiers."""

from __future__ import annotations

from typing import Callable, Optional

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from ..types import ArrayLike, FigureSize, MatplotlibAxes, PlotlyFigure
from ..utils import setup_plot, apply_theme


def _mesh(x: np.ndarray, y: np.ndarray, resolution: int, padding: float):
    pad_x = (x.max() - x.min()) * padding
    pad_y = (y.max() - y.min()) * padding
    xx, yy = np.meshgrid(
        np.linspace(x.min() - pad_x, x.max() + pad_x, resolution),
        np.linspace(y.min() - pad_y, y.max() + pad_y, resolution),
    )
    return xx, yy


def decision_boundary_plot_static(
    x: ArrayLike,
    y: ArrayLike,
    labels: ArrayLike,
    predict_fn: Callable[[np.ndarray], np.ndarray],
    resolution: int = 200,
    padding: float = 0.1,
    title: Optional[str] = None,
    figsize: FigureSize = (8, 7),
    cmap: str = "tab10",
    alpha_region: float = 0.25,
    alpha_points: float = 0.85,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
) -> MatplotlibAxes:
    """Decision-boundary visualization for a 2-D classifier.

    Args:
        x, y: Coordinates of the training points.
        labels: Class label per point.
        predict_fn: Callable ``f(points)`` taking an ``(n, 2)`` array and
            returning class predictions.
    """
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    labels = np.asarray(labels)
    xx, yy = _mesh(x, y, resolution, padding)
    grid = np.column_stack([xx.ravel(), yy.ravel()])
    zz = np.asarray(predict_fn(grid)).reshape(xx.shape)
    classes = np.unique(labels)
    class_to_idx = {c: i for i, c in enumerate(classes)}
    zz_idx = np.vectorize(class_to_idx.get)(zz)
    title = title or "Decision boundary"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="x", ylabel="y", figsize=figsize)
        fig.set_dpi(dpi)
        cmap_obj = plt.get_cmap(cmap, len(classes))
        ax.contourf(xx, yy, zz_idx, levels=len(classes) - 1, cmap=cmap_obj,
                    alpha=alpha_region)
        for i, c in enumerate(classes):
            mask = labels == c
            ax.scatter(x[mask], y[mask], color=cmap_obj(i), edgecolor="black",
                       linewidth=0.4, s=28, alpha=alpha_points, label=str(c))
        ax.legend(loc="best")
        apply_theme(ax, theme)
    return ax


def decision_boundary_plot_interactive(
    x: ArrayLike,
    y: ArrayLike,
    labels: ArrayLike,
    predict_fn: Callable[[np.ndarray], np.ndarray],
    resolution: int = 150,
    padding: float = 0.1,
    title: Optional[str] = None,
    height: int = 650,
    width: int = 750,
    template: str = "plotly",
    colorscale: str = "Viridis",
) -> PlotlyFigure:
    """Interactive 2-D decision-boundary plot."""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    labels = np.asarray(labels)
    xx, yy = _mesh(x, y, resolution, padding)
    grid = np.column_stack([xx.ravel(), yy.ravel()])
    zz = np.asarray(predict_fn(grid)).reshape(xx.shape)
    classes = np.unique(labels)
    class_to_idx = {c: i for i, c in enumerate(classes)}
    zz_idx = np.vectorize(class_to_idx.get)(zz)
    title = title or "Decision boundary"
    fig = go.Figure()
    fig.add_trace(go.Heatmap(x=xx[0], y=yy[:, 0], z=zz_idx,
                             colorscale=colorscale, showscale=False, opacity=0.4))
    for c in classes:
        mask = labels == c
        fig.add_trace(go.Scatter(x=x[mask], y=y[mask], mode="markers",
                                 marker=dict(size=8, line=dict(width=0.5, color="black")),
                                 name=str(c)))
    fig.update_layout(title=title, xaxis_title="x", yaxis_title="y",
                      template=template, height=height, width=width)
    return fig
