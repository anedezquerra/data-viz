"""Variable-data SPC charts."""

from typing import Optional, Tuple

import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from ..types import ArrayLike, FigureSize, MatrixLike, MatplotlibAxes, PlotlyFigure
from ..utils import apply_theme, setup_plot, validate_alpha, validate_positive_int
from .rules import ControlLimits, as_numeric_series, individuals_limits, moving_ranges, xbar_r_limits, xbar_s_limits


def _add_limits_static(ax: MatplotlibAxes, limits: ControlLimits, color: str = "red") -> None:
    """Add center and control limits to a matplotlib axes.

    Args:
        ax (MatplotlibAxes): Axes to update.
        limits (ControlLimits): Control limits to draw.
        color (str): Limit line color.

    Returns:
        None: The axes is modified in place.

    Raises:
        TypeError: If the axes object is invalid.
        ValueError: If limits cannot be rendered.

    Examples:
        ```python
        _add_limits_static(ax, limits)
        ```

    Notes:
        Center lines are green and limits use the supplied color.
    """
    ax.axhline(limits.center, color="green", linestyle="-", label="Center")
    ax.axhline(limits.upper, color=color, linestyle="--", label="UCL")
    ax.axhline(limits.lower, color=color, linestyle="--", label="LCL")


def _add_limits_interactive(fig: go.Figure, limits: ControlLimits, color: str = "red") -> None:
    """Add center and control limits to a Plotly figure.

    Args:
        fig (go.Figure): Figure to update.
        limits (ControlLimits): Control limits to draw.
        color (str): Limit line color.

    Returns:
        None: The figure is modified in place.

    Raises:
        TypeError: If the figure object is invalid.
        ValueError: If limits cannot be rendered.

    Examples:
        ```python
        _add_limits_interactive(fig, limits)
        ```

    Notes:
        Plotly horizontal lines are layout shapes rather than data traces.
    """
    fig.add_hline(y=limits.center, line_color="green", line_dash="solid", annotation_text="Center")
    fig.add_hline(y=limits.upper, line_color=color, line_dash="dash", annotation_text="UCL")
    fig.add_hline(y=limits.lower, line_color=color, line_dash="dash", annotation_text="LCL")


def moving_range_chart_static(
    data: ArrayLike,
    span: int = 2,
    title: str = "Moving Range Chart",
    figsize: FigureSize = (12, 6),
    color: str = "orange",
    theme: str = "default",
    style: str = "default",
) -> MatplotlibAxes:
    """Create a static moving range chart.

    Args:
        data (ArrayLike): Process observations.
        span (int): Difference span used for moving ranges.
        title (str): Chart title.
        figsize (FigureSize): Figure size in inches.
        color (str): Moving range line color.
        theme (str): Named style theme.
        style (str): Matplotlib style context.

    Returns:
        matplotlib.axes.Axes: Moving range chart axes.

    Raises:
        TypeError: If data cannot be converted to numeric observations.
        ValueError: If span is invalid.

    Examples:
        ```python
        ax = dv.spc.moving_range_chart_static(values)
        ```

    Notes:
        Moving ranges are useful alongside individuals charts.
    """
    ranges = moving_ranges(data, span=span)
    limits = individuals_limits(ranges)
    with plt.style.context(style):
        _, ax = setup_plot(figsize=figsize, title=title, xlabel="Sample", ylabel="Moving Range")
        ax.plot(ranges, marker="o", color=color, label=f"MR({span})")
        _add_limits_static(ax, limits)
        ax.legend()
        apply_theme(ax, theme)
        return ax


