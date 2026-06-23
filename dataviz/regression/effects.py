"""Marginal-effects and partial-dependence regression charts."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from ..types import MatplotlibAxes, PlotlyFigure
from ..utils import setup_plot, apply_theme
from .helpers import _as_array


def partial_dependence_regression_static(grid, pd_values, title=None, figsize=(10, 6),
                                         color="#4c78a8", feature_name="x",
                                         style="default", theme="default", dpi=100,
                                         **kwargs) -> MatplotlibAxes:
    """Partial dependence curve of predicted target on a single feature."""
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or f"Partial Dependence: {feature_name}",
                             xlabel=feature_name, ylabel="ŷ", figsize=figsize)
        fig.set_dpi(dpi)
        ax.plot(_as_array(grid), _as_array(pd_values), color=color, linewidth=2, **kwargs)
        ax.grid(True, alpha=0.3); apply_theme(ax, theme)
    return ax


def partial_dependence_regression_interactive(grid, pd_values, title=None,
                                              color="#4c78a8", feature_name="x",
                                              template="plotly", height=600,
                                              width=1000, **kwargs) -> PlotlyFigure:
    """Interactive PD curve."""
    fig = go.Figure([go.Scatter(x=_as_array(grid), y=_as_array(pd_values), mode="lines",
                                line=dict(color=color, width=2), **kwargs)])
    fig.update_layout(title=title or f"Partial Dependence: {feature_name}",
                      template=template, height=height, width=width,
                      xaxis_title=feature_name, yaxis_title="ŷ")
    return fig


def ice_plot_regression_static(grid, ice_matrix, title=None, figsize=(10, 6),
                               line_color="#4c78a8", mean_color="#e45756",
                               feature_name="x", style="default", theme="default",
                               dpi=100, alpha=0.15, **kwargs) -> MatplotlibAxes:
    """Individual Conditional Expectation lines with average overlay."""
    g = _as_array(grid); M = np.asarray(ice_matrix, dtype=float)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or f"ICE: {feature_name}",
                             xlabel=feature_name, ylabel="ŷ", figsize=figsize)
        fig.set_dpi(dpi)
        for row in M:
            ax.plot(g, row, color=line_color, alpha=alpha, linewidth=0.7, **kwargs)
        ax.plot(g, M.mean(axis=0), color=mean_color, linewidth=2, label="mean (PD)")
        ax.legend(); ax.grid(True, alpha=0.3); apply_theme(ax, theme)
    return ax


def ice_plot_regression_interactive(grid, ice_matrix, title=None, line_color="#4c78a8",
                                    mean_color="#e45756", feature_name="x",
                                    template="plotly", height=600, width=1000,
                                    opacity=0.15, **kwargs) -> PlotlyFigure:
    """Interactive ICE plot."""
    g = _as_array(grid); M = np.asarray(ice_matrix, dtype=float)
    fig = go.Figure()
    for i, row in enumerate(M):
        fig.add_trace(go.Scatter(x=g, y=row, mode="lines",
                                 line=dict(color=line_color, width=1),
                                 opacity=opacity, showlegend=False, **kwargs))
    fig.add_trace(go.Scatter(x=g, y=M.mean(axis=0), mode="lines",
                             line=dict(color=mean_color, width=3), name="mean (PD)"))
    fig.update_layout(title=title or f"ICE: {feature_name}", template=template,
                      height=height, width=width,
                      xaxis_title=feature_name, yaxis_title="ŷ")
    return fig


def marginal_effects_plot_static(feature_names, effects, ci_lower=None, ci_upper=None,
                                 title=None, figsize=(10, 6), color="#4c78a8",
                                 style="default", theme="default", dpi=100,
                                 **kwargs) -> MatplotlibAxes:
    """Average marginal effect per feature with optional CIs."""
    names = list(feature_names); e = _as_array(effects)
    pos = np.arange(len(names))
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Marginal Effects", xlabel="effect",
                             ylabel="feature", figsize=figsize)
        fig.set_dpi(dpi)
        if ci_lower is not None and ci_upper is not None:
            lo, hi = _as_array(ci_lower), _as_array(ci_upper)
            ax.errorbar(e, pos, xerr=[e - lo, hi - e], fmt="o", color=color, **kwargs)
        else:
            ax.scatter(e, pos, color=color, **kwargs)
        ax.axvline(0, color="#888", linestyle="--")
        ax.set_yticks(pos); ax.set_yticklabels(names)
        ax.grid(True, axis="x", alpha=0.3); apply_theme(ax, theme)
    return ax


def marginal_effects_plot_interactive(feature_names, effects, ci_lower=None,
                                      ci_upper=None, title=None, color="#4c78a8",
                                      template="plotly", height=600, width=1000,
                                      **kwargs) -> PlotlyFigure:
    """Interactive marginal-effects forest."""
    names = list(feature_names); e = _as_array(effects)
    err = None
    if ci_lower is not None and ci_upper is not None:
        lo, hi = _as_array(ci_lower), _as_array(ci_upper)
        err = dict(type="data", symmetric=False, array=hi - e, arrayminus=e - lo)
    fig = go.Figure([go.Scatter(x=e, y=names, mode="markers",
                                marker=dict(color=color, size=10),
                                error_x=err, **kwargs)])
    fig.add_vline(x=0, line_dash="dash", line_color="#888")
    fig.update_layout(title=title or "Marginal Effects", template=template,
                      height=height, width=width,
                      xaxis_title="effect", yaxis_title="feature")
    return fig


def interaction_effect_plot_static(x_grid, curves, curve_labels, title=None,
                                   figsize=(10, 6), cmap="viridis",
                                   feature_name="x", style="default", theme="default",
                                   dpi=100, **kwargs) -> MatplotlibAxes:
    """Conditional ŷ vs x under different levels of a second feature."""
    g = _as_array(x_grid); C = np.asarray(curves, dtype=float)
    cmap_obj = plt.get_cmap(cmap)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Interaction Effect",
                             xlabel=feature_name, ylabel="ŷ", figsize=figsize)
        fig.set_dpi(dpi)
        for i, row in enumerate(C):
            ax.plot(g, row, color=cmap_obj(i / max(len(C) - 1, 1)),
                    label=str(curve_labels[i]), **kwargs)
        ax.legend(); ax.grid(True, alpha=0.3); apply_theme(ax, theme)
    return ax


def interaction_effect_plot_interactive(x_grid, curves, curve_labels, title=None,
                                        feature_name="x", template="plotly",
                                        height=600, width=1000, **kwargs) -> PlotlyFigure:
    """Interactive interaction-effect overlay."""
    g = _as_array(x_grid); C = np.asarray(curves, dtype=float)
    fig = go.Figure()
    for i, row in enumerate(C):
        fig.add_trace(go.Scatter(x=g, y=row, mode="lines",
                                 name=str(curve_labels[i]), **kwargs))
    fig.update_layout(title=title or "Interaction Effect", template=template,
                      height=height, width=width,
                      xaxis_title=feature_name, yaxis_title="ŷ")
    return fig


def conditional_expectation_curve_static(x_grid, ce_values, ci_lower=None,
                                         ci_upper=None, title=None, figsize=(10, 6),
                                         color="#4c78a8", band_color="#a8c5e0",
                                         feature_name="x", style="default",
                                         theme="default", dpi=100, **kwargs) -> MatplotlibAxes:
    """E[Y|x] curve with optional confidence band."""
    g = _as_array(x_grid)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or f"E[Y|{feature_name}]",
                             xlabel=feature_name, ylabel="E[Y|x]", figsize=figsize)
        fig.set_dpi(dpi)
        if ci_lower is not None and ci_upper is not None:
            ax.fill_between(g, _as_array(ci_lower), _as_array(ci_upper),
                            color=band_color, alpha=0.4)
        ax.plot(g, _as_array(ce_values), color=color, linewidth=2, **kwargs)
        ax.grid(True, alpha=0.3); apply_theme(ax, theme)
    return ax


def conditional_expectation_curve_interactive(x_grid, ce_values, ci_lower=None,
                                              ci_upper=None, title=None,
                                              color="#4c78a8",
                                              band_color="rgba(168,197,224,0.4)",
                                              feature_name="x", template="plotly",
                                              height=600, width=1000,
                                              **kwargs) -> PlotlyFigure:
    """Interactive E[Y|x] curve."""
    g = _as_array(x_grid)
    fig = go.Figure()
    if ci_lower is not None and ci_upper is not None:
        fig.add_trace(go.Scatter(x=g, y=_as_array(ci_upper), mode="lines",
                                 line=dict(width=0), showlegend=False))
        fig.add_trace(go.Scatter(x=g, y=_as_array(ci_lower), mode="lines",
                                 line=dict(width=0), fill="tonexty",
                                 fillcolor=band_color, name="CI"))
    fig.add_trace(go.Scatter(x=g, y=_as_array(ce_values), mode="lines",
                             line=dict(color=color, width=2), name="E[Y|x]", **kwargs))
    fig.update_layout(title=title or f"E[Y|{feature_name}]", template=template,
                      height=height, width=width,
                      xaxis_title=feature_name, yaxis_title="E[Y|x]")
    return fig


def elasticity_plot_static(x_grid, elasticity, title=None, figsize=(10, 6),
                           color="#4c78a8", feature_name="x", style="default",
                           theme="default", dpi=100, **kwargs) -> MatplotlibAxes:
    """Elasticity (∂lnŷ/∂lnx) curve."""
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or f"Elasticity wrt {feature_name}",
                             xlabel=feature_name, ylabel="elasticity", figsize=figsize)
        fig.set_dpi(dpi)
        ax.plot(_as_array(x_grid), _as_array(elasticity), color=color, linewidth=2, **kwargs)
        ax.axhline(0, color="#888", linestyle="--"); ax.grid(True, alpha=0.3); apply_theme(ax, theme)
    return ax


def elasticity_plot_interactive(x_grid, elasticity, title=None, color="#4c78a8",
                                feature_name="x", template="plotly", height=600,
                                width=1000, **kwargs) -> PlotlyFigure:
    """Interactive elasticity curve."""
    fig = go.Figure([go.Scatter(x=_as_array(x_grid), y=_as_array(elasticity),
                                mode="lines", line=dict(color=color, width=2), **kwargs)])
    fig.add_hline(y=0, line_dash="dash", line_color="#888")
    fig.update_layout(title=title or f"Elasticity wrt {feature_name}", template=template,
                      height=height, width=width, xaxis_title=feature_name,
                      yaxis_title="elasticity")
    return fig


partial_dependence_regression = partial_dependence_regression_static
ice_plot_regression = ice_plot_regression_static
marginal_effects_plot = marginal_effects_plot_static
interaction_effect_plot = interaction_effect_plot_static
conditional_expectation_curve = conditional_expectation_curve_static
elasticity_plot = elasticity_plot_static
