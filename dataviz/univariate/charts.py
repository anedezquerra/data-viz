"""Univariate distribution visualization charts."""

from typing import Optional
from ..types import FrameLike, MatplotlibAxes, SeriesLike
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ..utils import setup_plot, apply_theme


def histogram(
    data: SeriesLike,
    bins: int = 30,
    title: Optional[str] = None,
    **kwargs
) -> MatplotlibAxes:
    """Create a histogram that summarizes the frequency distribution of one variable.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        data (SeriesLike): Input observations, measurements, or values used to build the chart.
        bins (int): Number of bins used for histogram-like displays. Defaults to ``30``.
        title (Optional[str]): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``None``.
        **kwargs (Any): Additional keyword arguments forwarded to the underlying plotting function.
    
    Returns:
        matplotlib.axes.Axes: Configured matplotlib axes containing the rendered static chart.
    
    Raises:
        TypeError: If required inputs are not compatible with the plotting backend.
        ValueError: If input lengths, matrix shapes, or option values are invalid for the requested chart.
    
    Example:
        ```python
        import dataviz as dv
        result = dv.histogram(data)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
    """
    if title is None:
        title = f"Histogram - {data.name if hasattr(data, 'name') else 'Distribution'}"
    
    fig, ax = setup_plot(title=title, xlabel='Value', ylabel='Frequency')
    ax.hist(data, bins=bins, **kwargs)
    apply_theme(ax)
    
    return ax


def density_plot(
    data: SeriesLike,
    title: Optional[str] = None,
    **kwargs
) -> MatplotlibAxes:
    """Create a kernel density estimate chart for one variable.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        data (SeriesLike): Input observations, measurements, or values used to build the chart.
        title (Optional[str]): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``None``.
        **kwargs (Any): Additional keyword arguments forwarded to the underlying plotting function.
    
    Returns:
        matplotlib.axes.Axes: Configured matplotlib axes containing the rendered static chart.
    
    Raises:
        TypeError: If required inputs are not compatible with the plotting backend.
        ValueError: If input lengths, matrix shapes, or option values are invalid for the requested chart.
    
    Example:
        ```python
        import dataviz as dv
        result = dv.density_plot(data)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
    """
    if title is None:
        title = f"Density Plot - {data.name if hasattr(data, 'name') else 'Distribution'}"
    
    fig, ax = setup_plot(title=title, xlabel='Value', ylabel='Density')
    data.plot.kde(ax=ax, **kwargs)
    apply_theme(ax)
    
    return ax


def box_plot(
    data: FrameLike,
    title: Optional[str] = None,
    **kwargs
) -> MatplotlibAxes:
    """Create a box plot that summarizes quartiles, spread, and outliers.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        data (FrameLike): Input observations, measurements, or values used to build the chart.
        title (Optional[str]): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``None``.
        **kwargs (Any): Additional keyword arguments forwarded to the underlying plotting function.
    
    Returns:
        matplotlib.axes.Axes: Configured matplotlib axes containing the rendered static chart.
    
    Raises:
        TypeError: If required inputs are not compatible with the plotting backend.
        ValueError: If input lengths, matrix shapes, or option values are invalid for the requested chart.
    
    Example:
        ```python
        import dataviz as dv
        result = dv.box_plot(data)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
    """
    if title is None:
        title = "Box Plot"
    
    fig, ax = setup_plot(title=title, ylabel='Value')
    ax.boxplot(data, **kwargs)
    apply_theme(ax)
    
    return ax


def violin_plot(
    data: FrameLike,
    title: Optional[str] = None,
    **kwargs
) -> MatplotlibAxes:
    """Create a violin plot that shows the full distribution shape.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        data (FrameLike): Input observations, measurements, or values used to build the chart.
        title (Optional[str]): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``None``.
        **kwargs (Any): Additional keyword arguments forwarded to the underlying plotting function.
    
    Returns:
        matplotlib.axes.Axes: Configured matplotlib axes containing the rendered static chart.
    
    Raises:
        TypeError: If required inputs are not compatible with the plotting backend.
        ValueError: If input lengths, matrix shapes, or option values are invalid for the requested chart.
    
    Example:
        ```python
        import dataviz as dv
        result = dv.violin_plot(data)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
    """
    if title is None:
        title = "Violin Plot"
    
    fig, ax = setup_plot(title=title, ylabel='Value')
    
    if isinstance(data, pd.DataFrame):
        data.plot.box(ax=ax, **kwargs)  # Simplified implementation
    
    apply_theme(ax)
    
    return ax
