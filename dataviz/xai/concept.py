"""Concept / representation explanations: TCAV, saliency, attention, embeddings."""

from __future__ import annotations

from typing import Mapping, Optional, Sequence

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from ..types import FigureSize, MatplotlibAxes, PlotlyFigure
from ..utils import setup_plot, apply_theme


def concept_activation_bar_static(
    scores: Mapping[str, float], p_values: Optional[Mapping[str, float]] = None,
    significance: float = 0.05, title: Optional[str] = None,
    figsize: FigureSize = (10, 6), color_sig: str = "steelblue",
    color_ns: str = "lightgray", theme: str = "default",
    dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """TCAV-style concept-activation scores; non-significant bars greyed."""
    items = sorted(scores.items(), key=lambda kv: kv[1])
    names = [k for k, _ in items]
    vals = [v for _, v in items]
    colors = []
    for name in names:
        if p_values is not None and p_values.get(name, 0) > significance:
            colors.append(color_ns)
        else:
            colors.append(color_sig)
    title = title or "Concept activation (TCAV)"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Score", ylabel="Concept",
                             figsize=figsize)
        fig.set_dpi(dpi)
        ax.barh(names, vals, color=colors, edgecolor="black")
        ax.axvline(0.5, color="black", linestyle="--", alpha=0.6)
        ax.grid(True, axis="x", alpha=0.3)
        apply_theme(ax, theme)
    return ax


def concept_activation_bar_interactive(
    scores: Mapping[str, float], p_values: Optional[Mapping[str, float]] = None,
    significance: float = 0.05, title: Optional[str] = None,
    figsize: FigureSize = (1000, 600), color_sig: str = "steelblue",
    color_ns: str = "lightgray",
) -> PlotlyFigure:
    """Interactive TCAV concept-activation bar."""
    items = sorted(scores.items(), key=lambda kv: kv[1])
    names = [k for k, _ in items]
    vals = [v for _, v in items]
    colors = []
    for name in names:
        if p_values is not None and p_values.get(name, 0) > significance:
            colors.append(color_ns)
        else:
            colors.append(color_sig)
    fig = go.Figure(go.Bar(x=vals, y=names, orientation="h",
                           marker_color=colors))
    fig.add_vline(x=0.5, line=dict(color="black", dash="dash"))
    fig.update_layout(title=title or "Concept activation (TCAV)",
                      xaxis_title="Score", yaxis_title="Concept",
                      width=figsize[0], height=figsize[1])
    return fig


def saliency_overlay_plot_static(
    images: Sequence[np.ndarray], saliencies: Sequence[np.ndarray],
    labels: Optional[Sequence[str]] = None, title: Optional[str] = None,
    figsize: FigureSize = (12, 6), cmap: str = "jet",
    alpha: float = 0.45, theme: str = "default",
    dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Grid of images with saliency/Grad-CAM-style overlays."""
    n = len(images)
    ncols = min(4, n)
    nrows = int(np.ceil(n / ncols))
    title = title or "Saliency overlay"
    with plt.style.context(style):
        fig, axes = plt.subplots(nrows, ncols, figsize=figsize, dpi=dpi,
                                 squeeze=False)
        for i, ax in enumerate(axes.flat):
            if i >= n:
                ax.axis("off")
                continue
            img = images[i]
            sal = saliencies[i]
            ax.imshow(img, cmap="gray" if img.ndim == 2 else None)
            ax.imshow(sal, cmap=cmap, alpha=alpha)
            ax.set_title(labels[i] if labels else f"#{i}", fontsize=9)
            ax.axis("off")
        fig.suptitle(title)
        fig.tight_layout()
    return axes[0, 0]


def saliency_overlay_plot_interactive(
    images: Sequence[np.ndarray], saliencies: Sequence[np.ndarray],
    labels: Optional[Sequence[str]] = None, title: Optional[str] = None,
    figsize: FigureSize = (1100, 600), colorscale: str = "Jet",
) -> PlotlyFigure:
    """Interactive saliency overlay grid (heatmap subplots)."""
    from plotly.subplots import make_subplots
    n = len(images)
    ncols = min(4, n)
    nrows = int(np.ceil(n / ncols))
    titles = list(labels) if labels else [f"#{i}" for i in range(n)]
    fig = make_subplots(rows=nrows, cols=ncols, subplot_titles=titles,
                        horizontal_spacing=0.04, vertical_spacing=0.06)
    for i in range(n):
        r = i // ncols + 1
        c = i % ncols + 1
        sal = saliencies[i]
        fig.add_trace(go.Heatmap(z=sal, colorscale=colorscale,
                                 showscale=(i == n - 1)),
                      row=r, col=c)
        fig.update_xaxes(visible=False, row=r, col=c)
        fig.update_yaxes(visible=False, scaleanchor=None, row=r, col=c)
    fig.update_layout(title=title or "Saliency overlay",
                      width=figsize[0], height=figsize[1])
    return fig


def attention_heatmap_static(
    attention: np.ndarray, tokens_x: Sequence[str],
    tokens_y: Optional[Sequence[str]] = None,
    title: Optional[str] = None, figsize: FigureSize = (10, 8),
    cmap: str = "magma", theme: str = "default",
    dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Token/feature attention-weights heatmap."""
    tokens_y = list(tokens_y) if tokens_y is not None else list(tokens_x)
    title = title or "Attention weights"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Key", ylabel="Query",
                             figsize=figsize)
        fig.set_dpi(dpi)
        im = ax.imshow(attention, cmap=cmap, aspect="auto")
        ax.set_xticks(range(len(tokens_x)))
        ax.set_xticklabels(tokens_x, rotation=45, ha="right")
        ax.set_yticks(range(len(tokens_y)))
        ax.set_yticklabels(tokens_y)
        fig.colorbar(im, ax=ax, label="Attention")
        apply_theme(ax, theme)
    return ax


