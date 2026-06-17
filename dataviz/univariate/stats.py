"""Statistical summaries and helper calculations for univariate data."""

from dataclasses import dataclass
from typing import Literal, Optional

import numpy as np
import pandas as pd

from ..types import SeriesLike

BinMethod = Literal["auto", "fd", "sturges", "rice", "sqrt"]


@dataclass(frozen=True)
class UnivariateStats:
    """Summary statistics for one variable.

    Args:
        count (int): Number of non-missing observations.
        missing (int): Number of missing observations removed from the summary.
        mean (float): Arithmetic mean.
        median (float): Median value.
        std (float): Sample standard deviation.
        variance (float): Sample variance.
        minimum (float): Minimum observed value.
        q1 (float): First quartile.
        q3 (float): Third quartile.
        maximum (float): Maximum observed value.
        iqr (float): Interquartile range.
        skewness (float): Fisher-Pearson skewness estimate.
        kurtosis (float): Fisher kurtosis estimate.
        sem (float): Standard error of the mean.
        mad (float): Median absolute deviation from the median.

    Returns:
        UnivariateStats: Immutable univariate summary record.

    Raises:
        TypeError: If provided values cannot be represented by the declared fields.
        ValueError: If a statistic is incompatible with downstream numeric use.

    Examples:
        ```python
        stats = UnivariateStats(10, 0, 5.0, 5.0, 1.0, 1.0, 3.0, 4.0, 6.0, 7.0, 2.0, 0.0, -1.2, 0.3, 1.0)
        ```

    Notes:
        The dataclass is returned by ``univariate_summary`` and can be converted with ``dataclasses.asdict``.
    """

    count: int
    missing: int
    mean: float
    median: float
    std: float
    variance: float
    minimum: float
    q1: float
    q3: float
    maximum: float
    iqr: float
    skewness: float
    kurtosis: float
    sem: float
    mad: float


def as_numeric_series(data: SeriesLike, name: str = "Value") -> pd.Series:
    """Convert series-like data to a clean numeric pandas Series.

    Args:
        data (SeriesLike): Input observations.
        name (str): Fallback series name for unnamed arrays.

    Returns:
        pandas.Series: Numeric observations with missing values removed.

    Raises:
        TypeError: If values cannot be coerced to numeric values.
        ValueError: If no numeric observations remain.

    Examples:
        ```python
        values = as_numeric_series([1, 2, 3])
        ```

    Notes:
        This helper is intentionally shared by visual and non-visual univariate utilities.
    """
    series = data if isinstance(data, pd.Series) else pd.Series(data, name=name)
    if series.name is None:
        series = series.rename(name)
    numeric = pd.to_numeric(series, errors="raise").dropna()
    if numeric.empty:
        raise ValueError("data must contain at least one numeric observation.")
    return numeric.reset_index(drop=True)


def univariate_summary(data: SeriesLike) -> UnivariateStats:
    """Compute robust descriptive statistics for one numeric variable.

    Args:
        data (SeriesLike): Input observations.

    Returns:
        UnivariateStats: Count, center, spread, shape, and robust spread statistics.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If no non-missing numeric observations remain.

    Examples:
        ```python
        summary = univariate_summary([1, 2, 3, 4])
        ```

    Notes:
        Sample standard deviation and variance use pandas defaults with ``ddof=1``.
    """
    original = pd.Series(data)
    values = as_numeric_series(data)
    q1 = float(values.quantile(0.25))
    q3 = float(values.quantile(0.75))
    median = float(values.median())
    mad = float((values - median).abs().median())
    return UnivariateStats(
        count=int(values.count()),
        missing=int(original.isna().sum()),
        mean=float(values.mean()),
        median=median,
        std=float(values.std(ddof=1)) if len(values) > 1 else 0.0,
        variance=float(values.var(ddof=1)) if len(values) > 1 else 0.0,
        minimum=float(values.min()),
        q1=q1,
        q3=q3,
        maximum=float(values.max()),
        iqr=float(q3 - q1),
        skewness=float(values.skew()) if len(values) > 2 else 0.0,
        kurtosis=float(values.kurt()) if len(values) > 3 else 0.0,
        sem=float(values.sem()) if len(values) > 1 else 0.0,
        mad=mad,
    )


