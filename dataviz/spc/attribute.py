"""Attribute-data SPC charts."""

from typing import Optional

import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go

from ..types import ArrayLike, FigureSize, MatplotlibAxes, PlotlyFigure
from ..utils import apply_theme, setup_plot, validate_positive_int
from .rules import ControlLimits, as_numeric_series


def _attribute_limits(center: float, sigma: float, lower_clip: float = 0.0, upper_clip: Optional[float] = None) -> ControlLimits:
    """Build clipped three-sigma attribute control limits.

    Args:
        center (float): Center-line value.
        sigma (float): Standard-error estimate.
        lower_clip (float): Minimum lower limit value.
        upper_clip (Optional[float]): Optional maximum upper limit value.

    Returns:
        ControlLimits: Clipped attribute control limits.

    Raises:
        TypeError: If values cannot be converted to floats.
        ValueError: If sigma is negative.

    Examples:
        ```python
        limits = _attribute_limits(0.05, 0.01, upper_clip=1.0)
        ```

    Notes:
        Attribute charts often clip lower limits at zero and proportions at one.
    """
    if sigma < 0:
        raise ValueError("sigma must be nonnegative.")
    lower = max(lower_clip, center - 3 * sigma)
    upper = center + 3 * sigma
    if upper_clip is not None:
        upper = min(upper_clip, upper)
    return ControlLimits(center=float(center), lower=float(lower), upper=float(upper), sigma=float(sigma))


def _plot_attribute_static(values: ArrayLike, limits: ControlLimits, title: str, ylabel: str, figsize: FigureSize, theme: str, color: str) -> MatplotlibAxes:
    """Render a static attribute control chart.

    Args:
        values (ArrayLike): Chart values.
        limits (ControlLimits): Control limits to draw.
        title (str): Chart title.
        ylabel (str): Y-axis label.
        figsize (FigureSize): Figure size in inches.
        theme (str): Named style theme.
        color (str): Data line color.

    Returns:
        matplotlib.axes.Axes: Attribute chart axes.

    Raises:
        TypeError: If values cannot be plotted.
        ValueError: If limits are invalid.

    Examples:
        ```python
        ax = _plot_attribute_static(values, limits, "p Chart", "Proportion", (12, 6), "default", "steelblue")
        ```

    Notes:
        This helper keeps all attribute charts visually consistent.
    """
    _, ax = setup_plot(figsize=figsize, title=title, xlabel="Sample", ylabel=ylabel)
    ax.plot(values, marker="o", color=color, label=ylabel)
    ax.axhline(limits.center, color="green", label="Center")
    ax.axhline(limits.upper, color="red", linestyle="--", label="UCL")
    ax.axhline(limits.lower, color="red", linestyle="--", label="LCL")
    ax.legend()
    apply_theme(ax, theme)
    return ax


def _plot_attribute_interactive(values: ArrayLike, limits: ControlLimits, title: str, ylabel: str, template: str, height: int, width: int, color: str) -> PlotlyFigure:
    """Render an interactive attribute control chart.

    Args:
        values (ArrayLike): Chart values.
        limits (ControlLimits): Control limits to draw.
        title (str): Chart title.
        ylabel (str): Y-axis label.
        template (str): Plotly template.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.
        color (str): Data line color.

    Returns:
        plotly.graph_objects.Figure: Interactive attribute chart.

    Raises:
        TypeError: If values cannot be plotted.
        ValueError: If limits are invalid.

    Examples:
        ```python
        fig = _plot_attribute_interactive(values, limits, "p Chart", "Proportion", "plotly", 500, 1000, "steelblue")
        ```

    Notes:
        Limit lines are added as Plotly horizontal layout shapes.
    """
    fig = go.Figure(data=[go.Scatter(y=values, mode="lines+markers", name=ylabel, line=dict(color=color))])
    fig.add_hline(y=limits.center, line_color="green", annotation_text="Center")
    fig.add_hline(y=limits.upper, line_color="red", line_dash="dash", annotation_text="UCL")
    fig.add_hline(y=limits.lower, line_color="red", line_dash="dash", annotation_text="LCL")
    fig.update_layout(title=title, xaxis_title="Sample", yaxis_title=ylabel, template=template, height=height, width=width)
    return fig


def p_chart_static(
    defects: ArrayLike,
    sample_sizes: ArrayLike,
    title: str = "p Chart",
    figsize: FigureSize = (12, 6),
    theme: str = "default",
) -> MatplotlibAxes:
    """Create a static p chart for defect proportions.

    Args:
        defects (ArrayLike): Defective counts per sample.
        sample_sizes (ArrayLike): Sample sizes for each count.
        title (str): Chart title.
        figsize (FigureSize): Figure size in inches.
        theme (str): Named style theme.

    Returns:
        matplotlib.axes.Axes: p chart axes.

    Raises:
        TypeError: If inputs cannot be converted to numeric values.
        ValueError: If counts and sample sizes are incompatible.

    Examples:
        ```python
        ax = dv.spc.p_chart_static(defects, sample_sizes)
        ```

    Notes:
        Limits are based on average sample size when subgroup sizes vary.
    """
    counts = as_numeric_series(defects, name="Defects")
    sizes = as_numeric_series(sample_sizes, name="Sample Size")
    if len(counts) != len(sizes):
        raise ValueError("defects and sample_sizes must have the same length.")
    if (sizes <= 0).any() or (counts < 0).any() or (counts > sizes).any():
        raise ValueError("sample sizes must be positive and defects must be between 0 and sample size.")
    proportions = counts / sizes
    pbar = float(counts.sum() / sizes.sum())
    sigma = float(np.sqrt(pbar * (1 - pbar) / sizes.mean()))
    limits = _attribute_limits(pbar, sigma, upper_clip=1.0)
    return _plot_attribute_static(proportions, limits, title, "Proportion Defective", figsize, theme, "steelblue")


