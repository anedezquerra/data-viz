"""Statistical bivariate analysis helpers and diagnostic charts."""

from dataclasses import dataclass
from typing import Literal, Optional, Tuple, Union

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objects as go

from ..types import FigureSize, MatplotlibAxes, PlotlyFigure, SeriesLike
from ..utils import apply_theme, resolve_xy_data, setup_plot, validate_positive_int
from ..utils.validation import NaPolicy


@dataclass(frozen=True)
class BivariateStats:
    """Summary statistics for a pair of variables.

    Args:
        n (int): Number of observations used in the calculations.
        missing_x (int): Count of missing x values in the original input.
        missing_y (int): Count of missing y values in the original input.
        pearson (float): Pearson correlation coefficient.
        spearman (float): Spearman rank correlation coefficient.
        covariance (float): Sample covariance between x and y.
        slope (float): Least-squares linear slope.
        intercept (float): Least-squares linear intercept.
        r_squared (float): Coefficient of determination for the linear fit.
        x_mean (float): Mean of x.
        y_mean (float): Mean of y.
        x_std (float): Sample standard deviation of x.
        y_std (float): Sample standard deviation of y.

    Returns:
        BivariateStats: Immutable bivariate summary object.

    Raises:
        TypeError: If values cannot be represented as numeric statistics.
        ValueError: If insufficient observations are available.

    Example:
        ```python
        stats = dv.bivariate.bivariate_summary(x, y)
        ```

    Notes:
        Instances are returned by ``bivariate_summary`` and by plotting functions with ``return_stats=True``.
    """

    n: int
    missing_x: int
    missing_y: int
    pearson: float
    spearman: float
    covariance: float
    slope: float
    intercept: float
    r_squared: float
    x_mean: float
    y_mean: float
    x_std: float
    y_std: float


def _label(values: object, fallback: str) -> str:
    """Return a plotting label from a named object or fallback text.

    Args:
        values (object): Object that may expose a ``name`` attribute.
        fallback (str): Label used when no name is available.

    Returns:
        str: Label for an axis, legend, or title.

    Raises:
        TypeError: If fallback cannot be represented as text.

    Example:
        ```python
        label = _label(series, "X")
        ```

    Notes:
        The helper keeps generated chart titles consistent.
    """
    return getattr(values, "name", None) or fallback


def _numeric_xy(
    x: Union[str, SeriesLike],
    y: Union[str, SeriesLike],
    data: Optional[pd.DataFrame],
    na_policy: NaPolicy,
) -> Tuple[pd.Series, pd.Series]:
    """Resolve paired x and y values as numeric series.

    Args:
        x (Union[str, SeriesLike]): X values or dataframe column name.
        y (Union[str, SeriesLike]): Y values or dataframe column name.
        data (Optional[pd.DataFrame]): Optional dataframe for column lookup.
        na_policy (NaPolicy): Missing-value behavior.

    Returns:
        Tuple[pandas.Series, pandas.Series]: Numeric x and y series.

    Raises:
        TypeError: If values cannot be resolved or converted to numeric.
        ValueError: If inputs are empty or lengths differ.

    Example:
        ```python
        x_values, y_values = _numeric_xy("a", "b", df, "drop")
        ```

    Notes:
        This wrapper centralizes numeric coercion for statistical charts.
    """
    return resolve_xy_data(x, y, data=data, na_policy=na_policy, require_numeric=True)


