"""Categorical univariate frequency and Pareto charts."""

from typing import Optional

import pandas as pd
import plotly.graph_objects as go

from ..types import FigureSize, MatplotlibAxes, PlotlyFigure, SeriesLike
from ..utils import apply_theme, setup_plot, validate_positive_int


def category_counts(
    data: SeriesLike,
    normalize: bool = False,
    dropna: bool = True,
    sort: bool = True,
    top_n: Optional[int] = None,
) -> pd.Series:
    """Compute category counts or proportions for one variable.

    Args:
        data (SeriesLike): Input categorical observations.
        normalize (bool): Whether to return proportions instead of counts.
        dropna (bool): Whether to omit missing values.
        sort (bool): Whether to sort categories by frequency descending.
        top_n (Optional[int]): Optional number of most common categories to keep.

    Returns:
        pandas.Series: Category counts or proportions indexed by category label.

    Raises:
        TypeError: If input data cannot be represented as a pandas Series.
        ValueError: If ``top_n`` is provided and is not positive, or no categories remain.

    Examples:
        ```python
        counts = category_counts(["A", "B", "A"])
        ```

    Notes:
        This helper underpins categorical bar and Pareto chart functions.
    """
    if top_n is not None:
        validate_positive_int(top_n, "top_n")
    counts = pd.Series(data).value_counts(normalize=normalize, dropna=dropna, sort=sort)
    if top_n is not None:
        counts = counts.head(top_n)
    if counts.empty:
        raise ValueError("data must contain at least one category.")
    return counts


def frequency_bar_static(
    data: SeriesLike,
    normalize: bool = False,
    dropna: bool = True,
    sort: bool = True,
    top_n: Optional[int] = None,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    color: Optional[str] = None,
    rotation: int = 45,
    theme: str = "default",
    grid: bool = True,
    grid_alpha: float = 0.3,
    **kwargs,
) -> MatplotlibAxes:
    """Create a static categorical frequency bar chart.

    Args:
        data (SeriesLike): Input categorical observations.
        normalize (bool): Whether to plot proportions instead of counts.
        dropna (bool): Whether to omit missing values.
        sort (bool): Whether to sort categories by frequency descending.
        top_n (Optional[int]): Optional number of most common categories to show.
        title (Optional[str]): Optional chart title.
        xlabel (Optional[str]): Optional x-axis label.
        ylabel (Optional[str]): Optional y-axis label.
        figsize (FigureSize): Matplotlib figure size.
        color (Optional[str]): Optional bar color.
        rotation (int): X tick label rotation in degrees.
        theme (str): Styling theme name.
        grid (bool): Whether to show y-axis grid lines.
        grid_alpha (float): Grid opacity.
        **kwargs: Additional keyword arguments forwarded to ``Axes.bar``.

    Returns:
        matplotlib.axes.Axes: Axes containing the frequency chart.

    Raises:
        TypeError: If input data cannot be represented as a pandas Series.
        ValueError: If no categories remain or ``top_n`` is invalid.

    Examples:
        ```python
        ax = frequency_bar_static(["A", "B", "A"])
        ```

    Notes:
        Use ``normalize=True`` when relative frequency is more meaningful than count.
    """
    counts = category_counts(data, normalize=normalize, dropna=dropna, sort=sort, top_n=top_n)
    ylabel = ylabel or ("Proportion" if normalize else "Count")
    ax = setup_plot(
        title=title or "Category Frequency",
        xlabel=xlabel or "Category",
        ylabel=ylabel,
        figsize=figsize,
    )[1]
    ax.bar(counts.index.astype(str), counts.to_numpy(), color=color, **kwargs)
    ax.tick_params(axis="x", rotation=rotation)
    if grid:
        ax.grid(True, axis="y", alpha=grid_alpha)
    apply_theme(ax, theme)
    return ax


def frequency_bar_interactive(
    data: SeriesLike,
    normalize: bool = False,
    dropna: bool = True,
    sort: bool = True,
    top_n: Optional[int] = None,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    color: Optional[str] = None,
    template: str = "plotly",
    height: int = 600,
    width: int = 1000,
    **kwargs,
) -> PlotlyFigure:
    """Create an interactive categorical frequency bar chart.

    Args:
        data (SeriesLike): Input categorical observations.
        normalize (bool): Whether to plot proportions instead of counts.
        dropna (bool): Whether to omit missing values.
        sort (bool): Whether to sort categories by frequency descending.
        top_n (Optional[int]): Optional number of most common categories to show.
        title (Optional[str]): Optional chart title.
        xlabel (Optional[str]): Optional x-axis label.
        ylabel (Optional[str]): Optional y-axis label.
        color (Optional[str]): Optional bar color.
        template (str): Plotly template name.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.
        **kwargs: Additional keyword arguments forwarded to ``go.Bar``.

    Returns:
        plotly.graph_objects.Figure: Interactive frequency chart.

    Raises:
        TypeError: If input data cannot be represented as a pandas Series.
        ValueError: If no categories remain or ``top_n`` is invalid.

    Examples:
        ```python
        fig = frequency_bar_interactive(["A", "B", "A"])
        ```

    Notes:
        Hover labels show the category and frequency value.
    """
    counts = category_counts(data, normalize=normalize, dropna=dropna, sort=sort, top_n=top_n)
    ylabel = ylabel or ("Proportion" if normalize else "Count")
    fig = go.Figure(
        go.Bar(x=counts.index.astype(str), y=counts.to_numpy(), marker_color=color, **kwargs)
    )
    fig.update_layout(
        title=title or "Category Frequency",
        xaxis_title=xlabel or "Category",
        yaxis_title=ylabel,
        template=template,
        height=height,
        width=width,
    )
    return fig


