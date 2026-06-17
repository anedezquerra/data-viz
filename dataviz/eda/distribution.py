"""Distribution summary implementation - static and interactive versions."""

from typing import Optional, Tuple
from ..types import FigureSize, MatplotlibFigure, PlotlyFigure
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.subplots as sp
import plotly.graph_objects as go
import plotly.express as px


def distribution_summary_static(
    df: pd.DataFrame,
    title: Optional[str] = None,
    figsize: Optional[FigureSize] = None,
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
) -> MatplotlibFigure:
    """Create static summary charts for dataframe column distributions.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        df (pd.DataFrame): Input dataframe containing the variables to visualize.
        title (Optional[str]): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``None``.
        figsize (Optional[FigureSize]): Matplotlib figure size as ``(width, height)`` in inches. Defaults to ``None``.
        bins (int): Number of bins used for histogram-like displays. Defaults to ``30``.
        color (Optional[str]): Configuration value for ``color``. Defaults to ``None``.
        alpha (float): Configuration value for ``alpha``. Defaults to ``0.7``.
        edgecolor (str): Configuration value for ``edgecolor``. Defaults to ``'black'``.
        grid (bool): Configuration value for ``grid``. Defaults to ``True``.
        grid_alpha (float): Configuration value for ``grid_alpha``. Defaults to ``0.3``.
        theme (str): Named styling theme applied after the base plot is created. Defaults to ``'default'``.
        font_size (int): Configuration value for ``font_size``. Defaults to ``10``.
        title_size (int): Configuration value for ``title_size``. Defaults to ``14``.
        label_size (int): Configuration value for ``label_size``. Defaults to ``11``.
        dpi (int): Configuration value for ``dpi``. Defaults to ``100``.
        style (str): Matplotlib style context used while building the figure. Defaults to ``'default'``.
        **kwargs (Any): Additional keyword arguments forwarded to the underlying plotting function.
    
    Returns:
        matplotlib.figure.Figure: Configured matplotlib figure containing the rendered static chart.
    
    Raises:
        TypeError: If required inputs are not compatible with the plotting backend.
        ValueError: If input lengths, matrix shapes, or option values are invalid for the requested chart.
    
    Example:
        ```python
        import dataviz as dv
        result = dv.distribution_summary_static(df)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
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
) -> PlotlyFigure:
    """Create interactive summary charts for dataframe column distributions.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        df (pd.DataFrame): Input dataframe containing the variables to visualize.
        title (Optional[str]): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``None``.
        bins (int): Number of bins used for histogram-like displays. Defaults to ``30``.
        color (Optional[str]): Configuration value for ``color``. Defaults to ``None``.
        marker_color (Optional[str]): Configuration value for ``marker_color``. Defaults to ``None``.
        hovermode (str): Configuration value for ``hovermode``. Defaults to ``'closest'``.
        template (str): Plotly template used to style the interactive figure. Defaults to ``'plotly'``.
        font_size (int): Configuration value for ``font_size``. Defaults to ``12``.
        title_size (int): Configuration value for ``title_size``. Defaults to ``16``.
        height (Optional[int]): Plotly figure height in pixels. Defaults to ``None``.
        width (int): Plotly figure width in pixels. Defaults to ``1200``.
        **kwargs (Any): Additional keyword arguments forwarded to the underlying plotting function.
    
    Returns:
        plotly.graph_objects.Figure: Configured Plotly figure containing the rendered interactive chart.
    
    Raises:
        TypeError: If required inputs are not compatible with the plotting backend.
        ValueError: If input lengths, matrix shapes, or option values are invalid for the requested chart.
    
    Example:
        ```python
        import dataviz as dv
        result = dv.distribution_summary_interactive(df)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
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
