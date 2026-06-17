"""Univariate transformation helpers and comparison plots."""

from dataclasses import dataclass
from typing import Dict, Literal, Optional

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy import stats

from ..types import FigureSize, MatplotlibFigure, PlotlyFigure, SeriesLike
from ..utils import validate_positive_int
from .stats import as_numeric_series

TransformMethod = Literal["identity", "log", "sqrt", "boxcox", "yeojohnson"]


@dataclass(frozen=True)
class TransformResult:
    """Transformed univariate data and transformation metadata.

    Args:
        values (pandas.Series): Transformed observations.
        method (str): Transformation method name.
        parameter (Optional[float]): Fitted transformation parameter when applicable.

    Returns:
        TransformResult: Immutable transformation result.

    Raises:
        TypeError: If values cannot be represented by the declared fields.
        ValueError: If transformation metadata is invalid.

    Examples:
        ```python
        result = TransformResult(pd.Series([0.0, 1.0]), "log", None)
        ```

    Notes:
        Box-Cox and Yeo-Johnson parameters are estimated by SciPy.
    """

    values: pd.Series
    method: str
    parameter: Optional[float]


def transform_series(data: SeriesLike, method: TransformMethod = "identity") -> TransformResult:
    """Transform a numeric series with a common univariate transformation.

    Args:
        data (SeriesLike): Input observations.
        method (TransformMethod): Transformation method.

    Returns:
        TransformResult: Transformed values and fitted parameter metadata.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If the method is unsupported or data violates transformation constraints.

    Examples:
        ```python
        transformed = transform_series(data, method="yeojohnson")
        ```

    Notes:
        ``log`` and ``sqrt`` require non-negative-compatible values; Box-Cox requires strictly positive data.
    """
    values = as_numeric_series(data)
    if method == "identity":
        return TransformResult(values=values.copy(), method=method, parameter=None)
    if method == "log":
        if (values < 0).any():
            raise ValueError("log transformation requires non-negative values.")
        return TransformResult(values=pd.Series(np.log1p(values), name=f"log_{values.name}"), method=method, parameter=None)
    if method == "sqrt":
        if (values < 0).any():
            raise ValueError("sqrt transformation requires non-negative values.")
        return TransformResult(values=pd.Series(np.sqrt(values), name=f"sqrt_{values.name}"), method=method, parameter=None)
    if method == "boxcox":
        if (values <= 0).any():
            raise ValueError("Box-Cox transformation requires strictly positive values.")
        transformed, parameter = stats.boxcox(values.to_numpy(dtype=float))
        return TransformResult(values=pd.Series(transformed, name=f"boxcox_{values.name}"), method=method, parameter=float(parameter))
    if method == "yeojohnson":
        transformed, parameter = stats.yeojohnson(values.to_numpy(dtype=float))
        return TransformResult(values=pd.Series(transformed, name=f"yeojohnson_{values.name}"), method=method, parameter=float(parameter))
    raise ValueError("method must be one of 'identity', 'log', 'sqrt', 'boxcox', or 'yeojohnson'.")


def transformation_summary(data: SeriesLike) -> pd.DataFrame:
    """Summarize skewness and kurtosis across common transformations.

    Args:
        data (SeriesLike): Input observations.

    Returns:
        pandas.DataFrame: Transformation method, parameter, skewness, kurtosis, and standard deviation.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If no transformations can be computed.

    Examples:
        ```python
        table = transformation_summary(data)
        ```

    Notes:
        Invalid transformations for the input range are skipped rather than failing the entire summary.
    """
    rows = []
    for method in ("identity", "log", "sqrt", "boxcox", "yeojohnson"):
        try:
            result = transform_series(data, method=method)  # type: ignore[arg-type]
        except ValueError:
            continue
        values = result.values
        rows.append(
            {
                "method": method,
                "parameter": result.parameter,
                "skewness": float(values.skew()) if len(values) > 2 else 0.0,
                "kurtosis": float(values.kurt()) if len(values) > 3 else 0.0,
                "std": float(values.std(ddof=1)) if len(values) > 1 else 0.0,
            }
        )
    if not rows:
        raise ValueError("No transformations could be computed for the input data.")
    return pd.DataFrame(rows)


def transformation_comparison_static(
    data: SeriesLike,
    bins: int = 25,
    title: Optional[str] = None,
    figsize: FigureSize = (12, 8),
    color: Optional[str] = None,
) -> MatplotlibFigure:
    """Create a static histogram grid comparing common transformations.

    Args:
        data (SeriesLike): Input observations.
        bins (int): Number of histogram bins in each panel.
        title (Optional[str]): Optional figure title.
        figsize (FigureSize): Matplotlib figure size.
        color (Optional[str]): Histogram color.

    Returns:
        matplotlib.figure.Figure: Figure containing transformation histograms.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If ``bins`` is invalid or no transformations can be computed.

    Examples:
        ```python
        fig = transformation_comparison_static(data)
        ```

    Notes:
        Invalid transformations for the input range are skipped.
    """
    validate_positive_int(bins, "bins")
    transformed: Dict[str, TransformResult] = {}
    for method in ("identity", "log", "sqrt", "boxcox", "yeojohnson"):
        try:
            transformed[method] = transform_series(data, method=method)  # type: ignore[arg-type]
        except ValueError:
            continue
    if not transformed:
        raise ValueError("No transformations could be computed for the input data.")
    fig, axes = plt.subplots(1, len(transformed), figsize=figsize)
    if not isinstance(axes, np.ndarray):
        axes = np.asarray([axes])
    fig.suptitle(title or "Transformation Comparison")
    for ax, (method, result) in zip(axes, transformed.items()):
        ax.hist(result.values, bins=bins, color=color, alpha=0.7, edgecolor="black")
        ax.set_title(method)
        ax.grid(True, axis="y", alpha=0.3)
    fig.tight_layout()
    return fig


def transformation_comparison_interactive(
    data: SeriesLike,
    bins: int = 25,
    title: Optional[str] = None,
    color: Optional[str] = None,
    template: str = "plotly",
    height: int = 700,
    width: int = 1100,
) -> PlotlyFigure:
    """Create an interactive histogram grid comparing common transformations.

    Args:
        data (SeriesLike): Input observations.
        bins (int): Number of histogram bins in each panel.
        title (Optional[str]): Optional figure title.
        color (Optional[str]): Histogram color.
        template (str): Plotly template name.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.

    Returns:
        plotly.graph_objects.Figure: Interactive transformation comparison figure.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If ``bins`` is invalid or no transformations can be computed.

    Examples:
        ```python
        fig = transformation_comparison_interactive(data)
        ```

    Notes:
        Each subplot uses the same bin count for quick visual comparison.
    """
    validate_positive_int(bins, "bins")
    transformed: Dict[str, TransformResult] = {}
    for method in ("identity", "log", "sqrt", "boxcox", "yeojohnson"):
        try:
            transformed[method] = transform_series(data, method=method)  # type: ignore[arg-type]
        except ValueError:
            continue
    if not transformed:
        raise ValueError("No transformations could be computed for the input data.")
    fig = make_subplots(rows=1, cols=len(transformed), subplot_titles=list(transformed.keys()))
    for index, result in enumerate(transformed.values(), start=1):
        fig.add_trace(go.Histogram(x=result.values, nbinsx=bins, marker_color=color, showlegend=False), row=1, col=index)
    fig.update_layout(title=title or "Transformation Comparison", template=template, height=height, width=width)
    return fig

