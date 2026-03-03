"""Confusion matrix implementation - static and interactive versions."""

from typing import Optional, Tuple
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from ..utils import setup_plot, apply_theme


def confusion_matrix_plot_static(
    cm: np.ndarray,
    labels: Optional[list] = None,
    title: Optional[str] = None,
    figsize: Tuple[int, int] = (8, 6),
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
) -> plt.Axes:
    """
    Create a static confusion matrix using matplotlib.

    Parameters
    ----------
    cm : array
        Confusion matrix
    labels : list, optional
        Class labels
    title : str, optional
        Chart title
    figsize : tuple, default (8, 6)
        Figure size (width, height)
    cmap : str, default 'Blues'
        Colormap name
    annot : bool, default True
        Show annotations
    fmt : str, default 'd'
        Annotation format
    cbar : bool, default True
        Show colorbar
    linewidths : float, default 0.5
        Cell border line width
    linecolor : str, default 'gray'
        Cell border color
    theme : str, default 'default'
        Theme: 'default', 'dark', 'minimal'
    font_size : int, default 10
        Base font size
    title_size : int, default 14
        Title font size
    label_size : int, default 11
        Axis label font size
    dpi : int, default 100
        Figure DPI
    style : str, default 'default'
        Matplotlib style
    **kwargs
        Additional plot arguments

    Returns
    -------
    matplotlib.axes.Axes
        The plot axes
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
    cm: np.ndarray,
    labels: Optional[list] = None,
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
) -> go.Figure:
    """
    Create an interactive confusion matrix using plotly.

    Parameters
    ----------
    cm : array
        Confusion matrix
    labels : list, optional
        Class labels
    title : str, optional
        Chart title
    colorscale : str, default 'Blues'
        Plotly colorscale
    showscale : bool, default True
        Show color scale
    annot : bool, default True
        Show values in cells
    hovermode : str, default 'closest'
        Hover mode type
    template : str, default 'plotly'
        Plotly template
    font_size : int, default 12
        Font size
    title_size : int, default 16
        Title font size
    height : int, default 600
        Figure height in pixels
    width : int, default 700
        Figure width in pixels
    **kwargs
        Additional plot arguments

    Returns
    -------
    plotly.graph_objects.Figure
        The interactive figure
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
