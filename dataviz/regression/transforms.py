"""Transform diagnostics (Box–Cox, Yeo–Johnson, log-log, power)."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from ..types import MatplotlibAxes, MatplotlibFigure, PlotlyFigure
from ..utils import setup_plot, apply_theme
from .helpers import _as_array, box_cox_loglikelihood, yeo_johnson_loglikelihood


def boxcox_likelihood_curve_static(y, lambdas=None, title=None, figsize=(10, 6),
                                   color="#4c78a8", style="default", theme="default",
                                   dpi=100, **kwargs) -> MatplotlibAxes:
    """Profile log-likelihood vs λ for Box–Cox."""
    if lambdas is None: lambdas = np.linspace(-2, 2, 81)
    lam = _as_array(lambdas)
    ll = box_cox_loglikelihood(_as_array(y), lam)
    star = float(lam[int(np.argmax(ll))])
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or f"Box–Cox Log-Likelihood (λ*={star:.2f})",
                             xlabel="λ", ylabel="log L", figsize=figsize)
        fig.set_dpi(dpi)
        ax.plot(lam, ll, color=color, **kwargs)
        ax.axvline(star, color="#e45756", linestyle="--", label=f"λ*={star:.2f}")
        ax.legend(); ax.grid(True, alpha=0.3); apply_theme(ax, theme)
    return ax


def boxcox_likelihood_curve_interactive(y, lambdas=None, title=None, color="#4c78a8",
                                        template="plotly", height=600, width=1000,
                                        **kwargs) -> PlotlyFigure:
    """Interactive Box–Cox log-likelihood curve."""
    if lambdas is None: lambdas = np.linspace(-2, 2, 81)
    lam = _as_array(lambdas)
    ll = box_cox_loglikelihood(_as_array(y), lam)
    star = float(lam[int(np.argmax(ll))])
    fig = go.Figure([go.Scatter(x=lam, y=ll, mode="lines",
                                line=dict(color=color), **kwargs)])
    fig.add_vline(x=star, line_dash="dash", line_color="#e45756",
                  annotation_text=f"λ*={star:.2f}")
    fig.update_layout(title=title or f"Box–Cox Log-Likelihood (λ*={star:.2f})",
                      template=template, height=height, width=width,
                      xaxis_title="λ", yaxis_title="log L")
    return fig


def yeojohnson_lambda_search_static(y, lambdas=None, title=None, figsize=(10, 6),
                                    color="#4c78a8", style="default", theme="default",
                                    dpi=100, **kwargs) -> MatplotlibAxes:
    """Yeo–Johnson profile log-likelihood vs λ."""
    if lambdas is None: lambdas = np.linspace(-2, 2, 81)
    lam = _as_array(lambdas)
    ll = yeo_johnson_loglikelihood(_as_array(y), lam)
    star = float(lam[int(np.argmax(ll))])
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or f"Yeo–Johnson Log-Likelihood (λ*={star:.2f})",
                             xlabel="λ", ylabel="log L", figsize=figsize)
        fig.set_dpi(dpi)
        ax.plot(lam, ll, color=color, **kwargs)
        ax.axvline(star, color="#e45756", linestyle="--", label=f"λ*={star:.2f}")
        ax.legend(); ax.grid(True, alpha=0.3); apply_theme(ax, theme)
    return ax


def yeojohnson_lambda_search_interactive(y, lambdas=None, title=None, color="#4c78a8",
                                         template="plotly", height=600, width=1000,
                                         **kwargs) -> PlotlyFigure:
    """Interactive Yeo–Johnson log-likelihood curve."""
    if lambdas is None: lambdas = np.linspace(-2, 2, 81)
    lam = _as_array(lambdas)
    ll = yeo_johnson_loglikelihood(_as_array(y), lam)
    star = float(lam[int(np.argmax(ll))])
    fig = go.Figure([go.Scatter(x=lam, y=ll, mode="lines",
                                line=dict(color=color), **kwargs)])
    fig.add_vline(x=star, line_dash="dash", line_color="#e45756",
                  annotation_text=f"λ*={star:.2f}")
    fig.update_layout(title=title or f"Yeo–Johnson Log-Likelihood (λ*={star:.2f})",
                      template=template, height=height, width=width,
                      xaxis_title="λ", yaxis_title="log L")
    return fig


def log_log_diagnostic_static(x, y, title=None, figsize=(10, 6), color="#4c78a8",
                              line_color="#e45756", style="default", theme="default",
                              dpi=100, **kwargs) -> MatplotlibAxes:
    """Log-log scatter with OLS line on log(x), log(y)."""
    xa, ya = _as_array(x), _as_array(y)
    mask = (xa > 0) & (ya > 0)
    lx, ly = np.log(xa[mask]), np.log(ya[mask])
    slope, inter = np.polyfit(lx, ly, 1) if lx.size > 1 else (0.0, 0.0)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or f"Log-Log (slope={slope:.2f})",
                             xlabel="log x", ylabel="log y", figsize=figsize)
        fig.set_dpi(dpi)
        ax.scatter(lx, ly, color=color, alpha=0.7, **kwargs)
        if lx.size > 1:
            xs = np.linspace(lx.min(), lx.max(), 50)
            ax.plot(xs, slope * xs + inter, color=line_color, linestyle="--")
        ax.grid(True, alpha=0.3); apply_theme(ax, theme)
    return ax


def log_log_diagnostic_interactive(x, y, title=None, color="#4c78a8",
                                   line_color="#e45756", template="plotly",
                                   height=600, width=1000, **kwargs) -> PlotlyFigure:
    """Interactive log-log diagnostic."""
    xa, ya = _as_array(x), _as_array(y)
    mask = (xa > 0) & (ya > 0)
    lx, ly = np.log(xa[mask]), np.log(ya[mask])
    slope, inter = np.polyfit(lx, ly, 1) if lx.size > 1 else (0.0, 0.0)
    fig = go.Figure([go.Scatter(x=lx, y=ly, mode="markers",
                                marker=dict(color=color), name="data", **kwargs)])
    if lx.size > 1:
        xs = np.linspace(lx.min(), lx.max(), 50)
        fig.add_trace(go.Scatter(x=xs, y=slope * xs + inter, mode="lines",
                                 line=dict(color=line_color, dash="dash"),
                                 name=f"slope={slope:.2f}"))
    fig.update_layout(title=title or f"Log-Log (slope={slope:.2f})",
                      template=template, height=height, width=width,
                      xaxis_title="log x", yaxis_title="log y")
    return fig


def power_transform_residual_panel_static(y_pred, residuals_orig, residuals_log,
                                          residuals_sqrt, title=None,
                                          figsize=(12, 4), color="#4c78a8",
                                          line_color="#e45756", style="default",
                                          theme="default", dpi=100) -> MatplotlibFigure:
    """Three-panel residuals-vs-fitted for raw / log / sqrt transforms."""
    yp = _as_array(y_pred)
    with plt.style.context(style):
        fig, (a, b, c) = plt.subplots(1, 3, figsize=figsize, dpi=dpi)
        if title: fig.suptitle(title, fontsize=14)
        for ax_, r, name in ((a, residuals_orig, "raw"),
                             (b, residuals_log, "log"),
                             (c, residuals_sqrt, "sqrt")):
            ax_.scatter(yp, _as_array(r), color=color, alpha=0.6)
            ax_.axhline(0, color=line_color, linestyle="--")
            ax_.set_title(name); ax_.set_xlabel("ŷ"); ax_.set_ylabel("residual")
            ax_.grid(True, alpha=0.3); apply_theme(ax_, theme)
        fig.tight_layout()
    return fig


def power_transform_residual_panel_interactive(y_pred, residuals_orig, residuals_log,
                                               residuals_sqrt, title=None,
                                               color="#4c78a8", line_color="#e45756",
                                               template="plotly", height=450,
                                               width=1200) -> PlotlyFigure:
    """Interactive power-transform residual panel."""
    yp = _as_array(y_pred)
    fig = make_subplots(rows=1, cols=3, subplot_titles=("raw", "log", "sqrt"))
    for i, r in enumerate((residuals_orig, residuals_log, residuals_sqrt), start=1):
        fig.add_trace(go.Scatter(x=yp, y=_as_array(r), mode="markers",
                                 marker=dict(color=color), showlegend=False), row=1, col=i)
        fig.add_hline(y=0, line_dash="dash", line_color=line_color, row=1, col=i)
    fig.update_layout(title=title or "Power Transform Residual Panel", template=template,
                      height=height, width=width)
    return fig


boxcox_likelihood_curve = boxcox_likelihood_curve_static
yeojohnson_lambda_search = yeojohnson_lambda_search_static
log_log_diagnostic = log_log_diagnostic_static
power_transform_residual_panel = power_transform_residual_panel_static
