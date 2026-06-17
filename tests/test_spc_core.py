"""Focused tests for SPC calculations and summaries."""

import numpy as np
import pandas as pd
import pytest

from dataviz.spc.capability import capability_summary
from dataviz.spc.constants import get_spc_constants
from dataviz.spc.multivariate import hotelling_t2_summary
from dataviz.spc.rules import ControlLimits, detect_rule_violations, xbar_r_limits, xbar_s_limits


def test_get_spc_constants_for_supported_subgroup_size():
    """SPC constants return traditional table values for common subgroup sizes."""
    constants = get_spc_constants(5)

    assert constants.n == 5
    assert constants.a2 == pytest.approx(0.577)
    assert constants.d4 == pytest.approx(2.114)
    assert constants.b4 == pytest.approx(2.089)


def test_xbar_r_limits_use_traditional_constants():
    """Xbar-R limits use A2/D3/D4 constants when subgroup size is supported."""
    data = np.array([[10, 12, 11, 13, 12], [9, 11, 10, 12, 11], [12, 13, 12, 14, 13]])
    x_limits, r_limits, means, ranges = xbar_r_limits(data)
    rbar = ranges.mean()
    xbarbar = means.mean()

    assert x_limits.center == pytest.approx(xbarbar)
    assert x_limits.upper == pytest.approx(xbarbar + 0.577 * rbar)
    assert r_limits.lower == pytest.approx(0.0)
    assert r_limits.upper == pytest.approx(2.114 * rbar)


def test_xbar_s_limits_use_traditional_constants():
    """Xbar-S limits use A3/B3/B4 constants when subgroup size is supported."""
    data = np.array([[10, 12, 11, 13, 12], [9, 11, 10, 12, 11], [12, 13, 12, 14, 13]])
    x_limits, s_limits, means, stds = xbar_s_limits(data)
    sbar = stds.mean()
    xbarbar = means.mean()

    assert x_limits.center == pytest.approx(xbarbar)
    assert x_limits.upper == pytest.approx(xbarbar + 1.427 * sbar)
    assert s_limits.lower == pytest.approx(0.0)
    assert s_limits.upper == pytest.approx(2.089 * sbar)


def test_detect_rule_violations_supports_rule_selection():
    """Rule detection can be restricted to specific rule families."""
    data = [0, 0, 0, 0, 0, 0, 0, 10]
    limits = ControlLimits(center=0.0, lower=-3.0, upper=3.0, sigma=1.0)

    violations = detect_rule_violations(data, limits=limits, rules=["beyond_limits"])

    assert len(violations) == 1
    assert violations[0].rule == "beyond_limits"
    assert violations[0].index == 7


def test_detect_rule_violations_rejects_unknown_rule():
    """Unknown rule names fail clearly."""
    with pytest.raises(ValueError, match="Unsupported SPC rule"):
        detect_rule_violations([1, 2, 3], rules=["not_a_rule"])


def test_capability_summary_includes_normal_ppm():
    """Capability summaries include empirical and normal-theory PPM metrics."""
    stats = capability_summary([9.8, 10.0, 10.2, 10.1, 9.9], lsl=9.5, usl=10.5)

    assert stats.cp is not None
    assert stats.cpk is not None
    assert stats.ppm_below == pytest.approx(0.0)
    assert stats.ppm_above == pytest.approx(0.0)
    assert stats.ppm_total_normal is not None
    assert stats.ppm_total_normal >= 0


def test_hotelling_t2_summary_returns_scores_and_limit():
    """Hotelling T-squared summary returns one score per complete observation."""
    frame = pd.DataFrame({"a": [1.0, 2.0, 3.0, 4.0], "b": [1.1, 1.9, 3.2, 3.8]})

    result = hotelling_t2_summary(frame, limit_quantile=0.95)

    assert len(result.scores) == len(frame)
    assert result.limit > 0
    assert list(result.center.index) == ["a", "b"]
