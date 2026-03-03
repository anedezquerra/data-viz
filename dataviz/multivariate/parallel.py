"""Parallel coordinates implementation - static and interactive versions."""

from typing import Optional, Tuple
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from ..utils import setup_plot, apply_theme


def parallel_coordinates_static(
    df: pd.DataFrame,
    title: Optional[str] = None,
    figsize: Tuple[int, int] = (12, 6),
    alpha: float = 0.3,
    linewidth: float = 1.0,
    color: Optional[str] = None,
    style: str = 'default',
    font_size: int = 10,
    title_size: int = 14,
    label_size: int = 11,
    dpi: int = 100,
    **kwargs
) -> plt.Axes:
    """
    Create a static parallel coordinates plot using matplotlib.

    Parameters
    ----------
    df : DataFrame
        Input data (numeric columns only)
    title : str, optional
        Chart title
    figsize : tuple, default (12, 6)
        Figure size (width, height)
    alpha : float, default 0.3
        Line transparency
    linewidth : float, default 1.0
        Line width
    color : str, optional
        Line color
    style : str, default 'default'
        Matplotlib style
    font_size : int, default 10
        Base font size
    title_size : int, default 14
        Title font size
    label_size : int, default 11
        Axis label font size
    dpi : int, default 100
        Figure DPI
    **kwargs
        Additional plot arguments

    Returns
    -------
    matplotlib.axes.Axes
        The plot axes
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
) -> go.Figure:
    """
    Create an interactive parallel coordinates plot using plotly.

    Parameters
    ----------
    df : DataFrame
        Input data
    title : str, optional
        Chart title
    color_col : str, optional
        Column to use for color encoding
    colorscale : str, default 'Viridis'
        Plotly colorscale
    showlegend : bool, default True
        Show legend
    hovermode : str, default 'closest'
        Hover mode type
    template : str, default 'plotly'
        Plotly template
    font_size : int, default 12
        Font size
    title_size : int, default 16
        Title font size
    height : int, default 600
        Figure height in pixels
    width : int, default 1000
        Figure width in pixels
    **kwargs
        Additional plot arguments

    Returns
    -------
    plotly.graph_objects.Figure
        The interactive figure
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
