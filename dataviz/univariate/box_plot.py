"""Box plot implementation - static and interactive versions."""

from typing import Optional, Tuple
from ..types import FigureSize, FrameLike, MatplotlibAxes, PlotlyFigure
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from ..utils import setup_plot, apply_theme


def box_plot_static(
    data: FrameLike,
    title: Optional[str] = None,
    ylabel: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    color: Optional[str] = None,
    patch_artist: bool = True,
    notch: bool = False,
    grid: bool = True,
    grid_alpha: float = 0.3,
    theme: str = 'default',
    font_size: int = 10,
    title_size: int = 14,
    label_size: int = 11,
    dpi: int = 100,
    style: str = 'default',
    widths: float = 0.6,
    **kwargs
) -> MatplotlibAxes:
    """Create a static box plot that summarizes quartiles, spread, and outliers.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        data (FrameLike): Input observations, measurements, or values used to build the chart.
        title (Optional[str]): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``None``.
        ylabel (Optional[str]): Optional y-axis label. Defaults to ``None``.
        figsize (FigureSize): Matplotlib figure size as ``(width, height)`` in inches. Defaults to ``(10, 6)``.
        color (Optional[str]): Configuration value for ``color``. Defaults to ``None``.
        patch_artist (bool): Configuration value for ``patch_artist``. Defaults to ``True``.
        notch (bool): Configuration value for ``notch``. Defaults to ``False``.
        grid (bool): Configuration value for ``grid``. Defaults to ``True``.
        grid_alpha (float): Configuration value for ``grid_alpha``. Defaults to ``0.3``.
        theme (str): Named styling theme applied after the base plot is created. Defaults to ``'default'``.
        font_size (int): Configuration value for ``font_size``. Defaults to ``10``.
        title_size (int): Configuration value for ``title_size``. Defaults to ``14``.
        label_size (int): Configuration value for ``label_size``. Defaults to ``11``.
        dpi (int): Configuration value for ``dpi``. Defaults to ``100``.
        style (str): Matplotlib style context used while building the figure. Defaults to ``'default'``.
        widths (float): Configuration value for ``widths``. Defaults to ``0.6``.
        **kwargs (Any): Additional keyword arguments forwarded to the underlying plotting function.
    
    Returns:
        matplotlib.axes.Axes: Configured matplotlib axes containing the rendered static chart.
    
    Raises:
        TypeError: If required inputs are not compatible with the plotting backend.
        ValueError: If input lengths, matrix shapes, or option values are invalid for the requested chart.
    
    Example:
        ```python
        import dataviz as dv
        result = dv.box_plot_static(data)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
    """
    if title is None:
        title = "Box Plot"
    if ylabel is None:
        ylabel = 'Value'
    
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, ylabel=ylabel, figsize=figsize)
        fig.set_dpi(dpi)
        
        bp = ax.boxplot(data, patch_artist=patch_artist, notch=notch, widths=widths, **kwargs)
        
        # Color boxes
        if color and patch_artist:
            for box in bp['boxes']:
                box.set_facecolor(color)
        
        # Customize fonts
        ax.title.set_fontsize(title_size)
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


def box_plot_interactive(
    data: FrameLike,
    title: Optional[str] = None,
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
    boxmean: bool = True,
    points: str = 'outliers',
    **kwargs
) -> PlotlyFigure:
    """Create an interactive box plot that summarizes quartiles, spread, and outliers.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        data (FrameLike): Input observations, measurements, or values used to build the chart.
        title (Optional[str]): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``None``.
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
        boxmean (bool): Configuration value for ``boxmean``. Defaults to ``True``.
        points (str): Configuration value for ``points``. Defaults to ``'outliers'``.
        **kwargs (Any): Additional keyword arguments forwarded to the underlying plotting function.
    
    Returns:
        plotly.graph_objects.Figure: Configured Plotly figure containing the rendered interactive chart.
    
    Raises:
        TypeError: If required inputs are not compatible with the plotting backend.
        ValueError: If input lengths, matrix shapes, or option values are invalid for the requested chart.
    
    Example:
        ```python
        import dataviz as dv
        result = dv.box_plot_interactive(data)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
    """
    if title is None:
        title = "Box Plot"
    if ylabel is None:
        ylabel = 'Value'
    if color is None:
        color = marker_color
    
    fig = go.Figure()
    
    if isinstance(data, pd.DataFrame):
        for col in data.columns:
            fig.add_trace(go.Box(
                y=data[col],
                name=str(col),
                marker_color=color,
                boxmean=boxmean,
                points=points,
                **kwargs
            ))
    else:
        fig.add_trace(go.Box(
            y=data,
            marker_color=color,
            boxmean=boxmean,
            points=points,
            **kwargs
        ))
    
    fig.update_layout(
        title=dict(text=title, font=dict(size=title_size)),
        yaxis_title=ylabel,
        hovermode=hovermode,
        template=template,
        font=dict(size=font_size),
        height=height,
        width=width,
        showlegend=showlegend,
    )
    
    return fig
