"""Feature importance implementation - static and interactive versions."""

from typing import Optional, List
from ..types import FigureSize, MatplotlibAxes, PlotlyFigure, SeriesLike
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from ..utils import setup_plot, apply_theme


def feature_importance_static(
    importances: SeriesLike,
    title: Optional[str] = None,
    top_n: Optional[int] = None,
    sort_order: str = 'descending',
    xlabel: str = "Importance",
    ylabel: str = "Features",
    figsize: FigureSize = (10, 8),
    dpi: int = 100,
    color: str = 'steelblue',
    alpha: float = 0.8,
    edgecolor: str = 'black',
    linewidth: float = 1.0,
    font_size: int = 10,
    title_size: int = 14,
    label_size: int = 11,
    show_values: bool = True,
    value_format: str = '.3f',
    theme: str = 'default',
    style: str = 'default',
    grid: bool = True,
    grid_alpha: float = 0.3,
    grid_axis: str = 'x',
    **kwargs
) -> MatplotlibAxes:
    """Create a static feature-importance visualization.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        importances (SeriesLike): Feature-importance values indexed or paired with feature names.
        title (Optional[str]): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``None``.
        top_n (Optional[int]): Maximum number of highest-ranked features to display. Defaults to ``None``.
        sort_order (str): Configuration value for ``sort_order``. Defaults to ``'descending'``.
        xlabel (str): Optional x-axis label. Defaults to ``'Importance'``.
        ylabel (str): Optional y-axis label. Defaults to ``'Features'``.
        figsize (FigureSize): Matplotlib figure size as ``(width, height)`` in inches. Defaults to ``(10, 8)``.
        dpi (int): Configuration value for ``dpi``. Defaults to ``100``.
        color (str): Configuration value for ``color``. Defaults to ``'steelblue'``.
        alpha (float): Configuration value for ``alpha``. Defaults to ``0.8``.
        edgecolor (str): Configuration value for ``edgecolor``. Defaults to ``'black'``.
        linewidth (float): Configuration value for ``linewidth``. Defaults to ``1.0``.
        font_size (int): Configuration value for ``font_size``. Defaults to ``10``.
        title_size (int): Configuration value for ``title_size``. Defaults to ``14``.
        label_size (int): Configuration value for ``label_size``. Defaults to ``11``.
        show_values (bool): Configuration value for ``show_values``. Defaults to ``True``.
        value_format (str): Configuration value for ``value_format``. Defaults to ``'.3f'``.
        theme (str): Named styling theme applied after the base plot is created. Defaults to ``'default'``.
        style (str): Matplotlib style context used while building the figure. Defaults to ``'default'``.
        grid (bool): Configuration value for ``grid``. Defaults to ``True``.
        grid_alpha (float): Configuration value for ``grid_alpha``. Defaults to ``0.3``.
        grid_axis (str): Configuration value for ``grid_axis``. Defaults to ``'x'``.
        **kwargs (Any): Additional keyword arguments forwarded to the underlying plotting function.
    
    Returns:
        matplotlib.axes.Axes: Configured matplotlib axes containing the rendered static chart.
    
    Raises:
        TypeError: If required inputs are not compatible with the plotting backend.
        ValueError: If input lengths, matrix shapes, or option values are invalid for the requested chart.
    
    Example:
        ```python
        import dataviz as dv
        result = dv.feature_importance_static(importances)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
    """
    if title is None:
        title = "Feature Importance"
    
    if top_n is not None:
        importances = importances.nlargest(top_n)
    
    # Sort by specified order
    importances_sorted = importances.sort_values(
        ascending=(sort_order == 'ascending')
    )
    
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, figsize=figsize)
        fig.set_dpi(dpi)
        
        bars = ax.barh(
            importances_sorted.index,
            importances_sorted.values,
            color=color,
            alpha=alpha,
            edgecolor=edgecolor,
            linewidth=linewidth,
            **kwargs
        )
        
        # Show values on bars
        if show_values:
            for i, (feature, value) in enumerate(importances_sorted.items()):
                ax.text(
                    value,
                    i,
                    f' {value:{value_format}}',
                    va='center',
                    fontsize=font_size
                )
        
        # Apply labels
        ax.set_xlabel(xlabel, fontsize=label_size)
        ax.set_ylabel(ylabel, fontsize=label_size)
        ax.title.set_fontsize(title_size)
        ax.tick_params(labelsize=font_size)
        
        # Apply grid
        if grid:
            ax.grid(True, axis=grid_axis, alpha=grid_alpha)
        
        # Apply theme
        if theme == 'dark':
            ax.set_facecolor('#2b2b2b')
            fig.patch.set_facecolor('#1e1e1e')
        elif theme == 'minimal':
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.spines['left'].set_visible(False)
        
        apply_theme(ax, theme)
    
    return ax


