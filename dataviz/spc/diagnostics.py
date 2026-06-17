"""SPC diagnostics, rule annotation, and defect analysis charts."""

from typing import Optional, Sequence, Tuple

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from ..types import ArrayLike, FigureSize, MatplotlibAxes, PlotlyFigure, SeriesLike
from ..utils import apply_theme, setup_plot, validate_positive_int
from .rules import ControlLimits, as_numeric_series, detect_rule_violations, individuals_limits, violations_by_index


def run_chart_static(
    data: ArrayLike,
    title: str = "Run Chart",
    figsize: FigureSize = (12, 6),
    show_median: bool = True,
    theme: str = "default",
) -> MatplotlibAxes:
    """Create a static run chart with optional median reference.

    Args:
        data (ArrayLike): Ordered process observations.
        title (str): Chart title.
        figsize (FigureSize): Figure size in inches.
        show_median (bool): Whether to draw the median reference line.
        theme (str): Named style theme.

    Returns:
        matplotlib.axes.Axes: Run chart axes.

    Raises:
        TypeError: If data cannot be converted to numeric observations.
        ValueError: If data is empty.

    Examples:
        ```python
        ax = dv.spc.run_chart_static(values)
        ```

    Notes:
        Run charts are useful before estimating formal control limits.
    """
    values = as_numeric_series(data)
    _, ax = setup_plot(figsize=figsize, title=title, xlabel="Sample", ylabel="Value")
    ax.plot(values, marker="o", color="steelblue", label="Process Data")
    if show_median:
        ax.axhline(values.median(), color="orange", linestyle="--", label="Median")
    ax.legend()
    apply_theme(ax, theme)
    return ax


def run_chart_interactive(
    data: ArrayLike,
    title: str = "Run Chart",
    show_median: bool = True,
    template: str = "plotly",
    height: int = 500,
    width: int = 1000,
) -> PlotlyFigure:
    """Create an interactive run chart with optional median reference.

    Args:
        data (ArrayLike): Ordered process observations.
        title (str): Chart title.
        show_median (bool): Whether to draw the median reference line.
        template (str): Plotly template.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.

    Returns:
        plotly.graph_objects.Figure: Interactive run chart.

    Raises:
        TypeError: If data cannot be converted to numeric observations.
        ValueError: If data is empty.

    Examples:
        ```python
        fig = dv.spc.run_chart_interactive(values)
        ```

    Notes:
        The median line is added as a Plotly horizontal shape.
    """
    values = as_numeric_series(data)
    fig = go.Figure(data=[go.Scatter(y=values, mode="lines+markers", name="Process Data")])
    if show_median:
        fig.add_hline(y=float(values.median()), line_color="orange", line_dash="dash", annotation_text="Median")
    fig.update_layout(title=title, xaxis_title="Sample", yaxis_title="Value", template=template, height=height, width=width)
    return fig


def rule_violation_chart_static(
    data: ArrayLike,
    limits: Optional[ControlLimits] = None,
    title: str = "SPC Rule Violation Chart",
    figsize: FigureSize = (12, 6),
    theme: str = "default",
) -> MatplotlibAxes:
    """Create a static control chart that highlights detected rule violations.

    Args:
        data (ArrayLike): Process observations.
        limits (Optional[ControlLimits]): Optional precomputed control limits.
        title (str): Chart title.
        figsize (FigureSize): Figure size in inches.
        theme (str): Named style theme.

    Returns:
        matplotlib.axes.Axes: Rule-annotated control chart axes.

    Raises:
        TypeError: If data cannot be converted to numeric observations.
        ValueError: If data is empty or limits are invalid.

    Examples:
        ```python
        ax = dv.spc.rule_violation_chart_static(values)
        ```

    Notes:
        Detected rules include beyond-limits points, long center-line runs, and monotonic trends.
    """
    values = as_numeric_series(data)
    limits = limits or individuals_limits(values)
    violations = detect_rule_violations(values, limits=limits)
    grouped = violations_by_index(violations)
    _, ax = setup_plot(figsize=figsize, title=title, xlabel="Sample", ylabel="Value")
    ax.plot(values, marker="o", color="steelblue", label="Process Data")
    ax.axhline(limits.center, color="green", label="Center")
    ax.axhline(limits.upper, color="red", linestyle="--", label="UCL")
    ax.axhline(limits.lower, color="red", linestyle="--", label="LCL")
    if grouped:
        indexes = sorted(grouped)
        ax.scatter(indexes, values.iloc[indexes], color="crimson", s=80, zorder=3, label="Rule Violation")
        for idx in indexes:
            labels = ",".join(sorted({v.rule for v in grouped[idx]}))
            ax.annotate(labels, (idx, values.iloc[idx]), textcoords="offset points", xytext=(5, 8), fontsize=8)
    ax.legend()
    apply_theme(ax, theme)
    return ax


