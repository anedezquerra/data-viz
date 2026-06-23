"""Domain-specific regression charts (economics, biology, finance)."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from ..types import MatplotlibAxes, PlotlyFigure
from ..utils import setup_plot, apply_theme
from .helpers import _as_array


def price_elasticity_curve_static(price, quantity, fitted_curve=None, title=None,
                                  figsize=(10, 6), color="#4c78a8",
                                  line_color="#e45756", style="default",
                                  theme="default", dpi=100, **kwargs) -> MatplotlibAxes:
    """Price vs quantity scatter with elasticity fit overlay."""
    p, q = _as_array(price), _as_array(quantity)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Price Elasticity",
                             xlabel="price", ylabel="quantity", figsize=figsize)
        fig.set_dpi(dpi)
        ax.scatter(p, q, color=color, alpha=0.7, **kwargs)
        if fitted_curve is not None:
            order = np.argsort(p)
            ax.plot(p[order], _as_array(fitted_curve)[order], color=line_color, linewidth=2)
        ax.grid(True, alpha=0.3); apply_theme(ax, theme)
    return ax


def price_elasticity_curve_interactive(price, quantity, fitted_curve=None, title=None,
                                       color="#4c78a8", line_color="#e45756",
                                       template="plotly", height=600, width=1000,
                                       **kwargs) -> PlotlyFigure:
    """Interactive price-elasticity curve."""
    p, q = _as_array(price), _as_array(quantity)
    fig = go.Figure([go.Scatter(x=p, y=q, mode="markers",
                                marker=dict(color=color), name="data", **kwargs)])
    if fitted_curve is not None:
        order = np.argsort(p)
        fig.add_trace(go.Scatter(x=p[order], y=_as_array(fitted_curve)[order],
                                 mode="lines", line=dict(color=line_color, width=2),
                                 name="fit"))
    fig.update_layout(title=title or "Price Elasticity", template=template,
                      height=height, width=width, xaxis_title="price", yaxis_title="quantity")
    return fig


def dose_response_curve_static(dose, response, lower=None, upper=None, title=None,
                               figsize=(10, 6), color="#4c78a8",
                               band_color="#a8c5e0", style="default", theme="default",
                               dpi=100, **kwargs) -> MatplotlibAxes:
    """Dose vs response curve with optional CI band, log-x scale."""
    d, r = _as_array(dose), _as_array(response)
    order = np.argsort(d)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Dose–Response",
                             xlabel="dose (log)", ylabel="response", figsize=figsize)
        fig.set_dpi(dpi)
        if lower is not None and upper is not None:
            ax.fill_between(d[order], _as_array(lower)[order], _as_array(upper)[order],
                            color=band_color, alpha=0.4)
        ax.plot(d[order], r[order], color=color, marker="o", **kwargs)
        ax.set_xscale("log"); ax.grid(True, alpha=0.3, which="both"); apply_theme(ax, theme)
    return ax


def dose_response_curve_interactive(dose, response, lower=None, upper=None, title=None,
                                    color="#4c78a8",
                                    band_color="rgba(168,197,224,0.4)",
                                    template="plotly", height=600, width=1000,
                                    **kwargs) -> PlotlyFigure:
    """Interactive dose-response curve."""
    d, r = _as_array(dose), _as_array(response)
    order = np.argsort(d)
    fig = go.Figure()
    if lower is not None and upper is not None:
        fig.add_trace(go.Scatter(x=d[order], y=_as_array(upper)[order], mode="lines",
                                 line=dict(width=0), showlegend=False))
        fig.add_trace(go.Scatter(x=d[order], y=_as_array(lower)[order], mode="lines",
                                 line=dict(width=0), fill="tonexty",
                                 fillcolor=band_color, name="CI"))
    fig.add_trace(go.Scatter(x=d[order], y=r[order], mode="lines+markers",
                             line=dict(color=color), name="response", **kwargs))
    fig.update_layout(title=title or "Dose–Response", template=template,
                      height=height, width=width, xaxis_type="log",
                      xaxis_title="dose (log)", yaxis_title="response")
    return fig


def demand_forecast_fan_chart_static(time, central, quantile_bands, title=None,
                                     figsize=(11, 6), color="#4c78a8",
                                     cmap="Blues", style="default", theme="default",
                                     dpi=100, **kwargs) -> MatplotlibAxes:
    """Fan chart for demand forecast with multiple quantile bands.

    ``quantile_bands`` is a list of (lower, upper) array pairs ordered widest→narrowest.
    """
    t = _as_array(time); c = _as_array(central)
    cmap_obj = plt.get_cmap(cmap)
    n = len(quantile_bands)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Demand Forecast Fan",
                             xlabel="time", ylabel="demand", figsize=figsize)
        fig.set_dpi(dpi)
        for i, (lo, hi) in enumerate(quantile_bands):
            ax.fill_between(t, _as_array(lo), _as_array(hi),
                            color=cmap_obj(0.3 + 0.6 * (i + 1) / max(n, 1)), alpha=0.6)
        ax.plot(t, c, color=color, linewidth=2, label="central", **kwargs)
        ax.legend(); ax.grid(True, alpha=0.3); apply_theme(ax, theme)
    return ax


def demand_forecast_fan_chart_interactive(time, central, quantile_bands, title=None,
                                          color="#4c78a8", colorscale="Blues",
                                          template="plotly", height=600, width=1100,
                                          **kwargs) -> PlotlyFigure:
    """Interactive demand-forecast fan chart."""
    t = _as_array(time); c = _as_array(central)
    n = len(quantile_bands)
    fig = go.Figure()
    for i, (lo, hi) in enumerate(quantile_bands):
        shade = 0.2 + 0.6 * (i + 1) / max(n, 1)
        fig.add_trace(go.Scatter(x=t, y=_as_array(hi), mode="lines",
                                 line=dict(width=0), showlegend=False))
        fig.add_trace(go.Scatter(x=t, y=_as_array(lo), mode="lines", line=dict(width=0),
                                 fill="tonexty",
                                 fillcolor=f"rgba(70,130,180,{shade:.2f})",
                                 name=f"band {i + 1}"))
    fig.add_trace(go.Scatter(x=t, y=c, mode="lines",
                             line=dict(color=color, width=2), name="central", **kwargs))
    fig.update_layout(title=title or "Demand Forecast Fan", template=template,
                      height=height, width=width,
                      xaxis_title="time", yaxis_title="demand")
    return fig


def yield_curve_fit_plot_static(maturities, observed_yields, fitted_yields, title=None,
                                figsize=(10, 6), obs_color="#4c78a8",
                                fit_color="#e45756", style="default", theme="default",
                                dpi=100, **kwargs) -> MatplotlibAxes:
    """Observed vs fitted bond yield curve."""
    m = _as_array(maturities)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Yield Curve Fit",
                             xlabel="maturity", ylabel="yield", figsize=figsize)
        fig.set_dpi(dpi)
        ax.scatter(m, _as_array(observed_yields), color=obs_color, label="observed", **kwargs)
        order = np.argsort(m)
        ax.plot(m[order], _as_array(fitted_yields)[order], color=fit_color,
                linewidth=2, label="fitted")
        ax.legend(); ax.grid(True, alpha=0.3); apply_theme(ax, theme)
    return ax


def yield_curve_fit_plot_interactive(maturities, observed_yields, fitted_yields,
                                     title=None, obs_color="#4c78a8",
                                     fit_color="#e45756", template="plotly",
                                     height=600, width=1000, **kwargs) -> PlotlyFigure:
    """Interactive yield-curve fit."""
    m = _as_array(maturities); order = np.argsort(m)
    fig = go.Figure([
        go.Scatter(x=m, y=_as_array(observed_yields), mode="markers",
                   marker=dict(color=obs_color, size=8), name="observed", **kwargs),
        go.Scatter(x=m[order], y=_as_array(fitted_yields)[order], mode="lines",
                   line=dict(color=fit_color, width=2), name="fitted"),
    ])
    fig.update_layout(title=title or "Yield Curve Fit", template=template,
                      height=height, width=width,
                      xaxis_title="maturity", yaxis_title="yield")
    return fig


price_elasticity_curve = price_elasticity_curve_static
dose_response_curve = dose_response_curve_static
demand_forecast_fan_chart = demand_forecast_fan_chart_static
yield_curve_fit_plot = yield_curve_fit_plot_static
