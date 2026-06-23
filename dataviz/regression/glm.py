"""Generalized linear model diagnostic charts."""

from __future__ import annotations

from typing import Optional

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from ..types import ArrayLike, FigureSize, MatplotlibAxes, MatplotlibFigure, PlotlyFigure
from ..utils import setup_plot, apply_theme
from .helpers import _as_array


def _link_eta(mu: np.ndarray, link: str) -> np.ndarray:
    if link == "identity": return mu
    if link == "log": return np.log(np.clip(mu, 1e-12, None))
    if link == "logit":
        p = np.clip(mu, 1e-12, 1 - 1e-12); return np.log(p / (1 - p))
    if link == "inverse": return 1.0 / np.where(mu == 0, 1e-12, mu)
    if link == "sqrt": return np.sqrt(np.clip(mu, 0, None))
    raise ValueError(f"unknown link {link!r}")


def _variance(mu: np.ndarray, family: str) -> np.ndarray:
    if family == "gaussian": return np.ones_like(mu)
    if family == "poisson": return np.clip(mu, 1e-12, None)
    if family == "binomial": return np.clip(mu * (1 - mu), 1e-12, None)
    if family == "gamma": return mu ** 2
    if family == "inverse_gaussian": return mu ** 3
    raise ValueError(f"unknown family {family!r}")


def _deviance_resid(y, mu, family):
    eps = 1e-12
    if family == "gaussian":
        return y - mu
    if family == "poisson":
        m = np.clip(mu, eps, None)
        term = np.where(y > 0, y * np.log(y / m), 0.0) - (y - m)
        return np.sign(y - m) * np.sqrt(2 * term)
    if family == "binomial":
        m = np.clip(mu, eps, 1 - eps)
        a = np.where(y > 0, y * np.log(y / m), 0.0)
        b = np.where(y < 1, (1 - y) * np.log((1 - y) / (1 - m)), 0.0)
        return np.sign(y - m) * np.sqrt(2 * (a + b))
    if family == "gamma":
        m = np.clip(mu, eps, None)
        return np.sign(y - m) * np.sqrt(2 * (-np.log(y / m) + (y - m) / m))
    if family == "inverse_gaussian":
        m = np.clip(mu, eps, None)
        return np.sign(y - m) * np.sqrt((y - m) ** 2 / (y * m ** 2))
    raise ValueError(f"unknown family {family!r}")


# ---- link function plot ----

def link_function_plot_static(y_true, mu, link="log", title=None, figsize=(10, 6),
                              color="#4c78a8", grid=True, theme="default",
                              dpi=100, style="default", **kwargs) -> MatplotlibAxes:
    """Scatter of linear predictor η vs response y_true (binned mean optional)."""
    y = _as_array(y_true); m = _as_array(mu)
    eta = _link_eta(m, link)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or f"Link Function ({link})",
                             xlabel="η = link(μ)", ylabel="y", figsize=figsize)
        fig.set_dpi(dpi)
        ax.scatter(eta, y, color=color, alpha=0.6, **kwargs)
        if grid: ax.grid(True, alpha=0.3)
        apply_theme(ax, theme)
    return ax


def link_function_plot_interactive(y_true, mu, link="log", title=None,
                                   color="#4c78a8", template="plotly",
                                   height=600, width=1000, **kwargs) -> PlotlyFigure:
    """Interactive link-function diagnostic scatter."""
    y = _as_array(y_true); m = _as_array(mu)
    eta = _link_eta(m, link)
    fig = go.Figure([go.Scatter(x=eta, y=y, mode="markers",
                                marker=dict(color=color), **kwargs)])
    fig.update_layout(title=title or f"Link Function ({link})",
                      xaxis_title="η = link(μ)", yaxis_title="y",
                      template=template, height=height, width=width)
    return fig


# ---- deviance residual plot ----

def deviance_residual_plot_static(y_true, mu, family="poisson", title=None,
                                  figsize=(10, 6), color="#4c78a8", grid=True,
                                  theme="default", dpi=100, style="default",
                                  **kwargs) -> MatplotlibAxes:
    """Deviance residuals vs fitted μ for a GLM family."""
    d = _deviance_resid(_as_array(y_true), _as_array(mu), family)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or f"Deviance Residuals ({family})",
                             xlabel="μ", ylabel="Deviance residual", figsize=figsize)
        fig.set_dpi(dpi)
        ax.scatter(_as_array(mu), d, color=color, alpha=0.7, **kwargs)
        ax.axhline(0, color="#e45756", linestyle="--", linewidth=1)
        if grid: ax.grid(True, alpha=0.3)
        apply_theme(ax, theme)
    return ax


