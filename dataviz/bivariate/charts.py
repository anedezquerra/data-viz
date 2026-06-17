"""Compatibility wrappers for bivariate relationship charts."""

from typing import Any

from ..types import MatplotlibAxes
from .correlation import correlation_heatmap_static
from .line import line_plot_static
from .scatter import scatter_plot_static


def scatter_plot(*args: Any, **kwargs: Any) -> MatplotlibAxes:
    """Create a static scatter plot to compare two variables.

    Args:
        *args (Any): Positional arguments forwarded to ``scatter_plot_static``.
        **kwargs (Any): Keyword arguments forwarded to ``scatter_plot_static``.

    Returns:
        matplotlib.axes.Axes: Configured matplotlib axes containing the scatter plot.

    Raises:
        TypeError: If inputs cannot be resolved or plotted.
        ValueError: If input lengths differ, inputs are empty, or options are invalid.

    Example:
        ```python
        ax = scatter_plot(x, y)
        ```

    Notes:
        This wrapper preserves the legacy ``dataviz.bivariate.charts`` API.
    """
    return scatter_plot_static(*args, **kwargs)


def line_plot(*args: Any, **kwargs: Any) -> MatplotlibAxes:
    """Create a static line plot for ordered bivariate data.

    Args:
        *args (Any): Positional arguments forwarded to ``line_plot_static``.
        **kwargs (Any): Keyword arguments forwarded to ``line_plot_static``.

    Returns:
        matplotlib.axes.Axes: Configured matplotlib axes containing the line plot.

    Raises:
        TypeError: If inputs cannot be resolved or plotted.
        ValueError: If input lengths differ, inputs are empty, or options are invalid.

    Example:
        ```python
        ax = line_plot(x, y)
        ```

    Notes:
        This wrapper preserves the legacy ``dataviz.bivariate.charts`` API.
    """
    return line_plot_static(*args, **kwargs)


def correlation_heatmap(*args: Any, **kwargs: Any) -> MatplotlibAxes:
    """Create a static heatmap of pairwise correlations.

    Args:
        *args (Any): Positional arguments forwarded to ``correlation_heatmap_static``.
        **kwargs (Any): Keyword arguments forwarded to ``correlation_heatmap_static``.

    Returns:
        matplotlib.axes.Axes: Configured matplotlib axes containing the correlation heatmap.

    Raises:
        TypeError: If the input is not dataframe-like.
        ValueError: If too few numeric columns exist or options are invalid.

    Example:
        ```python
        ax = correlation_heatmap(df)
        ```

    Notes:
        This wrapper preserves the legacy ``dataviz.bivariate.charts`` API.
    """
    return correlation_heatmap_static(*args, **kwargs)
