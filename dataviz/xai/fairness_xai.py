"""Fairness / cohort XAI: disparate impact, subgroup divergence, intersectional importance."""

from __future__ import annotations

from typing import Mapping, Optional, Sequence

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from ..types import FigureSize, MatplotlibAxes, PlotlyFigure
from ..utils import setup_plot, apply_theme


def disparate_impact_by_segment_static(
    segment_metrics: pd.DataFrame, importance_col: str = "importance",
    rate_col: str = "positive_rate", reference_rate: Optional[float] = None,
    title: Optional[str] = None, figsize: FigureSize = (11, 6),
    color_imp: str = "steelblue", color_rate: str = "darkorange",
    theme: str = "default", dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Per-segment importance bar with overlaid positive/outcome rate.

    ``segment_metrics``: index = segment label; columns include
    ``importance_col`` and ``rate_col``.
    """
    df = segment_metrics.sort_values(importance_col)
    title = title or "Disparate impact by segment"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Segment",
                             ylabel="Importance", figsize=figsize)
        fig.set_dpi(dpi)
        x = np.arange(len(df))
        ax.bar(x, df[importance_col], color=color_imp, alpha=0.85,
               label="Importance")
        ax.set_xticks(x)
        ax.set_xticklabels(df.index, rotation=30, ha="right")
        ax2 = ax.twinx()
        ax2.plot(x, df[rate_col], "o-", color=color_rate, label="Rate")
        ax2.set_ylabel("Positive rate")
        if reference_rate is not None:
            ax2.axhline(reference_rate, color="red", linestyle="--",
                        label="Reference")
        h1, l1 = ax.get_legend_handles_labels()
        h2, l2 = ax2.get_legend_handles_labels()
        ax.legend(h1 + h2, l1 + l2, loc="upper left")
        apply_theme(ax, theme)
    return ax


def disparate_impact_by_segment_interactive(
    segment_metrics: pd.DataFrame, importance_col: str = "importance",
    rate_col: str = "positive_rate", reference_rate: Optional[float] = None,
    title: Optional[str] = None, figsize: FigureSize = (1100, 600),
    color_imp: str = "steelblue", color_rate: str = "darkorange",
) -> PlotlyFigure:
    """Interactive disparate impact view."""
    df = segment_metrics.sort_values(importance_col)
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Bar(x=list(df.index), y=df[importance_col],
                         marker_color=color_imp, name="Importance"),
                  secondary_y=False)
    fig.add_trace(go.Scatter(x=list(df.index), y=df[rate_col],
                             mode="lines+markers",
                             marker_color=color_rate, name="Rate"),
                  secondary_y=True)
    if reference_rate is not None:
        fig.add_hline(y=reference_rate, line=dict(color="red", dash="dash"),
                      annotation_text="Reference")
    fig.update_layout(title=title or "Disparate impact by segment",
                      width=figsize[0], height=figsize[1])
    fig.update_yaxes(title_text="Importance", secondary_y=False)
    fig.update_yaxes(title_text="Positive rate", secondary_y=True)
    return fig


def subgroup_shap_divergence_static(
    divergence: Mapping[str, float], metric: str = "KL",
    title: Optional[str] = None, figsize: FigureSize = (10, 6),
    cmap: str = "viridis", theme: str = "default",
    dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Bar of per-feature divergence between subgroup SHAP distributions."""
    items = sorted(divergence.items(), key=lambda kv: kv[1])
    names = [k for k, _ in items]
    vals = [v for _, v in items]
    colors = plt.get_cmap(cmap)(np.linspace(0.2, 0.95, len(vals)))
    title = title or f"Subgroup SHAP divergence ({metric})"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel=f"{metric} divergence",
                             ylabel="Feature", figsize=figsize)
        fig.set_dpi(dpi)
        ax.barh(names, vals, color=colors, edgecolor="black")
        ax.grid(True, axis="x", alpha=0.3)
        apply_theme(ax, theme)
    return ax


def subgroup_shap_divergence_interactive(
    divergence: Mapping[str, float], metric: str = "KL",
    title: Optional[str] = None, figsize: FigureSize = (1000, 600),
    colorscale: str = "Viridis",
) -> PlotlyFigure:
    """Interactive subgroup-divergence bar."""
    items = sorted(divergence.items(), key=lambda kv: kv[1])
    names = [k for k, _ in items]
    vals = [v for _, v in items]
    fig = go.Figure(go.Bar(x=vals, y=names, orientation="h",
                           marker=dict(color=vals, colorscale=colorscale,
                                       showscale=True,
                                       colorbar=dict(title=metric))))
    fig.update_layout(title=title or f"Subgroup SHAP divergence ({metric})",
                      xaxis_title=f"{metric} divergence", yaxis_title="Feature",
                      width=figsize[0], height=figsize[1])
    return fig


def intersectional_importance_heatmap_static(
    importance_cube: pd.DataFrame, title: Optional[str] = None,
    figsize: FigureSize = (10, 8), cmap: str = "viridis",
    annot: bool = True, theme: str = "default",
    dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Importance per feature × intersectional segment.

    ``importance_cube``: index = feature, columns = "group_a|group_b" labels.
    """
    df = importance_cube
    title = title or "Intersectional importance"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Intersection",
                             ylabel="Feature", figsize=figsize)
        fig.set_dpi(dpi)
        im = ax.imshow(df.values, cmap=cmap, aspect="auto")
        ax.set_xticks(range(len(df.columns)))
        ax.set_xticklabels(df.columns, rotation=45, ha="right")
        ax.set_yticks(range(len(df.index)))
        ax.set_yticklabels(df.index)
        if annot:
            vmax = float(df.values.max() or 1.0)
            for i in range(df.shape[0]):
                for j in range(df.shape[1]):
                    ax.text(j, i, f"{df.values[i, j]:.2f}",
                            ha="center", va="center", fontsize=7,
                            color="white" if df.values[i, j] > 0.5 * vmax else "black")
        fig.colorbar(im, ax=ax, label="Importance")
        apply_theme(ax, theme)
    return ax


def intersectional_importance_heatmap_interactive(
    importance_cube: pd.DataFrame, title: Optional[str] = None,
    figsize: FigureSize = (1000, 800), colorscale: str = "Viridis",
) -> PlotlyFigure:
    """Interactive intersectional importance heatmap."""
    df = importance_cube
    fig = go.Figure(go.Heatmap(
        z=df.values, x=list(df.columns), y=list(df.index),
        colorscale=colorscale, text=np.round(df.values, 2),
        texttemplate="%{text}", colorbar=dict(title="Importance"),
    ))
    fig.update_layout(title=title or "Intersectional importance",
                      width=figsize[0], height=figsize[1])
    return fig
