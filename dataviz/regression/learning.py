"""Learning curve implementation - static and interactive versions."""

from typing import Optional, Tuple
from ..types import ArrayLike, FigureSize, MatplotlibAxes, PlotlyFigure
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from ..utils import setup_plot, apply_theme


def learning_curve_static(
    train_sizes: ArrayLike,
    train_scores: ArrayLike,
    val_scores: ArrayLike,
    title: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    train_color: Optional[str] = None,
    val_color: Optional[str] = None,
    linewidth: float = 2.0,
    marker_size: int = 6,
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
    """Create a static learning curve across training-set sizes.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        train_sizes (ArrayLike): Training-set sizes used to compute learning-curve scores.
        train_scores (ArrayLike): Training scores corresponding to each training-set size.
        val_scores (ArrayLike): Validation scores corresponding to each training-set size.
        title (Optional[str]): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``None``.
        figsize (FigureSize): Matplotlib figure size as ``(width, height)`` in inches. Defaults to ``(10, 6)``.
        train_color (Optional[str]): Configuration value for ``train_color``. Defaults to ``None``.
        val_color (Optional[str]): Configuration value for ``val_color``. Defaults to ``None``.
        linewidth (float): Configuration value for ``linewidth``. Defaults to ``2.0``.
        marker_size (int): Configuration value for ``marker_size``. Defaults to ``6``.
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
        result = dv.learning_curve_static(train_sizes)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
    """
    if title is None:
        title = "Learning Curve"
    
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel='Training Set Size', ylabel='Score', figsize=figsize)
        fig.set_dpi(dpi)
        
        ax.plot(
            train_sizes, train_scores,
            'o-',
            label='Training Score',
            color=train_color,
            linewidth=linewidth,
            markersize=marker_size,
            alpha=alpha,
            **kwargs
        )
        ax.plot(
            train_sizes, val_scores,
            'o-',
            label='Validation Score',
            color=val_color,
            linewidth=linewidth,
            markersize=marker_size,
            alpha=alpha,
            **kwargs
        )
        
        # Customize fonts
        ax.title.set_fontsize(title_size)
        ax.xaxis.label.set_fontsize(label_size)
        ax.yaxis.label.set_fontsize(label_size)
        ax.tick_params(labelsize=font_size)
        
        if grid:
            ax.grid(True, alpha=grid_alpha)
        
        ax.legend(fontsize=font_size)
        
        # Theme
        if theme == 'dark':
            ax.set_facecolor('#f0f0f0')
        elif theme == 'minimal':
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
        
        apply_theme(ax, theme)
    
    return ax


def learning_curve_interactive(
    train_sizes: ArrayLike,
    train_scores: ArrayLike,
    val_scores: ArrayLike,
    title: Optional[str] = None,
    train_color: Optional[str] = None,
    val_color: Optional[str] = None,
    linewidth: float = 2.0,
    marker_size: int = 8,
    showlegend: bool = True,
    hovermode: str = 'x unified',
    template: str = 'plotly',
    font_size: int = 12,
    title_size: int = 16,
    height: int = 600,
    width: int = 1000,
    **kwargs
) -> PlotlyFigure:
    """Create an interactive learning curve across training-set sizes.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        train_sizes (ArrayLike): Training-set sizes used to compute learning-curve scores.
        train_scores (ArrayLike): Training scores corresponding to each training-set size.
        val_scores (ArrayLike): Validation scores corresponding to each training-set size.
        title (Optional[str]): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``None``.
        train_color (Optional[str]): Configuration value for ``train_color``. Defaults to ``None``.
        val_color (Optional[str]): Configuration value for ``val_color``. Defaults to ``None``.
        linewidth (float): Configuration value for ``linewidth``. Defaults to ``2.0``.
        marker_size (int): Configuration value for ``marker_size``. Defaults to ``8``.
        showlegend (bool): Configuration value for ``showlegend``. Defaults to ``True``.
        hovermode (str): Configuration value for ``hovermode``. Defaults to ``'x unified'``.
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
        result = dv.learning_curve_interactive(train_sizes)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
    """
    if title is None:
        title = "Learning Curve"
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=train_sizes,
        y=train_scores,
        mode='lines+markers',
        name='Training Score',
        line=dict(color=train_color, width=linewidth),
        marker=dict(size=marker_size),
        **kwargs
    ))
    
    fig.add_trace(go.Scatter(
        x=train_sizes,
        y=val_scores,
        mode='lines+markers',
        name='Validation Score',
        line=dict(color=val_color, width=linewidth),
        marker=dict(size=marker_size),
        **kwargs
    ))
    
    fig.update_layout(
        title=dict(text=title, font=dict(size=title_size)),
        xaxis_title='Training Set Size',
        yaxis_title='Score',
        hovermode=hovermode,
        template=template,
        font=dict(size=font_size),
        height=height,
        width=width,
        showlegend=showlegend,
    )
    
    return fig
