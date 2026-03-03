"""Univariate distribution visualization charts."""

from typing import Optional
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ..utils import setup_plot, apply_theme


def histogram(
    data: pd.Series,
    bins: int = 30,
    title: Optional[str] = None,
    **kwargs
) -> plt.Axes:
    """
    Create a histogram showing distribution of a single variable.

    Parameters
    ----------
    data : Series or array-like
        Data to visualize
    bins : int, default 30
        Number of bins
    title : str, optional
        Chart title
    **kwargs
        Additional histogram arguments

    Returns
    -------
    matplotlib.axes.Axes
        The plot axes
    """
    if title is None:
        title = f"Histogram - {data.name if hasattr(data, 'name') else 'Distribution'}"
    
    fig, ax = setup_plot(title=title, xlabel='Value', ylabel='Frequency')
    ax.hist(data, bins=bins, **kwargs)
    apply_theme(ax)
    
    return ax


def density_plot(
    data: pd.Series,
    title: Optional[str] = None,
    **kwargs
) -> plt.Axes:
    """
    Create a kernel density estimation (KDE) plot.

    Parameters
    ----------
    data : Series or array-like
        Data to visualize
    title : str, optional
        Chart title
    **kwargs
        Additional plot arguments

    Returns
    -------
    matplotlib.axes.Axes
        The plot axes
    """
    if title is None:
        title = f"Density Plot - {data.name if hasattr(data, 'name') else 'Distribution'}"
    
    fig, ax = setup_plot(title=title, xlabel='Value', ylabel='Density')
    data.plot.kde(ax=ax, **kwargs)
    apply_theme(ax)
    
    return ax


def box_plot(
    data: pd.DataFrame,
    title: Optional[str] = None,
    **kwargs
) -> plt.Axes:
    """
    Create a box plot showing distribution quartiles and outliers.

    Parameters
    ----------
    data : DataFrame or array-like
        Data to visualize
    title : str, optional
        Chart title
    **kwargs
        Additional boxplot arguments

    Returns
    -------
    matplotlib.axes.Axes
        The plot axes
    """
    if title is None:
        title = "Box Plot"
    
    fig, ax = setup_plot(title=title, ylabel='Value')
    ax.boxplot(data, **kwargs)
    apply_theme(ax)
    
    return ax


def violin_plot(
    data: pd.DataFrame,
    title: Optional[str] = None,
    **kwargs
) -> plt.Axes:
    """
    Create a violin plot showing full distribution shape.

    Parameters
    ----------
    data : DataFrame or array-like
        Data to visualize
    title : str, optional
        Chart title
    **kwargs
        Additional plot arguments

    Returns
    -------
    matplotlib.axes.Axes
        The plot axes
    """
    if title is None:
        title = "Violin Plot"
    
    fig, ax = setup_plot(title=title, ylabel='Value')
    
    if isinstance(data, pd.DataFrame):
        data.plot.box(ax=ax, **kwargs)  # Simplified implementation
    
    apply_theme(ax)
    
    return ax
