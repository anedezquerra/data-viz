"""Variable-data SPC charts."""

from typing import Optional, Tuple

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from ..types import ArrayLike, FigureSize, MatrixLike, MatplotlibAxes, PlotlyFigure
from ..utils import apply_theme, setup_plot, validate_alpha
from .constants import get_d2, get_spc_constants
from .rules import (
    ControlLimits,
    as_numeric_series,
    individuals_limits,
    moving_ranges,
    subgroup_matrix,
    xbar_r_limits,
    xbar_s_limits,
)


def _add_limits_static(
    ax: MatplotlibAxes, limits: ControlLimits, color: str = "red"
) -> None:
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


def _add_limits_interactive(
    fig: go.Figure, limits: ControlLimits, color: str = "red"
) -> None:
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
    fig.add_hline(
        y=limits.center, line_color="green", line_dash="solid", annotation_text="Center"
    )
    fig.add_hline(
        y=limits.upper, line_color=color, line_dash="dash", annotation_text="UCL"
    )
    fig.add_hline(
        y=limits.lower, line_color=color, line_dash="dash", annotation_text="LCL"
    )


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
        _, ax = setup_plot(
            figsize=figsize, title=title, xlabel="Sample", ylabel="Moving Range"
        )
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
    fig = go.Figure(
        data=[
            go.Scatter(
                y=ranges,
                mode="lines+markers",
                name=f"MR({span})",
                line=dict(color=color),
            )
        ]
    )
    _add_limits_interactive(fig, limits)
    fig.update_layout(
        title=title,
        xaxis_title="Sample",
        yaxis_title="Moving Range",
        template=template,
        height=height,
        width=width,
    )
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
    fig = make_subplots(
        rows=2, cols=1, shared_xaxes=True, subplot_titles=("Xbar", "Range")
    )
    fig.add_trace(
        go.Scatter(y=means, mode="lines+markers", name="Subgroup Mean"), row=1, col=1
    )
    fig.add_trace(
        go.Scatter(y=ranges, mode="lines+markers", name="Range"), row=2, col=1
    )
    fig.add_hline(
        y=x_limits.center, line_color="green", annotation_text="Center", row=1, col=1
    )
    fig.add_hline(
        y=x_limits.upper,
        line_color="red",
        line_dash="dash",
        annotation_text="UCL",
        row=1,
        col=1,
    )
    fig.add_hline(
        y=x_limits.lower,
        line_color="red",
        line_dash="dash",
        annotation_text="LCL",
        row=1,
        col=1,
    )
    fig.add_hline(
        y=r_limits.center, line_color="green", annotation_text="Center", row=2, col=1
    )
    fig.add_hline(
        y=r_limits.upper,
        line_color="red",
        line_dash="dash",
        annotation_text="UCL",
        row=2,
        col=1,
    )
    fig.add_hline(
        y=r_limits.lower,
        line_color="red",
        line_dash="dash",
        annotation_text="LCL",
        row=2,
        col=1,
    )
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
    fig.add_trace(
        go.Scatter(y=means, mode="lines+markers", name="Subgroup Mean"), row=1, col=1
    )
    fig.add_trace(
        go.Scatter(y=stds, mode="lines+markers", name="Subgroup Std"), row=2, col=1
    )
    fig.add_hline(
        y=x_limits.center, line_color="green", annotation_text="Center", row=1, col=1
    )
    fig.add_hline(
        y=x_limits.upper,
        line_color="red",
        line_dash="dash",
        annotation_text="UCL",
        row=1,
        col=1,
    )
    fig.add_hline(
        y=x_limits.lower,
        line_color="red",
        line_dash="dash",
        annotation_text="LCL",
        row=1,
        col=1,
    )
    fig.add_hline(
        y=s_limits.center, line_color="green", annotation_text="Center", row=2, col=1
    )
    fig.add_hline(
        y=s_limits.upper,
        line_color="red",
        line_dash="dash",
        annotation_text="UCL",
        row=2,
        col=1,
    )
    fig.add_hline(
        y=s_limits.lower,
        line_color="red",
        line_dash="dash",
        annotation_text="LCL",
        row=2,
        col=1,
    )
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
    fig.update_layout(
        title=title,
        xaxis_title="Sample",
        yaxis_title="EWMA",
        template=template,
        height=height,
        width=width,
    )
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
        _, ax = setup_plot(
            figsize=figsize, title=title, xlabel="Sample", ylabel="CUSUM"
        )
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
    fig.add_hline(
        y=h, line_color="red", line_dash="dash", annotation_text="Decision interval"
    )
    fig.update_layout(
        title=title,
        xaxis_title="Sample",
        yaxis_title="CUSUM",
        template=template,
        height=height,
        width=width,
    )
    return fig