def rule_violation_chart_interactive(
    data: ArrayLike,
    limits: Optional[ControlLimits] = None,
    title: str = "SPC Rule Violation Chart",
    template: str = "plotly",
    height: int = 500,
    width: int = 1000,
) -> PlotlyFigure:
    """Create an interactive control chart that highlights detected rule violations.

    Args:
        data (ArrayLike): Process observations.
        limits (Optional[ControlLimits]): Optional precomputed control limits.
        title (str): Chart title.
        template (str): Plotly template.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.

    Returns:
        plotly.graph_objects.Figure: Interactive rule-annotated control chart.

    Raises:
        TypeError: If data cannot be converted to numeric observations.
        ValueError: If data is empty or limits are invalid.

    Examples:
        ```python
        fig = dv.spc.rule_violation_chart_interactive(values)
        ```

    Notes:
        Rule names are included in the hover text for highlighted points.
    """
    values = as_numeric_series(data)
    limits = limits or individuals_limits(values)
    violations = detect_rule_violations(values, limits=limits)
    grouped = violations_by_index(violations)
    fig = go.Figure()
    fig.add_trace(go.Scatter(y=values, mode="lines+markers", name="Process Data"))
    if grouped:
        indexes = sorted(grouped)
        hover = ["<br>".join(v.message for v in grouped[idx]) for idx in indexes]
        fig.add_trace(go.Scatter(x=indexes, y=values.iloc[indexes], mode="markers", name="Rule Violation", marker=dict(color="crimson", size=11), text=hover, hovertemplate="%{text}<extra></extra>"))
    fig.add_hline(y=limits.center, line_color="green", annotation_text="Center")
    fig.add_hline(y=limits.upper, line_color="red", line_dash="dash", annotation_text="UCL")
    fig.add_hline(y=limits.lower, line_color="red", line_dash="dash", annotation_text="LCL")
    fig.update_layout(title=title, xaxis_title="Sample", yaxis_title="Value", template=template, height=height, width=width)
    return fig


def pareto_chart_static(
    categories: Sequence[str],
    counts: ArrayLike,
    title: str = "Pareto Chart",
    figsize: FigureSize = (12, 6),
    theme: str = "default",
) -> MatplotlibAxes:
    """Create a static Pareto chart for defect categories.

    Args:
        categories (Sequence[str]): Defect category labels.
        counts (ArrayLike): Defect counts for each category.
        title (str): Chart title.
        figsize (FigureSize): Figure size in inches.
        theme (str): Named style theme.

    Returns:
        matplotlib.axes.Axes: Pareto chart primary axes.

    Raises:
        TypeError: If counts cannot be converted to numeric values.
        ValueError: If categories and counts lengths differ.

    Examples:
        ```python
        ax = dv.spc.pareto_chart_static(["Scratch", "Dent"], [12, 5])
        ```

    Notes:
        Bars are sorted descending and the secondary axis shows cumulative percent.
    """
    values = as_numeric_series(counts, name="Count")
    if len(categories) != len(values):
        raise ValueError("categories and counts must have the same length.")
    frame = pd.DataFrame({"category": categories, "count": values}).sort_values("count", ascending=False)
    cumulative = frame["count"].cumsum() / frame["count"].sum() * 100
    _, ax = setup_plot(figsize=figsize, title=title, xlabel="Category", ylabel="Count")
    ax.bar(frame["category"], frame["count"], color="steelblue")
    ax.tick_params(axis="x", rotation=45)
    ax2 = ax.twinx()
    ax2.plot(frame["category"], cumulative, color="crimson", marker="o", label="Cumulative %")
    ax2.set_ylabel("Cumulative %")
    ax2.set_ylim(0, 105)
    apply_theme(ax, theme)
    return ax


