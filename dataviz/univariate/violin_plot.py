"""Violin plot implementation - static and interactive versions."""

from typing import Optional, Tuple
from ..types import FigureSize, FrameLike, MatplotlibAxes, PlotlyFigure
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
from ..utils import setup_plot, apply_theme


def violin_plot_static(
    data: FrameLike,
    x: Optional[str] = None,
    y: Optional[str] = None,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    color: Optional[str] = None,
    palette: Optional[str] = None,
    inner: str = 'box',
    cut: float = 0.0,
    alpha: float = 0.7,
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = 'default',
    font_size: int = 10,
    title_size: int = 14,
    label_size: int = 11,
    dpi: int = 100,
    style: str = 'default',
    linewidth: float = 1.5,
    **kwargs
) -> MatplotlibAxes:
    """Create a static violin plot that shows the full distribution shape.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        data (FrameLike): Input observations, measurements, or values used to build the chart.
        x (Optional[str]): Values plotted along the x-axis. Defaults to ``None``.
        y (Optional[str]): Values plotted along the y-axis. Defaults to ``None``.
        title (Optional[str]): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``None``.
        xlabel (Optional[str]): Optional x-axis label. Defaults to ``None``.
        ylabel (Optional[str]): Optional y-axis label. Defaults to ``None``.
        figsize (FigureSize): Matplotlib figure size as ``(width, height)`` in inches. Defaults to ``(10, 6)``.
        color (Optional[str]): Configuration value for ``color``. Defaults to ``None``.
        palette (Optional[str]): Configuration value for ``palette``. Defaults to ``None``.
        inner (str): Configuration value for ``inner``. Defaults to ``'box'``.
        cut (float): Configuration value for ``cut``. Defaults to ``0.0``.
        alpha (float): Configuration value for ``alpha``. Defaults to ``0.7``.
        grid (bool): Configuration value for ``grid``. Defaults to ``True``.
        grid_alpha (float): Configuration value for ``grid_alpha``. Defaults to ``0.3``.
        theme (str): Named styling theme applied after the base plot is created. Defaults to ``'default'``.
        font_size (int): Configuration value for ``font_size``. Defaults to ``10``.
        title_size (int): Configuration value for ``title_size``. Defaults to ``14``.
        label_size (int): Configuration value for ``label_size``. Defaults to ``11``.
        dpi (int): Configuration value for ``dpi``. Defaults to ``100``.
        style (str): Matplotlib style context used while building the figure. Defaults to ``'default'``.
        linewidth (float): Configuration value for ``linewidth``. Defaults to ``1.5``.
        **kwargs (Any): Additional keyword arguments forwarded to the underlying plotting function.
    
    Returns:
        matplotlib.axes.Axes: Configured matplotlib axes containing the rendered static chart.
    
    Raises:
        TypeError: If required inputs are not compatible with the plotting backend.
        ValueError: If input lengths, matrix shapes, or option values are invalid for the requested chart.
    
    Examples:
        ```python
        import dataviz as dv
        result = dv.violin_plot_static(data, x, y)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
    """
    if title is None:
        title = "Violin Plot"
    
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel=xlabel, ylabel=ylabel, figsize=figsize)
        fig.set_dpi(dpi)
        
        ax = sns.violinplot(
            data=data,
            x=x,
            y=y,
            color=color,
            palette=palette,
            inner=inner,
            cut=cut,
            alpha=alpha,
            linewidth=linewidth,
            ax=ax,
            **kwargs
        )
        
        # Customize fonts
        ax.title.set_fontsize(title_size)
        if xlabel:
            ax.xaxis.label.set_fontsize(label_size)
        if ylabel:
            ax.yaxis.label.set_fontsize(label_size)
        ax.tick_params(labelsize=font_size)
        
        # Grid
        if grid:
            ax.grid(True, alpha=grid_alpha, axis='y')
        
        # Theme
        if theme == 'dark':
            ax.set_facecolor('#f0f0f0')
        elif theme == 'minimal':
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
        
        apply_theme(ax, theme)
    
    return ax


def violin_plot_interactive(
    data: FrameLike,
    x: Optional[str] = None,
    y: Optional[str] = None,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    color: Optional[str] = None,
    marker_color: Optional[str] = None,
    showlegend: bool = True,
    hovermode: str = 'closest',
    template: str = 'plotly',
    font_size: int = 12,
    title_size: int = 16,
    height: int = 600,
    width: int = 1000,
    meanline: bool = True,
    points: bool = False,
    **kwargs
) -> PlotlyFigure:
    """Create an interactive violin plot that shows the full distribution shape.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        data (FrameLike): Input observations, measurements, or values used to build the chart.
        x (Optional[str]): Values plotted along the x-axis. Defaults to ``None``.
        y (Optional[str]): Values plotted along the y-axis. Defaults to ``None``.
        title (Optional[str]): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``None``.
        xlabel (Optional[str]): Optional x-axis label. Defaults to ``None``.
        ylabel (Optional[str]): Optional y-axis label. Defaults to ``None``.
        color (Optional[str]): Configuration value for ``color``. Defaults to ``None``.
        marker_color (Optional[str]): Configuration value for ``marker_color``. Defaults to ``None``.
        showlegend (bool): Configuration value for ``showlegend``. Defaults to ``True``.
        hovermode (str): Configuration value for ``hovermode``. Defaults to ``'closest'``.
        template (str): Plotly template used to style the interactive figure. Defaults to ``'plotly'``.
        font_size (int): Configuration value for ``font_size``. Defaults to ``12``.
        title_size (int): Configuration value for ``title_size``. Defaults to ``16``.
        height (int): Plotly figure height in pixels. Defaults to ``600``.
        width (int): Plotly figure width in pixels. Defaults to ``1000``.
        meanline (bool): Configuration value for ``meanline``. Defaults to ``True``.
        points (bool): Configuration value for ``points``. Defaults to ``False``.
        **kwargs (Any): Additional keyword arguments forwarded to the underlying plotting function.
    
    Returns:
        plotly.graph_objects.Figure: Configured Plotly figure containing the rendered interactive chart.
    
    Raises:
        TypeError: If required inputs are not compatible with the plotting backend.
        ValueError: If input lengths, matrix shapes, or option values are invalid for the requested chart.
    
    Examples:
        ```python
        import dataviz as dv
        result = dv.violin_plot_interactive(data, x, y)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
    """
    if title is None:
        title = "Violin Plot"
    if color is None:
        color = marker_color
    
    fig = go.Figure()
    
    if x and isinstance(data, pd.DataFrame):
        groups = data[x].unique()
        for group in groups:
            group_data = data[data[x] == group][y] if y else data[data[x] == group]
            fig.add_trace(go.Violin(
                y=group_data,
                name=str(group),
                marker_color=color,
                meanline_visible=meanline,
                points='all' if points else False,
                **kwargs
            ))
    else:
        fig.add_trace(go.Violin(
            y=data,
            marker_color=color,
            meanline_visible=meanline,
            points='all' if points else False,
            **kwargs
        ))
    
    fig.update_layout(
        title=dict(text=title, font=dict(size=title_size)),
        xaxis_title=xlabel,
        yaxis_title=ylabel,
        hovermode=hovermode,
        template=template,
        font=dict(size=font_size),
        height=height,
        width=width,
        showlegend=showlegend,
    )
    
    return fig
