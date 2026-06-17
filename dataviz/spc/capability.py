"""Process capability analysis for SPC."""

from dataclasses import dataclass
from math import erf, sqrt
from typing import Optional, Tuple

import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go

from ..types import ArrayLike, FigureSize, MatplotlibAxes, PlotlyFigure
from ..utils import apply_theme, setup_plot
from .rules import as_numeric_series


@dataclass(frozen=True)
class CapabilityStats:
    """Process capability statistics.

    Args:
        n (int): Number of observations.
        mean (float): Process mean.
        std (float): Sample standard deviation.
        lsl (Optional[float]): Lower specification limit.
        usl (Optional[float]): Upper specification limit.
        cp (Optional[float]): Potential capability index.
        cpk (Optional[float]): Centered capability index.
        ppm_below (Optional[float]): Parts per million below LSL.
        ppm_above (Optional[float]): Parts per million above USL.
        ppm_below_normal (Optional[float]): Normal-theory parts per million below LSL.
        ppm_above_normal (Optional[float]): Normal-theory parts per million above USL.
        ppm_total_normal (Optional[float]): Total normal-theory parts per million outside specifications.

    Returns:
        CapabilityStats: Immutable capability summary.

    Raises:
        TypeError: If values cannot be converted to numeric statistics.
        ValueError: If specification limits are invalid.

    Examples:
        ```python
        stats = dv.spc.capability_summary(values, lsl=9.5, usl=10.5)
        ```

    Notes:
        PPM estimates include empirical observed values and normal-theory estimates.
    """

    n: int
    mean: float
    std: float
    lsl: Optional[float]
    usl: Optional[float]
    cp: Optional[float]
    cpk: Optional[float]
    ppm_below: Optional[float]
    ppm_above: Optional[float]
    ppm_below_normal: Optional[float]
    ppm_above_normal: Optional[float]
    ppm_total_normal: Optional[float]


def _normal_cdf(value: float, mean: float, std: float) -> float:
    """Evaluate a normal cumulative distribution function.

    Args:
        value (float): Value at which to evaluate the CDF.
        mean (float): Normal distribution mean.
        std (float): Normal distribution standard deviation.

    Returns:
        float: Cumulative probability at ``value``.

    Raises:
        TypeError: If inputs cannot be represented as floats.
        ValueError: If standard deviation is not positive.

    Examples:
        ```python
        probability = _normal_cdf(10.0, mean=9.5, std=0.2)
        ```

    Notes:
        This implementation uses ``math.erf`` to avoid a SciPy dependency.
    """
    if std <= 0:
        raise ValueError("std must be greater than zero.")
    z = (value - mean) / (std * sqrt(2.0))
    return 0.5 * (1.0 + erf(z))


def capability_summary(data: ArrayLike, lsl: Optional[float] = None, usl: Optional[float] = None) -> CapabilityStats:
    """Compute process capability statistics.

    Args:
        data (ArrayLike): Process observations.
        lsl (Optional[float]): Lower specification limit.
        usl (Optional[float]): Upper specification limit.

    Returns:
        CapabilityStats: Capability summary with Cp, Cpk, and empirical PPM values.

    Raises:
        TypeError: If data cannot be converted to numeric observations.
        ValueError: If specification limits are missing or invalid for requested indexes.

    Examples:
        ```python
        stats = dv.spc.capability_summary(values, lsl=9.5, usl=10.5)
        ```

    Notes:
        Cp requires both specification limits; Cpk can use one or both.
    """
    values = as_numeric_series(data)
    if lsl is not None and usl is not None and lsl >= usl:
        raise ValueError("lsl must be less than usl.")
    mean = float(values.mean())
    std = float(values.std(ddof=1)) if len(values) > 1 else 0.0
    cp = (float(usl) - float(lsl)) / (6 * std) if lsl is not None and usl is not None and std > 0 else None
    cpu = (float(usl) - mean) / (3 * std) if usl is not None and std > 0 else None
    cpl = (mean - float(lsl)) / (3 * std) if lsl is not None and std > 0 else None
    cpk_values = [value for value in (cpu, cpl) if value is not None]
    cpk = min(cpk_values) if cpk_values else None
    ppm_below = float((values < lsl).mean() * 1_000_000) if lsl is not None else None
    ppm_above = float((values > usl).mean() * 1_000_000) if usl is not None else None
    ppm_below_normal = float(_normal_cdf(float(lsl), mean, std) * 1_000_000) if lsl is not None and std > 0 else None
    ppm_above_normal = float((1.0 - _normal_cdf(float(usl), mean, std)) * 1_000_000) if usl is not None and std > 0 else None
    ppm_total_normal = sum(value for value in (ppm_below_normal, ppm_above_normal) if value is not None)
    if ppm_below_normal is None and ppm_above_normal is None:
        ppm_total_normal = None
    return CapabilityStats(len(values), mean, std, lsl, usl, cp, cpk, ppm_below, ppm_above, ppm_below_normal, ppm_above_normal, ppm_total_normal)


