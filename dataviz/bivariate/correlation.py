"""Correlation heatmap implementation - static and interactive versions."""

from typing import Iterable, Literal, Optional, Tuple, Union

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objects as go

from ..types import FigureSize, MatplotlibAxes, PlotlyFigure
from ..utils import apply_theme, numeric_dataframe, setup_plot, validate_positive_int

CorrelationMethod = Literal["pearson", "kendall", "spearman"]


def _correlation_matrix(
    df: pd.DataFrame,
    columns: Optional[Iterable[str]],
    method: CorrelationMethod,
    min_periods: int,
    absolute: bool,
    mask_upper: bool,
) -> pd.DataFrame:
    """Compute a validated correlation matrix.

    Args:
        df (pd.DataFrame): Input dataframe.
        columns (Optional[Iterable[str]]): Optional numeric column subset.
        method (CorrelationMethod): Correlation method.
        min_periods (int): Minimum observations required per pair.
        absolute (bool): Whether to use absolute correlations.
        mask_upper (bool): Whether to mask the upper triangle.

    Returns:
        pandas.DataFrame: Computed correlation matrix.

    Raises:
        TypeError: If ``df`` is not a dataframe.
        ValueError: If there are too few numeric columns or invalid options.

    Example:
        ```python
        corr = _correlation_matrix(df, None, "pearson", 1, False, True)
        ```

    Notes:
        This helper is shared by static and interactive heatmaps.
    """
    validate_positive_int(min_periods, "min_periods")
    numeric = numeric_dataframe(df, columns=columns, min_columns=2)
    corr = numeric.corr(method=method, min_periods=min_periods)
    if absolute:
        corr = corr.abs()
    if mask_upper:
        mask = np.triu(np.ones(corr.shape, dtype=bool), k=1)
        corr = corr.mask(mask)
    return corr


def correlation_heatmap_static(
    df: pd.DataFrame,
    title: Optional[str] = None,
    figsize: FigureSize = (10, 8),
    cmap: str = "coolwarm",
    annot: bool = True,
    fmt: str = ".2f",
    cbar: bool = True,
    vmin: Optional[float] = -1.0,
    vmax: Optional[float] = 1.0,
    linewidths: float = 0.5,
    linecolor: str = "gray",
    theme: str = "default",
    font_size: int = 10,
    title_size: int = 14,
    label_size: int = 11,
    dpi: int = 100,
    style: str = "default",
    columns: Optional[Iterable[str]] = None,
    method: CorrelationMethod = "pearson",
    min_periods: int = 1,
    mask_upper: bool = False,
    absolute: bool = False,
    ax: Optional[MatplotlibAxes] = None,
    return_corr: bool = False,
    **kwargs,
) -> Union[MatplotlibAxes, Tuple[MatplotlibAxes, pd.DataFrame]]:
    """Create a static heatmap of pairwise correlations between dataframe columns.

    Args:
        df (pd.DataFrame): Input dataframe containing variables to correlate.
        title (Optional[str]): Chart title. Defaults to a generated title.
        figsize (FigureSize): Matplotlib figure size in inches.
        cmap (str): Matplotlib colormap.
        annot (bool): Whether to annotate cells with correlation values.
        fmt (str): Format string used for annotations.
        cbar (bool): Whether to draw a colorbar.
        vmin (Optional[float]): Minimum color scale value.
        vmax (Optional[float]): Maximum color scale value.
        linewidths (float): Grid line width between heatmap cells.
        linecolor (str): Grid line color.
        theme (str): Named style theme.
        font_size (int): Annotation and colorbar font size.
        title_size (int): Title font size.
        label_size (int): Axis-label font size.
        dpi (int): Figure DPI when a new figure is created.
        style (str): Matplotlib style context.
        columns (Optional[Iterable[str]]): Optional column subset to include.
        method (CorrelationMethod): Correlation method: ``"pearson"``, ``"kendall"``, or ``"spearman"``.
        min_periods (int): Minimum observations required per column pair.
        mask_upper (bool): Whether to hide the upper triangle.
        absolute (bool): Whether to plot absolute correlation values.
        ax (Optional[MatplotlibAxes]): Existing axes to draw into.
        return_corr (bool): Whether to return the computed matrix with the axes.
        **kwargs: Additional keyword arguments forwarded to ``Axes.imshow``.

    Returns:
        Union[matplotlib.axes.Axes, Tuple[matplotlib.axes.Axes, pandas.DataFrame]]: Heatmap axes, optionally with correlation matrix.

    Raises:
        TypeError: If ``df`` is not a dataframe.
        ValueError: If columns are missing, too few numeric columns exist, or options are invalid.

    Example:
        ```python
        ax, corr = dv.correlation_heatmap_static(df, method="spearman", return_corr=True)
        ```

    Notes:
        Non-numeric columns are ignored after any explicit column selection.
    """
    title = title or f"{method.title()} Correlation Heatmap"
    corr_matrix = _correlation_matrix(df, columns, method, min_periods, absolute, mask_upper)
    if absolute and vmin == -1.0:
        vmin = 0.0

    with plt.style.context(style):
        if ax is None:
            fig, ax = setup_plot(title=title, figsize=figsize)
            fig.set_dpi(dpi)
        else:
            ax.set_title(title)

        im = ax.imshow(corr_matrix.values, cmap=cmap, aspect="auto", vmin=vmin, vmax=vmax, **kwargs)
        ax.set_xticks(range(len(corr_matrix.columns)))
        ax.set_yticks(range(len(corr_matrix.index)))
        ax.set_xticklabels(corr_matrix.columns, rotation=45, ha="right", fontsize=label_size)
        ax.set_yticklabels(corr_matrix.index, fontsize=label_size)

        if annot:
            for i in range(len(corr_matrix.index)):
                for j in range(len(corr_matrix.columns)):
                    value = corr_matrix.iloc[i, j]
                    if not pd.isna(value):
                        ax.text(j, i, format(value, fmt), ha="center", va="center", color="black", fontsize=font_size)

        ax.set_xticks(np.arange(len(corr_matrix.columns)) - 0.5, minor=True)
        ax.set_yticks(np.arange(len(corr_matrix.index)) - 0.5, minor=True)
        ax.grid(which="minor", color=linecolor, linestyle="-", linewidth=linewidths)
        if cbar:
            colorbar = plt.colorbar(im, ax=ax)
            colorbar.ax.tick_params(labelsize=font_size)
        ax.title.set_fontsize(title_size)
        apply_theme(ax, theme)
        if return_corr:
            return ax, corr_matrix
        return ax


