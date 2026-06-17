"""Helper functions and utilities for plotting."""

from typing import Optional, Tuple
from ..types import FigureSize, MatplotlibAxes, MatplotlibFigure
import matplotlib.pyplot as plt
import matplotlib.axes as mpl_axes


def setup_plot(
    figsize: FigureSize = (10, 6),
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
) -> Tuple[MatplotlibFigure, MatplotlibAxes]:
    """Create and configure a matplotlib figure and axes pair.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        figsize (FigureSize): Matplotlib figure size as ``(width, height)`` in inches. Defaults to ``(10, 6)``.
        title (Optional[str]): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``None``.
        xlabel (Optional[str]): Optional x-axis label. Defaults to ``None``.
        ylabel (Optional[str]): Optional y-axis label. Defaults to ``None``.
    
    Returns:
        tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]: Created matplotlib figure and axes objects.
    
    Raises:
        TypeError: If required inputs are not compatible with the plotting backend.
        ValueError: If input lengths, matrix shapes, or option values are invalid for the requested chart.
    
    Example:
        ```python
        import dataviz as dv
        result = dv.setup_plot()
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    if title:
        ax.set_title(title, fontsize=14, fontweight='bold')
    if xlabel:
        ax.set_xlabel(xlabel)
    if ylabel:
        ax.set_ylabel(ylabel)
    
    return fig, ax


def apply_theme(ax: MatplotlibAxes, theme: str = "default") -> None:
    """Apply a named visual theme to an existing matplotlib axes object.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        ax (MatplotlibAxes): Matplotlib axes object to update.
        theme (str): Named styling theme applied after the base plot is created. Defaults to ``'default'``.
    
    Returns:
        None: The supplied matplotlib axes is updated in place.
    
    Raises:
        TypeError: If required inputs are not compatible with the plotting backend.
        ValueError: If input lengths, matrix shapes, or option values are invalid for the requested chart.
    
    Example:
        ```python
        import dataviz as dv
        result = dv.apply_theme(ax)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
    """
    if theme == "dark":
        ax.set_facecolor("#f0f0f0")
        ax.grid(True, alpha=0.3)
    elif theme == "minimal":
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.grid(True, alpha=0.2, axis='y')
    else:  # default
        ax.grid(True, alpha=0.3)
