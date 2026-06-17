"""X-Range chart implementation - static and interactive versions."""

from typing import Optional
from ..types import ArrayLike, FigureSize, MatplotlibAxes, PlotlyFigure
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from ..utils import setup_plot, apply_theme


def x_range_chart_static(
    data: ArrayLike,
    subgroup_size: int = 5,
    title: Optional[str] = None,
    xlabel: str = "Sample",
    ylabel: str = "Value",
    figsize: FigureSize = (12, 6),
    dpi: int = 100,
    color_individuals: str = 'steelblue',
    color_range: str = 'orange',
    color_mean: str = 'green',
    color_limits: str = 'red',
    marker: str = 'o',
    marker_size: int = 6,
    linewidth: float = 2.0,
    font_size: int = 10,
    title_size: int = 14,
    label_size: int = 11,
    show_moving_avg: bool = True,
    show_range_bounds: bool = True,
    alpha: float = 0.7,
    theme: str = 'default',
    style: str = 'default',
    grid: bool = True,
    grid_alpha: float = 0.3,
    **kwargs
) -> MatplotlibAxes:
    """Create a static X-range chart for individual values and range monitoring.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        data (ArrayLike): Input observations, measurements, or values used to build the chart.
        subgroup_size (int): Number of observations used in each subgroup calculation. Defaults to ``5``.
        title (Optional[str]): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``None``.
        xlabel (str): Optional x-axis label. Defaults to ``'Sample'``.
        ylabel (str): Optional y-axis label. Defaults to ``'Value'``.
        figsize (FigureSize): Matplotlib figure size as ``(width, height)`` in inches. Defaults to ``(12, 6)``.
        dpi (int): Configuration value for ``dpi``. Defaults to ``100``.
        color_individuals (str): Configuration value for ``color_individuals``. Defaults to ``'steelblue'``.
        color_range (str): Configuration value for ``color_range``. Defaults to ``'orange'``.
        color_mean (str): Configuration value for ``color_mean``. Defaults to ``'green'``.
        color_limits (str): Configuration value for ``color_limits``. Defaults to ``'red'``.
        marker (str): Configuration value for ``marker``. Defaults to ``'o'``.
        marker_size (int): Configuration value for ``marker_size``. Defaults to ``6``.
        linewidth (float): Configuration value for ``linewidth``. Defaults to ``2.0``.
        font_size (int): Configuration value for ``font_size``. Defaults to ``10``.
        title_size (int): Configuration value for ``title_size``. Defaults to ``14``.
        label_size (int): Configuration value for ``label_size``. Defaults to ``11``.
        show_moving_avg (bool): Configuration value for ``show_moving_avg``. Defaults to ``True``.
        show_range_bounds (bool): Configuration value for ``show_range_bounds``. Defaults to ``True``.
        alpha (float): Configuration value for ``alpha``. Defaults to ``0.7``.
        theme (str): Named styling theme applied after the base plot is created. Defaults to ``'default'``.
        style (str): Matplotlib style context used while building the figure. Defaults to ``'default'``.
        grid (bool): Configuration value for ``grid``. Defaults to ``True``.
        grid_alpha (float): Configuration value for ``grid_alpha``. Defaults to ``0.3``.
        **kwargs (Any): Additional keyword arguments forwarded to the underlying plotting function.
    
    Returns:
        matplotlib.axes.Axes: Configured matplotlib axes containing the rendered static chart.
    
    Raises:
        TypeError: If required inputs are not compatible with the plotting backend.
        ValueError: If input lengths, matrix shapes, or option values are invalid for the requested chart.
    
    Example:
        ```python
        import dataviz as dv
        result = dv.x_range_chart_static(data)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
    """
    if title is None:
        title = "X-Range Chart"
    
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel=xlabel, ylabel=ylabel, figsize=figsize)
        fig.set_dpi(dpi)
        
        # Plot individual values
        ax.plot(
            data,
            marker=marker,
            markersize=marker_size,
            linewidth=linewidth,
            color=color_individuals,
            alpha=alpha,
            label='Individual Values',
            **kwargs
        )
        
        # Calculate and plot moving average
        if show_moving_avg:
            moving_avg = np.convolve(data, np.ones(subgroup_size)/subgroup_size, mode='valid')
            ax.plot(
                range(subgroup_size-1, len(data)),
                moving_avg,
                marker='s',
                markersize=marker_size,
                linewidth=linewidth,
                color=color_range,
                alpha=alpha,
                label=f'Moving Avg (n={subgroup_size})',
                linestyle='--'
            )
        
        # Add mean line
        mean = np.mean(data)
        ax.axhline(mean, color=color_mean, linestyle='-', linewidth=1.5, label='Mean')
        
        # Apply formatting
        ax.set_xlabel(xlabel, fontsize=label_size)
        ax.set_ylabel(ylabel, fontsize=label_size)
        ax.title.set_fontsize(title_size)
        ax.tick_params(labelsize=font_size)
        
        # Apply grid
        if grid:
            ax.grid(True, alpha=grid_alpha)
        
        # Apply legend
        ax.legend(fontsize=font_size)
        
        # Apply theme
        if theme == 'dark':
            ax.set_facecolor('#2b2b2b')
            fig.patch.set_facecolor('#1e1e1e')
        elif theme == 'minimal':
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
        
        apply_theme(ax, theme)
    
    return ax


