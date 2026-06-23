"""Regression metric visualizations."""

from __future__ import annotations

from typing import Mapping, Optional, Sequence

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from ..types import ArrayLike, FigureSize, MatplotlibAxes, PlotlyFigure
from ..utils import setup_plot, apply_theme
from .helpers import _as_array, compute_regression_metrics


# ---------------------------------------------------------------------------
# Single-model metrics bar
# ---------------------------------------------------------------------------

def regression_metrics_bar_static(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    metrics: Sequence[str] = ("mae", "rmse", "medae", "r2"),
    title: Optional[str] = None,
    figsize: FigureSize = (9, 5),
    color: str = "#4c78a8",
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Bar chart of selected regression metrics for a single model."""
    m = compute_regression_metrics(y_true, y_pred).as_dict()
    values = [float(m[k]) for k in metrics]
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Regression Metrics",
                             xlabel="Metric", ylabel="Value", figsize=figsize)
        fig.set_dpi(dpi)
        ax.bar(list(metrics), values, color=color, alpha=0.85, **kwargs)
        for x, v in zip(metrics, values):
            ax.text(x, v, f"{v:.3g}", ha="center", va="bottom", fontsize=10)
        if grid:
            ax.grid(True, alpha=grid_alpha, axis="y")
        apply_theme(ax, theme)
    return ax


def regression_metrics_bar_interactive(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    metrics: Sequence[str] = ("mae", "rmse", "medae", "r2"),
    title: Optional[str] = None,
    color: str = "#4c78a8",
    template: str = "plotly",
    height: int = 500,
    width: int = 900,
    **kwargs,
) -> PlotlyFigure:
    """Interactive metrics bar chart."""
    m = compute_regression_metrics(y_true, y_pred).as_dict()
    values = [float(m[k]) for k in metrics]
    fig = go.Figure()
    fig.add_trace(go.Bar(x=list(metrics), y=values, marker_color=color,
                         text=[f"{v:.3g}" for v in values], textposition="outside",
                         name="Metric", **kwargs))
    fig.update_layout(title=title or "Regression Metrics",
                      xaxis_title="Metric", yaxis_title="Value",
                      template=template, height=height, width=width)
    return fig


# ---------------------------------------------------------------------------
# Multi-model metric comparison
# ---------------------------------------------------------------------------

def metric_comparison_bar_static(
    model_metrics: Mapping[str, Mapping[str, float]],
    metrics: Sequence[str] = ("mae", "rmse", "r2"),
    title: Optional[str] = None,
    figsize: FigureSize = (11, 6),
    cmap: str = "tab10",
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Grouped bar chart comparing metrics across models.

    ``model_metrics`` maps a model label to a mapping of metric name → value.
    Use :func:`compute_regression_metrics` (and ``.as_dict()``) to assemble.
    """
    models = list(model_metrics.keys())
    x = np.arange(len(metrics))
    width = 0.8 / max(len(models), 1)
    cmap_obj = plt.get_cmap(cmap)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Metric Comparison",
                             xlabel="Metric", ylabel="Value", figsize=figsize)
        fig.set_dpi(dpi)
        for i, name in enumerate(models):
            vals = [float(model_metrics[name].get(m, np.nan)) for m in metrics]
            ax.bar(x + i * width, vals, width,
                   color=cmap_obj(i % cmap_obj.N), label=name, **kwargs)
        ax.set_xticks(x + width * (len(models) - 1) / 2)
        ax.set_xticklabels(list(metrics))
        ax.legend()
        if grid:
            ax.grid(True, alpha=grid_alpha, axis="y")
        apply_theme(ax, theme)
    return ax


def metric_comparison_bar_interactive(
    model_metrics: Mapping[str, Mapping[str, float]],
    metrics: Sequence[str] = ("mae", "rmse", "r2"),
    title: Optional[str] = None,
    template: str = "plotly",
    height: int = 600,
    width: int = 1000,
    **kwargs,
) -> PlotlyFigure:
    """Interactive grouped metric comparison."""
    fig = go.Figure()
    for name, values in model_metrics.items():
        fig.add_trace(go.Bar(x=list(metrics),
                             y=[float(values.get(m, np.nan)) for m in metrics],
                             name=name, **kwargs))
    fig.update_layout(title=title or "Metric Comparison",
                      xaxis_title="Metric", yaxis_title="Value",
                      barmode="group", template=template,
                      height=height, width=width)
    return fig


# ---------------------------------------------------------------------------
# Metric radar
# ---------------------------------------------------------------------------

def _normalize_radar(values: np.ndarray) -> np.ndarray:
    rng = values.max() - values.min()
    if rng <= 0:
        return np.zeros_like(values)
    return (values - values.min()) / rng


