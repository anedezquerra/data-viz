"""Partial dependence implementation - static and interactive versions."""

from typing import Optional
from ..types import ArrayLike, FigureSize, MatplotlibAxes, MatrixLike, PlotlyFigure
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from ..utils import setup_plot, apply_theme


def partial_dependence_static(
    feature_values: ArrayLike,
    predictions: ArrayLike,
    feature_name: str = "Feature",
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: str = "Prediction",
    figsize: FigureSize = (10, 6),
    dpi: int = 100,
    color: str = 'steelblue',
    marker: str = 'o',
    marker_size: int = 6,
    linewidth: float = 2.0,
    linestyle: str = '-',
    alpha: float = 0.7,
    font_size: int = 10,
    title_size: int = 14,
    label_size: int = 11,
    show_rugs: bool = False,
    show_confidence: bool = False,
    confidence_interval: Optional[MatrixLike] = None,
    confidence_alpha: float = 0.2,
    theme: str = 'default',
    style: str = 'default',
    grid: bool = True,
    grid_alpha: float = 0.3,
    **kwargs
) -> MatplotlibAxes:
    """Create a static partial-dependence relationship for one feature.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        feature_values (ArrayLike): Feature grid or observed feature values for partial dependence.
        predictions (ArrayLike): Predicted response values corresponding to the feature grid.
        feature_name (str): Configuration value for ``feature_name``. Defaults to ``'Feature'``.
        title (Optional[str]): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``None``.
        xlabel (Optional[str]): Optional x-axis label. Defaults to ``None``.
        ylabel (str): Optional y-axis label. Defaults to ``'Prediction'``.
        figsize (FigureSize): Matplotlib figure size as ``(width, height)`` in inches. Defaults to ``(10, 6)``.
        dpi (int): Configuration value for ``dpi``. Defaults to ``100``.
        color (str): Configuration value for ``color``. Defaults to ``'steelblue'``.
        marker (str): Configuration value for ``marker``. Defaults to ``'o'``.
        marker_size (int): Configuration value for ``marker_size``. Defaults to ``6``.
        linewidth (float): Configuration value for ``linewidth``. Defaults to ``2.0``.
        linestyle (str): Configuration value for ``linestyle``. Defaults to ``'-'``.
        alpha (float): Configuration value for ``alpha``. Defaults to ``0.7``.
        font_size (int): Configuration value for ``font_size``. Defaults to ``10``.
        title_size (int): Configuration value for ``title_size``. Defaults to ``14``.
        label_size (int): Configuration value for ``label_size``. Defaults to ``11``.
        show_rugs (bool): Configuration value for ``show_rugs``. Defaults to ``False``.
        show_confidence (bool): Configuration value for ``show_confidence``. Defaults to ``False``.
        confidence_interval (Optional[MatrixLike]): Optional lower and upper confidence bounds for partial-dependence values. Defaults to ``None``.
        confidence_alpha (float): Configuration value for ``confidence_alpha``. Defaults to ``0.2``.
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
        result = dv.partial_dependence_static(feature_values, predictions)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
    """
    if title is None:
        title = f"Partial Dependence - {feature_name}"
    
    if xlabel is None:
        xlabel = feature_name
    
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel=xlabel, ylabel=ylabel, figsize=figsize)
        fig.set_dpi(dpi)
        
        # Plot main line
        ax.plot(
            feature_values,
            predictions,
            marker=marker,
            markersize=marker_size,
            linewidth=linewidth,
            linestyle=linestyle,
            color=color,
            alpha=alpha,
            **kwargs
        )
        
        # Add confidence interval if provided
        if show_confidence and confidence_interval is not None:
            ax.fill_between(
                feature_values,
                confidence_interval[:, 0],
                confidence_interval[:, 1],
                alpha=confidence_alpha,
                color=color
            )
        
        # Add rug marks
        if show_rugs:
            ax.plot(
                feature_values,
                np.zeros_like(feature_values),
                '|',
                markersize=10,
                color=color,
                alpha=0.5
            )
        
        # Apply labels and formatting
        ax.set_xlabel(xlabel, fontsize=label_size)
        ax.set_ylabel(ylabel, fontsize=label_size)
        ax.title.set_fontsize(title_size)
        ax.tick_params(labelsize=font_size)
        
        # Apply grid
        if grid:
            ax.grid(True, alpha=grid_alpha)
        
        # Apply theme
        if theme == 'dark':
            ax.set_facecolor('#2b2b2b')
            fig.patch.set_facecolor('#1e1e1e')
        elif theme == 'minimal':
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
        
        apply_theme(ax, theme)
    
    return ax