def deviance_residual_plot_interactive(y_true, mu, family="poisson", title=None,
                                       color="#4c78a8", template="plotly",
                                       height=600, width=1000, **kwargs) -> PlotlyFigure:
    """Interactive deviance-residual scatter."""
    d = _deviance_resid(_as_array(y_true), _as_array(mu), family)
    fig = go.Figure([go.Scatter(x=_as_array(mu), y=d, mode="markers",
                                marker=dict(color=color), **kwargs)])
    fig.add_hline(y=0, line_dash="dash", line_color="#e45756")
    fig.update_layout(title=title or f"Deviance Residuals ({family})",
                      xaxis_title="μ", yaxis_title="Deviance residual",
                      template=template, height=height, width=width)
    return fig


# ---- pearson residual plot ----

def pearson_residual_plot_static(y_true, mu, family="poisson", title=None,
                                 figsize=(10, 6), color="#4c78a8", grid=True,
                                 theme="default", dpi=100, style="default",
                                 **kwargs) -> MatplotlibAxes:
    """Pearson residuals (y-μ)/√V(μ) vs fitted μ."""
    y, m = _as_array(y_true), _as_array(mu)
    pr = (y - m) / np.sqrt(_variance(m, family))
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or f"Pearson Residuals ({family})",
                             xlabel="μ", ylabel="Pearson residual", figsize=figsize)
        fig.set_dpi(dpi)
        ax.scatter(m, pr, color=color, alpha=0.7, **kwargs)
        ax.axhline(0, color="#e45756", linestyle="--", linewidth=1)
        if grid: ax.grid(True, alpha=0.3)
        apply_theme(ax, theme)
    return ax


def pearson_residual_plot_interactive(y_true, mu, family="poisson", title=None,
                                      color="#4c78a8", template="plotly",
                                      height=600, width=1000, **kwargs) -> PlotlyFigure:
    """Interactive Pearson residuals."""
    y, m = _as_array(y_true), _as_array(mu)
    pr = (y - m) / np.sqrt(_variance(m, family))
    fig = go.Figure([go.Scatter(x=m, y=pr, mode="markers",
                                marker=dict(color=color), **kwargs)])
    fig.add_hline(y=0, line_dash="dash", line_color="#e45756")
    fig.update_layout(title=title or f"Pearson Residuals ({family})",
                      xaxis_title="μ", yaxis_title="Pearson residual",
                      template=template, height=height, width=width)
    return fig


# ---- working residual plot ----

def working_residual_plot_static(y_true, mu, link="log", title=None,
                                 figsize=(10, 6), color="#4c78a8", grid=True,
                                 theme="default", dpi=100, style="default",
                                 **kwargs) -> MatplotlibAxes:
    """Working residuals (y - μ)·g'(μ) vs linear predictor η."""
    y, m = _as_array(y_true), _as_array(mu)
    eta = _link_eta(m, link)
    if link == "log": dlink = 1.0 / np.clip(m, 1e-12, None)
    elif link == "logit": dlink = 1.0 / np.clip(m * (1 - m), 1e-12, None)
    elif link == "inverse": dlink = -1.0 / np.where(m == 0, 1e-12, m) ** 2
    elif link == "sqrt": dlink = 0.5 / np.sqrt(np.clip(m, 1e-12, None))
    else: dlink = np.ones_like(m)
    wr = (y - m) * dlink
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or f"Working Residuals ({link})",
                             xlabel="η", ylabel="Working residual", figsize=figsize)
        fig.set_dpi(dpi)
        ax.scatter(eta, wr, color=color, alpha=0.7, **kwargs)
        ax.axhline(0, color="#e45756", linestyle="--", linewidth=1)
        if grid: ax.grid(True, alpha=0.3)
        apply_theme(ax, theme)
    return ax


def working_residual_plot_interactive(y_true, mu, link="log", title=None,
                                      color="#4c78a8", template="plotly",
                                      height=600, width=1000, **kwargs) -> PlotlyFigure:
    """Interactive working-residual chart."""
    y, m = _as_array(y_true), _as_array(mu)
    eta = _link_eta(m, link)
    dlink = {"log": 1 / np.clip(m, 1e-12, None),
             "logit": 1 / np.clip(m * (1 - m), 1e-12, None),
             "inverse": -1 / np.where(m == 0, 1e-12, m) ** 2,
             "sqrt": 0.5 / np.sqrt(np.clip(m, 1e-12, None))}.get(link, np.ones_like(m))
    wr = (y - m) * dlink
    fig = go.Figure([go.Scatter(x=eta, y=wr, mode="markers",
                                marker=dict(color=color), **kwargs)])
    fig.add_hline(y=0, line_dash="dash", line_color="#e45756")
    fig.update_layout(title=title or f"Working Residuals ({link})",
                      xaxis_title="η", yaxis_title="Working residual",
                      template=template, height=height, width=width)
    return fig


# ---- variance function plot ----