def _imr_limits(
    data: ArrayLike, span: int = 2
) -> Tuple[ControlLimits, ControlLimits, "pd.Series", "pd.Series"]:
    """Compute individuals and moving-range limits for an I-MR chart.

    Args:
        data (ArrayLike): Process observations.
        span (int): Moving-range span.

    Returns:
        Tuple[ControlLimits, ControlLimits, pandas.Series, pandas.Series]: Individuals
        limits, moving-range limits, the observations, and the moving ranges.

    Raises:
        TypeError: If data cannot be converted to numeric observations.
        ValueError: If span is unsupported for I-MR estimation.

    Examples:
        ```python
        x_limits, mr_limits, values, ranges = _imr_limits(values)
        ```

    Notes:
        Individuals sigma is estimated as ``MRbar / d2`` following the I-MR convention.
    """
    values = as_numeric_series(data)
    ranges = moving_ranges(values, span=span)
    mrbar = float(ranges.mean())
    sigma = mrbar / get_d2(span)
    center = float(values.mean())
    x_limits = ControlLimits(
        center=center, lower=center - 3 * sigma, upper=center + 3 * sigma, sigma=sigma
    )
    constants = get_spc_constants(span)
    d3 = constants.d3 if constants.d3 is not None else 0.0
    d4 = constants.d4 if constants.d4 is not None else 0.0
    mr_limits = ControlLimits(
        center=mrbar, lower=d3 * mrbar, upper=d4 * mrbar, sigma=sigma
    )
    return x_limits, mr_limits, values, ranges


def imr_chart_static(
    data: ArrayLike,
    span: int = 2,
    title: str = "I-MR Chart",
    figsize: FigureSize = (12, 8),
    theme: str = "default",
    style: str = "default",
) -> Tuple[MatplotlibAxes, MatplotlibAxes]:
    """Create combined static individuals and moving-range charts.

    Args:
        data (ArrayLike): Process observations.
        span (int): Moving-range span used to estimate sigma.
        title (str): Figure title.
        figsize (FigureSize): Figure size in inches.
        theme (str): Named style theme.
        style (str): Matplotlib style context.

    Returns:
        Tuple[matplotlib.axes.Axes, matplotlib.axes.Axes]: Individuals axes and moving-range axes.

    Raises:
        TypeError: If data cannot be converted to numeric observations.
        ValueError: If span is invalid for the data length.

    Examples:
        ```python
        ax_i, ax_mr = dv.spc.imr_chart_static(values)
        ```

    Notes:
        Individuals limits use ``MRbar / d2`` so both panels share one sigma estimate.
    """
    x_limits, mr_limits, values, ranges = _imr_limits(data, span=span)
    with plt.style.context(style):
        fig, axes = plt.subplots(2, 1, figsize=figsize, sharex=True)
        fig.suptitle(title)
        axes[0].plot(values, marker="o", color="steelblue", label="Individual")
        axes[0].set_ylabel("Individual Value")
        _add_limits_static(axes[0], x_limits)
        axes[1].plot(
            range(span - 1, span - 1 + len(ranges)),
            ranges,
            marker="o",
            color="orange",
            label=f"MR({span})",
        )
        axes[1].set_xlabel("Sample")
        axes[1].set_ylabel("Moving Range")
        _add_limits_static(axes[1], mr_limits)
        for ax in axes:
            ax.legend()
            apply_theme(ax, theme)
        return axes[0], axes[1]


