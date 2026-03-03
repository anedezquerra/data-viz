"""X-Range chart implementation - static and interactive versions."""

from typing import Optional
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from ..utils import setup_plot, apply_theme


def x_range_chart_static(
    data: np.ndarray,
    subgroup_size: int = 5,
    title: Optional[str] = None,
    xlabel: str = "Sample",
    ylabel: str = "Value",
    figsize: tuple = (12, 6),
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
) -> plt.Axes:
    """
    Create a static X-Range (individuals and moving range) chart using matplotlib.

    Parameters
    ----------
    data : array-like
        Process measurements
    subgroup_size : int, default 5
        Size of subgroups for moving range calculation
    title : str, optional
        Chart title (auto-generated if None)
    xlabel : str, default "Sample"
        X-axis label
    ylabel : str, default "Value"
        Y-axis label
    figsize : tuple, default (12, 6)
        Figure size (width, height)
    dpi : int, default 100
        Figure DPI
    color_individuals : str, default 'steelblue'
        Color for individual values
    color_range : str, default 'orange'
        Color for moving range
    color_mean : str, default 'green'
        Center line color
    color_limits : str, default 'red'
        Control limit color
    marker : str, default 'o'
        Marker style
    marker_size : int, default 6
        Marker size
    linewidth : float, default 2.0
        Line width
    font_size : int, default 10
        Base font size
    title_size : int, default 14
        Title font size
    label_size : int, default 11
        Axis label font size
    show_moving_avg : bool, default True
        Show moving average
    show_range_bounds : bool, default True
        Show range control bounds
    alpha : float, default 0.7
        Line transparency
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
    data: np.ndarray,
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
) -> go.Figure:
    """
    Create an interactive X-Range chart using plotly.

    Parameters
    ----------
    data : array-like
        Process measurements
    subgroup_size : int, default 5
        Size of subgroups for moving range calculation
    title : str, optional
        Chart title (auto-generated if None)
    xlabel : str, default "Sample"
        X-axis label
    ylabel : str, default "Value"
        Y-axis label
    height : int, default 500
        Figure height
    width : int, default 1000
        Figure width
    color_individuals : str, default 'steelblue'
        Color for individual values
    color_range : str, default 'orange'
        Color for moving range
    color_mean : str, default 'green'
        Center line color
    marker_size : int, default 8
        Marker size
    line_width : int, default 2
        Line width
    font_size : int, default 12
        Base font size
    title_size : int, default 16
        Title font size
    label_size : int, default 12
        Axis label font size
    show_moving_avg : bool, default True
        Show moving average
    show_range_bounds : bool, default True
        Show range control bounds
    hovermode : str, default 'x unified'
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
