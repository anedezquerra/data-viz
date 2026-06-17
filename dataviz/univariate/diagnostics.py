"""Diagnostic plots and normality checks for one variable."""

from dataclasses import dataclass
from typing import Literal, Optional

import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy import stats

from ..types import FigureSize, MatplotlibAxes, MatplotlibFigure, PlotlyFigure, SeriesLike
from ..utils import apply_theme, setup_plot, validate_positive_int
from .stats import as_numeric_series, iqr_outliers, percentile_table, univariate_summary, zscore_outliers

OutlierMethod = Literal["iqr", "zscore"]
NormalityMethod = Literal["shapiro", "normaltest"]


@dataclass(frozen=True)
class NormalityTestResult:
    """Normality test result for one variable.

    Args:
        statistic (float): Test statistic.
        p_value (float): Test p-value.
        method (str): Normality test method.
        is_normal (bool): Whether ``p_value`` is greater than or equal to ``alpha``.
        alpha (float): Significance threshold used for the decision.

    Returns:
        NormalityTestResult: Immutable normality test summary.

    Raises:
        TypeError: If values cannot be represented in the declared fields.
        ValueError: If fields are incompatible with downstream numeric use.

    Examples:
        ```python
        result = NormalityTestResult(0.98, 0.42, "shapiro", True, 0.05)
        ```

    Notes:
        Statistical tests are most useful when paired with QQ or PP plots.
    """

    statistic: float
    p_value: float
    method: str
    is_normal: bool
    alpha: float


def normality_test(
    data: SeriesLike,
    method: NormalityMethod = "shapiro",
    alpha: float = 0.05,
) -> NormalityTestResult:
    """Run a normality test for one numeric variable.

    Args:
        data (SeriesLike): Input observations.
        method (NormalityMethod): Test method, either ``"shapiro"`` or ``"normaltest"``.
        alpha (float): Significance threshold used for the normality decision.

    Returns:
        NormalityTestResult: Statistic, p-value, method, and decision.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If ``method`` or ``alpha`` is invalid, or too few observations are available.

    Examples:
        ```python
        result = normality_test(data, method="shapiro")
        ```

    Notes:
        Shapiro-Wilk requires at least three observations; D'Agostino-Pearson requires at least eight.
    """
    if alpha <= 0 or alpha >= 1:
        raise ValueError("alpha must be between 0 and 1.")
    values = as_numeric_series(data).to_numpy(dtype=float)
    if method == "shapiro":
        if len(values) < 3:
            raise ValueError("Shapiro-Wilk normality test requires at least 3 observations.")
        statistic, p_value = stats.shapiro(values)
    elif method == "normaltest":
        if len(values) < 8:
            raise ValueError("D'Agostino-Pearson normality test requires at least 8 observations.")
        statistic, p_value = stats.normaltest(values)
    else:
        raise ValueError("method must be either 'shapiro' or 'normaltest'.")
    p_value_float = float(p_value)
    return NormalityTestResult(
        statistic=float(statistic),
        p_value=p_value_float,
        method=method,
        is_normal=p_value_float >= alpha,
        alpha=alpha,
    )