def moving_range_chart_interactive(
    data: ArrayLike,
    span: int = 2,
    title: str = "Moving Range Chart",
    color: str = "orange",
    template: str = "plotly",
    height: int = 500,
    width: int = 1000,
) -> PlotlyFigure:
    """Create an interactive moving range chart.

    Args:
        data (ArrayLike): Process observations.
        span (int): Difference span used for moving ranges.
        title (str): Chart title.
        color (str): Moving range line color.
        template (str): Plotly template.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.

    Returns:
        plotly.graph_objects.Figure: Interactive moving range chart.

    Raises:
        TypeError: If data cannot be converted to numeric observations.
        ValueError: If span is invalid.

    Examples:
        ```python
        fig = dv.spc.moving_range_chart_interactive(values)
        ```

    Notes:
        Control limits are computed from the moving ranges themselves.
    """
    ranges = moving_ranges(data, span=span)
    limits = individuals_limits(ranges)
    fig = go.Figure(data=[go.Scatter(y=ranges, mode="lines+markers", name=f"MR({span})", line=dict(color=color))])
    _add_limits_interactive(fig, limits)
    fig.update_layout(title=title, xaxis_title="Sample", yaxis_title="Moving Range", template=template, height=height, width=width)
    return fig


def xbar_r_chart_static(
    data: MatrixLike,
    subgroup_size: Optional[int] = None,
    title: str = "Xbar-R Chart",
    figsize: FigureSize = (12, 8),
    theme: str = "default",
    style: str = "default",
) -> Tuple[MatplotlibAxes, MatplotlibAxes]:
    """Create static Xbar and R charts for subgrouped measurements.

    Args:
        data (MatrixLike): Matrix-like subgroup data or flat process observations.
        subgroup_size (Optional[int]): Subgroup size for flat data.
        title (str): Figure title.
        figsize (FigureSize): Figure size in inches.
        theme (str): Named style theme.
        style (str): Matplotlib style context.

    Returns:
        Tuple[matplotlib.axes.Axes, matplotlib.axes.Axes]: Xbar axes and R axes.

    Raises:
        TypeError: If data cannot be converted to numeric subgroups.
        ValueError: If subgroup construction fails.

    Examples:
        ```python
        ax_x, ax_r = dv.spc.xbar_r_chart_static(values, subgroup_size=5)
        ```

    Notes:
        Limits use empirical subgroup means and ranges for broad subgroup-size support.
    """
    x_limits, r_limits, means, ranges = xbar_r_limits(data, subgroup_size=subgroup_size)
    with plt.style.context(style):
        fig, axes = plt.subplots(2, 1, figsize=figsize, sharex=True)
        fig.suptitle(title)
        axes[0].plot(means, marker="o", color="steelblue", label="Subgroup Mean")
        axes[0].set_ylabel("Mean")
        _add_limits_static(axes[0], x_limits)
        axes[1].plot(ranges, marker="o", color="orange", label="Range")
        axes[1].set_xlabel("Subgroup")
        axes[1].set_ylabel("Range")
        _add_limits_static(axes[1], r_limits)
        for ax in axes:
            ax.legend()
            apply_theme(ax, theme)
        return axes[0], axes[1]


def xbar_r_chart_interactive(
    data: MatrixLike,
    subgroup_size: Optional[int] = None,
    title: str = "Xbar-R Chart",
    template: str = "plotly",
    height: int = 700,
    width: int = 1000,
) -> PlotlyFigure:
    """Create an interactive Xbar-R chart for subgrouped measurements.

    Args:
        data (MatrixLike): Matrix-like subgroup data or flat process observations.
        subgroup_size (Optional[int]): Subgroup size for flat data.
        title (str): Figure title.
        template (str): Plotly template.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.

    Returns:
        plotly.graph_objects.Figure: Interactive Xbar-R figure.

    Raises:
        TypeError: If data cannot be converted to numeric subgroups.
        ValueError: If subgroup construction fails.

    Examples:
        ```python
        fig = dv.spc.xbar_r_chart_interactive(values, subgroup_size=5)
        ```

    Notes:
        Mean and range series are shown in stacked subplots.
    """
    x_limits, r_limits, means, ranges = xbar_r_limits(data, subgroup_size=subgroup_size)
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Xbar", "Range"))
    fig.add_trace(go.Scatter(y=means, mode="lines+markers", name="Subgroup Mean"), row=1, col=1)
    fig.add_trace(go.Scatter(y=ranges, mode="lines+markers", name="Range"), row=2, col=1)
    fig.add_hline(y=x_limits.center, line_color="green", annotation_text="Center", row=1, col=1)
    fig.add_hline(y=x_limits.upper, line_color="red", line_dash="dash", annotation_text="UCL", row=1, col=1)
    fig.add_hline(y=x_limits.lower, line_color="red", line_dash="dash", annotation_text="LCL", row=1, col=1)
    fig.add_hline(y=r_limits.center, line_color="green", annotation_text="Center", row=2, col=1)
    fig.add_hline(y=r_limits.upper, line_color="red", line_dash="dash", annotation_text="UCL", row=2, col=1)
    fig.add_hline(y=r_limits.lower, line_color="red", line_dash="dash", annotation_text="LCL", row=2, col=1)
    fig.update_layout(title=title, template=template, height=height, width=width)
    fig.update_yaxes(title_text="Mean", row=1, col=1)
    fig.update_yaxes(title_text="Range", row=2, col=1)
    fig.update_xaxes(title_text="Subgroup", row=2, col=1)
    return fig


