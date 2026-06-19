"""Validation and data-preparation helpers for plotting functions."""

from typing import Iterable, Literal, Optional, Sequence, Tuple, Union

import matplotlib.axes as mpl_axes
import numpy as np
import pandas as pd
import plotly.graph_objects as go

from ..types import ArrayLike, SeriesLike

NaPolicy = Literal["drop", "raise", "keep"]


def validate_alpha(alpha: float, name: str = "alpha") -> None:
    """Validate an opacity value.

    Args:
        alpha (float): Opacity value to validate.
        name (str): Parameter name used in the error message.

    Returns:
        None: The function returns only when validation succeeds.

    Raises:
        TypeError: If ``alpha`` is not numeric.
        ValueError: If ``alpha`` is outside the inclusive ``[0, 1]`` range.

    Example:
        ```python
        validate_alpha(0.7)
        ```

    Notes:
        Matplotlib and Plotly both expect opacity-like values in this range.
    """
    if not isinstance(alpha, (int, float)):
        raise TypeError(f"{name} must be numeric.")
    if alpha < 0 or alpha > 1:
        raise ValueError(f"{name} must be between 0 and 1.")


def validate_positive_int(value: int, name: str) -> None:
    """Validate a positive integer parameter.

    Args:
        value (int): Value to validate.
        name (str): Parameter name used in the error message.

    Returns:
        None: The function returns only when validation succeeds.

    Raises:
        TypeError: If the value is not an integer.
        ValueError: If the value is less than one.

    Example:
        ```python
        validate_positive_int(30, "bins")
        ```

    Notes:
        This helper is intended for bins, marker sizes, and similar counts.
    """
    if not isinstance(value, int):
        raise TypeError(f"{name} must be an integer.")
    if value < 1:
        raise ValueError(f"{name} must be greater than zero.")


def validate_equal_length(*values: Sequence[object], names: Optional[Sequence[str]] = None) -> None:
    """Validate that multiple sequences share the same length.

    Args:
        *values (Sequence[object]): Sequences to compare.
        names (Optional[Sequence[str]]): Optional names used in error messages.

    Returns:
        None: The function returns only when validation succeeds.

    Raises:
        TypeError: If a value does not expose ``len``.
        ValueError: If provided sequences have different lengths.

    Example:
        ```python
        validate_equal_length(x, y, names=("x", "y"))
        ```

    Notes:
        Empty inputs are handled separately by ``resolve_xy_data``.
    """
    lengths = [len(value) for value in values]
    if len(set(lengths)) > 1:
        labels = list(names or [f"value_{i}" for i in range(len(values))])
        details = ", ".join(f"{label}={length}" for label, length in zip(labels, lengths))
        raise ValueError(f"Input lengths must match ({details}).")


def resolve_series(
    value: Union[str, SeriesLike],
    data: Optional[pd.DataFrame] = None,
    fallback_name: str = "Value",
) -> pd.Series:
    """Resolve a series-like object or dataframe column name to a pandas Series.

    Args:
        value (Union[str, SeriesLike]): Series-like values or a dataframe column name.
        data (Optional[pd.DataFrame]): Dataframe used when ``value`` is a column name.
        fallback_name (str): Name assigned to unnamed array-like values.

    Returns:
        pandas.Series: Resolved series.

    Raises:
        TypeError: If ``value`` is a column name and no dataframe is provided.
        ValueError: If the requested dataframe column is missing.

    Example:
        ```python
        series = resolve_series("sales", data=df)
        ```

    Notes:
        This helper enables both ``plot(df["x"], df["y"])`` and ``plot("x", "y", data=df)`` APIs.
    """
    if isinstance(value, str):
        if data is None:
            raise TypeError(f"Column name {value!r} requires a dataframe via data=.")
        if value not in data.columns:
            raise ValueError(f"Column {value!r} was not found in data.")
        return data[value]
    if isinstance(value, pd.Series):
        return value
    return pd.Series(value, name=fallback_name)


def resolve_xy_data(
    x: Union[str, SeriesLike],
    y: Union[str, SeriesLike],
    data: Optional[pd.DataFrame] = None,
    na_policy: NaPolicy = "drop",
    require_numeric: bool = False,
) -> Tuple[pd.Series, pd.Series]:
    """Resolve and validate paired bivariate inputs.

    Args:
        x (Union[str, SeriesLike]): X values or a dataframe column name.
        y (Union[str, SeriesLike]): Y values or a dataframe column name.
        data (Optional[pd.DataFrame]): Optional dataframe used for column-name lookup.
        na_policy (NaPolicy): Missing-value behavior: ``"drop"``, ``"raise"``, or ``"keep"``.
        require_numeric (bool): Whether to coerce both series to numeric values.

    Returns:
        Tuple[pandas.Series, pandas.Series]: Aligned x and y series.

    Raises:
        TypeError: If inputs cannot be resolved or coerced as requested.
        ValueError: If lengths differ, data is empty, or missing values violate ``na_policy``.

    Example:
        ```python
        x_values, y_values = resolve_xy_data("height", "weight", data=df)
        ```

    Notes:
        The returned series preserve names for use in default axis labels.
    """
    x_series = resolve_series(x, data=data, fallback_name="X")
    y_series = resolve_series(y, data=data, fallback_name="Y")
    validate_equal_length(x_series, y_series, names=("x", "y"))
    if na_policy not in {"drop", "raise", "keep"}:
        raise ValueError("na_policy must be 'drop', 'raise', or 'keep'.")
    frame = pd.DataFrame(
        {"x": x_series.to_numpy(), "y": y_series.to_numpy()}
    )
    if frame.empty:
        raise ValueError("x and y must contain at least one observation.")
    if frame.isna().any().any():
        if na_policy == "raise":
            raise ValueError("x and y contain missing values.")
        if na_policy == "drop":
            frame = frame.dropna()
    if frame.empty:
        raise ValueError("No observations remain after missing-value handling.")
    if require_numeric:
        frame["x"] = pd.to_numeric(frame["x"], errors="raise")
        frame["y"] = pd.to_numeric(frame["y"], errors="raise")
    x_out = pd.Series(frame["x"].to_numpy(), name=x_series.name)
    y_out = pd.Series(frame["y"].to_numpy(), name=y_series.name)
    return x_out, y_out