def metric_radar_static(
    model_metrics: Mapping[str, Mapping[str, float]],
    metrics: Sequence[str] = ("mae", "rmse", "medae", "r2", "explained_variance"),
    higher_is_better: Optional[Mapping[str, bool]] = None,
    title: Optional[str] = None,
    figsize: FigureSize = (8, 8),
    cmap: str = "tab10",
    fill_alpha: float = 0.15,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Radar chart of normalized metrics across models."""
    higher = dict(higher_is_better) if higher_is_better else {"r2": True,
                                                              "explained_variance": True}
    models = list(model_metrics.keys())
    n_metrics = len(metrics)
    angles = np.linspace(0, 2 * np.pi, n_metrics, endpoint=False).tolist()
    angles += angles[:1]
    cmap_obj = plt.get_cmap(cmap)
    raw = np.array([[float(model_metrics[m].get(k, np.nan)) for m in models] for k in metrics])
    norm = np.zeros_like(raw)
    for i, k in enumerate(metrics):
        n = _normalize_radar(raw[i])
        norm[i] = n if higher.get(k, False) else 1.0 - n
    with plt.style.context(style):
        fig, ax = plt.subplots(figsize=figsize, dpi=dpi,
                               subplot_kw={"projection": "polar"})
        for i, name in enumerate(models):
            values = list(norm[:, i]) + [norm[0, i]]
            ax.plot(angles, values, color=cmap_obj(i % cmap_obj.N),
                    linewidth=2, label=name, **kwargs)
            ax.fill(angles, values, color=cmap_obj(i % cmap_obj.N), alpha=fill_alpha)
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(list(metrics))
        ax.set_title(title or "Metric Radar")
        ax.legend(loc="upper right", bbox_to_anchor=(1.25, 1.1))
        apply_theme(ax, theme)
    return ax


def metric_radar_interactive(
    model_metrics: Mapping[str, Mapping[str, float]],
    metrics: Sequence[str] = ("mae", "rmse", "medae", "r2", "explained_variance"),
    higher_is_better: Optional[Mapping[str, bool]] = None,
    title: Optional[str] = None,
    template: str = "plotly",
    height: int = 700,
    width: int = 800,
    **kwargs,
) -> PlotlyFigure:
    """Interactive metric radar chart."""
    higher = dict(higher_is_better) if higher_is_better else {"r2": True,
                                                              "explained_variance": True}
    models = list(model_metrics.keys())
    raw = np.array([[float(model_metrics[m].get(k, np.nan)) for m in models] for k in metrics])
    norm = np.zeros_like(raw)
    for i, k in enumerate(metrics):
        n = _normalize_radar(raw[i])
        norm[i] = n if higher.get(k, False) else 1.0 - n
    fig = go.Figure()
    cats = list(metrics) + [metrics[0]]
    for i, name in enumerate(models):
        vals = list(norm[:, i]) + [norm[0, i]]
        fig.add_trace(go.Scatterpolar(r=vals, theta=cats, fill="toself",
                                      name=name, **kwargs))
    fig.update_layout(title=title or "Metric Radar",
                      polar=dict(radialaxis=dict(range=[0, 1])),
                      template=template, height=height, width=width)
    return fig


# ---------------------------------------------------------------------------
# Per-segment metrics heatmap
# ---------------------------------------------------------------------------

def per_segment_metrics_heatmap_static(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    segments: ArrayLike,
    metrics: Sequence[str] = ("mae", "rmse", "medae", "r2"),
    title: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    cmap: str = "viridis",
    annotate: bool = True,
    theme: str = "default",
    dpi: int = 100,
    style: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Heatmap of metrics computed per segment of the data."""
    seg = pd.Series(np.asarray(segments))
    if seg.size != _as_array(y_true).size:
        raise ValueError("segments must align with y_true / y_pred.")
    df = pd.DataFrame({"y_true": _as_array(y_true), "y_pred": _as_array(y_pred),
                       "segment": seg.astype(str)})
    levels = list(df["segment"].unique())
    matrix = np.zeros((len(levels), len(metrics)))
    for r, lvl in enumerate(levels):
        sub = df.loc[df["segment"] == lvl]
        m = compute_regression_metrics(sub["y_true"], sub["y_pred"]).as_dict()
        matrix[r] = [float(m[k]) for k in metrics]
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Per-Segment Metrics",
                             xlabel="Metric", ylabel="Segment", figsize=figsize)
        fig.set_dpi(dpi)
        im = ax.imshow(matrix, aspect="auto", cmap=cmap, **kwargs)
        ax.set_xticks(np.arange(len(metrics)))
        ax.set_xticklabels(list(metrics))
        ax.set_yticks(np.arange(len(levels)))
        ax.set_yticklabels(levels)
        fig.colorbar(im, ax=ax, label="Value")
        if annotate:
            for i in range(len(levels)):
                for j in range(len(metrics)):
                    ax.text(j, i, f"{matrix[i, j]:.3g}", ha="center", va="center",
                            color="white", fontsize=8)
        apply_theme(ax, theme)
    return ax


def per_segment_metrics_heatmap_interactive(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    segments: ArrayLike,
    metrics: Sequence[str] = ("mae", "rmse", "medae", "r2"),
    title: Optional[str] = None,
    colorscale: str = "Viridis",
    template: str = "plotly",
    height: int = 600,
    width: int = 900,
    **kwargs,
) -> PlotlyFigure:
    """Interactive per-segment metric heatmap."""
    seg = pd.Series(np.asarray(segments)).astype(str)
    df = pd.DataFrame({"y_true": _as_array(y_true), "y_pred": _as_array(y_pred),
                       "segment": seg})
    levels = list(df["segment"].unique())
    matrix = np.zeros((len(levels), len(metrics)))
    for r, lvl in enumerate(levels):
        sub = df.loc[df["segment"] == lvl]
        m = compute_regression_metrics(sub["y_true"], sub["y_pred"]).as_dict()
        matrix[r] = [float(m[k]) for k in metrics]
    fig = go.Figure()
    fig.add_trace(go.Heatmap(z=matrix, x=list(metrics), y=levels,
                             colorscale=colorscale,
                             colorbar=dict(title="Value"), **kwargs))
    fig.update_layout(title=title or "Per-Segment Metrics",
                      xaxis_title="Metric", yaxis_title="Segment",
                      template=template, height=height, width=width)
    return fig


regression_metrics_bar = regression_metrics_bar_static
metric_comparison_bar = metric_comparison_bar_static
metric_radar = metric_radar_static
per_segment_metrics_heatmap = per_segment_metrics_heatmap_static
