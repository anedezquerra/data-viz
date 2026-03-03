"""Bivariate relationships visualization charts."""

from typing import Optional
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ..utils import setup_plot, apply_theme


def scatter_plot(
    x: pd.Series,
    y: pd.Series,
    title: Optional[str] = None,
    **kwargs
) -> plt.Axes:
    """
    Create a scatter plot showing relationship between two variables.

    Parameters
    ----------
    x : Series or array-like
        X-axis data
    y : Series or array-like
        Y-axis data
    title : str, optional
        Chart title
    **kwargs
        Additional scatter plot arguments

    Returns
    -------
    matplotlib.axes.Axes
        The plot axes
    """
    if title is None:
        x_name = x.name if hasattr(x, 'name') else 'X'
        y_name = y.name if hasattr(y, 'name') else 'Y'
        title = f"Scatter Plot: {x_name} vs {y_name}"
    
    x_label = x.name if hasattr(x, 'name') else 'X'
    y_label = y.name if hasattr(y, 'name') else 'Y'
    
    fig, ax = setup_plot(title=title, xlabel=x_label, ylabel=y_label)
    ax.scatter(x, y, alpha=0.6, **kwargs)
    apply_theme(ax)
    
    return ax


def line_plot(
    x: pd.Series,
    y: pd.Series,
    title: Optional[str] = None,
    **kwargs
) -> plt.Axes:
    """
    Create a line plot showing relationship between two variables over time/order.

    Parameters
    ----------
    x : Series or array-like
        X-axis data
    y : Series or array-like
        Y-axis data
    title : str, optional
        Chart title
    **kwargs
        Additional line plot arguments

    Returns
    -------
    matplotlib.axes.Axes
        The plot axes
    """
    if title is None:
        x_name = x.name if hasattr(x, 'name') else 'X'
        y_name = y.name if hasattr(y, 'name') else 'Y'
        title = f"Line Plot: {x_name} vs {y_name}"
    
    x_label = x.name if hasattr(x, 'name') else 'X'
    y_label = y.name if hasattr(y, 'name') else 'Y'
    
    fig, ax = setup_plot(title=title, xlabel=x_label, ylabel=y_label)
    ax.plot(x, y, **kwargs)
    apply_theme(ax)
    
    return ax


def correlation_heatmap(
    df: pd.DataFrame,
    title: str = "Correlation Heatmap",
    **kwargs
) -> plt.Axes:
    """
    Create a heatmap showing correlations between variables.

    Parameters
    ----------
    df : DataFrame
        Input data
    title : str, default "Correlation Heatmap"
        Chart title
    **kwargs
        Additional heatmap arguments

    Returns
    -------
    matplotlib.axes.Axes
        The plot axes
    """
    fig, ax = setup_plot(title=title)
    
    corr_matrix = df.corr()
    im = ax.imshow(corr_matrix, cmap='coolwarm', aspect='auto', vmin=-1, vmax=1)
    
    ax.set_xticks(range(len(corr_matrix.columns)))
    ax.set_yticks(range(len(corr_matrix.columns)))
    ax.set_xticklabels(corr_matrix.columns, rotation=45, ha='right')
    ax.set_yticklabels(corr_matrix.columns)
    
    plt.colorbar(im, ax=ax)
    
    return ax
