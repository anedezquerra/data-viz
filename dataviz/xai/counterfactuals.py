"""Counterfactual / what-if explanations: paths, diverse alternatives, sliders."""

from __future__ import annotations

from typing import Mapping, Optional, Sequence

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from ..types import FigureSize, MatplotlibAxes, PlotlyFigure
from ..utils import setup_plot, apply_theme


def counterfactual_path_plot_static(
    steps: pd.DataFrame, predictions: Sequence[float],
    target_threshold: float = 0.5, title: Optional[str] = None,
    figsize: FigureSize = (11, 6), cmap: str = "tab10",
    theme: str = "default", dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Trajectory of feature changes flipping a prediction.

    ``steps``: rows = sequential states, columns = features.
    """
    title = title or "Counterfactual path"
    cols = list(steps.columns)
    x = np.arange(len(steps))
    with plt.style.context(style):
        fig, axes = plt.subplots(2, 1, figsize=figsize, dpi=dpi,
                                 sharex=True, gridspec_kw={"height_ratios": [3, 1]})
        ax = axes[0]
        colors = plt.get_cmap(cmap)(np.linspace(0, 1, len(cols)))
        norm = steps.copy()
        for c in cols:
            v = steps[c].astype(float)
            if v.max() != v.min():
                norm[c] = (v - v.min()) / (v.max() - v.min())
            else:
                norm[c] = 0.0
        for c, col in zip(colors, cols):
            ax.plot(x, norm[col], marker="o", color=c, label=col)
        ax.set_ylabel("Normalised feature value")
        ax.legend(loc="upper right", fontsize=8)
        ax.set_title(title)
        ax2 = axes[1]
        ax2.plot(x, predictions, "o-", color="black")
        ax2.axhline(target_threshold, color="red", linestyle="--",
                    label="Threshold")
        ax2.set_ylabel("Prediction")
        ax2.set_xlabel("Step")
        ax2.legend()
        apply_theme(ax, theme)
        apply_theme(ax2, theme)
    return axes[0]


def counterfactual_path_plot_interactive(
    steps: pd.DataFrame, predictions: Sequence[float],
    target_threshold: float = 0.5, title: Optional[str] = None,
    figsize: FigureSize = (1100, 700),
) -> PlotlyFigure:
    """Interactive counterfactual path with dual subplot."""
    from plotly.subplots import make_subplots
    cols = list(steps.columns)
    x = list(range(len(steps)))
    norm = steps.copy()
    for c in cols:
        v = steps[c].astype(float)
        if v.max() != v.min():
            norm[c] = (v - v.min()) / (v.max() - v.min())
        else:
            norm[c] = 0.0
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True,
                        row_heights=[0.7, 0.3], vertical_spacing=0.08)
    for col in cols:
        fig.add_trace(go.Scatter(x=x, y=norm[col], mode="lines+markers",
                                 name=col), row=1, col=1)
    fig.add_trace(go.Scatter(x=x, y=list(predictions), mode="lines+markers",
                             line=dict(color="black"), name="Prediction"),
                  row=2, col=1)
    fig.add_hline(y=target_threshold, line=dict(color="red", dash="dash"),
                  row=2, col=1)
    fig.update_layout(title=title or "Counterfactual path",
                      width=figsize[0], height=figsize[1])
    return fig


def diverse_counterfactual_grid_static(
    original: Mapping[str, float], counterfactuals: pd.DataFrame,
    title: Optional[str] = None, figsize: FigureSize = (11, 6),
    cmap: str = "RdBu_r", theme: str = "default",
    dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """Grid of diverse counterfactuals showing per-feature delta from original."""
    cols = list(original.keys())
    orig = np.array([original[c] for c in cols], dtype=float)
    M = counterfactuals[cols].to_numpy(dtype=float) - orig
    vmax = float(np.abs(M).max() or 1.0)
    title = title or "Diverse counterfactuals (Δ from original)"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Feature",
                             ylabel="Counterfactual", figsize=figsize)
        fig.set_dpi(dpi)
        im = ax.imshow(M, cmap=cmap, aspect="auto", vmin=-vmax, vmax=vmax)
        ax.set_xticks(range(len(cols)))
        ax.set_xticklabels(cols, rotation=45, ha="right")
        ax.set_yticks(range(len(counterfactuals)))
        ax.set_yticklabels([f"CF {i}" for i in range(len(counterfactuals))])
        for i in range(M.shape[0]):
            for j in range(M.shape[1]):
                if abs(M[i, j]) > 1e-9:
                    ax.text(j, i, f"{M[i, j]:+.2f}",
                            ha="center", va="center", fontsize=8,
                            color="white" if abs(M[i, j]) > 0.6 * vmax else "black")
        fig.colorbar(im, ax=ax, label="Δ")
        apply_theme(ax, theme)
    return ax


def diverse_counterfactual_grid_interactive(
    original: Mapping[str, float], counterfactuals: pd.DataFrame,
    title: Optional[str] = None, figsize: FigureSize = (1100, 600),
    colorscale: str = "RdBu",
) -> PlotlyFigure:
    """Interactive diverse counterfactuals delta heatmap."""
    cols = list(original.keys())
    orig = np.array([original[c] for c in cols], dtype=float)
    M = counterfactuals[cols].to_numpy(dtype=float) - orig
    vmax = float(np.abs(M).max() or 1.0)
    fig = go.Figure(go.Heatmap(
        z=M, x=cols,
        y=[f"CF {i}" for i in range(len(counterfactuals))],
        colorscale=colorscale, zmin=-vmax, zmax=vmax,
        text=np.round(M, 2), texttemplate="%{text}",
        colorbar=dict(title="Δ"),
    ))
    fig.update_layout(title=title or "Diverse counterfactuals (Δ)",
                      width=figsize[0], height=figsize[1])
    return fig


def what_if_slider_plot_static(
    feature_grid: np.ndarray, predictions: np.ndarray,
    feature_name: str, current_value: Optional[float] = None,
    threshold: Optional[float] = None, title: Optional[str] = None,
    figsize: FigureSize = (10, 6), color: str = "steelblue",
    theme: str = "default", dpi: int = 100, style: str = "default",
) -> MatplotlibAxes:
    """What-if curve: prediction as a single feature is swept."""
    title = title or f"What-if — {feature_name}"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel=feature_name,
                             ylabel="Prediction", figsize=figsize)
        fig.set_dpi(dpi)
        ax.plot(feature_grid, predictions, color=color, linewidth=2.0)
        if current_value is not None:
            ax.axvline(current_value, color="black", linestyle=":",
                       label="Current value")
        if threshold is not None:
            ax.axhline(threshold, color="red", linestyle="--",
                       label="Threshold")
        if current_value is not None or threshold is not None:
            ax.legend()
        ax.grid(True, alpha=0.3)
        apply_theme(ax, theme)
    return ax


def what_if_slider_plot_interactive(
    feature_grid: np.ndarray, predictions: np.ndarray,
    feature_name: str, current_value: Optional[float] = None,
    threshold: Optional[float] = None, title: Optional[str] = None,
    figsize: FigureSize = (1000, 600), color: str = "steelblue",
) -> PlotlyFigure:
    """Interactive what-if slider curve."""
    fig = go.Figure(go.Scatter(x=feature_grid, y=predictions, mode="lines",
                               line=dict(color=color, width=3),
                               name="Prediction"))
    if current_value is not None:
        fig.add_vline(x=current_value, line=dict(color="black", dash="dot"),
                      annotation_text="Current")
    if threshold is not None:
        fig.add_hline(y=threshold, line=dict(color="red", dash="dash"),
                      annotation_text="Threshold")
    fig.update_layout(title=title or f"What-if — {feature_name}",
                      xaxis_title=feature_name, yaxis_title="Prediction",
                      width=figsize[0], height=figsize[1])
    return fig