def partial_dependence_interactive(
    feature_values: ArrayLike,
    predictions: ArrayLike,
    feature_name: str = "Feature",
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: str = "Prediction",
    height: int = 500,
    width: int = 800,
    color: str = 'steelblue',
    marker_size: int = 8,
    line_width: int = 2,
    font_size: int = 12,
    title_size: int = 16,
    label_size: int = 12,
    show_rugs: bool = False,
    show_confidence: bool = False,
    confidence_interval: Optional[MatrixLike] = None,
    confidence_alpha: float = 0.2,
    hovermode: str = 'closest',
    template: str = 'plotly',
    **kwargs
) -> PlotlyFigure:
    """Create an interactive partial-dependence relationship for one feature.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        feature_values (ArrayLike): Feature grid or observed feature values for partial dependence.
        predictions (ArrayLike): Predicted response values corresponding to the feature grid.
        feature_name (str): Configuration value for ``feature_name``. Defaults to ``'Feature'``.
        title (Optional[str]): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``None``.
        xlabel (Optional[str]): Optional x-axis label. Defaults to ``None``.
        ylabel (str): Optional y-axis label. Defaults to ``'Prediction'``.
        height (int): Plotly figure height in pixels. Defaults to ``500``.
        width (int): Plotly figure width in pixels. Defaults to ``800``.
        color (str): Configuration value for ``color``. Defaults to ``'steelblue'``.
        marker_size (int): Configuration value for ``marker_size``. Defaults to ``8``.
        line_width (int): Configuration value for ``line_width``. Defaults to ``2``.
        font_size (int): Configuration value for ``font_size``. Defaults to ``12``.
        title_size (int): Configuration value for ``title_size``. Defaults to ``16``.
        label_size (int): Configuration value for ``label_size``. Defaults to ``12``.
        show_rugs (bool): Configuration value for ``show_rugs``. Defaults to ``False``.
        show_confidence (bool): Configuration value for ``show_confidence``. Defaults to ``False``.
        confidence_interval (Optional[MatrixLike]): Optional lower and upper confidence bounds for partial-dependence values. Defaults to ``None``.
        confidence_alpha (float): Configuration value for ``confidence_alpha``. Defaults to ``0.2``.
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
        result = dv.partial_dependence_interactive(feature_values, predictions)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
    """
    if title is None:
        title = f"Partial Dependence - {feature_name}"
    
    if xlabel is None:
        xlabel = feature_name
    
    fig = go.Figure()
    
    # Add main trace
    fig.add_trace(go.Scatter(
        x=feature_values,
        y=predictions,
        mode='lines+markers',
        name='Partial Dependence',
        marker=dict(size=marker_size, color=color),
        line=dict(color=color, width=line_width),
        hovertemplate='<b>%{x:.3f}</b><br>Prediction: %{y:.4f}<extra></extra>',
        **kwargs
    ))
    
    # Add confidence interval if provided
    if show_confidence and confidence_interval is not None:
        fig.add_trace(go.Scatter(
            x=np.concatenate([feature_values, feature_values[::-1]]),
            y=np.concatenate([
                confidence_interval[:, 0],
                confidence_interval[::-1, 1]
            ]),
            fill='toself',
            name='Confidence Interval',
            fillcolor=f'rgba(70, 130, 180, {confidence_alpha})',
            line=dict(color='rgba(255,255,255,0)'),
            hoverinfo='skip',
            showlegend=True
        ))
    
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
partial_dependence = partial_dependence_static
