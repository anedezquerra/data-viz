"""Curated rich examples for spc member pages."""

EXAMPLES = {
    "dataviz.spc.attribute.p_chart_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.spc.attribute import p_chart_static

rng = np.random.default_rng(42)
# 30 shifts of filling-line inspection with varying sample sizes
sample_sizes = rng.integers(180, 260, size=30)
defects = rng.binomial(sample_sizes, 0.04)
defects[24] = 28  # special cause after a supplier lot change

ax = p_chart_static(defects, sample_sizes, title="Filling Line - Proportion Defective per Shift")
ax.set_xlabel("Shift")
plt.show()''',
    "dataviz.spc.attribute.p_chart_interactive": '''import numpy as np
from dataviz.spc.attribute import p_chart_interactive

rng = np.random.default_rng(42)
# 30 shifts of filling-line inspection with varying sample sizes
sample_sizes = rng.integers(180, 260, size=30)
defects = rng.binomial(sample_sizes, 0.04)
defects[24] = 28  # special cause after a supplier lot change

fig = p_chart_interactive(defects, sample_sizes, title="Filling Line - Proportion Defective per Shift")
fig.show()''',
    "dataviz.spc.attribute.np_chart_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.spc.attribute import np_chart_static

rng = np.random.default_rng(42)
# 28 incoming lots, 200 parts inspected from each lot
defects = rng.binomial(200, 0.04, size=28)
defects[19] = 19  # lot from a new supplier runs high

ax = np_chart_static(defects, sample_size=200, title="Incoming Inspection - Defective Parts per Lot")
ax.set_xlabel("Lot")
plt.show()''',
    "dataviz.spc.attribute.np_chart_interactive": '''import numpy as np
from dataviz.spc.attribute import np_chart_interactive

rng = np.random.default_rng(42)
# 28 incoming lots, 200 parts inspected from each lot
defects = rng.binomial(200, 0.04, size=28)
defects[19] = 19  # lot from a new supplier runs high

fig = np_chart_interactive(defects, sample_size=200, title="Incoming Inspection - Defective Parts per Lot")
fig.show()''',
    "dataviz.spc.attribute.c_chart_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.spc.attribute import c_chart_static

rng = np.random.default_rng(42)
# Surface defects counted on 28 painted panels (constant inspection area)
defects = rng.poisson(3.5, size=28)
defects[21] = 14  # spray nozzle clog on panel 21

ax = c_chart_static(defects, title="Painted Panels - Surface Defects per Panel")
ax.set_xlabel("Panel")
plt.show()''',
    "dataviz.spc.attribute.c_chart_interactive": '''import numpy as np
from dataviz.spc.attribute import c_chart_interactive

rng = np.random.default_rng(42)
# Surface defects counted on 28 painted panels (constant inspection area)
defects = rng.poisson(3.5, size=28)
defects[21] = 14  # spray nozzle clog on panel 21

fig = c_chart_interactive(defects, title="Painted Panels - Surface Defects per Panel")
fig.show()''',
    "dataviz.spc.attribute.u_chart_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.spc.attribute import u_chart_static

rng = np.random.default_rng(42)
# Defects per fabric roll with varying roll lengths
units = rng.integers(8, 16, size=30)
defects = rng.poisson(units * 0.4)
defects[22] = 18  # loom tension fault on roll 22

ax = u_chart_static(defects, units, title="Fabric Rolls - Defects per Unit")
ax.set_xlabel("Roll")
plt.show()''',
    "dataviz.spc.attribute.u_chart_interactive": '''import numpy as np
from dataviz.spc.attribute import u_chart_interactive

rng = np.random.default_rng(42)
# Defects per fabric roll with varying roll lengths
units = rng.integers(8, 16, size=30)
defects = rng.poisson(units * 0.4)
defects[22] = 18  # loom tension fault on roll 22

fig = u_chart_interactive(defects, units, title="Fabric Rolls - Defects per Unit")
fig.show()''',
    "dataviz.spc.attribute.g_chart_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.spc.attribute import g_chart_static

rng = np.random.default_rng(42)
# Units produced between rare contamination events on a filling line
counts = rng.geometric(p=0.03, size=25)
counts[15] = 160  # unusually long clean run after filter upgrade

ax = g_chart_static(counts, title="Contamination Events - Units Between Occurrences")
ax.set_xlabel("Event Number")
plt.show()''',
    "dataviz.spc.attribute.g_chart_interactive": '''import numpy as np
from dataviz.spc.attribute import g_chart_interactive

rng = np.random.default_rng(42)
# Units produced between rare contamination events on a filling line
counts = rng.geometric(p=0.03, size=25)
counts[15] = 160  # unusually long clean run after filter upgrade

fig = g_chart_interactive(counts, title="Contamination Events - Units Between Occurrences")
fig.show()''',
    "dataviz.spc.attribute.t_chart_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.spc.attribute import t_chart_static

rng = np.random.default_rng(42)
# Hours between recordable safety incidents across a plant
times = rng.exponential(scale=12.0, size=25)
times[14] = 85.0  # long incident-free stretch after retraining

ax = t_chart_static(times, title="Safety Incidents - Hours Between Events")
ax.set_xlabel("Event Number")
plt.show()''',
    "dataviz.spc.attribute.t_chart_interactive": '''import numpy as np
from dataviz.spc.attribute import t_chart_interactive

rng = np.random.default_rng(42)
# Hours between recordable safety incidents across a plant
times = rng.exponential(scale=12.0, size=25)
times[14] = 85.0  # long incident-free stretch after retraining

fig = t_chart_interactive(times, title="Safety Incidents - Hours Between Events")
fig.show()''',
    "dataviz.spc.attribute.laney_p_chart_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.spc.attribute import laney_p_chart_static

rng = np.random.default_rng(42)
# Large, widely varying supplier-lot samples with overdispersion
sample_sizes = rng.integers(400, 900, size=30)
defects = rng.binomial(sample_sizes, 0.05)
defects[24] = 120  # special cause from a tooling drift

ax = laney_p_chart_static(defects, sample_sizes, title="Supplier Lots - Defect Rate (Laney p-prime)")
ax.set_xlabel("Lot")
plt.show()''',
    "dataviz.spc.attribute.laney_p_chart_interactive": '''import numpy as np
from dataviz.spc.attribute import laney_p_chart_interactive

rng = np.random.default_rng(42)
# Large, widely varying supplier-lot samples with overdispersion
sample_sizes = rng.integers(400, 900, size=30)
defects = rng.binomial(sample_sizes, 0.05)
defects[24] = 120  # special cause from a tooling drift

fig = laney_p_chart_interactive(defects, sample_sizes, title="Supplier Lots - Defect Rate (Laney p-prime)")
fig.show()''',
    "dataviz.spc.attribute.laney_u_chart_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.spc.attribute import laney_u_chart_static

rng = np.random.default_rng(42)
# Cable defects per unit with varying production volumes and overdispersion
units = rng.integers(20, 60, size=28)
defects = rng.poisson(units * 0.6)
defects[20] = 70  # extruder contamination event

ax = laney_u_chart_static(defects, units, title="Cable Production - Defects per Unit (Laney u-prime)")
ax.set_xlabel("Batch")
plt.show()''',
    "dataviz.spc.attribute.laney_u_chart_interactive": '''import numpy as np
from dataviz.spc.attribute import laney_u_chart_interactive

rng = np.random.default_rng(42)
# Cable defects per unit with varying production volumes and overdispersion
units = rng.integers(20, 60, size=28)
defects = rng.poisson(units * 0.6)
defects[20] = 70  # extruder contamination event

fig = laney_u_chart_interactive(defects, units, title="Cable Production - Defects per Unit (Laney u-prime)")
fig.show()''',
    "dataviz.spc.capability.CapabilityStats": '''from dataviz.spc.capability import CapabilityStats

# Capability summary recorded for a 500 g filling process
result = CapabilityStats(
    n=60,
    mean=500.1,
    std=1.2,
    lsl=497.0,
    usl=503.0,
    cp=0.833,
    cpk=0.806,
    ppm_below=0.0,
    ppm_above=0.0,
    ppm_below_normal=5123.4,
    ppm_above_normal=4012.6,
    ppm_total_normal=9136.0,
)
print(result)''',
    "dataviz.spc.capability.capability_summary": '''import numpy as np
from dataviz.spc.capability import capability_summary

rng = np.random.default_rng(42)
# Fill weights (g) from a bottling line, spec 497-503 g
weights = rng.normal(500.0, 1.2, size=60)
weights[41] = 504.8  # overfilled bottle after valve wear

result = capability_summary(weights, lsl=497.0, usl=503.0)
print(result)''',
    "dataviz.spc.capability.capability_histogram_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.spc.capability import capability_histogram_static

rng = np.random.default_rng(42)
# Fill weights (g) from a bottling line, spec 497-503 g
weights = rng.normal(500.0, 1.2, size=60)
weights[41] = 504.8  # overfilled bottle after valve wear

ax = capability_histogram_static(
    weights, lsl=497.0, usl=503.0, bins=20, title="Fill Weight Capability"
)
ax.set_xlabel("Fill weight (g)")
plt.show()''',
    "dataviz.spc.capability.capability_histogram_interactive": '''import numpy as np
from dataviz.spc.capability import capability_histogram_interactive

rng = np.random.default_rng(42)
# Fill weights (g) from a bottling line, spec 497-503 g
weights = rng.normal(500.0, 1.2, size=60)
weights[41] = 504.8  # overfilled bottle after valve wear

fig = capability_histogram_interactive(
    weights, lsl=497.0, usl=503.0, bins=20, title="Fill Weight Capability"
)
fig.show()''',
    "dataviz.spc.charts.control_chart": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.spc.charts import control_chart

rng = np.random.default_rng(42)
# Oven temperature (deg C) logged every 15 minutes over one shift
temps = rng.normal(180.0, 1.5, size=30)
temps[22] = 186.4  # heating element surge

ax = control_chart(temps, title="Oven Temperature Control Chart", ylabel="Temperature (deg C)")
plt.show()''',
    "dataviz.spc.charts.x_range_chart": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.spc.charts import x_range_chart

rng = np.random.default_rng(42)
# Shaft diameters (mm) sampled from a CNC lathe
diameters = rng.normal(25.0, 0.08, size=30)
diameters[19] = 25.42  # tool wear spike

ax = x_range_chart(
    diameters, subgroup_size=5, title="Shaft Diameter X-Range Chart", ylabel="Diameter (mm)"
)
plt.show()''',
    "dataviz.spc.constants.SPCConstants": '''from dataviz.spc.constants import SPCConstants

# Constants for a subgroup size of 5, as used on a machining line
result = SPCConstants(
    n=5, a2=0.577, d3=0.0, d4=2.114, a3=1.427, b3=0.0, b4=2.089, c4=0.94
)
print(result)''',
    "dataviz.spc.constants.get_d2": '''from dataviz.spc.constants import get_d2

# Estimate sigma from the mean moving range of a filling line
mean_moving_range = 0.32
result = mean_moving_range / get_d2(2)
print(result)''',
    "dataviz.spc.constants.get_spc_constants": '''from dataviz.spc.constants import get_spc_constants

# Constants for subgroups of 5 pulled hourly from a packaging line
result = get_spc_constants(5)
print(result)''',
    "dataviz.spc.control.control_chart_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.spc.control import control_chart_static

rng = np.random.default_rng(42)
# Oven temperature (deg C) logged every 15 minutes over one shift
temps = rng.normal(180.0, 1.5, size=30)
temps[22] = 186.4  # heating element surge

ax = control_chart_static(
    temps,
    title="Oven Temperature Control Chart",
    ylabel="Temperature (deg C)",
    sigma_multiplier=3.0,
    color_data="navy",
    marker_size=5,
)
plt.show()''',
    "dataviz.spc.control.control_chart_interactive": '''import numpy as np
from dataviz.spc.control import control_chart_interactive

rng = np.random.default_rng(42)
# Oven temperature (deg C) logged every 15 minutes over one shift
temps = rng.normal(180.0, 1.5, size=30)
temps[22] = 186.4  # heating element surge

fig = control_chart_interactive(
    temps,
    title="Oven Temperature Control Chart",
    ylabel="Temperature (deg C)",
    marker_size=6,
)
fig.show()''',
    "dataviz.spc.dashboard.spc_dashboard_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.spc.dashboard import spc_dashboard_static

rng = np.random.default_rng(42)
# Moisture content (%) of granola batches across 36 production runs
moisture = rng.normal(12.0, 0.3, size=36)
moisture[26] = 13.4  # dryer malfunction on run 26

fig = spc_dashboard_static(
    moisture, span=2, bins=15, title="Granola Moisture Content - SPC Dashboard"
)
plt.show()''',
    "dataviz.spc.dashboard.spc_dashboard_interactive": '''import numpy as np
from dataviz.spc.dashboard import spc_dashboard_interactive

rng = np.random.default_rng(42)
# Moisture content (%) of granola batches across 36 production runs
moisture = rng.normal(12.0, 0.3, size=36)
moisture[26] = 13.4  # dryer malfunction on run 26

fig = spc_dashboard_interactive(
    moisture, span=2, bins=15, title="Granola Moisture Content - SPC Dashboard"
)
fig.show()''',
    "dataviz.spc.diagnostics.run_chart_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.spc.diagnostics import run_chart_static

rng = np.random.default_rng(42)
# Changeover time (minutes) for 32 consecutive line changeovers
changeover = rng.normal(45.0, 3.0, size=32)
changeover[24:] -= 6.0  # improvement after SMED kaizen event

ax = run_chart_static(changeover, title="Changeover Time Run Chart", show_median=True)
ax.set_ylabel("Changeover time (min)")
plt.show()''',
    "dataviz.spc.diagnostics.run_chart_interactive": '''import numpy as np
from dataviz.spc.diagnostics import run_chart_interactive

rng = np.random.default_rng(42)
# Changeover time (minutes) for 32 consecutive line changeovers
changeover = rng.normal(45.0, 3.0, size=32)
changeover[24:] -= 6.0  # improvement after SMED kaizen event

fig = run_chart_interactive(changeover, title="Changeover Time Run Chart", show_median=True)
fig.show()''',
    "dataviz.spc.diagnostics.rule_violation_chart_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.spc.diagnostics import rule_violation_chart_static

rng = np.random.default_rng(42)
# Batch pH from a fermentation process with a shift after a recipe change
ph = rng.normal(7.2, 0.05, size=30)
ph[18:] += 0.25  # upward shift after cleaning-cycle change

ax = rule_violation_chart_static(ph, title="Fermentation Batch pH - Rule Violations")
ax.set_ylabel("pH")
plt.show()''',
    "dataviz.spc.diagnostics.rule_violation_chart_interactive": '''import numpy as np
from dataviz.spc.diagnostics import rule_violation_chart_interactive

rng = np.random.default_rng(42)
# Batch pH from a fermentation process with a shift after a recipe change
ph = rng.normal(7.2, 0.05, size=30)
ph[18:] += 0.25  # upward shift after cleaning-cycle change

fig = rule_violation_chart_interactive(ph, title="Fermentation Batch pH - Rule Violations")
fig.show()''',
    "dataviz.spc.diagnostics.pareto_chart_static": '''import matplotlib.pyplot as plt
from dataviz.spc.diagnostics import pareto_chart_static

# Surface defect tally from a quarter of final visual inspection
categories = ["Scratch", "Dent", "Contamination", "Misprint", "Crack", "Discoloration"]
counts = [87, 54, 38, 22, 11, 6]

ax = pareto_chart_static(categories, counts, title="Q3 Surface Defect Pareto")
plt.show()''',
    "dataviz.spc.diagnostics.pareto_chart_interactive": '''from dataviz.spc.diagnostics import pareto_chart_interactive

# Surface defect tally from a quarter of final visual inspection
categories = ["Scratch", "Dent", "Contamination", "Misprint", "Crack", "Discoloration"]
counts = [87, 54, 38, 22, 11, 6]

fig = pareto_chart_interactive(categories, counts, title="Q3 Surface Defect Pareto")
fig.show()''',
    "dataviz.spc.diagnostics.process_distribution_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.spc.diagnostics import process_distribution_static

rng = np.random.default_rng(42)
# Fill weights (g) collected during a capability study on line 3
weights = rng.normal(500.0, 1.1, size=40)
weights[33] = 504.6  # overfill after valve wear

ax = process_distribution_static(weights, bins=15, title="Line 3 Fill Weight Distribution")
ax.set_xlabel("Fill weight (g)")
plt.show()''',
    "dataviz.spc.diagnostics.process_distribution_interactive": '''import numpy as np
from dataviz.spc.diagnostics import process_distribution_interactive

rng = np.random.default_rng(42)
# Fill weights (g) collected during a capability study on line 3
weights = rng.normal(500.0, 1.1, size=40)
weights[33] = 504.6  # overfill after valve wear

fig = process_distribution_interactive(weights, bins=15, title="Line 3 Fill Weight Distribution")
fig.show()''',
    "dataviz.spc.diagnostics.zone_chart_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.spc.diagnostics import zone_chart_static

rng = np.random.default_rng(42)
# Reactor temperature (deg C) sampled hourly with a slow upward drift
temps = rng.normal(85.0, 0.8, size=30)
temps[22:] += np.linspace(0.0, 1.8, 8)  # fouling heat exchanger

ax = zone_chart_static(temps, title="Reactor Temperature Zone Chart")
ax.set_ylabel("Temperature (deg C)")
plt.show()''',
    "dataviz.spc.diagnostics.zone_chart_interactive": '''import numpy as np
from dataviz.spc.diagnostics import zone_chart_interactive

rng = np.random.default_rng(42)
# Reactor temperature (deg C) sampled hourly with a slow upward drift
temps = rng.normal(85.0, 0.8, size=30)
temps[22:] += np.linspace(0.0, 1.8, 8)  # fouling heat exchanger

fig = zone_chart_interactive(temps, title="Reactor Temperature Zone Chart")
fig.show()''',
    "dataviz.spc.multivariate.HotellingT2Result": '''import numpy as np
import pandas as pd
from dataviz.spc.multivariate import HotellingT2Result

# T-squared monitoring result for a reactor temp/pressure loop
scores = pd.Series([1.2, 2.0, 0.8, 5.4], name="T2")
center = pd.Series({"temp": 180.0, "pressure": 4.2})
covariance = pd.DataFrame(np.eye(2), index=["temp", "pressure"], columns=["temp", "pressure"])
result = HotellingT2Result(scores=scores, center=center, covariance=covariance, limit=4.0)
print(result)''',
    "dataviz.spc.multivariate.hotelling_t2_summary": '''import numpy as np
import pandas as pd
from dataviz.spc.multivariate import hotelling_t2_summary

rng = np.random.default_rng(42)
# 30 hourly readings of correlated reactor variables
temp = rng.normal(180.0, 1.5, size=30)
pressure = 4.0 + 0.02 * (temp - 180.0) + rng.normal(0.0, 0.05, size=30)
flow = rng.normal(12.0, 0.4, size=30)
temp[24] = 185.8  # heater excursion
df = pd.DataFrame({"temp": temp, "pressure": pressure, "flow": flow})

result = hotelling_t2_summary(df, limit_quantile=0.99)
print(result)''',
    "dataviz.spc.multivariate.hotelling_t2_chart_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.spc.multivariate import hotelling_t2_chart_static

rng = np.random.default_rng(42)
# 30 hourly readings of correlated reactor variables
temp = rng.normal(180.0, 1.5, size=30)
pressure = 4.0 + 0.02 * (temp - 180.0) + rng.normal(0.0, 0.05, size=30)
flow = rng.normal(12.0, 0.4, size=30)
temp[24] = 185.8  # heater excursion
df = pd.DataFrame({"temp": temp, "pressure": pressure, "flow": flow})

ax = hotelling_t2_chart_static(df, limit_quantile=0.99, title="Reactor Hotelling T-squared Chart")
plt.show()''',
    "dataviz.spc.multivariate.hotelling_t2_chart_interactive": '''import numpy as np
import pandas as pd
from dataviz.spc.multivariate import hotelling_t2_chart_interactive

rng = np.random.default_rng(42)
# 30 hourly readings of correlated reactor variables
temp = rng.normal(180.0, 1.5, size=30)
pressure = 4.0 + 0.02 * (temp - 180.0) + rng.normal(0.0, 0.05, size=30)
flow = rng.normal(12.0, 0.4, size=30)
temp[24] = 185.8  # heater excursion
df = pd.DataFrame({"temp": temp, "pressure": pressure, "flow": flow})

fig = hotelling_t2_chart_interactive(df, limit_quantile=0.99, title="Reactor Hotelling T-squared Chart")
fig.show()''',
    "dataviz.spc.rules.ControlLimits": '''from dataviz.spc.rules import ControlLimits

# Individuals-chart limits for a 500 g filling process
result = ControlLimits(center=500.2, lower=497.1, upper=503.3, sigma=1.03)
print(result)''',
    "dataviz.spc.rules.RuleViolation": '''from dataviz.spc.rules import RuleViolation

# Violation logged when shift 24 exceeded the upper control limit
result = RuleViolation(
    index=24, value=508.7, rule="beyond_limits", message="Point outside control limits"
)
print(result)''',
    "dataviz.spc.rules.as_numeric_series": '''from dataviz.spc.rules import as_numeric_series

# Raw fill-weight log entries from a text export (strings and a gap)
raw = ["500.2", "499.8", None, "501.1", "500.6", "499.5", "500.9"]
result = as_numeric_series(raw, name="Fill Weight")
print(result)''',
    "dataviz.spc.rules.individuals_limits": '''import numpy as np
from dataviz.spc.rules import individuals_limits

rng = np.random.default_rng(42)
# Fill weights (g) from 30 consecutive bottles on a filling line
weights = rng.normal(500.0, 1.1, size=30)
weights[24] = 504.9  # overfill after valve wear

result = individuals_limits(weights, sigma_multiplier=3.0)
print(result)''',
    "dataviz.spc.rules.moving_ranges": '''import numpy as np
from dataviz.spc.rules import moving_ranges

rng = np.random.default_rng(42)
# Fill weights (g) from 30 consecutive bottles on a filling line
weights = rng.normal(500.0, 1.1, size=30)
weights[24] = 504.9  # overfill after valve wear

result = moving_ranges(weights, span=2)
print(result)''',
    "dataviz.spc.rules.subgroup_matrix": '''import numpy as np
from dataviz.spc.rules import subgroup_matrix

rng = np.random.default_rng(42)
# Torque readings (N m) from 25 subgroups of 5 fasteners each
torque = rng.normal(18.0, 0.6, size=125)

result = subgroup_matrix(torque, subgroup_size=5)
print(result)''',
    "dataviz.spc.rules.xbar_r_limits": '''import numpy as np
from dataviz.spc.rules import xbar_r_limits

rng = np.random.default_rng(42)
# Shaft diameters (mm): 25 subgroups of 5 parts from a CNC lathe
diameters = rng.normal(25.0, 0.08, size=125)
diameters[100:105] += 0.25  # tool wear shift in subgroup 20

result = xbar_r_limits(diameters, subgroup_size=5)
print(result)''',
    "dataviz.spc.rules.xbar_s_limits": '''import numpy as np
from dataviz.spc.rules import xbar_s_limits

rng = np.random.default_rng(42)
# Viscosity readings (cP): 22 subgroups of 6 samples per batch
viscosity = rng.normal(350.0, 4.0, size=132)
viscosity[90:96] += 14.0  # raw-material change in subgroup 15

result = xbar_s_limits(viscosity, subgroup_size=6)
print(result)''',
    "dataviz.spc.rules.detect_rule_violations": '''import numpy as np
from dataviz.spc.rules import detect_rule_violations

rng = np.random.default_rng(42)
# Coating thickness (microns) with a spike and a sustained shift
thickness = rng.normal(100.0, 1.0, size=32)
thickness[22] = 105.1  # spray gun surge beyond limits
thickness[26:] += 2.5  # nozzle wear shifts the process mean

result = detect_rule_violations(thickness, run_length=8, trend_length=6)
print(result)''',
    "dataviz.spc.rules.violations_by_index": '''import numpy as np
from dataviz.spc.rules import detect_rule_violations, violations_by_index

rng = np.random.default_rng(42)
# Coating thickness (microns) with a spike and a sustained shift
thickness = rng.normal(100.0, 1.0, size=32)
thickness[22] = 105.1  # spray gun surge beyond limits
thickness[26:] += 2.5  # nozzle wear shifts the process mean

violations = detect_rule_violations(thickness)
result = violations_by_index(violations)
print(result)''',
    "dataviz.spc.variable.moving_range_chart_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.spc.variable import moving_range_chart_static

rng = np.random.default_rng(42)
# Fill weights (g) from 30 consecutive bottles on a filling line
weights = rng.normal(500.0, 1.1, size=30)
weights[24] = 504.9  # overfill after valve wear

ax = moving_range_chart_static(weights, span=2, title="Fill Weight Moving Range")
ax.set_ylabel("Moving range (g)")
plt.show()''',
    "dataviz.spc.variable.moving_range_chart_interactive": '''import numpy as np
from dataviz.spc.variable import moving_range_chart_interactive

rng = np.random.default_rng(42)
# Fill weights (g) from 30 consecutive bottles on a filling line
weights = rng.normal(500.0, 1.1, size=30)
weights[24] = 504.9  # overfill after valve wear

fig = moving_range_chart_interactive(weights, span=2, title="Fill Weight Moving Range")
fig.show()''',
    "dataviz.spc.variable.xbar_r_chart_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.spc.variable import xbar_r_chart_static

rng = np.random.default_rng(42)
# Shaft diameters (mm): 25 subgroups of 5 parts from a CNC lathe
diameters = rng.normal(25.0, 0.08, size=125)
diameters[100:105] += 0.25  # tool wear shift in subgroup 20

ax_xbar, ax_r = xbar_r_chart_static(
    diameters, subgroup_size=5, title="Shaft Diameter Xbar-R Chart"
)
ax_xbar.set_ylabel("Subgroup mean (mm)")
plt.show()''',
    "dataviz.spc.variable.xbar_r_chart_interactive": '''import numpy as np
from dataviz.spc.variable import xbar_r_chart_interactive

rng = np.random.default_rng(42)
# Shaft diameters (mm): 25 subgroups of 5 parts from a CNC lathe
diameters = rng.normal(25.0, 0.08, size=125)
diameters[100:105] += 0.25  # tool wear shift in subgroup 20

fig = xbar_r_chart_interactive(
    diameters, subgroup_size=5, title="Shaft Diameter Xbar-R Chart"
)
fig.show()''',
    "dataviz.spc.variable.xbar_s_chart_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.spc.variable import xbar_s_chart_static

rng = np.random.default_rng(42)
# Viscosity readings (cP): 22 subgroups of 6 samples per batch
viscosity = rng.normal(350.0, 4.0, size=132)
viscosity[90:96] += 14.0  # raw-material change in subgroup 15

ax_xbar, ax_s = xbar_s_chart_static(
    viscosity, subgroup_size=6, title="Batch Viscosity Xbar-S Chart"
)
ax_xbar.set_ylabel("Subgroup mean (cP)")
plt.show()''',
    "dataviz.spc.variable.xbar_s_chart_interactive": '''import numpy as np
from dataviz.spc.variable import xbar_s_chart_interactive

rng = np.random.default_rng(42)
# Viscosity readings (cP): 22 subgroups of 6 samples per batch
viscosity = rng.normal(350.0, 4.0, size=132)
viscosity[90:96] += 14.0  # raw-material change in subgroup 15

fig = xbar_s_chart_interactive(
    viscosity, subgroup_size=6, title="Batch Viscosity Xbar-S Chart"
)
fig.show()''',
    "dataviz.spc.variable.ewma_chart_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.spc.variable import ewma_chart_static

rng = np.random.default_rng(42)
# Film thickness (mm) with a slow drift from die-lip buildup
thickness = rng.normal(2.0, 0.02, size=32)
thickness[20:] += np.linspace(0.0, 0.06, 12)  # gradual drift

ax = ewma_chart_static(thickness, lambda_=0.25, title="Film Thickness EWMA Chart")
ax.set_ylabel("Thickness (mm)")
plt.show()''',
    "dataviz.spc.variable.ewma_chart_interactive": '''import numpy as np
from dataviz.spc.variable import ewma_chart_interactive

rng = np.random.default_rng(42)
# Film thickness (mm) with a slow drift from die-lip buildup
thickness = rng.normal(2.0, 0.02, size=32)
thickness[20:] += np.linspace(0.0, 0.06, 12)  # gradual drift

fig = ewma_chart_interactive(thickness, lambda_=0.25, title="Film Thickness EWMA Chart")
fig.show()''',
    "dataviz.spc.variable.cusum_chart_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.spc.variable import cusum_chart_static

rng = np.random.default_rng(42)
# Fill weights (g) with a small sustained shift that a Shewhart chart misses
weights = rng.normal(500.0, 1.0, size=32)
weights[22:] += 1.5  # slow valve drift shifts the mean

ax = cusum_chart_static(
    weights, target=500.0, k=0.5, h=5.0, title="Fill Weight CUSUM Chart"
)
plt.show()''',
    "dataviz.spc.variable.cusum_chart_interactive": '''import numpy as np
from dataviz.spc.variable import cusum_chart_interactive

rng = np.random.default_rng(42)
# Fill weights (g) with a small sustained shift that a Shewhart chart misses
weights = rng.normal(500.0, 1.0, size=32)
weights[22:] += 1.5  # slow valve drift shifts the mean

fig = cusum_chart_interactive(
    weights, target=500.0, k=0.5, h=5.0, title="Fill Weight CUSUM Chart"
)
fig.show()''',
    "dataviz.spc.variable.imr_chart_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.spc.variable import imr_chart_static

rng = np.random.default_rng(42)
# Product purity (%) measured once per batch (individuals data)
purity = rng.normal(99.2, 0.15, size=30)
purity[23] = 98.4  # contaminated raw-material drum

ax_i, ax_mr = imr_chart_static(purity, span=2, title="Batch Purity I-MR Chart")
ax_i.set_ylabel("Purity (%)")
plt.show()''',
    "dataviz.spc.variable.imr_chart_interactive": '''import numpy as np
from dataviz.spc.variable import imr_chart_interactive

rng = np.random.default_rng(42)
# Product purity (%) measured once per batch (individuals data)
purity = rng.normal(99.2, 0.15, size=30)
purity[23] = 98.4  # contaminated raw-material drum

fig = imr_chart_interactive(purity, span=2, title="Batch Purity I-MR Chart")
fig.show()''',
    "dataviz.spc.variable.median_chart_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.spc.variable import median_chart_static

rng = np.random.default_rng(42)
# Hardness readings (HRC): 24 subgroups of 5 parts from heat treatment
hardness = rng.normal(58.0, 1.2, size=120)
hardness[75:80] -= 3.5  # quench-tank temperature drop in subgroup 15

ax = median_chart_static(hardness, subgroup_size=5, title="Part Hardness Median Chart")
ax.set_ylabel("Subgroup median (HRC)")
plt.show()''',
    "dataviz.spc.variable.median_chart_interactive": '''import numpy as np
from dataviz.spc.variable import median_chart_interactive

rng = np.random.default_rng(42)
# Hardness readings (HRC): 24 subgroups of 5 parts from heat treatment
hardness = rng.normal(58.0, 1.2, size=120)
hardness[75:80] -= 3.5  # quench-tank temperature drop in subgroup 15

fig = median_chart_interactive(hardness, subgroup_size=5, title="Part Hardness Median Chart")
fig.show()''',
    "dataviz.spc.variable.levey_jennings_chart_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.spc.variable import levey_jennings_chart_static

rng = np.random.default_rng(42)
# Daily runs of a glucose control material (mean 5.5, sd 0.12 mmol/L)
qc = rng.normal(5.5, 0.12, size=30)
qc[21] = 5.98  # reagent lot change pushes one run past 3 sd

ax = levey_jennings_chart_static(
    qc, mean=5.5, sd=0.12, title="Glucose Control Level 1 - Levey-Jennings"
)
ax.set_ylabel("Glucose (mmol/L)")
plt.show()''',
    "dataviz.spc.variable.levey_jennings_chart_interactive": '''import numpy as np
from dataviz.spc.variable import levey_jennings_chart_interactive

rng = np.random.default_rng(42)
# Daily runs of a glucose control material (mean 5.5, sd 0.12 mmol/L)
qc = rng.normal(5.5, 0.12, size=30)
qc[21] = 5.98  # reagent lot change pushes one run past 3 sd

fig = levey_jennings_chart_interactive(
    qc, mean=5.5, sd=0.12, title="Glucose Control Level 1 - Levey-Jennings"
)
fig.show()''',
    "dataviz.spc.x_range.x_range_chart_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.spc.x_range import x_range_chart_static

rng = np.random.default_rng(42)
# Shaft diameters (mm) sampled from a CNC lathe
diameters = rng.normal(25.0, 0.08, size=30)
diameters[19] = 25.42  # tool wear spike

ax = x_range_chart_static(
    diameters, subgroup_size=5, title="Shaft Diameter X-Range Chart", ylabel="Diameter (mm)"
)
ax.set_xlabel("Sample")
plt.show()''',
    "dataviz.spc.x_range.x_range_chart_interactive": '''import numpy as np
from dataviz.spc.x_range import x_range_chart_interactive

rng = np.random.default_rng(42)
# Shaft diameters (mm) sampled from a CNC lathe
diameters = rng.normal(25.0, 0.08, size=30)
diameters[19] = 25.42  # tool wear spike

fig = x_range_chart_interactive(
    diameters, subgroup_size=5, title="Shaft Diameter X-Range Chart", ylabel="Diameter (mm)"
)
fig.show()''',
}