def feature_importance_interactive(
    importances: SeriesLike,
    title: Optional[str] = None,
    top_n: Optional[int] = None,
    sort_order: str = 'descending',
    xlabel: str = "Importance",
    ylabel: str = "Features",
    height: int = 600,
    width: int = 900,
    color: str = 'steelblue',
    marker_color: Optional[str] = None,
    font_size: int = 12,
    title_size: int = 16,
    label_size: int = 12,
    show_values: bool = True,
    value_format: str = '.3f',
    hovermode: str = 'closest',
    template: str = 'plotly',
    **kwargs
) -> PlotlyFigure:
    """Create an interactive feature-importance visualization.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        importances (SeriesLike): Feature-importance values indexed or paired with feature names.
        title (Optional[str]): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``None``.
        top_n (Optional[int]): Maximum number of highest-ranked features to display. Defaults to ``None``.
        sort_order (str): Configuration value for ``sort_order``. Defaults to ``'descending'``.
        xlabel (str): Optional x-axis label. Defaults to ``'Importance'``.
        ylabel (str): Optional y-axis label. Defaults to ``'Features'``.
        height (int): Plotly figure height in pixels. Defaults to ``600``.
        width (int): Plotly figure width in pixels. Defaults to ``900``.
        color (str): Configuration value for ``color``. Defaults to ``'steelblue'``.
        marker_color (Optional[str]): Configuration value for ``marker_color``. Defaults to ``None``.
        font_size (int): Configuration value for ``font_size``. Defaults to ``12``.
        title_size (int): Configuration value for ``title_size``. Defaults to ``16``.
        label_size (int): Configuration value for ``label_size``. Defaults to ``12``.
        show_values (bool): Configuration value for ``show_values``. Defaults to ``True``.
        value_format (str): Configuration value for ``value_format``. Defaults to ``'.3f'``.
        hovermode (str): Configuration value for ``hovermode``. Defaults to ``'closest'``.
        template (str): Plotly template used to style the interactive figure. Defaults to ``'plotly'``.
        **kwargs (Any): Additional keyword arguments forwarded to the underlying plotting function.
    
    Returns:
        plotly.graph_objects.Figure: Configured Plotly figure containing the rendered interactive chart.
    
    Raises:
        TypeError: If required inputs are not compatible with the plotting backend.
        ValueError: If input lengths, matrix shapes, or option values are invalid for the requested chart.
    
    Example:
        ```python
        import dataviz as dv
        result = dv.feature_importance_interactive(importances)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
    """
    if title is None:
        title = "Feature Importance"
    
    if top_n is not None:
        importances = importances.nlargest(top_n)
    
    # Sort by specified order
    importances_sorted = importances.sort_values(
        ascending=(sort_order == 'ascending')
    )
    
    bar_color = marker_color if marker_color is not None else color
    
    # Prepare text for display
    text = None
    if show_values:
        text = [f'{v:{value_format}}' for v in importances_sorted.values]
    
    fig = go.Figure(data=[
        go.Bar(
            x=importances_sorted.values,
            y=importances_sorted.index,
            orientation='h',
            marker=dict(color=bar_color),
            text=text,
            textposition='auto' if show_values else None,
            hovertemplate='<b>%{y}</b><br>Importance: %{x:.4f}<extra></extra>',
            **kwargs
        )
    ])
    
    fig.update_layout(
        title=dict(text=title, font=dict(size=title_size)),
        xaxis_title=xlabel,
        yaxis_title=ylabel,
        xaxis=dict(
            title_font=dict(size=label_size),
            tickfont=dict(size=font_size)
        ),
        yaxis=dict(
            title_font=dict(size=label_size),
            tickfont=dict(size=font_size)
        ),
        height=height,
        width=width,
        hovermode=hovermode,
        template=template,
        font=dict(size=font_size)
    )
    
    return fig


# Default alias
feature_importance = feature_importance_static
