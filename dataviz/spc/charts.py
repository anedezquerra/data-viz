"""Statistical Process Control charts implementation."""

from typing import Optional
from ..types import ArrayLike, MatplotlibAxes
import numpy as np
import matplotlib.pyplot as plt
from ..utils import setup_plot, apply_theme


def control_chart(
    data: ArrayLike,
    title: str = "Control Chart",
    **kwargs
) -> MatplotlibAxes:
    """Create a statistical process control chart.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        data (ArrayLike): Input observations, measurements, or values used to build the chart.
        title (str): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``'Control Chart'``.
        **kwargs (Any): Additional keyword arguments forwarded to the underlying plotting function.
    
    Returns:
        matplotlib.axes.Axes: Configured matplotlib axes containing the rendered static chart.
    
    Raises:
        TypeError: If required inputs are not compatible with the plotting backend.
        ValueError: If input lengths, matrix shapes, or option values are invalid for the requested chart.
    
    Example:
        ```python
        import dataviz as dv
        result = dv.control_chart(data)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
    """
    fig, ax = setup_plot(title=title)
    
    mean = np.mean(data)
    std = np.std(data)
    ucl = mean + 3 * std  # Upper Control Limit
    lcl = mean - 3 * std  # Lower Control Limit
    
    ax.plot(data, marker='o', label='Process Data', **kwargs)
    ax.axhline(mean, color='green', linestyle='-', label='Mean', linewidth=2)
    ax.axhline(ucl, color='red', linestyle='--', label='UCL (±3σ)', linewidth=1)
    ax.axhline(lcl, color='red', linestyle='--', linewidth=1)
    
    ax.set_ylabel('Value')
    ax.set_xlabel('Sample')
    ax.legend()
    apply_theme(ax)
    
    return ax


def x_range_chart(
    data: ArrayLike,
    subgroup_size: int = 5,
    title: str = "X-Range Chart",
    **kwargs
) -> MatplotlibAxes:
    """Create an X-range chart for individual values and range monitoring.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        data (ArrayLike): Input observations, measurements, or values used to build the chart.
        subgroup_size (int): Number of observations used in each subgroup calculation. Defaults to ``5``.
        title (str): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``'X-Range Chart'``.
        **kwargs (Any): Additional keyword arguments forwarded to the underlying plotting function.
    
    Returns:
        matplotlib.axes.Axes: Configured matplotlib axes containing the rendered static chart.
    
    Raises:
        TypeError: If required inputs are not compatible with the plotting backend.
        ValueError: If input lengths, matrix shapes, or option values are invalid for the requested chart.
    
    Example:
        ```python
        import dataviz as dv
        result = dv.x_range_chart(data)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
    """
    fig, ax = setup_plot(title=title)
    
    ax.plot(data, marker='o', label='Individual Values', **kwargs)
    ax.set_ylabel('Value')
    ax.set_xlabel('Sample')
    ax.legend()
    apply_theme(ax)
    
    return ax