def imr_chart_interactive(
    data: ArrayLike,
    span: int = 2,
    title: str = "I-MR Chart",
    template: str = "plotly",
    height: int = 700,
    width: int = 1000,
) -> PlotlyFigure:
    """Create a combined interactive individuals and moving-range chart.

    Args:
        data (ArrayLike): Process observations.
        span (int): Moving-range span used to estimate sigma.
        title (str): Figure title.
        template (str): Plotly template.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.

    Returns:
        plotly.graph_objects.Figure: Stacked individuals and moving-range chart.

    Raises:
        TypeError: If data cannot be converted to numeric observations.
        ValueError: If span is invalid for the data length.

    Examples:
        ```python
        fig = dv.spc.imr_chart_interactive(values)
        ```

    Notes:
        The two panels share one sigma estimate derived from the moving ranges.
    """
    x_limits, mr_limits, values, ranges = _imr_limits(data, span=span)
    fig = make_subplots(
        rows=2,
        cols=1,
        shared_xaxes=True,
        subplot_titles=("Individuals", "Moving Range"),
    )
    fig.add_trace(
        go.Scatter(
            y=values,
            mode="lines+markers",
            name="Individual",
            line=dict(color="steelblue"),
        ),
        row=1,
        col=1,
    )
    for value, color, dash in (
        (x_limits.center, "green", "solid"),
        (x_limits.upper, "red", "dash"),
        (x_limits.lower, "red", "dash"),
    ):
        fig.add_hline(y=value, line_color=color, line_dash=dash, row=1, col=1)
    fig.add_trace(
        go.Scatter(
            x=list(range(span - 1, span - 1 + len(ranges))),
            y=ranges,
            mode="lines+markers",
            name=f"MR({span})",
            line=dict(color="orange"),
        ),
        row=2,
        col=1,
    )
    for value, color, dash in (
        (mr_limits.center, "green", "solid"),
        (mr_limits.upper, "red", "dash"),
        (mr_limits.lower, "red", "dash"),
    ):
        fig.add_hline(y=value, line_color=color, line_dash=dash, row=2, col=1)
    fig.update_layout(title=title, template=template, height=height, width=width)
    fig.update_xaxes(title_text="Sample", row=2, col=1)
    return fig


def median_chart_static(
    data: MatrixLike,
    subgroup_size: Optional[int] = None,
    title: str = "Median Chart",
    figsize: FigureSize = (12, 6),
    theme: str = "default",
    style: str = "default",
) -> MatplotlibAxes:
    """Create a static median (X-tilde) chart for subgrouped measurements.

    Args:
        data (MatrixLike): Matrix-like subgroup data or flat process observations.
        subgroup_size (Optional[int]): Subgroup size for flat data.
        title (str): Chart title.
        figsize (FigureSize): Figure size in inches.
        theme (str): Named style theme.
        style (str): Matplotlib style context.

    Returns:
        matplotlib.axes.Axes: Median chart axes.

    Raises:
        TypeError: If data cannot be converted to numeric subgroups.
        ValueError: If the subgroup size lacks tabulated SPC constants.

    Examples:
        ```python
        ax = dv.spc.median_chart_static(values, subgroup_size=5)
        ```

    Notes:
        Limits use ``A2 * Rbar`` around the mean of subgroup medians.
    """
    limits, medians = _median_limits(data, subgroup_size=subgroup_size)
    with plt.style.context(style):
        _, ax = setup_plot(
            figsize=figsize, title=title, xlabel="Subgroup", ylabel="Median"
        )
        ax.plot(medians, marker="o", color="steelblue", label="Subgroup Median")
        _add_limits_static(ax, limits)
        ax.legend()
        apply_theme(ax, theme)
        return ax


