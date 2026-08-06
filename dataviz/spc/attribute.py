"""Attribute-data SPC charts."""

from typing import Optional

import numpy as np
import plotly.graph_objects as go

from ..types import ArrayLike, FigureSize, MatplotlibAxes, PlotlyFigure
from ..utils import apply_theme, setup_plot, validate_positive_int
from .constants import get_d2
from .rules import ControlLimits, as_numeric_series, moving_ranges


def _attribute_limits(
    center: float,
    sigma: float,
    lower_clip: float = 0.0,
    upper_clip: Optional[float] = None,
) -> ControlLimits:
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
    return ControlLimits(
        center=float(center), lower=float(lower), upper=float(upper), sigma=float(sigma)
    )


def _plot_attribute_static(
    values: ArrayLike,
    limits: ControlLimits,
    title: str,
    ylabel: str,
    figsize: FigureSize,
    theme: str,
    color: str,
) -> MatplotlibAxes:
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


def _plot_attribute_interactive(
    values: ArrayLike,
    limits: ControlLimits,
    title: str,
    ylabel: str,
    template: str,
    height: int,
    width: int,
    color: str,
) -> PlotlyFigure:
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
    fig = go.Figure(
        data=[
            go.Scatter(
                y=values, mode="lines+markers", name=ylabel, line=dict(color=color)
            )
        ]
    )
    fig.add_hline(y=limits.center, line_color="green", annotation_text="Center")
    fig.add_hline(
        y=limits.upper, line_color="red", line_dash="dash", annotation_text="UCL"
    )
    fig.add_hline(
        y=limits.lower, line_color="red", line_dash="dash", annotation_text="LCL"
    )
    fig.update_layout(
        title=title,
        xaxis_title="Sample",
        yaxis_title=ylabel,
        template=template,
        height=height,
        width=width,
    )
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
        raise ValueError(
            "sample sizes must be positive and defects must be between 0 and sample size."
        )
    proportions = counts / sizes
    pbar = float(counts.sum() / sizes.sum())
    sigma = float(np.sqrt(pbar * (1 - pbar) / sizes.mean()))
    limits = _attribute_limits(pbar, sigma, upper_clip=1.0)
    return _plot_attribute_static(
        proportions, limits, title, "Proportion Defective", figsize, theme, "steelblue"
    )


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
        raise ValueError(
            "sample sizes must be positive and defects must be between 0 and sample size."
        )
    proportions = counts / sizes
    pbar = float(counts.sum() / sizes.sum())
    sigma = float(np.sqrt(pbar * (1 - pbar) / sizes.mean()))
    limits = _attribute_limits(pbar, sigma, upper_clip=1.0)
    return _plot_attribute_interactive(
        proportions,
        limits,
        title,
        "Proportion Defective",
        template,
        height,
        width,
        "steelblue",
    )


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
    return _plot_attribute_static(
        counts, limits, title, "Defective Count", figsize, theme, "steelblue"
    )


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
    return _plot_attribute_interactive(
        counts, limits, title, "Defective Count", template, height, width, "steelblue"
    )


def c_chart_static(
    defects: ArrayLike,
    title: str = "c Chart",
    figsize: FigureSize = (12, 6),
    theme: str = "default",
) -> MatplotlibAxes:
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
    return _plot_attribute_static(
        counts, limits, title, "Defect Count", figsize, theme, "orange"
    )


def c_chart_interactive(
    defects: ArrayLike,
    title: str = "c Chart",
    template: str = "plotly",
    height: int = 500,
    width: int = 1000,
) -> PlotlyFigure:
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
    return _plot_attribute_interactive(
        counts, limits, title, "Defect Count", template, height, width, "orange"
    )


def u_chart_static(
    defects: ArrayLike,
    units: ArrayLike,
    title: str = "u Chart",
    figsize: FigureSize = (12, 6),
    theme: str = "default",
) -> MatplotlibAxes:
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
    return _plot_attribute_static(
        rates, limits, title, "Defects per Unit", figsize, theme, "purple"
    )


def u_chart_interactive(
    defects: ArrayLike,
    units: ArrayLike,
    title: str = "u Chart",
    template: str = "plotly",
    height: int = 500,
    width: int = 1000,
) -> PlotlyFigure:
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
    return _plot_attribute_interactive(
        rates, limits, title, "Defects per Unit", template, height, width, "purple"
    )


