"""Exploratory Data Analysis (EDA) visualization charts."""

from typing import Optional
from ..types import MatplotlibAxes, MatplotlibFigure, SeriesLike
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ..utils import setup_plot, apply_theme


def missing_data_plot(
    df: pd.DataFrame,
    title: str = "Missing Data Analysis",
    **kwargs
) -> MatplotlibAxes:
    """Visualize missing values by dataframe column.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        df (pd.DataFrame): Input dataframe containing the variables to visualize.
        title (str): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``'Missing Data Analysis'``.
        **kwargs (Any): Additional keyword arguments forwarded to the underlying plotting function.
    
    Returns:
        matplotlib.axes.Axes: Configured matplotlib axes containing the rendered static chart.
    
    Raises:
        TypeError: If required inputs are not compatible with the plotting backend.
        ValueError: If input lengths, matrix shapes, or option values are invalid for the requested chart.
    
    Example:
        ```python
        import dataviz as dv
        result = dv.missing_data_plot(df)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
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
) -> MatplotlibFigure:
    """Create summary charts for dataframe column distributions.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        df (pd.DataFrame): Input dataframe containing the variables to visualize.
        title (str): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``'Distribution Summary'``.
        **kwargs (Any): Additional keyword arguments forwarded to the underlying plotting function.
    
    Returns:
        matplotlib.figure.Figure: Configured matplotlib figure containing the rendered static chart.
    
    Raises:
        TypeError: If required inputs are not compatible with the plotting backend.
        ValueError: If input lengths, matrix shapes, or option values are invalid for the requested chart.
    
    Example:
        ```python
        import dataviz as dv
        result = dv.distribution_summary(df)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
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
    series: SeriesLike,
    title: Optional[str] = None,
    **kwargs
) -> MatplotlibAxes:
    """Visualize class frequencies for a target variable.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        series (SeriesLike): Input series containing categorical or numeric values to summarize.
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
        result = dv.class_distribution(series)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
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
