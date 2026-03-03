"""Multivariate relationships visualization charts."""

from typing import Optional
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ..utils import setup_plot, apply_theme


def pairplot(
    df: pd.DataFrame,
    title: str = "Pairplot",
    **kwargs
) -> plt.Figure:
    """
    Create pairwise relationships plot for all numeric columns.

    Parameters
    ----------
    df : DataFrame
        Input data
    title : str, default "Pairplot"
        Figure title
    **kwargs
        Additional arguments

    Returns
    -------
    matplotlib.figure.Figure
        The figure object
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
) -> plt.Axes:
    """
    Create a heatmap visualization of data.

    Parameters
    ----------
    df : DataFrame
        Input data
    title : str, default "Heatmap"
        Chart title
    cmap : str, default 'viridis'
        Colormap name
    **kwargs
        Additional heatmap arguments

    Returns
    -------
    matplotlib.axes.Axes
        The plot axes
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
) -> plt.Axes:
    """
    Create a parallel coordinates plot for exploring multivariate data.

    Parameters
    ----------
    df : DataFrame
        Input data (numeric columns only)
    title : str, default "Parallel Coordinates"
        Chart title
    **kwargs
        Additional plot arguments

    Returns
    -------
    matplotlib.axes.Axes
        The plot axes
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
