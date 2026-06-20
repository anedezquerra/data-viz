"""Extra threshold-based metric curves: F-beta, MCC, kappa, Youden's J, LR, PV."""

from __future__ import annotations

from typing import Optional, Sequence

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from ..types import ArrayLike, FigureSize, MatplotlibAxes, PlotlyFigure
from ..utils import setup_plot, apply_theme
from .threshold import _binary_counts


def _safe_div(a, b):
    return np.divide(a, b, out=np.zeros_like(a, dtype=float), where=np.asarray(b) > 0)


def _line_plot_static(thresholds, series, title, xlabel, ylabel, figsize, grid,
                      grid_alpha, theme, dpi, style, ymin=None, ymax=None,
                      best_idx=None, hlines=None):
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel=xlabel, ylabel=ylabel, figsize=figsize)
        fig.set_dpi(dpi)
        for name, y in series.items():
            ax.plot(thresholds, y, linewidth=2, label=name)
        if hlines:
            for y, lbl in hlines:
                ax.axhline(y, linestyle=":", color="grey", label=lbl)
        if best_idx is not None:
            t = thresholds[best_idx]
            ax.axvline(t, color="red", linestyle="--",
                       label=f"optimal t={t:.2f}")
        if ymin is not None or ymax is not None:
            ax.set_ylim(ymin, ymax)
        ax.set_xlim(thresholds.min(), thresholds.max())
        if grid:
            ax.grid(True, alpha=grid_alpha)
        ax.legend(fontsize=9)
        apply_theme(ax, theme)
    return ax


def _line_plot_interactive(thresholds, series, title, xlabel, ylabel,
                            height, width, template, best_idx=None, hlines=None):
    fig = go.Figure()
    for name, y in series.items():
        fig.add_trace(go.Scatter(x=thresholds, y=y, mode="lines", name=name))
    if hlines:
        for y, lbl in hlines:
            fig.add_hline(y=y, line_dash="dot", annotation_text=lbl)
    if best_idx is not None:
        t = float(thresholds[best_idx])
        fig.add_vline(x=t, line_dash="dash", line_color="red",
                      annotation_text=f"optimal t={t:.2f}")
    fig.update_layout(title=title, xaxis_title=xlabel, yaxis_title=ylabel,
                      template=template, height=height, width=width)
    return fig


def _counts(y_true, y_prob, n):
    thresholds = np.linspace(0, 1, n)
    counts = _binary_counts(np.asarray(y_true).astype(int),
                            np.asarray(y_prob, dtype=float), thresholds)
    return thresholds, counts.T  # tp, fp, tn, fn


def f_beta_curve_static(y_true: ArrayLike, y_prob: ArrayLike,
                        betas: Sequence[float] = (0.5, 1.0, 2.0),
                        n_thresholds: int = 100, title: Optional[str] = None,
                        figsize: FigureSize = (10, 6), grid: bool = True,
                        grid_alpha: float = 0.3, theme: str = "default",
                        dpi: int = 100, style: str = "default") -> MatplotlibAxes:
    """F-beta scores vs decision threshold for several beta values."""
    thresholds, (tp, fp, _, fn) = _counts(y_true, y_prob, n_thresholds)
    p = _safe_div(tp, tp + fp)
    r = _safe_div(tp, tp + fn)
    series = {}
    for b in betas:
        b2 = b * b
        series[f"F{b:g}"] = _safe_div((1 + b2) * p * r, b2 * p + r)
    title = title or "F-beta vs threshold"
    return _line_plot_static(thresholds, series, title, "Threshold", "F-beta",
                              figsize, grid, grid_alpha, theme, dpi, style,
                              ymin=0, ymax=1.02)


def f_beta_curve_interactive(y_true: ArrayLike, y_prob: ArrayLike,
                              betas: Sequence[float] = (0.5, 1.0, 2.0),
                              n_thresholds: int = 100,
                              title: Optional[str] = None, height: int = 600,
                              width: int = 800, template: str = "plotly") -> PlotlyFigure:
    """Interactive F-beta vs threshold."""
    thresholds, (tp, fp, _, fn) = _counts(y_true, y_prob, n_thresholds)
    p = _safe_div(tp, tp + fp); r = _safe_div(tp, tp + fn)
    series = {}
    for b in betas:
        b2 = b * b
        series[f"F{b:g}"] = _safe_div((1 + b2) * p * r, b2 * p + r)
    return _line_plot_interactive(thresholds, series, title or "F-beta vs threshold",
                                   "Threshold", "F-beta", height, width, template)