def xbar_s_chart_static(
    data: MatrixLike,
    subgroup_size: Optional[int] = None,
    title: str = "Xbar-S Chart",
    figsize: FigureSize = (12, 8),
    theme: str = "default",
    style: str = "default",
) -> Tuple[MatplotlibAxes, MatplotlibAxes]:
    """Create static Xbar and S charts for subgrouped measurements.

    Args:
        data (MatrixLike): Matrix-like subgroup data or flat process observations.
        subgroup_size (Optional[int]): Subgroup size for flat data.
        title (str): Figure title.
        figsize (FigureSize): Figure size in inches.
        theme (str): Named style theme.
        style (str): Matplotlib style context.

    Returns:
        Tuple[matplotlib.axes.Axes, matplotlib.axes.Axes]: Xbar axes and S axes.

    Raises:
        TypeError: If data cannot be converted to numeric subgroups.
        ValueError: If subgroup construction fails.

    Examples:
        ```python
        ax_x, ax_s = dv.spc.xbar_s_chart_static(values, subgroup_size=5)
        ```

    Notes:
        S charts use subgroup standard deviations instead of ranges.
    """
    x_limits, s_limits, means, stds = xbar_s_limits(data, subgroup_size=subgroup_size)
    with plt.style.context(style):
        fig, axes = plt.subplots(2, 1, figsize=figsize, sharex=True)
        fig.suptitle(title)
        axes[0].plot(means, marker="o", color="steelblue", label="Subgroup Mean")
        axes[0].set_ylabel("Mean")
        _add_limits_static(axes[0], x_limits)
        axes[1].plot(stds, marker="o", color="purple", label="Subgroup Std")
        axes[1].set_xlabel("Subgroup")
        axes[1].set_ylabel("Std Dev")
        _add_limits_static(axes[1], s_limits)
        for ax in axes:
            ax.legend()
            apply_theme(ax, theme)
        return axes[0], axes[1]


def xbar_s_chart_interactive(
    data: MatrixLike,
    subgroup_size: Optional[int] = None,
    title: str = "Xbar-S Chart",
    template: str = "plotly",
    height: int = 700,
    width: int = 1000,
) -> PlotlyFigure:
    """Create an interactive Xbar-S chart for subgrouped measurements.

    Args:
        data (MatrixLike): Matrix-like subgroup data or flat process observations.
        subgroup_size (Optional[int]): Subgroup size for flat data.
        title (str): Figure title.
        template (str): Plotly template.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.

    Returns:
        plotly.graph_objects.Figure: Interactive Xbar-S figure.

    Raises:
        TypeError: If data cannot be converted to numeric subgroups.
        ValueError: If subgroup construction fails.

    Examples:
        ```python
        fig = dv.spc.xbar_s_chart_interactive(values, subgroup_size=5)
        ```

    Notes:
        Mean and standard-deviation series are shown in stacked subplots.
    """
    x_limits, s_limits, means, stds = xbar_s_limits(data, subgroup_size=subgroup_size)
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Xbar", "S"))
    fig.add_trace(go.Scatter(y=means, mode="lines+markers", name="Subgroup Mean"), row=1, col=1)
    fig.add_trace(go.Scatter(y=stds, mode="lines+markers", name="Subgroup Std"), row=2, col=1)
    fig.add_hline(y=x_limits.center, line_color="green", annotation_text="Center", row=1, col=1)
    fig.add_hline(y=x_limits.upper, line_color="red", line_dash="dash", annotation_text="UCL", row=1, col=1)
    fig.add_hline(y=x_limits.lower, line_color="red", line_dash="dash", annotation_text="LCL", row=1, col=1)
    fig.add_hline(y=s_limits.center, line_color="green", annotation_text="Center", row=2, col=1)
    fig.add_hline(y=s_limits.upper, line_color="red", line_dash="dash", annotation_text="UCL", row=2, col=1)
    fig.add_hline(y=s_limits.lower, line_color="red", line_dash="dash", annotation_text="LCL", row=2, col=1)
    fig.update_layout(title=title, template=template, height=height, width=width)
    fig.update_yaxes(title_text="Mean", row=1, col=1)
    fig.update_yaxes(title_text="Std Dev", row=2, col=1)
    fig.update_xaxes(title_text="Subgroup", row=2, col=1)
    return fig


