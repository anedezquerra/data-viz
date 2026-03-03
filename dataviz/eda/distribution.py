"""Distribution summary implementation - static and interactive versions."""

from typing import Optional, Tuple
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.subplots as sp
import plotly.graph_objects as go
import plotly.express as px


def distribution_summary_static(
    df: pd.DataFrame,
    title: Optional[str] = None,
    figsize: Optional[Tuple[int, int]] = None,
    bins: int = 30,
    color: Optional[str] = None,
    alpha: float = 0.7,
    edgecolor: str = 'black',
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = 'default',
    font_size: int = 10,
    title_size: int = 14,
    label_size: int = 11,
    dpi: int = 100,
    style: str = 'default',
    **kwargs
) -> plt.Figure:
    """
    Create static subplots showing distribution of all numeric columns.

    Parameters
    ----------
    df : DataFrame
        Input data
    title : str, optional
        Figure title
    figsize : tuple, optional
        Figure size (width, height)
    bins : int, default 30
        Number of histogram bins
    color : str, optional
        Bar color
    alpha : float, default 0.7
        Transparency
    edgecolor : str, default 'black'
        Edge color
    grid : bool, default True
        Show grid
    grid_alpha : float, default 0.3
        Grid transparency
    theme : str, default 'default'
        Theme: 'default', 'dark', 'minimal'
    font_size : int, default 10
        Base font size
    title_size : int, default 14
        Title font size
    label_size : int, default 11
        Axis label font size
    dpi : int, default 100
        Figure DPI
    style : str, default 'default'
        Matplotlib style
    **kwargs
        Additional plot arguments

    Returns
    -------
    matplotlib.figure.Figure
        The figure object
    """
    if title is None:
        title = "Distribution Summary"
    
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    n_cols_data = len(numeric_cols)
    
    if n_cols_data == 0:
        fig = plt.figure()
        return fig
    
    n_rows = (n_cols_data + 2) // 3
    n_cols_plot = 3
    if figsize is None:
        figsize = (15, 5 * n_rows)
    
    with plt.style.context(style):
        fig, axes = plt.subplots(n_rows, n_cols_plot, figsize=figsize)
        fig.set_dpi(dpi)
        fig.suptitle(title, fontsize=title_size, fontweight='bold')
        
        axes = axes.flatten() if isinstance(axes, np.ndarray) else [axes]
        
        for idx, col in enumerate(numeric_cols):
            ax = axes[idx]
            ax.hist(df[col], bins=bins, color=color, alpha=alpha, edgecolor=edgecolor, **kwargs)
            ax.set_title(col, fontsize=label_size)
            ax.set_ylabel('Frequency', fontsize=label_size)
            ax.tick_params(labelsize=font_size)
            if grid:
                ax.grid(True, alpha=grid_alpha, axis='y')
            
            if theme == 'minimal':
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)
        
        # Hide unused subplots
        for idx in range(len(numeric_cols), len(axes)):
            axes[idx].set_visible(False)
        
        plt.tight_layout()
    
    return fig


def distribution_summary_interactive(
    df: pd.DataFrame,
    title: Optional[str] = None,
    bins: int = 30,
    color: Optional[str] = None,
    marker_color: Optional[str] = None,
    hovermode: str = 'closest',
    template: str = 'plotly',
    font_size: int = 12,
    title_size: int = 16,
    height: Optional[int] = None,
    width: int = 1200,
    **kwargs
) -> go.Figure:
    """
    Create interactive subplots showing distribution of numeric columns.

    Parameters
    ----------
    df : DataFrame
        Input data
    title : str, optional
        Figure title
    bins : int, default 30
        Number of histogram bins
    color : str, optional
        Bar color
    marker_color : str, optional
        Alternative marker color parameter
    hovermode : str, default 'closest'
        Hover mode type
    template : str, default 'plotly'
        Plotly template
    font_size : int, default 12
        Font size
    title_size : int, default 16
        Title font size
    height : int, optional
        Figure height in pixels
    width : int, default 1200
        Figure width in pixels
    **kwargs
        Additional plot arguments

    Returns
    -------
    plotly.graph_objects.Figure
        The interactive figure
    """
    if title is None:
        title = "Distribution Summary"
    if color is None:
        color = marker_color
    
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    
    if len(numeric_cols) == 0:
        return go.Figure()
    
    n_rows = (len(numeric_cols) + 2) // 3
    n_cols = 3
    if height is None:
        height = 300 * n_rows
    
    fig = sp.make_subplots(rows=n_rows, cols=n_cols, subplot_titles=tuple(numeric_cols))
    
    for idx, col in enumerate(numeric_cols):
        row = idx // 3 + 1
        col_pos = idx % 3 + 1
        
        fig.add_trace(
            go.Histogram(x=df[col], name=col, marker_color=color, nbinsx=bins, **kwargs),
            row=row, col=col_pos
        )
    
    fig.update_layout(
        title=dict(text=title, font=dict(size=title_size)),
        hovermode=hovermode,
        template=template,
        font=dict(size=font_size),
        height=height,
        width=width,
        showlegend=False
    )
    
    return fig
