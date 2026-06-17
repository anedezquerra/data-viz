"""Confusion matrix implementation - static and interactive versions."""

from typing import Optional, Tuple
from ..types import FigureSize, Labels, MatplotlibAxes, MatrixLike, PlotlyFigure
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from ..utils import setup_plot, apply_theme


def confusion_matrix_plot_static(
    cm: MatrixLike,
    labels: Optional[Labels] = None,
    title: Optional[str] = None,
    figsize: FigureSize = (8, 6),
    cmap: str = 'Blues',
    annot: bool = True,
    fmt: str = 'd',
    cbar: bool = True,
    linewidths: float = 0.5,
    linecolor: str = 'gray',
    theme: str = 'default',
    font_size: int = 10,
    title_size: int = 14,
    label_size: int = 11,
    dpi: int = 100,
    style: str = 'default',
    **kwargs
) -> MatplotlibAxes:
    """Create a static visualization of a classification confusion matrix.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        cm (MatrixLike): Confusion matrix values arranged as actual classes by predicted classes.
        labels (Optional[Labels]): Class, feature, sample, or cluster labels shown on the chart. Defaults to ``None``.
        title (Optional[str]): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``None``.
        figsize (FigureSize): Matplotlib figure size as ``(width, height)`` in inches. Defaults to ``(8, 6)``.
        cmap (str): Configuration value for ``cmap``. Defaults to ``'Blues'``.
        annot (bool): Configuration value for ``annot``. Defaults to ``True``.
        fmt (str): Configuration value for ``fmt``. Defaults to ``'d'``.
        cbar (bool): Configuration value for ``cbar``. Defaults to ``True``.
        linewidths (float): Configuration value for ``linewidths``. Defaults to ``0.5``.
        linecolor (str): Configuration value for ``linecolor``. Defaults to ``'gray'``.
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
        result = dv.confusion_matrix_plot_static(cm)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
    """
    if title is None:
        title = "Confusion Matrix"
    
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, figsize=figsize)
        fig.set_dpi(dpi)
        
        im = ax.imshow(cm, cmap=cmap, aspect='auto')
        
        n_classes = len(cm)
        if labels is None:
            labels = [f'Class {i}' for i in range(n_classes)]
        
        ax.set_xticks(range(n_classes))
        ax.set_yticks(range(n_classes))
        ax.set_xticklabels(labels, fontsize=label_size)
        ax.set_yticklabels(labels, fontsize=label_size)
        ax.set_xlabel('Predicted', fontsize=label_size)
        ax.set_ylabel('Actual', fontsize=label_size)
        ax.title.set_fontsize(title_size)
        ax.tick_params(labelsize=font_size)
        
        # Add text annotations
        if annot:
            for i in range(n_classes):
                for j in range(n_classes):
                    text = ax.text(j, i, format(cm[i, j], fmt), ha='center', va='center', 
                                  color='white' if cm[i, j] > cm.max() / 2 else 'black',
                                  fontsize=font_size)
        
        # Add grid
        ax.set_xticks(np.arange(n_classes) - 0.5, minor=True)
        ax.set_yticks(np.arange(n_classes) - 0.5, minor=True)
        ax.grid(which="minor", color=linecolor, linestyle="-", linewidth=linewidths)
        
        # Colorbar
        if cbar:
            cbar = plt.colorbar(im, ax=ax)
            cbar.ax.tick_params(labelsize=font_size)
        
        # Theme
        if theme == 'dark':
            ax.set_facecolor('#f0f0f0')
        elif theme == 'minimal':
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
    
    return ax


def confusion_matrix_plot_interactive(
    cm: MatrixLike,
    labels: Optional[Labels] = None,
    title: Optional[str] = None,
    colorscale: str = 'Blues',
    showscale: bool = True,
    annot: bool = True,
    hovermode: str = 'closest',
    template: str = 'plotly',
    font_size: int = 12,
    title_size: int = 16,
    height: int = 600,
    width: int = 700,
    **kwargs
) -> PlotlyFigure:
    """Create an interactive visualization of a classification confusion matrix.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        cm (MatrixLike): Confusion matrix values arranged as actual classes by predicted classes.
        labels (Optional[Labels]): Class, feature, sample, or cluster labels shown on the chart. Defaults to ``None``.
        title (Optional[str]): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``None``.
        colorscale (str): Configuration value for ``colorscale``. Defaults to ``'Blues'``.
        showscale (bool): Configuration value for ``showscale``. Defaults to ``True``.
        annot (bool): Configuration value for ``annot``. Defaults to ``True``.
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
        result = dv.confusion_matrix_plot_interactive(cm)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
    """
    if title is None:
        title = "Confusion Matrix"
    
    n_classes = len(cm)
    if labels is None:
        labels = [f'Class {i}' for i in range(n_classes)]
    
    # Prepare text annotations
    z_text = None
    if annot:
        z_text = [[str(val) for val in row] for row in cm]
    
    fig = go.Figure(data=go.Heatmap(
        z=cm,
        x=labels,
        y=labels,
        colorscale=colorscale,
        showscale=showscale,
        text=z_text,
        texttemplate="%{text}" if annot else None,
        textfont={"size": font_size},
        **kwargs
    ))
    
    fig.update_layout(
        title=dict(text=title, font=dict(size=title_size)),
        xaxis_title='Predicted',
        yaxis_title='Actual',
        hovermode=hovermode,
        template=template,
        font=dict(size=font_size),
        height=height,
        width=width,
    )
    
    return fig