def _linear_fit(x: SeriesLike, y: SeriesLike, degree: int = 1) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Fit a polynomial model and return sorted predictions and residuals.

    Args:
        x (SeriesLike): Numeric x values.
        y (SeriesLike): Numeric y values.
        degree (int): Polynomial degree.

    Returns:
        Tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray]: Sorted x values, fitted y values, and residuals in original order.

    Raises:
        TypeError: If x or y cannot be converted to floats.
        ValueError: If there are too few observations for the polynomial degree.

    Example:
        ```python
        x_fit, y_fit, residuals = _linear_fit(x, y, 1)
        ```

    Notes:
        Residuals are aligned to the original input order.
    """
    x_values = np.asarray(x, dtype=float)
    y_values = np.asarray(y, dtype=float)
    coefficients = np.polyfit(x_values, y_values, deg=degree)
    fitted_original = np.polyval(coefficients, x_values)
    order = np.argsort(x_values)
    x_sorted = x_values[order]
    y_sorted_fit = np.polyval(coefficients, x_sorted)
    return x_sorted, y_sorted_fit, y_values - fitted_original


def _outlier_mask(values: pd.Series, method: Literal["zscore", "iqr"], threshold: float) -> pd.Series:
    """Identify outliers in one numeric series.

    Args:
        values (pd.Series): Numeric values to evaluate.
        method (Literal["zscore", "iqr"]): Outlier detection method.
        threshold (float): Z-score or IQR multiplier threshold.

    Returns:
        pandas.Series: Boolean mask where ``True`` identifies outliers.

    Raises:
        TypeError: If values cannot be evaluated numerically.
        ValueError: If method or threshold is invalid.

    Example:
        ```python
        mask = _outlier_mask(values, "iqr", 1.5)
        ```

    Notes:
        The public outlier scatter combines masks from both x and y.
    """
    if threshold <= 0:
        raise ValueError("threshold must be greater than zero.")
    if method == "zscore":
        std = values.std()
        if std == 0:
            return pd.Series(False, index=values.index)
        return ((values - values.mean()).abs() / std) > threshold
    if method == "iqr":
        q1 = values.quantile(0.25)
        q3 = values.quantile(0.75)
        iqr = q3 - q1
        return (values < q1 - threshold * iqr) | (values > q3 + threshold * iqr)
    raise ValueError("method must be 'zscore' or 'iqr'.")


def bivariate_summary(
    x: Union[str, SeriesLike],
    y: Union[str, SeriesLike],
    data: Optional[pd.DataFrame] = None,
    na_policy: NaPolicy = "drop",
) -> BivariateStats:
    """Compute a compact statistical summary for two numeric variables.

    Args:
        x (Union[str, SeriesLike]): X values or dataframe column name.
        y (Union[str, SeriesLike]): Y values or dataframe column name.
        data (Optional[pd.DataFrame]): Optional dataframe for column lookup.
        na_policy (NaPolicy): Missing-value behavior: ``"drop"``, ``"raise"``, or ``"keep"``.

    Returns:
        BivariateStats: Immutable summary with correlations, covariance, fit coefficients, and descriptive statistics.

    Raises:
        TypeError: If inputs cannot be resolved as numeric series.
        ValueError: If fewer than two observations are available.

    Example:
        ```python
        stats = dv.bivariate_summary("height", "weight", data=df)
        ```

    Notes:
        Spearman correlation is computed with pandas ranking, so no SciPy dependency is required.
    """
    raw_x = pd.Series(data[x] if isinstance(x, str) and data is not None else x)
    raw_y = pd.Series(data[y] if isinstance(y, str) and data is not None else y)
    x_values, y_values = _numeric_xy(x, y, data, na_policy)
    if len(x_values) < 2:
        raise ValueError("At least two observations are required.")
    coefficients = np.polyfit(x_values, y_values, deg=1)
    fitted = np.polyval(coefficients, x_values)
    residuals = np.asarray(y_values) - fitted
    total = np.asarray(y_values) - float(np.mean(y_values))
    ss_res = float(np.sum(residuals**2))
    ss_tot = float(np.sum(total**2))
    return BivariateStats(
        n=int(len(x_values)),
        missing_x=int(raw_x.isna().sum()),
        missing_y=int(raw_y.isna().sum()),
        pearson=float(pd.Series(x_values).corr(pd.Series(y_values), method="pearson")),
        spearman=float(pd.Series(x_values).corr(pd.Series(y_values), method="spearman")),
        covariance=float(np.cov(x_values, y_values, ddof=1)[0, 1]),
        slope=float(coefficients[0]),
        intercept=float(coefficients[1]),
        r_squared=float(1 - ss_res / ss_tot) if ss_tot else 0.0,
        x_mean=float(pd.Series(x_values).mean()),
        y_mean=float(pd.Series(y_values).mean()),
        x_std=float(pd.Series(x_values).std()),
        y_std=float(pd.Series(y_values).std()),
    )


def outlier_scatter_static(
    x: Union[str, SeriesLike],
    y: Union[str, SeriesLike],
    data: Optional[pd.DataFrame] = None,
    method: Literal["zscore", "iqr"] = "iqr",
    threshold: float = 1.5,
    title: str = "Outlier Scatter",
    figsize: FigureSize = (10, 6),
    normal_color: str = "steelblue",
    outlier_color: str = "crimson",
    theme: str = "default",
    na_policy: NaPolicy = "drop",
) -> MatplotlibAxes:
    """Create a static scatter plot highlighting bivariate outliers.

    Args:
        x (Union[str, SeriesLike]): X values or dataframe column name.
        y (Union[str, SeriesLike]): Y values or dataframe column name.
        data (Optional[pd.DataFrame]): Optional dataframe for column lookup.
        method (Literal["zscore", "iqr"]): Outlier detection method.
        threshold (float): Z-score threshold or IQR multiplier.
        title (str): Chart title.
        figsize (FigureSize): Figure size in inches.
        normal_color (str): Color for non-outlier observations.
        outlier_color (str): Color for outlier observations.
        theme (str): Named style theme.
        na_policy (NaPolicy): Missing-value behavior.

    Returns:
        matplotlib.axes.Axes: Scatter plot axes with outliers highlighted.

    Raises:
        TypeError: If inputs cannot be resolved as numeric series.
        ValueError: If threshold or method is invalid.

    Example:
        ```python
        ax = dv.bivariate.outlier_scatter_static(x, y, method="zscore", threshold=3)
        ```

    Notes:
        A point is highlighted when either its x or y value is considered an outlier.
    """
    x_values, y_values = _numeric_xy(x, y, data, na_policy)
    mask = _outlier_mask(x_values, method, threshold) | _outlier_mask(y_values, method, threshold)
    _, ax = setup_plot(figsize=figsize, title=title, xlabel=_label(x_values, "X"), ylabel=_label(y_values, "Y"))
    ax.scatter(x_values[~mask], y_values[~mask], color=normal_color, alpha=0.65, label="Typical")
    ax.scatter(x_values[mask], y_values[mask], color=outlier_color, alpha=0.9, label="Outlier")
    ax.legend()
    apply_theme(ax, theme)
    return ax


def outlier_scatter_interactive(
    x: Union[str, SeriesLike],
    y: Union[str, SeriesLike],
    data: Optional[pd.DataFrame] = None,
    method: Literal["zscore", "iqr"] = "iqr",
    threshold: float = 1.5,
    title: str = "Outlier Scatter",
    template: str = "plotly",
    height: int = 600,
    width: int = 900,
    na_policy: NaPolicy = "drop",
) -> PlotlyFigure:
    """Create an interactive scatter plot highlighting bivariate outliers.

    Args:
        x (Union[str, SeriesLike]): X values or dataframe column name.
        y (Union[str, SeriesLike]): Y values or dataframe column name.
        data (Optional[pd.DataFrame]): Optional dataframe for column lookup.
        method (Literal["zscore", "iqr"]): Outlier detection method.
        threshold (float): Z-score threshold or IQR multiplier.
        title (str): Chart title.
        template (str): Plotly template.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.
        na_policy (NaPolicy): Missing-value behavior.

    Returns:
        plotly.graph_objects.Figure: Interactive scatter plot with outliers highlighted.

    Raises:
        TypeError: If inputs cannot be resolved as numeric series.
        ValueError: If threshold or method is invalid.

    Example:
        ```python
        fig = dv.bivariate.outlier_scatter_interactive(x, y)
        ```

    Notes:
        Outlier labels are computed from x and y independently.
    """
    x_values, y_values = _numeric_xy(x, y, data, na_policy)
    mask = _outlier_mask(x_values, method, threshold) | _outlier_mask(y_values, method, threshold)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_values[~mask], y=y_values[~mask], mode="markers", name="Typical"))
    fig.add_trace(go.Scatter(x=x_values[mask], y=y_values[mask], mode="markers", name="Outlier", marker=dict(color="crimson")))
    fig.update_layout(title=title, xaxis_title=_label(x_values, "X"), yaxis_title=_label(y_values, "Y"), template=template, height=height, width=width)
    return fig


def residual_relationship_static(
    x: Union[str, SeriesLike],
    y: Union[str, SeriesLike],
    data: Optional[pd.DataFrame] = None,
    degree: int = 1,
    title: str = "Residual Relationship",
    figsize: FigureSize = (10, 6),
    theme: str = "default",
    na_policy: NaPolicy = "drop",
) -> MatplotlibAxes:
    """Create a static residual-vs-x plot after polynomial fitting.

    Args:
        x (Union[str, SeriesLike]): X values or dataframe column name.
        y (Union[str, SeriesLike]): Y values or dataframe column name.
        data (Optional[pd.DataFrame]): Optional dataframe for column lookup.
        degree (int): Polynomial degree for fitted values.
        title (str): Chart title.
        figsize (FigureSize): Figure size in inches.
        theme (str): Named style theme.
        na_policy (NaPolicy): Missing-value behavior.

    Returns:
        matplotlib.axes.Axes: Residual plot axes.

    Raises:
        TypeError: If inputs cannot be resolved as numeric series.
        ValueError: If degree is invalid for the available observations.

    Example:
        ```python
        ax = dv.bivariate.residual_relationship_static(x, y, degree=2)
        ```

    Notes:
        Patterns in residuals can reveal nonlinearity or heteroscedasticity.
    """
    validate_positive_int(degree, "degree")
    x_values, y_values = _numeric_xy(x, y, data, na_policy)
    _, _, residuals = _linear_fit(x_values, y_values, degree)
    _, ax = setup_plot(figsize=figsize, title=title, xlabel=_label(x_values, "X"), ylabel="Residual")
    ax.scatter(x_values, residuals, color="steelblue", alpha=0.7)
    ax.axhline(0, color="crimson", linestyle="--")
    apply_theme(ax, theme)
    return ax


def residual_relationship_interactive(
    x: Union[str, SeriesLike],
    y: Union[str, SeriesLike],
    data: Optional[pd.DataFrame] = None,
    degree: int = 1,
    title: str = "Residual Relationship",
    template: str = "plotly",
    height: int = 600,
    width: int = 900,
    na_policy: NaPolicy = "drop",
) -> PlotlyFigure:
    """Create an interactive residual-vs-x plot after polynomial fitting.

    Args:
        x (Union[str, SeriesLike]): X values or dataframe column name.
        y (Union[str, SeriesLike]): Y values or dataframe column name.
        data (Optional[pd.DataFrame]): Optional dataframe for column lookup.
        degree (int): Polynomial degree for fitted values.
        title (str): Chart title.
        template (str): Plotly template.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.
        na_policy (NaPolicy): Missing-value behavior.

    Returns:
        plotly.graph_objects.Figure: Interactive residual plot.

    Raises:
        TypeError: If inputs cannot be resolved as numeric series.
        ValueError: If degree is invalid for the available observations.

    Example:
        ```python
        fig = dv.bivariate.residual_relationship_interactive(x, y)
        ```

    Notes:
        The horizontal zero line marks perfect fitted values.
    """
    validate_positive_int(degree, "degree")
    x_values, y_values = _numeric_xy(x, y, data, na_policy)
    _, _, residuals = _linear_fit(x_values, y_values, degree)
    fig = go.Figure(data=[go.Scatter(x=x_values, y=residuals, mode="markers", name="Residual")])
    fig.add_hline(y=0, line_color="crimson", line_dash="dash")
    fig.update_layout(title=title, xaxis_title=_label(x_values, "X"), yaxis_title="Residual", template=template, height=height, width=width)
    return fig


def quantile_bin_plot_static(
    x: Union[str, SeriesLike],
    y: Union[str, SeriesLike],
    data: Optional[pd.DataFrame] = None,
    q: int = 10,
    statistic: Literal["mean", "median"] = "mean",
    title: str = "Quantile Bin Plot",
    figsize: FigureSize = (10, 6),
    theme: str = "default",
    na_policy: NaPolicy = "drop",
) -> MatplotlibAxes:
    """Create a static plot of y summaries across x quantile bins.

    Args:
        x (Union[str, SeriesLike]): X values or dataframe column name.
        y (Union[str, SeriesLike]): Y values or dataframe column name.
        data (Optional[pd.DataFrame]): Optional dataframe for column lookup.
        q (int): Number of quantile bins.
        statistic (Literal["mean", "median"]): Summary statistic to plot.
        title (str): Chart title.
        figsize (FigureSize): Figure size in inches.
        theme (str): Named style theme.
        na_policy (NaPolicy): Missing-value behavior.

    Returns:
        matplotlib.axes.Axes: Quantile-bin summary plot axes.

    Raises:
        TypeError: If inputs cannot be resolved as numeric series.
        ValueError: If quantile bins or statistic are invalid.

    Example:
        ```python
        ax = dv.bivariate.quantile_bin_plot_static(x, y, q=5, statistic="median")
        ```

    Notes:
        Quantile bins keep group sizes roughly balanced.
    """
    validate_positive_int(q, "q")
    x_values, y_values = _numeric_xy(x, y, data, na_policy)
    frame = pd.DataFrame({"x": x_values, "y": y_values})
    frame["bin"] = pd.qcut(frame["x"], q=q, duplicates="drop")
    grouped = frame.groupby("bin", observed=True)["y"]
    summary = grouped.mean() if statistic == "mean" else grouped.median()
    lower = grouped.quantile(0.25)
    upper = grouped.quantile(0.75)
    centers = [interval.mid for interval in summary.index]
    _, ax = setup_plot(figsize=figsize, title=title, xlabel=_label(x_values, "X"), ylabel=f"{statistic.title()} {_label(y_values, 'Y')}")
    ax.plot(centers, summary.values, marker="o", color="steelblue")
    ax.fill_between(centers, lower.values, upper.values, color="steelblue", alpha=0.2, label="IQR")
    ax.legend()
    apply_theme(ax, theme)
    return ax


def quantile_bin_plot_interactive(
    x: Union[str, SeriesLike],
    y: Union[str, SeriesLike],
    data: Optional[pd.DataFrame] = None,
    q: int = 10,
    statistic: Literal["mean", "median"] = "mean",
    title: str = "Quantile Bin Plot",
    template: str = "plotly",
    height: int = 600,
    width: int = 900,
    na_policy: NaPolicy = "drop",
) -> PlotlyFigure:
    """Create an interactive plot of y summaries across x quantile bins.

    Args:
        x (Union[str, SeriesLike]): X values or dataframe column name.
        y (Union[str, SeriesLike]): Y values or dataframe column name.
        data (Optional[pd.DataFrame]): Optional dataframe for column lookup.
        q (int): Number of quantile bins.
        statistic (Literal["mean", "median"]): Summary statistic to plot.
        title (str): Chart title.
        template (str): Plotly template.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.
        na_policy (NaPolicy): Missing-value behavior.

    Returns:
        plotly.graph_objects.Figure: Interactive quantile-bin summary plot.

    Raises:
        TypeError: If inputs cannot be resolved as numeric series.
        ValueError: If quantile bins or statistic are invalid.

    Example:
        ```python
        fig = dv.bivariate.quantile_bin_plot_interactive(x, y)
        ```

    Notes:
        The hover labels use quantile-bin centers on the x-axis.
    """
    validate_positive_int(q, "q")
    x_values, y_values = _numeric_xy(x, y, data, na_policy)
    frame = pd.DataFrame({"x": x_values, "y": y_values})
    frame["bin"] = pd.qcut(frame["x"], q=q, duplicates="drop")
    grouped = frame.groupby("bin", observed=True)["y"]
    summary = grouped.mean() if statistic == "mean" else grouped.median()
    centers = [interval.mid for interval in summary.index]
    fig = go.Figure(data=[go.Scatter(x=centers, y=summary.values, mode="lines+markers", name=statistic.title())])
    fig.update_layout(title=title, xaxis_title=_label(x_values, "X"), yaxis_title=f"{statistic.title()} {_label(y_values, 'Y')}", template=template, height=height, width=width)
    return fig


def bland_altman_static(
    x: Union[str, SeriesLike],
    y: Union[str, SeriesLike],
    data: Optional[pd.DataFrame] = None,
    title: str = "Bland-Altman Plot",
    figsize: FigureSize = (10, 6),
    theme: str = "default",
    na_policy: NaPolicy = "drop",
) -> MatplotlibAxes:
    """Create a static Bland-Altman agreement plot for two measurements.

    Args:
        x (Union[str, SeriesLike]): First measurement series or column name.
        y (Union[str, SeriesLike]): Second measurement series or column name.
        data (Optional[pd.DataFrame]): Optional dataframe for column lookup.
        title (str): Chart title.
        figsize (FigureSize): Figure size in inches.
        theme (str): Named style theme.
        na_policy (NaPolicy): Missing-value behavior.

    Returns:
        matplotlib.axes.Axes: Bland-Altman plot axes.

    Raises:
        TypeError: If inputs cannot be resolved as numeric series.
        ValueError: If fewer than two observations are available.

    Example:
        ```python
        ax = dv.bivariate.bland_altman_static(method_a, method_b)
        ```

    Notes:
        Agreement limits are mean difference plus or minus 1.96 standard deviations.
    """
    x_values, y_values = _numeric_xy(x, y, data, na_policy)
    mean_values = (x_values + y_values) / 2
    diff = x_values - y_values
    mean_diff = diff.mean()
    limit = 1.96 * diff.std()
    _, ax = setup_plot(figsize=figsize, title=title, xlabel="Measurement Mean", ylabel="Difference")
    ax.scatter(mean_values, diff, color="steelblue", alpha=0.7)
    ax.axhline(mean_diff, color="crimson", linestyle="-", label="Mean difference")
    ax.axhline(mean_diff + limit, color="gray", linestyle="--", label="Limits of agreement")
    ax.axhline(mean_diff - limit, color="gray", linestyle="--")
    ax.legend()
    apply_theme(ax, theme)
    return ax


def bland_altman_interactive(
    x: Union[str, SeriesLike],
    y: Union[str, SeriesLike],
    data: Optional[pd.DataFrame] = None,
    title: str = "Bland-Altman Plot",
    template: str = "plotly",
    height: int = 600,
    width: int = 900,
    na_policy: NaPolicy = "drop",
) -> PlotlyFigure:
    """Create an interactive Bland-Altman agreement plot for two measurements.

    Args:
        x (Union[str, SeriesLike]): First measurement series or column name.
        y (Union[str, SeriesLike]): Second measurement series or column name.
        data (Optional[pd.DataFrame]): Optional dataframe for column lookup.
        title (str): Chart title.
        template (str): Plotly template.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.
        na_policy (NaPolicy): Missing-value behavior.

    Returns:
        plotly.graph_objects.Figure: Interactive Bland-Altman plot.

    Raises:
        TypeError: If inputs cannot be resolved as numeric series.
        ValueError: If fewer than two observations are available.

    Example:
        ```python
        fig = dv.bivariate.bland_altman_interactive(method_a, method_b)
        ```

    Notes:
        Agreement limits are drawn as horizontal reference lines.
    """
    x_values, y_values = _numeric_xy(x, y, data, na_policy)
    mean_values = (x_values + y_values) / 2
    diff = x_values - y_values
    mean_diff = diff.mean()
    limit = 1.96 * diff.std()
    fig = go.Figure(data=[go.Scatter(x=mean_values, y=diff, mode="markers", name="Difference")])
    fig.add_hline(y=mean_diff, line_color="crimson", annotation_text="Mean difference")
    fig.add_hline(y=mean_diff + limit, line_color="gray", line_dash="dash", annotation_text="+1.96 SD")
    fig.add_hline(y=mean_diff - limit, line_color="gray", line_dash="dash", annotation_text="-1.96 SD")
    fig.update_layout(title=title, xaxis_title="Measurement Mean", yaxis_title="Difference", template=template, height=height, width=width)
    return fig


def rank_scatter_static(
    x: Union[str, SeriesLike],
    y: Union[str, SeriesLike],
    data: Optional[pd.DataFrame] = None,
    title: str = "Rank Scatter",
    figsize: FigureSize = (10, 6),
    theme: str = "default",
    na_policy: NaPolicy = "drop",
) -> MatplotlibAxes:
    """Create a static scatter plot comparing ranks of two variables.

    Args:
        x (Union[str, SeriesLike]): X values or dataframe column name.
        y (Union[str, SeriesLike]): Y values or dataframe column name.
        data (Optional[pd.DataFrame]): Optional dataframe for column lookup.
        title (str): Chart title.
        figsize (FigureSize): Figure size in inches.
        theme (str): Named style theme.
        na_policy (NaPolicy): Missing-value behavior.

    Returns:
        matplotlib.axes.Axes: Rank scatter axes.

    Raises:
        TypeError: If inputs cannot be resolved as numeric series.
        ValueError: If fewer than two observations are available.

    Example:
        ```python
        ax = dv.bivariate.rank_scatter_static(x, y)
        ```

    Notes:
        Rank scatter plots emphasize monotonic relationships.
    """
    x_values, y_values = _numeric_xy(x, y, data, na_policy)
    x_rank = x_values.rank()
    y_rank = y_values.rank()
    _, ax = setup_plot(figsize=figsize, title=title, xlabel=f"Rank {_label(x_values, 'X')}", ylabel=f"Rank {_label(y_values, 'Y')}")
    ax.scatter(x_rank, y_rank, color="steelblue", alpha=0.7)
    apply_theme(ax, theme)
    return ax


def rank_scatter_interactive(
    x: Union[str, SeriesLike],
    y: Union[str, SeriesLike],
    data: Optional[pd.DataFrame] = None,
    title: str = "Rank Scatter",
    template: str = "plotly",
    height: int = 600,
    width: int = 900,
    na_policy: NaPolicy = "drop",
) -> PlotlyFigure:
    """Create an interactive scatter plot comparing ranks of two variables.

    Args:
        x (Union[str, SeriesLike]): X values or dataframe column name.
        y (Union[str, SeriesLike]): Y values or dataframe column name.
        data (Optional[pd.DataFrame]): Optional dataframe for column lookup.
        title (str): Chart title.
        template (str): Plotly template.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.
        na_policy (NaPolicy): Missing-value behavior.

    Returns:
        plotly.graph_objects.Figure: Interactive rank scatter plot.

    Raises:
        TypeError: If inputs cannot be resolved as numeric series.
        ValueError: If fewer than two observations are available.

    Example:
        ```python
        fig = dv.bivariate.rank_scatter_interactive(x, y)
        ```

    Notes:
        Rank scatter plots pair naturally with Spearman correlation.
    """
    x_values, y_values = _numeric_xy(x, y, data, na_policy)
    fig = go.Figure(data=[go.Scatter(x=x_values.rank(), y=y_values.rank(), mode="markers")])
    fig.update_layout(title=title, xaxis_title=f"Rank {_label(x_values, 'X')}", yaxis_title=f"Rank {_label(y_values, 'Y')}", template=template, height=height, width=width)
    return fig


def lag_plot_static(
    x: Union[str, SeriesLike],
    y: Union[str, SeriesLike],
    data: Optional[pd.DataFrame] = None,
    lag: int = 1,
    title: str = "Lag Relationship Plot",
    figsize: FigureSize = (10, 6),
    theme: str = "default",
    na_policy: NaPolicy = "drop",
) -> MatplotlibAxes:
    """Create a static lagged relationship plot for two ordered variables.

    Args:
        x (Union[str, SeriesLike]): Leading series or column name.
        y (Union[str, SeriesLike]): Lagged series or column name.
        data (Optional[pd.DataFrame]): Optional dataframe for column lookup.
        lag (int): Positive lag applied to y.
        title (str): Chart title.
        figsize (FigureSize): Figure size in inches.
        theme (str): Named style theme.
        na_policy (NaPolicy): Missing-value behavior.

    Returns:
        matplotlib.axes.Axes: Lag relationship axes.

    Raises:
        TypeError: If inputs cannot be resolved as numeric series.
        ValueError: If lag is invalid for the available observations.

    Example:
        ```python
        ax = dv.bivariate.lag_plot_static(series_a, series_b, lag=3)
        ```

    Notes:
        The plot compares ``x[t]`` against ``y[t-lag]``.
    """
    validate_positive_int(lag, "lag")
    x_values, y_values = _numeric_xy(x, y, data, na_policy)
    if lag >= len(x_values):
        raise ValueError("lag must be smaller than the number of observations.")
    x_lagged = x_values.iloc[lag:].reset_index(drop=True)
    y_lagged = y_values.iloc[:-lag].reset_index(drop=True)
    _, ax = setup_plot(figsize=figsize, title=title, xlabel=f"{_label(x_values, 'X')}[t]", ylabel=f"{_label(y_values, 'Y')}[t-{lag}]")
    ax.scatter(x_lagged, y_lagged, color="steelblue", alpha=0.7)
    apply_theme(ax, theme)
    return ax


def lag_plot_interactive(
    x: Union[str, SeriesLike],
    y: Union[str, SeriesLike],
    data: Optional[pd.DataFrame] = None,
    lag: int = 1,
    title: str = "Lag Relationship Plot",
    template: str = "plotly",
    height: int = 600,
    width: int = 900,
    na_policy: NaPolicy = "drop",
) -> PlotlyFigure:
    """Create an interactive lagged relationship plot for two ordered variables.

    Args:
        x (Union[str, SeriesLike]): Leading series or column name.
        y (Union[str, SeriesLike]): Lagged series or column name.
        data (Optional[pd.DataFrame]): Optional dataframe for column lookup.
        lag (int): Positive lag applied to y.
        title (str): Chart title.
        template (str): Plotly template.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.
        na_policy (NaPolicy): Missing-value behavior.

    Returns:
        plotly.graph_objects.Figure: Interactive lag relationship plot.

    Raises:
        TypeError: If inputs cannot be resolved as numeric series.
        ValueError: If lag is invalid for the available observations.

    Example:
        ```python
        fig = dv.bivariate.lag_plot_interactive(series_a, series_b, lag=3)
        ```

    Notes:
        Lag plots are useful for ordered or time-indexed data.
    """
    validate_positive_int(lag, "lag")
    x_values, y_values = _numeric_xy(x, y, data, na_policy)
    if lag >= len(x_values):
        raise ValueError("lag must be smaller than the number of observations.")
    x_lagged = x_values.iloc[lag:].reset_index(drop=True)
    y_lagged = y_values.iloc[:-lag].reset_index(drop=True)
    fig = go.Figure(data=[go.Scatter(x=x_lagged, y=y_lagged, mode="markers")])
    fig.update_layout(title=title, xaxis_title=f"{_label(x_values, 'X')}[t]", yaxis_title=f"{_label(y_values, 'Y')}[t-{lag}]", template=template, height=height, width=width)
    return fig


def conditional_box_static(
    x: Union[str, SeriesLike],
    y: Union[str, SeriesLike],
    data: Optional[pd.DataFrame] = None,
    bins: int = 10,
    title: str = "Conditional Box Plot",
    figsize: FigureSize = (12, 6),
    theme: str = "default",
    na_policy: NaPolicy = "drop",
) -> MatplotlibAxes:
    """Create a static box plot of y distributions across x bins.

    Args:
        x (Union[str, SeriesLike]): Numeric conditioning variable or column name.
        y (Union[str, SeriesLike]): Numeric response variable or column name.
        data (Optional[pd.DataFrame]): Optional dataframe for column lookup.
        bins (int): Number of x bins.
        title (str): Chart title.
        figsize (FigureSize): Figure size in inches.
        theme (str): Named style theme.
        na_policy (NaPolicy): Missing-value behavior.

    Returns:
        matplotlib.axes.Axes: Conditional box plot axes.

    Raises:
        TypeError: If inputs cannot be resolved as numeric series.
        ValueError: If bins are invalid.

    Example:
        ```python
        ax = dv.bivariate.conditional_box_static(x, y, bins=6)
        ```

    Notes:
        This chart shows how the distribution of y changes over ranges of x.
    """
    validate_positive_int(bins, "bins")
    x_values, y_values = _numeric_xy(x, y, data, na_policy)
    frame = pd.DataFrame({"x": x_values, "y": y_values})
    frame["bin"] = pd.cut(frame["x"], bins=bins)
    grouped = frame.groupby("bin", observed=True)["y"]
    labels = [str(interval) for interval, _ in grouped]
    values = [group.to_numpy() for _, group in grouped]
    _, ax = setup_plot(figsize=figsize, title=title, xlabel=_label(x_values, "X"), ylabel=_label(y_values, "Y"))
    ax.boxplot(values, labels=labels)
    ax.tick_params(axis="x", rotation=45)
    apply_theme(ax, theme)
    return ax


def conditional_box_interactive(
    x: Union[str, SeriesLike],
    y: Union[str, SeriesLike],
    data: Optional[pd.DataFrame] = None,
    bins: int = 10,
    title: str = "Conditional Box Plot",
    template: str = "plotly",
    height: int = 600,
    width: int = 1000,
    na_policy: NaPolicy = "drop",
) -> PlotlyFigure:
    """Create an interactive box plot of y distributions across x bins.

    Args:
        x (Union[str, SeriesLike]): Numeric conditioning variable or column name.
        y (Union[str, SeriesLike]): Numeric response variable or column name.
        data (Optional[pd.DataFrame]): Optional dataframe for column lookup.
        bins (int): Number of x bins.
        title (str): Chart title.
        template (str): Plotly template.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.
        na_policy (NaPolicy): Missing-value behavior.

    Returns:
        plotly.graph_objects.Figure: Interactive conditional box plot.

    Raises:
        TypeError: If inputs cannot be resolved as numeric series.
        ValueError: If bins are invalid.

    Example:
        ```python
        fig = dv.bivariate.conditional_box_interactive(x, y, bins=6)
        ```

    Notes:
        Each x bin is rendered as a separate box trace.
    """
    validate_positive_int(bins, "bins")
    x_values, y_values = _numeric_xy(x, y, data, na_policy)
    frame = pd.DataFrame({"x": x_values, "y": y_values})
    frame["bin"] = pd.cut(frame["x"], bins=bins)
    fig = go.Figure()
    for interval, group in frame.groupby("bin", observed=True):
        fig.add_trace(go.Box(y=group["y"], name=str(interval), boxpoints="outliers"))
    fig.update_layout(title=title, xaxis_title=_label(x_values, "X"), yaxis_title=_label(y_values, "Y"), template=template, height=height, width=width)
    return fig
