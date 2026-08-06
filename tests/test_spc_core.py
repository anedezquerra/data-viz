"""Focused tests for SPC calculations and summaries."""

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import pytest
import matplotlib.pyplot as plt

import dataviz.spc as spc
from dataviz.spc.attribute import _laney_p_limits, _laney_u_limits, _t_chart_limits
from dataviz.spc.capability import capability_summary
from dataviz.spc.constants import get_d2, get_spc_constants
from dataviz.spc.multivariate import hotelling_t2_summary
from dataviz.spc.rules import (
    ControlLimits,
    detect_rule_violations,
    xbar_r_limits,
    xbar_s_limits,
)
from dataviz.spc.variable import _imr_limits, _median_limits


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


def test_get_d2_returns_tabulated_constant():
    """The d2 helper returns the standard bias-correction value for span 2."""
    assert get_d2(2) == pytest.approx(1.128)


def test_get_d2_rejects_unsupported_span():
    """Unsupported moving-range spans fail clearly."""
    with pytest.raises(ValueError, match="spans 2 through 10"):
        get_d2(11)


def test_imr_limits_use_moving_range_sigma():
    """I-MR individuals limits estimate sigma as MRbar / d2."""
    values = [10.0, 11.0, 12.0, 11.0, 10.0]
    x_limits, mr_limits, obs, ranges = _imr_limits(values, span=2)

    expected_sigma = float(np.mean([1.0, 1.0, 1.0, 1.0])) / get_d2(2)
    assert x_limits.sigma == pytest.approx(expected_sigma)
    assert x_limits.center == pytest.approx(np.mean(values))
    assert x_limits.upper == pytest.approx(x_limits.center + 3 * expected_sigma)
    assert mr_limits.lower == pytest.approx(0.0)
    assert mr_limits.upper == pytest.approx(
        get_spc_constants(2).d4 * float(ranges.mean())
    )


def test_median_limits_use_a2_constant():
    """Median-chart limits center on the mean of subgroup medians using A2 * Rbar."""
    data = np.array([[10, 12, 11, 13, 12], [9, 11, 10, 12, 11], [12, 13, 12, 14, 13]])
    limits, medians = _median_limits(data)

    rbar = float((data.max(axis=1) - data.min(axis=1)).mean())
    center = float(np.median(data, axis=1).mean())
    assert limits.center == pytest.approx(center)
    assert medians.tolist() == pytest.approx([12.0, 11.0, 13.0])
    assert limits.upper == pytest.approx(center + get_spc_constants(5).a2 * rbar)


def test_t_chart_limits_are_positive_and_back_transformed():
    """t-chart limits stay on a positive time scale after back-transformation."""
    times = [4.0, 6.0, 5.0, 8.0, 3.0, 7.0]
    values, limits = _t_chart_limits(times)

    assert limits.lower >= 0.0
    assert limits.upper > limits.center > limits.lower
    assert values.tolist() == pytest.approx(times)


def test_laney_p_limits_reduce_to_binomial_without_overdispersion():
    """Laney p' limits center on pbar and step per sample size within the proportion range."""
    defects = [5, 6, 4, 5, 6, 5]
    sizes = [100, 100, 100, 100, 100, 100]
    proportions, center, lower, upper = _laney_p_limits(defects, sizes)

    pbar = sum(defects) / sum(sizes)
    assert center == pytest.approx(pbar)
    assert (lower >= 0.0).all() and (upper <= 1.0).all()
    assert (lower <= upper).all()
    assert len(upper) == len(defects)
    assert proportions.tolist() == pytest.approx([d / 100 for d in defects])


def test_laney_p_limits_step_with_sample_size():
    """Laney p' limits widen for smaller samples, so per-sample limits vary."""
    defects = [5, 3, 6, 2, 5, 3]
    sizes = [200, 50, 200, 50, 200, 50]
    _, _, lower, upper = _laney_p_limits(defects, sizes)

    widths = (upper - lower).round(6)
    assert widths.nunique() > 1


def test_laney_u_limits_center_on_ubar():
    """Laney u' limits center on the overall defects-per-unit rate and step per subgroup."""
    defects = [4, 6, 5, 7, 3]
    units = [10, 12, 11, 13, 9]
    rates, center, lower, upper = _laney_u_limits(defects, units)

    ubar = sum(defects) / sum(units)
    assert center == pytest.approx(ubar)
    assert (lower >= 0.0).all()
    assert len(upper) == len(defects)
    assert rates.tolist() == pytest.approx([d / u for d, u in zip(defects, units)])


_RNG = np.random.default_rng(7)
_IND = _RNG.normal(10.0, 1.0, 40)
_SUB = _RNG.normal(10.0, 1.0, (30, 5))
_COUNTS_BETWEEN = _RNG.integers(0, 20, 30)
_TIMES = _RNG.exponential(5.0, 30) + 0.1
_DEFECTS = _RNG.integers(0, 8, 30)
_SIZES = _RNG.integers(80, 120, 30)
_UNITS = _RNG.integers(5, 15, 30)
_QC = _RNG.normal(100.0, 2.0, 40)

_NEW_STATIC_CHARTS = [
    ("imr_chart_static", (_IND,), {}),
    ("median_chart_static", (_SUB,), {}),
    ("levey_jennings_chart_static", (_QC,), {}),
    ("g_chart_static", (_COUNTS_BETWEEN,), {}),
    ("t_chart_static", (_TIMES,), {}),
    ("laney_p_chart_static", (_DEFECTS, _SIZES), {}),
    ("laney_u_chart_static", (_DEFECTS, _UNITS), {}),
]

_NEW_INTERACTIVE_CHARTS = [
    ("imr_chart_interactive", (_IND,), {}),
    ("median_chart_interactive", (_SUB,), {}),
    ("levey_jennings_chart_interactive", (_QC,), {}),
    ("g_chart_interactive", (_COUNTS_BETWEEN,), {}),
    ("t_chart_interactive", (_TIMES,), {}),
    ("laney_p_chart_interactive", (_DEFECTS, _SIZES), {}),
    ("laney_u_chart_interactive", (_DEFECTS, _UNITS), {}),
]


@pytest.mark.parametrize("name, args, kwargs", _NEW_STATIC_CHARTS)
def test_new_static_spc_charts_construct(name, args, kwargs):
    """New static SPC chart constructors return matplotlib artists."""
    result = getattr(spc, name)(*args, **kwargs)
    plt.close("all")
    assert result is not None


@pytest.mark.parametrize("name, args, kwargs", _NEW_INTERACTIVE_CHARTS)
def test_new_interactive_spc_charts_construct(name, args, kwargs):
    """New interactive SPC chart constructors return Plotly figures."""
    figure = getattr(spc, name)(*args, **kwargs)
    assert isinstance(figure, go.Figure)
