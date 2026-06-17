"""Categorical bivariate comparison charts."""

from typing import Callable, Optional, Union

import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go

from ..types import FigureSize, MatplotlibAxes, PlotlyFigure, SeriesLike
from ..utils import apply_theme, setup_plot

Aggregator = Union[str, Callable[[pd.Series], float]]


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
        label = _label(series, "Category")
        ```

    Notes:
        This helper centralizes default label generation.
    """
    return getattr(values, "name", None) or fallback


def _frame(category: SeriesLike, values: Optional[SeriesLike] = None) -> pd.DataFrame:
    """Build a temporary dataframe for category/value calculations.

    Args:
        category (SeriesLike): Category labels.
        values (Optional[SeriesLike]): Optional numeric values associated with each label.

    Returns:
        pandas.DataFrame: Dataframe with ``category`` and optional ``value`` columns.

    Raises:
        TypeError: If inputs cannot be converted into a dataframe.
        ValueError: If category and value lengths differ.

    Example:
        ```python
        frame = _frame(category, values)
        ```

    Notes:
        The public plotting functions use this helper before pandas grouping.
    """
    data = {"category": category}
    if values is not None:
        data["value"] = values
    return pd.DataFrame(data)


def grouped_bar_static(
    category: SeriesLike,
    values: SeriesLike,
    aggfunc: Aggregator = "mean",
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    color: str = "steelblue",
    figsize: FigureSize = (10, 6),
    theme: str = "default",
    style: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Create a static aggregated bar chart for a numeric value by category.

    Args:
        category (SeriesLike): Categorical group labels.
        values (SeriesLike): Numeric values aggregated within each category.
        aggfunc (Aggregator): Pandas aggregation function or name.
        title (Optional[str]): Chart title. Defaults to a generated title.
        xlabel (Optional[str]): X-axis label.
        ylabel (Optional[str]): Y-axis label.
        color (str): Bar color.
        figsize (FigureSize): Figure size in inches.
        theme (str): Theme name applied to the axes.
        style (str): Matplotlib style context.
        **kwargs: Additional arguments forwarded to ``Axes.bar``.

    Returns:
        matplotlib.axes.Axes: Aggregated bar chart axes.

    Raises:
        TypeError: If values cannot be aggregated.
        ValueError: If category and values lengths differ.

    Example:
        ```python
        ax = dv.bivariate.grouped_bar_static(groups, sales, aggfunc="sum")
        ```

    Notes:
        Use box or violin plots when the distribution inside each group matters.
    """
    xlabel = xlabel or _label(category, "Category")
    ylabel = ylabel or _label(values, str(aggfunc).title())
    title = title or f"{ylabel} by {xlabel}"
    summary = _frame(category, values).groupby("category")["value"].agg(aggfunc)
    with plt.style.context(style):
        _, ax = setup_plot(figsize=figsize, title=title, xlabel=xlabel, ylabel=ylabel)
        ax.bar(summary.index.astype(str), summary.values, color=color, **kwargs)
        ax.tick_params(axis="x", rotation=45)
        apply_theme(ax, theme)
        return ax


def grouped_bar_interactive(
    category: SeriesLike,
    values: SeriesLike,
    aggfunc: Aggregator = "mean",
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    color: str = "steelblue",
    template: str = "plotly",
    height: int = 600,
    width: int = 900,
    **kwargs,
) -> PlotlyFigure:
    """Create an interactive aggregated bar chart for a numeric value by category.

    Args:
        category (SeriesLike): Categorical group labels.
        values (SeriesLike): Numeric values aggregated within each category.
        aggfunc (Aggregator): Pandas aggregation function or name.
        title (Optional[str]): Chart title. Defaults to a generated title.
        xlabel (Optional[str]): X-axis label.
        ylabel (Optional[str]): Y-axis label.
        color (str): Bar color.
        template (str): Plotly layout template.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.
        **kwargs: Additional arguments forwarded to ``go.Bar``.

    Returns:
        plotly.graph_objects.Figure: Interactive aggregated bar chart.

    Raises:
        TypeError: If values cannot be aggregated.
        ValueError: If category and values lengths differ.

    Example:
        ```python
        fig = dv.bivariate.grouped_bar_interactive(groups, sales, aggfunc="median")
        ```

    Notes:
        Aggregation is performed with pandas before plotting.
    """
    xlabel = xlabel or _label(category, "Category")
    ylabel = ylabel or _label(values, str(aggfunc).title())
    title = title or f"{ylabel} by {xlabel}"
    summary = _frame(category, values).groupby("category")["value"].agg(aggfunc)
    fig = go.Figure(data=[go.Bar(x=summary.index.astype(str), y=summary.values, marker_color=color, **kwargs)])
    fig.update_layout(title=title, xaxis_title=xlabel, yaxis_title=ylabel, template=template, height=height, width=width)
    return fig


def box_by_category_static(
    category: SeriesLike,
    values: SeriesLike,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    theme: str = "default",
    style: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Create a static box plot of numeric values grouped by category.

    Args:
        category (SeriesLike): Categorical group labels.
        values (SeriesLike): Numeric values to summarize.
        title (Optional[str]): Chart title. Defaults to a generated title.
        xlabel (Optional[str]): X-axis label.
        ylabel (Optional[str]): Y-axis label.
        figsize (FigureSize): Figure size in inches.
        theme (str): Theme name applied to the axes.
        style (str): Matplotlib style context.
        **kwargs: Additional arguments forwarded to ``Axes.boxplot``.

    Returns:
        matplotlib.axes.Axes: Grouped box plot axes.

    Raises:
        TypeError: If values are not numeric.
        ValueError: If category and values lengths differ.

    Example:
        ```python
        ax = dv.bivariate.box_by_category_static(groups, scores)
        ```

    Notes:
        Categories are ordered by their natural pandas group order.
    """
    xlabel = xlabel or _label(category, "Category")
    ylabel = ylabel or _label(values, "Value")
    title = title or f"{ylabel} Distribution by {xlabel}"
    grouped = _frame(category, values).groupby("category")["value"]
    labels = [str(name) for name, _ in grouped]
    data = [group.to_numpy() for _, group in grouped]
    with plt.style.context(style):
        _, ax = setup_plot(figsize=figsize, title=title, xlabel=xlabel, ylabel=ylabel)
        ax.boxplot(data, labels=labels, **kwargs)
        ax.tick_params(axis="x", rotation=45)
        apply_theme(ax, theme)
        return ax


def box_by_category_interactive(
    category: SeriesLike,
    values: SeriesLike,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    template: str = "plotly",
    height: int = 600,
    width: int = 900,
    **kwargs,
) -> PlotlyFigure:
    """Create an interactive box plot of numeric values grouped by category.

    Args:
        category (SeriesLike): Categorical group labels.
        values (SeriesLike): Numeric values to summarize.
        title (Optional[str]): Chart title. Defaults to a generated title.
        xlabel (Optional[str]): X-axis label.
        ylabel (Optional[str]): Y-axis label.
        template (str): Plotly layout template.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.
        **kwargs: Additional arguments forwarded to ``go.Box``.

    Returns:
        plotly.graph_objects.Figure: Interactive grouped box plot.

    Raises:
        TypeError: If values are not numeric.
        ValueError: If category and values lengths differ.

    Example:
        ```python
        fig = dv.bivariate.box_by_category_interactive(groups, scores)
        ```

    Notes:
        Plotly handles per-category grouping from the x values.
    """
    xlabel = xlabel or _label(category, "Category")
    ylabel = ylabel or _label(values, "Value")
    title = title or f"{ylabel} Distribution by {xlabel}"
    fig = go.Figure(data=[go.Box(x=category, y=values, boxpoints="outliers", **kwargs)])
    fig.update_layout(title=title, xaxis_title=xlabel, yaxis_title=ylabel, template=template, height=height, width=width)
    return fig


def violin_by_category_static(
    category: SeriesLike,
    values: SeriesLike,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    theme: str = "default",
    style: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Create a static violin plot of numeric values grouped by category.

    Args:
        category (SeriesLike): Categorical group labels.
        values (SeriesLike): Numeric values to summarize.
        title (Optional[str]): Chart title. Defaults to a generated title.
        xlabel (Optional[str]): X-axis label.
        ylabel (Optional[str]): Y-axis label.
        figsize (FigureSize): Figure size in inches.
        theme (str): Theme name applied to the axes.
        style (str): Matplotlib style context.
        **kwargs: Additional arguments forwarded to ``Axes.violinplot``.

    Returns:
        matplotlib.axes.Axes: Grouped violin plot axes.

    Raises:
        TypeError: If values are not numeric.
        ValueError: If category and values lengths differ.

    Example:
        ```python
        ax = dv.bivariate.violin_by_category_static(groups, scores)
        ```

    Notes:
        Use this chart when each group has enough observations to show density.
    """
    xlabel = xlabel or _label(category, "Category")
    ylabel = ylabel or _label(values, "Value")
    title = title or f"{ylabel} Shape by {xlabel}"
    grouped = _frame(category, values).groupby("category")["value"]
    labels = [str(name) for name, _ in grouped]
    data = [group.to_numpy() for _, group in grouped]
    with plt.style.context(style):
        _, ax = setup_plot(figsize=figsize, title=title, xlabel=xlabel, ylabel=ylabel)
        ax.violinplot(data, showmeans=True, **kwargs)
        ax.set_xticks(range(1, len(labels) + 1))
        ax.set_xticklabels(labels, rotation=45, ha="right")
        apply_theme(ax, theme)
        return ax


def violin_by_category_interactive(
    category: SeriesLike,
    values: SeriesLike,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    template: str = "plotly",
    height: int = 600,
    width: int = 900,
    **kwargs,
) -> PlotlyFigure:
    """Create an interactive violin plot of numeric values grouped by category.

    Args:
        category (SeriesLike): Categorical group labels.
        values (SeriesLike): Numeric values to summarize.
        title (Optional[str]): Chart title. Defaults to a generated title.
        xlabel (Optional[str]): X-axis label.
        ylabel (Optional[str]): Y-axis label.
        template (str): Plotly layout template.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.
        **kwargs: Additional arguments forwarded to ``go.Violin``.

    Returns:
        plotly.graph_objects.Figure: Interactive grouped violin plot.

    Raises:
        TypeError: If values are not numeric.
        ValueError: If category and values lengths differ.

    Example:
        ```python
        fig = dv.bivariate.violin_by_category_interactive(groups, scores)
        ```

    Notes:
        Each category is rendered as a separate violin trace.
    """
    xlabel = xlabel or _label(category, "Category")
    ylabel = ylabel or _label(values, "Value")
    title = title or f"{ylabel} Shape by {xlabel}"
    frame = _frame(category, values)
    fig = go.Figure()
    for name, group in frame.groupby("category"):
        fig.add_trace(go.Violin(y=group["value"], name=str(name), box_visible=True, meanline_visible=True, **kwargs))
    fig.update_layout(title=title, xaxis_title=xlabel, yaxis_title=ylabel, template=template, height=height, width=width)
    return fig


def crosstab_heatmap_static(
    row_category: SeriesLike,
    column_category: SeriesLike,
    normalize: Optional[str] = None,
    title: str = "Crosstab Heatmap",
    cmap: str = "Blues",
    figsize: FigureSize = (10, 6),
    theme: str = "default",
    style: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Create a static heatmap for two categorical variables.

    Args:
        row_category (SeriesLike): Categories shown on the y-axis.
        column_category (SeriesLike): Categories shown on the x-axis.
        normalize (Optional[str]): Normalization mode accepted by ``pandas.crosstab``.
        title (str): Chart title.
        cmap (str): Matplotlib colormap.
        figsize (FigureSize): Figure size in inches.
        theme (str): Theme name applied to the axes.
        style (str): Matplotlib style context.
        **kwargs: Additional arguments forwarded to ``Axes.imshow``.

    Returns:
        matplotlib.axes.Axes: Crosstab heatmap axes.

    Raises:
        TypeError: If categories cannot be tabulated.
        ValueError: If category lengths differ.

    Example:
        ```python
        ax = dv.bivariate.crosstab_heatmap_static(region, segment)
        ```

    Notes:
        Set ``normalize="index"`` or ``normalize="columns"`` for proportions.
    """
    table = pd.crosstab(row_category, column_category, normalize=normalize)
    with plt.style.context(style):
        _, ax = setup_plot(figsize=figsize, title=title)
        image = ax.imshow(table.values, cmap=cmap, aspect="auto", **kwargs)
        ax.set_xticks(range(len(table.columns)))
        ax.set_xticklabels(table.columns.astype(str), rotation=45, ha="right")
        ax.set_yticks(range(len(table.index)))
        ax.set_yticklabels(table.index.astype(str))
        for i in range(table.shape[0]):
            for j in range(table.shape[1]):
                ax.text(j, i, f"{table.iloc[i, j]:.2f}" if normalize else str(table.iloc[i, j]), ha="center", va="center")
        plt.colorbar(image, ax=ax)
        apply_theme(ax, theme)
        return ax


def crosstab_heatmap_interactive(
    row_category: SeriesLike,
    column_category: SeriesLike,
    normalize: Optional[str] = None,
    title: str = "Crosstab Heatmap",
    colorscale: str = "Blues",
    template: str = "plotly",
    height: int = 600,
    width: int = 900,
    **kwargs,
) -> PlotlyFigure:
    """Create an interactive heatmap for two categorical variables.

    Args:
        row_category (SeriesLike): Categories shown on the y-axis.
        column_category (SeriesLike): Categories shown on the x-axis.
        normalize (Optional[str]): Normalization mode accepted by ``pandas.crosstab``.
        title (str): Chart title.
        colorscale (str): Plotly colorscale.
        template (str): Plotly layout template.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.
        **kwargs: Additional arguments forwarded to ``go.Heatmap``.

    Returns:
        plotly.graph_objects.Figure: Interactive crosstab heatmap.

    Raises:
        TypeError: If categories cannot be tabulated.
        ValueError: If category lengths differ.

    Example:
        ```python
        fig = dv.bivariate.crosstab_heatmap_interactive(region, segment)
        ```

    Notes:
        Hover labels expose the tabulated count or proportion.
    """
    table = pd.crosstab(row_category, column_category, normalize=normalize)
    fig = go.Figure(data=go.Heatmap(z=table.values, x=table.columns.astype(str), y=table.index.astype(str), colorscale=colorscale, **kwargs))
    fig.update_layout(title=title, template=template, height=height, width=width)
    return fig