def _plot_varying_attribute_static(
    values: ArrayLike,
    center: float,
    lower: ArrayLike,
    upper: ArrayLike,
    title: str,
    ylabel: str,
    figsize: FigureSize,
    theme: str,
    color: str,
) -> MatplotlibAxes:
    """Render a static attribute chart with per-sample (stepped) control limits.

    Args:
        values (ArrayLike): Chart values.
        center (float): Center-line value.
        lower (ArrayLike): Per-sample lower control limits.
        upper (ArrayLike): Per-sample upper control limits.
        title (str): Chart title.
        ylabel (str): Y-axis label.
        figsize (FigureSize): Figure size in inches.
        theme (str): Named style theme.
        color (str): Data line color.

    Returns:
        matplotlib.axes.Axes: Attribute chart axes.

    Raises:
        TypeError: If values cannot be plotted.
        ValueError: If the limit arrays do not match the data length.

    Examples:
        ```python
        ax = _plot_varying_attribute_static(values, pbar, lower, upper, "Laney p' Chart", "Proportion", (12, 6), "default", "steelblue")
        ```

    Notes:
        Stepped limits reflect how control limits tighten or widen with each sample size.
    """
    x = np.arange(len(values))
    _, ax = setup_plot(figsize=figsize, title=title, xlabel="Sample", ylabel=ylabel)
    ax.plot(x, values, marker="o", color=color, label=ylabel)
    ax.axhline(center, color="green", label="Center")
    ax.step(x, upper, color="red", linestyle="--", where="mid", label="UCL")
    ax.step(x, lower, color="red", linestyle="--", where="mid", label="LCL")
    ax.legend()
    apply_theme(ax, theme)
    return ax


def _plot_varying_attribute_interactive(
    values: ArrayLike,
    center: float,
    lower: ArrayLike,
    upper: ArrayLike,
    title: str,
    ylabel: str,
    template: str,
    height: int,
    width: int,
    color: str,
) -> PlotlyFigure:
    """Render an interactive attribute chart with per-sample (stepped) control limits.

    Args:
        values (ArrayLike): Chart values.
        center (float): Center-line value.
        lower (ArrayLike): Per-sample lower control limits.
        upper (ArrayLike): Per-sample upper control limits.
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
        ValueError: If the limit arrays do not match the data length.

    Examples:
        ```python
        fig = _plot_varying_attribute_interactive(values, pbar, lower, upper, "Laney p' Chart", "Proportion", "plotly", 500, 1000, "steelblue")
        ```

    Notes:
        Limit traces use a horizontal-vertical shape so the steps align with each sample.
    """
    x = list(range(len(values)))
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=x,
            y=list(values),
            mode="lines+markers",
            name=ylabel,
            line=dict(color=color),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=x,
            y=list(upper),
            mode="lines",
            name="UCL",
            line=dict(color="red", dash="dash", shape="hv"),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=x,
            y=list(lower),
            mode="lines",
            name="LCL",
            line=dict(color="red", dash="dash", shape="hv"),
        )
    )
    fig.add_hline(y=center, line_color="green", annotation_text="Center")
    fig.update_layout(
        title=title,
        xaxis_title="Sample",
        yaxis_title=ylabel,
        template=template,
        height=height,
        width=width,
    )
    return fig


def _sigma_z(z_scores: ArrayLike) -> float:
    """Estimate the Laney sigma-Z correction from standardized values.

    Args:
        z_scores (ArrayLike): Standardized subgroup statistics.

    Returns:
        float: The average moving range of the z-scores divided by ``d2(2)``.

    Raises:
        TypeError: If z-scores cannot be converted to numeric values.
        ValueError: If fewer than two z-scores are supplied.

    Examples:
        ```python
        correction = _sigma_z(z_scores)
        ```

    Notes:
        A value near one indicates negligible over-dispersion.
    """
    ranges = moving_ranges(z_scores, span=2)
    return float(ranges.mean()) / get_d2(2)


