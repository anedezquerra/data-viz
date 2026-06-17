"""Ordinal and Likert-style univariate summaries and charts."""

from typing import Optional, Sequence

import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go

from ..types import FigureSize, MatplotlibAxes, PlotlyFigure, SeriesLike
from ..utils import apply_theme, setup_plot


def ordered_category_counts(
    data: SeriesLike,
    order: Optional[Sequence[str]] = None,
    normalize: bool = False,
    dropna: bool = True,
) -> pd.Series:
    """Compute category counts in a meaningful order.

    Args:
        data (SeriesLike): Input ordinal or categorical observations.
        order (Optional[Sequence[str]]): Explicit category order.
        normalize (bool): Whether to return proportions instead of counts.
        dropna (bool): Whether to omit missing values.

    Returns:
        pandas.Series: Ordered category counts or proportions.

    Raises:
        TypeError: If input data cannot be represented as a pandas Series.
        ValueError: If the requested order omits observed categories.

    Examples:
        ```python
        counts = ordered_category_counts(responses, order=["Low", "Medium", "High"])
        ```

    Notes:
        Without ``order``, categories are sorted by their natural label order.
    """
    series = pd.Series(data)
    if dropna:
        series = series.dropna()
    counts = series.value_counts(normalize=normalize, sort=False)
    if order is None:
        return counts.sort_index()
    missing = [value for value in counts.index.astype(str) if value not in order]
    if missing:
        raise ValueError(f"order does not include observed categories: {missing}.")
    return counts.reindex(order, fill_value=0)


def likert_summary(
    data: SeriesLike,
    order: Sequence[str] = ("Strongly disagree", "Disagree", "Neutral", "Agree", "Strongly agree"),
) -> pd.DataFrame:
    """Summarize one Likert-style variable.

    Args:
        data (SeriesLike): Input Likert responses.
        order (Sequence[str]): Ordered response labels.

    Returns:
        pandas.DataFrame: Response, count, proportion, and cumulative proportion columns.

    Raises:
        TypeError: If input data cannot be represented as a pandas Series.
        ValueError: If the response order omits observed categories.

    Examples:
        ```python
        table = likert_summary(responses)
        ```

    Notes:
        The default order follows a five-point agreement scale.
    """
    counts = ordered_category_counts(data, order=order, normalize=False)
    total = counts.sum()
    if total == 0:
        raise ValueError("data must contain at least one response.")
    proportions = counts / total
    return pd.DataFrame(
        {
            "response": counts.index.astype(str),
            "count": counts.to_numpy(),
            "proportion": proportions.to_numpy(),
            "cumulative_proportion": proportions.cumsum().to_numpy(),
        }
    )


def ordinal_bar_static(
    data: SeriesLike,
    order: Optional[Sequence[str]] = None,
    normalize: bool = False,
    title: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    color: Optional[str] = None,
    theme: str = "default",
) -> MatplotlibAxes:
    """Create a static ordered category bar chart.

    Args:
        data (SeriesLike): Input ordinal or categorical observations.
        order (Optional[Sequence[str]]): Explicit category order.
        normalize (bool): Whether to plot proportions instead of counts.
        title (Optional[str]): Optional chart title.
        figsize (FigureSize): Matplotlib figure size.
        color (Optional[str]): Bar color.
        theme (str): Styling theme name.

    Returns:
        matplotlib.axes.Axes: Axes containing the ordered bar chart.

    Raises:
        TypeError: If input data cannot be represented as a pandas Series.
        ValueError: If the requested order omits observed categories.

    Examples:
        ```python
        ax = ordinal_bar_static(ratings, order=["Low", "Medium", "High"])
        ```

    Notes:
        Ordered bars avoid misleading frequency sorting for ordinal variables.
    """
    counts = ordered_category_counts(data, order=order, normalize=normalize)
    ax = setup_plot(title=title or "Ordered Category Counts", xlabel="Category", ylabel="Proportion" if normalize else "Count", figsize=figsize)[1]
    ax.bar(counts.index.astype(str), counts.to_numpy(), color=color)
    ax.tick_params(axis="x", rotation=45)
    ax.grid(True, axis="y", alpha=0.3)
    apply_theme(ax, theme)
    return ax


def ordinal_bar_interactive(
    data: SeriesLike,
    order: Optional[Sequence[str]] = None,
    normalize: bool = False,
    title: Optional[str] = None,
    color: Optional[str] = None,
    template: str = "plotly",
    height: int = 600,
    width: int = 1000,
) -> PlotlyFigure:
    """Create an interactive ordered category bar chart.

    Args:
        data (SeriesLike): Input ordinal or categorical observations.
        order (Optional[Sequence[str]]): Explicit category order.
        normalize (bool): Whether to plot proportions instead of counts.
        title (Optional[str]): Optional chart title.
        color (Optional[str]): Bar color.
        template (str): Plotly template name.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.

    Returns:
        plotly.graph_objects.Figure: Interactive ordered bar chart.

    Raises:
        TypeError: If input data cannot be represented as a pandas Series.
        ValueError: If the requested order omits observed categories.

    Examples:
        ```python
        fig = ordinal_bar_interactive(ratings)
        ```

    Notes:
        The function keeps the caller-supplied order on the x-axis.
    """
    counts = ordered_category_counts(data, order=order, normalize=normalize)
    fig = go.Figure(go.Bar(x=counts.index.astype(str), y=counts.to_numpy(), marker_color=color))
    fig.update_layout(title=title or "Ordered Category Counts", xaxis_title="Category", yaxis_title="Proportion" if normalize else "Count", template=template, height=height, width=width)
    return fig