def pareto_chart_static(
    data: SeriesLike,
    dropna: bool = True,
    top_n: Optional[int] = None,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: str = "Count",
    cumulative_label: str = "Cumulative %",
    figsize: FigureSize = (10, 6),
    color: Optional[str] = None,
    line_color: str = "crimson",
    theme: str = "default",
    **kwargs,
) -> MatplotlibAxes:
    """Create a static Pareto chart for categorical frequencies.

    Args:
        data (SeriesLike): Input categorical observations.
        dropna (bool): Whether to omit missing values.
        top_n (Optional[int]): Optional number of most common categories to show.
        title (Optional[str]): Optional chart title.
        xlabel (Optional[str]): Optional x-axis label.
        ylabel (str): Left y-axis label for counts.
        cumulative_label (str): Right y-axis label for cumulative percentage.
        figsize (FigureSize): Matplotlib figure size.
        color (Optional[str]): Optional bar color.
        line_color (str): Cumulative percentage line color.
        theme (str): Styling theme name.
        **kwargs: Additional keyword arguments forwarded to ``Axes.bar``.

    Returns:
        matplotlib.axes.Axes: Primary axes containing the Pareto bars.

    Raises:
        TypeError: If input data cannot be represented as a pandas Series.
        ValueError: If no categories remain or ``top_n`` is invalid.

    Examples:
        ```python
        ax = pareto_chart_static(defect_types)
        ```

    Notes:
        The cumulative line is drawn on a secondary y-axis.
    """
    counts = category_counts(data, normalize=False, dropna=dropna, sort=True, top_n=top_n)
    cumulative = counts.cumsum() / counts.sum() * 100
    fig, ax = setup_plot(title=title or "Pareto Chart", xlabel=xlabel or "Category", ylabel=ylabel, figsize=figsize)
    ax.bar(counts.index.astype(str), counts.to_numpy(), color=color, **kwargs)
    ax.tick_params(axis="x", rotation=45)
    ax2 = ax.twinx()
    ax2.plot(counts.index.astype(str), cumulative.to_numpy(), color=line_color, marker="o")
    ax2.set_ylabel(cumulative_label)
    ax2.set_ylim(0, 105)
    apply_theme(ax, theme)
    return ax


def pareto_chart_interactive(
    data: SeriesLike,
    dropna: bool = True,
    top_n: Optional[int] = None,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: str = "Count",
    cumulative_label: str = "Cumulative %",
    color: Optional[str] = None,
    line_color: str = "crimson",
    template: str = "plotly",
    height: int = 600,
    width: int = 1000,
    **kwargs,
) -> PlotlyFigure:
    """Create an interactive Pareto chart for categorical frequencies.

    Args:
        data (SeriesLike): Input categorical observations.
        dropna (bool): Whether to omit missing values.
        top_n (Optional[int]): Optional number of most common categories to show.
        title (Optional[str]): Optional chart title.
        xlabel (Optional[str]): Optional x-axis label.
        ylabel (str): Left y-axis label for counts.
        cumulative_label (str): Right y-axis label for cumulative percentage.
        color (Optional[str]): Optional bar color.
        line_color (str): Cumulative percentage line color.
        template (str): Plotly template name.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.
        **kwargs: Additional keyword arguments forwarded to ``go.Bar``.

    Returns:
        plotly.graph_objects.Figure: Interactive Pareto chart.

    Raises:
        TypeError: If input data cannot be represented as a pandas Series.
        ValueError: If no categories remain or ``top_n`` is invalid.

    Examples:
        ```python
        fig = pareto_chart_interactive(defect_types)
        ```

    Notes:
        The cumulative percentage trace uses the secondary y-axis.
    """
    counts = category_counts(data, normalize=False, dropna=dropna, sort=True, top_n=top_n)
    cumulative = counts.cumsum() / counts.sum() * 100
    categories = counts.index.astype(str)
    fig = go.Figure()
    fig.add_trace(go.Bar(x=categories, y=counts.to_numpy(), name=ylabel, marker_color=color, **kwargs))
    fig.add_trace(
        go.Scatter(
            x=categories,
            y=cumulative.to_numpy(),
            name=cumulative_label,
            yaxis="y2",
            mode="lines+markers",
            line=dict(color=line_color),
        )
    )
    fig.update_layout(
        title=title or "Pareto Chart",
        xaxis_title=xlabel or "Category",
        yaxis_title=ylabel,
        yaxis2=dict(title=cumulative_label, overlaying="y", side="right", range=[0, 105]),
        template=template,
        height=height,
        width=width,
    )
    return fig
