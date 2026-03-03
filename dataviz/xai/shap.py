"""SHAP plot implementation - static and interactive versions."""

from typing import Optional, List
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from ..utils import setup_plot, apply_theme


def shap_plot_static(
    shap_values: np.ndarray,
    feature_names: List[str],
    title: Optional[str] = None,
    sort_order: str = 'descending',
    xlabel: str = "Mean |SHAP value|",
    ylabel: str = "Features",
    figsize: tuple = (10, 8),
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
    color_positive: str = 'steelblue',
    color_negative: str = 'coral',
    theme: str = 'default',
    style: str = 'default',
    grid: bool = True,
    grid_alpha: float = 0.3,
    **kwargs
) -> plt.Axes:
    """
    Create a static SHAP feature importance plot using matplotlib.

    Parameters
    ----------
    shap_values : array
        SHAP values array
    feature_names : list
        Names of features
    title : str, optional
        Chart title (auto-generated if None)
    sort_order : str, default 'descending'
        Sort order ('ascending' or 'descending')
    xlabel : str, default "Mean |SHAP value|"
        X-axis label
    ylabel : str, default "Features"
        Y-axis label
    figsize : tuple, default (10, 8)
        Figure size (width, height)
    dpi : int, default 100
        Figure DPI
    color : str, default 'steelblue'
        Bar color
    alpha : float, default 0.8
        Bar transparency
    edgecolor : str, default 'black'
        Bar edge color
    linewidth : float, default 1.0
        Bar edge width
    font_size : int, default 10
        Base font size
    title_size : int, default 14
        Title font size
    label_size : int, default 11
        Axis label font size
    show_values : bool, default True
        Show values on bars
    value_format : str, default '.3f'
        Format string for values
    color_positive : str, default 'steelblue'
        Color for positive SHAP values
    color_negative : str, default 'coral'
        Color for negative SHAP values
    theme : str, default 'default'
        Plot theme
    style : str, default 'default'
        Matplotlib style
    grid : bool, default True
        Show grid
    grid_alpha : float, default 0.3
        Grid transparency
    **kwargs
        Additional plot arguments

    Returns
    -------
    matplotlib.axes.Axes
        The plot axes
    """
    if title is None:
        title = "SHAP Feature Importance"
    
    # Calculate mean SHAP values (with sign preserved for directionality)
    mean_shap = shap_values.mean(axis=0)
    shap_importance = pd.Series(mean_shap, index=feature_names).sort_values(
        ascending=(sort_order == 'ascending')
    )
    
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, figsize=figsize)
        fig.set_dpi(dpi)
        
        # Determine colors based on sign
        colors = [color_positive if v >= 0 else color_negative for v in shap_importance.values]
        
        bars = ax.barh(
            shap_importance.index,
            shap_importance.values,
            color=colors,
            alpha=alpha,
            edgecolor=edgecolor,
            linewidth=linewidth,
            **kwargs
        )
        
        # Show values on bars
        if show_values:
            for i, (feature, value) in enumerate(shap_importance.items()):
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
            ax.grid(True, axis='x', alpha=grid_alpha)
        
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


def shap_plot_interactive(
    shap_values: np.ndarray,
    feature_names: List[str],
    title: Optional[str] = None,
    sort_order: str = 'descending',
    xlabel: str = "Mean SHAP value",
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
    color_positive: str = 'steelblue',
    color_negative: str = 'coral',
    hovermode: str = 'closest',
    template: str = 'plotly',
    **kwargs
) -> go.Figure:
    """
    Create an interactive SHAP feature importance plot using plotly.

    Parameters
    ----------
    shap_values : array
        SHAP values array
    feature_names : list
        Names of features
    title : str, optional
        Chart title (auto-generated if None)
    sort_order : str, default 'descending'
        Sort order ('ascending' or 'descending')
    xlabel : str, default "Mean SHAP value"
        X-axis label
    ylabel : str, default "Features"
        Y-axis label
    height : int, default 600
        Figure height
    width : int, default 900
        Figure width
    color : str, default 'steelblue'
        Default bar color
    marker_color : str, optional
        Override bar color
    font_size : int, default 12
        Base font size
    title_size : int, default 16
        Title font size
    label_size : int, default 12
        Axis label font size
    show_values : bool, default True
        Show values on bars
    value_format : str, default '.3f'
        Format string for values
    color_positive : str, default 'steelblue'
        Color for positive SHAP values
    color_negative : str, default 'coral'
        Color for negative SHAP values
    hovermode : str, default 'closest'
        Hover mode
    template : str, default 'plotly'
        Plotly template
    **kwargs
        Additional plot arguments

    Returns
    -------
    plotly.graph_objects.Figure
        The interactive figure
    """
    if title is None:
        title = "SHAP Feature Importance"
    
    # Calculate mean SHAP values (with sign preserved)
    mean_shap = shap_values.mean(axis=0)
    shap_importance = pd.Series(mean_shap, index=feature_names).sort_values(
        ascending=(sort_order == 'ascending')
    )
    
    # Determine colors based on sign
    bar_colors = [color_positive if v >= 0 else color_negative for v in shap_importance.values]
    
    # Prepare text for display
    text = None
    if show_values:
        text = [f'{v:{value_format}}' for v in shap_importance.values]
    
    fig = go.Figure(data=[
        go.Bar(
            x=shap_importance.values,
            y=shap_importance.index,
            orientation='h',
            marker=dict(color=bar_colors),
            text=text,
            textposition='auto' if show_values else None,
            hovertemplate='<b>%{y}</b><br>SHAP value: %{x:.4f}<extra></extra>',
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
shap_plot = shap_plot_static
