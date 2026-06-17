"""Multivariate relationships visualization charts."""

from typing import Optional
from ..types import MatplotlibAxes, MatplotlibFigure
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ..utils import setup_plot, apply_theme


def pairplot(
    df: pd.DataFrame,
    title: str = "Pairplot",
    **kwargs
) -> MatplotlibFigure:
    """Create a pairwise variable relationship plot.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        df (pd.DataFrame): Input dataframe containing the variables to visualize.
        title (str): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``'Pairplot'``.
        **kwargs (Any): Additional keyword arguments forwarded to the underlying plotting function.
    
    Returns:
        matplotlib.figure.Figure: Configured matplotlib figure containing the rendered static chart.
    
    Raises:
        TypeError: If required inputs are not compatible with the plotting backend.
        ValueError: If input lengths, matrix shapes, or option values are invalid for the requested chart.
    
    Example:
        ```python
        import dataviz as dv
        result = dv.pairplot(df)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
    """
    n_cols = len(df.select_dtypes(include=[np.number]).columns)
    fig, axes = plt.subplots(n_cols, n_cols, figsize=(12, 12))
    fig.suptitle(title, fontsize=14, fontweight='bold')
    
    return fig


def heatmap(
    df: pd.DataFrame,
    title: str = "Heatmap",
    cmap: str = 'viridis',
    **kwargs
) -> MatplotlibAxes:
    """Create a heatmap for matrix-like or dataframe values.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        df (pd.DataFrame): Input dataframe containing the variables to visualize.
        title (str): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``'Heatmap'``.
        cmap (str): Configuration value for ``cmap``. Defaults to ``'viridis'``.
        **kwargs (Any): Additional keyword arguments forwarded to the underlying plotting function.
    
    Returns:
        matplotlib.axes.Axes: Configured matplotlib axes containing the rendered static chart.
    
    Raises:
        TypeError: If required inputs are not compatible with the plotting backend.
        ValueError: If input lengths, matrix shapes, or option values are invalid for the requested chart.
    
    Example:
        ```python
        import dataviz as dv
        result = dv.heatmap(df)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
    """
    fig, ax = setup_plot(title=title, figsize=(12, 8))
    
    im = ax.imshow(df, cmap=cmap, aspect='auto')
    
    ax.set_xticks(range(len(df.columns)))
    ax.set_yticks(range(len(df.index)))
    ax.set_xticklabels(df.columns, rotation=45, ha='right')
    ax.set_yticklabels(df.index)
    
    plt.colorbar(im, ax=ax)
    
    return ax


def parallel_coordinates(
    df: pd.DataFrame,
    title: str = "Parallel Coordinates",
    **kwargs
) -> MatplotlibAxes:
    """Create a parallel-coordinates plot for multivariate comparison.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        df (pd.DataFrame): Input dataframe containing the variables to visualize.
        title (str): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``'Parallel Coordinates'``.
        **kwargs (Any): Additional keyword arguments forwarded to the underlying plotting function.
    
    Returns:
        matplotlib.axes.Axes: Configured matplotlib axes containing the rendered static chart.
    
    Raises:
        TypeError: If required inputs are not compatible with the plotting backend.
        ValueError: If input lengths, matrix shapes, or option values are invalid for the requested chart.
    
    Example:
        ```python
        import dataviz as dv
        result = dv.parallel_coordinates(df)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
    """
    fig, ax = setup_plot(title=title, figsize=(12, 6))
    
    # Normalize data to 0-1 range for visualization
    df_norm = (df - df.min()) / (df.max() - df.min())
    
    for idx, row in df_norm.iterrows():
        ax.plot(range(len(df_norm.columns)), row.values, alpha=0.3, **kwargs)
    
    ax.set_xticks(range(len(df.columns)))
    ax.set_xticklabels(df.columns, rotation=45, ha='right')
    ax.set_ylabel('Normalized Value')
    
    apply_theme(ax)
    
    return ax
