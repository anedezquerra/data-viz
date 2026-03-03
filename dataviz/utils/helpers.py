"""Helper functions and utilities for plotting."""

from typing import Optional, Tuple
import matplotlib.pyplot as plt
import matplotlib.axes as mpl_axes


def setup_plot(
    figsize: Tuple[int, int] = (10, 6),
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
) -> Tuple[plt.Figure, mpl_axes.Axes]:
    """
    Set up a basic plot with standard configuration.

    Parameters
    ----------
    figsize : tuple, default (10, 6)
        Figure size in inches (width, height)
    title : str, optional
        Plot title
    xlabel : str, optional
        X-axis label
    ylabel : str, optional
        Y-axis label

    Returns
    -------
    fig : matplotlib.figure.Figure
        The figure object
    ax : matplotlib.axes.Axes
        The axes object
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    if title:
        ax.set_title(title, fontsize=14, fontweight='bold')
    if xlabel:
        ax.set_xlabel(xlabel)
    if ylabel:
        ax.set_ylabel(ylabel)
    
    return fig, ax


def apply_theme(ax: mpl_axes.Axes, theme: str = "default") -> None:
    """
    Apply a theme to the plot.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The axes object to apply theme to
    theme : str, default 'default'
        Theme name: 'default', 'dark', 'minimal'
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