def mcc_curve_static(y_true: ArrayLike, y_prob: ArrayLike,
                     n_thresholds: int = 100, title: Optional[str] = None,
                     figsize: FigureSize = (10, 6), grid: bool = True,
                     grid_alpha: float = 0.3, theme: str = "default",
                     dpi: int = 100, style: str = "default") -> MatplotlibAxes:
    """Matthews correlation coefficient vs threshold, with argmax marker."""
    thresholds, (tp, fp, tn, fn) = _counts(y_true, y_prob, n_thresholds)
    denom = np.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))
    mcc = _safe_div(tp * tn - fp * fn, denom)
    best = int(np.argmax(mcc))
    title = title or f"MCC vs threshold (best={mcc[best]:.3f} @ t={thresholds[best]:.2f})"
    return _line_plot_static(thresholds, {"MCC": mcc}, title, "Threshold", "MCC",
                              figsize, grid, grid_alpha, theme, dpi, style,
                              ymin=-1, ymax=1, best_idx=best)


def mcc_curve_interactive(y_true: ArrayLike, y_prob: ArrayLike,
                          n_thresholds: int = 100, title: Optional[str] = None,
                          height: int = 600, width: int = 800,
                          template: str = "plotly") -> PlotlyFigure:
    thresholds, (tp, fp, tn, fn) = _counts(y_true, y_prob, n_thresholds)
    denom = np.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))
    mcc = _safe_div(tp * tn - fp * fn, denom)
    best = int(np.argmax(mcc))
    return _line_plot_interactive(thresholds, {"MCC": mcc},
                                   title or "MCC vs threshold", "Threshold", "MCC",
                                   height, width, template, best_idx=best)


def youden_j_curve_static(y_true: ArrayLike, y_prob: ArrayLike,
                          n_thresholds: int = 100, title: Optional[str] = None,
                          figsize: FigureSize = (10, 6), grid: bool = True,
                          grid_alpha: float = 0.3, theme: str = "default",
                          dpi: int = 100, style: str = "default") -> MatplotlibAxes:
    """Youden's J statistic (sensitivity + specificity - 1) vs threshold."""
    thresholds, (tp, fp, tn, fn) = _counts(y_true, y_prob, n_thresholds)
    sens = _safe_div(tp, tp + fn); spec = _safe_div(tn, tn + fp)
    j = sens + spec - 1
    best = int(np.argmax(j))
    title = title or f"Youden's J (max={j[best]:.3f} @ t={thresholds[best]:.2f})"
    return _line_plot_static(thresholds,
                              {"sensitivity": sens, "specificity": spec, "J": j},
                              title, "Threshold", "Score",
                              figsize, grid, grid_alpha, theme, dpi, style,
                              ymin=0, ymax=1.02, best_idx=best)


def youden_j_curve_interactive(y_true: ArrayLike, y_prob: ArrayLike,
                                n_thresholds: int = 100, title: Optional[str] = None,
                                height: int = 600, width: int = 800,
                                template: str = "plotly") -> PlotlyFigure:
    thresholds, (tp, fp, tn, fn) = _counts(y_true, y_prob, n_thresholds)
    sens = _safe_div(tp, tp + fn); spec = _safe_div(tn, tn + fp)
    j = sens + spec - 1
    return _line_plot_interactive(thresholds,
                                   {"sensitivity": sens, "specificity": spec, "J": j},
                                   title or "Youden's J vs threshold",
                                   "Threshold", "Score", height, width, template,
                                   best_idx=int(np.argmax(j)))