def ewma_chart_static(
    data: ArrayLike,
    lambda_: float = 0.2,
    title: str = "EWMA Chart",
    figsize: FigureSize = (12, 6),
    theme: str = "default",
    style: str = "default",
) -> MatplotlibAxes:
    """Create a static exponentially weighted moving average chart.

    Args:
        data (ArrayLike): Process observations.
        lambda_ (float): EWMA smoothing parameter from 0 to 1.
        title (str): Chart title.
        figsize (FigureSize): Figure size in inches.
        theme (str): Named style theme.
        style (str): Matplotlib style context.

    Returns:
        matplotlib.axes.Axes: EWMA chart axes.

    Raises:
        TypeError: If data cannot be converted to numeric observations.
        ValueError: If ``lambda_`` is outside ``(0, 1]``.

    Examples:
        ```python
        ax = dv.spc.ewma_chart_static(values, lambda_=0.3)
        ```

    Notes:
        EWMA charts are sensitive to small sustained process shifts.
    """
    validate_alpha(lambda_, name="lambda_")
    if lambda_ == 0:
        raise ValueError("lambda_ must be greater than zero.")
    values = as_numeric_series(data)
    ewma = values.ewm(alpha=lambda_, adjust=False).mean()
    limits = individuals_limits(ewma)
    with plt.style.context(style):
        _, ax = setup_plot(figsize=figsize, title=title, xlabel="Sample", ylabel="EWMA")
        ax.plot(ewma, marker="o", color="steelblue", label="EWMA")
        _add_limits_static(ax, limits)
        ax.legend()
        apply_theme(ax, theme)
        return ax


def ewma_chart_interactive(
    data: ArrayLike,
    lambda_: float = 0.2,
    title: str = "EWMA Chart",
    template: str = "plotly",
    height: int = 500,
    width: int = 1000,
) -> PlotlyFigure:
    """Create an interactive exponentially weighted moving average chart.

    Args:
        data (ArrayLike): Process observations.
        lambda_ (float): EWMA smoothing parameter from 0 to 1.
        title (str): Chart title.
        template (str): Plotly template.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.

    Returns:
        plotly.graph_objects.Figure: Interactive EWMA chart.

    Raises:
        TypeError: If data cannot be converted to numeric observations.
        ValueError: If ``lambda_`` is outside ``(0, 1]``.

    Examples:
        ```python
        fig = dv.spc.ewma_chart_interactive(values)
        ```

    Notes:
        Control limits are estimated from the EWMA series.
    """
    validate_alpha(lambda_, name="lambda_")
    if lambda_ == 0:
        raise ValueError("lambda_ must be greater than zero.")
    values = as_numeric_series(data)
    ewma = values.ewm(alpha=lambda_, adjust=False).mean()
    limits = individuals_limits(ewma)
    fig = go.Figure(data=[go.Scatter(y=ewma, mode="lines+markers", name="EWMA")])
    _add_limits_interactive(fig, limits)
    fig.update_layout(title=title, xaxis_title="Sample", yaxis_title="EWMA", template=template, height=height, width=width)
    return fig


