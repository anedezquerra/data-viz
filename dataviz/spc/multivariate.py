"""Multivariate SPC monitoring charts."""

from dataclasses import dataclass
from typing import Optional, Tuple

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objects as go

from ..types import FigureSize, MatplotlibAxes, MatrixLike, PlotlyFigure
from ..utils import apply_theme, setup_plot


@dataclass(frozen=True)
class HotellingT2Result:
    """Hotelling T-squared monitoring result.

    Args:
        scores (pd.Series): T-squared score for each observation.
        center (pd.Series): Multivariate process center.
        covariance (pd.DataFrame): Sample covariance matrix.
        limit (float): Empirical control limit.

    Returns:
        HotellingT2Result: Immutable multivariate SPC result.

    Raises:
        TypeError: If inputs cannot be represented as numeric matrices.
        ValueError: If covariance cannot be estimated.

    Examples:
        ```python
        result = dv.spc.hotelling_t2_summary(df)
        ```

    Notes:
        The default limit is empirical and percentile-based to avoid a SciPy dependency.
    """

    scores: pd.Series
    center: pd.Series
    covariance: pd.DataFrame
    limit: float


def _numeric_matrix(data: MatrixLike) -> pd.DataFrame:
    """Convert matrix-like data to a numeric dataframe.

    Args:
        data (MatrixLike): Multivariate process observations.

    Returns:
        pandas.DataFrame: Numeric dataframe with complete observations.

    Raises:
        TypeError: If data cannot be converted to a numeric dataframe.
        ValueError: If fewer than two variables or observations remain.

    Examples:
        ```python
        frame = _numeric_matrix(data)
        ```

    Notes:
        Rows are observations and columns are monitored variables.
    """
    frame = data.copy() if isinstance(data, pd.DataFrame) else pd.DataFrame(data)
    frame = frame.apply(pd.to_numeric, errors="raise").dropna()
    if frame.shape[0] < 2 or frame.shape[1] < 2:
        raise ValueError("At least two complete observations and two variables are required.")
    return frame.reset_index(drop=True)


def hotelling_t2_summary(data: MatrixLike, limit_quantile: float = 0.99) -> HotellingT2Result:
    """Compute Hotelling T-squared scores for multivariate process data.

    Args:
        data (MatrixLike): Multivariate process observations.
        limit_quantile (float): Empirical quantile used as the control limit.

    Returns:
        HotellingT2Result: T-squared scores, center, covariance, and control limit.

    Raises:
        TypeError: If data cannot be converted to a numeric dataframe.
        ValueError: If quantile is invalid or covariance is singular.

    Examples:
        ```python
        result = dv.spc.hotelling_t2_summary(df, limit_quantile=0.995)
        ```

    Notes:
        A pseudo-inverse is used for numerical stability when variables are highly correlated.
    """
    if limit_quantile <= 0 or limit_quantile >= 1:
        raise ValueError("limit_quantile must be between 0 and 1.")
    frame = _numeric_matrix(data)
    center = frame.mean()
    covariance = frame.cov()
    inverse = np.linalg.pinv(covariance.to_numpy())
    centered = frame - center
    scores = np.einsum("ij,jk,ik->i", centered.to_numpy(), inverse, centered.to_numpy())
    score_series = pd.Series(scores, name="T2")
    return HotellingT2Result(scores=score_series, center=center, covariance=covariance, limit=float(score_series.quantile(limit_quantile)))


def hotelling_t2_chart_static(
    data: MatrixLike,
    limit_quantile: float = 0.99,
    title: str = "Hotelling T-squared Chart",
    figsize: FigureSize = (12, 6),
    theme: str = "default",
) -> MatplotlibAxes:
    """Create a static Hotelling T-squared control chart.

    Args:
        data (MatrixLike): Multivariate process observations.
        limit_quantile (float): Empirical quantile used as the control limit.
        title (str): Chart title.
        figsize (FigureSize): Figure size in inches.
        theme (str): Named style theme.

    Returns:
        matplotlib.axes.Axes: Hotelling T-squared chart axes.

    Raises:
        TypeError: If data cannot be converted to a numeric dataframe.
        ValueError: If quantile is invalid or covariance cannot be estimated.

    Examples:
        ```python
        ax = dv.spc.hotelling_t2_chart_static(df)
        ```

    Notes:
        Points above the empirical limit deserve investigation.
    """
    result = hotelling_t2_summary(data, limit_quantile=limit_quantile)
    _, ax = setup_plot(figsize=figsize, title=title, xlabel="Observation", ylabel="T-squared")
    ax.plot(result.scores, marker="o", color="steelblue", label="T-squared")
    ax.axhline(result.limit, color="red", linestyle="--", label=f"{limit_quantile:.1%} limit")
    ax.legend()
    apply_theme(ax, theme)
    return ax


def hotelling_t2_chart_interactive(
    data: MatrixLike,
    limit_quantile: float = 0.99,
    title: str = "Hotelling T-squared Chart",
    template: str = "plotly",
    height: int = 500,
    width: int = 1000,
) -> PlotlyFigure:
    """Create an interactive Hotelling T-squared control chart.

    Args:
        data (MatrixLike): Multivariate process observations.
        limit_quantile (float): Empirical quantile used as the control limit.
        title (str): Chart title.
        template (str): Plotly template.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.

    Returns:
        plotly.graph_objects.Figure: Interactive Hotelling T-squared chart.

    Raises:
        TypeError: If data cannot be converted to a numeric dataframe.
        ValueError: If quantile is invalid or covariance cannot be estimated.

    Examples:
        ```python
        fig = dv.spc.hotelling_t2_chart_interactive(df)
        ```

    Notes:
        The limit is empirical rather than distribution-based to keep dependencies light.
    """
    result = hotelling_t2_summary(data, limit_quantile=limit_quantile)
    fig = go.Figure(data=[go.Scatter(y=result.scores, mode="lines+markers", name="T-squared")])
    fig.add_hline(y=result.limit, line_color="red", line_dash="dash", annotation_text=f"{limit_quantile:.1%} limit")
    fig.update_layout(title=title, xaxis_title="Observation", yaxis_title="T-squared", template=template, height=height, width=width)
    return fig
