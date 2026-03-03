"""Regression analysis visualization charts."""

from typing import Optional
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ..utils import setup_plot, apply_theme


def residual_plot(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    title: str = "Residual Plot",
    **kwargs
) -> plt.Axes:
    """
    Create a residual plot for regression model diagnostics.

    Parameters
    ----------
    y_true : array
        Actual target values
    y_pred : array
        Predicted values
    title : str, default "Residual Plot"
        Chart title
    **kwargs
        Additional plot arguments

    Returns
    -------
    matplotlib.axes.Axes
        The plot axes
    """
    residuals = y_true - y_pred
    
    fig, ax = setup_plot(title=title, xlabel='Predicted Values', ylabel='Residuals')
    ax.scatter(y_pred, residuals, alpha=0.6, **kwargs)
    ax.axhline(y=0, color='r', linestyle='--', linewidth=2)
    
    apply_theme(ax)
    
    return ax


def prediction_plot(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    title: str = "Prediction Plot",
    **kwargs
) -> plt.Axes:
    """
    Create a prediction vs actual plot for regression models.

    Parameters
    ----------
    y_true : array
        Actual target values
    y_pred : array
        Predicted values
    title : str, default "Prediction Plot"
        Chart title
    **kwargs
        Additional plot arguments

    Returns
    -------
    matplotlib.axes.Axes
        The plot axes
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
    train_sizes: np.ndarray,
    train_scores: np.ndarray,
    val_scores: np.ndarray,
    title: str = "Learning Curve",
    **kwargs
) -> plt.Axes:
    """
    Visualize learning curve showing model performance vs training set size.

    Parameters
    ----------
    train_sizes : array
        Training set sizes
    train_scores : array
        Training scores
    val_scores : array
        Validation scores
    title : str, default "Learning Curve"
        Chart title
    **kwargs
        Additional plot arguments

    Returns
    -------
    matplotlib.axes.Axes
        The plot axes
    """
    fig, ax = setup_plot(title=title, xlabel='Training Set Size', ylabel='Score')
    
    ax.plot(train_sizes, train_scores, 'o-', label='Training Score', **kwargs)
    ax.plot(train_sizes, val_scores, 'o-', label='Validation Score', **kwargs)
    
    ax.legend()
    ax.grid(True, alpha=0.3)
    apply_theme(ax)
    
    return ax