def cusum_chart_static(
    data: ArrayLike,
    target: Optional[float] = None,
    k: float = 0.5,
    h: float = 5.0,
    title: str = "CUSUM Chart",
    figsize: FigureSize = (12, 6),
    theme: str = "default",
    style: str = "default",
) -> MatplotlibAxes:
    """Create a static cumulative sum chart.

    Args:
        data (ArrayLike): Process observations.
        target (Optional[float]): Process target. Defaults to data mean.
        k (float): Reference value.
        h (float): Decision interval.
        title (str): Chart title.
        figsize (FigureSize): Figure size in inches.
        theme (str): Named style theme.
        style (str): Matplotlib style context.

    Returns:
        matplotlib.axes.Axes: CUSUM chart axes.

    Raises:
        TypeError: If data cannot be converted to numeric observations.
        ValueError: If ``k`` or ``h`` is invalid.

    Examples:
        ```python
        ax = dv.spc.cusum_chart_static(values, target=10)
        ```

    Notes:
        The chart shows positive and negative one-sided cumulative sums.
    """
    if k < 0 or h <= 0:
        raise ValueError("k must be nonnegative and h must be greater than zero.")
    values = as_numeric_series(data)
    center = float(values.mean()) if target is None else float(target)
    c_plus = np.maximum.accumulate(np.zeros(len(values)))
    c_minus = np.maximum.accumulate(np.zeros(len(values)))
    for idx in range(1, len(values)):
        c_plus[idx] = max(0.0, c_plus[idx - 1] + values.iloc[idx] - center - k)
        c_minus[idx] = max(0.0, c_minus[idx - 1] + center - values.iloc[idx] - k)
    with plt.style.context(style):
        _, ax = setup_plot(figsize=figsize, title=title, xlabel="Sample", ylabel="CUSUM")
        ax.plot(c_plus, color="steelblue", label="C+")
        ax.plot(c_minus, color="orange", label="C-")
        ax.axhline(h, color="red", linestyle="--", label="Decision interval")
        ax.legend()
        apply_theme(ax, theme)
        return ax


def cusum_chart_interactive(
    data: ArrayLike,
    target: Optional[float] = None,
    k: float = 0.5,
    h: float = 5.0,
    title: str = "CUSUM Chart",
    template: str = "plotly",
    height: int = 500,
    width: int = 1000,
) -> PlotlyFigure:
    """Create an interactive cumulative sum chart.

    Args:
        data (ArrayLike): Process observations.
        target (Optional[float]): Process target. Defaults to data mean.
        k (float): Reference value.
        h (float): Decision interval.
        title (str): Chart title.
        template (str): Plotly template.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.

    Returns:
        plotly.graph_objects.Figure: Interactive CUSUM chart.

    Raises:
        TypeError: If data cannot be converted to numeric observations.
        ValueError: If ``k`` or ``h`` is invalid.

    Examples:
        ```python
        fig = dv.spc.cusum_chart_interactive(values)
        ```

    Notes:
        Points beyond the decision interval indicate potential process shifts.
    """
    if k < 0 or h <= 0:
        raise ValueError("k must be nonnegative and h must be greater than zero.")
    values = as_numeric_series(data)
    center = float(values.mean()) if target is None else float(target)
    c_plus = np.zeros(len(values))
    c_minus = np.zeros(len(values))
    for idx in range(1, len(values)):
        c_plus[idx] = max(0.0, c_plus[idx - 1] + values.iloc[idx] - center - k)
        c_minus[idx] = max(0.0, c_minus[idx - 1] + center - values.iloc[idx] - k)
    fig = go.Figure()
    fig.add_trace(go.Scatter(y=c_plus, mode="lines", name="C+"))
    fig.add_trace(go.Scatter(y=c_minus, mode="lines", name="C-"))
    fig.add_hline(y=h, line_color="red", line_dash="dash", annotation_text="Decision interval")
    fig.update_layout(title=title, xaxis_title="Sample", yaxis_title="CUSUM", template=template, height=height, width=width)
    return fig