def outlier_plot_static(
    data: SeriesLike,
    method: OutlierMethod = "iqr",
    threshold: float = 3.0,
    multiplier: float = 1.5,
    title: Optional[str] = None,
    xlabel: str = "Observation",
    ylabel: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    color: Optional[str] = None,
    outlier_color: str = "crimson",
    theme: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Create a static index plot that highlights univariate outliers.

    Args:
        data (SeriesLike): Input observations.
        method (OutlierMethod): Outlier rule, either ``"iqr"`` or ``"zscore"``.
        threshold (float): Z-score threshold when ``method="zscore"``.
        multiplier (float): IQR multiplier when ``method="iqr"``.
        title (Optional[str]): Optional chart title.
        xlabel (str): X-axis label.
        ylabel (Optional[str]): Optional y-axis label.
        figsize (FigureSize): Matplotlib figure size.
        color (Optional[str]): Regular point color.
        outlier_color (str): Highlight color for outlier points.
        theme (str): Styling theme name.
        **kwargs: Additional keyword arguments forwarded to ``Axes.scatter``.

    Returns:
        matplotlib.axes.Axes: Axes containing the outlier diagnostic plot.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If the selected outlier rule or threshold is invalid.

    Examples:
        ```python
        ax = outlier_plot_static(data, method="iqr")
        ```

    Notes:
        The x-axis is the cleaned observation order after missing values are removed.
    """
    values = as_numeric_series(data)
    if method == "iqr":
        mask = iqr_outliers(values, multiplier=multiplier)
    elif method == "zscore":
        mask = zscore_outliers(values, threshold=threshold)
    else:
        raise ValueError("method must be either 'iqr' or 'zscore'.")
    ax = setup_plot(title=title or "Outlier Diagnostic", xlabel=xlabel, ylabel=ylabel or values.name, figsize=figsize)[1]
    positions = np.arange(len(values))
    ax.scatter(positions[~mask], values[~mask], color=color, label="Observation", **kwargs)
    if mask.any():
        ax.scatter(positions[mask], values[mask], color=outlier_color, label="Outlier", **kwargs)
    ax.legend()
    ax.grid(True, alpha=0.3)
    apply_theme(ax, theme)
    return ax


def outlier_plot_interactive(
    data: SeriesLike,
    method: OutlierMethod = "iqr",
    threshold: float = 3.0,
    multiplier: float = 1.5,
    title: Optional[str] = None,
    xlabel: str = "Observation",
    ylabel: Optional[str] = None,
    color: Optional[str] = None,
    outlier_color: str = "crimson",
    template: str = "plotly",
    height: int = 600,
    width: int = 1000,
    **kwargs,
) -> PlotlyFigure:
    """Create an interactive index plot that highlights univariate outliers.

    Args:
        data (SeriesLike): Input observations.
        method (OutlierMethod): Outlier rule, either ``"iqr"`` or ``"zscore"``.
        threshold (float): Z-score threshold when ``method="zscore"``.
        multiplier (float): IQR multiplier when ``method="iqr"``.
        title (Optional[str]): Optional chart title.
        xlabel (str): X-axis label.
        ylabel (Optional[str]): Optional y-axis label.
        color (Optional[str]): Regular point color.
        outlier_color (str): Highlight color for outlier points.
        template (str): Plotly template name.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.
        **kwargs: Additional keyword arguments forwarded to ``go.Scatter``.

    Returns:
        plotly.graph_objects.Figure: Interactive outlier diagnostic plot.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If the selected outlier rule or threshold is invalid.

    Examples:
        ```python
        fig = outlier_plot_interactive(data)
        ```

    Notes:
        Hover labels make it easy to inspect extreme observations by index.
    """
    values = as_numeric_series(data)
    if method == "iqr":
        mask = iqr_outliers(values, multiplier=multiplier)
    elif method == "zscore":
        mask = zscore_outliers(values, threshold=threshold)
    else:
        raise ValueError("method must be either 'iqr' or 'zscore'.")
    positions = np.arange(len(values))
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=positions[~mask],
            y=values[~mask],
            mode="markers",
            name="Observation",
            marker=dict(color=color),
            **kwargs,
        )
    )
    if mask.any():
        fig.add_trace(
            go.Scatter(
                x=positions[mask],
                y=values[mask],
                mode="markers",
                name="Outlier",
                marker=dict(color=outlier_color),
                **kwargs,
            )
        )
    fig.update_layout(
        title=title or "Outlier Diagnostic",
        xaxis_title=xlabel,
        yaxis_title=ylabel or values.name,
        template=template,
        height=height,
        width=width,
    )
    return fig


def percentile_plot_static(
    data: SeriesLike,
    step: int = 5,
    title: Optional[str] = None,
    xlabel: str = "Percentile",
    ylabel: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    color: Optional[str] = None,
    marker: str = "o",
    theme: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Create a static percentile profile plot.

    Args:
        data (SeriesLike): Input observations.
        step (int): Percentile interval between points.
        title (Optional[str]): Optional chart title.
        xlabel (str): X-axis label.
        ylabel (Optional[str]): Optional y-axis label.
        figsize (FigureSize): Matplotlib figure size.
        color (Optional[str]): Optional line color.
        marker (str): Marker style.
        theme (str): Styling theme name.
        **kwargs: Additional keyword arguments forwarded to ``Axes.plot``.

    Returns:
        matplotlib.axes.Axes: Axes containing the percentile profile.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If ``step`` is invalid or no observations remain.

    Examples:
        ```python
        ax = percentile_plot_static(data, step=10)
        ```

    Notes:
        Percentile profiles provide a compact view of distribution shape.
    """
    table = percentile_table(data, step=step)
    ax = setup_plot(title=title or "Percentile Profile", xlabel=xlabel, ylabel=ylabel or "Value", figsize=figsize)[1]
    ax.plot(table["percentile"], table["value"], color=color, marker=marker, **kwargs)
    ax.grid(True, alpha=0.3)
    apply_theme(ax, theme)
    return ax


def percentile_plot_interactive(
    data: SeriesLike,
    step: int = 5,
    title: Optional[str] = None,
    xlabel: str = "Percentile",
    ylabel: Optional[str] = None,
    color: Optional[str] = None,
    template: str = "plotly",
    height: int = 600,
    width: int = 1000,
    **kwargs,
) -> PlotlyFigure:
    """Create an interactive percentile profile plot.

    Args:
        data (SeriesLike): Input observations.
        step (int): Percentile interval between points.
        title (Optional[str]): Optional chart title.
        xlabel (str): X-axis label.
        ylabel (Optional[str]): Optional y-axis label.
        color (Optional[str]): Optional line color.
        template (str): Plotly template name.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.
        **kwargs: Additional keyword arguments forwarded to ``go.Scatter``.

    Returns:
        plotly.graph_objects.Figure: Interactive percentile profile.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If ``step`` is invalid or no observations remain.

    Examples:
        ```python
        fig = percentile_plot_interactive(data, step=10)
        ```

    Notes:
        Percentile values are available in hover labels.
    """
    table = percentile_table(data, step=step)
    fig = go.Figure(
        go.Scatter(
            x=table["percentile"],
            y=table["value"],
            mode="lines+markers",
            line=dict(color=color),
            **kwargs,
        )
    )
    fig.update_layout(
        title=title or "Percentile Profile",
        xaxis_title=xlabel,
        yaxis_title=ylabel or "Value",
        template=template,
        height=height,
        width=width,
    )
    return fig


def univariate_diagnostic_panel_static(
    data: SeriesLike,
    bins: int = 30,
    title: Optional[str] = None,
    figsize: FigureSize = (12, 8),
    color: Optional[str] = None,
    theme: str = "default",
) -> MatplotlibFigure:
    """Create a static four-panel univariate diagnostic figure.

    Args:
        data (SeriesLike): Input observations.
        bins (int): Number of histogram bins.
        title (Optional[str]): Optional figure title.
        figsize (FigureSize): Matplotlib figure size.
        color (Optional[str]): Optional primary color.
        theme (str): Styling theme name.

    Returns:
        matplotlib.figure.Figure: Figure containing histogram, box plot, QQ plot, and percentile profile.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If no observations remain or ``bins`` is invalid.

    Examples:
        ```python
        fig = univariate_diagnostic_panel_static(data)
        ```

    Notes:
        This panel is designed as a compact first-pass inspection tool.
    """
    validate_positive_int(bins, "bins")
    values = as_numeric_series(data)
    summary = univariate_summary(values)
    fig, axes = plt.subplots(2, 2, figsize=figsize)
    fig.suptitle(title or f"Univariate Diagnostics (n={summary.count})")
    axes[0, 0].hist(values, bins=bins, color=color, alpha=0.7, edgecolor="black")
    axes[0, 0].set_title("Histogram")
    axes[0, 1].boxplot(values, vert=True)
    axes[0, 1].set_title("Box Plot")
    theoretical, ordered = stats.probplot(values.to_numpy(dtype=float), dist="norm", fit=False)
    axes[1, 0].scatter(theoretical, ordered, color=color)
    axes[1, 0].set_title("QQ Plot")
    table = percentile_table(values, step=10)
    axes[1, 1].plot(table["percentile"], table["value"], marker="o", color=color)
    axes[1, 1].set_title("Percentile Profile")
    for ax in axes.ravel():
        ax.grid(True, alpha=0.3)
        apply_theme(ax, theme)
    fig.tight_layout()
    return fig


def univariate_diagnostic_panel_interactive(
    data: SeriesLike,
    bins: int = 30,
    title: Optional[str] = None,
    color: Optional[str] = None,
    template: str = "plotly",
    height: int = 800,
    width: int = 1000,
) -> PlotlyFigure:
    """Create an interactive four-panel univariate diagnostic figure.

    Args:
        data (SeriesLike): Input observations.
        bins (int): Number of histogram bins.
        title (Optional[str]): Optional figure title.
        color (Optional[str]): Optional primary color.
        template (str): Plotly template name.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.

    Returns:
        plotly.graph_objects.Figure: Interactive diagnostic panel.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If no observations remain or ``bins`` is invalid.

    Examples:
        ```python
        fig = univariate_diagnostic_panel_interactive(data)
        ```

    Notes:
        The panel combines distribution, spread, normality, and percentile diagnostics.
    """
    validate_positive_int(bins, "bins")
    values = as_numeric_series(data)
    summary = univariate_summary(values)
    theoretical, ordered = stats.probplot(values.to_numpy(dtype=float), dist="norm", fit=False)
    table = percentile_table(values, step=10)
    fig = make_subplots(
        rows=2,
        cols=2,
        subplot_titles=("Histogram", "Box Plot", "QQ Plot", "Percentile Profile"),
    )
    fig.add_trace(go.Histogram(x=values, nbinsx=bins, marker_color=color, name="Histogram"), row=1, col=1)
    fig.add_trace(go.Box(y=values, marker_color=color, name="Box"), row=1, col=2)
    fig.add_trace(go.Scatter(x=theoretical, y=ordered, mode="markers", marker=dict(color=color), name="QQ"), row=2, col=1)
    fig.add_trace(
        go.Scatter(x=table["percentile"], y=table["value"], mode="lines+markers", line=dict(color=color), name="Percentile"),
        row=2,
        col=2,
    )
    fig.update_layout(
        title=title or f"Univariate Diagnostics (n={summary.count})",
        template=template,
        height=height,
        width=width,
        showlegend=False,
    )
    return fig