def correlation_heatmap_interactive(
    df: pd.DataFrame,
    title: Optional[str] = None,
    colorscale: str = "RdBu",
    showscale: bool = True,
    annot: bool = True,
    hovermode: str = "closest",
    template: str = "plotly",
    font_size: int = 12,
    title_size: int = 16,
    height: int = 700,
    width: int = 800,
    columns: Optional[Iterable[str]] = None,
    method: CorrelationMethod = "pearson",
    min_periods: int = 1,
    mask_upper: bool = False,
    absolute: bool = False,
    return_corr: bool = False,
    **kwargs,
) -> Union[PlotlyFigure, Tuple[PlotlyFigure, pd.DataFrame]]:
    """Create an interactive heatmap of pairwise correlations between dataframe columns.

    Args:
        df (pd.DataFrame): Input dataframe containing variables to correlate.
        title (Optional[str]): Chart title. Defaults to a generated title.
        colorscale (str): Plotly colorscale.
        showscale (bool): Whether to show the color scale.
        annot (bool): Whether to annotate cells with correlation values.
        hovermode (str): Plotly hover mode.
        template (str): Plotly template.
        font_size (int): Base font size.
        title_size (int): Title font size.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.
        columns (Optional[Iterable[str]]): Optional column subset to include.
        method (CorrelationMethod): Correlation method: ``"pearson"``, ``"kendall"``, or ``"spearman"``.
        min_periods (int): Minimum observations required per column pair.
        mask_upper (bool): Whether to hide the upper triangle.
        absolute (bool): Whether to plot absolute correlation values.
        return_corr (bool): Whether to return the computed matrix with the figure.
        **kwargs: Additional keyword arguments forwarded to ``go.Heatmap``.

    Returns:
        Union[plotly.graph_objects.Figure, Tuple[plotly.graph_objects.Figure, pandas.DataFrame]]: Heatmap figure, optionally with correlation matrix.

    Raises:
        TypeError: If ``df`` is not a dataframe.
        ValueError: If columns are missing, too few numeric columns exist, or options are invalid.

    Example:
        ```python
        fig = dv.correlation_heatmap_interactive(df, columns=["a", "b", "c"])
        ```

    Notes:
        Masked cells are represented as missing values in the heatmap.
    """
    title = title or f"{method.title()} Correlation Heatmap"
    corr_matrix = _correlation_matrix(df, columns, method, min_periods, absolute, mask_upper)
    z_text = None
    if annot:
        z_text = [[None if pd.isna(value) else f"{value:.2f}" for value in row] for row in corr_matrix.values]

    fig = go.Figure(
        data=go.Heatmap(
            z=corr_matrix.values,
            x=corr_matrix.columns,
            y=corr_matrix.index,
            colorscale=colorscale,
            zmid=None if absolute else 0,
            showscale=showscale,
            text=z_text,
            texttemplate="%{text}" if annot else None,
            textfont={"size": font_size},
            **kwargs,
        )
    )
    fig.update_layout(
        title=dict(text=title, font=dict(size=title_size)),
        hovermode=hovermode,
        template=template,
        font=dict(size=font_size),
        height=height,
        width=width,
    )
    if return_corr:
        return fig, corr_matrix
    return fig