def g_chart_static(
    counts: ArrayLike,
    title: str = "g Chart",
    figsize: FigureSize = (12, 6),
    theme: str = "default",
) -> MatplotlibAxes:
    """Create a static g chart for opportunities between rare events.

    Args:
        counts (ArrayLike): Non-negative counts of units or opportunities between events.
        title (str): Chart title.
        figsize (FigureSize): Figure size in inches.
        theme (str): Named style theme.

    Returns:
        matplotlib.axes.Axes: g chart axes.

    Raises:
        TypeError: If counts cannot be converted to numeric values.
        ValueError: If any count is negative.

    Examples:
        ```python
        ax = dv.spc.g_chart_static(units_between_defects)
        ```

    Notes:
        Limits use the geometric-distribution standard error ``sqrt(gbar * (gbar + 1))``.
    """
    values = as_numeric_series(counts, name="Counts")
    if (values < 0).any():
        raise ValueError("counts must be nonnegative.")
    gbar = float(values.mean())
    sigma = float(np.sqrt(gbar * (gbar + 1)))
    limits = _attribute_limits(gbar, sigma)
    return _plot_attribute_static(
        values, limits, title, "Opportunities Between Events", figsize, theme, "teal"
    )


def g_chart_interactive(
    counts: ArrayLike,
    title: str = "g Chart",
    template: str = "plotly",
    height: int = 500,
    width: int = 1000,
) -> PlotlyFigure:
    """Create an interactive g chart for opportunities between rare events.

    Args:
        counts (ArrayLike): Non-negative counts of units or opportunities between events.
        title (str): Chart title.
        template (str): Plotly template.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.

    Returns:
        plotly.graph_objects.Figure: Interactive g chart.

    Raises:
        TypeError: If counts cannot be converted to numeric values.
        ValueError: If any count is negative.

    Examples:
        ```python
        fig = dv.spc.g_chart_interactive(units_between_defects)
        ```

    Notes:
        The chart is well suited to processes where defects are rare.
    """
    values = as_numeric_series(counts, name="Counts")
    if (values < 0).any():
        raise ValueError("counts must be nonnegative.")
    gbar = float(values.mean())
    sigma = float(np.sqrt(gbar * (gbar + 1)))
    limits = _attribute_limits(gbar, sigma)
    return _plot_attribute_interactive(
        values,
        limits,
        title,
        "Opportunities Between Events",
        template,
        height,
        width,
        "teal",
    )


def t_chart_static(
    times: ArrayLike,
    title: str = "t Chart",
    figsize: FigureSize = (12, 6),
    theme: str = "default",
) -> MatplotlibAxes:
    """Create a static t chart for elapsed time between rare events.

    Args:
        times (ArrayLike): Positive elapsed times between consecutive events.
        title (str): Chart title.
        figsize (FigureSize): Figure size in inches.
        theme (str): Named style theme.

    Returns:
        matplotlib.axes.Axes: t chart axes.

    Raises:
        TypeError: If times cannot be converted to numeric values.
        ValueError: If any time is not positive.

    Examples:
        ```python
        ax = dv.spc.t_chart_static(days_between_incidents)
        ```

    Notes:
        Times are Weibull-transformed with exponent ``1 / 3.6`` before limits are computed.
    """
    values, limits = _t_chart_limits(times)
    return _plot_attribute_static(
        values, limits, title, "Time Between Events", figsize, theme, "darkred"
    )


def t_chart_interactive(
    times: ArrayLike,
    title: str = "t Chart",
    template: str = "plotly",
    height: int = 500,
    width: int = 1000,
) -> PlotlyFigure:
    """Create an interactive t chart for elapsed time between rare events.

    Args:
        times (ArrayLike): Positive elapsed times between consecutive events.
        title (str): Chart title.
        template (str): Plotly template.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.

    Returns:
        plotly.graph_objects.Figure: Interactive t chart.

    Raises:
        TypeError: If times cannot be converted to numeric values.
        ValueError: If any time is not positive.

    Examples:
        ```python
        fig = dv.spc.t_chart_interactive(days_between_incidents)
        ```

    Notes:
        Limits are computed in the transformed space and mapped back to the time scale.
    """
    values, limits = _t_chart_limits(times)
    return _plot_attribute_interactive(
        values, limits, title, "Time Between Events", template, height, width, "darkred"
    )