def pareto_chart_interactive(
    categories: Sequence[str],
    counts: ArrayLike,
    title: str = "Pareto Chart",
    template: str = "plotly",
    height: int = 600,
    width: int = 1000,
) -> PlotlyFigure:
    """Create an interactive Pareto chart for defect categories.

    Args:
        categories (Sequence[str]): Defect category labels.
        counts (ArrayLike): Defect counts for each category.
        title (str): Chart title.
        template (str): Plotly template.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.

    Returns:
        plotly.graph_objects.Figure: Interactive Pareto chart.

    Raises:
        TypeError: If counts cannot be converted to numeric values.
        ValueError: If categories and counts lengths differ.

    Examples:
        ```python
        fig = dv.spc.pareto_chart_interactive(categories, counts)
        ```

    Notes:
        Cumulative percent is plotted against the right y-axis.
    """
    values = as_numeric_series(counts, name="Count")
    if len(categories) != len(values):
        raise ValueError("categories and counts must have the same length.")
    frame = pd.DataFrame({"category": categories, "count": values}).sort_values("count", ascending=False)
    cumulative = frame["count"].cumsum() / frame["count"].sum() * 100
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Bar(x=frame["category"], y=frame["count"], name="Count"), secondary_y=False)
    fig.add_trace(go.Scatter(x=frame["category"], y=cumulative, mode="lines+markers", name="Cumulative %"), secondary_y=True)
    fig.update_layout(title=title, template=template, height=height, width=width)
    fig.update_yaxes(title_text="Count", secondary_y=False)
    fig.update_yaxes(title_text="Cumulative %", range=[0, 105], secondary_y=True)
    return fig


def process_distribution_static(
    data: ArrayLike,
    bins: int = 30,
    title: str = "Process Distribution",
    figsize: FigureSize = (12, 6),
    theme: str = "default",
) -> MatplotlibAxes:
    """Create a static process distribution histogram with sigma bands.

    Args:
        data (ArrayLike): Process observations.
        bins (int): Number of histogram bins.
        title (str): Chart title.
        figsize (FigureSize): Figure size in inches.
        theme (str): Named style theme.

    Returns:
        matplotlib.axes.Axes: Process distribution axes.

    Raises:
        TypeError: If data cannot be converted to numeric observations.
        ValueError: If bins is invalid.

    Examples:
        ```python
        ax = dv.spc.process_distribution_static(values)
        ```

    Notes:
        Vertical lines mark mean and plus/minus one, two, and three sigma.
    """
    validate_positive_int(bins, "bins")
    values = as_numeric_series(data)
    mean = values.mean()
    std = values.std(ddof=1)
    _, ax = setup_plot(figsize=figsize, title=title, xlabel="Value", ylabel="Frequency")
    ax.hist(values, bins=bins, color="steelblue", alpha=0.7, edgecolor="black")
    ax.axvline(mean, color="green", linewidth=2, label="Mean")
    for multiplier in (1, 2, 3):
        ax.axvline(mean + multiplier * std, color="red", linestyle="--", alpha=0.6)
        ax.axvline(mean - multiplier * std, color="red", linestyle="--", alpha=0.6)
    ax.legend()
    apply_theme(ax, theme)
    return ax


