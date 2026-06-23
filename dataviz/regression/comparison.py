"""Multi-model comparison charts."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from ..types import MatplotlibAxes, PlotlyFigure
from ..utils import setup_plot, apply_theme
from .helpers import _as_array


def _kde(x, n=200):
    x = _as_array(x)
    if x.size == 0: return np.array([]), np.array([])
    lo, hi = x.min() - 0.1 * (x.std() + 1e-9), x.max() + 0.1 * (x.std() + 1e-9)
    grid = np.linspace(lo, hi, n)
    bw = 1.06 * (x.std() + 1e-9) * x.size ** (-1 / 5)
    d = (grid[:, None] - x[None, :]) / bw
    k = np.exp(-0.5 * d ** 2) / np.sqrt(2 * np.pi)
    return grid, k.mean(axis=1) / bw


def multi_model_pred_vs_actual_overlay_static(y_true, predictions_per_model,
                                              model_labels, title=None,
                                              figsize=(8, 8), cmap="viridis",
                                              line_color="#e45756", style="default",
                                              theme="default", dpi=100,
                                              **kwargs) -> MatplotlibAxes:
    """Overlay predicted vs actual scatter for multiple models."""
    yt = _as_array(y_true)
    cmap_obj = plt.get_cmap(cmap)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Predicted vs Actual (overlay)",
                             xlabel="actual", ylabel="predicted", figsize=figsize)
        fig.set_dpi(dpi)
        for i, (p, lbl) in enumerate(zip(predictions_per_model, model_labels)):
            ax.scatter(yt, _as_array(p),
                       color=cmap_obj(i / max(len(model_labels) - 1, 1)),
                       alpha=0.5, label=str(lbl), **kwargs)
        lo, hi = float(yt.min()), float(yt.max())
        ax.plot([lo, hi], [lo, hi], color=line_color, linestyle="--")
        ax.legend(); ax.grid(True, alpha=0.3); apply_theme(ax, theme)
    return ax


def multi_model_pred_vs_actual_overlay_interactive(y_true, predictions_per_model,
                                                   model_labels, title=None,
                                                   line_color="#e45756",
                                                   template="plotly", height=700,
                                                   width=800, **kwargs) -> PlotlyFigure:
    """Interactive multi-model predicted vs actual overlay."""
    yt = _as_array(y_true)
    fig = go.Figure()
    for p, lbl in zip(predictions_per_model, model_labels):
        fig.add_trace(go.Scatter(x=yt, y=_as_array(p), mode="markers",
                                 name=str(lbl), opacity=0.6, **kwargs))
    lo, hi = float(yt.min()), float(yt.max())
    fig.add_trace(go.Scatter(x=[lo, hi], y=[lo, hi], mode="lines",
                             line=dict(color=line_color, dash="dash"),
                             showlegend=False))
    fig.update_layout(title=title or "Predicted vs Actual (overlay)",
                      template=template, height=height, width=width,
                      xaxis_title="actual", yaxis_title="predicted")
    return fig


def residual_density_overlay_multi_static(residuals_per_model, model_labels,
                                          title=None, figsize=(10, 6), cmap="viridis",
                                          style="default", theme="default", dpi=100,
                                          **kwargs) -> MatplotlibAxes:
    """Overlay residual KDEs for multiple models."""
    cmap_obj = plt.get_cmap(cmap)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Residual Density Overlay",
                             xlabel="residual", ylabel="density", figsize=figsize)
        fig.set_dpi(dpi)
        for i, (r, lbl) in enumerate(zip(residuals_per_model, model_labels)):
            xs, ys = _kde(r)
            ax.plot(xs, ys, color=cmap_obj(i / max(len(model_labels) - 1, 1)),
                    label=str(lbl), **kwargs)
        ax.axvline(0, color="#888", linestyle="--")
        ax.legend(); ax.grid(True, alpha=0.3); apply_theme(ax, theme)
    return ax


def residual_density_overlay_multi_interactive(residuals_per_model, model_labels,
                                               title=None, template="plotly",
                                               height=600, width=1000,
                                               **kwargs) -> PlotlyFigure:
    """Interactive residual density overlay."""
    fig = go.Figure()
    for r, lbl in zip(residuals_per_model, model_labels):
        xs, ys = _kde(r)
        fig.add_trace(go.Scatter(x=xs, y=ys, mode="lines", name=str(lbl), **kwargs))
    fig.add_vline(x=0, line_dash="dash", line_color="#888")
    fig.update_layout(title=title or "Residual Density Overlay",
                      template=template, height=height, width=width,
                      xaxis_title="residual", yaxis_title="density")
    return fig


def error_ecdf_overlay_static(errors_per_model, model_labels, title=None,
                              figsize=(10, 6), cmap="viridis", style="default",
                              theme="default", dpi=100, **kwargs) -> MatplotlibAxes:
    """Overlay empirical CDFs of \\|error\\| per model."""
    cmap_obj = plt.get_cmap(cmap)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Error ECDF (overlay)",
                             xlabel="|error|", ylabel="F(|error|)", figsize=figsize)
        fig.set_dpi(dpi)
        for i, (e, lbl) in enumerate(zip(errors_per_model, model_labels)):
            ea = np.sort(np.abs(_as_array(e)))
            y = np.arange(1, len(ea) + 1) / max(len(ea), 1)
            ax.plot(ea, y, color=cmap_obj(i / max(len(model_labels) - 1, 1)),
                    label=str(lbl), **kwargs)
        ax.legend(); ax.grid(True, alpha=0.3); apply_theme(ax, theme)
    return ax


def error_ecdf_overlay_interactive(errors_per_model, model_labels, title=None,
                                   template="plotly", height=600, width=1000,
                                   **kwargs) -> PlotlyFigure:
    """Interactive error ECDF overlay."""
    fig = go.Figure()
    for e, lbl in zip(errors_per_model, model_labels):
        ea = np.sort(np.abs(_as_array(e)))
        y = np.arange(1, len(ea) + 1) / max(len(ea), 1)
        fig.add_trace(go.Scatter(x=ea, y=y, mode="lines", name=str(lbl), **kwargs))
    fig.update_layout(title=title or "Error ECDF (overlay)", template=template,
                      height=height, width=width,
                      xaxis_title="|error|", yaxis_title="F(|error|)")
    return fig


def model_winner_heatmap_static(model_labels, metric_labels, win_matrix, title=None,
                                figsize=(9, 7), cmap="viridis", style="default",
                                theme="default", dpi=100, **kwargs) -> MatplotlibAxes:
    """Heatmap of which model "wins" per metric (1 = best, 0 = not)."""
    m = np.asarray(win_matrix, dtype=float)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Model Winner Heatmap",
                             xlabel="metric", ylabel="model", figsize=figsize)
        fig.set_dpi(dpi)
        im = ax.imshow(m, aspect="auto", cmap=cmap, vmin=0, vmax=1, **kwargs)
        ax.set_xticks(range(len(metric_labels))); ax.set_xticklabels(metric_labels, rotation=45, ha="right")
        ax.set_yticks(range(len(model_labels))); ax.set_yticklabels(model_labels)
        fig.colorbar(im, ax=ax, label="win"); apply_theme(ax, theme)
    return ax


def model_winner_heatmap_interactive(model_labels, metric_labels, win_matrix, title=None,
                                     colorscale="Viridis", template="plotly",
                                     height=700, width=900, **kwargs) -> PlotlyFigure:
    """Interactive model-winner heatmap."""
    m = np.asarray(win_matrix, dtype=float)
    fig = go.Figure([go.Heatmap(z=m, x=list(metric_labels), y=list(model_labels),
                                zmin=0, zmax=1, colorscale=colorscale,
                                colorbar=dict(title="win"), **kwargs)])
    fig.update_layout(title=title or "Model Winner Heatmap", template=template,
                      height=height, width=width)
    return fig


multi_model_pred_vs_actual_overlay = multi_model_pred_vs_actual_overlay_static
residual_density_overlay_multi = residual_density_overlay_multi_static
error_ecdf_overlay = error_ecdf_overlay_static
model_winner_heatmap = model_winner_heatmap_static
