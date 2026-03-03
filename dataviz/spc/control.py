"""Control chart implementation - static and interactive versions."""

from typing import Optional
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from ..utils import setup_plot, apply_theme


def control_chart_static(
    data: np.ndarray,
    title: Optional[str] = None,
    xlabel: str = "Sample",
    ylabel: str = "Value",
    figsize: tuple = (12, 6),
    dpi: int = 100,
    color_data: str = 'steelblue',
    color_mean: str = 'green',
    color_limit: str = 'red',
    marker: str = 'o',
    marker_size: int = 6,
    linewidth: float = 2.0,
    line_width_limit: float = 1.0,
    font_size: int = 10,
    title_size: int = 14,
    label_size: int = 11,
    sigma_multiplier: float = 3.0,
    show_center_line: bool = True,
    show_control_limits: bool = True,
    show_legend: bool = True,
    alpha_data: float = 0.7,
    alpha_limits: float = 0.5,
    theme: str = 'default',
    style: str = 'default',
    grid: bool = True,
    grid_alpha: float = 0.3,
    **kwargs
) -> plt.Axes:
    """
    Create a static control chart using matplotlib.

    Parameters
    ----------
    data : array-like
        Process measurements
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
    color_data : str, default 'steelblue'
        Data point color
    color_mean : str, default 'green'
        Center line color
    color_limit : str, default 'red'
        Control limit color
    marker : str, default 'o'
        Marker style
    marker_size : int, default 6
        Marker size
    linewidth : float, default 2.0
        Data line width
    line_width_limit : float, default 1.0
        Control limit line width
    font_size : int, default 10
        Base font size
    title_size : int, default 14
        Title font size
    label_size : int, default 11
        Axis label font size
    sigma_multiplier : float, default 3.0
        Standard deviation multiplier for control limits
    show_center_line : bool, default True
        Show center line (mean)
    show_control_limits : bool, default True
        Show control limits
    show_legend : bool, default True
        Show legend
    alpha_data : float, default 0.7
        Data transparency
    alpha_limits : float, default 0.5
        Control limit transparency
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
        title = "Control Chart"
    
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel=xlabel, ylabel=ylabel, figsize=figsize)
        fig.set_dpi(dpi)
        
        mean = np.mean(data)
        std = np.std(data)
        ucl = mean + sigma_multiplier * std
        lcl = mean - sigma_multiplier * std
        
        # Plot data
        ax.plot(
            data,
            marker=marker,
            markersize=marker_size,
            linewidth=linewidth,
            color=color_data,
            alpha=alpha_data,
            label='Process Data',
            **kwargs
        )
        
        # Plot center line
        if show_center_line:
            ax.axhline(
                mean,
                color=color_mean,
                linestyle='-',
                linewidth=line_width_limit,
                label='Mean',
                alpha=alpha_limits
            )
        
        # Plot control limits
        if show_control_limits:
            ax.axhline(
                ucl,
                color=color_limit,
                linestyle='--',
                linewidth=line_width_limit,
                label=f'UCL (±{sigma_multiplier}σ)',
                alpha=alpha_limits
            )
            ax.axhline(
                lcl,
                color=color_limit,
                linestyle='--',
                linewidth=line_width_limit,
                label=f'LCL (±{sigma_multiplier}σ)',
                alpha=alpha_limits
            )
        
        # Apply formatting
        ax.set_xlabel(xlabel, fontsize=label_size)
        ax.set_ylabel(ylabel, fontsize=label_size)
        ax.title.set_fontsize(title_size)
        ax.tick_params(labelsize=font_size)
        
        # Apply grid
        if grid:
            ax.grid(True, alpha=grid_alpha)
        
        # Apply legend
        if show_legend:
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


def control_chart_interactive(
    data: np.ndarray,
    title: Optional[str] = None,
    xlabel: str = "Sample",
    ylabel: str = "Value",
    height: int = 500,
    width: int = 1000,
    color_data: str = 'steelblue',
    color_mean: str = 'green',
    color_limit: str = 'red',
    marker_size: int = 8,
    line_width: int = 2,
    line_width_limit: int = 1,
    font_size: int = 12,
    title_size: int = 16,
    label_size: int = 12,
    sigma_multiplier: float = 3.0,
    show_center_line: bool = True,
    show_control_limits: bool = True,
    show_legend: bool = True,
    hovermode: str = 'x unified',
    template: str = 'plotly',
    **kwargs
) -> go.Figure:
    """
    Create an interactive control chart using plotly.

    Parameters
    ----------
    data : array-like
        Process measurements
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
    color_data : str, default 'steelblue'
        Data point color
    color_mean : str, default 'green'
        Center line color
    color_limit : str, default 'red'
        Control limit color
    marker_size : int, default 8
        Marker size
    line_width : int, default 2
        Data line width
    line_width_limit : int, default 1
        Control limit line width
    font_size : int, default 12
        Base font size
    title_size : int, default 16
        Title font size
    label_size : int, default 12
        Axis label font size
    sigma_multiplier : float, default 3.0
        Standard deviation multiplier for control limits
    show_center_line : bool, default True
        Show center line (mean)
    show_control_limits : bool, default True
        Show control limits
    show_legend : bool, default True
        Show legend
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
        title = "Control Chart"
    
    mean = np.mean(data)
    std = np.std(data)
    ucl = mean + sigma_multiplier * std
    lcl = mean - sigma_multiplier * std
    
    fig = go.Figure()
    
    # Add data trace
    fig.add_trace(go.Scatter(
        y=data,
        mode='lines+markers',
        name='Process Data',
        marker=dict(size=marker_size, color=color_data),
        line=dict(color=color_data, width=line_width),
        hovertemplate='<b>Sample %{x}</b><br>Value: %{y:.4f}<extra></extra>',
        **kwargs
    ))
    
    # Add center line
    if show_center_line:
        fig.add_hline(
            y=mean,
            line_color=color_mean,
            line_dash='solid',
            line_width=line_width_limit,
            name='Mean'
        )
    
    # Add control limits
    if show_control_limits:
        fig.add_hline(
            y=ucl,
            line_dash='dash',
            line_color=color_limit,
            line_width=line_width_limit,
            name=f'UCL (±{sigma_multiplier}σ)'
        )
        fig.add_hline(
            y=lcl,
            line_dash='dash',
            line_color=color_limit,
            line_width=line_width_limit,
            name=f'LCL (±{sigma_multiplier}σ)'
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
        font=dict(size=font_size),
        showlegend=show_legend
    )
    
    return fig


# Default alias
control_chart = control_chart_static
