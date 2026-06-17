"""SPC rule evaluation and shared calculations."""

from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import numpy as np
import pandas as pd

from ..types import ArrayLike, MatrixLike
from ..utils import validate_positive_int
from .constants import get_spc_constants


@dataclass(frozen=True)
class ControlLimits:
    """Control limits for an SPC chart.

    Args:
        center (float): Center-line value.
        lower (float): Lower control limit.
        upper (float): Upper control limit.
        sigma (float): Estimated process standard deviation.

    Returns:
        ControlLimits: Immutable control-limit summary.

    Raises:
        TypeError: If values cannot be represented as floats.
        ValueError: If limits are not finite.

    Examples:
        ```python
        limits = ControlLimits(center=10.0, lower=7.0, upper=13.0, sigma=1.0)
        ```

    Notes:
        The class is shared by static and interactive SPC functions.
    """

    center: float
    lower: float
    upper: float
    sigma: float


@dataclass(frozen=True)
class RuleViolation:
    """Detected SPC rule violation.

    Args:
        index (int): Zero-based observation index.
        value (float): Observation value at the violation.
        rule (str): Rule identifier.
        message (str): Human-readable rule explanation.

    Returns:
        RuleViolation: Immutable rule-violation record.

    Raises:
        TypeError: If values cannot be represented in the expected types.
        ValueError: If index or value is invalid.

    Examples:
        ```python
        violation = RuleViolation(4, 12.5, "beyond_limits", "Point outside limits")
        ```

    Notes:
        Chart functions can highlight these records on top of process data.
    """

    index: int
    value: float
    rule: str
    message: str


def as_numeric_series(data: ArrayLike, name: str = "Value") -> pd.Series:
    """Convert array-like process data to a numeric pandas Series.

    Args:
        data (ArrayLike): Process observations.
        name (str): Series name.

    Returns:
        pandas.Series: Numeric process observations.

    Raises:
        TypeError: If data cannot be converted to numeric values.
        ValueError: If data is empty after missing values are removed.

    Examples:
        ```python
        values = as_numeric_series(data)
        ```

    Notes:
        Missing values are dropped because SPC limits require observed values.
    """
    series = pd.Series(data, name=name)
    series = pd.to_numeric(series, errors="raise").dropna()
    if series.empty:
        raise ValueError("SPC data must contain at least one numeric observation.")
    return series.reset_index(drop=True)


def individuals_limits(data: ArrayLike, sigma_multiplier: float = 3.0) -> ControlLimits:
    """Compute individuals chart limits from process observations.

    Args:
        data (ArrayLike): Process observations.
        sigma_multiplier (float): Number of standard deviations for limits.

    Returns:
        ControlLimits: Center, lower limit, upper limit, and sigma estimate.

    Raises:
        TypeError: If data cannot be converted to numeric values.
        ValueError: If sigma multiplier is not positive.

    Examples:
        ```python
        limits = individuals_limits(values)
        ```

    Notes:
        Sigma uses the sample standard deviation with ``ddof=1`` when possible.
    """
    if sigma_multiplier <= 0:
        raise ValueError("sigma_multiplier must be greater than zero.")
    values = as_numeric_series(data)
    sigma = float(values.std(ddof=1)) if len(values) > 1 else 0.0
    center = float(values.mean())
    return ControlLimits(center=center, lower=center - sigma_multiplier * sigma, upper=center + sigma_multiplier * sigma, sigma=sigma)


def moving_ranges(data: ArrayLike, span: int = 2) -> pd.Series:
    """Compute moving ranges for process observations.

    Args:
        data (ArrayLike): Process observations.
        span (int): Difference span used for moving ranges.

    Returns:
        pandas.Series: Absolute moving ranges.

    Raises:
        TypeError: If data cannot be converted to numeric values.
        ValueError: If span is invalid for the data length.

    Examples:
        ```python
        ranges = moving_ranges(values, span=2)
        ```

    Notes:
        The first ``span - 1`` positions cannot produce a moving range and are omitted.
    """
    validate_positive_int(span, "span")
    values = as_numeric_series(data)
    if span > len(values):
        raise ValueError("span must not exceed the number of observations.")
    return values.diff(periods=span - 1).abs().dropna().reset_index(drop=True)