def variance_function_plot_static(mu, family="poisson", title=None, figsize=(10, 6),
                                  color="#4c78a8", grid=True, theme="default",
                                  dpi=100, style="default", **kwargs) -> MatplotlibAxes:
    """Plot Var(y|μ) = V(μ) for the chosen GLM family across μ values."""
    m = _as_array(mu); order = np.argsort(m)
    v = _variance(m, family)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or f"Variance Function ({family})",
                             xlabel="μ", ylabel="V(μ)", figsize=figsize)
        fig.set_dpi(dpi)
        ax.plot(m[order], v[order], color=color, linewidth=2, **kwargs)
        if grid: ax.grid(True, alpha=0.3)
        apply_theme(ax, theme)
    return ax


def variance_function_plot_interactive(mu, family="poisson", title=None,
                                       color="#4c78a8", template="plotly",
                                       height=600, width=900, **kwargs) -> PlotlyFigure:
    """Interactive variance-function curve."""
    m = _as_array(mu); order = np.argsort(m)
    v = _variance(m, family)
    fig = go.Figure([go.Scatter(x=m[order], y=v[order], mode="lines",
                                line=dict(color=color, width=2), **kwargs)])
    fig.update_layout(title=title or f"Variance Function ({family})",
                      xaxis_title="μ", yaxis_title="V(μ)",
                      template=template, height=height, width=width)
    return fig


# ---- glm diagnostic panel ----

def glm_diagnostic_panel_static(y_true, mu, family="poisson", link="log",
                                title=None, figsize=(12, 9), color="#4c78a8",
                                line_color="#e45756", theme="default", dpi=100,
                                style="default") -> MatplotlibFigure:
    """Four-panel GLM diagnostics: deviance, Pearson, working, link."""
    y, m = _as_array(y_true), _as_array(mu)
    d = _deviance_resid(y, m, family)
    pr = (y - m) / np.sqrt(_variance(m, family))
    eta = _link_eta(m, link)
    with plt.style.context(style):
        fig, axes = plt.subplots(2, 2, figsize=figsize, dpi=dpi)
        ((a, b), (c, d_ax)) = axes
        if title: fig.suptitle(title, fontsize=14)
        a.scatter(m, d, color=color, alpha=0.7); a.axhline(0, color=line_color, linestyle="--")
        a.set_title("Deviance Residuals"); a.set_xlabel("μ"); a.set_ylabel("dev res")
        b.scatter(m, pr, color=color, alpha=0.7); b.axhline(0, color=line_color, linestyle="--")
        b.set_title("Pearson Residuals"); b.set_xlabel("μ"); b.set_ylabel("Pearson res")
        c.scatter(eta, y, color=color, alpha=0.6); c.set_title(f"Link ({link})")
        c.set_xlabel("η"); c.set_ylabel("y")
        d_ax.scatter(m, y - m, color=color, alpha=0.7); d_ax.axhline(0, color=line_color, linestyle="--")
        d_ax.set_title("Raw residual"); d_ax.set_xlabel("μ"); d_ax.set_ylabel("y-μ")
        for ax_ in axes.ravel(): ax_.grid(True, alpha=0.3); apply_theme(ax_, theme)
        fig.tight_layout()
    return fig


def glm_diagnostic_panel_interactive(y_true, mu, family="poisson", link="log",
                                     title=None, color="#4c78a8",
                                     line_color="#e45756", template="plotly",
                                     height=850, width=1100) -> PlotlyFigure:
    """Interactive GLM diagnostic panel."""
    y, m = _as_array(y_true), _as_array(mu)
    d = _deviance_resid(y, m, family)
    pr = (y - m) / np.sqrt(_variance(m, family))
    eta = _link_eta(m, link)
    fig = make_subplots(rows=2, cols=2, subplot_titles=(
        "Deviance Residuals", "Pearson Residuals", f"Link ({link})", "Raw residual"))
    fig.add_trace(go.Scatter(x=m, y=d, mode="markers", marker=dict(color=color),
                             showlegend=False), row=1, col=1)
    fig.add_trace(go.Scatter(x=m, y=pr, mode="markers", marker=dict(color=color),
                             showlegend=False), row=1, col=2)
    fig.add_trace(go.Scatter(x=eta, y=y, mode="markers", marker=dict(color=color),
                             showlegend=False), row=2, col=1)
    fig.add_trace(go.Scatter(x=m, y=y - m, mode="markers", marker=dict(color=color),
                             showlegend=False), row=2, col=2)
    for r, c in ((1, 1), (1, 2), (2, 2)):
        fig.add_hline(y=0, line_dash="dash", line_color=line_color, row=r, col=c)
    fig.update_layout(title=title or "GLM Diagnostics", template=template,
                      height=height, width=width)
    return fig


# aliases
link_function_plot = link_function_plot_static
deviance_residual_plot = deviance_residual_plot_static
pearson_residual_plot = pearson_residual_plot_static
working_residual_plot = working_residual_plot_static
variance_function_plot = variance_function_plot_static
glm_diagnostic_panel = glm_diagnostic_panel_static
