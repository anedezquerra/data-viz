"""Predictive uncertainty charts (conformal, jackknife+, calibration)."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from ..types import MatplotlibAxes, PlotlyFigure
from ..utils import setup_plot, apply_theme
from .helpers import _as_array


def conformal_interval_plot_static(y_true, y_pred, lower, upper, title=None,
                                   figsize=(10, 6), color="#4c78a8",
                                   band_color="#a8c5e0", style="default",
                                   theme="default", dpi=100, **kwargs) -> MatplotlibAxes:
    """Sorted-by-prediction view of conformal prediction intervals."""
    yp = _as_array(y_pred); yt = _as_array(y_true)
    lo, hi = _as_array(lower), _as_array(upper)
    order = np.argsort(yp)
    idx = np.arange(len(yp))
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Conformal Intervals",
                             xlabel="rank by prediction", ylabel="y", figsize=figsize)
        fig.set_dpi(dpi)
        ax.fill_between(idx, lo[order], hi[order], color=band_color, alpha=0.5)
        ax.plot(idx, yp[order], color=color, linewidth=2, label="prediction", **kwargs)
        ax.scatter(idx, yt[order], color="#222", s=10, alpha=0.6, label="actual")
        ax.legend(); ax.grid(True, alpha=0.3); apply_theme(ax, theme)
    return ax


def conformal_interval_plot_interactive(y_true, y_pred, lower, upper, title=None,
                                        color="#4c78a8",
                                        band_color="rgba(168,197,224,0.5)",
                                        template="plotly", height=600, width=1100,
                                        **kwargs) -> PlotlyFigure:
    """Interactive conformal intervals."""
    yp = _as_array(y_pred); yt = _as_array(y_true)
    lo, hi = _as_array(lower), _as_array(upper)
    order = np.argsort(yp); idx = np.arange(len(yp))
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=idx, y=hi[order], mode="lines",
                             line=dict(width=0), showlegend=False))
    fig.add_trace(go.Scatter(x=idx, y=lo[order], mode="lines", line=dict(width=0),
                             fill="tonexty", fillcolor=band_color, name="interval"))
    fig.add_trace(go.Scatter(x=idx, y=yp[order], mode="lines",
                             line=dict(color=color, width=2), name="prediction", **kwargs))
    fig.add_trace(go.Scatter(x=idx, y=yt[order], mode="markers",
                             marker=dict(color="#222", size=4), name="actual"))
    fig.update_layout(title=title or "Conformal Intervals", template=template,
                      height=height, width=width,
                      xaxis_title="rank by prediction", yaxis_title="y")
    return fig


def jackknife_plus_band_static(y_true, y_pred, lower, upper, title=None,
                               figsize=(10, 6), color="#4c78a8",
                               band_color="#fcd9b6", style="default",
                               theme="default", dpi=100, **kwargs) -> MatplotlibAxes:
    """Jackknife+ predictive band (same view as conformal, distinct colour)."""
    return conformal_interval_plot_static(y_true, y_pred, lower, upper,
                                          title=title or "Jackknife+ Band",
                                          figsize=figsize, color=color,
                                          band_color=band_color, style=style,
                                          theme=theme, dpi=dpi, **kwargs)


def jackknife_plus_band_interactive(y_true, y_pred, lower, upper, title=None,
                                    color="#4c78a8",
                                    band_color="rgba(252,217,182,0.5)",
                                    template="plotly", height=600, width=1100,
                                    **kwargs) -> PlotlyFigure:
    """Interactive jackknife+ band."""
    return conformal_interval_plot_interactive(y_true, y_pred, lower, upper,
                                               title=title or "Jackknife+ Band",
                                               color=color, band_color=band_color,
                                               template=template, height=height,
                                               width=width, **kwargs)


def quantile_calibration_plot_static(nominal_quantiles, empirical_quantiles, title=None,
                                     figsize=(8, 8), color="#4c78a8",
                                     line_color="#e45756", style="default",
                                     theme="default", dpi=100, **kwargs) -> MatplotlibAxes:
    """Calibration of predicted quantiles: nominal vs empirical coverage."""
    n = _as_array(nominal_quantiles); e = _as_array(empirical_quantiles)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Quantile Calibration",
                             xlabel="nominal", ylabel="empirical", figsize=figsize)
        fig.set_dpi(dpi)
        ax.plot([0, 1], [0, 1], color=line_color, linestyle="--", label="ideal")
        ax.plot(n, e, color=color, marker="o", **kwargs)
        ax.set_xlim(0, 1); ax.set_ylim(0, 1)
        ax.legend(); ax.grid(True, alpha=0.3); apply_theme(ax, theme)
    return ax


def quantile_calibration_plot_interactive(nominal_quantiles, empirical_quantiles,
                                          title=None, color="#4c78a8",
                                          line_color="#e45756", template="plotly",
                                          height=600, width=700, **kwargs) -> PlotlyFigure:
    """Interactive quantile calibration."""
    fig = go.Figure([
        go.Scatter(x=[0, 1], y=[0, 1], mode="lines",
                   line=dict(color=line_color, dash="dash"), name="ideal"),
        go.Scatter(x=_as_array(nominal_quantiles), y=_as_array(empirical_quantiles),
                   mode="lines+markers", line=dict(color=color), name="model", **kwargs),
    ])
    fig.update_layout(title=title or "Quantile Calibration", template=template,
                      height=height, width=width, xaxis_title="nominal",
                      yaxis_title="empirical",
                      xaxis=dict(range=[0, 1]), yaxis=dict(range=[0, 1]))
    return fig


def sharpness_vs_coverage_plot_static(sharpness, coverage, model_labels=None,
                                      title=None, figsize=(8, 8), color="#4c78a8",
                                      style="default", theme="default", dpi=100,
                                      **kwargs) -> MatplotlibAxes:
    """Trade-off scatter: interval sharpness vs coverage per model."""
    s = _as_array(sharpness); c = _as_array(coverage)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Sharpness vs Coverage",
                             xlabel="sharpness (avg width)", ylabel="coverage",
                             figsize=figsize)
        fig.set_dpi(dpi)
        ax.scatter(s, c, color=color, s=80, **kwargs)
        if model_labels is not None:
            for xi, yi, lbl in zip(s, c, model_labels):
                ax.annotate(str(lbl), (xi, yi), fontsize=9)
        ax.grid(True, alpha=0.3); apply_theme(ax, theme)
    return ax


def sharpness_vs_coverage_plot_interactive(sharpness, coverage, model_labels=None,
                                           title=None, color="#4c78a8",
                                           template="plotly", height=650, width=750,
                                           **kwargs) -> PlotlyFigure:
    """Interactive sharpness vs coverage."""
    fig = go.Figure([go.Scatter(x=_as_array(sharpness), y=_as_array(coverage),
                                mode="markers+text" if model_labels else "markers",
                                text=list(model_labels) if model_labels is not None else None,
                                textposition="top center",
                                marker=dict(color=color, size=12), **kwargs)])
    fig.update_layout(title=title or "Sharpness vs Coverage", template=template,
                      height=height, width=width,
                      xaxis_title="sharpness (avg width)", yaxis_title="coverage")
    return fig


def coverage_by_segment_bar_static(segments, coverage, nominal=0.9, title=None,
                                   figsize=(10, 6), color="#4c78a8",
                                   line_color="#e45756", style="default",
                                   theme="default", dpi=100, **kwargs) -> MatplotlibAxes:
    """Empirical coverage per segment with nominal target line."""
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Coverage by Segment",
                             xlabel="segment", ylabel="coverage", figsize=figsize)
        fig.set_dpi(dpi)
        ax.bar(list(segments), _as_array(coverage), color=color, **kwargs)
        ax.axhline(nominal, color=line_color, linestyle="--", label=f"nominal={nominal}")
        ax.set_ylim(0, 1.05); ax.legend(); ax.grid(True, axis="y", alpha=0.3)
        apply_theme(ax, theme)
    return ax


def coverage_by_segment_bar_interactive(segments, coverage, nominal=0.9, title=None,
                                        color="#4c78a8", line_color="#e45756",
                                        template="plotly", height=600, width=1000,
                                        **kwargs) -> PlotlyFigure:
    """Interactive coverage-by-segment bar."""
    fig = go.Figure([go.Bar(x=list(segments), y=_as_array(coverage),
                            marker_color=color, **kwargs)])
    fig.add_hline(y=nominal, line_dash="dash", line_color=line_color,
                  annotation_text=f"nominal={nominal}")
    fig.update_layout(title=title or "Coverage by Segment", template=template,
                      height=height, width=width, xaxis_title="segment",
                      yaxis_title="coverage", yaxis=dict(range=[0, 1.05]))
    return fig


conformal_interval_plot = conformal_interval_plot_static
jackknife_plus_band = jackknife_plus_band_static
quantile_calibration_plot = quantile_calibration_plot_static
sharpness_vs_coverage_plot = sharpness_vs_coverage_plot_static
coverage_by_segment_bar = coverage_by_segment_bar_static
