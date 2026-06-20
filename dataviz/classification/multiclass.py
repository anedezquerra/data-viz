"""Multiclass and multi-model ROC / PR curves."""

from __future__ import annotations

from typing import Mapping, Optional, Sequence, Tuple

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from ..types import ArrayLike, FigureSize, MatplotlibAxes, PlotlyFigure
from ..utils import setup_plot, apply_theme


def _auc(x: ArrayLike, y: ArrayLike) -> float:
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    order = np.argsort(x)
    return float(np.trapezoid(y[order], x[order]))


def multiclass_roc_curve_static(
    curves: Mapping[str, Tuple[ArrayLike, ArrayLike]],
    title: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    linewidth: float = 2.0,
    show_macro: bool = True,
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = "default",
    legend_loc: str = "lower right",
    dpi: int = 100,
    style: str = "default",
) -> MatplotlibAxes:
    """Static one-vs-rest ROC curves for a multiclass classifier.

    Args:
        curves: Mapping ``class_name -> (fpr, tpr)`` for each one-vs-rest class.
        show_macro: Overlay the macro-averaged ROC curve.

    Returns:
        Matplotlib ``Axes`` containing one curve per class.
    """
    title = title or "Multiclass ROC (one-vs-rest)"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="False Positive Rate",
                             ylabel="True Positive Rate", figsize=figsize)
        fig.set_dpi(dpi)
        all_fpr = np.linspace(0, 1, 200)
        mean_tpr = np.zeros_like(all_fpr)
        for name, (fpr, tpr) in curves.items():
            auc = _auc(fpr, tpr)
            ax.plot(fpr, tpr, linewidth=linewidth, label=f"{name} (AUC={auc:.3f})")
            mean_tpr += np.interp(all_fpr, np.sort(fpr), np.asarray(tpr)[np.argsort(fpr)])
        if show_macro and curves:
            mean_tpr /= len(curves)
            macro_auc = _auc(all_fpr, mean_tpr)
            ax.plot(all_fpr, mean_tpr, color="black", linestyle="--",
                    linewidth=linewidth, label=f"macro avg (AUC={macro_auc:.3f})")
        ax.plot([0, 1], [0, 1], color="grey", linestyle=":", linewidth=1.0,
                label="random")
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1.02)
        if grid:
            ax.grid(True, alpha=grid_alpha)
        ax.legend(loc=legend_loc, fontsize=9)
        apply_theme(ax, theme)
    return ax


def multiclass_roc_curve_interactive(
    curves: Mapping[str, Tuple[ArrayLike, ArrayLike]],
    title: Optional[str] = None,
    show_macro: bool = True,
    height: int = 600,
    width: int = 700,
    template: str = "plotly",
) -> PlotlyFigure:
    """Interactive one-vs-rest ROC curves."""
    title = title or "Multiclass ROC (one-vs-rest)"
    fig = go.Figure()
    all_fpr = np.linspace(0, 1, 200)
    mean_tpr = np.zeros_like(all_fpr)
    for name, (fpr, tpr) in curves.items():
        auc = _auc(fpr, tpr)
        fig.add_trace(go.Scatter(x=list(fpr), y=list(tpr), mode="lines",
                                 name=f"{name} (AUC={auc:.3f})"))
        mean_tpr += np.interp(all_fpr, np.sort(fpr), np.asarray(tpr)[np.argsort(fpr)])
    if show_macro and curves:
        mean_tpr /= len(curves)
        fig.add_trace(go.Scatter(x=all_fpr, y=mean_tpr, mode="lines",
                                 line=dict(color="black", dash="dash"),
                                 name=f"macro (AUC={_auc(all_fpr, mean_tpr):.3f})"))
    fig.add_trace(go.Scatter(x=[0, 1], y=[0, 1], mode="lines",
                             line=dict(color="grey", dash="dot"), name="random"))
    fig.update_layout(title=title, xaxis_title="False Positive Rate",
                      yaxis_title="True Positive Rate", template=template,
                      height=height, width=width,
                      xaxis=dict(range=[0, 1]), yaxis=dict(range=[0, 1.02]))
    return fig


def multiclass_pr_curve_static(
    curves: Mapping[str, Tuple[ArrayLike, ArrayLike]],
    title: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    linewidth: float = 2.0,
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = "default",
    legend_loc: str = "lower left",
    dpi: int = 100,
    style: str = "default",
) -> MatplotlibAxes:
    """Static one-vs-rest precision-recall curves.

    Args:
        curves: Mapping ``class_name -> (recall, precision)`` arrays.
    """
    title = title or "Multiclass Precision-Recall (one-vs-rest)"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Recall", ylabel="Precision",
                             figsize=figsize)
        fig.set_dpi(dpi)
        for name, (recall, precision) in curves.items():
            ap = _auc(recall, precision)
            ax.plot(recall, precision, linewidth=linewidth,
                    label=f"{name} (AP={abs(ap):.3f})")
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1.02)
        if grid:
            ax.grid(True, alpha=grid_alpha)
        ax.legend(loc=legend_loc, fontsize=9)
        apply_theme(ax, theme)
    return ax


