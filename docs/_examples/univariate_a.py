"""Curated rich examples for univariate member pages."""

EXAMPLES = {
    # ------------------------------------------------------------------
    # dataviz.univariate.accessors
    # ------------------------------------------------------------------
    "dataviz.univariate.accessors.UnivariateInput": '''import pandas as pd
from dataviz.univariate.accessors import UnivariateInput

# Resolved input summary produced by a support-ticket logging system
wait_times = pd.Series(
    [4.2, 6.1, 3.8, 5.5, 7.0, 4.9, 6.6, 5.1, 3.4, 8.2],
    name="wait_time_min",
)
result = UnivariateInput(
    values=wait_times,
    name="wait_time_min",
    kind="numeric",
    missing_count=0,
)
print(result)''',
    "dataviz.univariate.accessors.resolve_univariate_data": '''import numpy as np
import pandas as pd
from dataviz.univariate.accessors import resolve_univariate_data

# Call-center log with a few abandoned calls recorded as missing
rng = np.random.default_rng(42)
calls = pd.DataFrame({
    "wait_time_min": np.round(rng.gamma(shape=2.0, scale=2.5, size=60), 1),
    "agent": rng.choice(["North", "South", "East", "West"], size=60),
})
calls.loc[rng.choice(calls.index, size=4, replace=False), "wait_time_min"] = np.nan

result = resolve_univariate_data(
    "wait_time_min",
    data=calls,
    na_policy="drop",
    require_numeric=True,
)
print(result.name, result.kind, result.missing_count)''',
    "dataviz.univariate.accessors.infer_univariate_kind": '''import numpy as np
import pandas as pd
from dataviz.univariate.accessors import infer_univariate_kind

# Survey satisfaction responses recorded as short text labels
rng = np.random.default_rng(42)
satisfaction = pd.Series(
    rng.choice(
        ["Very Satisfied", "Satisfied", "Neutral", "Dissatisfied"],
        size=50,
        p=[0.35, 0.35, 0.20, 0.10],
    ),
    name="satisfaction",
)

result = infer_univariate_kind(satisfaction)
print(result)''',
    "dataviz.univariate.accessors.numeric_or_none": '''import pandas as pd
from dataviz.univariate.accessors import numeric_or_none

# Device readings exported as text, with occasional sensor error codes
readings = pd.Series(
    ["21.4", "22.0", "ERR", "21.8", "23.1", "ERR", "22.6", "21.9",
     "22.3", "21.7", "22.8", "ERR", "21.5", "22.1", "22.4"],
    name="temperature_c",
)

result = numeric_or_none(readings)
print(result.describe())''',
    # ------------------------------------------------------------------
    # dataviz.univariate.advanced
    # ------------------------------------------------------------------
    "dataviz.univariate.advanced.rug_plot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.univariate.advanced import rug_plot_static

# Packet round-trip times captured on a network link
rng = np.random.default_rng(42)
latency_ms = pd.Series(
    np.round(rng.lognormal(mean=3.4, sigma=0.35, size=45), 1),
    name="latency_ms",
)

ax = rug_plot_static(
    latency_ms,
    title="Round-Trip Latency Observations",
    xlabel="Latency (ms)",
    color="steelblue",
    height=0.6,
    alpha=0.6,
    theme="minimal",
)
ax.set_xlabel("Latency (ms)")
plt.show()''',
    "dataviz.univariate.advanced.rug_plot_interactive": '''import numpy as np
import pandas as pd
from dataviz.univariate.advanced import rug_plot_interactive

# Packet round-trip times captured on a network link
rng = np.random.default_rng(42)
latency_ms = pd.Series(
    np.round(rng.lognormal(mean=3.4, sigma=0.35, size=45), 1),
    name="latency_ms",
)

fig = rug_plot_interactive(
    latency_ms,
    title="Round-Trip Latency Observations",
    xlabel="Latency (ms)",
    color="steelblue",
    template="plotly_white",
)
fig.show()''',
    "dataviz.univariate.advanced.strip_plot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.univariate.advanced import strip_plot_static

# Daily coffee-shop transaction amounts over six weeks
rng = np.random.default_rng(42)
amounts = pd.Series(
    np.round(rng.gamma(shape=4.0, scale=1.8, size=42), 2),
    name="transaction_usd",
)

ax = strip_plot_static(
    amounts,
    title="Individual Transaction Amounts",
    ylabel="Amount (USD)",
    color="darkorange",
    jitter=0.12,
    alpha=0.75,
    seed=7,
    theme="minimal",
)
ax.axhline(amounts.mean(), color="crimson", linestyle="--", linewidth=1)
plt.show()''',
    "dataviz.univariate.advanced.strip_plot_interactive": '''import numpy as np
import pandas as pd
from dataviz.univariate.advanced import strip_plot_interactive

# Daily coffee-shop transaction amounts over six weeks
rng = np.random.default_rng(42)
amounts = pd.Series(
    np.round(rng.gamma(shape=4.0, scale=1.8, size=42), 2),
    name="transaction_usd",
)

fig = strip_plot_interactive(
    amounts,
    title="Individual Transaction Amounts",
    ylabel="Amount (USD)",
    color="darkorange",
    jitter=0.12,
    seed=7,
    template="plotly_white",
)
fig.show()''',
    "dataviz.univariate.advanced.dot_plot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.univariate.advanced import dot_plot_static

# Support tickets classified by resolution channel last quarter
rng = np.random.default_rng(42)
channels = pd.Series(
    rng.choice(
        ["Email", "Phone", "Chat", "Self-Service", "Social", "In Person", "Forum"],
        size=320,
        p=[0.28, 0.24, 0.20, 0.12, 0.08, 0.05, 0.03],
    ),
    name="channel",
)

ax = dot_plot_static(
    channels,
    title="Tickets by Resolution Channel",
    xlabel="Tickets Resolved",
    ylabel="Channel",
    color="seagreen",
    top_n=6,
    theme="minimal",
)
ax.set_xlabel("Tickets Resolved")
plt.show()''',
    "dataviz.univariate.advanced.dot_plot_interactive": '''import numpy as np
import pandas as pd
from dataviz.univariate.advanced import dot_plot_interactive

# Support tickets classified by resolution channel last quarter
rng = np.random.default_rng(42)
channels = pd.Series(
    rng.choice(
        ["Email", "Phone", "Chat", "Self-Service", "Social", "In Person", "Forum"],
        size=320,
        p=[0.28, 0.24, 0.20, 0.12, 0.08, 0.05, 0.03],
    ),
    name="channel",
)

fig = dot_plot_interactive(
    channels,
    title="Tickets by Resolution Channel",
    xlabel="Tickets Resolved",
    ylabel="Channel",
    color="seagreen",
    top_n=6,
    template="plotly_white",
)
fig.show()''',
    "dataviz.univariate.advanced.lollipop_chart_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.univariate.advanced import lollipop_chart_static

# Online orders grouped by product category for one month
rng = np.random.default_rng(42)
categories = pd.Series(
    rng.choice(
        ["Books", "Electronics", "Clothing", "Home", "Toys", "Sports", "Beauty"],
        size=280,
        p=[0.24, 0.22, 0.18, 0.14, 0.10, 0.07, 0.05],
    ),
    name="category",
)

ax = lollipop_chart_static(
    categories,
    title="Monthly Orders by Product Category",
    xlabel="Product Category",
    ylabel="Orders",
    color="navy",
    stem_color="lightgray",
    top_n=7,
    theme="minimal",
)
ax.set_ylabel("Orders")
plt.show()''',
    "dataviz.univariate.advanced.lollipop_chart_interactive": '''import numpy as np
import pandas as pd
from dataviz.univariate.advanced import lollipop_chart_interactive

# Online orders grouped by product category for one month
rng = np.random.default_rng(42)
categories = pd.Series(
    rng.choice(
        ["Books", "Electronics", "Clothing", "Home", "Toys", "Sports", "Beauty"],
        size=280,
        p=[0.24, 0.22, 0.18, 0.14, 0.10, 0.07, 0.05],
    ),
    name="category",
)

fig = lollipop_chart_interactive(
    categories,
    title="Monthly Orders by Product Category",
    xlabel="Product Category",
    ylabel="Orders",
    color="navy",
    top_n=7,
    template="plotly_white",
)
fig.show()''',
    "dataviz.univariate.advanced.reference_band_histogram_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.univariate.advanced import reference_band_histogram_static

# Bottling line fill volumes audited over one production shift
rng = np.random.default_rng(42)
fill_ml = pd.Series(
    np.round(rng.normal(loc=500.0, scale=4.5, size=48), 1),
    name="fill_volume_ml",
)

ax = reference_band_histogram_static(
    fill_ml,
    bins=14,
    title="Bottle Fill Volume with +/- 1 SD Band",
    xlabel="Fill Volume (ml)",
    color="cornflowerblue",
    band_color="khaki",
    mean_color="crimson",
    theme="default",
)
ax.set_ylabel("Bottles")
plt.show()''',
    "dataviz.univariate.advanced.reference_band_histogram_interactive": '''import numpy as np
import pandas as pd
from dataviz.univariate.advanced import reference_band_histogram_interactive

# Bottling line fill volumes audited over one production shift
rng = np.random.default_rng(42)
fill_ml = pd.Series(
    np.round(rng.normal(loc=500.0, scale=4.5, size=48), 1),
    name="fill_volume_ml",
)

fig = reference_band_histogram_interactive(
    fill_ml,
    bins=14,
    title="Bottle Fill Volume with +/- 1 SD Band",
    xlabel="Fill Volume (ml)",
    color="cornflowerblue",
    band_color="khaki",
    mean_color="crimson",
    template="plotly_white",
)
fig.show()''',
    "dataviz.univariate.advanced.raincloud_plot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.univariate.advanced import raincloud_plot_static

# Resting heart rates recorded by a wellness study cohort
rng = np.random.default_rng(42)
heart_rate = pd.Series(
    np.round(rng.normal(loc=68.0, scale=7.5, size=55), 1),
    name="heart_rate_bpm",
)

ax = raincloud_plot_static(
    heart_rate,
    title="Resting Heart Rate Raincloud",
    ylabel="Heart Rate (bpm)",
    color="mediumpurple",
    alpha=0.55,
    theme="minimal",
)
ax.set_ylabel("Heart Rate (bpm)")
plt.show()''',
    "dataviz.univariate.advanced.raincloud_plot_interactive": '''import numpy as np
import pandas as pd
from dataviz.univariate.advanced import raincloud_plot_interactive

# Resting heart rates recorded by a wellness study cohort
rng = np.random.default_rng(42)
heart_rate = pd.Series(
    np.round(rng.normal(loc=68.0, scale=7.5, size=55), 1),
    name="heart_rate_bpm",
)

fig = raincloud_plot_interactive(
    heart_rate,
    title="Resting Heart Rate Raincloud",
    ylabel="Heart Rate (bpm)",
    color="mediumpurple",
    template="plotly_white",
)
fig.show()''',
    "dataviz.univariate.advanced.ridgeline_plot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.univariate.advanced import ridgeline_plot_static

# Weekly delivery times (days) for three regional warehouses
rng = np.random.default_rng(42)
deliveries = pd.DataFrame({
    "North": rng.normal(loc=3.1, scale=0.8, size=40),
    "Central": rng.normal(loc=2.6, scale=0.6, size=40),
    "South": rng.normal(loc=3.8, scale=1.0, size=40),
})

ax = ridgeline_plot_static(
    deliveries,
    title="Delivery Time by Warehouse",
    xlabel="Delivery Time (days)",
    color="teal",
    theme="minimal",
)
ax.set_xlabel("Delivery Time (days)")
plt.show()''',
    "dataviz.univariate.advanced.ridgeline_plot_interactive": '''import numpy as np
import pandas as pd
from dataviz.univariate.advanced import ridgeline_plot_interactive

# Weekly delivery times (days) for three regional warehouses
rng = np.random.default_rng(42)
deliveries = pd.DataFrame({
    "North": rng.normal(loc=3.1, scale=0.8, size=40),
    "Central": rng.normal(loc=2.6, scale=0.6, size=40),
    "South": rng.normal(loc=3.8, scale=1.0, size=40),
})

fig = ridgeline_plot_interactive(
    deliveries,
    title="Delivery Time by Warehouse",
    xlabel="Delivery Time (days)",
    template="plotly_white",
)
fig.show()''',
    # ------------------------------------------------------------------
    # dataviz.univariate.box_plot
    # ------------------------------------------------------------------
    "dataviz.univariate.box_plot.box_plot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.univariate.box_plot import box_plot_static

# Daily household electricity consumption with a few heavy-usage days
rng = np.random.default_rng(42)
usage_kwh = pd.Series(
    np.concatenate([
        rng.normal(loc=18.0, scale=3.5, size=36),
        np.array([34.2, 37.8]),
    ]),
    name="usage_kwh",
)

ax = box_plot_static(
    usage_kwh,
    title="Daily Electricity Consumption",
    ylabel="Consumption (kWh)",
    color="lightsteelblue",
    notch=True,
    widths=0.4,
    theme="minimal",
)
ax.axhline(usage_kwh.mean(), color="crimson", linestyle="--", linewidth=1)
plt.show()''',
    "dataviz.univariate.box_plot.box_plot_interactive": '''import numpy as np
import pandas as pd
from dataviz.univariate.box_plot import box_plot_interactive

# Daily household electricity consumption with a few heavy-usage days
rng = np.random.default_rng(42)
usage_kwh = pd.Series(
    np.concatenate([
        rng.normal(loc=18.0, scale=3.5, size=36),
        np.array([34.2, 37.8]),
    ]),
    name="usage_kwh",
)

fig = box_plot_interactive(
    usage_kwh,
    title="Daily Electricity Consumption",
    ylabel="Consumption (kWh)",
    marker_color="steelblue",
    boxmean=True,
    points="all",
    template="plotly_white",
)
fig.show()''',
    # ------------------------------------------------------------------
    # dataviz.univariate.categorical
    # ------------------------------------------------------------------
    "dataviz.univariate.categorical.category_counts": '''import numpy as np
import pandas as pd
from dataviz.univariate.categorical import category_counts

# Exit-survey responses for a public library membership program
rng = np.random.default_rng(42)
ratings = pd.Series(
    rng.choice(
        ["Excellent", "Good", "Average", "Poor"],
        size=180,
        p=[0.45, 0.32, 0.16, 0.07],
    ),
    name="rating",
)

result = category_counts(ratings, normalize=True, top_n=4)
print(result)''',
    "dataviz.univariate.categorical.frequency_bar_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.univariate.categorical import frequency_bar_static

# Exit-survey responses for a public library membership program
rng = np.random.default_rng(42)
ratings = pd.Series(
    rng.choice(
        ["Excellent", "Good", "Average", "Poor"],
        size=180,
        p=[0.45, 0.32, 0.16, 0.07],
    ),
    name="rating",
)

ax = frequency_bar_static(
    ratings,
    normalize=True,
    title="Library Exit Survey Ratings",
    xlabel="Rating",
    ylabel="Proportion of Responses",
    color="slateblue",
    rotation=0,
    theme="minimal",
)
ax.set_ylabel("Proportion of Responses")
plt.show()''',
    "dataviz.univariate.categorical.frequency_bar_interactive": '''import numpy as np
import pandas as pd
from dataviz.univariate.categorical import frequency_bar_interactive

# Exit-survey responses for a public library membership program
rng = np.random.default_rng(42)
ratings = pd.Series(
    rng.choice(
        ["Excellent", "Good", "Average", "Poor"],
        size=180,
        p=[0.45, 0.32, 0.16, 0.07],
    ),
    name="rating",
)

fig = frequency_bar_interactive(
    ratings,
    normalize=True,
    title="Library Exit Survey Ratings",
    xlabel="Rating",
    ylabel="Proportion of Responses",
    color="slateblue",
    template="plotly_white",
)
fig.show()''',
    "dataviz.univariate.categorical.pareto_chart_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.univariate.categorical import pareto_chart_static

# Assembly-line defect codes logged during a quality audit
rng = np.random.default_rng(42)
defects = pd.Series(
    rng.choice(
        ["Scratch", "Misalignment", "Dent", "Paint Void", "Loose Fastener", "Label Error"],
        size=260,
        p=[0.34, 0.26, 0.16, 0.11, 0.08, 0.05],
    ),
    name="defect_code",
)

ax = pareto_chart_static(
    defects,
    top_n=6,
    title="Pareto Chart of Assembly Defects",
    xlabel="Defect Code",
    ylabel="Occurrences",
    color="steelblue",
    line_color="firebrick",
    theme="default",
)
ax.set_ylabel("Occurrences")
plt.show()''',
    "dataviz.univariate.categorical.pareto_chart_interactive": '''import numpy as np
import pandas as pd
from dataviz.univariate.categorical import pareto_chart_interactive

# Assembly-line defect codes logged during a quality audit
rng = np.random.default_rng(42)
defects = pd.Series(
    rng.choice(
        ["Scratch", "Misalignment", "Dent", "Paint Void", "Loose Fastener", "Label Error"],
        size=260,
        p=[0.34, 0.26, 0.16, 0.11, 0.08, 0.05],
    ),
    name="defect_code",
)

fig = pareto_chart_interactive(
    defects,
    top_n=6,
    title="Pareto Chart of Assembly Defects",
    xlabel="Defect Code",
    ylabel="Occurrences",
    color="steelblue",
    line_color="firebrick",
    template="plotly_white",
)
fig.show()''',
    # ------------------------------------------------------------------
    # dataviz.univariate.charts
    # ------------------------------------------------------------------
    "dataviz.univariate.charts.histogram": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.univariate.charts import histogram

# Commute times reported by employees in a hybrid-work survey
rng = np.random.default_rng(42)
commute_min = pd.Series(
    np.round(rng.gamma(shape=3.0, scale=8.0, size=55), 1),
    name="commute_min",
)

ax = histogram(
    commute_min,
    bins=12,
    title="Employee Commute Times",
    color="darkseagreen",
    edgecolor="black",
)
ax.set_xlabel("Commute Time (min)")
ax.set_ylabel("Employees")
plt.show()''',
    "dataviz.univariate.charts.density_plot": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.univariate.charts import density_plot

# Commute times reported by employees in a hybrid-work survey
rng = np.random.default_rng(42)
commute_min = pd.Series(
    np.round(rng.gamma(shape=3.0, scale=8.0, size=55), 1),
    name="commute_min",
)

ax = density_plot(
    commute_min,
    title="Employee Commute Time Density",
    color="teal",
    linewidth=2.0,
)
ax.set_xlabel("Commute Time (min)")
plt.show()''',
    "dataviz.univariate.charts.box_plot": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.univariate.charts import box_plot

# Commute times reported by employees in a hybrid-work survey
rng = np.random.default_rng(42)
commute_min = pd.Series(
    np.round(rng.gamma(shape=3.0, scale=8.0, size=55), 1),
    name="commute_min",
)

ax = box_plot(
    commute_min,
    title="Employee Commute Time Spread",
    patch_artist=True,
)
ax.set_ylabel("Commute Time (min)")
plt.show()''',
    "dataviz.univariate.charts.violin_plot": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.univariate.charts import violin_plot

# Commute times compared across three office locations
rng = np.random.default_rng(42)
commutes = pd.DataFrame({
    "Downtown": rng.gamma(shape=3.0, scale=8.0, size=40),
    "Suburban": rng.gamma(shape=2.5, scale=5.0, size=40),
    "Rural": rng.gamma(shape=4.0, scale=10.0, size=40),
})

ax = violin_plot(
    commutes,
    title="Commute Times by Office Location",
)
ax.set_ylabel("Commute Time (min)")
plt.show()''',
    # ------------------------------------------------------------------
    # dataviz.univariate.dashboard
    # ------------------------------------------------------------------
    "dataviz.univariate.dashboard.univariate_analysis_dashboard_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.univariate.dashboard import univariate_analysis_dashboard_static

# Quarterly revenue per store for a regional retail chain
rng = np.random.default_rng(42)
revenue_k = pd.Series(
    np.round(rng.lognormal(mean=11.2, sigma=0.4, size=46) / 1000.0, 1),
    name="revenue_kusd",
)

fig = univariate_analysis_dashboard_static(
    revenue_k,
    bins=12,
    title="Store Revenue Profile (USD thousands)",
    color="steelblue",
    theme="default",
)
plt.show()''',
    "dataviz.univariate.dashboard.univariate_analysis_dashboard_interactive": '''import numpy as np
import pandas as pd
from dataviz.univariate.dashboard import univariate_analysis_dashboard_interactive

# Quarterly revenue per store for a regional retail chain
rng = np.random.default_rng(42)
revenue_k = pd.Series(
    np.round(rng.lognormal(mean=11.2, sigma=0.4, size=46) / 1000.0, 1),
    name="revenue_kusd",
)

fig = univariate_analysis_dashboard_interactive(
    revenue_k,
    bins=12,
    title="Store Revenue Profile (USD thousands)",
    color="steelblue",
    template="plotly_white",
)
fig.show()''',
    # ------------------------------------------------------------------
    # dataviz.univariate.datetime
    # ------------------------------------------------------------------
    "dataviz.univariate.datetime.as_datetime_series": '''import numpy as np
import pandas as pd
from dataviz.univariate.datetime import as_datetime_series

# Newsletter signup timestamps exported from a marketing platform
rng = np.random.default_rng(42)
raw = pd.Timestamp("2026-01-05") + pd.to_timedelta(
    rng.uniform(0, 90 * 24, size=40), unit="h"
)
raw_strings = raw.strftime("%Y-%m-%d %H:%M")

result = as_datetime_series(raw_strings, name="signup_time")
print(result.head())''',
    "dataviz.univariate.datetime.event_counts": '''import numpy as np
import pandas as pd
from dataviz.univariate.datetime import event_counts

# Newsletter signup timestamps exported from a marketing platform
rng = np.random.default_rng(42)
signups = pd.Series(
    pd.Timestamp("2026-01-05")
    + pd.to_timedelta(rng.uniform(0, 90 * 24, size=40), unit="h"),
    name="signup_time",
)

result = event_counts(signups, freq="W")
print(result)''',
    "dataviz.univariate.datetime.event_frequency_plot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.univariate.datetime import event_frequency_plot_static

# Newsletter signup timestamps exported from a marketing platform
rng = np.random.default_rng(42)
signups = pd.Series(
    pd.Timestamp("2026-01-05")
    + pd.to_timedelta(rng.uniform(0, 90 * 24, size=40), unit="h"),
    name="signup_time",
)

ax = event_frequency_plot_static(
    signups,
    freq="W",
    title="Weekly Newsletter Signups",
    xlabel="Week",
    ylabel="Signups",
    color="darkcyan",
    theme="minimal",
)
ax.set_ylabel("Signups")
plt.show()''',
    "dataviz.univariate.datetime.event_frequency_plot_interactive": '''import numpy as np
import pandas as pd
from dataviz.univariate.datetime import event_frequency_plot_interactive

# Newsletter signup timestamps exported from a marketing platform
rng = np.random.default_rng(42)
signups = pd.Series(
    pd.Timestamp("2026-01-05")
    + pd.to_timedelta(rng.uniform(0, 90 * 24, size=40), unit="h"),
    name="signup_time",
)

fig = event_frequency_plot_interactive(
    signups,
    freq="W",
    title="Weekly Newsletter Signups",
    xlabel="Week",
    ylabel="Signups",
    color="darkcyan",
    template="plotly_white",
)
fig.show()''',
    "dataviz.univariate.datetime.interarrival_times": '''import numpy as np
import pandas as pd
from dataviz.univariate.datetime import interarrival_times

# Equipment failure timestamps from a fleet monitoring system
rng = np.random.default_rng(42)
failures = pd.Series(
    pd.Timestamp("2026-02-01")
    + pd.to_timedelta(np.sort(rng.uniform(0, 120 * 24, size=32)), unit="h"),
    name="failure_time",
)

result = interarrival_times(failures, unit="h")
print(result.describe())''',
    "dataviz.univariate.datetime.interarrival_plot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.univariate.datetime import interarrival_plot_static

# Equipment failure timestamps from a fleet monitoring system
rng = np.random.default_rng(42)
failures = pd.Series(
    pd.Timestamp("2026-02-01")
    + pd.to_timedelta(np.sort(rng.uniform(0, 120 * 24, size=32)), unit="h"),
    name="failure_time",
)

ax = interarrival_plot_static(
    failures,
    unit="h",
    title="Time Between Equipment Failures",
    color="indianred",
    theme="minimal",
)
ax.set_xlabel("Hours Between Failures")
plt.show()''',
    "dataviz.univariate.datetime.interarrival_plot_interactive": '''import numpy as np
import pandas as pd
from dataviz.univariate.datetime import interarrival_plot_interactive

# Equipment failure timestamps from a fleet monitoring system
rng = np.random.default_rng(42)
failures = pd.Series(
    pd.Timestamp("2026-02-01")
    + pd.to_timedelta(np.sort(rng.uniform(0, 120 * 24, size=32)), unit="h"),
    name="failure_time",
)

fig = interarrival_plot_interactive(
    failures,
    unit="h",
    title="Time Between Equipment Failures",
    color="indianred",
    template="plotly_white",
)
fig.show()''',
    # ------------------------------------------------------------------
    # dataviz.univariate.density
    # ------------------------------------------------------------------
    "dataviz.univariate.density.density_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.univariate.density import density_static

# Nightly server room temperatures sampled by an IoT sensor
rng = np.random.default_rng(42)
temp_c = pd.Series(
    np.round(rng.normal(loc=21.5, scale=1.2, size=60), 2),
    name="temperature_c",
)

ax = density_static(
    temp_c,
    title="Server Room Temperature Density",
    xlabel="Temperature (C)",
    color="darkred",
    linewidth=2.5,
    fill=True,
    theme="minimal",
)
ax.axvline(temp_c.mean(), color="navy", linestyle="--", linewidth=1)
plt.show()''',
    "dataviz.univariate.density.density_interactive": '''import numpy as np
import pandas as pd
from dataviz.univariate.density import density_interactive

# Nightly server room temperatures sampled by an IoT sensor
rng = np.random.default_rng(42)
temp_c = pd.Series(
    np.round(rng.normal(loc=21.5, scale=1.2, size=60), 2),
    name="temperature_c",
)

fig = density_interactive(
    temp_c,
    title="Server Room Temperature Density",
    xlabel="Temperature (C)",
    color="darkred",
    histnorm="probability density",
    template="plotly_white",
)
fig.show()''',
    # ------------------------------------------------------------------
    # dataviz.univariate.diagnostics
    # ------------------------------------------------------------------
    "dataviz.univariate.diagnostics.NormalityTestResult": '''from dataviz.univariate.diagnostics import NormalityTestResult

# Summary object returned by a Shapiro-Wilk check on exam scores
result = NormalityTestResult(
    statistic=0.973,
    p_value=0.31,
    method="shapiro",
    is_normal=True,
    alpha=0.05,
)
print(result)''',
    "dataviz.univariate.diagnostics.normality_test": '''import numpy as np
import pandas as pd
from dataviz.univariate.diagnostics import normality_test

# Final exam scores for one section of an introductory course
rng = np.random.default_rng(42)
scores = pd.Series(
    np.round(rng.normal(loc=78.0, scale=9.0, size=52), 1),
    name="exam_score",
)

result = normality_test(scores, method="shapiro", alpha=0.05)
print(result)''',
    "dataviz.univariate.diagnostics.outlier_plot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.univariate.diagnostics import outlier_plot_static

# Daily website sessions with two traffic spikes from a campaign
rng = np.random.default_rng(42)
sessions = pd.Series(
    np.concatenate([
        rng.normal(loc=4200.0, scale=380.0, size=44),
        np.array([7200.0, 2300.0]),
    ]),
    name="daily_sessions",
)

ax = outlier_plot_static(
    sessions,
    method="iqr",
    multiplier=1.5,
    title="Daily Session Outlier Review",
    xlabel="Day Index",
    ylabel="Sessions",
    color="steelblue",
    outlier_color="crimson",
    theme="default",
)
ax.set_xlabel("Day Index")
plt.show()''',
    "dataviz.univariate.diagnostics.outlier_plot_interactive": '''import numpy as np
import pandas as pd
from dataviz.univariate.diagnostics import outlier_plot_interactive

# Daily website sessions with two traffic spikes from a campaign
rng = np.random.default_rng(42)
sessions = pd.Series(
    np.concatenate([
        rng.normal(loc=4200.0, scale=380.0, size=44),
        np.array([7200.0, 2300.0]),
    ]),
    name="daily_sessions",
)

fig = outlier_plot_interactive(
    sessions,
    method="iqr",
    multiplier=1.5,
    title="Daily Session Outlier Review",
    xlabel="Day Index",
    ylabel="Sessions",
    color="steelblue",
    outlier_color="crimson",
    template="plotly_white",
)
fig.show()''',
    "dataviz.univariate.diagnostics.percentile_plot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.univariate.diagnostics import percentile_plot_static

# Response times for an internal API endpoint over one day
rng = np.random.default_rng(42)
response_ms = pd.Series(
    np.round(rng.lognormal(mean=4.6, sigma=0.5, size=58), 1),
    name="response_ms",
)

ax = percentile_plot_static(
    response_ms,
    step=10,
    title="API Response Time Percentile Profile",
    xlabel="Percentile",
    ylabel="Response Time (ms)",
    color="darkmagenta",
    marker="s",
    theme="minimal",
)
ax.set_ylabel("Response Time (ms)")
plt.show()''',
    "dataviz.univariate.diagnostics.percentile_plot_interactive": '''import numpy as np
import pandas as pd
from dataviz.univariate.diagnostics import percentile_plot_interactive

# Response times for an internal API endpoint over one day
rng = np.random.default_rng(42)
response_ms = pd.Series(
    np.round(rng.lognormal(mean=4.6, sigma=0.5, size=58), 1),
    name="response_ms",
)

fig = percentile_plot_interactive(
    response_ms,
    step=10,
    title="API Response Time Percentile Profile",
    xlabel="Percentile",
    ylabel="Response Time (ms)",
    color="darkmagenta",
    template="plotly_white",
)
fig.show()''',
    "dataviz.univariate.diagnostics.univariate_diagnostic_panel_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.univariate.diagnostics import univariate_diagnostic_panel_static

# Patient systolic blood pressure readings from a screening clinic
rng = np.random.default_rng(42)
systolic = pd.Series(
    np.round(rng.normal(loc=126.0, scale=14.0, size=50), 0),
    name="systolic_mmhg",
)

fig = univariate_diagnostic_panel_static(
    systolic,
    bins=14,
    title="Systolic Blood Pressure Diagnostics",
    color="cadetblue",
    theme="default",
)
plt.show()''',
    "dataviz.univariate.diagnostics.univariate_diagnostic_panel_interactive": '''import numpy as np
import pandas as pd
from dataviz.univariate.diagnostics import univariate_diagnostic_panel_interactive

# Patient systolic blood pressure readings from a screening clinic
rng = np.random.default_rng(42)
systolic = pd.Series(
    np.round(rng.normal(loc=126.0, scale=14.0, size=50), 0),
    name="systolic_mmhg",
)

fig = univariate_diagnostic_panel_interactive(
    systolic,
    bins=14,
    title="Systolic Blood Pressure Diagnostics",
    color="cadetblue",
    template="plotly_white",
)
fig.show()''',
    # ------------------------------------------------------------------
    # dataviz.univariate.distribution
    # ------------------------------------------------------------------
    "dataviz.univariate.distribution.ecdf_values": '''import numpy as np
import pandas as pd
from dataviz.univariate.distribution import ecdf_values

# Rental durations for a bike-share station over one week
rng = np.random.default_rng(42)
duration_min = pd.Series(
    np.round(rng.gamma(shape=2.2, scale=9.0, size=38), 1),
    name="rental_min",
)

values, probabilities = ecdf_values(duration_min)
print("n =", len(values), "median =", np.median(values))''',
    "dataviz.univariate.distribution.ecdf_plot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.univariate.distribution import ecdf_plot_static

# Rental durations for a bike-share station over one week
rng = np.random.default_rng(42)
duration_min = pd.Series(
    np.round(rng.gamma(shape=2.2, scale=9.0, size=38), 1),
    name="rental_min",
)

ax = ecdf_plot_static(
    duration_min,
    title="Bike-Share Rental Duration ECDF",
    xlabel="Rental Duration (min)",
    color="darkgreen",
    linewidth=2.5,
    theme="minimal",
)
ax.axhline(0.5, color="gray", linestyle=":", linewidth=1)
plt.show()''',
    "dataviz.univariate.distribution.ecdf_plot_interactive": '''import numpy as np
import pandas as pd
from dataviz.univariate.distribution import ecdf_plot_interactive

# Rental durations for a bike-share station over one week
rng = np.random.default_rng(42)
duration_min = pd.Series(
    np.round(rng.gamma(shape=2.2, scale=9.0, size=38), 1),
    name="rental_min",
)

fig = ecdf_plot_interactive(
    duration_min,
    title="Bike-Share Rental Duration ECDF",
    xlabel="Rental Duration (min)",
    color="darkgreen",
    template="plotly_white",
)
fig.show()''',
    "dataviz.univariate.distribution.cumulative_histogram_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.univariate.distribution import cumulative_histogram_static

# Order values processed by an online checkout during a sale
rng = np.random.default_rng(42)
order_usd = pd.Series(
    np.round(rng.lognormal(mean=4.2, sigma=0.6, size=54), 2),
    name="order_usd",
)

ax = cumulative_histogram_static(
    order_usd,
    bins=15,
    title="Cumulative Order Value Distribution",
    xlabel="Order Value (USD)",
    ylabel="Cumulative Orders",
    color="goldenrod",
    alpha=0.8,
    theme="default",
)
ax.set_ylabel("Cumulative Orders")
plt.show()''',
    "dataviz.univariate.distribution.cumulative_histogram_interactive": '''import numpy as np
import pandas as pd
from dataviz.univariate.distribution import cumulative_histogram_interactive

# Order values processed by an online checkout during a sale
rng = np.random.default_rng(42)
order_usd = pd.Series(
    np.round(rng.lognormal(mean=4.2, sigma=0.6, size=54), 2),
    name="order_usd",
)

fig = cumulative_histogram_interactive(
    order_usd,
    bins=15,
    title="Cumulative Order Value Distribution",
    xlabel="Order Value (USD)",
    ylabel="Cumulative Orders",
    color="goldenrod",
    alpha=0.8,
    template="plotly_white",
)
fig.show()''',
    "dataviz.univariate.distribution.qq_plot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.univariate.distribution import qq_plot_static

# Heights measured in a university anthropometry study
rng = np.random.default_rng(42)
height_cm = pd.Series(
    np.round(rng.normal(loc=171.0, scale=9.5, size=48), 1),
    name="height_cm",
)

ax = qq_plot_static(
    height_cm,
    distribution="norm",
    title="Height Normality QQ Plot",
    color="steelblue",
    reference_color="crimson",
    theme="default",
)
ax.set_xlabel("Theoretical Normal Quantiles")
plt.show()''',
    "dataviz.univariate.distribution.qq_plot_interactive": '''import numpy as np
import pandas as pd
from dataviz.univariate.distribution import qq_plot_interactive

# Heights measured in a university anthropometry study
rng = np.random.default_rng(42)
height_cm = pd.Series(
    np.round(rng.normal(loc=171.0, scale=9.5, size=48), 1),
    name="height_cm",
)

fig = qq_plot_interactive(
    height_cm,
    distribution="norm",
    title="Height Normality QQ Plot",
    color="steelblue",
    reference_color="crimson",
    template="plotly_white",
)
fig.show()''',
    "dataviz.univariate.distribution.pp_plot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.univariate.distribution import pp_plot_static

# Machine cycle times fitted against a gamma reference
rng = np.random.default_rng(42)
cycle_s = pd.Series(
    np.round(rng.gamma(shape=5.0, scale=2.1, size=52), 2),
    name="cycle_s",
)

ax = pp_plot_static(
    cycle_s,
    distribution="gamma",
    title="Cycle Time PP Plot (Gamma)",
    color="darkslategray",
    reference_color="crimson",
    theme="minimal",
)
ax.set_xlabel("Theoretical Probability")
plt.show()''',
    "dataviz.univariate.distribution.pp_plot_interactive": '''import numpy as np
import pandas as pd
from dataviz.univariate.distribution import pp_plot_interactive

# Machine cycle times fitted against a gamma reference
rng = np.random.default_rng(42)
cycle_s = pd.Series(
    np.round(rng.gamma(shape=5.0, scale=2.1, size=52), 2),
    name="cycle_s",
)

fig = pp_plot_interactive(
    cycle_s,
    distribution="gamma",
    title="Cycle Time PP Plot (Gamma)",
    color="darkslategray",
    reference_color="crimson",
    template="plotly_white",
)
fig.show()''',
    # ------------------------------------------------------------------
    # dataviz.univariate.fitting
    # ------------------------------------------------------------------
    "dataviz.univariate.fitting.DistributionFit": '''from dataviz.univariate.fitting import DistributionFit

# Fitted summary for claim severities modeled with a lognormal law
result = DistributionFit(
    distribution="lognorm",
    parameters=(0.42, 2.1, 8.9),
    statistic=0.061,
    p_value=0.58,
    aic=412.3,
    bic=420.1,
)
print(result)''',
    "dataviz.univariate.fitting.fit_distribution": '''import numpy as np
import pandas as pd
from dataviz.univariate.fitting import fit_distribution

# Insurance claim severities recorded by an auto portfolio
rng = np.random.default_rng(42)
claims = pd.Series(
    np.round(rng.lognormal(mean=8.1, sigma=0.9, size=56), 0),
    name="claim_usd",
)

result = fit_distribution(claims, distribution="lognorm")
print(result)''',
    "dataviz.univariate.fitting.compare_distributions": '''import numpy as np
import pandas as pd
from dataviz.univariate.fitting import compare_distributions

# Insurance claim severities recorded by an auto portfolio
rng = np.random.default_rng(42)
claims = pd.Series(
    np.round(rng.lognormal(mean=8.1, sigma=0.9, size=56), 0),
    name="claim_usd",
)

result = compare_distributions(
    claims,
    distributions=["norm", "lognorm", "gamma"],
)
print(result)''',
    "dataviz.univariate.fitting.fitted_pdf_values": '''import numpy as np
import pandas as pd
from dataviz.univariate.fitting import fitted_pdf_values

# Insurance claim severities recorded by an auto portfolio
rng = np.random.default_rng(42)
claims = pd.Series(
    np.round(rng.lognormal(mean=8.1, sigma=0.9, size=56), 0),
    name="claim_usd",
)

x_values, pdf_values, fit = fitted_pdf_values(
    claims,
    distribution="lognorm",
    points=150,
)
print("curve points:", len(x_values), "KS p-value:", round(fit.p_value, 3))''',
    "dataviz.univariate.fitting.fitted_distribution_histogram_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.univariate.fitting import fitted_distribution_histogram_static

# Insurance claim severities recorded by an auto portfolio
rng = np.random.default_rng(42)
claims = pd.Series(
    np.round(rng.lognormal(mean=8.1, sigma=0.9, size=56), 0),
    name="claim_usd",
)

ax = fitted_distribution_histogram_static(
    claims,
    distribution="lognorm",
    bins=16,
    title="Claim Severity with Fitted Lognormal",
    xlabel="Claim Amount (USD)",
    color="lightsteelblue",
    fit_color="crimson",
    theme="default",
)
ax.set_ylabel("Density")
plt.show()''',
    "dataviz.univariate.fitting.fitted_distribution_histogram_interactive": '''import numpy as np
import pandas as pd
from dataviz.univariate.fitting import fitted_distribution_histogram_interactive

# Insurance claim severities recorded by an auto portfolio
rng = np.random.default_rng(42)
claims = pd.Series(
    np.round(rng.lognormal(mean=8.1, sigma=0.9, size=56), 0),
    name="claim_usd",
)

fig = fitted_distribution_histogram_interactive(
    claims,
    distribution="lognorm",
    bins=16,
    title="Claim Severity with Fitted Lognormal",
    xlabel="Claim Amount (USD)",
    color="lightsteelblue",
    fit_color="crimson",
    template="plotly_white",
)
fig.show()''',
    # ------------------------------------------------------------------
    # dataviz.univariate.histogram
    # ------------------------------------------------------------------
    "dataviz.univariate.histogram.histogram_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.univariate.histogram import histogram_static

# Call-center wait times sampled during business hours
rng = np.random.default_rng(42)
wait_min = pd.Series(
    np.round(rng.gamma(shape=2.0, scale=2.5, size=60), 1),
    name="wait_time_min",
)

ax = histogram_static(
    wait_min,
    bins=14,
    title="Call-Center Wait Time Distribution",
    xlabel="Wait Time (min)",
    ylabel="Calls",
    color="cornflowerblue",
    edgecolor="black",
    alpha=0.8,
    theme="minimal",
)
ax.axvline(wait_min.mean(), color="crimson", linestyle="--", linewidth=1)
plt.show()''',
    "dataviz.univariate.histogram.histogram_interactive": '''import numpy as np
import pandas as pd
from dataviz.univariate.histogram import histogram_interactive

# Call-center wait times sampled during business hours
rng = np.random.default_rng(42)
wait_min = pd.Series(
    np.round(rng.gamma(shape=2.0, scale=2.5, size=60), 1),
    name="wait_time_min",
)

fig = histogram_interactive(
    wait_min,
    bins=14,
    title="Call-Center Wait Time Distribution",
    xlabel="Wait Time (min)",
    ylabel="Calls",
    marker_color="cornflowerblue",
    alpha=0.8,
    bargap=0.05,
    template="plotly_white",
)
fig.show()''',
}