def median_chart_interactive(
    data: MatrixLike,
    subgroup_size: Optional[int] = None,
    title: str = "Median Chart",
    template: str = "plotly",
    height: int = 500,
    width: int = 1000,
) -> PlotlyFigure:
    """Create an interactive median (X-tilde) chart for subgrouped measurements.

    Args:
        data (MatrixLike): Matrix-like subgroup data or flat process observations.
        subgroup_size (Optional[int]): Subgroup size for flat data.
        title (str): Chart title.
        template (str): Plotly template.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.

    Returns:
        plotly.graph_objects.Figure: Interactive median chart.

    Raises:
        TypeError: If data cannot be converted to numeric subgroups.
        ValueError: If the subgroup size lacks tabulated SPC constants.

    Examples:
        ```python
        fig = dv.spc.median_chart_interactive(values, subgroup_size=5)
        ```

    Notes:
        Limits use ``A2 * Rbar`` around the mean of subgroup medians.
    """
    limits, medians = _median_limits(data, subgroup_size=subgroup_size)
    fig = go.Figure(
        data=[
            go.Scatter(
                y=medians,
                mode="lines+markers",
                name="Subgroup Median",
                line=dict(color="steelblue"),
            )
        ]
    )
    _add_limits_interactive(fig, limits)
    fig.update_layout(
        title=title,
        xaxis_title="Subgroup",
        yaxis_title="Median",
        template=template,
        height=height,
        width=width,
    )
    return fig


def _median_limits(
    data: MatrixLike, subgroup_size: Optional[int] = None
) -> Tuple[ControlLimits, "pd.Series"]:
    """Compute median-chart limits from subgrouped measurements.

    Args:
        data (MatrixLike): Matrix-like subgroup data or flat process observations.
        subgroup_size (Optional[int]): Subgroup size for flat data.

    Returns:
        Tuple[ControlLimits, pandas.Series]: Median-chart limits and subgroup medians.

    Raises:
        TypeError: If data cannot be converted to numeric subgroups.
        ValueError: If the subgroup size lacks tabulated SPC constants.

    Examples:
        ```python
        limits, medians = _median_limits(values, subgroup_size=5)
        ```

    Notes:
        The center line is the mean of subgroup medians for robustness to outliers.
    """
    groups = subgroup_matrix(data, subgroup_size=subgroup_size)
    n = groups.shape[1]
    constants = get_spc_constants(n)
    if constants.a2 is None:
        raise ValueError("Median charts require an A2 constant for the subgroup size.")
    medians = groups.median(axis=1).reset_index(drop=True)
    ranges = (groups.max(axis=1) - groups.min(axis=1)).reset_index(drop=True)
    center = float(medians.mean())
    rbar = float(ranges.mean())
    spread = constants.a2 * rbar
    sigma = rbar / get_d2(n) if n in range(2, 11) else 0.0
    limits = ControlLimits(
        center=center, lower=center - spread, upper=center + spread, sigma=sigma
    )
    return limits, medians


def levey_jennings_chart_static(
    data: ArrayLike,
    mean: Optional[float] = None,
    sd: Optional[float] = None,
    title: str = "Levey-Jennings Chart",
    figsize: FigureSize = (12, 6),
    theme: str = "default",
    style: str = "default",
) -> MatplotlibAxes:
    """Create a static Levey-Jennings chart with 1, 2, and 3 sigma zones.

    Args:
        data (ArrayLike): Quality-control measurements over time.
        mean (Optional[float]): Target mean; estimated from data when omitted.
        sd (Optional[float]): Target standard deviation; estimated when omitted.
        title (str): Chart title.
        figsize (FigureSize): Figure size in inches.
        theme (str): Named style theme.
        style (str): Matplotlib style context.

    Returns:
        matplotlib.axes.Axes: Levey-Jennings chart axes.

    Raises:
        TypeError: If data cannot be converted to numeric observations.
        ValueError: If the supplied standard deviation is not positive.

    Examples:
        ```python
        ax = dv.spc.levey_jennings_chart_static(values, mean=10.0, sd=0.2)
        ```

    Notes:
        Zone lines follow the laboratory Westgard convention at 1, 2, and 3 sigma.
    """
    values, center, sigma = _levey_jennings_stats(data, mean=mean, sd=sd)
    with plt.style.context(style):
        _, ax = setup_plot(
            figsize=figsize, title=title, xlabel="Sample", ylabel="Measurement"
        )
        ax.plot(values, marker="o", color="steelblue", label="Measurement")
        ax.axhline(center, color="green", label="Mean")
        for k, color in ((1, "green"), (2, "orange"), (3, "red")):
            ax.axhline(center + k * sigma, color=color, linestyle="--", label=f"+{k}s")
            ax.axhline(center - k * sigma, color=color, linestyle="--", label=f"-{k}s")
        ax.legend(ncol=2, fontsize=8)
        apply_theme(ax, theme)
        return ax