def _t_chart_limits(times: ArrayLike) -> tuple:
    """Compute t-chart limits on the original time scale.

    Args:
        times (ArrayLike): Positive elapsed times between events.

    Returns:
        tuple: The observed times and their back-transformed control limits.

    Raises:
        TypeError: If times cannot be converted to numeric values.
        ValueError: If any time is not positive.

    Examples:
        ```python
        values, limits = _t_chart_limits(times)
        ```

    Notes:
        The Weibull exponent ``1 / 3.6`` approximates normality for time-between-events data.
    """
    values = as_numeric_series(times, name="Time")
    if (values <= 0).any():
        raise ValueError("times must be positive.")
    exponent = 1.0 / 3.6
    transformed = values**exponent
    center = float(transformed.mean())
    sigma = float(moving_ranges(transformed, span=2).mean()) / get_d2(2)
    upper = (center + 3 * sigma) ** 3.6
    lower_transformed = max(center - 3 * sigma, 0.0)
    lower = lower_transformed**3.6
    limits = ControlLimits(
        center=center**3.6, lower=float(lower), upper=float(upper), sigma=sigma
    )
    return values, limits


def laney_p_chart_static(
    defects: ArrayLike,
    sample_sizes: ArrayLike,
    title: str = "Laney p' Chart",
    figsize: FigureSize = (12, 6),
    theme: str = "default",
) -> MatplotlibAxes:
    """Create a static Laney p' chart correcting for over-dispersion.

    Args:
        defects (ArrayLike): Defective counts per sample.
        sample_sizes (ArrayLike): Sample sizes for each count.
        title (str): Chart title.
        figsize (FigureSize): Figure size in inches.
        theme (str): Named style theme.

    Returns:
        matplotlib.axes.Axes: Laney p' chart axes.

    Raises:
        TypeError: If inputs cannot be converted to numeric values.
        ValueError: If counts and sample sizes are incompatible.

    Examples:
        ```python
        ax = dv.spc.laney_p_chart_static(defects, sample_sizes)
        ```

    Notes:
        The sigma-Z correction widens limits when between-sample variation exceeds the binomial model.
    """
    proportions, center, lower, upper = _laney_p_limits(defects, sample_sizes)
    return _plot_varying_attribute_static(
        proportions,
        center,
        lower,
        upper,
        title,
        "Proportion Defective",
        figsize,
        theme,
        "steelblue",
    )


def laney_p_chart_interactive(
    defects: ArrayLike,
    sample_sizes: ArrayLike,
    title: str = "Laney p' Chart",
    template: str = "plotly",
    height: int = 500,
    width: int = 1000,
) -> PlotlyFigure:
    """Create an interactive Laney p' chart correcting for over-dispersion.

    Args:
        defects (ArrayLike): Defective counts per sample.
        sample_sizes (ArrayLike): Sample sizes for each count.
        title (str): Chart title.
        template (str): Plotly template.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.

    Returns:
        plotly.graph_objects.Figure: Interactive Laney p' chart.

    Raises:
        TypeError: If inputs cannot be converted to numeric values.
        ValueError: If counts and sample sizes are incompatible.

    Examples:
        ```python
        fig = dv.spc.laney_p_chart_interactive(defects, sample_sizes)
        ```

    Notes:
        Use this chart when a standard p chart flags too many false out-of-control points.
    """
    proportions, center, lower, upper = _laney_p_limits(defects, sample_sizes)
    return _plot_varying_attribute_interactive(
        proportions,
        center,
        lower,
        upper,
        title,
        "Proportion Defective",
        template,
        height,
        width,
        "steelblue",
    )


def _laney_p_limits(defects: ArrayLike, sample_sizes: ArrayLike) -> tuple:
    """Compute Laney p' control limits with the sigma-Z correction.

    Args:
        defects (ArrayLike): Defective counts per sample.
        sample_sizes (ArrayLike): Sample sizes for each count.

    Returns:
        tuple: The observed proportions, the center line, and per-sample lower and
        upper control limits.

    Raises:
        TypeError: If inputs cannot be converted to numeric values.
        ValueError: If counts and sample sizes are incompatible.

    Examples:
        ```python
        proportions, center, lower, upper = _laney_p_limits(defects, sample_sizes)
        ```

    Notes:
        Limits are computed per sample size so they step with each subgroup.
    """
    counts = as_numeric_series(defects, name="Defects")
    sizes = as_numeric_series(sample_sizes, name="Sample Size")
    if len(counts) != len(sizes):
        raise ValueError("defects and sample_sizes must have the same length.")
    if (sizes <= 0).any() or (counts < 0).any() or (counts > sizes).any():
        raise ValueError(
            "sample sizes must be positive and defects must be between 0 and sample size."
        )
    proportions = counts / sizes
    pbar = float(counts.sum() / sizes.sum())
    sigma_i = np.sqrt(pbar * (1 - pbar) / sizes)
    z_scores = (proportions - pbar) / sigma_i
    sigma_z = _sigma_z(z_scores)
    spread = 3 * sigma_i * sigma_z
    upper = (pbar + spread).clip(upper=1.0)
    lower = (pbar - spread).clip(lower=0.0)
    return proportions, pbar, lower, upper