def balanced_accuracy_curve_static(y_true: ArrayLike, y_prob: ArrayLike,
                                    n_thresholds: int = 100, title: Optional[str] = None,
                                    figsize: FigureSize = (10, 6), grid: bool = True,
                                    grid_alpha: float = 0.3, theme: str = "default",
                                    dpi: int = 100, style: str = "default") -> MatplotlibAxes:
    """Balanced accuracy ((sens+spec)/2) vs threshold."""
    thresholds, (tp, fp, tn, fn) = _counts(y_true, y_prob, n_thresholds)
    bacc = (_safe_div(tp, tp + fn) + _safe_div(tn, tn + fp)) / 2
    best = int(np.argmax(bacc))
    title = title or f"Balanced accuracy (max={bacc[best]:.3f})"
    return _line_plot_static(thresholds, {"balanced accuracy": bacc}, title,
                              "Threshold", "Balanced accuracy",
                              figsize, grid, grid_alpha, theme, dpi, style,
                              ymin=0, ymax=1.02, best_idx=best)


def balanced_accuracy_curve_interactive(y_true: ArrayLike, y_prob: ArrayLike,
                                         n_thresholds: int = 100,
                                         title: Optional[str] = None,
                                         height: int = 600, width: int = 800,
                                         template: str = "plotly") -> PlotlyFigure:
    thresholds, (tp, fp, tn, fn) = _counts(y_true, y_prob, n_thresholds)
    bacc = (_safe_div(tp, tp + fn) + _safe_div(tn, tn + fp)) / 2
    return _line_plot_interactive(thresholds, {"balanced accuracy": bacc},
                                   title or "Balanced accuracy vs threshold",
                                   "Threshold", "Balanced accuracy",
                                   height, width, template,
                                   best_idx=int(np.argmax(bacc)))


def cohen_kappa_curve_static(y_true: ArrayLike, y_prob: ArrayLike,
                              n_thresholds: int = 100, title: Optional[str] = None,
                              figsize: FigureSize = (10, 6), grid: bool = True,
                              grid_alpha: float = 0.3, theme: str = "default",
                              dpi: int = 100, style: str = "default") -> MatplotlibAxes:
    """Cohen's kappa vs threshold."""
    thresholds, (tp, fp, tn, fn) = _counts(y_true, y_prob, n_thresholds)
    n = tp + fp + tn + fn
    po = (tp + tn) / n
    pe = ((tp + fp) * (tp + fn) + (tn + fp) * (tn + fn)) / (n * n)
    kappa = _safe_div(po - pe, 1 - pe)
    best = int(np.argmax(kappa))
    title = title or f"Cohen's kappa (max={kappa[best]:.3f})"
    return _line_plot_static(thresholds, {"kappa": kappa}, title,
                              "Threshold", "Kappa",
                              figsize, grid, grid_alpha, theme, dpi, style,
                              ymin=-0.05, ymax=1.02, best_idx=best)


def cohen_kappa_curve_interactive(y_true: ArrayLike, y_prob: ArrayLike,
                                   n_thresholds: int = 100, title: Optional[str] = None,
                                   height: int = 600, width: int = 800,
                                   template: str = "plotly") -> PlotlyFigure:
    thresholds, (tp, fp, tn, fn) = _counts(y_true, y_prob, n_thresholds)
    n = tp + fp + tn + fn
    po = (tp + tn) / n
    pe = ((tp + fp) * (tp + fn) + (tn + fp) * (tn + fn)) / (n * n)
    kappa = _safe_div(po - pe, 1 - pe)
    return _line_plot_interactive(thresholds, {"kappa": kappa},
                                   title or "Cohen's kappa vs threshold",
                                   "Threshold", "Kappa", height, width, template,
                                   best_idx=int(np.argmax(kappa)))


def likelihood_ratio_curve_static(y_true: ArrayLike, y_prob: ArrayLike,
                                   n_thresholds: int = 100,
                                   log_scale: bool = True,
                                   title: Optional[str] = None,
                                   figsize: FigureSize = (10, 6),
                                   grid: bool = True, grid_alpha: float = 0.3,
                                   theme: str = "default", dpi: int = 100,
                                   style: str = "default") -> MatplotlibAxes:
    """Positive / negative likelihood ratios vs threshold (clinical diagnostics)."""
    thresholds, (tp, fp, tn, fn) = _counts(y_true, y_prob, n_thresholds)
    sens = _safe_div(tp, tp + fn); spec = _safe_div(tn, tn + fp)
    lr_pos = _safe_div(sens, 1 - spec)
    lr_neg = _safe_div(1 - sens, spec)
    title = title or "Likelihood ratios"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Threshold",
                             ylabel="Likelihood ratio", figsize=figsize)
        fig.set_dpi(dpi)
        ax.plot(thresholds, lr_pos, linewidth=2, label="LR+")
        ax.plot(thresholds, lr_neg, linewidth=2, label="LR-")
        ax.axhline(1.0, linestyle=":", color="grey")
        if log_scale:
            ax.set_yscale("log")
        if grid:
            ax.grid(True, alpha=grid_alpha)
        ax.legend()
        apply_theme(ax, theme)
    return ax