def levey_jennings_chart_interactive(
    data: ArrayLike,
    mean: Optional[float] = None,
    sd: Optional[float] = None,
    title: str = "Levey-Jennings Chart",
    template: str = "plotly",
    height: int = 500,
    width: int = 1000,
) -> PlotlyFigure:
    """Create an interactive Levey-Jennings chart with 1, 2, and 3 sigma zones.

    Args:
        data (ArrayLike): Quality-control measurements over time.
        mean (Optional[float]): Target mean; estimated from data when omitted.
        sd (Optional[float]): Target standard deviation; estimated when omitted.
        title (str): Chart title.
        template (str): Plotly template.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.

    Returns:
        plotly.graph_objects.Figure: Interactive Levey-Jennings chart.

    Raises:
        TypeError: If data cannot be converted to numeric observations.
        ValueError: If the supplied standard deviation is not positive.

    Examples:
        ```python
        fig = dv.spc.levey_jennings_chart_interactive(values, mean=10.0, sd=0.2)
        ```

    Notes:
        Zone lines follow the laboratory Westgard convention at 1, 2, and 3 sigma.
    """
    values, center, sigma = _levey_jennings_stats(data, mean=mean, sd=sd)
    fig = go.Figure(
        data=[
            go.Scatter(
                y=values,
                mode="lines+markers",
                name="Measurement",
                line=dict(color="steelblue"),
            )
        ]
    )
    fig.add_hline(y=center, line_color="green", annotation_text="Mean")
    for k, color in ((1, "green"), (2, "orange"), (3, "red")):
        fig.add_hline(
            y=center + k * sigma,
            line_color=color,
            line_dash="dash",
            annotation_text=f"+{k}s",
        )
        fig.add_hline(
            y=center - k * sigma,
            line_color=color,
            line_dash="dash",
            annotation_text=f"-{k}s",
        )
    fig.update_layout(
        title=title,
        xaxis_title="Sample",
        yaxis_title="Measurement",
        template=template,
        height=height,
        width=width,
    )
    return fig


def _levey_jennings_stats(
    data: ArrayLike, mean: Optional[float] = None, sd: Optional[float] = None
) -> Tuple["pd.Series", float, float]:
    """Resolve the center and sigma used by a Levey-Jennings chart.

    Args:
        data (ArrayLike): Quality-control measurements.
        mean (Optional[float]): Target mean; estimated from data when omitted.
        sd (Optional[float]): Target standard deviation; estimated when omitted.

    Returns:
        Tuple[pandas.Series, float, float]: Observations, center line, and sigma.

    Raises:
        TypeError: If data cannot be converted to numeric observations.
        ValueError: If the supplied standard deviation is not positive.

    Examples:
        ```python
        values, center, sigma = _levey_jennings_stats(values)
        ```

    Notes:
        A supplied target mean and sigma let repeated runs share fixed control zones.
    """
    values = as_numeric_series(data)
    center = float(values.mean()) if mean is None else float(mean)
    if sd is None:
        sigma = float(values.std(ddof=1)) if len(values) > 1 else 0.0
    else:
        if sd <= 0:
            raise ValueError("sd must be greater than zero.")
        sigma = float(sd)
    return values, center, sigma
