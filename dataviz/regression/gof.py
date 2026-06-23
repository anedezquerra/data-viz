"""Goodness-of-fit and residual statistical-test charts."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from ..types import MatplotlibAxes, MatplotlibFigure, PlotlyFigure
from ..utils import setup_plot, apply_theme
from .helpers import (
    _as_array, _as_matrix, breusch_pagan_statistic, white_test_statistic,
    durbin_watson_statistic, ljung_box_statistic, jarque_bera_statistic, _chi2_sf,
)
from .residual_extended import _normal_quantiles


# ---- normality test panel ----

def normality_test_panel_static(residuals, title=None, figsize=(12, 5),
                                color="#4c78a8", line_color="#e45756",
                                style="default", theme="default", dpi=100,
                                bins=30) -> MatplotlibFigure:
    """Normality panel: histogram + Q-Q + Jarque–Bera annotation."""
    r = _as_array(residuals)
    jb, p = jarque_bera_statistic(r)
    with plt.style.context(style):
        fig, (a, b) = plt.subplots(1, 2, figsize=figsize, dpi=dpi)
        if title: fig.suptitle(title, fontsize=14)
        a.hist(r, bins=bins, color=color, edgecolor="white"); a.set_title("Residual histogram")
        a.set_xlabel("residual"); a.set_ylabel("count")
        rs = np.sort(r); n = len(rs)
        tq = _normal_quantiles(n)
        b.scatter(tq, rs, color=color, alpha=0.6)
        lo, hi = float(np.min(tq)), float(np.max(tq))
        b.plot([lo, hi], [np.mean(rs) + np.std(rs) * lo, np.mean(rs) + np.std(rs) * hi],
               color=line_color, linestyle="--")
        b.set_title(f"Q-Q (JB={jb:.2f}, p={p:.3f})")
        b.set_xlabel("theoretical"); b.set_ylabel("sample")
        for ax_ in (a, b): ax_.grid(True, alpha=0.3); apply_theme(ax_, theme)
        fig.tight_layout()
    return fig


def normality_test_panel_interactive(residuals, title=None, color="#4c78a8",
                                     line_color="#e45756", template="plotly",
                                     height=500, width=1100, nbins=30) -> PlotlyFigure:
    """Interactive normality panel."""
    r = _as_array(residuals); jb, p = jarque_bera_statistic(r)
    rs = np.sort(r); n = len(rs); tq = _normal_quantiles(n)
    fig = make_subplots(rows=1, cols=2, subplot_titles=(
        "Residual histogram", f"Q-Q (JB={jb:.2f}, p={p:.3f})"))
    fig.add_trace(go.Histogram(x=r, nbinsx=nbins, marker_color=color,
                               showlegend=False), row=1, col=1)
    fig.add_trace(go.Scatter(x=tq, y=rs, mode="markers",
                             marker=dict(color=color), showlegend=False), row=1, col=2)
    mu, sd = float(np.mean(rs)), float(np.std(rs))
    fig.add_trace(go.Scatter(x=[tq.min(), tq.max()],
                             y=[mu + sd * tq.min(), mu + sd * tq.max()],
                             mode="lines", line=dict(color=line_color, dash="dash"),
                             showlegend=False), row=1, col=2)
    fig.update_layout(title=title or "Normality Test Panel", template=template,
                      height=height, width=width)
    return fig


# ---- breusch-pagan ----

def breusch_pagan_plot_static(X, residuals, title=None, figsize=(10, 6),
                              color="#4c78a8", style="default", theme="default",
                              dpi=100, **kwargs) -> MatplotlibAxes:
    """Squared residuals vs fitted with BP statistic annotation."""
    Xm = _as_matrix(X); r = _as_array(residuals)
    bp, p = breusch_pagan_statistic(Xm, r)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or f"Breusch–Pagan (LM={bp:.2f}, p={p:.3f})",
                             xlabel="obs index", ylabel="r²", figsize=figsize)
        fig.set_dpi(dpi)
        ax.scatter(np.arange(len(r)), r ** 2, color=color, alpha=0.7, **kwargs)
        ax.grid(True, alpha=0.3); apply_theme(ax, theme)
    return ax


def breusch_pagan_plot_interactive(X, residuals, title=None, color="#4c78a8",
                                   template="plotly", height=600, width=1000,
                                   **kwargs) -> PlotlyFigure:
    """Interactive BP scatter."""
    Xm = _as_matrix(X); r = _as_array(residuals)
    bp, p = breusch_pagan_statistic(Xm, r)
    fig = go.Figure([go.Scatter(x=np.arange(len(r)), y=r ** 2, mode="markers",
                                marker=dict(color=color), **kwargs)])
    fig.update_layout(title=title or f"Breusch–Pagan (LM={bp:.2f}, p={p:.3f})",
                      template=template, height=height, width=width,
                      xaxis_title="obs index", yaxis_title="r²")
    return fig


# ---- white ----

def white_test_plot_static(X, residuals, title=None, figsize=(10, 6), color="#4c78a8",
                           style="default", theme="default", dpi=100,
                           **kwargs) -> MatplotlibAxes:
    """White-test scatter of r² vs predictor index with statistic annotation."""
    Xm = _as_matrix(X); r = _as_array(residuals)
    w, p = white_test_statistic(Xm, r)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or f"White (LM={w:.2f}, p={p:.3f})",
                             xlabel="obs index", ylabel="r²", figsize=figsize)
        fig.set_dpi(dpi)
        ax.scatter(np.arange(len(r)), r ** 2, color=color, alpha=0.7, **kwargs)
        ax.grid(True, alpha=0.3); apply_theme(ax, theme)
    return ax


def white_test_plot_interactive(X, residuals, title=None, color="#4c78a8",
                                template="plotly", height=600, width=1000,
                                **kwargs) -> PlotlyFigure:
    """Interactive White-test scatter."""
    Xm = _as_matrix(X); r = _as_array(residuals)
    w, p = white_test_statistic(Xm, r)
    fig = go.Figure([go.Scatter(x=np.arange(len(r)), y=r ** 2, mode="markers",
                                marker=dict(color=color), **kwargs)])
    fig.update_layout(title=title or f"White (LM={w:.2f}, p={p:.3f})",
                      template=template, height=height, width=width,
                      xaxis_title="obs index", yaxis_title="r²")
    return fig


# ---- durbin-watson gauge ----

def _dw_gauge_values(dw):
    # 0 (positive autocorr) .. 2 (none) .. 4 (negative)
    return dw


def durbin_watson_gauge_static(residuals, title=None, figsize=(8, 5),
                               color="#4c78a8", style="default", theme="default",
                               dpi=100, **kwargs) -> MatplotlibAxes:
    """Horizontal gauge for Durbin–Watson statistic in [0, 4]."""
    dw = durbin_watson_statistic(_as_array(residuals))
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or f"Durbin–Watson = {dw:.3f}",
                             xlabel="DW", ylabel="", figsize=figsize)
        fig.set_dpi(dpi)
        ax.barh([0], [4], color="#eee", edgecolor="black", **kwargs)
        ax.axvline(2.0, color="#888", linestyle="--", label="DW=2 (no autocorr)")
        ax.scatter([dw], [0], color=color, s=120, zorder=5)
        ax.set_xlim(0, 4); ax.set_yticks([]); ax.legend(loc="upper right")
        apply_theme(ax, theme)
    return ax


def durbin_watson_gauge_interactive(residuals, title=None, color="#4c78a8",
                                    template="plotly", height=350, width=900,
                                    **kwargs) -> PlotlyFigure:
    """Interactive DW gauge."""
    dw = durbin_watson_statistic(_as_array(residuals))
    fig = go.Figure([go.Bar(x=[4], y=[""], orientation="h",
                            marker_color="#eee", showlegend=False, **kwargs)])
    fig.add_trace(go.Scatter(x=[dw], y=[""], mode="markers",
                             marker=dict(color=color, size=16), name=f"DW={dw:.3f}"))
    fig.add_vline(x=2.0, line_dash="dash", line_color="#888")
    fig.update_layout(title=title or f"Durbin–Watson = {dw:.3f}", template=template,
                      height=height, width=width, xaxis=dict(range=[0, 4]))
    return fig


# ---- ljung-box ----

def ljung_box_plot_static(residuals, lags=20, title=None, figsize=(10, 6),
                          color="#4c78a8", alpha=0.05, style="default",
                          theme="default", dpi=100, **kwargs) -> MatplotlibAxes:
    """Ljung–Box p-values for lags 1..lags."""
    r = _as_array(residuals)
    pvals = []
    for k in range(1, lags + 1):
        q, p = ljung_box_statistic(r, k)
        pvals.append(p)
    pvals = np.asarray(pvals)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Ljung–Box p-values", xlabel="lag",
                             ylabel="p-value", figsize=figsize)
        fig.set_dpi(dpi)
        ax.bar(np.arange(1, lags + 1), pvals, color=color, **kwargs)
        ax.axhline(alpha, color="#e45756", linestyle="--", label=f"α={alpha}")
        ax.legend(); ax.grid(True, axis="y", alpha=0.3); apply_theme(ax, theme)
    return ax


def ljung_box_plot_interactive(residuals, lags=20, title=None, color="#4c78a8",
                               alpha=0.05, template="plotly", height=600, width=1000,
                               **kwargs) -> PlotlyFigure:
    """Interactive Ljung–Box p-values."""
    r = _as_array(residuals)
    pvals = [ljung_box_statistic(r, k)[1] for k in range(1, lags + 1)]
    fig = go.Figure([go.Bar(x=list(range(1, lags + 1)), y=pvals,
                            marker_color=color, **kwargs)])
    fig.add_hline(y=alpha, line_dash="dash", line_color="#e45756",
                  annotation_text=f"α={alpha}")
    fig.update_layout(title=title or "Ljung–Box p-values", template=template,
                      height=height, width=width, xaxis_title="lag", yaxis_title="p-value")
    return fig


# ---- residual dependence test panel ----

def residual_dependence_test_panel_static(X, residuals, title=None, figsize=(12, 9),
                                          color="#4c78a8", style="default",
                                          theme="default", dpi=100) -> MatplotlibFigure:
    """Composite panel: BP, White, DW gauge, Ljung-Box."""
    Xm = _as_matrix(X); r = _as_array(residuals)
    bp, bp_p = breusch_pagan_statistic(Xm, r)
    wt, wt_p = white_test_statistic(Xm, r)
    dw = durbin_watson_statistic(r)
    pvals = [ljung_box_statistic(r, k)[1] for k in range(1, 21)]
    with plt.style.context(style):
        fig, axes = plt.subplots(2, 2, figsize=figsize, dpi=dpi)
        ((a, b), (c, d)) = axes
        if title: fig.suptitle(title, fontsize=14)
        a.scatter(np.arange(len(r)), r ** 2, color=color, alpha=0.6)
        a.set_title(f"BP LM={bp:.2f} (p={bp_p:.3f})"); a.set_xlabel("idx"); a.set_ylabel("r²")
        b.scatter(np.arange(len(r)), r, color=color, alpha=0.6)
        b.set_title(f"White LM={wt:.2f} (p={wt_p:.3f})"); b.set_xlabel("idx"); b.set_ylabel("r")
        c.barh([0], [4], color="#eee"); c.scatter([dw], [0], color=color, s=110)
        c.axvline(2.0, color="#888", linestyle="--"); c.set_xlim(0, 4); c.set_yticks([])
        c.set_title(f"DW = {dw:.3f}")
        d.bar(np.arange(1, 21), pvals, color=color); d.axhline(0.05, color="#e45756", linestyle="--")
        d.set_title("Ljung–Box p"); d.set_xlabel("lag"); d.set_ylabel("p")
        for ax_ in axes.ravel(): ax_.grid(True, alpha=0.3); apply_theme(ax_, theme)
        fig.tight_layout()
    return fig


def residual_dependence_test_panel_interactive(X, residuals, title=None,
                                               color="#4c78a8", template="plotly",
                                               height=850, width=1100) -> PlotlyFigure:
    """Interactive composite residual-dependence panel."""
    Xm = _as_matrix(X); r = _as_array(residuals)
    bp, bp_p = breusch_pagan_statistic(Xm, r)
    wt, wt_p = white_test_statistic(Xm, r)
    dw = durbin_watson_statistic(r)
    pvals = [ljung_box_statistic(r, k)[1] for k in range(1, 21)]
    fig = make_subplots(rows=2, cols=2, subplot_titles=(
        f"BP LM={bp:.2f} (p={bp_p:.3f})", f"White LM={wt:.2f} (p={wt_p:.3f})",
        f"DW = {dw:.3f}", "Ljung–Box p"))
    fig.add_trace(go.Scatter(x=np.arange(len(r)), y=r ** 2, mode="markers",
                             marker=dict(color=color), showlegend=False), row=1, col=1)
    fig.add_trace(go.Scatter(x=np.arange(len(r)), y=r, mode="markers",
                             marker=dict(color=color), showlegend=False), row=1, col=2)
    fig.add_trace(go.Bar(x=[4], y=[""], orientation="h", marker_color="#eee",
                         showlegend=False), row=2, col=1)
    fig.add_trace(go.Scatter(x=[dw], y=[""], mode="markers",
                             marker=dict(color=color, size=14), showlegend=False), row=2, col=1)
    fig.add_trace(go.Bar(x=list(range(1, 21)), y=pvals, marker_color=color,
                         showlegend=False), row=2, col=2)
    fig.add_hline(y=0.05, line_dash="dash", line_color="#e45756", row=2, col=2)
    fig.update_xaxes(range=[0, 4], row=2, col=1)
    fig.update_layout(title=title or "Residual Dependence Tests", template=template,
                      height=height, width=width)
    return fig


normality_test_panel = normality_test_panel_static
breusch_pagan_plot = breusch_pagan_plot_static
white_test_plot = white_test_plot_static
durbin_watson_gauge = durbin_watson_gauge_static
ljung_box_plot = ljung_box_plot_static
residual_dependence_test_panel = residual_dependence_test_panel_static
