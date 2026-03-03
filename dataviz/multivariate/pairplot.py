"""Pairplot implementation - static and interactive versions."""

from typing import Optional, Tuple
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px


def pairplot_static(
    df: pd.DataFrame,
    title: Optional[str] = None,
    figsize: Tuple[int, int] = (12, 12),
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
) -> plt.Figure:
    """
    Create a static pairwise relationships plot using matplotlib.

    Parameters
    ----------
    df : DataFrame
        Input data
    title : str, optional
        Figure title
    figsize : tuple, default (12, 12)
        Figure size (width, height)
    diag_kind : str, default 'hist'
        Diagonal plot type: 'hist', 'kde'
    plot_kind : str, default 'scatter'
        Off-diagonal plot type: 'scatter', 'hist'
    color : str, optional
        Plot color
    alpha : float, default 0.5
        Transparency
    bins : int, default 20
        Number of bins for histograms
    dpi : int, default 100
        Figure DPI
    style : str, default 'default'
        Matplotlib style
    font_size : int, default 10
        Base font size
    title_size : int, default 14
        Title font size
    label_size : int, default 11
        Axis label font size
    marker_size : int, default 50
        Marker size for scatter plots
    **kwargs
        Additional arguments

    Returns
    -------
    matplotlib.figure.Figure
        The figure object
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
) -> go.Figure:
    """
    Create an interactive pairplot using plotly.

    Parameters
    ----------
    df : DataFrame
        Input data
    title : str, optional
        Figure title
    color : str, optional
        Plot color
    marker_size : int, default 5
        Marker size
    diagonal_type : str, default 'histogram'
        Diagonal plot type: 'histogram', 'axis'
    hovermode : str, default 'closest'
        Hover mode type
    template : str, default 'plotly'
        Plotly template
    font_size : int, default 12
        Font size
    title_size : int, default 16
        Title font size
    height : int, default 1000
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
