"""Curated Complete-example snippets for dataviz.bivariate API pages."""

EXAMPLES = {
    "dataviz.bivariate.advanced.bubble_plot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.bivariate.advanced import bubble_plot_static

rng = np.random.default_rng(42)
n = 60
gdp = pd.Series(rng.normal(loc=45.0, scale=12.0, size=n), name="GDP per capita (k USD)")
life = pd.Series(60.0 + 0.4 * gdp + rng.normal(loc=0.0, scale=3.0, size=n), name="Life expectancy (years)")
population = pd.Series(rng.uniform(low=2.0, high=300.0, size=n), name="Population (millions)")
co2 = pd.Series(rng.uniform(low=1.0, high=20.0, size=n), name="CO2 per capita (t)")

ax = bubble_plot_static(
    gdp,
    life,
    population,
    color=co2,
    title="Life Expectancy vs Wealth by Country",
    size_scale=500.0,
    alpha=0.65,
    cmap="plasma",
)
plt.show()
''',
    "dataviz.bivariate.advanced.bubble_plot_interactive": '''import numpy as np
import pandas as pd
from dataviz.bivariate.advanced import bubble_plot_interactive

rng = np.random.default_rng(42)
n = 60
gdp = pd.Series(rng.normal(loc=45.0, scale=12.0, size=n), name="GDP per capita (k USD)")
life = pd.Series(60.0 + 0.4 * gdp + rng.normal(loc=0.0, scale=3.0, size=n), name="Life expectancy (years)")
population = pd.Series(rng.uniform(low=2.0, high=300.0, size=n), name="Population (millions)")
co2 = pd.Series(rng.uniform(low=1.0, high=20.0, size=n), name="CO2 per capita (t)")

fig = bubble_plot_interactive(
    gdp,
    life,
    population,
    color=co2,
    title="Life Expectancy vs Wealth by Country",
    size_scale=55.0,
    colorscale="Plasma",
)
fig.show()
''',
    "dataviz.bivariate.advanced.hexbin_plot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.bivariate.advanced import hexbin_plot_static

rng = np.random.default_rng(42)
n = 2000
load = pd.Series(rng.normal(loc=70.0, scale=8.0, size=n), name="Server load (%)")
latency = pd.Series(20.0 + 0.8 * load + rng.normal(loc=0.0, scale=6.0, size=n), name="Latency (ms)")

ax = hexbin_plot_static(
    load,
    latency,
    gridsize=25,
    title="Latency vs Server Load Density",
    cmap="magma",
)
plt.show()
''',
    "dataviz.bivariate.advanced.hexbin_plot_interactive": '''import numpy as np
import pandas as pd
from dataviz.bivariate.advanced import hexbin_plot_interactive

rng = np.random.default_rng(42)
n = 2000
load = pd.Series(rng.normal(loc=70.0, scale=8.0, size=n), name="Server load (%)")
latency = pd.Series(20.0 + 0.8 * load + rng.normal(loc=0.0, scale=6.0, size=n), name="Latency (ms)")

fig = hexbin_plot_interactive(
    load,
    latency,
    nbinsx=30,
    nbinsy=30,
    title="Latency vs Server Load Density",
    colorscale="Magma",
)
fig.show()
''',
    "dataviz.bivariate.advanced.regression_plot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.bivariate.advanced import regression_plot_static

rng = np.random.default_rng(42)
n = 50
spend = pd.Series(rng.uniform(low=5.0, high=100.0, size=n), name="Marketing spend (k USD)")
revenue = pd.Series(
    50.0 + 3.2 * spend - 0.015 * spend**2 + rng.normal(loc=0.0, scale=18.0, size=n),
    name="Revenue (k USD)",
)

ax = regression_plot_static(
    spend,
    revenue,
    degree=2,
    title="Revenue Response to Marketing Spend",
    scatter_color="darkslategray",
    line_color="crimson",
)
plt.show()
''',
    "dataviz.bivariate.advanced.regression_plot_interactive": '''import numpy as np
import pandas as pd
from dataviz.bivariate.advanced import regression_plot_interactive

rng = np.random.default_rng(42)
n = 50
spend = pd.Series(rng.uniform(low=5.0, high=100.0, size=n), name="Marketing spend (k USD)")
revenue = pd.Series(
    50.0 + 3.2 * spend - 0.015 * spend**2 + rng.normal(loc=0.0, scale=18.0, size=n),
    name="Revenue (k USD)",
)

fig = regression_plot_interactive(
    spend,
    revenue,
    degree=2,
    title="Revenue Response to Marketing Spend",
)
fig.show()
''',
    "dataviz.bivariate.advanced.density_contour_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.bivariate.advanced import density_contour_static

rng = np.random.default_rng(42)
n = 800
temperature = pd.Series(rng.normal(loc=22.0, scale=3.0, size=n), name="Temperature (C)")
humidity = pd.Series(80.0 - 1.5 * temperature + rng.normal(loc=0.0, scale=5.0, size=n), name="Humidity (%)")

ax = density_contour_static(
    temperature,
    humidity,
    bins=25,
    levels=10,
    title="Greenhouse Climate Density",
    cmap="cividis",
    fill=True,
)
plt.show()
''',
    "dataviz.bivariate.advanced.density_contour_interactive": '''import numpy as np
import pandas as pd
from dataviz.bivariate.advanced import density_contour_interactive

rng = np.random.default_rng(42)
n = 800
temperature = pd.Series(rng.normal(loc=22.0, scale=3.0, size=n), name="Temperature (C)")
humidity = pd.Series(80.0 - 1.5 * temperature + rng.normal(loc=0.0, scale=5.0, size=n), name="Humidity (%)")

fig = density_contour_interactive(
    temperature,
    humidity,
    title="Greenhouse Climate Density",
    colorscale="Cividis",
    contours_coloring="heatmap",
)
fig.show()
''',
    "dataviz.bivariate.categorical.grouped_bar_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.bivariate.categorical import grouped_bar_static

rng = np.random.default_rng(42)
n = 90
region = pd.Series(np.repeat(["North", "South", "East", "West"], n // 4)[:n], name="Region")
sales = pd.Series(rng.normal(loc=120.0, scale=25.0, size=n), name="Quarterly sales (k USD)")

ax = grouped_bar_static(
    region,
    sales,
    aggfunc="median",
    title="Median Quarterly Sales by Region",
    color="seagreen",
)
plt.show()
''',
    "dataviz.bivariate.categorical.grouped_bar_interactive": '''import numpy as np
import pandas as pd
from dataviz.bivariate.categorical import grouped_bar_interactive

rng = np.random.default_rng(42)
n = 90
region = pd.Series(np.repeat(["North", "South", "East", "West"], n // 4)[:n], name="Region")
sales = pd.Series(rng.normal(loc=120.0, scale=25.0, size=n), name="Quarterly sales (k USD)")

fig = grouped_bar_interactive(
    region,
    sales,
    aggfunc="median",
    title="Median Quarterly Sales by Region",
    color="seagreen",
)
fig.show()
''',
    "dataviz.bivariate.categorical.box_by_category_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.bivariate.categorical import box_by_category_static

rng = np.random.default_rng(42)
n = 120
plan = pd.Series(np.repeat(["Basic", "Pro", "Enterprise"], n // 3), name="Plan")
support_hours = pd.Series(
    np.concatenate([
        rng.normal(loc=2.0, scale=0.8, size=n // 3),
        rng.normal(loc=6.0, scale=1.5, size=n // 3),
        rng.normal(loc=14.0, scale=3.0, size=n // 3),
    ]),
    name="Support hours per month",
)

ax = box_by_category_static(
    plan,
    support_hours,
    title="Support Usage by Subscription Plan",
)
plt.show()
''',
    "dataviz.bivariate.categorical.box_by_category_interactive": '''import numpy as np
import pandas as pd
from dataviz.bivariate.categorical import box_by_category_interactive

rng = np.random.default_rng(42)
n = 120
plan = pd.Series(np.repeat(["Basic", "Pro", "Enterprise"], n // 3), name="Plan")
support_hours = pd.Series(
    np.concatenate([
        rng.normal(loc=2.0, scale=0.8, size=n // 3),
        rng.normal(loc=6.0, scale=1.5, size=n // 3),
        rng.normal(loc=14.0, scale=3.0, size=n // 3),
    ]),
    name="Support hours per month",
)

fig = box_by_category_interactive(
    plan,
    support_hours,
    title="Support Usage by Subscription Plan",
)
fig.show()
''',
    "dataviz.bivariate.categorical.violin_by_category_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.bivariate.categorical import violin_by_category_static

rng = np.random.default_rng(42)
n = 150
shift = pd.Series(np.repeat(["Morning", "Afternoon", "Night"], n // 3), name="Shift")
cycle_time = pd.Series(
    np.concatenate([
        rng.normal(loc=45.0, scale=4.0, size=n // 3),
        rng.normal(loc=52.0, scale=6.0, size=n // 3),
        rng.normal(loc=49.0, scale=3.0, size=n // 3),
    ]),
    name="Cycle time (s)",
)

ax = violin_by_category_static(
    shift,
    cycle_time,
    title="Cycle Time Shape by Shift",
)
plt.show()
''',
    "dataviz.bivariate.categorical.violin_by_category_interactive": '''import numpy as np
import pandas as pd
from dataviz.bivariate.categorical import violin_by_category_interactive

rng = np.random.default_rng(42)
n = 150
shift = pd.Series(np.repeat(["Morning", "Afternoon", "Night"], n // 3), name="Shift")
cycle_time = pd.Series(
    np.concatenate([
        rng.normal(loc=45.0, scale=4.0, size=n // 3),
        rng.normal(loc=52.0, scale=6.0, size=n // 3),
        rng.normal(loc=49.0, scale=3.0, size=n // 3),
    ]),
    name="Cycle time (s)",
)

fig = violin_by_category_interactive(
    shift,
    cycle_time,
    title="Cycle Time Shape by Shift",
)
fig.show()
''',
    "dataviz.bivariate.categorical.crosstab_heatmap_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.bivariate.categorical import crosstab_heatmap_static

rng = np.random.default_rng(42)
n = 200
channel = pd.Series(rng.choice(["Email", "Social", "Search", "Referral"], size=n), name="Channel")
converted = pd.Series(rng.choice(["Converted", "Bounced"], size=n, p=[0.35, 0.65]), name="Outcome")

ax = crosstab_heatmap_static(
    channel,
    converted,
    normalize="index",
    title="Conversion Rate by Channel",
    cmap="YlGn",
)
plt.show()
''',
    "dataviz.bivariate.categorical.crosstab_heatmap_interactive": '''import numpy as np
import pandas as pd
from dataviz.bivariate.categorical import crosstab_heatmap_interactive

rng = np.random.default_rng(42)
n = 200
channel = pd.Series(rng.choice(["Email", "Social", "Search", "Referral"], size=n), name="Channel")
converted = pd.Series(rng.choice(["Converted", "Bounced"], size=n, p=[0.35, 0.65]), name="Outcome")

fig = crosstab_heatmap_interactive(
    channel,
    converted,
    normalize="index",
    title="Conversion Rate by Channel",
    colorscale="YlGn",
)
fig.show()
''',
    "dataviz.bivariate.charts.scatter_plot": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.bivariate.charts import scatter_plot

rng = np.random.default_rng(42)
n = 60
df = pd.DataFrame({
    "Ad Spend (k USD)": rng.uniform(low=10.0, high=200.0, size=n),
    "Segment": rng.choice(["Retail", "Online"], size=n),
})
df["Revenue (k USD)"] = 80.0 + 2.5 * df["Ad Spend (k USD)"] + rng.normal(loc=0.0, scale=30.0, size=n)

ax = scatter_plot(
    "Ad Spend (k USD)",
    "Revenue (k USD)",
    data=df,
    hue="Segment",
    title="Marketing Spend vs Revenue",
    fit_degree=1,
    show_corr=True,
)
plt.show()
''',
    "dataviz.bivariate.charts.line_plot": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.bivariate.charts import line_plot

rng = np.random.default_rng(42)
days = pd.Series(pd.date_range("2024-01-01", periods=90, freq="D"), name="Date")
visitors = pd.Series(
    5000.0 + np.cumsum(rng.normal(loc=20.0, scale=150.0, size=90)),
    name="Daily visitors",
)

ax = line_plot(
    days,
    visitors,
    title="Website Traffic Trend",
    color="steelblue",
    rolling_window=7,
    hline=5000.0,
)
plt.show()
''',
    "dataviz.bivariate.charts.correlation_heatmap": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.bivariate.charts import correlation_heatmap

rng = np.random.default_rng(42)
n = 80
speed = rng.normal(loc=120.0, scale=6.0, size=n)
df = pd.DataFrame({
    "Speed": speed,
    "Pressure": 40.0 + 0.3 * speed + rng.normal(loc=0.0, scale=2.0, size=n),
    "Temperature": rng.normal(loc=180.0, scale=5.0, size=n),
    "Yield": 95.0 - 0.2 * speed + rng.normal(loc=0.0, scale=1.5, size=n),
})

ax = correlation_heatmap(df, method="spearman", mask_upper=True, title="Process Variable Correlations")
plt.show()
''',
    "dataviz.bivariate.correlation.correlation_heatmap_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.bivariate.correlation import correlation_heatmap_static

rng = np.random.default_rng(42)
n = 80
speed = rng.normal(loc=120.0, scale=6.0, size=n)
df = pd.DataFrame({
    "Speed": speed,
    "Pressure": 40.0 + 0.3 * speed + rng.normal(loc=0.0, scale=2.0, size=n),
    "Temperature": rng.normal(loc=180.0, scale=5.0, size=n),
    "Yield": 95.0 - 0.2 * speed + rng.normal(loc=0.0, scale=1.5, size=n),
})

ax, corr = correlation_heatmap_static(
    df,
    method="spearman",
    mask_upper=True,
    return_corr=True,
    title="Process Variable Correlations",
)
print(corr.round(2))
plt.show()
''',
    "dataviz.bivariate.correlation.correlation_heatmap_interactive": '''import numpy as np
import pandas as pd
from dataviz.bivariate.correlation import correlation_heatmap_interactive

rng = np.random.default_rng(42)
n = 80
speed = rng.normal(loc=120.0, scale=6.0, size=n)
df = pd.DataFrame({
    "Speed": speed,
    "Pressure": 40.0 + 0.3 * speed + rng.normal(loc=0.0, scale=2.0, size=n),
    "Temperature": rng.normal(loc=180.0, scale=5.0, size=n),
    "Yield": 95.0 - 0.2 * speed + rng.normal(loc=0.0, scale=1.5, size=n),
})

fig = correlation_heatmap_interactive(
    df,
    method="spearman",
    mask_upper=True,
    title="Process Variable Correlations",
    colorscale="RdBu",
)
fig.show()
''',
    "dataviz.bivariate.joint.joint_scatter_hist_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.bivariate.joint import joint_scatter_hist_static

rng = np.random.default_rng(42)
n = 250
height_cm = pd.Series(rng.normal(loc=172.0, scale=9.0, size=n), name="Height (cm)")
weight_kg = pd.Series(0.9 * height_cm - 85.0 + rng.normal(loc=0.0, scale=6.0, size=n), name="Weight (kg)")

ax = joint_scatter_hist_static(
    height_cm,
    weight_kg,
    bins=20,
    title="Height vs Weight Joint Distribution",
)
plt.show()
''',
    "dataviz.bivariate.joint.joint_scatter_hist_interactive": '''import numpy as np
import pandas as pd
from dataviz.bivariate.joint import joint_scatter_hist_interactive

rng = np.random.default_rng(42)
n = 250
height_cm = pd.Series(rng.normal(loc=172.0, scale=9.0, size=n), name="Height (cm)")
weight_kg = pd.Series(0.9 * height_cm - 85.0 + rng.normal(loc=0.0, scale=6.0, size=n), name="Weight (kg)")

fig = joint_scatter_hist_interactive(
    height_cm,
    weight_kg,
    bins=20,
    title="Height vs Weight Joint Distribution",
)
fig.show()
''',
    "dataviz.bivariate.joint.bivariate_histogram_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.bivariate.joint import bivariate_histogram_static

rng = np.random.default_rng(42)
n = 600
wait_min = pd.Series(rng.gamma(shape=3.0, scale=2.0, size=n), name="Wait time (min)")
bill = pd.Series(15.0 + 2.0 * wait_min + rng.normal(loc=0.0, scale=8.0, size=n), name="Bill (USD)")

ax = bivariate_histogram_static(
    wait_min,
    bill,
    bins=25,
    title="Wait Time vs Bill Density",
    cmap="rocket_r",
)
plt.show()
''',
    "dataviz.bivariate.joint.bivariate_histogram_interactive": '''import numpy as np
import pandas as pd
from dataviz.bivariate.joint import bivariate_histogram_interactive

rng = np.random.default_rng(42)
n = 600
wait_min = pd.Series(rng.gamma(shape=3.0, scale=2.0, size=n), name="Wait time (min)")
bill = pd.Series(15.0 + 2.0 * wait_min + rng.normal(loc=0.0, scale=8.0, size=n), name="Bill (USD)")

fig = bivariate_histogram_interactive(
    wait_min,
    bill,
    nbinsx=25,
    nbinsy=25,
    title="Wait Time vs Bill Density",
    colorscale="Viridis",
)
fig.show()
''',
    "dataviz.bivariate.line.line_plot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.bivariate.line import line_plot_static

rng = np.random.default_rng(42)
df = pd.DataFrame({
    "Week": np.arange(1, 53),
    "Active users": 10000.0 + np.cumsum(rng.normal(loc=120.0, scale=300.0, size=52)),
})

ax = line_plot_static(
    "Week",
    "Active users",
    data=df,
    title="Weekly Active Users",
    marker="o",
    markersize=4,
    rolling_window=4,
    fill_to=9000.0,
)
plt.show()
''',
    "dataviz.bivariate.line.line_plot_interactive": '''import numpy as np
import pandas as pd
from dataviz.bivariate.line import line_plot_interactive

rng = np.random.default_rng(42)
df = pd.DataFrame({
    "Week": np.arange(1, 53),
    "Active users": 10000.0 + np.cumsum(rng.normal(loc=120.0, scale=300.0, size=52)),
})

fig = line_plot_interactive(
    "Week",
    "Active users",
    data=df,
    title="Weekly Active Users",
    mode="lines+markers",
    rolling_window=4,
    hline=10000.0,
)
fig.show()
''',
    "dataviz.bivariate.scatter.scatter_plot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.bivariate.scatter import scatter_plot_static

rng = np.random.default_rng(42)
n = 75
df = pd.DataFrame({
    "Engine size (L)": rng.uniform(low=1.0, high=5.5, size=n),
    "Body style": rng.choice(["Sedan", "SUV", "Truck"], size=n),
})
df["Fuel economy (mpg)"] = 42.0 - 4.0 * df["Engine size (L)"] + rng.normal(loc=0.0, scale=2.5, size=n)

ax = scatter_plot_static(
    "Engine size (L)",
    "Fuel economy (mpg)",
    data=df,
    hue="Body style",
    title="Engine Size vs Fuel Economy",
    fit_degree=1,
    diagonal=False,
    show_corr=True,
)
plt.show()
''',
    "dataviz.bivariate.scatter.scatter_plot_interactive": '''import numpy as np
import pandas as pd
from dataviz.bivariate.scatter import scatter_plot_interactive

rng = np.random.default_rng(42)
n = 75
df = pd.DataFrame({
    "Engine size (L)": rng.uniform(low=1.0, high=5.5, size=n),
    "Body style": rng.choice(["Sedan", "SUV", "Truck"], size=n),
})
df["Fuel economy (mpg)"] = 42.0 - 4.0 * df["Engine size (L)"] + rng.normal(loc=0.0, scale=2.5, size=n)

fig = scatter_plot_interactive(
    "Engine size (L)",
    "Fuel economy (mpg)",
    data=df,
    hue="Body style",
    title="Engine Size vs Fuel Economy",
    fit_degree=1,
    show_corr=True,
)
fig.show()
''',
    "dataviz.bivariate.stats.BivariateStats": '''import numpy as np
import pandas as pd
from dataviz.bivariate.stats import bivariate_summary

rng = np.random.default_rng(42)
n = 80
study_hours = pd.Series(rng.uniform(low=1.0, high=15.0, size=n), name="Study hours")
exam_score = pd.Series(45.0 + 3.5 * study_hours + rng.normal(loc=0.0, scale=6.0, size=n), name="Exam score")

result = bivariate_summary(study_hours, exam_score)
print(result)
''',
    "dataviz.bivariate.stats.bivariate_summary": '''import numpy as np
import pandas as pd
from dataviz.bivariate.stats import bivariate_summary

rng = np.random.default_rng(42)
n = 80
study_hours = pd.Series(rng.uniform(low=1.0, high=15.0, size=n), name="Study hours")
exam_score = pd.Series(45.0 + 3.5 * study_hours + rng.normal(loc=0.0, scale=6.0, size=n), name="Exam score")

result = bivariate_summary(study_hours, exam_score)
print(result)
''',
    "dataviz.bivariate.stats.outlier_scatter_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.bivariate.stats import outlier_scatter_static

rng = np.random.default_rng(42)
n = 90
sessions = pd.Series(rng.normal(loc=30.0, scale=6.0, size=n), name="Sessions per month")
orders = pd.Series(5.0 + 0.4 * sessions + rng.normal(loc=0.0, scale=2.0, size=n), name="Orders")
orders.iloc[[7, 33, 71]] = [40.0, 2.0, 45.0]

ax = outlier_scatter_static(
    sessions,
    orders,
    method="iqr",
    threshold=1.5,
    title="Customer Activity Outliers",
)
plt.show()
''',
    "dataviz.bivariate.stats.outlier_scatter_interactive": '''import numpy as np
import pandas as pd
from dataviz.bivariate.stats import outlier_scatter_interactive

rng = np.random.default_rng(42)
n = 90
sessions = pd.Series(rng.normal(loc=30.0, scale=6.0, size=n), name="Sessions per month")
orders = pd.Series(5.0 + 0.4 * sessions + rng.normal(loc=0.0, scale=2.0, size=n), name="Orders")
orders.iloc[[7, 33, 71]] = [40.0, 2.0, 45.0]

fig = outlier_scatter_interactive(
    sessions,
    orders,
    method="iqr",
    threshold=1.5,
    title="Customer Activity Outliers",
)
fig.show()
''',
    "dataviz.bivariate.stats.residual_relationship_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.bivariate.stats import residual_relationship_static

rng = np.random.default_rng(42)
n = 70
experience = pd.Series(rng.uniform(low=0.0, high=20.0, size=n), name="Experience (years)")
salary = pd.Series(40.0 + 4.0 * experience + 0.08 * experience**2 + rng.normal(loc=0.0, scale=6.0, size=n), name="Salary (k USD)")

ax = residual_relationship_static(
    experience,
    salary,
    degree=1,
    title="Linear Fit Residuals: Salary vs Experience",
)
plt.show()
''',
    "dataviz.bivariate.stats.residual_relationship_interactive": '''import numpy as np
import pandas as pd
from dataviz.bivariate.stats import residual_relationship_interactive

rng = np.random.default_rng(42)
n = 70
experience = pd.Series(rng.uniform(low=0.0, high=20.0, size=n), name="Experience (years)")
salary = pd.Series(40.0 + 4.0 * experience + 0.08 * experience**2 + rng.normal(loc=0.0, scale=6.0, size=n), name="Salary (k USD)")

fig = residual_relationship_interactive(
    experience,
    salary,
    degree=1,
    title="Linear Fit Residuals: Salary vs Experience",
)
fig.show()
''',
    "dataviz.bivariate.stats.quantile_bin_plot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.bivariate.stats import quantile_bin_plot_static

rng = np.random.default_rng(42)
n = 200
income = pd.Series(rng.lognormal(mean=10.8, sigma=0.4, size=n), name="Annual income (USD)")
savings_rate = pd.Series(
    5.0 + 0.0001 * income + rng.normal(loc=0.0, scale=3.0, size=n),
    name="Savings rate (%)",
)

ax = quantile_bin_plot_static(
    income,
    savings_rate,
    q=8,
    statistic="median",
    title="Median Savings Rate by Income Decile",
)
plt.show()
''',
    "dataviz.bivariate.stats.quantile_bin_plot_interactive": '''import numpy as np
import pandas as pd
from dataviz.bivariate.stats import quantile_bin_plot_interactive

rng = np.random.default_rng(42)
n = 200
income = pd.Series(rng.lognormal(mean=10.8, sigma=0.4, size=n), name="Annual income (USD)")
savings_rate = pd.Series(
    5.0 + 0.0001 * income + rng.normal(loc=0.0, scale=3.0, size=n),
    name="Savings rate (%)",
)

fig = quantile_bin_plot_interactive(
    income,
    savings_rate,
    q=8,
    statistic="median",
    title="Median Savings Rate by Income Decile",
)
fig.show()
''',
    "dataviz.bivariate.stats.bland_altman_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.bivariate.stats import bland_altman_static

rng = np.random.default_rng(42)
n = 60
lab_test = pd.Series(rng.normal(loc=120.0, scale=18.0, size=n), name="Lab assay (mg/dL)")
home_test = pd.Series(lab_test + rng.normal(loc=2.0, scale=6.0, size=n), name="Home kit (mg/dL)")

ax = bland_altman_static(
    lab_test,
    home_test,
    title="Bland-Altman: Lab vs Home Kit",
)
plt.show()
''',
    "dataviz.bivariate.stats.bland_altman_interactive": '''import numpy as np
import pandas as pd
from dataviz.bivariate.stats import bland_altman_interactive

rng = np.random.default_rng(42)
n = 60
lab_test = pd.Series(rng.normal(loc=120.0, scale=18.0, size=n), name="Lab assay (mg/dL)")
home_test = pd.Series(lab_test + rng.normal(loc=2.0, scale=6.0, size=n), name="Home kit (mg/dL)")

fig = bland_altman_interactive(
    lab_test,
    home_test,
    title="Bland-Altman: Lab vs Home Kit",
)
fig.show()
''',
    "dataviz.bivariate.stats.rank_scatter_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.bivariate.stats import rank_scatter_static

rng = np.random.default_rng(42)
n = 50
quality = pd.Series(rng.uniform(low=1.0, high=10.0, size=n), name="Quality score")
satisfaction = pd.Series(0.8 * quality + rng.normal(loc=0.0, scale=1.5, size=n), name="Satisfaction score")

ax = rank_scatter_static(
    quality,
    satisfaction,
    title="Rank Agreement: Quality vs Satisfaction",
)
plt.show()
''',
    "dataviz.bivariate.stats.rank_scatter_interactive": '''import numpy as np
import pandas as pd
from dataviz.bivariate.stats import rank_scatter_interactive

rng = np.random.default_rng(42)
n = 50
quality = pd.Series(rng.uniform(low=1.0, high=10.0, size=n), name="Quality score")
satisfaction = pd.Series(0.8 * quality + rng.normal(loc=0.0, scale=1.5, size=n), name="Satisfaction score")

fig = rank_scatter_interactive(
    quality,
    satisfaction,
    title="Rank Agreement: Quality vs Satisfaction",
)
fig.show()
''',
    "dataviz.bivariate.stats.lag_plot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.bivariate.stats import lag_plot_static

rng = np.random.default_rng(42)
n = 100
noise = rng.normal(loc=0.0, scale=1.0, size=n)
flow = pd.Series(np.zeros(n), name="River flow (m3/s)")
for i in range(1, n):
    flow.iloc[i] = 0.85 * flow.iloc[i - 1] + noise[i]

ax = lag_plot_static(
    flow,
    flow,
    lag=1,
    title="River Flow Lag-1 Autocorrelation",
)
plt.show()
''',
    "dataviz.bivariate.stats.lag_plot_interactive": '''import numpy as np
import pandas as pd
from dataviz.bivariate.stats import lag_plot_interactive

rng = np.random.default_rng(42)
n = 100
noise = rng.normal(loc=0.0, scale=1.0, size=n)
flow = pd.Series(np.zeros(n), name="River flow (m3/s)")
for i in range(1, n):
    flow.iloc[i] = 0.85 * flow.iloc[i - 1] + noise[i]

fig = lag_plot_interactive(
    flow,
    flow,
    lag=1,
    title="River Flow Lag-1 Autocorrelation",
)
fig.show()
''',
    "dataviz.bivariate.stats.conditional_box_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.bivariate.stats import conditional_box_static

rng = np.random.default_rng(42)
n = 180
temperature = pd.Series(rng.uniform(low=150.0, high=250.0, size=n), name="Oven temperature (C)")
hardness = pd.Series(30.0 + 0.25 * temperature + rng.normal(loc=0.0, scale=4.0, size=n), name="Coating hardness")

ax = conditional_box_static(
    temperature,
    hardness,
    bins=6,
    title="Hardness Distribution by Temperature Band",
)
plt.show()
''',
    "dataviz.bivariate.stats.conditional_box_interactive": '''import numpy as np
import pandas as pd
from dataviz.bivariate.stats import conditional_box_interactive

rng = np.random.default_rng(42)
n = 180
temperature = pd.Series(rng.uniform(low=150.0, high=250.0, size=n), name="Oven temperature (C)")
hardness = pd.Series(30.0 + 0.25 * temperature + rng.normal(loc=0.0, scale=4.0, size=n), name="Coating hardness")

fig = conditional_box_interactive(
    temperature,
    hardness,
    bins=6,
    title="Hardness Distribution by Temperature Band",
)
fig.show()
''',
    "dataviz.bivariate.trends.binned_mean_plot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.bivariate.trends import binned_mean_plot_static

rng = np.random.default_rng(42)
n = 160
depth = pd.Series(rng.uniform(low=0.0, high=200.0, size=n), name="Depth (m)")
temperature = pd.Series(25.0 - 0.08 * depth + rng.normal(loc=0.0, scale=1.5, size=n), name="Water temperature (C)")

ax = binned_mean_plot_static(
    depth,
    temperature,
    bins=8,
    title="Mean Water Temperature by Depth Bin",
    color="darkcyan",
)
plt.show()
''',
    "dataviz.bivariate.trends.binned_mean_plot_interactive": '''import numpy as np
import pandas as pd
from dataviz.bivariate.trends import binned_mean_plot_interactive

rng = np.random.default_rng(42)
n = 160
depth = pd.Series(rng.uniform(low=0.0, high=200.0, size=n), name="Depth (m)")
temperature = pd.Series(25.0 - 0.08 * depth + rng.normal(loc=0.0, scale=1.5, size=n), name="Water temperature (C)")

fig = binned_mean_plot_interactive(
    depth,
    temperature,
    bins=8,
    title="Mean Water Temperature by Depth Bin",
    color="darkcyan",
)
fig.show()
''',
    "dataviz.bivariate.trends.errorbar_plot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.bivariate.trends import errorbar_plot_static

rng = np.random.default_rng(42)
dose = pd.Series(np.arange(0, 11, 2), name="Fertilizer dose (kg/ha)")
mean_yield = pd.Series(2.5 + 0.6 * dose - 0.03 * dose**2, name="Mean yield (t/ha)")
yield_std = pd.Series(rng.uniform(low=0.15, high=0.35, size=len(dose)), name="Yield SD")

ax = errorbar_plot_static(
    dose,
    mean_yield,
    yerr=yield_std,
    title="Crop Yield Response to Fertilizer",
    color="darkgreen",
    capsize=5.0,
)
plt.show()
''',
    "dataviz.bivariate.trends.errorbar_plot_interactive": '''import numpy as np
import pandas as pd
from dataviz.bivariate.trends import errorbar_plot_interactive

rng = np.random.default_rng(42)
dose = pd.Series(np.arange(0, 11, 2), name="Fertilizer dose (kg/ha)")
mean_yield = pd.Series(2.5 + 0.6 * dose - 0.03 * dose**2, name="Mean yield (t/ha)")
yield_std = pd.Series(rng.uniform(low=0.15, high=0.35, size=len(dose)), name="Yield SD")

fig = errorbar_plot_interactive(
    dose,
    mean_yield,
    yerr=yield_std,
    title="Crop Yield Response to Fertilizer",
    color="darkgreen",
)
fig.show()
''',
    "dataviz.bivariate.trends.area_between_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.bivariate.trends import area_between_static

rng = np.random.default_rng(42)
month = pd.Series(np.arange(1, 37), name="Month")
forecast = 100.0 + 1.5 * month + np.cumsum(rng.normal(loc=0.0, scale=0.5, size=36))
lower = pd.Series(forecast - 8.0, name="Lower bound")
upper = pd.Series(forecast + 8.0, name="Upper bound")

ax = area_between_static(
    month,
    lower,
    upper,
    title="Demand Forecast Tolerance Band",
    xlabel="Month",
    ylabel="Demand (units)",
    color="steelblue",
    alpha=0.35,
)
plt.show()
''',
    "dataviz.bivariate.trends.area_between_interactive": '''import numpy as np
import pandas as pd
from dataviz.bivariate.trends import area_between_interactive

rng = np.random.default_rng(42)
month = pd.Series(np.arange(1, 37), name="Month")
forecast = 100.0 + 1.5 * month + np.cumsum(rng.normal(loc=0.0, scale=0.5, size=36))
lower = pd.Series(forecast - 8.0, name="Lower bound")
upper = pd.Series(forecast + 8.0, name="Upper bound")

fig = area_between_interactive(
    month,
    lower,
    upper,
    title="Demand Forecast Tolerance Band",
    xlabel="Month",
    ylabel="Demand (units)",
)
fig.show()
''',
    "dataviz.bivariate.trends.step_plot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.bivariate.trends import step_plot_static

quarter = pd.Series(np.arange(1, 13), name="Quarter")
price = pd.Series(
    [9.99, 9.99, 10.49, 10.49, 10.49, 10.99, 10.99, 11.49, 11.49, 11.49, 11.99, 11.99],
    name="Subscription price (USD)",
)

ax = step_plot_static(
    quarter,
    price,
    where="post",
    title="Subscription Price Changes Over Time",
    color="darkorange",
)
plt.show()
''',
    "dataviz.bivariate.trends.step_plot_interactive": '''import numpy as np
import pandas as pd
from dataviz.bivariate.trends import step_plot_interactive

quarter = pd.Series(np.arange(1, 13), name="Quarter")
price = pd.Series(
    [9.99, 9.99, 10.49, 10.49, 10.49, 10.99, 10.99, 11.49, 11.49, 11.49, 11.99, 11.99],
    name="Subscription price (USD)",
)

fig = step_plot_interactive(
    quarter,
    price,
    shape="hv",
    title="Subscription Price Changes Over Time",
    color="darkorange",
)
fig.show()
''',
}
