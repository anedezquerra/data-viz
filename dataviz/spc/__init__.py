"""Statistical Process Control (SPC) charts - static and interactive versions."""

# Static (matplotlib) imports
from .control import control_chart_static
from .x_range import x_range_chart_static
from .variable import (
    moving_range_chart_static,
    xbar_r_chart_static,
    xbar_s_chart_static,
    ewma_chart_static,
    cusum_chart_static,
)
from .attribute import (
    p_chart_static,
    np_chart_static,
    c_chart_static,
    u_chart_static,
)
from .capability import (
    CapabilityStats,
    capability_summary,
    capability_histogram_static,
)
from .diagnostics import (
    run_chart_static,
    rule_violation_chart_static,
    pareto_chart_static,
    process_distribution_static,
    zone_chart_static,
)
from .multivariate import (
    HotellingT2Result,
    hotelling_t2_summary,
    hotelling_t2_chart_static,
)
from .dashboard import spc_dashboard_static
from .rules import (
    ControlLimits,
    RuleViolation,
    detect_rule_violations,
    individuals_limits,
    moving_ranges,
)
from .constants import SPCConstants, SPC_CONSTANTS, get_spc_constants

# Interactive (plotly) imports
from .control import control_chart_interactive
from .x_range import x_range_chart_interactive
from .variable import (
    moving_range_chart_interactive,
    xbar_r_chart_interactive,
    xbar_s_chart_interactive,
    ewma_chart_interactive,
    cusum_chart_interactive,
)
from .attribute import (
    p_chart_interactive,
    np_chart_interactive,
    c_chart_interactive,
    u_chart_interactive,
)
from .capability import capability_histogram_interactive
from .diagnostics import (
    run_chart_interactive,
    rule_violation_chart_interactive,
    pareto_chart_interactive,
    process_distribution_interactive,
    zone_chart_interactive,
)
from .multivariate import hotelling_t2_chart_interactive
from .dashboard import spc_dashboard_interactive

# Convenience aliases
control_chart = control_chart_static
x_range_chart = x_range_chart_static
moving_range_chart = moving_range_chart_static
xbar_r_chart = xbar_r_chart_static
xbar_s_chart = xbar_s_chart_static
ewma_chart = ewma_chart_static
cusum_chart = cusum_chart_static
p_chart = p_chart_static
np_chart = np_chart_static
c_chart = c_chart_static
u_chart = u_chart_static
capability_histogram = capability_histogram_static
run_chart = run_chart_static
rule_violation_chart = rule_violation_chart_static
pareto_chart = pareto_chart_static
process_distribution = process_distribution_static
zone_chart = zone_chart_static
hotelling_t2_chart = hotelling_t2_chart_static
spc_dashboard = spc_dashboard_static

__all__ = [
    # Static versions
    "control_chart_static",
    "x_range_chart_static",
    "moving_range_chart_static",
    "xbar_r_chart_static",
    "xbar_s_chart_static",
    "ewma_chart_static",
    "cusum_chart_static",
    "p_chart_static",
    "np_chart_static",
    "c_chart_static",
    "u_chart_static",
    "capability_histogram_static",
    "run_chart_static",
    "rule_violation_chart_static",
    "pareto_chart_static",
    "process_distribution_static",
    "zone_chart_static",
    "hotelling_t2_chart_static",
    "spc_dashboard_static",
    # Interactive versions
    "control_chart_interactive",
    "x_range_chart_interactive",
    "moving_range_chart_interactive",
    "xbar_r_chart_interactive",
    "xbar_s_chart_interactive",
    "ewma_chart_interactive",
    "cusum_chart_interactive",
    "p_chart_interactive",
    "np_chart_interactive",
    "c_chart_interactive",
    "u_chart_interactive",
    "capability_histogram_interactive",
    "run_chart_interactive",
    "rule_violation_chart_interactive",
    "pareto_chart_interactive",
    "process_distribution_interactive",
    "zone_chart_interactive",
    "hotelling_t2_chart_interactive",
    "spc_dashboard_interactive",
    # Statistical helpers
    "ControlLimits",
    "RuleViolation",
    "SPCConstants",
    "SPC_CONSTANTS",
    "CapabilityStats",
    "HotellingT2Result",
    "capability_summary",
    "hotelling_t2_summary",
    "detect_rule_violations",
    "individuals_limits",
    "moving_ranges",
    "get_spc_constants",
    # Aliases (default to static)
    "control_chart",
    "x_range_chart",
    "moving_range_chart",
    "xbar_r_chart",
    "xbar_s_chart",
    "ewma_chart",
    "cusum_chart",
    "p_chart",
    "np_chart",
    "c_chart",
    "u_chart",
    "capability_histogram",
    "run_chart",
    "rule_violation_chart",
    "pareto_chart",
    "process_distribution",
    "zone_chart",
    "hotelling_t2_chart",
    "spc_dashboard",
]
