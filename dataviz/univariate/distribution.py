"""Empirical distribution and probability diagnostic charts."""

from typing import Optional, Tuple

import numpy as np
import plotly.graph_objects as go
from scipy import stats

from ..types import FigureSize, MatplotlibAxes, PlotlyFigure, SeriesLike
from ..utils import apply_theme, setup_plot, validate_positive_int
from .stats import as_numeric_series


def ecdf_values(data: SeriesLike) -> Tuple[np.ndarray, np.ndarray]:
    """Compute empirical cumulative distribution function values.

    Args:
        data (SeriesLike): Input observations.

    Returns:
        tuple[numpy.ndarray, numpy.ndarray]: Sorted values and cumulative probabilities.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If no non-missing numeric observations remain.

    Examples:
        ```python
        x, y = ecdf_values([3, 1, 2])
        ```

    Notes:
        Probabilities use the conventional ``rank / n`` plotting positions.
    """
    values = np.sort(as_numeric_series(data).to_numpy(dtype=float))
    probabilities = np.arange(1, len(values) + 1) / len(values)
    return values, probabilities


def ecdf_plot_static(
    data: SeriesLike,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: str = "Cumulative Probability",
    figsize: FigureSize = (10, 6),
    color: Optional[str] = None,
    linewidth: float = 2.0,
    marker: Optional[str] = None,
    theme: str = "default",
    grid: bool = True,
    **kwargs,
) -> MatplotlibAxes:
    """Create a static empirical cumulative distribution plot.

    Args:
        data (SeriesLike): Input observations.
        title (Optional[str]): Optional chart title.
        xlabel (Optional[str]): Optional x-axis label.
        ylabel (str): Y-axis label.
        figsize (FigureSize): Matplotlib figure size.
        color (Optional[str]): Optional line color.
        linewidth (float): Line width.
        marker (Optional[str]): Optional marker style.
        theme (str): Styling theme name.
        grid (bool): Whether to show grid lines.
        **kwargs: Additional keyword arguments forwarded to ``Axes.step``.

    Returns:
        matplotlib.axes.Axes: Axes containing the ECDF chart.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If no non-missing numeric observations remain.

    Examples:
        ```python
        ax = ecdf_plot_static(data)
        ```

    Notes:
        ECDF plots avoid binning and are useful for comparing distribution tails.
    """
    values, probabilities = ecdf_values(data)
    ax = setup_plot(
        title=title or "Empirical CDF",
        xlabel=xlabel or "Value",
        ylabel=ylabel,
        figsize=figsize,
    )[1]
    ax.step(values, probabilities, where="post", color=color, linewidth=linewidth, marker=marker, **kwargs)
    if grid:
        ax.grid(True, alpha=0.3)
    apply_theme(ax, theme)
    return ax


def ecdf_plot_interactive(
    data: SeriesLike,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: str = "Cumulative Probability",
    color: Optional[str] = None,
    template: str = "plotly",
    height: int = 600,
    width: int = 1000,
    **kwargs,
) -> PlotlyFigure:
    """Create an interactive empirical cumulative distribution plot.

    Args:
        data (SeriesLike): Input observations.
        title (Optional[str]): Optional chart title.
        xlabel (Optional[str]): Optional x-axis label.
        ylabel (str): Y-axis label.
        color (Optional[str]): Optional line color.
        template (str): Plotly template name.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.
        **kwargs: Additional keyword arguments forwarded to ``go.Scatter``.

    Returns:
        plotly.graph_objects.Figure: Interactive ECDF chart.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If no non-missing numeric observations remain.

    Examples:
        ```python
        fig = ecdf_plot_interactive(data)
        ```

    Notes:
        The line shape uses Plotly's horizontal-vertical step mode.
    """
    values, probabilities = ecdf_values(data)
    fig = go.Figure(
        go.Scatter(
            x=values,
            y=probabilities,
            mode="lines",
            line=dict(color=color, shape="hv"),
            **kwargs,
        )
    )
    fig.update_layout(
        title=title or "Empirical CDF",
        xaxis_title=xlabel or "Value",
        yaxis_title=ylabel,
        template=template,
        height=height,
        width=width,
    )
    return fig


