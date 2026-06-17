"""SPC dashboard views."""

import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from ..types import ArrayLike, FigureSize, MatplotlibFigure, PlotlyFigure
from ..utils import apply_theme, validate_positive_int
from .rules import as_numeric_series, detect_rule_violations, individuals_limits, moving_ranges


def spc_dashboard_static(
    data: ArrayLike,
    span: int = 2,
    bins: int = 30,
    title: str = "SPC Dashboard",
    figsize: FigureSize = (14, 10),
    theme: str = "default",
) -> MatplotlibFigure:
    """Create a static SPC dashboard with control, range, distribution, and rule panels.

    Args:
        data (ArrayLike): Process observations.
        span (int): Moving range span.
        bins (int): Number of histogram bins.
        title (str): Figure title.
        figsize (FigureSize): Figure size in inches.
        theme (str): Named style theme.

    Returns:
        matplotlib.figure.Figure: Dashboard figure.

    Raises:
        TypeError: If data cannot be converted to numeric observations.
        ValueError: If span or bins are invalid.

    Examples:
        ```python
        fig = dv.spc.spc_dashboard_static(values)
        ```

    Notes:
        The dashboard is intended for quick process screening rather than formal reporting.
    """
    validate_positive_int(bins, "bins")
    values = as_numeric_series(data)
    limits = individuals_limits(values)
    ranges = moving_ranges(values, span=span)
    violations = detect_rule_violations(values, limits=limits)
    fig, axes = plt.subplots(2, 2, figsize=figsize)
    fig.suptitle(title)
    axes[0, 0].plot(values, marker="o", color="steelblue")
    axes[0, 0].axhline(limits.center, color="green")
    axes[0, 0].axhline(limits.upper, color="red", linestyle="--")
    axes[0, 0].axhline(limits.lower, color="red", linestyle="--")
    axes[0, 0].set_title("Individuals")
    axes[0, 1].plot(ranges, marker="o", color="orange")
    axes[0, 1].set_title(f"Moving Range ({span})")
    axes[1, 0].hist(values, bins=bins, color="steelblue", alpha=0.75, edgecolor="black")
    axes[1, 0].axvline(limits.center, color="green")
    axes[1, 0].set_title("Distribution")
    axes[1, 1].bar(["Violations", "Observations"], [len(violations), len(values)], color=["crimson", "gray"])
    axes[1, 1].set_title("Rule Summary")
    for ax in axes.ravel():
        apply_theme(ax, theme)
    fig.tight_layout()
    return fig


def spc_dashboard_interactive(
    data: ArrayLike,
    span: int = 2,
    bins: int = 30,
    title: str = "SPC Dashboard",
    template: str = "plotly",
    height: int = 800,
    width: int = 1100,
) -> PlotlyFigure:
    """Create an interactive SPC dashboard with control, range, distribution, and rule panels.

    Args:
        data (ArrayLike): Process observations.
        span (int): Moving range span.
        bins (int): Number of histogram bins.
        title (str): Figure title.
        template (str): Plotly template.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.

    Returns:
        plotly.graph_objects.Figure: Interactive dashboard figure.

    Raises:
        TypeError: If data cannot be converted to numeric observations.
        ValueError: If span or bins are invalid.

    Examples:
        ```python
        fig = dv.spc.spc_dashboard_interactive(values)
        ```

    Notes:
        Rule summary counts use the default SPC rule detector.
    """
    validate_positive_int(bins, "bins")
    values = as_numeric_series(data)
    limits = individuals_limits(values)
    ranges = moving_ranges(values, span=span)
    violations = detect_rule_violations(values, limits=limits)
    fig = make_subplots(rows=2, cols=2, subplot_titles=("Individuals", f"Moving Range ({span})", "Distribution", "Rule Summary"))
    fig.add_trace(go.Scatter(y=values, mode="lines+markers", name="Process Data"), row=1, col=1)
    fig.add_trace(go.Scatter(y=ranges, mode="lines+markers", name="Moving Range"), row=1, col=2)
    fig.add_trace(go.Histogram(x=values, nbinsx=bins, name="Distribution"), row=2, col=1)
    fig.add_trace(go.Bar(x=["Violations", "Observations"], y=[len(violations), len(values)], name="Summary"), row=2, col=2)
    fig.add_hline(y=limits.center, line_color="green", row=1, col=1)
    fig.add_hline(y=limits.upper, line_color="red", line_dash="dash", row=1, col=1)
    fig.add_hline(y=limits.lower, line_color="red", line_dash="dash", row=1, col=1)
    fig.update_layout(title=title, template=template, height=height, width=width, showlegend=False)
    return fig
