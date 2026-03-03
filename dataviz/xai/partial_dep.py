"""Partial dependence implementation - static and interactive versions."""

from typing import Optional
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from ..utils import setup_plot, apply_theme


def partial_dependence_static(
    feature_values: np.ndarray,
    predictions: np.ndarray,
    feature_name: str = "Feature",
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: str = "Prediction",
    figsize: tuple = (10, 6),
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
    confidence_interval: Optional[np.ndarray] = None,
    confidence_alpha: float = 0.2,
    theme: str = 'default',
    style: str = 'default',
    grid: bool = True,
    grid_alpha: float = 0.3,
    **kwargs
) -> plt.Axes:
    """
    Create a static partial dependence plot using matplotlib.

    Parameters
    ----------
    feature_values : array
        Values of the feature
    predictions : array
        Predicted values/probabilities
    feature_name : str, default "Feature"
        Name of the feature
    title : str, optional
        Chart title (auto-generated if None)
    xlabel : str, optional
        X-axis label (defaults to feature_name)
    ylabel : str, default "Prediction"
        Y-axis label
    figsize : tuple, default (10, 6)
        Figure size (width, height)
    dpi : int, default 100
        Figure DPI
    color : str, default 'steelblue'
        Line color
    marker : str, default 'o'
        Marker style
    marker_size : int, default 6
        Marker size
    linewidth : float, default 2.0
        Line width
    linestyle : str, default '-'
        Line style
    alpha : float, default 0.7
        Line transparency
    font_size : int, default 10
        Base font size
    title_size : int, default 14
        Title font size
    label_size : int, default 11
        Axis label font size
    show_rugs : bool, default False
        Show rug marks
    show_confidence : bool, default False
        Show confidence interval
    confidence_interval : array, optional
        Confidence interval bounds
    confidence_alpha : float, default 0.2
        Confidence band transparency
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
    feature_values: np.ndarray,
    predictions: np.ndarray,
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
    confidence_interval: Optional[np.ndarray] = None,
    confidence_alpha: float = 0.2,
    hovermode: str = 'closest',
    template: str = 'plotly',
    **kwargs
) -> go.Figure:
    """
    Create an interactive partial dependence plot using plotly.

    Parameters
    ----------
    feature_values : array
        Values of the feature
    predictions : array
        Predicted values/probabilities
    feature_name : str, default "Feature"
        Name of the feature
    title : str, optional
        Chart title (auto-generated if None)
    xlabel : str, optional
        X-axis label (defaults to feature_name)
    ylabel : str, default "Prediction"
        Y-axis label
    height : int, default 500
        Figure height
    width : int, default 800
        Figure width
    color : str, default 'steelblue'
        Line color
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
    show_rugs : bool, default False
        Show rug marks
    show_confidence : bool, default False
        Show confidence interval
    confidence_interval : array, optional
        Confidence interval bounds
    confidence_alpha : float, default 0.2
        Confidence band transparency
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
