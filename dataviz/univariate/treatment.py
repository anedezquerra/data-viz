"""Outlier treatment and before-after comparison helpers."""

from dataclasses import dataclass
from typing import Literal, Optional

import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go

from ..types import FigureSize, MatplotlibAxes, PlotlyFigure, SeriesLike
from ..utils import apply_theme, setup_plot
from .robust import mad_outliers
from .stats import as_numeric_series, iqr_outliers, zscore_outliers

OutlierRule = Literal["iqr", "zscore", "mad"]


@dataclass(frozen=True)
class OutlierTreatmentResult:
    """Result of an outlier treatment operation.

    Args:
        original (pandas.Series): Cleaned original numeric observations.
        treated (pandas.Series): Treated observations.
        mask (pandas.Series): Boolean outlier mask.
        method (str): Treatment method name.
        rule (str): Outlier detection rule name.

    Returns:
        OutlierTreatmentResult: Immutable outlier treatment result.

    Raises:
        TypeError: If fields cannot be represented by declared types.
        ValueError: If fields are inconsistent.

    Examples:
        ```python
        result = OutlierTreatmentResult(original, treated, mask, "cap", "iqr")
        ```

    Notes:
        The result preserves both original and treated values for auditability.
    """

    original: pd.Series
    treated: pd.Series
    mask: pd.Series
    method: str
    rule: str


def outlier_mask(
    data: SeriesLike,
    rule: OutlierRule = "iqr",
    threshold: float = 3.0,
    multiplier: float = 1.5,
) -> pd.Series:
    """Compute an outlier mask using a named rule.

    Args:
        data (SeriesLike): Input observations.
        rule (OutlierRule): Outlier rule: ``"iqr"``, ``"zscore"``, or ``"mad"``.
        threshold (float): Threshold for z-score or MAD rules.
        multiplier (float): IQR multiplier for Tukey fences.

    Returns:
        pandas.Series: Boolean mask where ``True`` marks outliers.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If the rule or thresholds are invalid.

    Examples:
        ```python
        mask = outlier_mask(values, rule="mad")
        ```

    Notes:
        This helper provides a shared rule interface for cap, remove, and flag workflows.
    """
    if rule == "iqr":
        return iqr_outliers(data, multiplier=multiplier)
    if rule == "zscore":
        return zscore_outliers(data, threshold=threshold)
    if rule == "mad":
        return mad_outliers(data, threshold=threshold)
    raise ValueError("rule must be one of 'iqr', 'zscore', or 'mad'.")


def cap_outliers(
    data: SeriesLike,
    rule: OutlierRule = "iqr",
    threshold: float = 3.0,
    multiplier: float = 1.5,
) -> OutlierTreatmentResult:
    """Cap outliers to non-outlier min and max values.

    Args:
        data (SeriesLike): Input observations.
        rule (OutlierRule): Outlier rule: ``"iqr"``, ``"zscore"``, or ``"mad"``.
        threshold (float): Threshold for z-score or MAD rules.
        multiplier (float): IQR multiplier for Tukey fences.

    Returns:
        OutlierTreatmentResult: Original values, capped values, and mask.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If all observations are outliers or rule options are invalid.

    Examples:
        ```python
        result = cap_outliers(values)
        ```

    Notes:
        Capping preserves sample size while limiting extreme values.
    """
    values = as_numeric_series(data)
    mask = outlier_mask(values, rule=rule, threshold=threshold, multiplier=multiplier)
    if (~mask).sum() == 0:
        raise ValueError("Cannot cap outliers when every observation is flagged.")
    lower = values[~mask].min()
    upper = values[~mask].max()
    treated = values.clip(lower=lower, upper=upper)
    return OutlierTreatmentResult(original=values, treated=treated, mask=mask, method="cap", rule=rule)


def remove_outliers(
    data: SeriesLike,
    rule: OutlierRule = "iqr",
    threshold: float = 3.0,
    multiplier: float = 1.5,
) -> OutlierTreatmentResult:
    """Remove observations flagged as outliers.

    Args:
        data (SeriesLike): Input observations.
        rule (OutlierRule): Outlier rule: ``"iqr"``, ``"zscore"``, or ``"mad"``.
        threshold (float): Threshold for z-score or MAD rules.
        multiplier (float): IQR multiplier for Tukey fences.

    Returns:
        OutlierTreatmentResult: Original values, retained values, and mask.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If all observations are removed or rule options are invalid.

    Examples:
        ```python
        result = remove_outliers(values)
        ```

    Notes:
        Removal changes sample size and should be used with care.
    """
    values = as_numeric_series(data)
    mask = outlier_mask(values, rule=rule, threshold=threshold, multiplier=multiplier)
    treated = values[~mask].reset_index(drop=True)
    if treated.empty:
        raise ValueError("Cannot remove outliers because no observations would remain.")
    return OutlierTreatmentResult(original=values, treated=treated, mask=mask, method="remove", rule=rule)


