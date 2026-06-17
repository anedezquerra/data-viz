"""Classification analysis visualization charts."""

from typing import Optional
from ..types import ArrayLike, Labels, MatplotlibAxes, MatrixLike
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ..utils import setup_plot, apply_theme


def confusion_matrix_plot(
    cm: MatrixLike,
    labels: Optional[Labels] = None,
    title: str = "Confusion Matrix",
    **kwargs
) -> MatplotlibAxes:
    """Visualize a classification confusion matrix.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        cm (MatrixLike): Confusion matrix values arranged as actual classes by predicted classes.
        labels (Optional[Labels]): Class, feature, sample, or cluster labels shown on the chart. Defaults to ``None``.
        title (str): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``'Confusion Matrix'``.
        **kwargs (Any): Additional keyword arguments forwarded to the underlying plotting function.
    
    Returns:
        matplotlib.axes.Axes: Configured matplotlib axes containing the rendered static chart.
    
    Raises:
        TypeError: If required inputs are not compatible with the plotting backend.
        ValueError: If input lengths, matrix shapes, or option values are invalid for the requested chart.
    
    Example:
        ```python
        import dataviz as dv
        result = dv.confusion_matrix_plot(cm)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
    """
    fig, ax = setup_plot(title=title)
    
    im = ax.imshow(cm, cmap='Blues', aspect='auto')
    
    n_classes = len(cm)
    if labels is None:
        labels = [f'Class {i}' for i in range(n_classes)]
    
    ax.set_xticks(range(n_classes))
    ax.set_yticks(range(n_classes))
    ax.set_xticklabels(labels)
    ax.set_yticklabels(labels)
    ax.set_xlabel('Predicted')
    ax.set_ylabel('Actual')
    
    # Add text annotations
    for i in range(n_classes):
        for j in range(n_classes):
            ax.text(j, i, str(cm[i, j]), ha='center', va='center', color='white')
    
    plt.colorbar(im, ax=ax)
    
    return ax


def roc_curve(
    fpr: ArrayLike,
    tpr: ArrayLike,
    auc: Optional[float] = None,
    title: str = "ROC Curve",
    **kwargs
) -> MatplotlibAxes:
    """Plot a receiver operating characteristic curve.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        fpr (ArrayLike): False-positive-rate values for the ROC curve.
        tpr (ArrayLike): True-positive-rate values for the ROC curve.
        auc (Optional[float]): Area under the ROC curve to display in the legend. Defaults to ``None``.
        title (str): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``'ROC Curve'``.
        **kwargs (Any): Additional keyword arguments forwarded to the underlying plotting function.
    
    Returns:
        matplotlib.axes.Axes: Configured matplotlib axes containing the rendered static chart.
    
    Raises:
        TypeError: If required inputs are not compatible with the plotting backend.
        ValueError: If input lengths, matrix shapes, or option values are invalid for the requested chart.
    
    Example:
        ```python
        import dataviz as dv
        result = dv.roc_curve(fpr, tpr)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
    """
    fig, ax = setup_plot(title=title, xlabel='False Positive Rate', ylabel='True Positive Rate')
    
    label = 'ROC Curve'
    if auc is not None:
        label += f' (AUC = {auc:.3f})'
    
    ax.plot(fpr, tpr, label=label, **kwargs)
    ax.plot([0, 1], [0, 1], 'k--', label='Random Classifier')
    
    ax.set_xlim([0.0, 1.0])
    ax.set_ylim([0.0, 1.05])
    ax.legend()
    apply_theme(ax)
    
    return ax


def precision_recall_curve(
    precision: ArrayLike,
    recall: ArrayLike,
    ap: Optional[float] = None,
    title: str = "Precision-Recall Curve",
    **kwargs
) -> MatplotlibAxes:
    """Plot a precision-recall curve for classification performance.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        precision (ArrayLike): Precision values for the precision-recall curve.
        recall (ArrayLike): Recall values for the precision-recall curve.
        ap (Optional[float]): Average precision value to display in the legend. Defaults to ``None``.
        title (str): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``'Precision-Recall Curve'``.
        **kwargs (Any): Additional keyword arguments forwarded to the underlying plotting function.
    
    Returns:
        matplotlib.axes.Axes: Configured matplotlib axes containing the rendered static chart.
    
    Raises:
        TypeError: If required inputs are not compatible with the plotting backend.
        ValueError: If input lengths, matrix shapes, or option values are invalid for the requested chart.
    
    Example:
        ```python
        import dataviz as dv
        result = dv.precision_recall_curve(precision, recall)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
    """
    fig, ax = setup_plot(title=title, xlabel='Recall', ylabel='Precision')
    
    label = 'Precision-Recall'
    if ap is not None:
        label += f' (AP = {ap:.3f})'
    
    ax.plot(recall, precision, label=label, **kwargs)
    
    ax.set_xlim([0.0, 1.0])
    ax.set_ylim([0.0, 1.05])
    ax.legend()
    apply_theme(ax)
    
    return ax
