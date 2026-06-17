"""Explainable AI (XAI) visualization charts."""

from typing import Optional, List
from ..types import ArrayLike, Labels, MatplotlibAxes, MatrixLike, SeriesLike
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ..utils import setup_plot, apply_theme


def feature_importance(
    importances: SeriesLike,
    title: str = "Feature Importance",
    top_n: Optional[int] = None,
    **kwargs
) -> MatplotlibAxes:
    """Visualize model feature-importance values.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        importances (SeriesLike): Feature-importance values indexed or paired with feature names.
        title (str): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``'Feature Importance'``.
        top_n (Optional[int]): Maximum number of highest-ranked features to display. Defaults to ``None``.
        **kwargs (Any): Additional keyword arguments forwarded to the underlying plotting function.
    
    Returns:
        matplotlib.axes.Axes: Configured matplotlib axes containing the rendered static chart.
    
    Raises:
        TypeError: If required inputs are not compatible with the plotting backend.
        ValueError: If input lengths, matrix shapes, or option values are invalid for the requested chart.
    
    Example:
        ```python
        import dataviz as dv
        result = dv.feature_importance(importances)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
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
    shap_values: MatrixLike,
    feature_names: Labels,
    title: str = "SHAP Feature Importance",
    **kwargs
) -> MatplotlibAxes:
    """Visualize SHAP values for explainable model analysis.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        shap_values (MatrixLike): SHAP contribution values to summarize or plot.
        feature_names (Labels): Names of the features represented by the values.
        title (str): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``'SHAP Feature Importance'``.
        **kwargs (Any): Additional keyword arguments forwarded to the underlying plotting function.
    
    Returns:
        matplotlib.axes.Axes: Configured matplotlib axes containing the rendered static chart.
    
    Raises:
        TypeError: If required inputs are not compatible with the plotting backend.
        ValueError: If input lengths, matrix shapes, or option values are invalid for the requested chart.
    
    Example:
        ```python
        import dataviz as dv
        result = dv.shap_plot(shap_values)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
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
    feature_values: ArrayLike,
    predictions: ArrayLike,
    feature_name: str = "Feature",
    title: Optional[str] = None,
    **kwargs
) -> MatplotlibAxes:
    """Visualize a partial-dependence relationship for one feature.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        feature_values (ArrayLike): Feature grid or observed feature values for partial dependence.
        predictions (ArrayLike): Predicted response values corresponding to the feature grid.
        feature_name (str): Configuration value for ``feature_name``. Defaults to ``'Feature'``.
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
        result = dv.partial_dependence(feature_values, predictions)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
    """
    if title is None:
        title = f"Partial Dependence - {feature_name}"
    
    fig, ax = setup_plot(title=title, xlabel=feature_name, ylabel='Prediction')
    ax.plot(feature_values, predictions, marker='o', **kwargs)
    
    apply_theme(ax)
    
    return ax