def flag_outliers(
    data: SeriesLike,
    rule: OutlierRule = "iqr",
    threshold: float = 3.0,
    multiplier: float = 1.5,
) -> pd.DataFrame:
    """Return values with an explicit outlier flag.

    Args:
        data (SeriesLike): Input observations.
        rule (OutlierRule): Outlier rule: ``"iqr"``, ``"zscore"``, or ``"mad"``.
        threshold (float): Threshold for z-score or MAD rules.
        multiplier (float): IQR multiplier for Tukey fences.

    Returns:
        pandas.DataFrame: Value and outlier flag columns.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If rule options are invalid.

    Examples:
        ```python
        frame = flag_outliers(values)
        ```

    Notes:
        Flagging is often preferable when downstream users need transparency.
    """
    values = as_numeric_series(data)
    mask = outlier_mask(values, rule=rule, threshold=threshold, multiplier=multiplier)
    return pd.DataFrame({"value": values, "is_outlier": mask})


def outlier_treatment_comparison_static(
    data: SeriesLike,
    rule: OutlierRule = "iqr",
    treatment: Literal["cap", "remove"] = "cap",
    title: Optional[str] = None,
    figsize: FigureSize = (10, 6),
    color: Optional[str] = None,
    theme: str = "default",
) -> MatplotlibAxes:
    """Create a static before-after box plot for outlier treatment.

    Args:
        data (SeriesLike): Input observations.
        rule (OutlierRule): Outlier rule used for treatment.
        treatment (Literal["cap", "remove"]): Treatment method.
        title (Optional[str]): Optional chart title.
        figsize (FigureSize): Matplotlib figure size.
        color (Optional[str]): Box color.
        theme (str): Styling theme name.

    Returns:
        matplotlib.axes.Axes: Axes containing before-after treatment comparison.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If treatment or rule options are invalid.

    Examples:
        ```python
        ax = outlier_treatment_comparison_static(values)
        ```

    Notes:
        This plot is intended for treatment review, not automatic data cleaning approval.
    """
    if treatment not in {"cap", "remove"}:
        raise ValueError("treatment must be either 'cap' or 'remove'.")
    result = cap_outliers(data, rule=rule) if treatment == "cap" else remove_outliers(data, rule=rule)
    ax = setup_plot(title=title or "Outlier Treatment Comparison", ylabel="Value", figsize=figsize)[1]
    box = ax.boxplot([result.original, result.treated], labels=["Original", "Treated"], patch_artist=True)
    if color:
        for patch in box["boxes"]:
            patch.set_facecolor(color)
    ax.grid(True, axis="y", alpha=0.3)
    apply_theme(ax, theme)
    return ax


def outlier_treatment_comparison_interactive(
    data: SeriesLike,
    rule: OutlierRule = "iqr",
    treatment: Literal["cap", "remove"] = "cap",
    title: Optional[str] = None,
    color: Optional[str] = None,
    template: str = "plotly",
    height: int = 600,
    width: int = 900,
) -> PlotlyFigure:
    """Create an interactive before-after box plot for outlier treatment.

    Args:
        data (SeriesLike): Input observations.
        rule (OutlierRule): Outlier rule used for treatment.
        treatment (Literal["cap", "remove"]): Treatment method.
        title (Optional[str]): Optional chart title.
        color (Optional[str]): Box color.
        template (str): Plotly template name.
        height (int): Figure height in pixels.
        width (int): Figure width in pixels.

    Returns:
        plotly.graph_objects.Figure: Interactive before-after treatment comparison.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If treatment or rule options are invalid.

    Examples:
        ```python
        fig = outlier_treatment_comparison_interactive(values)
        ```

    Notes:
        Hover labels expose original and treated distributions side by side.
    """
    if treatment == "cap":
        result = cap_outliers(data, rule=rule)
    elif treatment == "remove":
        result = remove_outliers(data, rule=rule)
    else:
        raise ValueError("treatment must be either 'cap' or 'remove'.")
    fig = go.Figure()
    fig.add_trace(go.Box(y=result.original, name="Original", marker_color=color))
    fig.add_trace(go.Box(y=result.treated, name="Treated", marker_color=color))
    fig.update_layout(title=title or "Outlier Treatment Comparison", yaxis_title="Value", template=template, height=height, width=width)
    return fig
