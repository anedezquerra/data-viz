"""Bayesian-regression diagnostic charts."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from ..types import MatplotlibAxes, MatplotlibFigure, PlotlyFigure
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


def posterior_coefficient_density_static(samples_per_coef, coef_names=None, title=None,
                                         figsize=(10, 6), cmap="viridis",
                                         style="default", theme="default", dpi=100,
                                         **kwargs) -> MatplotlibAxes:
    """Overlay posterior KDEs of coefficient samples."""
    cmap_obj = plt.get_cmap(cmap)
    names = list(coef_names) if coef_names is not None else [f"β{i}" for i in range(len(samples_per_coef))]
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Posterior Coefficient Densities",
                             xlabel="value", ylabel="density", figsize=figsize)
        fig.set_dpi(dpi)
        for i, s in enumerate(samples_per_coef):
            xs, ys = _kde(s)
            ax.plot(xs, ys, color=cmap_obj(i / max(len(samples_per_coef) - 1, 1)),
                    label=names[i], **kwargs)
        ax.legend(); ax.grid(True, alpha=0.3); apply_theme(ax, theme)
    return ax


def posterior_coefficient_density_interactive(samples_per_coef, coef_names=None,
                                              title=None, template="plotly",
                                              height=600, width=1000,
                                              **kwargs) -> PlotlyFigure:
    """Interactive posterior coefficient densities."""
    names = list(coef_names) if coef_names is not None else [f"β{i}" for i in range(len(samples_per_coef))]
    fig = go.Figure()
    for i, s in enumerate(samples_per_coef):
        xs, ys = _kde(s)
        fig.add_trace(go.Scatter(x=xs, y=ys, mode="lines", name=names[i], **kwargs))
    fig.update_layout(title=title or "Posterior Coefficient Densities",
                      template=template, height=height, width=width,
                      xaxis_title="value", yaxis_title="density")
    return fig


def posterior_predictive_check_static(y_true, y_predictive_samples, title=None,
                                      figsize=(10, 6), pred_color="#a8c5e0",
                                      true_color="#e45756", bins=30, style="default",
                                      theme="default", dpi=100,
                                      **kwargs) -> MatplotlibAxes:
    """Overlay densities of posterior-predictive draws vs observed y."""
    samples = np.asarray(y_predictive_samples, dtype=float)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Posterior Predictive Check",
                             xlabel="y", ylabel="density", figsize=figsize)
        fig.set_dpi(dpi)
        n_draws = samples.shape[0] if samples.ndim == 2 else 1
        for k in range(min(n_draws, 50)):
            row = samples[k] if samples.ndim == 2 else samples
            xs, ys = _kde(row)
            ax.plot(xs, ys, color=pred_color, alpha=0.3, **kwargs)
        xs, ys = _kde(_as_array(y_true))
        ax.plot(xs, ys, color=true_color, linewidth=2, label="observed")
        ax.legend(); ax.grid(True, alpha=0.3); apply_theme(ax, theme)
    return ax


def posterior_predictive_check_interactive(y_true, y_predictive_samples, title=None,
                                           pred_color="rgba(168,197,224,0.3)",
                                           true_color="#e45756", template="plotly",
                                           height=600, width=1000,
                                           **kwargs) -> PlotlyFigure:
    """Interactive posterior predictive check."""
    samples = np.asarray(y_predictive_samples, dtype=float)
    fig = go.Figure()
    n_draws = samples.shape[0] if samples.ndim == 2 else 1
    for k in range(min(n_draws, 50)):
        row = samples[k] if samples.ndim == 2 else samples
        xs, ys = _kde(row)
        fig.add_trace(go.Scatter(x=xs, y=ys, mode="lines",
                                 line=dict(color=pred_color), showlegend=False, **kwargs))
    xs, ys = _kde(_as_array(y_true))
    fig.add_trace(go.Scatter(x=xs, y=ys, mode="lines",
                             line=dict(color=true_color, width=2), name="observed"))
    fig.update_layout(title=title or "Posterior Predictive Check",
                      template=template, height=height, width=width,
                      xaxis_title="y", yaxis_title="density")
    return fig


def trace_plot_coefficients_static(traces, coef_names=None, title=None,
                                   figsize=(11, 6), cmap="viridis", style="default",
                                   theme="default", dpi=100, **kwargs) -> MatplotlibAxes:
    """MCMC trace lines for each coefficient."""
    cmap_obj = plt.get_cmap(cmap)
    names = list(coef_names) if coef_names is not None else [f"β{i}" for i in range(len(traces))]
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Trace Plot",
                             xlabel="iteration", ylabel="value", figsize=figsize)
        fig.set_dpi(dpi)
        for i, t in enumerate(traces):
            ax.plot(_as_array(t), color=cmap_obj(i / max(len(traces) - 1, 1)),
                    label=names[i], alpha=0.7, **kwargs)
        ax.legend(); ax.grid(True, alpha=0.3); apply_theme(ax, theme)
    return ax


def trace_plot_coefficients_interactive(traces, coef_names=None, title=None,
                                        template="plotly", height=600, width=1100,
                                        **kwargs) -> PlotlyFigure:
    """Interactive MCMC trace plot."""
    names = list(coef_names) if coef_names is not None else [f"β{i}" for i in range(len(traces))]
    fig = go.Figure()
    for i, t in enumerate(traces):
        fig.add_trace(go.Scatter(y=_as_array(t), mode="lines",
                                 name=names[i], **kwargs))
    fig.update_layout(title=title or "Trace Plot", template=template,
                      height=height, width=width,
                      xaxis_title="iteration", yaxis_title="value")
    return fig


def credible_interval_forest_static(coef_names, means, lower, upper, title=None,
                                    figsize=(10, 7), color="#4c78a8",
                                    style="default", theme="default", dpi=100,
                                    **kwargs) -> MatplotlibAxes:
    """Forest plot of credible intervals per coefficient."""
    n = list(coef_names); mu = _as_array(means)
    lo, hi = _as_array(lower), _as_array(upper)
    pos = np.arange(len(n))
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Credible Intervals",
                             xlabel="value", ylabel="coefficient", figsize=figsize)
        fig.set_dpi(dpi)
        ax.errorbar(mu, pos, xerr=[mu - lo, hi - mu], fmt="o", color=color, **kwargs)
        ax.axvline(0, color="#888", linestyle="--")
        ax.set_yticks(pos); ax.set_yticklabels(n)
        ax.grid(True, axis="x", alpha=0.3); apply_theme(ax, theme)
    return ax


def credible_interval_forest_interactive(coef_names, means, lower, upper, title=None,
                                         color="#4c78a8", template="plotly",
                                         height=700, width=1000, **kwargs) -> PlotlyFigure:
    """Interactive credible-interval forest."""
    mu = _as_array(means); lo, hi = _as_array(lower), _as_array(upper)
    fig = go.Figure([go.Scatter(x=mu, y=list(coef_names), mode="markers",
                                marker=dict(color=color, size=10),
                                error_x=dict(type="data", symmetric=False,
                                             array=hi - mu, arrayminus=mu - lo),
                                **kwargs)])
    fig.add_vline(x=0, line_dash="dash", line_color="#888")
    fig.update_layout(title=title or "Credible Intervals", template=template,
                      height=height, width=width,
                      xaxis_title="value", yaxis_title="coefficient")
    return fig


posterior_coefficient_density = posterior_coefficient_density_static
posterior_predictive_check = posterior_predictive_check_static
trace_plot_coefficients = trace_plot_coefficients_static
credible_interval_forest = credible_interval_forest_static