def add_reference_lines(
    ax: mpl_axes.Axes,
    hline: Optional[float] = None,
    vline: Optional[float] = None,
    diagonal: bool = False,
    color: str = "gray",
    linestyle: str = "--",
) -> None:
    """Add optional reference lines to a matplotlib axes object.

    Args:
        ax (matplotlib.axes.Axes): Axes to update.
        hline (Optional[float]): Optional horizontal reference line.
        vline (Optional[float]): Optional vertical reference line.
        diagonal (bool): Whether to draw a y=x diagonal reference.
        color (str): Reference-line color.
        linestyle (str): Reference-line style.

    Returns:
        None: The axes is modified in place.

    Raises:
        TypeError: If line positions are incompatible with matplotlib.
        ValueError: If axes limits cannot be determined for a diagonal line.

    Example:
        ```python
        add_reference_lines(ax, hline=0, diagonal=True)
        ```

    Notes:
        The diagonal line uses the current combined x/y limits.
    """
    if hline is not None:
        ax.axhline(hline, color=color, linestyle=linestyle, linewidth=1)
    if vline is not None:
        ax.axvline(vline, color=color, linestyle=linestyle, linewidth=1)
    if diagonal:
        limits = [
            min(ax.get_xlim()[0], ax.get_ylim()[0]),
            max(ax.get_xlim()[1], ax.get_ylim()[1]),
        ]
        ax.plot(limits, limits, color=color, linestyle=linestyle, linewidth=1)
        ax.set_xlim(limits)
        ax.set_ylim(limits)


def add_plotly_reference_lines(
    fig: go.Figure,
    hline: Optional[float] = None,
    vline: Optional[float] = None,
    diagonal: bool = False,
    x_values: Optional[ArrayLike] = None,
    y_values: Optional[ArrayLike] = None,
    color: str = "gray",
    dash: str = "dash",
) -> None:
    """Add optional reference lines to a Plotly figure.

    Args:
        fig (plotly.graph_objects.Figure): Figure to update.
        hline (Optional[float]): Optional horizontal reference line.
        vline (Optional[float]): Optional vertical reference line.
        diagonal (bool): Whether to draw a y=x diagonal reference.
        x_values (Optional[ArrayLike]): X values used to compute diagonal limits.
        y_values (Optional[ArrayLike]): Y values used to compute diagonal limits.
        color (str): Reference-line color.
        dash (str): Plotly line dash style.

    Returns:
        None: The figure is modified in place.

    Raises:
        TypeError: If line positions are incompatible with Plotly.
        ValueError: If diagonal limits are requested without x and y values.

    Example:
        ```python
        add_plotly_reference_lines(fig, hline=0)
        ```

    Notes:
        Diagonal support is data-driven because Plotly layout limits may be unset.
    """
    if hline is not None:
        fig.add_hline(y=hline, line_color=color, line_dash=dash)
    if vline is not None:
        fig.add_vline(x=vline, line_color=color, line_dash=dash)
    if diagonal:
        if x_values is None or y_values is None:
            raise ValueError("x_values and y_values are required when diagonal=True.")
        combined = np.concatenate([np.asarray(x_values, dtype=float), np.asarray(y_values, dtype=float)])
        low = float(np.nanmin(combined))
        high = float(np.nanmax(combined))
        fig.add_trace(
            go.Scatter(
                x=[low, high],
                y=[low, high],
                mode="lines",
                name="Reference",
                line=dict(color=color, dash=dash),
                showlegend=False,
            )
        )


def numeric_dataframe(
    df: pd.DataFrame,
    columns: Optional[Iterable[str]] = None,
    min_columns: int = 2,
) -> pd.DataFrame:
    """Select and validate numeric dataframe columns.

    Args:
        df (pandas.DataFrame): Input dataframe.
        columns (Optional[Iterable[str]]): Optional subset of columns to use.
        min_columns (int): Minimum number of numeric columns required.

    Returns:
        pandas.DataFrame: Numeric dataframe subset.

    Raises:
        TypeError: If ``df`` is not a dataframe.
        ValueError: If requested columns are missing or too few numeric columns remain.

    Example:
        ```python
        numeric = numeric_dataframe(df, columns=["a", "b"])
        ```

    Notes:
        Non-numeric columns are ignored after any explicit column selection.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame.")
    if columns is not None:
        missing = [column for column in columns if column not in df.columns]
        if missing:
            raise ValueError(f"Columns not found in dataframe: {missing}.")
        df = df.loc[:, list(columns)]
    numeric = df.select_dtypes(include=[np.number])
    if numeric.shape[1] < min_columns:
        raise ValueError(f"At least {min_columns} numeric columns are required.")
    return numeric