def attention_heatmap_interactive(
    attention: np.ndarray, tokens_x: Sequence[str],
    tokens_y: Optional[Sequence[str]] = None,
    title: Optional[str] = None, figsize: FigureSize = (1000, 800),
    colorscale: str = "Magma",
) -> PlotlyFigure:
    """Interactive attention heatmap."""
    tokens_y = list(tokens_y) if tokens_y is not None else list(tokens_x)
    fig = go.Figure(go.Heatmap(z=attention, x=list(tokens_x), y=tokens_y,
                               colorscale=colorscale,
                               colorbar=dict(title="Attention")))
    fig.update_layout(title=title or "Attention weights",
                      xaxis_title="Key", yaxis_title="Query",
                      width=figsize[0], height=figsize[1])
    return fig


def embedding_projection_plot_static(
    coords: np.ndarray, labels: Optional[Sequence] = None,
    color_values: Optional[np.ndarray] = None,
    title: Optional[str] = None, figsize: FigureSize = (10, 7),
    cmap_categorical: str = "tab10", cmap_continuous: str = "viridis",
    point_size: int = 20, theme: str = "default",
    dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """2-D embedding scatter colored by class or SHAP/feature value."""
    title = title or "Embedding projection"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Dim 1", ylabel="Dim 2",
                             figsize=figsize)
        fig.set_dpi(dpi)
        if color_values is not None:
            sc = ax.scatter(coords[:, 0], coords[:, 1], c=color_values,
                            cmap=cmap_continuous, s=point_size, alpha=0.8,
                            edgecolors="none")
            fig.colorbar(sc, ax=ax, label="Value")
        elif labels is not None:
            uniq = list(pd.unique(pd.Series(labels)))
            colors = plt.get_cmap(cmap_categorical)(np.linspace(0, 1, len(uniq)))
            for c, u in zip(colors, uniq):
                mask = np.array([lbl == u for lbl in labels])
                ax.scatter(coords[mask, 0], coords[mask, 1], color=c,
                           s=point_size, alpha=0.8, edgecolors="none",
                           label=str(u))
            ax.legend()
        else:
            ax.scatter(coords[:, 0], coords[:, 1], s=point_size, alpha=0.8)
        apply_theme(ax, theme)
    return ax


def embedding_projection_plot_interactive(
    coords: np.ndarray, labels: Optional[Sequence] = None,
    color_values: Optional[np.ndarray] = None,
    hover_text: Optional[Sequence[str]] = None,
    title: Optional[str] = None, figsize: FigureSize = (1000, 700),
    colorscale: str = "Viridis",
) -> PlotlyFigure:
    """Interactive 2-D embedding projection."""
    fig = go.Figure()
    if color_values is not None:
        fig.add_trace(go.Scatter(
            x=coords[:, 0], y=coords[:, 1], mode="markers",
            marker=dict(color=color_values, colorscale=colorscale,
                        showscale=True, size=7),
            text=hover_text, hoverinfo="text" if hover_text else "x+y",
        ))
    elif labels is not None:
        for u in pd.unique(pd.Series(labels)):
            mask = np.array([lbl == u for lbl in labels])
            fig.add_trace(go.Scatter(
                x=coords[mask, 0], y=coords[mask, 1], mode="markers",
                name=str(u), marker=dict(size=7),
            ))
    else:
        fig.add_trace(go.Scatter(x=coords[:, 0], y=coords[:, 1], mode="markers"))
    fig.update_layout(title=title or "Embedding projection",
                      xaxis_title="Dim 1", yaxis_title="Dim 2",
                      width=figsize[0], height=figsize[1])
    return fig
