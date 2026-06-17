"""Text-like and boolean univariate helpers."""

from dataclasses import dataclass
from typing import Optional

import numpy as np
import pandas as pd
import plotly.graph_objects as go

from ..types import FigureSize, MatplotlibAxes, PlotlyFigure, SeriesLike
from ..utils import apply_theme, setup_plot
from .categorical import frequency_bar_interactive, frequency_bar_static


@dataclass(frozen=True)
class BooleanSummary:
    """Boolean variable summary.

    Args:
        count (int): Number of non-missing boolean observations.
        true_count (int): Number of true observations.
        false_count (int): Number of false observations.
        true_rate (float): Share of true observations.

    Returns:
        BooleanSummary: Immutable boolean summary.

    Raises:
        TypeError: If values cannot be represented by declared fields.
        ValueError: If rates are incompatible with downstream numeric use.

    Examples:
        ```python
        summary = BooleanSummary(10, 7, 3, 0.7)
        ```

    Notes:
        Boolean summaries are useful for one-dimensional binary indicators.
    """

    count: int
    true_count: int
    false_count: int
    true_rate: float


@dataclass(frozen=True)
class BooleanRateInterval:
    """Wilson confidence interval for a boolean true rate.

    Args:
        true_rate (float): Observed true rate.
        lower (float): Lower Wilson confidence bound.
        upper (float): Upper Wilson confidence bound.
        confidence_level (float): Confidence level.

    Returns:
        BooleanRateInterval: Immutable boolean rate interval.

    Raises:
        TypeError: If fields cannot be represented by declared types.
        ValueError: If interval bounds are invalid.

    Examples:
        ```python
        interval = BooleanRateInterval(0.6, 0.4, 0.8, 0.95)
        ```

    Notes:
        Wilson intervals behave better than Wald intervals near 0 or 1.
    """

    true_rate: float
    lower: float
    upper: float
    confidence_level: float


def boolean_summary(data: SeriesLike) -> BooleanSummary:
    """Summarize a boolean-like variable.

    Args:
        data (SeriesLike): Input boolean-like observations.

    Returns:
        BooleanSummary: Counts and true-rate summary.

    Raises:
        TypeError: If input data cannot be represented as a pandas Series.
        ValueError: If no non-missing observations remain.

    Examples:
        ```python
        summary = boolean_summary([True, False, True])
        ```

    Notes:
        Values are coerced with pandas boolean semantics after missing values are removed.
    """
    values = pd.Series(data).dropna().astype(bool)
    if values.empty:
        raise ValueError("data must contain at least one non-missing observation.")
    true_count = int(values.sum())
    false_count = int(len(values) - true_count)
    return BooleanSummary(count=int(len(values)), true_count=true_count, false_count=false_count, true_rate=float(true_count / len(values)))


def boolean_wilson_interval(data: SeriesLike, confidence_level: float = 0.95) -> BooleanRateInterval:
    """Compute a Wilson confidence interval for a boolean true rate.

    Args:
        data (SeriesLike): Input boolean-like observations.
        confidence_level (float): Confidence level in the open ``(0, 1)`` interval.

    Returns:
        BooleanRateInterval: Observed rate and Wilson interval bounds.

    Raises:
        TypeError: If input data cannot be represented as a pandas Series.
        ValueError: If confidence level is invalid or no observations remain.

    Examples:
        ```python
        interval = boolean_wilson_interval(flags)
        ```

    Notes:
        The z value is computed from the normal quantile function.
    """
    if confidence_level <= 0 or confidence_level >= 1:
        raise ValueError("confidence_level must be between 0 and 1.")
    from scipy import stats

    summary = boolean_summary(data)
    z_value = float(stats.norm.ppf(1 - (1 - confidence_level) / 2))
    n = summary.count
    p = summary.true_rate
    denominator = 1 + z_value**2 / n
    center = (p + z_value**2 / (2 * n)) / denominator
    half_width = (z_value / denominator) * np.sqrt((p * (1 - p) / n) + (z_value**2 / (4 * n**2)))
    return BooleanRateInterval(
        true_rate=p,
        lower=float(max(0.0, center - half_width)),
        upper=float(min(1.0, center + half_width)),
        confidence_level=confidence_level,
    )


def string_length_summary(data: SeriesLike) -> pd.Series:
    """Compute string lengths for text-like observations.

    Args:
        data (SeriesLike): Input text-like observations.

    Returns:
        pandas.Series: String lengths for non-missing observations.

    Raises:
        TypeError: If input data cannot be represented as a pandas Series.
        ValueError: If no non-missing observations remain.

    Examples:
        ```python
        lengths = string_length_summary(["alpha", "beta"])
        ```

    Notes:
        Values are converted to strings before measuring length.
    """
    values = pd.Series(data).dropna()
    if values.empty:
        raise ValueError("data must contain at least one non-missing observation.")
    return values.astype(str).str.len().reset_index(drop=True)


def token_count_summary(data: SeriesLike) -> pd.Series:
    """Compute whitespace token counts for text-like observations.

    Args:
        data (SeriesLike): Input text-like observations.

    Returns:
        pandas.Series: Token counts for non-missing observations.

    Raises:
        TypeError: If input data cannot be represented as a pandas Series.
        ValueError: If no non-missing observations remain.

    Examples:
        ```python
        counts = token_count_summary(["hello world", "one"])
        ```

    Notes:
        Empty strings produce zero tokens.
    """
    values = pd.Series(data).dropna()
    if values.empty:
        raise ValueError("data must contain at least one non-missing observation.")
    return values.astype(str).str.split().str.len().reset_index(drop=True)