def laney_u_chart_static(
    defects: ArrayLike,
    units: ArrayLike,
    title: str = "Laney u' Chart",
    figsize: FigureSize = (12, 6),
    theme: str = "default",
) -> MatplotlibAxes:
    """Create a static Laney u' chart correcting for over-dispersion.

    Args:
        defects (ArrayLike): Defect counts per sample.
        units (ArrayLike): Units inspected per sample.
        title (str): Chart title.
        figsize (FigureSize): Figure size in inches.
        theme (str): Named style theme.

    Returns:
        matplotlib.axes.Axes: Laney u' chart axes.

    Raises:
        TypeError: If inputs cannot be converted to numeric values.
        ValueError: If defects and units are incompatible.

    Examples:
        ```python
        ax = dv.spc.laney_u_chart_static(defects, units)
        ```

    Notes:
        The sigma-Z correction widens limits when between-sample variation exceeds the Poisson model.
    """
    rates, center, lower, upper = _laney_u_limits(defects, units)
    return _plot_varying_attribute_static(
        rates, center, lower, upper, title, "Defects per Unit", figsize, theme, "purple"
    )


def laney_u_chart_interactive(
    defects: ArrayLike,
    units: ArrayLike,
    title: str = "Laney u' Chart",
    template: str = "plotly",
    height: int = 500,
    width: int = 1000,
) -> PlotlyFigure:
    """Create an interactive Laney u' chart correcting for over-dispersion.

    Args:
        defects (ArrayLike): Defect counts per sample.
        units (ArrayLike): Units inspected per sample.
        title (str): Chart title.
        template (str): Plotly template.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.

    Returns:
        plotly.graph_objects.Figure: Interactive Laney u' chart.

    Raises:
        TypeError: If inputs cannot be converted to numeric values.
        ValueError: If defects and units are incompatible.

    Examples:
        ```python
        fig = dv.spc.laney_u_chart_interactive(defects, units)
        ```

    Notes:
        Use this chart when a standard u chart flags too many false out-of-control points.
    """
    rates, center, lower, upper = _laney_u_limits(defects, units)
    return _plot_varying_attribute_interactive(
        rates,
        center,
        lower,
        upper,
        title,
        "Defects per Unit",
        template,
        height,
        width,
        "purple",
    )


def _laney_u_limits(defects: ArrayLike, units: ArrayLike) -> tuple:
    """Compute Laney u' control limits with the sigma-Z correction.

    Args:
        defects (ArrayLike): Defect counts per sample.
        units (ArrayLike): Units inspected per sample.

    Returns:
        tuple: The observed defect rates, the center line, and per-sample lower and
        upper control limits.

    Raises:
        TypeError: If inputs cannot be converted to numeric values.
        ValueError: If defects and units are incompatible.

    Examples:
        ```python
        rates, center, lower, upper = _laney_u_limits(defects, units)
        ```

    Notes:
        Limits are computed per inspected-unit count so they step with each subgroup.
    """
    counts = as_numeric_series(defects, name="Defects")
    inspected = as_numeric_series(units, name="Units")
    if len(counts) != len(inspected):
        raise ValueError("defects and units must have the same length.")
    if (counts < 0).any() or (inspected <= 0).any():
        raise ValueError("defects must be nonnegative and units must be positive.")
    rates = counts / inspected
    ubar = float(counts.sum() / inspected.sum())
    sigma_i = np.sqrt(ubar / inspected)
    z_scores = (rates - ubar) / sigma_i
    sigma_z = _sigma_z(z_scores)
    lower = (ubar - 3 * sigma_i * sigma_z).clip(lower=0.0)
    upper = ubar + 3 * sigma_i * sigma_z
    return rates, ubar, lower, upper