def likelihood_ratio_curve_interactive(y_true: ArrayLike, y_prob: ArrayLike,
                                        n_thresholds: int = 100,
                                        log_scale: bool = True,
                                        title: Optional[str] = None,
                                        height: int = 600, width: int = 800,
                                        template: str = "plotly") -> PlotlyFigure:
    thresholds, (tp, fp, tn, fn) = _counts(y_true, y_prob, n_thresholds)
    sens = _safe_div(tp, tp + fn); spec = _safe_div(tn, tn + fp)
    lr_pos = _safe_div(sens, 1 - spec)
    lr_neg = _safe_div(1 - sens, spec)
    title = title or "Likelihood ratios"
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=thresholds, y=lr_pos, mode="lines", name="LR+"))
    fig.add_trace(go.Scatter(x=thresholds, y=lr_neg, mode="lines", name="LR-"))
    fig.add_hline(y=1.0, line_dash="dot")
    fig.update_layout(title=title, xaxis_title="Threshold",
                      yaxis_title="Likelihood ratio",
                      yaxis_type="log" if log_scale else "linear",
                      template=template, height=height, width=width)
    return fig


def predictive_value_curve_static(sensitivity: float, specificity: float,
                                   prevalences: Optional[ArrayLike] = None,
                                   title: Optional[str] = None,
                                   figsize: FigureSize = (10, 6), grid: bool = True,
                                   grid_alpha: float = 0.3, theme: str = "default",
                                   dpi: int = 100, style: str = "default") -> MatplotlibAxes:
    """PPV and NPV as a function of disease prevalence for fixed sens / spec."""
    if prevalences is None:
        prev = np.linspace(0.001, 0.999, 200)
    else:
        prev = np.asarray(prevalences, dtype=float)
    ppv = (sensitivity * prev) / (sensitivity * prev + (1 - specificity) * (1 - prev))
    npv = (specificity * (1 - prev)) / ((1 - sensitivity) * prev + specificity * (1 - prev))
    title = title or f"Predictive values (sens={sensitivity:.2f}, spec={specificity:.2f})"
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel="Prevalence",
                             ylabel="Predictive value", figsize=figsize)
        fig.set_dpi(dpi)
        ax.plot(prev, ppv, linewidth=2, label="PPV")
        ax.plot(prev, npv, linewidth=2, label="NPV")
        ax.set_xlim(0, 1); ax.set_ylim(0, 1.02)
        if grid:
            ax.grid(True, alpha=grid_alpha)
        ax.legend()
        apply_theme(ax, theme)
    return ax


def predictive_value_curve_interactive(sensitivity: float, specificity: float,
                                        prevalences: Optional[ArrayLike] = None,
                                        title: Optional[str] = None,
                                        height: int = 600, width: int = 800,
                                        template: str = "plotly") -> PlotlyFigure:
    prev = np.linspace(0.001, 0.999, 200) if prevalences is None else np.asarray(prevalences, dtype=float)
    ppv = (sensitivity * prev) / (sensitivity * prev + (1 - specificity) * (1 - prev))
    npv = (specificity * (1 - prev)) / ((1 - sensitivity) * prev + specificity * (1 - prev))
    title = title or f"Predictive values (sens={sensitivity:.2f}, spec={specificity:.2f})"
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=prev, y=ppv, mode="lines", name="PPV"))
    fig.add_trace(go.Scatter(x=prev, y=npv, mode="lines", name="NPV"))
    fig.update_layout(title=title, xaxis_title="Prevalence",
                      yaxis_title="Predictive value", template=template,
                      height=height, width=width,
                      xaxis=dict(range=[0, 1]), yaxis=dict(range=[0, 1.02]))
    return fig