def x_range_chart_interactive(
    data: ArrayLike,
    subgroup_size: int = 5,
    title: Optional[str] = None,
    xlabel: str = "Sample",
    ylabel: str = "Value",
    height: int = 500,
    width: int = 1000,
    color_individuals: str = 'steelblue',
    color_range: str = 'orange',
    color_mean: str = 'green',
    marker_size: int = 8,
    line_width: int = 2,
    font_size: int = 12,
    title_size: int = 16,
    label_size: int = 12,
    show_moving_avg: bool = True,
    show_range_bounds: bool = True,
    hovermode: str = 'x unified',
    template: str = 'plotly',
    **kwargs
) -> PlotlyFigure:
    """Create an interactive X-range chart for individual values and range monitoring.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        data (ArrayLike): Input observations, measurements, or values used to build the chart.
        subgroup_size (int): Number of observations used in each subgroup calculation. Defaults to ``5``.
        title (Optional[str]): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``None``.
        xlabel (str): Optional x-axis label. Defaults to ``'Sample'``.
        ylabel (str): Optional y-axis label. Defaults to ``'Value'``.
        height (int): Plotly figure height in pixels. Defaults to ``500``.
        width (int): Plotly figure width in pixels. Defaults to ``1000``.
        color_individuals (str): Configuration value for ``color_individuals``. Defaults to ``'steelblue'``.
        color_range (str): Configuration value for ``color_range``. Defaults to ``'orange'``.
        color_mean (str): Configuration value for ``color_mean``. Defaults to ``'green'``.
        marker_size (int): Configuration value for ``marker_size``. Defaults to ``8``.
        line_width (int): Configuration value for ``line_width``. Defaults to ``2``.
        font_size (int): Configuration value for ``font_size``. Defaults to ``12``.
        title_size (int): Configuration value for ``title_size``. Defaults to ``16``.
        label_size (int): Configuration value for ``label_size``. Defaults to ``12``.
        show_moving_avg (bool): Configuration value for ``show_moving_avg``. Defaults to ``True``.
        show_range_bounds (bool): Configuration value for ``show_range_bounds``. Defaults to ``True``.
        hovermode (str): Configuration value for ``hovermode``. Defaults to ``'x unified'``.
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
        result = dv.x_range_chart_interactive(data)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
    """
    if title is None:
        title = "X-Range Chart"
    
    fig = go.Figure()
    
    # Add individual values trace
    fig.add_trace(go.Scatter(
        y=data,
        mode='lines+markers',
        name='Individual Values',
        marker=dict(size=marker_size, color=color_individuals),
        line=dict(color=color_individuals, width=line_width),
        hovertemplate='<b>Sample %{x}</b><br>Value: %{y:.4f}<extra></extra>',
        **kwargs
    ))
    
    # Add moving average if requested
    if show_moving_avg:
        moving_avg = np.convolve(data, np.ones(subgroup_size)/subgroup_size, mode='valid')
        fig.add_trace(go.Scatter(
            y=moving_avg,
            x=list(range(subgroup_size-1, len(data))),
            mode='lines+markers',
            name=f'Moving Avg (n={subgroup_size})',
            marker=dict(size=marker_size, color=color_range),
            line=dict(color=color_range, width=line_width, dash='dash'),
            hovertemplate='<b>Sample %{x}</b><br>Moving Avg: %{y:.4f}<extra></extra>'
        ))
    
    # Add mean line
    mean = np.mean(data)
    fig.add_hline(
        y=mean,
        line_color=color_mean,
        line_dash='solid',
        line_width=1,
        name='Mean'
    )
    
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
x_range_chart = x_range_chart_static
