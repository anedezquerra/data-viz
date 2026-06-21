"""Model comparison XAI: importance matrix, SHAP agreement, Rashomon band."""

from __future__ import annotations

from typing import Optional, Sequence

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from ..types import FigureSize, MatplotlibAxes, PlotlyFigure
from ..utils import setup_plot, apply_theme


def importance_comparison_heatmap_static(
    importance_matrix: pd.DataFrame, title: Optional[str] = None,
    figsize: FigureSize = (10, 8), cmap: str = "viridis",
    annot: bool = True, theme: str = "default",
    dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Feature × model importance heatmap (annotated)."""
    df = importance_matrix
    title = title or "Importance comparison across models"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Model", ylabel="Feature",
                             figsize=figsize)
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
                            ha="center", va="center", fontsize=8,
                            color="white" if df.values[i, j] > 0.5 * vmax else "black")
        fig.colorbar(im, ax=ax, label="Importance")
        apply_theme(ax, theme)
    return ax


def importance_comparison_heatmap_interactive(
    importance_matrix: pd.DataFrame, title: Optional[str] = None,
    figsize: FigureSize = (1000, 800), colorscale: str = "Viridis",
) -> PlotlyFigure:
    """Interactive importance-comparison heatmap."""
    df = importance_matrix
    fig = go.Figure(go.Heatmap(
        z=df.values, x=list(df.columns), y=list(df.index),
        colorscale=colorscale, text=np.round(df.values, 2),
        texttemplate="%{text}", colorbar=dict(title="Importance"),
    ))
    fig.update_layout(title=title or "Importance comparison across models",
                      xaxis_title="Model", yaxis_title="Feature",
                      width=figsize[0], height=figsize[1])
    return fig


def shap_model_agreement_scatter_static(
    shap_a: np.ndarray, shap_b: np.ndarray, model_a: str = "A",
    model_b: str = "B", feature_names: Optional[Sequence[str]] = None,
    title: Optional[str] = None, figsize: FigureSize = (8, 8),
    color: str = "steelblue", theme: str = "default",
    dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Per-instance SHAP agreement scatter with identity line and Pearson r."""
    x = shap_a.ravel()
    y = shap_b.ravel()
    r = float(np.corrcoef(x, y)[0, 1]) if x.size > 1 else float("nan")
    lim = max(np.abs(np.concatenate([x, y])).max(), 1e-12)
    title = title or f"SHAP agreement: {model_a} vs {model_b} (r={r:.3f})"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel=f"SHAP ({model_a})",
                             ylabel=f"SHAP ({model_b})", figsize=figsize)
        fig.set_dpi(dpi)
        ax.scatter(x, y, color=color, alpha=0.4, s=14, edgecolors="none")
        ax.plot([-lim, lim], [-lim, lim], "--", color="black", linewidth=0.8)
        ax.axhline(0, color="gray", linewidth=0.5)
        ax.axvline(0, color="gray", linewidth=0.5)
        ax.set_xlim(-lim, lim)
        ax.set_ylim(-lim, lim)
        apply_theme(ax, theme)
    return ax


def shap_model_agreement_scatter_interactive(
    shap_a: np.ndarray, shap_b: np.ndarray, model_a: str = "A",
    model_b: str = "B", feature_names: Optional[Sequence[str]] = None,
    title: Optional[str] = None, figsize: FigureSize = (800, 800),
    color: str = "steelblue",
) -> PlotlyFigure:
    """Interactive SHAP-agreement scatter."""
    x = shap_a.ravel()
    y = shap_b.ravel()
    r = float(np.corrcoef(x, y)[0, 1]) if x.size > 1 else float("nan")
    lim = max(float(np.abs(np.concatenate([x, y])).max()), 1e-12)
    hover = None
    if feature_names is not None:
        rep = int(np.ceil(x.size / len(feature_names)))
        hover = (list(feature_names) * rep)[: x.size]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode="markers",
                             marker=dict(color=color, size=5, opacity=0.5),
                             text=hover, hoverinfo="x+y+text",
                             name="SHAP"))
    fig.add_trace(go.Scatter(x=[-lim, lim], y=[-lim, lim], mode="lines",
                             line=dict(color="black", dash="dash"),
                             showlegend=False))
    fig.update_layout(title=title or f"SHAP agreement (r={r:.3f})",
                      xaxis_title=f"SHAP ({model_a})",
                      yaxis_title=f"SHAP ({model_b})",
                      width=figsize[0], height=figsize[1])
    return fig


def rashomon_importance_band_static(
    importances_by_model: pd.DataFrame, top_n: Optional[int] = None,
    title: Optional[str] = None, figsize: FigureSize = (10, 7),
    color: str = "steelblue", band_alpha: float = 0.25,
    theme: str = "default", dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Min/median/max importance band across near-optimal (Rashomon) models.

    Rows=features, columns=models. Bars show median; whiskers min→max.
    """
    df = importances_by_model
    med = df.median(axis=1)
    mn = df.min(axis=1)
    mx = df.max(axis=1)
    order = med.sort_values().index
    if top_n:
        order = order[-top_n:]
    title = title or "Rashomon importance band"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Importance",
                             ylabel="Feature", figsize=figsize)
        fig.set_dpi(dpi)
        y = np.arange(len(order))
        ax.barh(y, med.loc[order], color=color, alpha=0.5, label="Median")
        for yi, feat in zip(y, order):
            ax.plot([mn.loc[feat], mx.loc[feat]], [yi, yi],
                    color="black", linewidth=2)
            ax.plot([mn.loc[feat], mx.loc[feat]], [yi, yi], "|",
                    color="black", markersize=10)
        ax.set_yticks(y)
        ax.set_yticklabels(order)
        ax.grid(True, axis="x", alpha=band_alpha)
        ax.legend()
        apply_theme(ax, theme)
    return ax


def rashomon_importance_band_interactive(
    importances_by_model: pd.DataFrame, top_n: Optional[int] = None,
    title: Optional[str] = None, figsize: FigureSize = (1000, 700),
    color: str = "steelblue",
) -> PlotlyFigure:
    """Interactive Rashomon importance band with min/max error bars."""
    df = importances_by_model
    med = df.median(axis=1)
    mn = df.min(axis=1)
    mx = df.max(axis=1)
    order = med.sort_values().index
    if top_n:
        order = order[-top_n:]
    fig = go.Figure(go.Bar(
        x=med.loc[order], y=list(order), orientation="h",
        marker_color=color, opacity=0.6, name="Median",
        error_x=dict(type="data", symmetric=False,
                     array=(mx.loc[order] - med.loc[order]).values,
                     arrayminus=(med.loc[order] - mn.loc[order]).values),
    ))
    fig.update_layout(title=title or "Rashomon importance band",
                      xaxis_title="Importance", yaxis_title="Feature",
                      width=figsize[0], height=figsize[1])
    return fig
