"""Control chart implementation - static and interactive versions."""

from typing import Optional
from ..types import ArrayLike, FigureSize, MatplotlibAxes, PlotlyFigure
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from ..utils import setup_plot, apply_theme


def control_chart_static(
    data: ArrayLike,
    title: Optional[str] = None,
    xlabel: str = "Sample",
    ylabel: str = "Value",
    figsize: FigureSize = (12, 6),
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
) -> MatplotlibAxes:
    """Create a static statistical process control chart.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        data (ArrayLike): Input observations, measurements, or values used to build the chart.
        title (Optional[str]): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``None``.
        xlabel (str): Optional x-axis label. Defaults to ``'Sample'``.
        ylabel (str): Optional y-axis label. Defaults to ``'Value'``.
        figsize (FigureSize): Matplotlib figure size as ``(width, height)`` in inches. Defaults to ``(12, 6)``.
        dpi (int): Configuration value for ``dpi``. Defaults to ``100``.
        color_data (str): Configuration value for ``color_data``. Defaults to ``'steelblue'``.
        color_mean (str): Configuration value for ``color_mean``. Defaults to ``'green'``.
        color_limit (str): Configuration value for ``color_limit``. Defaults to ``'red'``.
        marker (str): Configuration value for ``marker``. Defaults to ``'o'``.
        marker_size (int): Configuration value for ``marker_size``. Defaults to ``6``.
        linewidth (float): Configuration value for ``linewidth``. Defaults to ``2.0``.
        line_width_limit (float): Configuration value for ``line_width_limit``. Defaults to ``1.0``.
        font_size (int): Configuration value for ``font_size``. Defaults to ``10``.
        title_size (int): Configuration value for ``title_size``. Defaults to ``14``.
        label_size (int): Configuration value for ``label_size``. Defaults to ``11``.
        sigma_multiplier (float): Configuration value for ``sigma_multiplier``. Defaults to ``3.0``.
        show_center_line (bool): Configuration value for ``show_center_line``. Defaults to ``True``.
        show_control_limits (bool): Configuration value for ``show_control_limits``. Defaults to ``True``.
        show_legend (bool): Configuration value for ``show_legend``. Defaults to ``True``.
        alpha_data (float): Configuration value for ``alpha_data``. Defaults to ``0.7``.
        alpha_limits (float): Configuration value for ``alpha_limits``. Defaults to ``0.5``.
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
    
    Examples:
        ```python
        import dataviz as dv
        result = dv.control_chart_static(data)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
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
    data: ArrayLike,
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
) -> PlotlyFigure:
    """Create an interactive statistical process control chart.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        data (ArrayLike): Input observations, measurements, or values used to build the chart.
        title (Optional[str]): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``None``.
        xlabel (str): Optional x-axis label. Defaults to ``'Sample'``.
        ylabel (str): Optional y-axis label. Defaults to ``'Value'``.
        height (int): Plotly figure height in pixels. Defaults to ``500``.
        width (int): Plotly figure width in pixels. Defaults to ``1000``.
        color_data (str): Configuration value for ``color_data``. Defaults to ``'steelblue'``.
        color_mean (str): Configuration value for ``color_mean``. Defaults to ``'green'``.
        color_limit (str): Configuration value for ``color_limit``. Defaults to ``'red'``.
        marker_size (int): Configuration value for ``marker_size``. Defaults to ``8``.
        line_width (int): Configuration value for ``line_width``. Defaults to ``2``.
        line_width_limit (int): Configuration value for ``line_width_limit``. Defaults to ``1``.
        font_size (int): Configuration value for ``font_size``. Defaults to ``12``.
        title_size (int): Configuration value for ``title_size``. Defaults to ``16``.
        label_size (int): Configuration value for ``label_size``. Defaults to ``12``.
        sigma_multiplier (float): Configuration value for ``sigma_multiplier``. Defaults to ``3.0``.
        show_center_line (bool): Configuration value for ``show_center_line``. Defaults to ``True``.
        show_control_limits (bool): Configuration value for ``show_control_limits``. Defaults to ``True``.
        show_legend (bool): Configuration value for ``show_legend``. Defaults to ``True``.
        hovermode (str): Configuration value for ``hovermode``. Defaults to ``'x unified'``.
        template (str): Plotly template used to style the interactive figure. Defaults to ``'plotly'``.
        **kwargs (Any): Additional keyword arguments forwarded to the underlying plotting function.
    
    Returns:
        plotly.graph_objects.Figure: Configured Plotly figure containing the rendered interactive chart.
    
    Raises:
        TypeError: If required inputs are not compatible with the plotting backend.
        ValueError: If input lengths, matrix shapes, or option values are invalid for the requested chart.
    
    Examples:
        ```python
        import dataviz as dv
        result = dv.control_chart_interactive(data)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
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
