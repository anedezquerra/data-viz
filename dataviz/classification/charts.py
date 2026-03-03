"""Classification analysis visualization charts."""

from typing import Optional
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ..utils import setup_plot, apply_theme


def confusion_matrix_plot(
    cm: np.ndarray,
    labels: Optional[list] = None,
    title: str = "Confusion Matrix",
    **kwargs
) -> plt.Axes:
    """
    Visualize a confusion matrix.

    Parameters
    ----------
    cm : array
        Confusion matrix
    labels : list, optional
        Class labels
    title : str, default "Confusion Matrix"
        Chart title
    **kwargs
        Additional plot arguments

    Returns
    -------
    matplotlib.axes.Axes
        The plot axes
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
    fpr: np.ndarray,
    tpr: np.ndarray,
    auc: Optional[float] = None,
    title: str = "ROC Curve",
    **kwargs
) -> plt.Axes:
    """
    Plot ROC (Receiver Operating Characteristic) curve.

    Parameters
    ----------
    fpr : array
        False positive rates
    tpr : array
        True positive rates
    auc : float, optional
        Area under curve value
    title : str, default "ROC Curve"
        Chart title
    **kwargs
        Additional plot arguments

    Returns
    -------
    matplotlib.axes.Axes
        The plot axes
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
    precision: np.ndarray,
    recall: np.ndarray,
    ap: Optional[float] = None,
    title: str = "Precision-Recall Curve",
    **kwargs
) -> plt.Axes:
    """
    Plot Precision-Recall curve.

    Parameters
    ----------
    precision : array
        Precision values
    recall : array
        Recall values
    ap : float, optional
        Average precision value
    title : str, default "Precision-Recall Curve"
        Chart title
    **kwargs
        Additional plot arguments

    Returns
    -------
    matplotlib.axes.Axes
        The plot axes
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
