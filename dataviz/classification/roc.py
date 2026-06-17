"""ROC curve implementation - static and interactive versions."""

from typing import Optional, Tuple
from ..types import ArrayLike, FigureSize, MatplotlibAxes, PlotlyFigure
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from ..utils import setup_plot, apply_theme


def roc_curve_static(
    fpr: ArrayLike,
    tpr: ArrayLike,
    auc: Optional[float] = None,
    title: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    color: Optional[str] = None,
    linewidth: float = 2.0,
    linestyle: str = '-',
    reference_color: str = 'black',
    reference_linestyle: str = '--',
    reference_linewidth: float = 1.5,
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
    """Create a static receiver operating characteristic curve.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        fpr (ArrayLike): False-positive-rate values for the ROC curve.
        tpr (ArrayLike): True-positive-rate values for the ROC curve.
        auc (Optional[float]): Area under the ROC curve to display in the legend. Defaults to ``None``.
        title (Optional[str]): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``None``.
        figsize (FigureSize): Matplotlib figure size as ``(width, height)`` in inches. Defaults to ``(10, 6)``.
        color (Optional[str]): Configuration value for ``color``. Defaults to ``None``.
        linewidth (float): Configuration value for ``linewidth``. Defaults to ``2.0``.
        linestyle (str): Configuration value for ``linestyle``. Defaults to ``'-'``.
        reference_color (str): Configuration value for ``reference_color``. Defaults to ``'black'``.
        reference_linestyle (str): Configuration value for ``reference_linestyle``. Defaults to ``'--'``.
        reference_linewidth (float): Configuration value for ``reference_linewidth``. Defaults to ``1.5``.
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
        result = dv.roc_curve_static(fpr, tpr)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
    """
    if title is None:
        title = "ROC Curve"
    
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, xlabel='False Positive Rate', ylabel='True Positive Rate', figsize=figsize)
        fig.set_dpi(dpi)
        
        label = 'ROC Curve'
        if auc is not None:
            label += f' (AUC = {auc:.3f})'
        
        ax.plot(fpr, tpr, color=color, linewidth=linewidth, linestyle=linestyle, label=label, **kwargs)
        ax.plot([0, 1], [0, 1], color=reference_color, linestyle=reference_linestyle, linewidth=reference_linewidth, label='Random Classifier')
        
        ax.set_xlim([0.0, 1.0])
        ax.set_ylim([0.0, 1.05])
        
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


def roc_curve_interactive(
    fpr: ArrayLike,
    tpr: ArrayLike,
    auc: Optional[float] = None,
    title: Optional[str] = None,
    color: Optional[str] = None,
    marker_color: Optional[str] = None,
    linewidth: float = 2.0,
    reference_color: str = 'black',
    reference_linestyle: str = 'dash',
    reference_linewidth: float = 1.5,
    showlegend: bool = True,
    hovermode: str = 'closest',
    template: str = 'plotly',
    font_size: int = 12,
    title_size: int = 16,
    height: int = 600,
    width: int = 700,
    **kwargs
) -> PlotlyFigure:
    """Create an interactive receiver operating characteristic curve.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        fpr (ArrayLike): False-positive-rate values for the ROC curve.
        tpr (ArrayLike): True-positive-rate values for the ROC curve.
        auc (Optional[float]): Area under the ROC curve to display in the legend. Defaults to ``None``.
        title (Optional[str]): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``None``.
        color (Optional[str]): Configuration value for ``color``. Defaults to ``None``.
        marker_color (Optional[str]): Configuration value for ``marker_color``. Defaults to ``None``.
        linewidth (float): Configuration value for ``linewidth``. Defaults to ``2.0``.
        reference_color (str): Configuration value for ``reference_color``. Defaults to ``'black'``.
        reference_linestyle (str): Configuration value for ``reference_linestyle``. Defaults to ``'dash'``.
        reference_linewidth (float): Configuration value for ``reference_linewidth``. Defaults to ``1.5``.
        showlegend (bool): Configuration value for ``showlegend``. Defaults to ``True``.
        hovermode (str): Configuration value for ``hovermode``. Defaults to ``'closest'``.
        template (str): Plotly template used to style the interactive figure. Defaults to ``'plotly'``.
        font_size (int): Configuration value for ``font_size``. Defaults to ``12``.
        title_size (int): Configuration value for ``title_size``. Defaults to ``16``.
        height (int): Plotly figure height in pixels. Defaults to ``600``.
        width (int): Plotly figure width in pixels. Defaults to ``700``.
        **kwargs (Any): Additional keyword arguments forwarded to the underlying plotting function.
    
    Returns:
        plotly.graph_objects.Figure: Configured Plotly figure containing the rendered interactive chart.
    
    Raises:
        TypeError: If required inputs are not compatible with the plotting backend.
        ValueError: If input lengths, matrix shapes, or option values are invalid for the requested chart.
    
    Example:
        ```python
        import dataviz as dv
        result = dv.roc_curve_interactive(fpr, tpr)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
    """
    if title is None:
        title = "ROC Curve"
    if color is None:
        color = marker_color
    
    fig = go.Figure()
    
    label = 'ROC Curve'
    if auc is not None:
        label += f' (AUC = {auc:.3f})'
    
    fig.add_trace(go.Scatter(
        x=fpr,
        y=tpr,
        mode='lines',
        name=label,
        line=dict(color=color, width=linewidth),
        **kwargs
    ))
    
    # Random classifier line
    fig.add_trace(go.Scatter(
        x=[0, 1],
        y=[0, 1],
        mode='lines',
        name='Random Classifier',
        line=dict(dash=reference_linestyle, color=reference_color, width=reference_linewidth)
    ))
    
    fig.update_layout(
        title=dict(text=title, font=dict(size=title_size)),
        xaxis_title='False Positive Rate',
        yaxis_title='True Positive Rate',
        xaxis=dict(range=[0, 1]),
        yaxis=dict(range=[0, 1.05]),
        hovermode=hovermode,
        template=template,
        font=dict(size=font_size),
        height=height,
        width=width,
        showlegend=showlegend,
    )
    
    return fig
