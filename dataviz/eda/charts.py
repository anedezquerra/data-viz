"""Exploratory Data Analysis (EDA) visualization charts."""

from typing import Optional
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ..utils import setup_plot, apply_theme


def missing_data_plot(
    df: pd.DataFrame,
    title: str = "Missing Data Analysis",
    **kwargs
) -> plt.Axes:
    """
    Visualize missing data patterns in the dataset.

    Parameters
    ----------
    df : DataFrame
        Input data
    title : str, default "Missing Data Analysis"
        Chart title
    **kwargs
        Additional plot arguments

    Returns
    -------
    matplotlib.axes.Axes
        The plot axes
    """
    fig, ax = setup_plot(title=title, figsize=(12, 6))
    
    missing = df.isnull().sum()
    missing_pct = (missing / len(df)) * 100
    
    if missing.sum() > 0:
        ax.barh(missing[missing > 0].index, missing_pct[missing > 0])
        ax.set_xlabel('Percentage Missing (%)')
        apply_theme(ax)
    else:
        ax.text(0.5, 0.5, 'No missing data found', 
                ha='center', va='center', transform=ax.transAxes)
    
    return ax


def distribution_summary(
    df: pd.DataFrame,
    title: str = "Distribution Summary",
    **kwargs
) -> plt.Figure:
    """
    Create subplots showing distribution of all numeric columns.

    Parameters
    ----------
    df : DataFrame
        Input data
    title : str, default "Distribution Summary"
        Figure title
    **kwargs
        Additional plot arguments

    Returns
    -------
    matplotlib.figure.Figure
        The figure object
    """
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    n_cols = len(numeric_cols)
    
    if n_cols == 0:
        fig, ax = plt.subplots()
        return fig
    
    n_rows = (n_cols + 2) // 3
    fig, axes = plt.subplots(n_rows, 3, figsize=(15, 5*n_rows))
    fig.suptitle(title, fontsize=14, fontweight='bold')
    
    axes = axes.flatten() if isinstance(axes, np.ndarray) else [axes]
    
    for idx, col in enumerate(numeric_cols):
        axes[idx].hist(df[col], bins=30, **kwargs)
        axes[idx].set_title(col)
        axes[idx].set_ylabel('Frequency')
    
    # Hide unused subplots
    for idx in range(len(numeric_cols), len(axes)):
        axes[idx].set_visible(False)
    
    plt.tight_layout()
    return fig


def class_distribution(
    series: pd.Series,
    title: Optional[str] = None,
    **kwargs
) -> plt.Axes:
    """
    Visualize the distribution of classes in a categorical variable.

    Parameters
    ----------
    series : Series
        Categorical data
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
        title = f"Class Distribution - {series.name if hasattr(series, 'name') else 'Distribution'}"
    
    fig, ax = setup_plot(title=title, figsize=(10, 6))
    
    value_counts = series.value_counts()
    ax.bar(value_counts.index, value_counts.values, **kwargs)
    ax.set_ylabel('Count')
    ax.set_xlabel('Class')
    
    apply_theme(ax)
    
    return ax