def iqr_outliers(data: SeriesLike, multiplier: float = 1.5) -> pd.Series:
    """Flag observations outside Tukey IQR fences.

    Args:
        data (SeriesLike): Input observations.
        multiplier (float): IQR multiplier used to define lower and upper fences.

    Returns:
        pandas.Series: Boolean mask where ``True`` marks an outlier.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If ``multiplier`` is not positive or no observations remain.

    Examples:
        ```python
        mask = iqr_outliers([1, 2, 3, 100])
        ```

    Notes:
        The returned mask is aligned to the cleaned non-missing numeric series.
    """
    if multiplier <= 0:
        raise ValueError("multiplier must be positive.")
    values = as_numeric_series(data)
    q1 = values.quantile(0.25)
    q3 = values.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - multiplier * iqr
    upper = q3 + multiplier * iqr
    return (values < lower) | (values > upper)


def zscore_outliers(data: SeriesLike, threshold: float = 3.0) -> pd.Series:
    """Flag observations whose absolute z-score exceeds a threshold.

    Args:
        data (SeriesLike): Input observations.
        threshold (float): Absolute z-score threshold used to mark outliers.

    Returns:
        pandas.Series: Boolean mask where ``True`` marks an outlier.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If ``threshold`` is not positive or no observations remain.

    Examples:
        ```python
        mask = zscore_outliers([1, 2, 3, 100], threshold=2.5)
        ```

    Notes:
        A constant series returns an all-false mask because the standard deviation is zero.
    """
    if threshold <= 0:
        raise ValueError("threshold must be positive.")
    values = as_numeric_series(data)
    std = float(values.std(ddof=0))
    if std == 0:
        return pd.Series(False, index=values.index)
    zscores = (values - values.mean()) / std
    return zscores.abs() > threshold


def recommended_bin_count(data: SeriesLike, method: BinMethod = "auto") -> int:
    """Recommend a histogram bin count from common univariate rules.

    Args:
        data (SeriesLike): Input observations.
        method (BinMethod): Rule name: ``"auto"``, ``"fd"``, ``"sturges"``, ``"rice"``, or ``"sqrt"``.

    Returns:
        int: Recommended positive number of bins.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If ``method`` is unknown or no observations remain.

    Examples:
        ```python
        bins = recommended_bin_count(data, method="fd")
        ```

    Notes:
        ``"auto"`` chooses the larger of Freedman-Diaconis and Sturges recommendations.
    """
    values = as_numeric_series(data)
    n = len(values)
    if method == "sqrt":
        return max(1, int(np.ceil(np.sqrt(n))))
    if method == "rice":
        return max(1, int(np.ceil(2 * n ** (1 / 3))))
    sturges = max(1, int(np.ceil(np.log2(n) + 1)))
    if method == "sturges":
        return sturges
    if method not in {"auto", "fd"}:
        raise ValueError("method must be one of 'auto', 'fd', 'sturges', 'rice', or 'sqrt'.")
    q1 = values.quantile(0.25)
    q3 = values.quantile(0.75)
    iqr = q3 - q1
    if iqr == 0:
        fd = sturges
    else:
        width = 2 * iqr / n ** (1 / 3)
        value_range = float(values.max() - values.min())
        fd = max(1, int(np.ceil(value_range / width))) if width > 0 else sturges
    return max(fd, sturges) if method == "auto" else fd


def percentile_table(data: SeriesLike, step: int = 10) -> pd.DataFrame:
    """Create a percentile table for one numeric variable.

    Args:
        data (SeriesLike): Input observations.
        step (int): Percentile interval between rows.

    Returns:
        pandas.DataFrame: Percentile and value columns.

    Raises:
        TypeError: If values cannot be converted to numeric data.
        ValueError: If ``step`` is not between 1 and 100 or no observations remain.

    Examples:
        ```python
        table = percentile_table(data, step=5)
        ```

    Notes:
        The table always includes 0 and 100 percentiles.
    """
    if step < 1 or step > 100:
        raise ValueError("step must be between 1 and 100.")
    values = as_numeric_series(data)
    percentiles = sorted(set(range(0, 101, step)) | {100})
    quantiles = [p / 100 for p in percentiles]
    return pd.DataFrame(
        {
            "percentile": percentiles,
            "value": [float(values.quantile(q)) for q in quantiles],
        }
    )

