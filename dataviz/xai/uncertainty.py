"""Uncertainty-aware XAI: predictive variance, attribution to uncertainty, decomposition."""

from __future__ import annotations

from typing import Mapping, Optional, Sequence

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from ..types import FigureSize, MatplotlibAxes, PlotlyFigure
from ..utils import setup_plot, apply_theme


def prediction_uncertainty_plot_static(
    feature_values: np.ndarray, predictions: np.ndarray,
    uncertainty: np.ndarray, feature_name: str,
    title: Optional[str] = None, figsize: FigureSize = (10, 6),
    color: str = "steelblue", band_color: str = "steelblue",
    band_alpha: float = 0.25, theme: str = "default",
    dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Prediction with ± uncertainty band against a single feature."""
    order = np.argsort(feature_values)
    x = feature_values[order]
    y = predictions[order]
    u = uncertainty[order]
    title = title or f"Predictive uncertainty — {feature_name}"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel=feature_name,
                             ylabel="Prediction", figsize=figsize)
        fig.set_dpi(dpi)
        ax.fill_between(x, y - u, y + u, color=band_color, alpha=band_alpha,
                        label="± uncertainty")
        ax.plot(x, y, color=color, linewidth=2.0, label="Mean")
        ax.legend()
        ax.grid(True, alpha=0.3)
        apply_theme(ax, theme)
    return ax


def prediction_uncertainty_plot_interactive(
    feature_values: np.ndarray, predictions: np.ndarray,
    uncertainty: np.ndarray, feature_name: str,
    title: Optional[str] = None, figsize: FigureSize = (1000, 600),
    color: str = "steelblue",
) -> PlotlyFigure:
    """Interactive predictive uncertainty band."""
    order = np.argsort(feature_values)
    x = feature_values[order]
    y = predictions[order]
    u = uncertainty[order]
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=np.concatenate([x, x[::-1]]),
        y=np.concatenate([y + u, (y - u)[::-1]]),
        fill="toself", fillcolor="rgba(70,130,180,0.25)",
        line=dict(color="rgba(0,0,0,0)"), name="± uncertainty",
        hoverinfo="skip",
    ))
    fig.add_trace(go.Scatter(x=x, y=y, mode="lines",
                             line=dict(color=color, width=3), name="Mean"))
    fig.update_layout(title=title or f"Predictive uncertainty — {feature_name}",
                      xaxis_title=feature_name, yaxis_title="Prediction",
                      width=figsize[0], height=figsize[1])
    return fig


def confidence_attribution_bar_static(
    attribution: Mapping[str, float], title: Optional[str] = None,
    figsize: FigureSize = (10, 6), color: str = "indianred",
    theme: str = "default", dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Per-feature contribution to predictive uncertainty (signed bar)."""
    items = sorted(attribution.items(), key=lambda kv: kv[1])
    names = [k for k, _ in items]
    vals = [v for _, v in items]
    colors = ["#2ca02c" if v < 0 else color for v in vals]
    title = title or "Uncertainty attribution"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title,
                             xlabel="Δ uncertainty", ylabel="Feature",
                             figsize=figsize)
        fig.set_dpi(dpi)
        ax.barh(names, vals, color=colors, edgecolor="black")
        ax.axvline(0, color="black", linewidth=0.6)
        ax.grid(True, axis="x", alpha=0.3)
        apply_theme(ax, theme)
    return ax


def confidence_attribution_bar_interactive(
    attribution: Mapping[str, float], title: Optional[str] = None,
    figsize: FigureSize = (1000, 600), color: str = "indianred",
) -> PlotlyFigure:
    """Interactive uncertainty-attribution bar."""
    items = sorted(attribution.items(), key=lambda kv: kv[1])
    names = [k for k, _ in items]
    vals = [v for _, v in items]
    colors = ["#2ca02c" if v < 0 else color for v in vals]
    fig = go.Figure(go.Bar(x=vals, y=names, orientation="h",
                           marker_color=colors))
    fig.update_layout(title=title or "Uncertainty attribution",
                      xaxis_title="Δ uncertainty", yaxis_title="Feature",
                      width=figsize[0], height=figsize[1])
    return fig


def epistemic_vs_aleatoric_plot_static(
    bin_centers: np.ndarray, epistemic: np.ndarray, aleatoric: np.ndarray,
    title: Optional[str] = None, figsize: FigureSize = (10, 6),
    color_e: str = "steelblue", color_a: str = "darkorange",
    theme: str = "default", dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Stacked area of epistemic vs aleatoric uncertainty across bins."""
    title = title or "Epistemic vs aleatoric uncertainty"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Bin",
                             ylabel="Uncertainty", figsize=figsize)
        fig.set_dpi(dpi)
        ax.stackplot(bin_centers, epistemic, aleatoric,
                     colors=[color_e, color_a],
                     labels=["Epistemic", "Aleatoric"], alpha=0.8)
        ax.legend(loc="upper right")
        ax.grid(True, alpha=0.3)
        apply_theme(ax, theme)
    return ax


def epistemic_vs_aleatoric_plot_interactive(
    bin_centers: np.ndarray, epistemic: np.ndarray, aleatoric: np.ndarray,
    title: Optional[str] = None, figsize: FigureSize = (1000, 600),
    color_e: str = "steelblue", color_a: str = "darkorange",
) -> PlotlyFigure:
    """Interactive stacked uncertainty decomposition."""
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=bin_centers, y=epistemic, mode="lines",
                             stackgroup="u", line=dict(color=color_e),
                             name="Epistemic"))
    fig.add_trace(go.Scatter(x=bin_centers, y=aleatoric, mode="lines",
                             stackgroup="u", line=dict(color=color_a),
                             name="Aleatoric"))
    fig.update_layout(title=title or "Epistemic vs aleatoric uncertainty",
                      xaxis_title="Bin", yaxis_title="Uncertainty",
                      width=figsize[0], height=figsize[1])
    return fig