def cumulative_histogram_static(
    data: SeriesLike,
    bins: int = 30,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: str = "Cumulative Count",
    figsize: FigureSize = (10, 6),
    color: Optional[str] = None,
    alpha: float = 0.7,
    density: bool = False,
    theme: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Create a static cumulative histogram for one numeric variable.

    Args:
        data (SeriesLike): Input observations.
        bins (int): Number of histogram bins.
        title (Optional[str]): Optional chart title.
        xlabel (Optional[str]): Optional x-axis label.
        ylabel (str): Y-axis label.
        figsize (FigureSize): Matplotlib figure size.
        color (Optional[str]): Optional bar color.
        alpha (float): Bar opacity.
        density (bool): Whether to normalize cumulative counts to density.
        theme (str): Styling theme name.
        **kwargs: Additional keyword arguments forwarded to ``Axes.hist``.

    Returns:
        matplotlib.axes.Axes: Axes containing the cumulative histogram.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If ``bins`` is not positive or no observations remain.

    Examples:
        ```python
        ax = cumulative_histogram_static(data, bins=20)
        ```

    Notes:
        Cumulative histograms emphasize accumulation across a measurement scale.
    """
    validate_positive_int(bins, "bins")
    values = as_numeric_series(data)
    ax = setup_plot(title=title or "Cumulative Histogram", xlabel=xlabel or values.name, ylabel=ylabel, figsize=figsize)[1]
    ax.hist(values, bins=bins, cumulative=True, density=density, color=color, alpha=alpha, **kwargs)
    ax.grid(True, axis="y", alpha=0.3)
    apply_theme(ax, theme)
    return ax


def cumulative_histogram_interactive(
    data: SeriesLike,
    bins: int = 30,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: str = "Cumulative Count",
    color: Optional[str] = None,
    alpha: float = 0.7,
    histnorm: Optional[str] = None,
    template: str = "plotly",
    height: int = 600,
    width: int = 1000,
    **kwargs,
) -> PlotlyFigure:
    """Create an interactive cumulative histogram for one numeric variable.

    Args:
        data (SeriesLike): Input observations.
        bins (int): Number of histogram bins.
        title (Optional[str]): Optional chart title.
        xlabel (Optional[str]): Optional x-axis label.
        ylabel (str): Y-axis label.
        color (Optional[str]): Optional bar color.
        alpha (float): Bar opacity.
        histnorm (Optional[str]): Optional Plotly histogram normalization.
        template (str): Plotly template name.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.
        **kwargs: Additional keyword arguments forwarded to ``go.Histogram``.

    Returns:
        plotly.graph_objects.Figure: Interactive cumulative histogram.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If ``bins`` is not positive or no observations remain.

    Examples:
        ```python
        fig = cumulative_histogram_interactive(data)
        ```

    Notes:
        Plotly handles cumulative aggregation through the trace ``cumulative`` option.
    """
    validate_positive_int(bins, "bins")
    values = as_numeric_series(data)
    fig = go.Figure(
        go.Histogram(
            x=values,
            nbinsx=bins,
            cumulative=dict(enabled=True),
            histnorm=histnorm,
            marker_color=color,
            opacity=alpha,
            **kwargs,
        )
    )
    fig.update_layout(
        title=title or "Cumulative Histogram",
        xaxis_title=xlabel or values.name,
        yaxis_title=ylabel,
        template=template,
        height=height,
        width=width,
    )
    return fig


def qq_plot_static(
    data: SeriesLike,
    distribution: str = "norm",
    title: Optional[str] = None,
    figsize: FigureSize = (8, 8),
    color: Optional[str] = None,
    reference_color: str = "crimson",
    theme: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Create a static quantile-quantile plot against a theoretical distribution.

    Args:
        data (SeriesLike): Input observations.
        distribution (str): SciPy distribution name used as the theoretical reference.
        title (Optional[str]): Optional chart title.
        figsize (FigureSize): Matplotlib figure size.
        color (Optional[str]): Optional marker color.
        reference_color (str): Reference line color.
        theme (str): Styling theme name.
        **kwargs: Additional keyword arguments forwarded to ``Axes.scatter``.

    Returns:
        matplotlib.axes.Axes: Axes containing the QQ plot.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If no observations remain or the distribution name is invalid.

    Examples:
        ```python
        ax = qq_plot_static(data, distribution="norm")
        ```

    Notes:
        Points close to the reference line indicate compatibility with the selected distribution.
    """
    values = as_numeric_series(data).to_numpy(dtype=float)
    if not hasattr(stats, distribution):
        raise ValueError(f"Unknown scipy.stats distribution: {distribution!r}.")
    theoretical, ordered = stats.probplot(values, dist=distribution, fit=False)
    slope, intercept, _ = stats.probplot(values, dist=distribution, fit=True)[1]
    ax = setup_plot(title=title or f"QQ Plot ({distribution})", xlabel="Theoretical Quantiles", ylabel="Sample Quantiles", figsize=figsize)[1]
    ax.scatter(theoretical, ordered, color=color, **kwargs)
    line_x = np.asarray([min(theoretical), max(theoretical)])
    ax.plot(line_x, intercept + slope * line_x, color=reference_color, linestyle="--")
    ax.grid(True, alpha=0.3)
    apply_theme(ax, theme)
    return ax


def qq_plot_interactive(
    data: SeriesLike,
    distribution: str = "norm",
    title: Optional[str] = None,
    color: Optional[str] = None,
    reference_color: str = "crimson",
    template: str = "plotly",
    height: int = 700,
    width: int = 700,
    **kwargs,
) -> PlotlyFigure:
    """Create an interactive quantile-quantile plot against a theoretical distribution.

    Args:
        data (SeriesLike): Input observations.
        distribution (str): SciPy distribution name used as the theoretical reference.
        title (Optional[str]): Optional chart title.
        color (Optional[str]): Optional marker color.
        reference_color (str): Reference line color.
        template (str): Plotly template name.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.
        **kwargs: Additional keyword arguments forwarded to ``go.Scatter``.

    Returns:
        plotly.graph_objects.Figure: Interactive QQ plot.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If no observations remain or the distribution name is invalid.

    Examples:
        ```python
        fig = qq_plot_interactive(data)
        ```

    Notes:
        Hover data exposes paired theoretical and sample quantiles.
    """
    values = as_numeric_series(data).to_numpy(dtype=float)
    if not hasattr(stats, distribution):
        raise ValueError(f"Unknown scipy.stats distribution: {distribution!r}.")
    theoretical, ordered = stats.probplot(values, dist=distribution, fit=False)
    slope, intercept, _ = stats.probplot(values, dist=distribution, fit=True)[1]
    line_x = np.asarray([min(theoretical), max(theoretical)])
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=theoretical, y=ordered, mode="markers", marker=dict(color=color), name="Observed", **kwargs))
    fig.add_trace(
        go.Scatter(
            x=line_x,
            y=intercept + slope * line_x,
            mode="lines",
            line=dict(color=reference_color, dash="dash"),
            name="Reference",
        )
    )
    fig.update_layout(
        title=title or f"QQ Plot ({distribution})",
        xaxis_title="Theoretical Quantiles",
        yaxis_title="Sample Quantiles",
        template=template,
        height=height,
        width=width,
    )
    return fig


