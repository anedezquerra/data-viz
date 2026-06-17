"""Pairplot implementation - static and interactive versions."""

from typing import Optional, Tuple
from ..types import FigureSize, MatplotlibFigure, PlotlyFigure
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px


def pairplot_static(
    df: pd.DataFrame,
    title: Optional[str] = None,
    figsize: FigureSize = (12, 12),
    diag_kind: str = 'hist',
    plot_kind: str = 'scatter',
    color: Optional[str] = None,
    alpha: float = 0.5,
    bins: int = 20,
    dpi: int = 100,
    style: str = 'default',
    font_size: int = 10,
    title_size: int = 14,
    label_size: int = 11,
    marker_size: int = 50,
    **kwargs
) -> MatplotlibFigure:
    """Create a static pairwise variable relationship plot.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        df (pd.DataFrame): Input dataframe containing the variables to visualize.
        title (Optional[str]): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``None``.
        figsize (FigureSize): Matplotlib figure size as ``(width, height)`` in inches. Defaults to ``(12, 12)``.
        diag_kind (str): Configuration value for ``diag_kind``. Defaults to ``'hist'``.
        plot_kind (str): Configuration value for ``plot_kind``. Defaults to ``'scatter'``.
        color (Optional[str]): Configuration value for ``color``. Defaults to ``None``.
        alpha (float): Configuration value for ``alpha``. Defaults to ``0.5``.
        bins (int): Number of bins used for histogram-like displays. Defaults to ``20``.
        dpi (int): Configuration value for ``dpi``. Defaults to ``100``.
        style (str): Matplotlib style context used while building the figure. Defaults to ``'default'``.
        font_size (int): Configuration value for ``font_size``. Defaults to ``10``.
        title_size (int): Configuration value for ``title_size``. Defaults to ``14``.
        label_size (int): Configuration value for ``label_size``. Defaults to ``11``.
        marker_size (int): Configuration value for ``marker_size``. Defaults to ``50``.
        **kwargs (Any): Additional keyword arguments forwarded to the underlying plotting function.
    
    Returns:
        matplotlib.figure.Figure: Configured matplotlib figure containing the rendered static chart.
    
    Raises:
        TypeError: If required inputs are not compatible with the plotting backend.
        ValueError: If input lengths, matrix shapes, or option values are invalid for the requested chart.
    
    Example:
        ```python
        import dataviz as dv
        result = dv.pairplot_static(df)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
    """
    if title is None:
        title = "Pairplot"
    
    with plt.style.context(style):
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        n_cols = len(numeric_cols)
        
        if n_cols == 0:
            fig = plt.figure()
            return fig
        
        fig, axes = plt.subplots(n_cols, n_cols, figsize=figsize)
        fig.set_dpi(dpi)
        fig.suptitle(title, fontsize=title_size, fontweight='bold')
        
        if n_cols == 1:
            axes = np.array([[axes]])
        elif n_cols > 1:
            axes = axes if len(axes.shape) == 2 else axes.reshape(1, -1)
        
        for i, col_y in enumerate(numeric_cols):
            for j, col_x in enumerate(numeric_cols):
                ax = axes[i, j] if n_cols > 1 else axes[0, 0]
                if i == j:
                    # Diagonal: histogram or KDE
                    if diag_kind == 'hist':
                        ax.hist(df[col_x], bins=bins, color=color, alpha=alpha, edgecolor='black')
                    else:
                        df[col_x].plot.kde(ax=ax, color=color)
                else:
                    # Off-diagonal: scatter or histogram
                    if plot_kind == 'scatter':
                        ax.scatter(df[col_x], df[col_y], alpha=alpha, s=marker_size, color=color, **kwargs)
                    else:
                        ax.hist2d(df[col_x], df[col_y], bins=15, cmap='viridis')
                
                if j == 0:
                    ax.set_ylabel(col_y, fontsize=label_size)
                else:
                    ax.set_ylabel('')
                
                if i == n_cols - 1:
                    ax.set_xlabel(col_x, fontsize=label_size)
                else:
                    ax.set_xlabel('')
                
                ax.tick_params(labelsize=font_size)
        
        plt.tight_layout()
    
    return fig


def pairplot_interactive(
    df: pd.DataFrame,
    title: Optional[str] = None,
    color: Optional[str] = None,
    marker_size: int = 5,
    diagonal_type: str = 'histogram',
    hovermode: str = 'closest',
    template: str = 'plotly',
    font_size: int = 12,
    title_size: int = 16,
    height: int = 1000,
    width: int = 1000,
    **kwargs
) -> PlotlyFigure:
    """Create an interactive pairwise variable relationship plot.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        df (pd.DataFrame): Input dataframe containing the variables to visualize.
        title (Optional[str]): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``None``.
        color (Optional[str]): Configuration value for ``color``. Defaults to ``None``.
        marker_size (int): Configuration value for ``marker_size``. Defaults to ``5``.
        diagonal_type (str): Configuration value for ``diagonal_type``. Defaults to ``'histogram'``.
        hovermode (str): Configuration value for ``hovermode``. Defaults to ``'closest'``.
        template (str): Plotly template used to style the interactive figure. Defaults to ``'plotly'``.
        font_size (int): Configuration value for ``font_size``. Defaults to ``12``.
        title_size (int): Configuration value for ``title_size``. Defaults to ``16``.
        height (int): Plotly figure height in pixels. Defaults to ``1000``.
        width (int): Plotly figure width in pixels. Defaults to ``1000``.
        **kwargs (Any): Additional keyword arguments forwarded to the underlying plotting function.
    
    Returns:
        plotly.graph_objects.Figure: Configured Plotly figure containing the rendered interactive chart.
    
    Raises:
        TypeError: If required inputs are not compatible with the plotting backend.
        ValueError: If input lengths, matrix shapes, or option values are invalid for the requested chart.
    
    Example:
        ```python
        import dataviz as dv
        result = dv.pairplot_interactive(df)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
    """
    if title is None:
        title = "Pairplot"
    
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    
    if len(numeric_cols) == 0:
        return go.Figure()
    
    fig = px.scatter_matrix(
        df[numeric_cols],
        color_continuous_scale='Viridis' if not color else None,
        hover_data=numeric_cols,
        **kwargs
    )
    
    fig.update_traces(marker=dict(size=marker_size, color=color))
    
    fig.update_layout(
        title=dict(text=title, font=dict(size=title_size)),
        hovermode=hovermode,
        template=template,
        font=dict(size=font_size),
        height=height,
        width=width,
    )
    
    return fig