def top_terms(data: SeriesLike, top_n: int = 20, lowercase: bool = True) -> pd.Series:
    """Count the most common whitespace-delimited terms.

    Args:
        data (SeriesLike): Input text-like observations.
        top_n (int): Number of terms to return.
        lowercase (bool): Whether to lowercase text before tokenization.

    Returns:
        pandas.Series: Term counts indexed by term.

    Raises:
        TypeError: If input data cannot be represented as a pandas Series.
        ValueError: If ``top_n`` is invalid or no terms are found.

    Examples:
        ```python
        terms = top_terms(["red blue", "red"], top_n=5)
        ```

    Notes:
        This lightweight helper is intentionally dependency-free and not a full NLP tokenizer.
    """
    if top_n < 1:
        raise ValueError("top_n must be positive.")
    values = pd.Series(data).dropna().astype(str)
    if lowercase:
        values = values.str.lower()
    tokens = values.str.split().explode()
    tokens = tokens[tokens.astype(str).str.len() > 0]
    if tokens.empty:
        raise ValueError("data must contain at least one token.")
    return tokens.value_counts().head(top_n)


def boolean_bar_static(
    data: SeriesLike,
    title: Optional[str] = None,
    figsize: FigureSize = (6, 5),
    color: Optional[str] = None,
    theme: str = "default",
) -> MatplotlibAxes:
    """Create a static true/false count chart.

    Args:
        data (SeriesLike): Input boolean-like observations.
        title (Optional[str]): Optional chart title.
        figsize (FigureSize): Matplotlib figure size.
        color (Optional[str]: Bar color.
        theme (str): Styling theme name.

    Returns:
        matplotlib.axes.Axes: Axes containing true/false counts.

    Raises:
        TypeError: If input data cannot be represented as a pandas Series.
        ValueError: If no non-missing observations remain.

    Examples:
        ```python
        ax = boolean_bar_static(flags)
        ```

    Notes:
        This is a semantic wrapper around categorical frequency bars.
    """
    values = pd.Series(data).dropna().astype(bool)
    ax = frequency_bar_static(values, title=title or "Boolean Counts", figsize=figsize, color=color)
    apply_theme(ax, theme)
    return ax


def boolean_bar_interactive(
    data: SeriesLike,
    title: Optional[str] = None,
    color: Optional[str] = None,
    template: str = "plotly",
    height: int = 500,
    width: int = 700,
) -> PlotlyFigure:
    """Create an interactive true/false count chart.

    Args:
        data (SeriesLike): Input boolean-like observations.
        title (Optional[str]): Optional chart title.
        color (Optional[str]: Bar color.
        template (str): Plotly template name.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.

    Returns:
        plotly.graph_objects.Figure: Interactive true/false count chart.

    Raises:
        TypeError: If input data cannot be represented as a pandas Series.
        ValueError: If no non-missing observations remain.

    Examples:
        ```python
        fig = boolean_bar_interactive(flags)
        ```

    Notes:
        This is a semantic wrapper around categorical frequency bars.
    """
    values = pd.Series(data).dropna().astype(bool)
    return frequency_bar_interactive(values, title=title or "Boolean Counts", color=color, template=template, height=height, width=width)


def top_terms_bar_static(
    data: SeriesLike,
    top_n: int = 20,
    title: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    color: Optional[str] = None,
    theme: str = "default",
) -> MatplotlibAxes:
    """Create a static bar chart of common text terms.

    Args:
        data (SeriesLike): Input text-like observations.
        top_n (int): Number of terms to show.
        title (Optional[str]): Optional chart title.
        figsize (FigureSize): Matplotlib figure size.
        color (Optional[str]: Bar color.
        theme (str): Styling theme name.

    Returns:
        matplotlib.axes.Axes: Axes containing top-term counts.

    Raises:
        TypeError: If input data cannot be represented as a pandas Series.
        ValueError: If no terms are found or ``top_n`` is invalid.

    Examples:
        ```python
        ax = top_terms_bar_static(messages)
        ```

    Notes:
        Use this for lightweight exploratory text profiling.
    """
    counts = top_terms(data, top_n=top_n)
    ax = setup_plot(title=title or "Top Terms", xlabel="Term", ylabel="Count", figsize=figsize)[1]
    ax.bar(counts.index.astype(str), counts.to_numpy(), color=color)
    ax.tick_params(axis="x", rotation=45)
    apply_theme(ax, theme)
    return ax


def top_terms_bar_interactive(
    data: SeriesLike,
    top_n: int = 20,
    title: Optional[str] = None,
    color: Optional[str] = None,
    template: str = "plotly",
    height: int = 600,
    width: int = 1000,
) -> PlotlyFigure:
    """Create an interactive bar chart of common text terms.

    Args:
        data (SeriesLike): Input text-like observations.
        top_n (int): Number of terms to show.
        title (Optional[str]): Optional chart title.
        color (Optional[str]: Bar color.
        template (str): Plotly template name.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.

    Returns:
        plotly.graph_objects.Figure: Interactive top-term chart.

    Raises:
        TypeError: If input data cannot be represented as a pandas Series.
        ValueError: If no terms are found or ``top_n`` is invalid.

    Examples:
        ```python
        fig = top_terms_bar_interactive(messages)
        ```

    Notes:
        This helper intentionally avoids NLP dependencies.
    """
    counts = top_terms(data, top_n=top_n)
    fig = go.Figure(go.Bar(x=counts.index.astype(str), y=counts.to_numpy(), marker_color=color))
    fig.update_layout(title=title or "Top Terms", xaxis_title="Term", yaxis_title="Count", template=template, height=height, width=width)
    return fig