def subgroup_matrix(data: MatrixLike, subgroup_size: Optional[int] = None) -> pd.DataFrame:
    """Convert raw or grouped observations into a subgroup matrix.

    Args:
        data (MatrixLike): Matrix-like subgroup data or a flat sequence.
        subgroup_size (Optional[int]): Subgroup size for flat sequences.

    Returns:
        pandas.DataFrame: Numeric subgroup matrix, one row per subgroup.

    Raises:
        TypeError: If data cannot be converted to a numeric dataframe.
        ValueError: If subgroup size is invalid or no complete subgroup remains.

    Examples:
        ```python
        groups = subgroup_matrix(values, subgroup_size=5)
        ```

    Notes:
        Flat sequences are truncated to complete subgroups.
    """
    if isinstance(data, pd.DataFrame):
        frame = data.copy()
    else:
        array = np.asarray(data, dtype=float)
        if array.ndim == 1:
            if subgroup_size is None:
                raise ValueError("subgroup_size is required for flat data.")
            validate_positive_int(subgroup_size, "subgroup_size")
            usable = (len(array) // subgroup_size) * subgroup_size
            if usable == 0:
                raise ValueError("No complete subgroups can be formed.")
            array = array[:usable].reshape(-1, subgroup_size)
        frame = pd.DataFrame(array)
    frame = frame.apply(pd.to_numeric, errors="raise").dropna(how="all")
    if frame.empty:
        raise ValueError("Subgroup data must contain numeric observations.")
    return frame


def xbar_r_limits(
    data: MatrixLike,
    subgroup_size: Optional[int] = None,
    sigma_multiplier: float = 3.0,
    use_constants: bool = True,
) -> Tuple[ControlLimits, ControlLimits, pd.Series, pd.Series]:
    """Compute Xbar and R chart limits.

    Args:
        data (MatrixLike): Matrix-like subgroup data or flat sequence.
        subgroup_size (Optional[int]): Subgroup size for flat sequences.
        sigma_multiplier (float): Number of range standard deviations for empirical fallback limits.
        use_constants (bool): Whether to use traditional SPC constants when subgroup size is supported.

    Returns:
        Tuple[ControlLimits, ControlLimits, pandas.Series, pandas.Series]: Xbar limits, R limits, subgroup means, and subgroup ranges.

    Raises:
        TypeError: If data cannot be converted to numeric subgroups.
        ValueError: If subgroup size or sigma multiplier is invalid.

    Examples:
        ```python
        x_limits, r_limits, means, ranges = xbar_r_limits(data, subgroup_size=5)
        ```

    Notes:
        Traditional constants are used by default for subgroup sizes 2 through 25.
    """
    groups = subgroup_matrix(data, subgroup_size=subgroup_size)
    means = groups.mean(axis=1)
    ranges = groups.max(axis=1) - groups.min(axis=1)
    r_center = float(ranges.mean())
    subgroup_n = int(groups.count(axis=1).mode().iloc[0])
    if use_constants:
        try:
            constants = get_spc_constants(subgroup_n)
            x_center = float(means.mean())
            x_limits = ControlLimits(
                center=x_center,
                lower=x_center - constants.a2 * r_center,
                upper=x_center + constants.a2 * r_center,
                sigma=r_center / subgroup_n**0.5,
            )
            r_limits = ControlLimits(
                center=r_center,
                lower=max(0.0, constants.d3 * r_center),
                upper=constants.d4 * r_center,
                sigma=float(ranges.std(ddof=1)) if len(ranges) > 1 else 0.0,
            )
            return x_limits, r_limits, means.reset_index(drop=True), ranges.reset_index(drop=True)
        except ValueError:
            pass
    x_limits = individuals_limits(means, sigma_multiplier=sigma_multiplier)
    r_sigma = float(ranges.std(ddof=1)) if len(ranges) > 1 else 0.0
    r_limits = ControlLimits(center=r_center, lower=max(0.0, r_center - sigma_multiplier * r_sigma), upper=r_center + sigma_multiplier * r_sigma, sigma=r_sigma)
    return x_limits, r_limits, means.reset_index(drop=True), ranges.reset_index(drop=True)


def xbar_s_limits(
    data: MatrixLike,
    subgroup_size: Optional[int] = None,
    sigma_multiplier: float = 3.0,
    use_constants: bool = True,
) -> Tuple[ControlLimits, ControlLimits, pd.Series, pd.Series]:
    """Compute Xbar and S chart limits.

    Args:
        data (MatrixLike): Matrix-like subgroup data or flat sequence.
        subgroup_size (Optional[int]): Subgroup size for flat sequences.
        sigma_multiplier (float): Number of standard deviations for empirical fallback limits.
        use_constants (bool): Whether to use traditional SPC constants when subgroup size is supported.

    Returns:
        Tuple[ControlLimits, ControlLimits, pandas.Series, pandas.Series]: Xbar limits, S limits, subgroup means, and subgroup standard deviations.

    Raises:
        TypeError: If data cannot be converted to numeric subgroups.
        ValueError: If subgroup size or sigma multiplier is invalid.

    Examples:
        ```python
        x_limits, s_limits, means, stds = xbar_s_limits(data, subgroup_size=5)
        ```

    Notes:
        S limits use traditional B3/B4 constants by default for subgroup sizes 2 through 25.
    """
    groups = subgroup_matrix(data, subgroup_size=subgroup_size)
    means = groups.mean(axis=1)
    stds = groups.std(axis=1, ddof=1).fillna(0.0)
    s_center = float(stds.mean())
    subgroup_n = int(groups.count(axis=1).mode().iloc[0])
    if use_constants:
        try:
            constants = get_spc_constants(subgroup_n)
            x_center = float(means.mean())
            x_limits = ControlLimits(
                center=x_center,
                lower=x_center - constants.a3 * s_center,
                upper=x_center + constants.a3 * s_center,
                sigma=s_center / subgroup_n**0.5,
            )
            s_limits = ControlLimits(
                center=s_center,
                lower=max(0.0, constants.b3 * s_center),
                upper=constants.b4 * s_center,
                sigma=float(stds.std(ddof=1)) if len(stds) > 1 else 0.0,
            )
            return x_limits, s_limits, means.reset_index(drop=True), stds.reset_index(drop=True)
        except ValueError:
            pass
    x_limits = individuals_limits(means, sigma_multiplier=sigma_multiplier)
    s_sigma = float(stds.std(ddof=1)) if len(stds) > 1 else 0.0
    s_limits = ControlLimits(center=s_center, lower=max(0.0, s_center - sigma_multiplier * s_sigma), upper=s_center + sigma_multiplier * s_sigma, sigma=s_sigma)
    return x_limits, s_limits, means.reset_index(drop=True), stds.reset_index(drop=True)


def detect_rule_violations(
    data: ArrayLike,
    limits: Optional[ControlLimits] = None,
    rules: Optional[Sequence[str]] = None,
    run_length: int = 8,
    trend_length: int = 6,
) -> List[RuleViolation]:
    """Detect common SPC rule violations.

    Args:
        data (ArrayLike): Process observations.
        limits (Optional[ControlLimits]): Precomputed limits. Defaults to individuals limits.
        rules (Optional[Sequence[str]]): Rule identifiers to evaluate. Defaults to all supported rules.
        run_length (int): Consecutive points on one side of center needed for a run signal.
        trend_length (int): Consecutive increasing or decreasing points needed for a trend signal.

    Returns:
        List[RuleViolation]: Detected rule violations.

    Raises:
        TypeError: If data cannot be converted to numeric values.
        ValueError: If run or trend lengths are invalid.

    Examples:
        ```python
        violations = detect_rule_violations(values)
        ```

    Notes:
        Supported rules include beyond limits, center runs, trends, zone A/B patterns, and zone C clustering.
    """
    validate_positive_int(run_length, "run_length")
    validate_positive_int(trend_length, "trend_length")
    values = as_numeric_series(data)
    limits = limits or individuals_limits(values)
    sigma = limits.sigma
    supported = {
        "beyond_limits",
        "center_run",
        "trend",
        "two_of_three_zone_a",
        "four_of_five_zone_b",
        "fifteen_zone_c",
    }
    selected = set(rules or supported)
    unknown = selected - supported
    if unknown:
        raise ValueError(f"Unsupported SPC rule(s): {sorted(unknown)}.")
    violations: List[RuleViolation] = []
    if "beyond_limits" in selected:
        for idx, value in enumerate(values):
            if value > limits.upper or value < limits.lower:
                violations.append(RuleViolation(idx, float(value), "beyond_limits", "Point outside control limits"))
    side = np.sign(values - limits.center)
    if "center_run" in selected:
        for idx in range(run_length - 1, len(side)):
            window = side.iloc[idx - run_length + 1 : idx + 1]
            if (window > 0).all() or (window < 0).all():
                violations.append(RuleViolation(idx, float(values.iloc[idx]), "center_run", f"{run_length} points on one side of center"))
    if "trend" in selected:
        diffs = values.diff().dropna()
        for idx in range(trend_length - 1, len(values)):
            window = diffs.iloc[idx - trend_length + 1 : idx]
            if len(window) == trend_length - 1 and ((window > 0).all() or (window < 0).all()):
                violations.append(RuleViolation(idx, float(values.iloc[idx]), "trend", f"{trend_length} point monotonic trend"))
    if sigma > 0 and "two_of_three_zone_a" in selected:
        distance = values - limits.center
        for idx in range(2, len(values)):
            window = distance.iloc[idx - 2 : idx + 1]
            high = (window > 2 * sigma).sum()
            low = (window < -2 * sigma).sum()
            if high >= 2 or low >= 2:
                violations.append(RuleViolation(idx, float(values.iloc[idx]), "two_of_three_zone_a", "Two of three points beyond two sigma on one side"))
    if sigma > 0 and "four_of_five_zone_b" in selected:
        distance = values - limits.center
        for idx in range(4, len(values)):
            window = distance.iloc[idx - 4 : idx + 1]
            high = (window > sigma).sum()
            low = (window < -sigma).sum()
            if high >= 4 or low >= 4:
                violations.append(RuleViolation(idx, float(values.iloc[idx]), "four_of_five_zone_b", "Four of five points beyond one sigma on one side"))
    if sigma > 0 and "fifteen_zone_c" in selected:
        distance = (values - limits.center).abs()
        for idx in range(14, len(values)):
            window = distance.iloc[idx - 14 : idx + 1]
            if (window < sigma).all():
                violations.append(RuleViolation(idx, float(values.iloc[idx]), "fifteen_zone_c", "Fifteen points within one sigma of center"))
    return violations


def violations_by_index(violations: Iterable[RuleViolation]) -> Dict[int, List[RuleViolation]]:
    """Group rule violations by observation index.

    Args:
        violations (Iterable[RuleViolation]): Rule violations to group.

    Returns:
        Dict[int, List[RuleViolation]]: Violations keyed by observation index.

    Raises:
        TypeError: If violations are not iterable.
        ValueError: If violation indexes are invalid.

    Examples:
        ```python
        grouped = violations_by_index(violations)
        ```

    Notes:
        Grouping helps chart functions annotate points with multiple violations.
    """
    grouped: Dict[int, List[RuleViolation]] = {}
    for violation in violations:
        grouped.setdefault(violation.index, []).append(violation)
    return grouped
