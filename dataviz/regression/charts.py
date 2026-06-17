"""Regression analysis visualization charts."""

from typing import Optional
from ..types import ArrayLike, MatplotlibAxes
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ..utils import setup_plot, apply_theme


def residual_plot(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    title: str = "Residual Plot",
    **kwargs
) -> MatplotlibAxes:
    """Create a residual diagnostic plot for regression predictions.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        y_true (ArrayLike): Observed target values.
        y_pred (ArrayLike): Predicted target values.
        title (str): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``'Residual Plot'``.
        **kwargs (Any): Additional keyword arguments forwarded to the underlying plotting function.
    
    Returns:
        matplotlib.axes.Axes: Configured matplotlib axes containing the rendered static chart.
    
    Raises:
        TypeError: If required inputs are not compatible with the plotting backend.
        ValueError: If input lengths, matrix shapes, or option values are invalid for the requested chart.
    
    Example:
        ```python
        import dataviz as dv
        result = dv.residual_plot(y_true, y_pred)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
    """
    residuals = y_true - y_pred
    
    fig, ax = setup_plot(title=title, xlabel='Predicted Values', ylabel='Residuals')
    ax.scatter(y_pred, residuals, alpha=0.6, **kwargs)
    ax.axhline(y=0, color='r', linestyle='--', linewidth=2)
    
    apply_theme(ax)
    
    return ax


def prediction_plot(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    title: str = "Prediction Plot",
    **kwargs
) -> MatplotlibAxes:
    """Compare observed and predicted regression values.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        y_true (ArrayLike): Observed target values.
        y_pred (ArrayLike): Predicted target values.
        title (str): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``'Prediction Plot'``.
        **kwargs (Any): Additional keyword arguments forwarded to the underlying plotting function.
    
    Returns:
        matplotlib.axes.Axes: Configured matplotlib axes containing the rendered static chart.
    
    Raises:
        TypeError: If required inputs are not compatible with the plotting backend.
        ValueError: If input lengths, matrix shapes, or option values are invalid for the requested chart.
    
    Example:
        ```python
        import dataviz as dv
        result = dv.prediction_plot(y_true, y_pred)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
    """
    fig, ax = setup_plot(title=title, xlabel='Actual Values', ylabel='Predicted Values')
    
    ax.scatter(y_true, y_pred, alpha=0.6, **kwargs)
    
    # Add perfect prediction line
    min_val = min(y_true.min(), y_pred.min())
    max_val = max(y_true.max(), y_pred.max())
    ax.plot([min_val, max_val], [min_val, max_val], 'r--', linewidth=2, label='Perfect Prediction')
    
    ax.legend()
    apply_theme(ax)
    
    return ax


def learning_curve(
    train_sizes: ArrayLike,
    train_scores: ArrayLike,
    val_scores: ArrayLike,
    title: str = "Learning Curve",
    **kwargs
) -> MatplotlibAxes:
    """Plot model performance across training-set sizes.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        train_sizes (ArrayLike): Training-set sizes used to compute learning-curve scores.
        train_scores (ArrayLike): Training scores corresponding to each training-set size.
        val_scores (ArrayLike): Validation scores corresponding to each training-set size.
        title (str): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``'Learning Curve'``.
        **kwargs (Any): Additional keyword arguments forwarded to the underlying plotting function.
    
    Returns:
        matplotlib.axes.Axes: Configured matplotlib axes containing the rendered static chart.
    
    Raises:
        TypeError: If required inputs are not compatible with the plotting backend.
        ValueError: If input lengths, matrix shapes, or option values are invalid for the requested chart.
    
    Example:
        ```python
        import dataviz as dv
        result = dv.learning_curve(train_sizes)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
    """
    fig, ax = setup_plot(title=title, xlabel='Training Set Size', ylabel='Score')
    
    ax.plot(train_sizes, train_scores, 'o-', label='Training Score', **kwargs)
    ax.plot(train_sizes, val_scores, 'o-', label='Validation Score', **kwargs)
    
    ax.legend()
    ax.grid(True, alpha=0.3)
    apply_theme(ax)
    
    return ax