def process_distribution_interactive(
    data: ArrayLike,
    bins: int = 30,
    title: str = "Process Distribution",
    template: str = "plotly",
    height: int = 600,
    width: int = 1000,
) -> PlotlyFigure:
    """Create an interactive process distribution histogram with sigma bands.

    Args:
        data (ArrayLike): Process observations.
        bins (int): Number of histogram bins.
        title (str): Chart title.
        template (str): Plotly template.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.

    Returns:
        plotly.graph_objects.Figure: Interactive process distribution chart.

    Raises:
        TypeError: If data cannot be converted to numeric observations.
        ValueError: If bins is invalid.

    Examples:
        ```python
        fig = dv.spc.process_distribution_interactive(values)
        ```

    Notes:
        Sigma bands are shown as vertical reference lines.
    """
    validate_positive_int(bins, "bins")
    values = as_numeric_series(data)
    mean = float(values.mean())
    std = float(values.std(ddof=1))
    fig = go.Figure(data=[go.Histogram(x=values, nbinsx=bins, name="Observed")])
    fig.add_vline(x=mean, line_color="green", annotation_text="Mean")
    for multiplier in (1, 2, 3):
        fig.add_vline(x=mean + multiplier * std, line_color="red", line_dash="dash", annotation_text=f"+{multiplier} sigma")
        fig.add_vline(x=mean - multiplier * std, line_color="red", line_dash="dash", annotation_text=f"-{multiplier} sigma")
    fig.update_layout(title=title, xaxis_title="Value", yaxis_title="Frequency", template=template, height=height, width=width)
    return fig


def zone_chart_static(
    data: ArrayLike,
    title: str = "Zone Chart",
    figsize: FigureSize = (12, 6),
    theme: str = "default",
) -> MatplotlibAxes:
    """Create a static zone chart with one-, two-, and three-sigma bands.

    Args:
        data (ArrayLike): Process observations.
        title (str): Chart title.
        figsize (FigureSize): Figure size in inches.
        theme (str): Named style theme.

    Returns:
        matplotlib.axes.Axes: Zone chart axes.

    Raises:
        TypeError: If data cannot be converted to numeric observations.
        ValueError: If data is empty.

    Examples:
        ```python
        ax = dv.spc.zone_chart_static(values)
        ```

    Notes:
        Zones give a visual reading of how far points sit from the center line.
    """
    values = as_numeric_series(data)
    mean = values.mean()
    std = values.std(ddof=1)
    _, ax = setup_plot(figsize=figsize, title=title, xlabel="Sample", ylabel="Value")
    colors = ["#e8f4ff", "#fff4d6", "#ffe4e4"]
    for multiplier, color in zip((1, 2, 3), colors):
        ax.axhspan(mean - multiplier * std, mean + multiplier * std, color=color, zorder=0)
    ax.plot(values, marker="o", color="steelblue", label="Process Data")
    ax.axhline(mean, color="green", label="Center")
    ax.legend()
    apply_theme(ax, theme)
    return ax


def zone_chart_interactive(
    data: ArrayLike,
    title: str = "Zone Chart",
    template: str = "plotly",
    height: int = 500,
    width: int = 1000,
) -> PlotlyFigure:
    """Create an interactive zone chart with one-, two-, and three-sigma bands.

    Args:
        data (ArrayLike): Process observations.
        title (str): Chart title.
        template (str): Plotly template.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.

    Returns:
        plotly.graph_objects.Figure: Interactive zone chart.

    Raises:
        TypeError: If data cannot be converted to numeric observations.
        ValueError: If data is empty.

    Examples:
        ```python
        fig = dv.spc.zone_chart_interactive(values)
        ```

    Notes:
        Plotly zones are rendered as horizontal rectangle shapes.
    """
    values = as_numeric_series(data)
    mean = float(values.mean())
    std = float(values.std(ddof=1))
    fig = go.Figure(data=[go.Scatter(y=values, mode="lines+markers", name="Process Data")])
    for multiplier, color in zip((3, 2, 1), ("rgba(255, 228, 228, 0.5)", "rgba(255, 244, 214, 0.5)", "rgba(232, 244, 255, 0.5)")):
        fig.add_hrect(y0=mean - multiplier * std, y1=mean + multiplier * std, fillcolor=color, line_width=0, layer="below")
    fig.add_hline(y=mean, line_color="green", annotation_text="Center")
    fig.update_layout(title=title, xaxis_title="Sample", yaxis_title="Value", template=template, height=height, width=width)
    return fig
