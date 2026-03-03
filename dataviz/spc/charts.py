"""Statistical Process Control charts implementation."""

from typing import Optional
import numpy as np
import matplotlib.pyplot as plt
from ..utils import setup_plot, apply_theme


def control_chart(
    data: np.ndarray,
    title: str = "Control Chart",
    **kwargs
) -> plt.Axes:
    """
    Create a control chart for monitoring process stability.

    Parameters
    ----------
    data : array-like
        Process measurements
    title : str, default "Control Chart"
        Chart title
    **kwargs
        Additional plotting arguments

    Returns
    -------
    matplotlib.axes.Axes
        The plot axes
    """
    fig, ax = setup_plot(title=title)
    
    mean = np.mean(data)
    std = np.std(data)
    ucl = mean + 3 * std  # Upper Control Limit
    lcl = mean - 3 * std  # Lower Control Limit
    
    ax.plot(data, marker='o', label='Process Data', **kwargs)
    ax.axhline(mean, color='green', linestyle='-', label='Mean', linewidth=2)
    ax.axhline(ucl, color='red', linestyle='--', label='UCL (±3σ)', linewidth=1)
    ax.axhline(lcl, color='red', linestyle='--', linewidth=1)
    
    ax.set_ylabel('Value')
    ax.set_xlabel('Sample')
    ax.legend()
    apply_theme(ax)
    
    return ax


def x_range_chart(
    data: np.ndarray,
    subgroup_size: int = 5,
    title: str = "X-Range Chart",
    **kwargs
) -> plt.Axes:
    """
    Create an X-Range (individuals and moving range) chart.

    Parameters
    ----------
    data : array-like
        Process measurements
    subgroup_size : int, default 5
        Size of subgroups for moving range calculation
    title : str, default "X-Range Chart"
        Chart title
    **kwargs
        Additional plotting arguments

    Returns
    -------
    matplotlib.axes.Axes
        The plot axes
    """
    fig, ax = setup_plot(title=title)
    
    ax.plot(data, marker='o', label='Individual Values', **kwargs)
    ax.set_ylabel('Value')
    ax.set_xlabel('Sample')
    ax.legend()
    apply_theme(ax)
    
    return ax
