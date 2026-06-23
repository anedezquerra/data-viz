"""Spatial and panel residual charts."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from ..types import MatplotlibAxes, PlotlyFigure
from ..utils import setup_plot, apply_theme
from .helpers import _as_array


def spatial_residual_map_static(longitudes, latitudes, residuals, title=None,
                                figsize=(10, 7), cmap="coolwarm", style="default",
                                theme="default", dpi=100, **kwargs) -> MatplotlibAxes:
    """Geographic residual scatter coloured by residual sign and magnitude."""
    r = _as_array(residuals); vmax = np.max(np.abs(r)) if r.size else 1.0
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Spatial Residual Map",
                             xlabel="longitude", ylabel="latitude", figsize=figsize)
        fig.set_dpi(dpi)
        sc = ax.scatter(_as_array(longitudes), _as_array(latitudes), c=r, cmap=cmap,
                        vmin=-vmax, vmax=vmax, s=30, **kwargs)
        fig.colorbar(sc, ax=ax, label="residual"); ax.grid(True, alpha=0.3); apply_theme(ax, theme)
    return ax


def spatial_residual_map_interactive(longitudes, latitudes, residuals, title=None,
                                     colorscale="RdBu", template="plotly", height=650,
                                     width=1000, **kwargs) -> PlotlyFigure:
    """Interactive spatial residual map (Cartesian)."""
    r = _as_array(residuals); vmax = float(np.max(np.abs(r))) if r.size else 1.0
    fig = go.Figure([go.Scatter(x=_as_array(longitudes), y=_as_array(latitudes),
                                mode="markers",
                                marker=dict(color=r, colorscale=colorscale, cmin=-vmax,
                                            cmax=vmax, showscale=True,
                                            colorbar=dict(title="residual")), **kwargs)])
    fig.update_layout(title=title or "Spatial Residual Map", template=template,
                      height=height, width=width,
                      xaxis_title="longitude", yaxis_title="latitude")
    return fig


def moran_scatter_static(values, spatial_lag, title=None, figsize=(8, 8),
                         color="#4c78a8", style="default", theme="default",
                         dpi=100, **kwargs) -> MatplotlibAxes:
    """Moran scatter: standardised value vs spatial lag."""
    v = _as_array(values); sl = _as_array(spatial_lag)
    vz = (v - v.mean()) / (v.std() + 1e-12)
    sz = (sl - sl.mean()) / (sl.std() + 1e-12)
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Moran Scatter", xlabel="z(value)",
                             ylabel="z(spatial lag)", figsize=figsize)
        fig.set_dpi(dpi)
        ax.scatter(vz, sz, color=color, alpha=0.7, **kwargs)
        ax.axhline(0, color="#888", linestyle="--"); ax.axvline(0, color="#888", linestyle="--")
        if vz.size > 1:
            slope = np.polyfit(vz, sz, 1)[0]
            xs = np.linspace(vz.min(), vz.max(), 50)
            ax.plot(xs, slope * xs, color="#e45756", label=f"I ≈ {slope:.2f}")
            ax.legend()
        ax.grid(True, alpha=0.3); apply_theme(ax, theme)
    return ax


def moran_scatter_interactive(values, spatial_lag, title=None, color="#4c78a8",
                              template="plotly", height=650, width=750,
                              **kwargs) -> PlotlyFigure:
    """Interactive Moran scatter."""
    v = _as_array(values); sl = _as_array(spatial_lag)
    vz = (v - v.mean()) / (v.std() + 1e-12); sz = (sl - sl.mean()) / (sl.std() + 1e-12)
    fig = go.Figure([go.Scatter(x=vz, y=sz, mode="markers",
                                marker=dict(color=color), name="data", **kwargs)])
    if vz.size > 1:
        slope = float(np.polyfit(vz, sz, 1)[0])
        xs = np.linspace(vz.min(), vz.max(), 50)
        fig.add_trace(go.Scatter(x=xs, y=slope * xs, mode="lines",
                                 line=dict(color="#e45756"), name=f"I ≈ {slope:.2f}"))
    fig.add_hline(y=0, line_dash="dash", line_color="#888")
    fig.add_vline(x=0, line_dash="dash", line_color="#888")
    fig.update_layout(title=title or "Moran Scatter", template=template,
                      height=height, width=width,
                      xaxis_title="z(value)", yaxis_title="z(spatial lag)")
    return fig


def panel_residual_heatmap_static(matrix, unit_labels=None, time_labels=None,
                                  title=None, figsize=(11, 7), cmap="coolwarm",
                                  style="default", theme="default", dpi=100,
                                  **kwargs) -> MatplotlibAxes:
    """Heatmap of residuals across panel units (rows) and time (cols)."""
    m = np.asarray(matrix, dtype=float)
    vmax = np.nanmax(np.abs(m)) if m.size else 1.0
    with plt.style.context(style):
        fig, ax = setup_plot(title=title or "Panel Residual Heatmap",
                             xlabel="time", ylabel="unit", figsize=figsize)
        fig.set_dpi(dpi)
        im = ax.imshow(m, aspect="auto", cmap=cmap, vmin=-vmax, vmax=vmax, **kwargs)
        if unit_labels is not None:
            ax.set_yticks(range(len(unit_labels))); ax.set_yticklabels(unit_labels)
        if time_labels is not None:
            ax.set_xticks(range(len(time_labels))); ax.set_xticklabels(time_labels, rotation=45)
        fig.colorbar(im, ax=ax, label="residual"); apply_theme(ax, theme)
    return ax


def panel_residual_heatmap_interactive(matrix, unit_labels=None, time_labels=None,
                                       title=None, colorscale="RdBu", template="plotly",
                                       height=700, width=1100, **kwargs) -> PlotlyFigure:
    """Interactive panel residual heatmap."""
    m = np.asarray(matrix, dtype=float)
    vmax = float(np.nanmax(np.abs(m))) if m.size else 1.0
    fig = go.Figure([go.Heatmap(z=m, x=time_labels, y=unit_labels, zmin=-vmax,
                                zmax=vmax, colorscale=colorscale,
                                colorbar=dict(title="residual"), **kwargs)])
    fig.update_layout(title=title or "Panel Residual Heatmap", template=template,
                      height=height, width=width, xaxis_title="time", yaxis_title="unit")
    return fig


spatial_residual_map = spatial_residual_map_static
moran_scatter = moran_scatter_static
panel_residual_heatmap = panel_residual_heatmap_static
