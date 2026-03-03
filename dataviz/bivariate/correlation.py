"""Correlation heatmap implementation - static and interactive versions."""

from typing import Optional, Tuple
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from ..utils import setup_plot, apply_theme


def correlation_heatmap_static(
    df: pd.DataFrame,
    title: Optional[str] = None,
    figsize: Tuple[int, int] = (10, 8),
    cmap: str = 'coolwarm',
    annot: bool = True,
    fmt: str = '.2f',
    cbar: bool = True,
    vmin: float = -1.0,
    vmax: float = 1.0,
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
    Create a static correlation heatmap using matplotlib.

    Parameters
    ----------
    df : DataFrame
        Input data
    title : str, optional
        Chart title
    figsize : tuple, default (10, 8)
        Figure size (width, height)
    cmap : str, default 'coolwarm'
        Color map name
    annot : bool, default True
        Show annotations (correlation values)
    fmt : str, default '.2f'
        Annotation format
    cbar : bool, default True
        Show colorbar
    vmin : float, default -1.0
        Minimum colorbar value
    vmax : float, default 1.0
        Maximum colorbar value
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
        Additional heatmap arguments

    Returns
    -------
    matplotlib.axes.Axes
        The plot axes
    """
    if title is None:
        title = "Correlation Heatmap"
    
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, figsize=figsize)
        fig.set_dpi(dpi)
        
        corr_matrix = df.corr()
        
        # Create heatmap using imshow
        im = ax.imshow(
            corr_matrix,
            cmap=cmap,
            aspect='auto',
            vmin=vmin,
            vmax=vmax
        )
        
        # Set ticks and labels
        ax.set_xticks(range(len(corr_matrix.columns)))
        ax.set_yticks(range(len(corr_matrix.columns)))
        ax.set_xticklabels(corr_matrix.columns, rotation=45, ha='right', fontsize=label_size)
        ax.set_yticklabels(corr_matrix.columns, fontsize=label_size)
        
        # Add annotations
        if annot:
            for i in range(len(corr_matrix)):
                for j in range(len(corr_matrix.columns)):
                    text = ax.text(
                        j, i,
                        format(corr_matrix.iloc[i, j], fmt),
                        ha="center",
                        va="center",
                        color="black",
                        fontsize=font_size
                    )
        
        # Add grid
        ax.set_xticks(np.arange(len(corr_matrix.columns)) - 0.5, minor=True)
        ax.set_yticks(np.arange(len(corr_matrix)) - 0.5, minor=True)
        ax.grid(which="minor", color=linecolor, linestyle="-", linewidth=linewidths)
        
        # Colorbar
        if cbar:
            cbar = plt.colorbar(im, ax=ax)
            cbar.ax.tick_params(labelsize=font_size)
        
        # Customize title
        ax.title.set_fontsize(title_size)
        
        # Theme
        if theme == 'dark':
            ax.set_facecolor('#f0f0f0')
        elif theme == 'minimal':
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
    
    return ax


def correlation_heatmap_interactive(
    df: pd.DataFrame,
    title: Optional[str] = None,
    colorscale: str = 'RdBu',
    showscale: bool = True,
    annot: bool = True,
    hovermode: str = 'closest',
    template: str = 'plotly',
    font_size: int = 12,
    title_size: int = 16,
    height: int = 700,
    width: int = 800,
    **kwargs
) -> go.Figure:
    """
    Create an interactive correlation heatmap using plotly.

    Parameters
    ----------
    df : DataFrame
        Input data
    title : str, optional
        Chart title
    colorscale : str, default 'RdBu'
        Plotly colorscale name
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
    height : int, default 700
        Figure height in pixels
    width : int, default 800
        Figure width in pixels
    **kwargs
        Additional plot arguments

    Returns
    -------
    plotly.graph_objects.Figure
        The interactive figure
    """
    if title is None:
        title = "Correlation Heatmap"
    
    corr_matrix = df.corr()
    
    # Prepare text annotations
    z_text = None
    if annot:
        z_text = [[f"{val:.2f}" for val in row] for row in corr_matrix.values]
    
    fig = go.Figure(data=go.Heatmap(
        z=corr_matrix.values,
        x=corr_matrix.columns,
        y=corr_matrix.index,
        colorscale=colorscale,
        zmid=0,
        showscale=showscale,
        text=z_text,
        texttemplate="%{text}" if annot else None,
        textfont={"size": font_size},
        **kwargs
    ))
    
    fig.update_layout(
        title=dict(text=title, font=dict(size=title_size)),
        hovermode=hovermode,
        template=template,
        font=dict(size=font_size),
        height=height,
        width=width,
    )
    
    return fig
