"""Core plotting functionality for DataViz."""

from typing import Any, Optional

import matplotlib.pyplot as plt

from .types import MatplotlibAxes


def plot(
    data: Any,
    x: Optional[str] = None,
    y: Optional[str] = None,
    kind: str = "line",
    **kwargs: Any
) -> MatplotlibAxes:
    """Create a general-purpose plot from dataframe-like or array-like data.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        data (Any): Input observations, measurements, or values used to build the chart.
        x (Optional[str]): Values plotted along the x-axis. Defaults to ``None``.
        y (Optional[str]): Values plotted along the y-axis. Defaults to ``None``.
        kind (str): Configuration value for ``kind``. Defaults to ``'line'``.
        **kwargs (Any): Additional keyword arguments forwarded to the underlying plotting function.
    
    Returns:
        matplotlib.axes.Axes: Configured matplotlib axes containing the rendered chart.
    
    Raises:
        TypeError: If required inputs are not compatible with the plotting backend.
        ValueError: If input lengths, matrix shapes, or option values are invalid for the requested chart.
    
    Example:
        ```python
        import dataviz as dv
        result = dv.plot(data, x, y)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
    """
    fig, ax = plt.subplots()
    
    if hasattr(data, 'plot'):
        # pandas DataFrame or Series
        data.plot(x=x, y=y, kind=kind, ax=ax, **kwargs)
    else:
        # array-like data
        ax.plot(data, **kwargs)
    
    return ax
