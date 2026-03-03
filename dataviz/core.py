"""Core plotting functionality for DataViz."""

from typing import Optional, Any
import matplotlib.pyplot as plt


def plot(
    data: Any,
    x: Optional[str] = None,
    y: Optional[str] = None,
    kind: str = "line",
    **kwargs: Any
) -> Any:
    """
    Create a plot from data.

    Parameters
    ----------
    data : DataFrame or array-like
        The data to plot
    x : str, optional
        Column name for x-axis
    y : str, optional
        Column name for y-axis
    kind : str, default 'line'
        Type of plot: 'line', 'bar', 'scatter', etc.
    **kwargs
        Additional arguments passed to matplotlib

    Returns
    -------
    matplotlib.axes.Axes
        The created plot axes object

    Examples
    --------
    >>> import pandas as pd
    >>> import dataviz as dv
    >>> df = pd.DataFrame({'x': [1, 2, 3], 'y': [2, 4, 6]})
    >>> ax = dv.plot(df, x='x', y='y')
    """
    fig, ax = plt.subplots()
    
    if hasattr(data, 'plot'):
        # pandas DataFrame or Series
        data.plot(x=x, y=y, kind=kind, ax=ax, **kwargs)
    else:
        # array-like data
        ax.plot(data, **kwargs)
    
    return ax
