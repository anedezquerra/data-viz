"""Automatic univariate profiling and type-aware visual dispatch."""

from dataclasses import dataclass
from typing import Dict, Optional

import pandas as pd

from ..types import PlotlyFigure, SeriesLike
from .accessors import UnivariateInput, infer_univariate_kind, resolve_univariate_data
from .categorical import frequency_bar_interactive
from .dashboard import univariate_analysis_dashboard_interactive
from .datetime import event_frequency_plot_interactive
from .quality import DataQualitySummary, data_quality_summary
from .stats import UnivariateStats, univariate_summary
from .text import BooleanSummary, boolean_bar_interactive, boolean_summary, top_terms_bar_interactive


@dataclass(frozen=True)
class UnivariateProfile:
    """Automatic univariate profile.

    Args:
        name (str): Variable name.
        kind (str): Inferred variable kind.
        quality (DataQualitySummary): Data quality summary.
        summary (Dict[str, object]): Type-specific summary payload.

    Returns:
        UnivariateProfile: Immutable automatic profile.

    Raises:
        TypeError: If fields cannot be represented by declared types.
        ValueError: If profile values are inconsistent.

    Examples:
        ```python
        profile = UnivariateProfile("sales", "numeric", quality, {"stats": stats})
        ```

    Notes:
        The summary payload intentionally stays dictionary-based for mixed variable kinds.
    """

    name: str
    kind: str
    quality: DataQualitySummary
    summary: Dict[str, object]


def auto_profile(value: SeriesLike, data: Optional[pd.DataFrame] = None, name: str = "Value") -> UnivariateProfile:
    """Create an automatic type-aware profile for one variable.

    Args:
        value (SeriesLike): Series-like values or a dataframe column name.
        data (Optional[pandas.DataFrame]): Optional dataframe for column-name lookup.
        name (str): Fallback name for unnamed arrays.

    Returns:
        UnivariateProfile: Quality metrics and type-specific summary information.

    Raises:
        TypeError: If input data cannot be resolved.
        ValueError: If no observations remain.

    Examples:
        ```python
        profile = auto_profile("sales", data=df)
        ```

    Notes:
        Numeric variables include descriptive statistics; boolean variables include true-rate summary.
    """
    resolved = resolve_univariate_data(value, data=data, fallback_name=name, na_policy="keep")
    quality = data_quality_summary(resolved.values)
    cleaned = resolved.values.dropna()
    kind = infer_univariate_kind(cleaned)
    summary: Dict[str, object]
    if kind == "numeric":
        summary = {"stats": univariate_summary(cleaned)}
    elif kind == "boolean":
        summary = {"boolean": boolean_summary(cleaned)}
    elif kind == "datetime":
        summary = {"start": cleaned.min(), "end": cleaned.max(), "count": int(cleaned.count())}
    elif kind == "text":
        summary = {"count": int(cleaned.count()), "unique": int(cleaned.nunique())}
    else:
        counts = cleaned.value_counts()
        summary = {"counts": counts}
    return UnivariateProfile(name=resolved.name, kind=kind, quality=quality, summary=summary)


def auto_profile_chart_interactive(
    value: SeriesLike,
    data: Optional[pd.DataFrame] = None,
    name: str = "Value",
    title: Optional[str] = None,
) -> PlotlyFigure:
    """Create an interactive chart selected from inferred variable type.

    Args:
        value (SeriesLike): Series-like values or a dataframe column name.
        data (Optional[pandas.DataFrame]): Optional dataframe for column-name lookup.
        name (str): Fallback name for unnamed arrays.
        title (Optional[str]): Optional chart title.

    Returns:
        plotly.graph_objects.Figure: Type-appropriate interactive profile chart.

    Raises:
        TypeError: If input data cannot be resolved.
        ValueError: If no observations remain or a chart cannot be selected.

    Examples:
        ```python
        fig = auto_profile_chart_interactive("sales", data=df)
        ```

    Notes:
        Numeric values use the univariate dashboard; categorical values use a frequency bar.
    """
    resolved: UnivariateInput = resolve_univariate_data(value, data=data, fallback_name=name)
    kind = infer_univariate_kind(resolved.values)
    if kind == "numeric":
        return univariate_analysis_dashboard_interactive(resolved.values, title=title or f"{resolved.name} Profile")
    if kind == "boolean":
        return boolean_bar_interactive(resolved.values, title=title or f"{resolved.name} Boolean Profile")
    if kind == "datetime":
        return event_frequency_plot_interactive(resolved.values, title=title or f"{resolved.name} Event Profile")
    if kind == "text":
        return top_terms_bar_interactive(resolved.values, title=title or f"{resolved.name} Top Terms")
    return frequency_bar_interactive(resolved.values, title=title or f"{resolved.name} Frequency")