def multiclass_pr_curve_interactive(
    curves: Mapping[str, Tuple[ArrayLike, ArrayLike]],
    title: Optional[str] = None,
    height: int = 600,
    width: int = 700,
    template: str = "plotly",
) -> PlotlyFigure:
    """Interactive one-vs-rest precision-recall curves."""
    title = title or "Multiclass Precision-Recall (one-vs-rest)"
    fig = go.Figure()
    for name, (recall, precision) in curves.items():
        ap = _auc(recall, precision)
        fig.add_trace(go.Scatter(x=list(recall), y=list(precision), mode="lines",
                                 name=f"{name} (AP={abs(ap):.3f})"))
    fig.update_layout(title=title, xaxis_title="Recall", yaxis_title="Precision",
                      template=template, height=height, width=width,
                      xaxis=dict(range=[0, 1]), yaxis=dict(range=[0, 1.02]))
    return fig


def roc_curve_comparison_static(
    models: Mapping[str, Tuple[ArrayLike, ArrayLike]],
    title: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    linewidth: float = 2.0,
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = "default",
    legend_loc: str = "lower right",
    dpi: int = 100,
    style: str = "default",
) -> MatplotlibAxes:
    """Overlay ROC curves from several models for direct comparison.

    Args:
        models: Mapping ``model_name -> (fpr, tpr)``.
    """
    title = title or "Model comparison: ROC"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="False Positive Rate",
                             ylabel="True Positive Rate", figsize=figsize)
        fig.set_dpi(dpi)
        for name, (fpr, tpr) in models.items():
            ax.plot(fpr, tpr, linewidth=linewidth,
                    label=f"{name} (AUC={_auc(fpr, tpr):.3f})")
        ax.plot([0, 1], [0, 1], color="grey", linestyle=":", linewidth=1.0,
                label="random")
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1.02)
        if grid:
            ax.grid(True, alpha=grid_alpha)
        ax.legend(loc=legend_loc, fontsize=9)
        apply_theme(ax, theme)
    return ax


def roc_curve_comparison_interactive(
    models: Mapping[str, Tuple[ArrayLike, ArrayLike]],
    title: Optional[str] = None,
    height: int = 600,
    width: int = 700,
    template: str = "plotly",
) -> PlotlyFigure:
    """Interactive overlay of ROC curves from several models."""
    title = title or "Model comparison: ROC"
    fig = go.Figure()
    for name, (fpr, tpr) in models.items():
        fig.add_trace(go.Scatter(x=list(fpr), y=list(tpr), mode="lines",
                                 name=f"{name} (AUC={_auc(fpr, tpr):.3f})"))
    fig.add_trace(go.Scatter(x=[0, 1], y=[0, 1], mode="lines",
                             line=dict(color="grey", dash="dot"), name="random"))
    fig.update_layout(title=title, xaxis_title="False Positive Rate",
                      yaxis_title="True Positive Rate", template=template,
                      height=height, width=width,
                      xaxis=dict(range=[0, 1]), yaxis=dict(range=[0, 1.02]))
    return fig


def pr_curve_comparison_static(
    models: Mapping[str, Tuple[ArrayLike, ArrayLike]],
    title: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    linewidth: float = 2.0,
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = "default",
    legend_loc: str = "lower left",
    dpi: int = 100,
    style: str = "default",
) -> MatplotlibAxes:
    """Overlay precision-recall curves from several models.

    Args:
        models: Mapping ``model_name -> (recall, precision)``.
    """
    title = title or "Model comparison: precision-recall"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Recall", ylabel="Precision",
                             figsize=figsize)
        fig.set_dpi(dpi)
        for name, (recall, precision) in models.items():
            ax.plot(recall, precision, linewidth=linewidth,
                    label=f"{name} (AP={abs(_auc(recall, precision)):.3f})")
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1.02)
        if grid:
            ax.grid(True, alpha=grid_alpha)
        ax.legend(loc=legend_loc, fontsize=9)
        apply_theme(ax, theme)
    return ax


def pr_curve_comparison_interactive(
    models: Mapping[str, Tuple[ArrayLike, ArrayLike]],
    title: Optional[str] = None,
    height: int = 600,
    width: int = 700,
    template: str = "plotly",
) -> PlotlyFigure:
    """Interactive overlay of PR curves from several models."""
    title = title or "Model comparison: precision-recall"
    fig = go.Figure()
    for name, (recall, precision) in models.items():
        ap = abs(_auc(recall, precision))
        fig.add_trace(go.Scatter(x=list(recall), y=list(precision), mode="lines",
                                 name=f"{name} (AP={ap:.3f})"))
    fig.update_layout(title=title, xaxis_title="Recall", yaxis_title="Precision",
                      template=template, height=height, width=width,
                      xaxis=dict(range=[0, 1]), yaxis=dict(range=[0, 1.02]))
    return fig
