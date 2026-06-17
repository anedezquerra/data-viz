"""Parallel coordinates implementation - static and interactive versions."""

from typing import Optional, Tuple
from ..types import FigureSize, MatplotlibAxes, PlotlyFigure
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from ..utils import setup_plot, apply_theme


def parallel_coordinates_static(
    df: pd.DataFrame,
    title: Optional[str] = None,
    figsize: FigureSize = (12, 6),
    alpha: float = 0.3,
    linewidth: float = 1.0,
    color: Optional[str] = None,
    style: str = 'default',
    font_size: int = 10,
    title_size: int = 14,
    label_size: int = 11,
    dpi: int = 100,
    **kwargs
) -> MatplotlibAxes:
    """Create a static parallel-coordinates plot for multivariate comparison.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        df (pd.DataFrame): Input dataframe containing the variables to visualize.
        title (Optional[str]): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``None``.
        figsize (FigureSize): Matplotlib figure size as ``(width, height)`` in inches. Defaults to ``(12, 6)``.
        alpha (float): Configuration value for ``alpha``. Defaults to ``0.3``.
        linewidth (float): Configuration value for ``linewidth``. Defaults to ``1.0``.
        color (Optional[str]): Configuration value for ``color``. Defaults to ``None``.
        style (str): Matplotlib style context used while building the figure. Defaults to ``'default'``.
        font_size (int): Configuration value for ``font_size``. Defaults to ``10``.
        title_size (int): Configuration value for ``title_size``. Defaults to ``14``.
        label_size (int): Configuration value for ``label_size``. Defaults to ``11``.
        dpi (int): Configuration value for ``dpi``. Defaults to ``100``.
        **kwargs (Any): Additional keyword arguments forwarded to the underlying plotting function.
    
    Returns:
        matplotlib.axes.Axes: Configured matplotlib axes containing the rendered static chart.
    
    Raises:
        TypeError: If required inputs are not compatible with the plotting backend.
        ValueError: If input lengths, matrix shapes, or option values are invalid for the requested chart.
    
    Example:
        ```python
        import dataviz as dv
        result = dv.parallel_coordinates_static(df)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
    """
    if title is None:
        title = "Parallel Coordinates"
    
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, figsize=figsize)
        fig.set_dpi(dpi)
        
        # Normalize data to 0-1 range for visualization
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        df_norm = (df[numeric_cols] - df[numeric_cols].min()) / (df[numeric_cols].max() - df[numeric_cols].min())
        
        for idx, row in df_norm.iterrows():
            ax.plot(range(len(df_norm.columns)), row.values, alpha=alpha, linewidth=linewidth, color=color, **kwargs)
        
        ax.set_xticks(range(len(df_norm.columns)))
        ax.set_xticklabels(df_norm.columns, rotation=45, ha='right', fontsize=label_size)
        ax.set_ylabel('Normalized Value', fontsize=label_size)
        ax.title.set_fontsize(title_size)
        ax.tick_params(labelsize=font_size)
        ax.grid(True, alpha=0.3)
        
        apply_theme(ax)
    
    return ax


def parallel_coordinates_interactive(
    df: pd.DataFrame,
    title: Optional[str] = None,
    color_col: Optional[str] = None,
    colorscale: str = 'Viridis',
    showlegend: bool = True,
    hovermode: str = 'closest',
    template: str = 'plotly',
    font_size: int = 12,
    title_size: int = 16,
    height: int = 600,
    width: int = 1000,
    **kwargs
) -> PlotlyFigure:
    """Create an interactive parallel-coordinates plot for multivariate comparison.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        df (pd.DataFrame): Input dataframe containing the variables to visualize.
        title (Optional[str]): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``None``.
        color_col (Optional[str]): Configuration value for ``color_col``. Defaults to ``None``.
        colorscale (str): Configuration value for ``colorscale``. Defaults to ``'Viridis'``.
        showlegend (bool): Configuration value for ``showlegend``. Defaults to ``True``.
        hovermode (str): Configuration value for ``hovermode``. Defaults to ``'closest'``.
        template (str): Plotly template used to style the interactive figure. Defaults to ``'plotly'``.
        font_size (int): Configuration value for ``font_size``. Defaults to ``12``.
        title_size (int): Configuration value for ``title_size``. Defaults to ``16``.
        height (int): Plotly figure height in pixels. Defaults to ``600``.
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
        result = dv.parallel_coordinates_interactive(df)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
    """
    if title is None:
        title = "Parallel Coordinates"
    
    if color_col is None:
        # Use first numeric column for coloring
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            color_col = numeric_cols[0]
    
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    dimensions = []
    for col in numeric_cols:
        dimensions.append(dict(label=col, values=df[col]))
    
    if color_col and color_col in df.columns:
        color_val = df[color_col]
    else:
        color_val = None
    
    fig = go.Figure(data=go.Parcoords(
        dimensions=dimensions,
        line=dict(
            color=color_val,
            colorscale=colorscale
        ) if color_val is not None else None,
        **kwargs
    ))
    
    fig.update_layout(
        title=dict(text=title, font=dict(size=title_size)),
        hovermode=hovermode,
        template=template,
        font=dict(size=font_size),
        height=height,
        width=width,
        showlegend=showlegend,
    )
    
    return fig