def p_chart_interactive(
    defects: ArrayLike,
    sample_sizes: ArrayLike,
    title: str = "p Chart",
    template: str = "plotly",
    height: int = 500,
    width: int = 1000,
) -> PlotlyFigure:
    """Create an interactive p chart for defect proportions.

    Args:
        defects (ArrayLike): Defective counts per sample.
        sample_sizes (ArrayLike): Sample sizes for each count.
        title (str): Chart title.
        template (str): Plotly template.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.

    Returns:
        plotly.graph_objects.Figure: Interactive p chart.

    Raises:
        TypeError: If inputs cannot be converted to numeric values.
        ValueError: If counts and sample sizes are incompatible.

    Examples:
        ```python
        fig = dv.spc.p_chart_interactive(defects, sample_sizes)
        ```

    Notes:
        The chart displays defective proportions rather than raw counts.
    """
    counts = as_numeric_series(defects, name="Defects")
    sizes = as_numeric_series(sample_sizes, name="Sample Size")
    if len(counts) != len(sizes):
        raise ValueError("defects and sample_sizes must have the same length.")
    if (sizes <= 0).any() or (counts < 0).any() or (counts > sizes).any():
        raise ValueError("sample sizes must be positive and defects must be between 0 and sample size.")
    proportions = counts / sizes
    pbar = float(counts.sum() / sizes.sum())
    sigma = float(np.sqrt(pbar * (1 - pbar) / sizes.mean()))
    limits = _attribute_limits(pbar, sigma, upper_clip=1.0)
    return _plot_attribute_interactive(proportions, limits, title, "Proportion Defective", template, height, width, "steelblue")


def np_chart_static(
    defects: ArrayLike,
    sample_size: int,
    title: str = "np Chart",
    figsize: FigureSize = (12, 6),
    theme: str = "default",
) -> MatplotlibAxes:
    """Create a static np chart for defective counts with constant sample size.

    Args:
        defects (ArrayLike): Defective counts per sample.
        sample_size (int): Constant sample size.
        title (str): Chart title.
        figsize (FigureSize): Figure size in inches.
        theme (str): Named style theme.

    Returns:
        matplotlib.axes.Axes: np chart axes.

    Raises:
        TypeError: If defects cannot be converted to numeric values.
        ValueError: If counts or sample size are invalid.

    Examples:
        ```python
        ax = dv.spc.np_chart_static(defects, sample_size=100)
        ```

    Notes:
        Use a p chart when subgroup sample sizes vary.
    """
    validate_positive_int(sample_size, "sample_size")
    counts = as_numeric_series(defects, name="Defects")
    if (counts < 0).any() or (counts > sample_size).any():
        raise ValueError("defects must be between 0 and sample_size.")
    pbar = float(counts.mean() / sample_size)
    center = sample_size * pbar
    sigma = float(np.sqrt(sample_size * pbar * (1 - pbar)))
    limits = _attribute_limits(center, sigma)
    return _plot_attribute_static(counts, limits, title, "Defective Count", figsize, theme, "steelblue")


def np_chart_interactive(
    defects: ArrayLike,
    sample_size: int,
    title: str = "np Chart",
    template: str = "plotly",
    height: int = 500,
    width: int = 1000,
) -> PlotlyFigure:
    """Create an interactive np chart for defective counts with constant sample size.

    Args:
        defects (ArrayLike): Defective counts per sample.
        sample_size (int): Constant sample size.
        title (str): Chart title.
        template (str): Plotly template.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.

    Returns:
        plotly.graph_objects.Figure: Interactive np chart.

    Raises:
        TypeError: If defects cannot be converted to numeric values.
        ValueError: If counts or sample size are invalid.

    Examples:
        ```python
        fig = dv.spc.np_chart_interactive(defects, sample_size=100)
        ```

    Notes:
        The center line represents the expected defective count.
    """
    validate_positive_int(sample_size, "sample_size")
    counts = as_numeric_series(defects, name="Defects")
    if (counts < 0).any() or (counts > sample_size).any():
        raise ValueError("defects must be between 0 and sample_size.")
    pbar = float(counts.mean() / sample_size)
    center = sample_size * pbar
    sigma = float(np.sqrt(sample_size * pbar * (1 - pbar)))
    limits = _attribute_limits(center, sigma)
    return _plot_attribute_interactive(counts, limits, title, "Defective Count", template, height, width, "steelblue")


