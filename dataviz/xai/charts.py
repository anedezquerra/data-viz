"""Explainable AI (XAI) visualization charts."""

from typing import Optional, List
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ..utils import setup_plot, apply_theme


def feature_importance(
    importances: pd.Series,
    title: str = "Feature Importance",
    top_n: Optional[int] = None,
    **kwargs
) -> plt.Axes:
    """
    Visualize feature importance scores.

    Parameters
    ----------
    importances : Series
        Feature importance values with feature names as index
    title : str, default "Feature Importance"
        Chart title
    top_n : int, optional
        Show only top N features
    **kwargs
        Additional plot arguments

    Returns
    -------
    matplotlib.axes.Axes
        The plot axes
    """
    if top_n is not None:
        importances = importances.nlargest(top_n)
    
    importances_sorted = importances.sort_values(ascending=True)
    
    fig, ax = setup_plot(title=title, figsize=(10, 6))
    ax.barh(importances_sorted.index, importances_sorted.values, **kwargs)
    ax.set_xlabel('Importance')
    
    apply_theme(ax)
    
    return ax


def shap_plot(
    shap_values: np.ndarray,
    feature_names: List[str],
    title: str = "SHAP Feature Importance",
    **kwargs
) -> plt.Axes:
    """
    Visualize SHAP feature importance (summary plot).

    Parameters
    ----------
    shap_values : array
        SHAP values array
    feature_names : list
        Names of features
    title : str, default "SHAP Feature Importance"
        Chart title
    **kwargs
        Additional plot arguments

    Returns
    -------
    matplotlib.axes.Axes
        The plot axes
    """
    fig, ax = setup_plot(title=title, figsize=(10, 6))
    
    # Calculate mean absolute SHAP values
    mean_abs_shap = np.abs(shap_values).mean(axis=0)
    shap_importance = pd.Series(mean_abs_shap, index=feature_names).sort_values()
    
    ax.barh(shap_importance.index, shap_importance.values, **kwargs)
    ax.set_xlabel('Mean |SHAP value|')
    
    apply_theme(ax)
    
    return ax


def partial_dependence(
    feature_values: np.ndarray,
    predictions: np.ndarray,
    feature_name: str = "Feature",
    title: Optional[str] = None,
    **kwargs
) -> plt.Axes:
    """
    Visualize partial dependence plot for a feature.

    Parameters
    ----------
    feature_values : array
        Values of the feature
    predictions : array
        Predicted values/probabilities
    feature_name : str, default "Feature"
        Name of the feature
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
        title = f"Partial Dependence - {feature_name}"
    
    fig, ax = setup_plot(title=title, xlabel=feature_name, ylabel='Prediction')
    ax.plot(feature_values, predictions, marker='o', **kwargs)
    
    apply_theme(ax)
    
    return ax