def pp_plot_static(
    data: SeriesLike,
    distribution: str = "norm",
    title: Optional[str] = None,
    figsize: FigureSize = (8, 8),
    color: Optional[str] = None,
    reference_color: str = "crimson",
    theme: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Create a static probability-probability plot.

    Args:
        data (SeriesLike): Input observations.
        distribution (str): SciPy distribution name used as the theoretical reference.
        title (Optional[str]): Optional chart title.
        figsize (FigureSize): Matplotlib figure size.
        color (Optional[str]): Optional marker color.
        reference_color (str): Reference line color.
        theme (str): Styling theme name.
        **kwargs: Additional keyword arguments forwarded to ``Axes.scatter``.

    Returns:
        matplotlib.axes.Axes: Axes containing the PP plot.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If no observations remain or the distribution name is invalid.

    Examples:
        ```python
        ax = pp_plot_static(data)
        ```

    Notes:
        PP plots compare cumulative probabilities rather than quantiles.
    """
    values = np.sort(as_numeric_series(data).to_numpy(dtype=float))
    if not hasattr(stats, distribution):
        raise ValueError(f"Unknown scipy.stats distribution: {distribution!r}.")
    distribution_obj = getattr(stats, distribution)
    params = distribution_obj.fit(values)
    theoretical = distribution_obj.cdf(values, *params)
    empirical = np.arange(1, len(values) + 1) / len(values)
    ax = setup_plot(title=title or f"PP Plot ({distribution})", xlabel="Theoretical Probability", ylabel="Empirical Probability", figsize=figsize)[1]
    ax.scatter(theoretical, empirical, color=color, **kwargs)
    ax.plot([0, 1], [0, 1], color=reference_color, linestyle="--")
    ax.grid(True, alpha=0.3)
    apply_theme(ax, theme)
    return ax


def pp_plot_interactive(
    data: SeriesLike,
    distribution: str = "norm",
    title: Optional[str] = None,
    color: Optional[str] = None,
    reference_color: str = "crimson",
    template: str = "plotly",
    height: int = 700,
    width: int = 700,
    **kwargs,
) -> PlotlyFigure:
    """Create an interactive probability-probability plot.

    Args:
        data (SeriesLike): Input observations.
        distribution (str): SciPy distribution name used as the theoretical reference.
        title (Optional[str]): Optional chart title.
        color (Optional[str]): Optional marker color.
        reference_color (str): Reference line color.
        template (str): Plotly template name.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.
        **kwargs: Additional keyword arguments forwarded to ``go.Scatter``.

    Returns:
        plotly.graph_objects.Figure: Interactive PP plot.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If no observations remain or the distribution name is invalid.

    Examples:
        ```python
        fig = pp_plot_interactive(data)
        ```

    Notes:
        The 45-degree reference line represents perfect distributional agreement.
    """
    values = np.sort(as_numeric_series(data).to_numpy(dtype=float))
    if not hasattr(stats, distribution):
        raise ValueError(f"Unknown scipy.stats distribution: {distribution!r}.")
    distribution_obj = getattr(stats, distribution)
    params = distribution_obj.fit(values)
    theoretical = distribution_obj.cdf(values, *params)
    empirical = np.arange(1, len(values) + 1) / len(values)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=theoretical, y=empirical, mode="markers", marker=dict(color=color), name="Observed", **kwargs))
    fig.add_trace(
        go.Scatter(
            x=[0, 1],
            y=[0, 1],
            mode="lines",
            line=dict(color=reference_color, dash="dash"),
            name="Reference",
        )
    )
    fig.update_layout(
        title=title or f"PP Plot ({distribution})",
        xaxis_title="Theoretical Probability",
        yaxis_title="Empirical Probability",
        template=template,
        height=height,
        width=width,
    )
    return fig