def c_chart_static(defects: ArrayLike, title: str = "c Chart", figsize: FigureSize = (12, 6), theme: str = "default") -> MatplotlibAxes:
    """Create a static c chart for defect counts per constant opportunity area.

    Args:
        defects (ArrayLike): Defect counts per sample.
        title (str): Chart title.
        figsize (FigureSize): Figure size in inches.
        theme (str): Named style theme.

    Returns:
        matplotlib.axes.Axes: c chart axes.

    Raises:
        TypeError: If defects cannot be converted to numeric values.
        ValueError: If any count is negative.

    Examples:
        ```python
        ax = dv.spc.c_chart_static(defect_counts)
        ```

    Notes:
        c charts assume constant inspection area or opportunity count.
    """
    counts = as_numeric_series(defects, name="Defects")
    if (counts < 0).any():
        raise ValueError("defects must be nonnegative.")
    cbar = float(counts.mean())
    limits = _attribute_limits(cbar, float(np.sqrt(cbar)))
    return _plot_attribute_static(counts, limits, title, "Defect Count", figsize, theme, "orange")


def c_chart_interactive(defects: ArrayLike, title: str = "c Chart", template: str = "plotly", height: int = 500, width: int = 1000) -> PlotlyFigure:
    """Create an interactive c chart for defect counts per constant opportunity area.

    Args:
        defects (ArrayLike): Defect counts per sample.
        title (str): Chart title.
        template (str): Plotly template.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.

    Returns:
        plotly.graph_objects.Figure: Interactive c chart.

    Raises:
        TypeError: If defects cannot be converted to numeric values.
        ValueError: If any count is negative.

    Examples:
        ```python
        fig = dv.spc.c_chart_interactive(defect_counts)
        ```

    Notes:
        Control limits use the Poisson approximation around c-bar.
    """
    counts = as_numeric_series(defects, name="Defects")
    if (counts < 0).any():
        raise ValueError("defects must be nonnegative.")
    cbar = float(counts.mean())
    limits = _attribute_limits(cbar, float(np.sqrt(cbar)))
    return _plot_attribute_interactive(counts, limits, title, "Defect Count", template, height, width, "orange")


def u_chart_static(defects: ArrayLike, units: ArrayLike, title: str = "u Chart", figsize: FigureSize = (12, 6), theme: str = "default") -> MatplotlibAxes:
    """Create a static u chart for defects per unit.

    Args:
        defects (ArrayLike): Defect counts per sample.
        units (ArrayLike): Units inspected per sample.
        title (str): Chart title.
        figsize (FigureSize): Figure size in inches.
        theme (str): Named style theme.

    Returns:
        matplotlib.axes.Axes: u chart axes.

    Raises:
        TypeError: If inputs cannot be converted to numeric values.
        ValueError: If defects and units are incompatible.

    Examples:
        ```python
        ax = dv.spc.u_chart_static(defects, units)
        ```

    Notes:
        u charts are useful when inspection opportunities vary by sample.
    """
    counts = as_numeric_series(defects, name="Defects")
    inspected = as_numeric_series(units, name="Units")
    if len(counts) != len(inspected):
        raise ValueError("defects and units must have the same length.")
    if (counts < 0).any() or (inspected <= 0).any():
        raise ValueError("defects must be nonnegative and units must be positive.")
    rates = counts / inspected
    ubar = float(counts.sum() / inspected.sum())
    sigma = float(np.sqrt(ubar / inspected.mean()))
    limits = _attribute_limits(ubar, sigma)
    return _plot_attribute_static(rates, limits, title, "Defects per Unit", figsize, theme, "purple")


def u_chart_interactive(defects: ArrayLike, units: ArrayLike, title: str = "u Chart", template: str = "plotly", height: int = 500, width: int = 1000) -> PlotlyFigure:
    """Create an interactive u chart for defects per unit.

    Args:
        defects (ArrayLike): Defect counts per sample.
        units (ArrayLike): Units inspected per sample.
        title (str): Chart title.
        template (str): Plotly template.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.

    Returns:
        plotly.graph_objects.Figure: Interactive u chart.

    Raises:
        TypeError: If inputs cannot be converted to numeric values.
        ValueError: If defects and units are incompatible.

    Examples:
        ```python
        fig = dv.spc.u_chart_interactive(defects, units)
        ```

    Notes:
        The y-axis displays defect rate per inspected unit.
    """
    counts = as_numeric_series(defects, name="Defects")
    inspected = as_numeric_series(units, name="Units")
    if len(counts) != len(inspected):
        raise ValueError("defects and units must have the same length.")
    if (counts < 0).any() or (inspected <= 0).any():
        raise ValueError("defects must be nonnegative and units must be positive.")
    rates = counts / inspected
    ubar = float(counts.sum() / inspected.sum())
    sigma = float(np.sqrt(ubar / inspected.mean()))
    limits = _attribute_limits(ubar, sigma)
    return _plot_attribute_interactive(rates, limits, title, "Defects per Unit", template, height, width, "purple")
