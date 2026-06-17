"""Dashboard-style univariate analysis figures."""

from typing import Optional

import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy import stats

from ..types import FigureSize, MatplotlibFigure, PlotlyFigure, SeriesLike
from ..utils import apply_theme, validate_positive_int
from .robust import robust_summary
from .stats import as_numeric_series, percentile_table, univariate_summary


def univariate_analysis_dashboard_static(
    data: SeriesLike,
    bins: int = 30,
    title: Optional[str] = None,
    figsize: FigureSize = (14, 10),
    color: Optional[str] = None,
    theme: str = "default",
) -> MatplotlibFigure:
    """Create a static multi-panel univariate analysis dashboard.

    Args:
        data (SeriesLike): Input observations.
        bins (int): Number of histogram bins.
        title (Optional[str]): Optional figure title.
        figsize (FigureSize): Matplotlib figure size.
        color (Optional[str]): Primary plot color.
        theme (str): Styling theme name.

    Returns:
        matplotlib.figure.Figure: Figure containing distribution, box, QQ, ECDF, percentile, and robust summaries.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If ``bins`` is invalid or no observations remain.

    Examples:
        ```python
        fig = univariate_analysis_dashboard_static(data)
        ```

    Notes:
        This dashboard is intended as a broad first-pass profile for one numeric variable.
    """
    validate_positive_int(bins, "bins")
    values = as_numeric_series(data)
    summary = univariate_summary(values)
    robust = robust_summary(values)
    fig, axes = plt.subplots(2, 3, figsize=figsize)
    fig.suptitle(title or f"Univariate Analysis Dashboard (n={summary.count})")
    axes[0, 0].hist(values, bins=bins, color=color, alpha=0.7, edgecolor="black")
    axes[0, 0].axvline(summary.mean, color="crimson", linestyle="--", label="Mean")
    axes[0, 0].axvline(summary.median, color="black", linestyle=":", label="Median")
    axes[0, 0].set_title("Distribution")
    axes[0, 0].legend()
    axes[0, 1].boxplot(values, vert=True)
    axes[0, 1].set_title("Spread")
    theoretical, ordered = stats.probplot(values.to_numpy(dtype=float), dist="norm", fit=False)
    axes[0, 2].scatter(theoretical, ordered, color=color)
    axes[0, 2].set_title("Normal QQ")
    sorted_values = np.sort(values.to_numpy(dtype=float))
    probabilities = np.arange(1, len(sorted_values) + 1) / len(sorted_values)
    axes[1, 0].step(sorted_values, probabilities, where="post", color=color)
    axes[1, 0].set_title("ECDF")
    table = percentile_table(values, step=10)
    axes[1, 1].plot(table["percentile"], table["value"], marker="o", color=color)
    axes[1, 1].set_title("Percentiles")
    labels = ["Mean", "Median", "Trimmed", "Winsorized"]
    locations = [summary.mean, summary.median, robust.trimmed_mean, robust.winsorized_mean]
    axes[1, 2].bar(labels, locations, color=color)
    axes[1, 2].set_title("Location Estimates")
    for ax in axes.ravel():
        ax.grid(True, alpha=0.3)
        apply_theme(ax, theme)
    fig.tight_layout()
    return fig


def univariate_analysis_dashboard_interactive(
    data: SeriesLike,
    bins: int = 30,
    title: Optional[str] = None,
    color: Optional[str] = None,
    template: str = "plotly",
    height: int = 900,
    width: int = 1200,
) -> PlotlyFigure:
    """Create an interactive multi-panel univariate analysis dashboard.

    Args:
        data (SeriesLike): Input observations.
        bins (int): Number of histogram bins.
        title (Optional[str]): Optional figure title.
        color (Optional[str]): Primary plot color.
        template (str): Plotly template name.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.

    Returns:
        plotly.graph_objects.Figure: Interactive univariate analysis dashboard.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If ``bins`` is invalid or no observations remain.

    Examples:
        ```python
        fig = univariate_analysis_dashboard_interactive(data)
        ```

    Notes:
        The dashboard combines distribution shape, spread, normality, and robust-location diagnostics.
    """
    validate_positive_int(bins, "bins")
    values = as_numeric_series(data)
    summary = univariate_summary(values)
    robust = robust_summary(values)
    theoretical, ordered = stats.probplot(values.to_numpy(dtype=float), dist="norm", fit=False)
    sorted_values = np.sort(values.to_numpy(dtype=float))
    probabilities = np.arange(1, len(sorted_values) + 1) / len(sorted_values)
    table = percentile_table(values, step=10)
    fig = make_subplots(
        rows=2,
        cols=3,
        subplot_titles=("Distribution", "Spread", "Normal QQ", "ECDF", "Percentiles", "Location Estimates"),
    )
    fig.add_trace(go.Histogram(x=values, nbinsx=bins, marker_color=color, name="Distribution"), row=1, col=1)
    fig.add_trace(go.Box(y=values, marker_color=color, name="Spread"), row=1, col=2)
    fig.add_trace(go.Scatter(x=theoretical, y=ordered, mode="markers", marker=dict(color=color), name="QQ"), row=1, col=3)
    fig.add_trace(go.Scatter(x=sorted_values, y=probabilities, mode="lines", line=dict(color=color, shape="hv"), name="ECDF"), row=2, col=1)
    fig.add_trace(go.Scatter(x=table["percentile"], y=table["value"], mode="lines+markers", line=dict(color=color), name="Percentiles"), row=2, col=2)
    fig.add_trace(
        go.Bar(
            x=["Mean", "Median", "Trimmed", "Winsorized"],
            y=[summary.mean, summary.median, robust.trimmed_mean, robust.winsorized_mean],
            marker_color=color,
            name="Location",
        ),
        row=2,
        col=3,
    )
    fig.update_layout(
        title=title or f"Univariate Analysis Dashboard (n={summary.count})",
        template=template,
        height=height,
        width=width,
        showlegend=False,
    )
    return fig

