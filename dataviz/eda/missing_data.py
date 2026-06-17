"""Missing data plot implementation - static and interactive versions."""

from typing import Optional, Tuple
from ..types import FigureSize, MatplotlibAxes, PlotlyFigure
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from ..utils import setup_plot, apply_theme


def missing_data_plot_static(
    df: pd.DataFrame,
    title: Optional[str] = None,
    figsize: FigureSize = (12, 6),
    color: Optional[str] = None,
    edgecolor: str = 'black',
    linewidth: float = 1.0,
    alpha: float = 0.7,
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = 'default',
    font_size: int = 10,
    title_size: int = 14,
    label_size: int = 11,
    dpi: int = 100,
    style: str = 'default',
    **kwargs
) -> MatplotlibAxes:
    """Create a static missing-value summary by dataframe column.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        df (pd.DataFrame): Input dataframe containing the variables to visualize.
        title (Optional[str]): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``None``.
        figsize (FigureSize): Matplotlib figure size as ``(width, height)`` in inches. Defaults to ``(12, 6)``.
        color (Optional[str]): Configuration value for ``color``. Defaults to ``None``.
        edgecolor (str): Configuration value for ``edgecolor``. Defaults to ``'black'``.
        linewidth (float): Configuration value for ``linewidth``. Defaults to ``1.0``.
        alpha (float): Configuration value for ``alpha``. Defaults to ``0.7``.
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
        matplotlib.axes.Axes: Configured matplotlib axes containing the rendered static chart.
    
    Raises:
        TypeError: If required inputs are not compatible with the plotting backend.
        ValueError: If input lengths, matrix shapes, or option values are invalid for the requested chart.
    
    Example:
        ```python
        import dataviz as dv
        result = dv.missing_data_plot_static(df)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
    """
    if title is None:
        title = "Missing Data Analysis"
    
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, figsize=figsize)
        fig.set_dpi(dpi)
        
        missing = df.isnull().sum()
        missing_pct = (missing / len(df)) * 100
        
        if missing.sum() > 0:
            ax.barh(
                missing[missing > 0].index,
                missing_pct[missing > 0],
                color=color,
                edgecolor=edgecolor,
                linewidth=linewidth,
                alpha=alpha,
                **kwargs
            )
            ax.set_xlabel('Percentage Missing (%)', fontsize=label_size)
            if grid:
                ax.grid(True, alpha=grid_alpha, axis='x')
        else:
            ax.text(0.5, 0.5, 'No missing data found', 
                    ha='center', va='center', transform=ax.transAxes,
                    fontsize=font_size)
        
        # Customize fonts
        ax.title.set_fontsize(title_size)
        ax.tick_params(labelsize=font_size)
        
        # Theme
        if theme == 'dark':
            ax.set_facecolor('#f0f0f0')
        elif theme == 'minimal':
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
        
        apply_theme(ax, theme)
    
    return ax


def missing_data_plot_interactive(
    df: pd.DataFrame,
    title: Optional[str] = None,
    color: Optional[str] = None,
    marker_color: Optional[str] = None,
    showlegend: bool = True,
    hovermode: str = 'closest',
    template: str = 'plotly',
    font_size: int = 12,
    title_size: int = 16,
    height: int = 600,
    width: int = 1000,
    **kwargs
) -> PlotlyFigure:
    """Create an interactive missing-value summary by dataframe column.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        df (pd.DataFrame): Input dataframe containing the variables to visualize.
        title (Optional[str]): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``None``.
        color (Optional[str]): Configuration value for ``color``. Defaults to ``None``.
        marker_color (Optional[str]): Configuration value for ``marker_color``. Defaults to ``None``.
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
        result = dv.missing_data_plot_interactive(df)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
    """
    if title is None:
        title = "Missing Data Analysis"
    if color is None:
        color = marker_color
    
    missing = df.isnull().sum()
    missing_pct = (missing / len(df)) * 100
    
    if missing.sum() > 0:
        fig = go.Figure(data=[
            go.Bar(
                y=missing[missing > 0].index,
                x=missing_pct[missing > 0],
                orientation='h',
                marker_color=color,
                **kwargs
            )
        ])
        fig.update_layout(
            title=dict(text=title, font=dict(size=title_size)),
            xaxis_title='Percentage Missing (%)',
            hovermode=hovermode,
            template=template,
            font=dict(size=font_size),
            height=height,
            width=width,
            showlegend=showlegend,
        )
    else:
        fig = go.Figure()
        fig.add_annotation(
            text='No missing data found',
            xref='paper', yref='paper',
            x=0.5, y=0.5, showarrow=False,
            font=dict(size=font_size)
        )
        fig.update_layout(
            title=dict(text=title, font=dict(size=title_size)),
            template=template,
            height=height,
            width=width,
        )
    
    return fig
