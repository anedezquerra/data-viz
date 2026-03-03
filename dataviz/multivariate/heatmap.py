"""Heatmap implementation - static and interactive versions."""

from typing import Optional, Tuple
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from ..utils import setup_plot, apply_theme


def heatmap_static(
    df: pd.DataFrame,
    title: Optional[str] = None,
    figsize: Tuple[int, int] = (12, 8),
    cmap: str = 'viridis',
    annot: bool = True,
    fmt: str = '.2f',
    cbar: bool = True,
    linewidths: float = 0.5,
    linecolor: str = 'gray',
    vmin: Optional[float] = None,
    vmax: Optional[float] = None,
    theme: str = 'default',
    font_size: int = 10,
    title_size: int = 14,
    label_size: int = 11,
    dpi: int = 100,
    style: str = 'default',
    **kwargs
) -> plt.Axes:
    """
    Create a static heatmap using matplotlib.

    Parameters
    ----------
    df : DataFrame
        Input data
    title : str, optional
        Chart title
    figsize : tuple, default (12, 8)
        Figure size (width, height)
    cmap : str, default 'viridis'
        Colormap name
    annot : bool, default True
        Show annotations (values)
    fmt : str, default '.2f'
        Annotation format
    cbar : bool, default True
        Show colorbar
    linewidths : float, default 0.5
        Cell border line width
    linecolor : str, default 'gray'
        Cell border color
    vmin : float, optional
        Minimum value for colormap
    vmax : float, optional
        Maximum value for colormap
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
        title = "Heatmap"
    
    with plt.style.context(style):
        fig, ax = setup_plot(title=title, figsize=figsize)
        fig.set_dpi(dpi)
        
        im = ax.imshow(df, cmap=cmap, aspect='auto', vmin=vmin, vmax=vmax)
        
        ax.set_xticks(range(len(df.columns)))
        ax.set_yticks(range(len(df.index)))
        ax.set_xticklabels(df.columns, rotation=45, ha='right', fontsize=label_size)
        ax.set_yticklabels(df.index, fontsize=label_size)
        
        # Add annotations
        if annot:
            for i in range(len(df)):
                for j in range(len(df.columns)):
                    text = ax.text(
                        j, i,
                        format(df.iloc[i, j], fmt),
                        ha="center",
                        va="center",
                        color="black",
                        fontsize=font_size
                    )
        
        # Add grid
        ax.set_xticks(np.arange(len(df.columns)) - 0.5, minor=True)
        ax.set_yticks(np.arange(len(df)) - 0.5, minor=True)
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


def heatmap_interactive(
    df: pd.DataFrame,
    title: Optional[str] = None,
    colorscale: str = 'Viridis',
    showscale: bool = True,
    annot: bool = True,
    hovermode: str = 'closest',
    template: str = 'plotly',
    font_size: int = 12,
    title_size: int = 16,
    height: int = 700,
    width: int = 900,
    **kwargs
) -> go.Figure:
    """
    Create an interactive heatmap using plotly.

    Parameters
    ----------
    df : DataFrame
        Input data
    title : str, optional
        Chart title
    colorscale : str, default 'Viridis'
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
    width : int, default 900
        Figure width in pixels
    **kwargs
        Additional plot arguments

    Returns
    -------
    plotly.graph_objects.Figure
        The interactive figure
    """
    if title is None:
        title = "Heatmap"
    
    # Prepare text annotations
    z_text = None
    if annot:
        z_text = [[f"{val:.2f}" for val in row] for row in df.values]
    
    fig = go.Figure(data=go.Heatmap(
        z=df.values,
        x=df.columns,
        y=df.index,
        colorscale=colorscale,
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
