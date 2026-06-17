"""Heatmap implementation - static and interactive versions."""

from typing import Optional, Tuple
from ..types import FigureSize, MatplotlibAxes, PlotlyFigure
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from ..utils import setup_plot, apply_theme


def heatmap_static(
    df: pd.DataFrame,
    title: Optional[str] = None,
    figsize: FigureSize = (12, 8),
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
) -> MatplotlibAxes:
    """Create a static heatmap for matrix-like or dataframe values.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        df (pd.DataFrame): Input dataframe containing the variables to visualize.
        title (Optional[str]): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``None``.
        figsize (FigureSize): Matplotlib figure size as ``(width, height)`` in inches. Defaults to ``(12, 8)``.
        cmap (str): Configuration value for ``cmap``. Defaults to ``'viridis'``.
        annot (bool): Configuration value for ``annot``. Defaults to ``True``.
        fmt (str): Configuration value for ``fmt``. Defaults to ``'.2f'``.
        cbar (bool): Configuration value for ``cbar``. Defaults to ``True``.
        linewidths (float): Configuration value for ``linewidths``. Defaults to ``0.5``.
        linecolor (str): Configuration value for ``linecolor``. Defaults to ``'gray'``.
        vmin (Optional[float]): Configuration value for ``vmin``. Defaults to ``None``.
        vmax (Optional[float]): Configuration value for ``vmax``. Defaults to ``None``.
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
        result = dv.heatmap_static(df)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
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
) -> PlotlyFigure:
    """Create an interactive heatmap for matrix-like or dataframe values.
    
    Builds the visualization with package defaults while allowing backend-specific customization through keyword arguments where supported.
    
    Args:
        df (pd.DataFrame): Input dataframe containing the variables to visualize.
        title (Optional[str]): Optional chart title. When omitted, a descriptive title is generated where possible. Defaults to ``None``.
        colorscale (str): Configuration value for ``colorscale``. Defaults to ``'Viridis'``.
        showscale (bool): Configuration value for ``showscale``. Defaults to ``True``.
        annot (bool): Configuration value for ``annot``. Defaults to ``True``.
        hovermode (str): Configuration value for ``hovermode``. Defaults to ``'closest'``.
        template (str): Plotly template used to style the interactive figure. Defaults to ``'plotly'``.
        font_size (int): Configuration value for ``font_size``. Defaults to ``12``.
        title_size (int): Configuration value for ``title_size``. Defaults to ``16``.
        height (int): Plotly figure height in pixels. Defaults to ``700``.
        width (int): Plotly figure width in pixels. Defaults to ``900``.
        **kwargs (Any): Additional keyword arguments forwarded to the underlying plotting function.
    
    Returns:
        plotly.graph_objects.Figure: Configured Plotly figure containing the rendered interactive chart.
    
    Raises:
        TypeError: If required inputs are not compatible with the plotting backend.
        ValueError: If input lengths, matrix shapes, or option values are invalid for the requested chart.
    
    Example:
        ```python
        import dataviz as dv
        result = dv.heatmap_interactive(df)
        ```
    
    Notes:
        Static functions return matplotlib objects; interactive functions return Plotly figures.
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