def _normal_curve(values: ArrayLike, mean: float, std: float) -> Tuple[np.ndarray, np.ndarray]:
    """Generate a fitted normal-density curve.

    Args:
        values (ArrayLike): Process observations.
        mean (float): Mean of the fitted normal curve.
        std (float): Standard deviation of the fitted normal curve.

    Returns:
        Tuple[numpy.ndarray, numpy.ndarray]: X and y values for a normal density curve.

    Raises:
        TypeError: If values cannot be converted to numeric observations.
        ValueError: If standard deviation is not positive.

    Examples:
        ```python
        xs, ys = _normal_curve(values, mean, std)
        ```

    Notes:
        The curve extends across the observed data range.
    """
    if std <= 0:
        raise ValueError("std must be greater than zero.")
    array = np.asarray(values, dtype=float)
    xs = np.linspace(float(np.min(array)), float(np.max(array)), 200)
    ys = (1 / (std * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((xs - mean) / std) ** 2)
    return xs, ys


def capability_histogram_static(
    data: ArrayLike,
    lsl: Optional[float] = None,
    usl: Optional[float] = None,
    bins: int = 30,
    title: str = "Process Capability Histogram",
    figsize: FigureSize = (12, 6),
    theme: str = "default",
) -> MatplotlibAxes:
    """Create a static capability histogram with specification limits.

    Args:
        data (ArrayLike): Process observations.
        lsl (Optional[float]): Lower specification limit.
        usl (Optional[float]): Upper specification limit.
        bins (int): Number of histogram bins.
        title (str): Chart title.
        figsize (FigureSize): Figure size in inches.
        theme (str): Named style theme.

    Returns:
        matplotlib.axes.Axes: Capability histogram axes.

    Raises:
        TypeError: If data cannot be converted to numeric observations.
        ValueError: If specification limits are invalid.

    Examples:
        ```python
        ax = dv.spc.capability_histogram_static(values, lsl=9.5, usl=10.5)
        ```

    Notes:
        A fitted normal density curve is added when standard deviation is positive.
    """
    values = as_numeric_series(data)
    stats = capability_summary(values, lsl=lsl, usl=usl)
    _, ax = setup_plot(figsize=figsize, title=title, xlabel="Value", ylabel="Density")
    ax.hist(values, bins=bins, density=True, alpha=0.65, color="steelblue", edgecolor="black", label="Observed")
    if stats.std > 0:
        xs, ys = _normal_curve(values, stats.mean, stats.std)
        ax.plot(xs, ys, color="crimson", linewidth=2, label="Normal fit")
    if lsl is not None:
        ax.axvline(lsl, color="red", linestyle="--", label="LSL")
    if usl is not None:
        ax.axvline(usl, color="red", linestyle="--", label="USL")
    subtitle = []
    if stats.cp is not None:
        subtitle.append(f"Cp={stats.cp:.3f}")
    if stats.cpk is not None:
        subtitle.append(f"Cpk={stats.cpk:.3f}")
    if subtitle:
        ax.set_title(f"{title} ({', '.join(subtitle)})")
    ax.legend()
    apply_theme(ax, theme)
    return ax


def capability_histogram_interactive(
    data: ArrayLike,
    lsl: Optional[float] = None,
    usl: Optional[float] = None,
    bins: int = 30,
    title: str = "Process Capability Histogram",
    template: str = "plotly",
    height: int = 600,
    width: int = 1000,
) -> PlotlyFigure:
    """Create an interactive capability histogram with specification limits.

    Args:
        data (ArrayLike): Process observations.
        lsl (Optional[float]): Lower specification limit.
        usl (Optional[float]): Upper specification limit.
        bins (int): Number of histogram bins.
        title (str): Chart title.
        template (str): Plotly template.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.

    Returns:
        plotly.graph_objects.Figure: Interactive capability histogram.

    Raises:
        TypeError: If data cannot be converted to numeric observations.
        ValueError: If specification limits are invalid.

    Examples:
        ```python
        fig = dv.spc.capability_histogram_interactive(values, lsl=9.5, usl=10.5)
        ```

    Notes:
        Cp and Cpk are included in the title when available.
    """
    values = as_numeric_series(data)
    stats = capability_summary(values, lsl=lsl, usl=usl)
    title_bits = [title]
    if stats.cp is not None:
        title_bits.append(f"Cp={stats.cp:.3f}")
    if stats.cpk is not None:
        title_bits.append(f"Cpk={stats.cpk:.3f}")
    fig = go.Figure(data=[go.Histogram(x=values, nbinsx=bins, histnorm="probability density", name="Observed")])
    if stats.std > 0:
        xs, ys = _normal_curve(values, stats.mean, stats.std)
        fig.add_trace(go.Scatter(x=xs, y=ys, mode="lines", name="Normal fit", line=dict(color="crimson")))
    if lsl is not None:
        fig.add_vline(x=lsl, line_color="red", line_dash="dash", annotation_text="LSL")
    if usl is not None:
        fig.add_vline(x=usl, line_color="red", line_dash="dash", annotation_text="USL")
    fig.update_layout(title=" | ".join(title_bits), xaxis_title="Value", yaxis_title="Density", template=template, height=height, width=width)
    return fig
