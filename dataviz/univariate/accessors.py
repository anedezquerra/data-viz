"""Shared univariate input resolution and type inference helpers."""

from dataclasses import dataclass
from typing import Literal, Optional, Union

import numpy as np
import pandas as pd

from ..types import SeriesLike

NaPolicy = Literal["drop", "raise", "keep"]
UnivariateKind = Literal["numeric", "categorical", "datetime", "boolean", "text"]


@dataclass(frozen=True)
class UnivariateInput:
    """Resolved univariate input data.

    Args:
        values (pandas.Series): Resolved observations.
        name (str): Display name for the variable.
        kind (str): Inferred variable kind.
        missing_count (int): Number of missing values in the original input.

    Returns:
        UnivariateInput: Immutable resolved input summary.

    Raises:
        TypeError: If fields cannot be represented by the declared types.
        ValueError: If fields are inconsistent with downstream use.

    Examples:
        ```python
        resolved = UnivariateInput(pd.Series([1, 2]), "sales", "numeric", 0)
        ```

    Notes:
        This dataclass is intended for wrappers and future API-normalization work.
    """

    values: pd.Series
    name: str
    kind: str
    missing_count: int


def resolve_univariate_data(
    value: Union[str, SeriesLike],
    data: Optional[pd.DataFrame] = None,
    na_policy: NaPolicy = "drop",
    require_numeric: bool = False,
    fallback_name: str = "Value",
) -> UnivariateInput:
    """Resolve a column name or series-like object for univariate functions.

    Args:
        value (Union[str, SeriesLike]): Series-like values or a dataframe column name.
        data (Optional[pandas.DataFrame]): Optional dataframe used for column-name lookup.
        na_policy (NaPolicy): Missing-value behavior: ``"drop"``, ``"raise"``, or ``"keep"``.
        require_numeric (bool): Whether to coerce the resolved values to numeric.
        fallback_name (str): Name used for unnamed array-like values.

    Returns:
        UnivariateInput: Resolved values, name, inferred kind, and missing count.

    Raises:
        TypeError: If a column name is provided without a dataframe or coercion fails.
        ValueError: If a column is missing, missing values violate policy, or no observations remain.

    Examples:
        ```python
        resolved = resolve_univariate_data("sales", data=df, require_numeric=True)
        ```

    Notes:
        This helper is the common bridge toward consistent ``data=`` support across the module.
    """
    if isinstance(value, str):
        if data is None:
            raise TypeError(f"Column name {value!r} requires a dataframe via data=.")
        if value not in data.columns:
            raise ValueError(f"Column {value!r} was not found in data.")
        series = data[value].copy()
        name = value
    else:
        series = value if isinstance(value, pd.Series) else pd.Series(value, name=fallback_name)
        name = str(series.name or fallback_name)
    missing_count = int(series.isna().sum())
    if missing_count and na_policy == "raise":
        raise ValueError("Input contains missing values.")
    if na_policy == "drop":
        series = series.dropna()
    elif na_policy != "keep":
        raise ValueError("na_policy must be one of 'drop', 'raise', or 'keep'.")
    if series.empty:
        raise ValueError("Input must contain at least one observation.")
    if require_numeric:
        series = pd.to_numeric(series, errors="raise")
    kind = infer_univariate_kind(series)
    return UnivariateInput(values=series.reset_index(drop=True), name=name, kind=kind, missing_count=missing_count)


def infer_univariate_kind(values: SeriesLike) -> UnivariateKind:
    """Infer a practical univariate data kind.

    Args:
        values (SeriesLike): Input observations.

    Returns:
        UnivariateKind: One of ``"numeric"``, ``"categorical"``, ``"datetime"``, ``"boolean"``, or ``"text"``.

    Raises:
        TypeError: If input data cannot be represented as a pandas Series.
        ValueError: If no non-missing observations remain.

    Examples:
        ```python
        kind = infer_univariate_kind([1, 2, 3])
        ```

    Notes:
        Object data with low cardinality is treated as categorical; otherwise it is treated as text.
    """
    series = pd.Series(values).dropna()
    if series.empty:
        raise ValueError("values must contain at least one non-missing observation.")
    if pd.api.types.is_bool_dtype(series):
        return "boolean"
    if pd.api.types.is_datetime64_any_dtype(series):
        return "datetime"
    if pd.api.types.is_numeric_dtype(series):
        return "numeric"
    converted_dates = pd.to_datetime(series, errors="coerce")
    if converted_dates.notna().mean() >= 0.9:
        return "datetime"
    unique_ratio = series.nunique() / len(series)
    if unique_ratio <= 0.5 or series.nunique() <= min(20, len(series)):
        return "categorical"
    return "text"


def numeric_or_none(values: SeriesLike) -> Optional[pd.Series]:
    """Try to coerce values to numeric data.

    Args:
        values (SeriesLike): Input observations.

    Returns:
        Optional[pandas.Series]: Numeric values when coercion leaves at least one observation, otherwise ``None``.

    Raises:
        TypeError: If input data cannot be represented as a pandas Series.
        ValueError: If no meaningful conversion can be attempted.

    Examples:
        ```python
        numeric = numeric_or_none(series)
        ```

    Notes:
        This helper is permissive and is intended for profile functions, not strict plotting APIs.
    """
    series = pd.to_numeric(pd.Series(values), errors="coerce").dropna()
    if series.empty:
        return None
    if not np.isfinite(series.to_numpy(dtype=float)).any():
        return None
    return series.reset_index(drop=True)

