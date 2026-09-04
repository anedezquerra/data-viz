"""Curated rich examples for univariate member pages."""

EXAMPLES = {
    "dataviz.univariate.inference.BootstrapCI": '''from dataviz.univariate.inference import BootstrapCI

result = BootstrapCI(
    statistic="mean",
    estimate=9.84,
    lower=9.12,
    upper=10.61,
    confidence_level=0.95,
    n_resamples=2000,
)
print(result)''',
    "dataviz.univariate.inference.bootstrap_distribution": '''import numpy as np
import pandas as pd
from dataviz.univariate.inference import bootstrap_distribution

rng = np.random.default_rng(42)
wait_minutes = pd.Series(
    rng.lognormal(mean=2.2, sigma=0.6, size=180).round(1),
    name="wait_minutes",
)
result = bootstrap_distribution(wait_minutes, statistic="median", n_resamples=1000, seed=7)
print(result)''',
    "dataviz.univariate.inference.bootstrap_ci": '''import numpy as np
import pandas as pd
from dataviz.univariate.inference import bootstrap_ci

rng = np.random.default_rng(42)
wait_minutes = pd.Series(
    rng.lognormal(mean=2.2, sigma=0.6, size=180).round(1),
    name="wait_minutes",
)
result = bootstrap_ci(wait_minutes, statistic="mean", confidence_level=0.90, n_resamples=1500, seed=7)
print(result)''',
    "dataviz.univariate.inference.bootstrap_distribution_plot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.univariate.inference import bootstrap_distribution_plot_static

rng = np.random.default_rng(42)
wait_minutes = pd.Series(
    rng.lognormal(mean=2.2, sigma=0.6, size=180).round(1),
    name="wait_minutes",
)
ax = bootstrap_distribution_plot_static(
    wait_minutes,
    statistic="mean",
    n_resamples=1000,
    seed=7,
    title="Bootstrap Mean Wait Time (Call Center)",
    color="steelblue",
)
ax.set_xlabel("Mean wait time (minutes)")
plt.show()''',
    "dataviz.univariate.inference.bootstrap_distribution_plot_interactive": '''import numpy as np
import pandas as pd
from dataviz.univariate.inference import bootstrap_distribution_plot_interactive

rng = np.random.default_rng(42)
wait_minutes = pd.Series(
    rng.lognormal(mean=2.2, sigma=0.6, size=180).round(1),
    name="wait_minutes",
)
fig = bootstrap_distribution_plot_interactive(
    wait_minutes,
    statistic="mean",
    n_resamples=1000,
    seed=7,
    title="Bootstrap Mean Wait Time (Call Center)",
    color="steelblue",
    height=500,
)
fig.show()''',
    "dataviz.univariate.ordinal.ordered_category_counts": '''import numpy as np
import pandas as pd
from dataviz.univariate.ordinal import ordered_category_counts

rng = np.random.default_rng(42)
scale = ["Very dissatisfied", "Dissatisfied", "Neutral", "Satisfied", "Very satisfied"]
satisfaction = pd.Series(
    rng.choice(scale, size=220, p=[0.08, 0.17, 0.20, 0.35, 0.20]),
    name="satisfaction",
)
result = ordered_category_counts(satisfaction, order=scale, normalize=True)
print(result)''',
    "dataviz.univariate.ordinal.likert_summary": '''import numpy as np
import pandas as pd
from dataviz.univariate.ordinal import likert_summary

rng = np.random.default_rng(42)
scale = ["Very dissatisfied", "Dissatisfied", "Neutral", "Satisfied", "Very satisfied"]
satisfaction = pd.Series(
    rng.choice(scale, size=220, p=[0.08, 0.17, 0.20, 0.35, 0.20]),
    name="satisfaction",
)
result = likert_summary(satisfaction, order=scale)
print(result)''',
    "dataviz.univariate.ordinal.ordinal_bar_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.univariate.ordinal import ordinal_bar_static

rng = np.random.default_rng(42)
scale = ["Very dissatisfied", "Dissatisfied", "Neutral", "Satisfied", "Very satisfied"]
satisfaction = pd.Series(
    rng.choice(scale, size=220, p=[0.08, 0.17, 0.20, 0.35, 0.20]),
    name="satisfaction",
)
ax = ordinal_bar_static(
    satisfaction,
    order=scale,
    normalize=True,
    title="Post-Purchase Satisfaction Survey (n=220)",
    color="teal",
    theme="minimal",
)
ax.set_ylabel("Share of respondents")
plt.show()''',
    "dataviz.univariate.ordinal.ordinal_bar_interactive": '''import numpy as np
import pandas as pd
from dataviz.univariate.ordinal import ordinal_bar_interactive

rng = np.random.default_rng(42)
scale = ["Very dissatisfied", "Dissatisfied", "Neutral", "Satisfied", "Very satisfied"]
satisfaction = pd.Series(
    rng.choice(scale, size=220, p=[0.08, 0.17, 0.20, 0.35, 0.20]),
    name="satisfaction",
)
fig = ordinal_bar_interactive(
    satisfaction,
    order=scale,
    normalize=True,
    title="Post-Purchase Satisfaction Survey (n=220)",
    color="teal",
    height=500,
)
fig.show()''',
    "dataviz.univariate.profile.UnivariateProfile": '''from dataviz.univariate.profile import UnivariateProfile
from dataviz.univariate.quality import DataQualitySummary

quality = DataQualitySummary(
    count=150, missing=3, missing_rate=0.02, unique=118,
    duplicate_rate=0.19, zero_rate=0.0, negative_rate=0.0,
)
result = UnivariateProfile(
    name="monthly_spend",
    kind="numeric",
    quality=quality,
    summary={"count": 147, "mean": 82.4},
)
print(result)''',
    "dataviz.univariate.profile.auto_profile": '''import numpy as np
import pandas as pd
from dataviz.univariate.profile import auto_profile

rng = np.random.default_rng(42)
customers = pd.DataFrame(
    {"monthly_spend": rng.gamma(shape=3.0, scale=28.0, size=150).round(2)}
)
customers.loc[[5, 41, 96], "monthly_spend"] = np.nan
result = auto_profile("monthly_spend", data=customers)
print(result)''',
    "dataviz.univariate.profile.auto_profile_chart_interactive": '''import numpy as np
import pandas as pd
from dataviz.univariate.profile import auto_profile_chart_interactive

rng = np.random.default_rng(42)
customers = pd.DataFrame(
    {"monthly_spend": rng.gamma(shape=3.0, scale=28.0, size=150).round(2)}
)
customers.loc[[5, 41, 96], "monthly_spend"] = np.nan
fig = auto_profile_chart_interactive(
    "monthly_spend",
    data=customers,
    title="Monthly Spend Profile",
)
fig.show()''',
    "dataviz.univariate.quality.DataQualitySummary": '''from dataviz.univariate.quality import DataQualitySummary

result = DataQualitySummary(
    count=140,
    missing=6,
    missing_rate=6 / 140,
    unique=129,
    duplicate_rate=0.036,
    zero_rate=0.01,
    negative_rate=0.02,
)
print(result)''',
    "dataviz.univariate.quality.data_quality_summary": '''import numpy as np
import pandas as pd
from dataviz.univariate.quality import data_quality_summary

rng = np.random.default_rng(42)
readings = rng.normal(loc=55.0, scale=4.0, size=140).round(2)
readings[[3, 27, 58, 91, 120]] = np.nan
readings[[10, 66, 101]] = -999.0
sensor = pd.Series(readings, name="temperature_c")
result = data_quality_summary(sensor)
print(result)''',
    "dataviz.univariate.quality.quality_bar_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.univariate.quality import quality_bar_static

rng = np.random.default_rng(42)
readings = rng.normal(loc=55.0, scale=4.0, size=140).round(2)
readings[[3, 27, 58, 91, 120]] = np.nan
readings[[10, 66, 101]] = -999.0
sensor = pd.Series(readings, name="temperature_c")
ax = quality_bar_static(
    sensor,
    title="Sensor Feed Quality Rates",
    color="slategray",
    theme="minimal",
)
ax.set_ylabel("Rate of observations")
plt.show()''',
    "dataviz.univariate.quality.quality_bar_interactive": '''import numpy as np
import pandas as pd
from dataviz.univariate.quality import quality_bar_interactive

rng = np.random.default_rng(42)
readings = rng.normal(loc=55.0, scale=4.0, size=140).round(2)
readings[[3, 27, 58, 91, 120]] = np.nan
readings[[10, 66, 101]] = -999.0
sensor = pd.Series(readings, name="temperature_c")
fig = quality_bar_interactive(
    sensor,
    title="Sensor Feed Quality Rates",
    color="slategray",
    height=450,
)
fig.show()''',
    "dataviz.univariate.quality.sentinel_value_counts": '''import numpy as np
import pandas as pd
from dataviz.univariate.quality import sentinel_value_counts

rng = np.random.default_rng(42)
readings = rng.normal(loc=55.0, scale=4.0, size=140).round(2)
readings[[3, 27, 58, 91, 120]] = np.nan
readings[[10, 66, 101]] = -999.0
sensor = pd.Series(readings, name="temperature_c")
result = sentinel_value_counts(sensor, sentinels=[-999.0])
print(result)''',
    "dataviz.univariate.quality.sentinel_rate": '''import numpy as np
import pandas as pd
from dataviz.univariate.quality import sentinel_rate

rng = np.random.default_rng(42)
readings = rng.normal(loc=55.0, scale=4.0, size=140).round(2)
readings[[3, 27, 58, 91, 120]] = np.nan
readings[[10, 66, 101]] = -999.0
sensor = pd.Series(readings, name="temperature_c")
result = sentinel_rate(sensor, sentinels=[-999.0])
print(result)''',
    "dataviz.univariate.robust.RobustStats": '''from dataviz.univariate.robust import RobustStats

result = RobustStats(
    count=150,
    median=41200.0,
    mad=9800.0,
    scaled_mad=14523.6,
    trimmed_mean=44750.0,
    winsorized_mean=46310.0,
    q1=31800.0,
    q3=58900.0,
    iqr=27100.0,
    lower_fence=-8850.0,
    upper_fence=99550.0,
)
print(result)''',
    "dataviz.univariate.robust.validate_proportion": '''from dataviz.univariate.robust import validate_proportion

result = validate_proportion(0.1, "trim_proportion")
print(result)''',
    "dataviz.univariate.robust.mad_zscores": '''import numpy as np
import pandas as pd
from dataviz.univariate.robust import mad_zscores

rng = np.random.default_rng(42)
income_k = rng.gamma(shape=2.5, scale=22.0, size=150).round(1)
income_k[[12, 77, 130]] = [950.0, 1200.0, 875.0]
household_income = pd.Series(income_k, name="household_income_k")
result = mad_zscores(household_income)
print(result)''',
    "dataviz.univariate.robust.mad_outliers": '''import numpy as np
import pandas as pd
from dataviz.univariate.robust import mad_outliers

rng = np.random.default_rng(42)
income_k = rng.gamma(shape=2.5, scale=22.0, size=150).round(1)
income_k[[12, 77, 130]] = [950.0, 1200.0, 875.0]
household_income = pd.Series(income_k, name="household_income_k")
result = mad_outliers(household_income, threshold=3.5)
print(result)''',
    "dataviz.univariate.robust.trimmed_mean": '''import numpy as np
import pandas as pd
from dataviz.univariate.robust import trimmed_mean

rng = np.random.default_rng(42)
income_k = rng.gamma(shape=2.5, scale=22.0, size=150).round(1)
income_k[[12, 77, 130]] = [950.0, 1200.0, 875.0]
household_income = pd.Series(income_k, name="household_income_k")
result = trimmed_mean(household_income, proportion=0.1)
print(result)''',
    "dataviz.univariate.robust.winsorize_series": '''import numpy as np
import pandas as pd
from dataviz.univariate.robust import winsorize_series

rng = np.random.default_rng(42)
income_k = rng.gamma(shape=2.5, scale=22.0, size=150).round(1)
income_k[[12, 77, 130]] = [950.0, 1200.0, 875.0]
household_income = pd.Series(income_k, name="household_income_k")
result = winsorize_series(household_income, limits=0.05)
print(result)''',
    "dataviz.univariate.robust.robust_summary": '''import numpy as np
import pandas as pd
from dataviz.univariate.robust import robust_summary

rng = np.random.default_rng(42)
income_k = rng.gamma(shape=2.5, scale=22.0, size=150).round(1)
income_k[[12, 77, 130]] = [950.0, 1200.0, 875.0]
household_income = pd.Series(income_k, name="household_income_k")
result = robust_summary(household_income, trim_proportion=0.1, winsor_limits=0.05)
print(result)''',
    "dataviz.univariate.robust.robust_location_plot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.univariate.robust import robust_location_plot_static

rng = np.random.default_rng(42)
income_k = rng.gamma(shape=2.5, scale=22.0, size=150).round(1)
income_k[[12, 77, 130]] = [950.0, 1200.0, 875.0]
household_income = pd.Series(income_k, name="household_income_k")
ax = robust_location_plot_static(
    household_income,
    title="Household Income with Robust Location Estimates",
    color="lightsteelblue",
    theme="minimal",
)
ax.set_xlabel("Household income (thousands)")
plt.show()''',
    "dataviz.univariate.robust.robust_location_plot_interactive": '''import numpy as np
import pandas as pd
from dataviz.univariate.robust import robust_location_plot_interactive

rng = np.random.default_rng(42)
income_k = rng.gamma(shape=2.5, scale=22.0, size=150).round(1)
income_k[[12, 77, 130]] = [950.0, 1200.0, 875.0]
household_income = pd.Series(income_k, name="household_income_k")
fig = robust_location_plot_interactive(
    household_income,
    title="Household Income with Robust Location Estimates",
    color="lightsteelblue",
    height=500,
)
fig.show()''',
    "dataviz.univariate.stats.UnivariateStats": '''from dataviz.univariate.stats import UnivariateStats

result = UnivariateStats(
    count=200,
    missing=0,
    mean=181.2,
    median=179.5,
    std=44.8,
    variance=2007.0,
    minimum=62.0,
    q1=149.0,
    q3=211.0,
    maximum=312.0,
    iqr=62.0,
    skewness=0.21,
    kurtosis=-0.12,
    sem=3.17,
    mad=37.5,
)
print(result)''',
    "dataviz.univariate.stats.as_numeric_series": '''import numpy as np
import pandas as pd
from dataviz.univariate.stats import as_numeric_series

rng = np.random.default_rng(42)
session_seconds = rng.normal(loc=180.0, scale=45.0, size=200).round(1)
result = as_numeric_series(session_seconds, name="session_seconds")
print(result)''',
    "dataviz.univariate.stats.univariate_summary": '''import numpy as np
import pandas as pd
from dataviz.univariate.stats import univariate_summary

rng = np.random.default_rng(42)
session_seconds = pd.Series(
    rng.normal(loc=180.0, scale=45.0, size=200).round(1),
    name="session_seconds",
)
result = univariate_summary(session_seconds)
print(result)''',
    "dataviz.univariate.stats.iqr_outliers": '''import numpy as np
import pandas as pd
from dataviz.univariate.stats import iqr_outliers

rng = np.random.default_rng(42)
session_seconds = pd.Series(
    rng.normal(loc=180.0, scale=45.0, size=200).round(1),
    name="session_seconds",
)
result = iqr_outliers(session_seconds, multiplier=1.5)
print(result)''',
    "dataviz.univariate.stats.zscore_outliers": '''import numpy as np
import pandas as pd
from dataviz.univariate.stats import zscore_outliers

rng = np.random.default_rng(42)
session_seconds = pd.Series(
    rng.normal(loc=180.0, scale=45.0, size=200).round(1),
    name="session_seconds",
)
result = zscore_outliers(session_seconds, threshold=3.0)
print(result)''',
    "dataviz.univariate.stats.recommended_bin_count": '''import numpy as np
import pandas as pd
from dataviz.univariate.stats import recommended_bin_count

rng = np.random.default_rng(42)
session_seconds = pd.Series(
    rng.normal(loc=180.0, scale=45.0, size=200).round(1),
    name="session_seconds",
)
result = recommended_bin_count(session_seconds, method="fd")
print(result)''',
    "dataviz.univariate.stats.percentile_table": '''import numpy as np
import pandas as pd
from dataviz.univariate.stats import percentile_table

rng = np.random.default_rng(42)
session_seconds = pd.Series(
    rng.normal(loc=180.0, scale=45.0, size=200).round(1),
    name="session_seconds",
)
result = percentile_table(session_seconds, step=10)
print(result)''',
    "dataviz.univariate.tail.ConcentrationStats": '''from dataviz.univariate.tail import ConcentrationStats

result = ConcentrationStats(
    total=1240500.0,
    gini=0.47,
    top_10_share=0.38,
    top_20_share=0.56,
)
print(result)''',
    "dataviz.univariate.tail.survival_values": '''import numpy as np
import pandas as pd
from dataviz.univariate.tail import survival_values

rng = np.random.default_rng(42)
claim_amounts = pd.Series(
    (rng.pareto(a=2.5, size=160) * 5000 + 1000).round(0),
    name="claim_amount",
)
result = survival_values(claim_amounts)
print(result)''',
    "dataviz.univariate.tail.exceedance_table": '''import numpy as np
import pandas as pd
from dataviz.univariate.tail import exceedance_table

rng = np.random.default_rng(42)
claim_amounts = pd.Series(
    (rng.pareto(a=2.5, size=160) * 5000 + 1000).round(0),
    name="claim_amount",
)
thresholds = [5000, 10000, 25000, 50000]
result = exceedance_table(claim_amounts, thresholds=thresholds)
print(result)''',
    "dataviz.univariate.tail.concentration_summary": '''import numpy as np
import pandas as pd
from dataviz.univariate.tail import concentration_summary

rng = np.random.default_rng(42)
claim_amounts = pd.Series(
    (rng.pareto(a=2.5, size=160) * 5000 + 1000).round(0),
    name="claim_amount",
)
result = concentration_summary(claim_amounts)
print(result)''',
    "dataviz.univariate.tail.lorenz_curve_values": '''import numpy as np
import pandas as pd
from dataviz.univariate.tail import lorenz_curve_values

rng = np.random.default_rng(42)
claim_amounts = pd.Series(
    (rng.pareto(a=2.5, size=160) * 5000 + 1000).round(0),
    name="claim_amount",
)
result = lorenz_curve_values(claim_amounts)
print(result)''',
    "dataviz.univariate.tail.survival_curve_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.univariate.tail import survival_curve_static

rng = np.random.default_rng(42)
claim_amounts = pd.Series(
    (rng.pareto(a=2.5, size=160) * 5000 + 1000).round(0),
    name="claim_amount",
)
ax = survival_curve_static(
    claim_amounts,
    title="Insurance Claim Survival Curve",
    color="darkred",
    theme="minimal",
)
ax.set_xlabel("Claim amount (USD)")
plt.show()''',
    "dataviz.univariate.tail.survival_curve_interactive": '''import numpy as np
import pandas as pd
from dataviz.univariate.tail import survival_curve_interactive

rng = np.random.default_rng(42)
claim_amounts = pd.Series(
    (rng.pareto(a=2.5, size=160) * 5000 + 1000).round(0),
    name="claim_amount",
)
fig = survival_curve_interactive(
    claim_amounts,
    title="Insurance Claim Survival Curve",
    color="darkred",
    height=500,
)
fig.show()''',
    "dataviz.univariate.tail.lorenz_curve_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.univariate.tail import lorenz_curve_static

rng = np.random.default_rng(42)
claim_amounts = pd.Series(
    (rng.pareto(a=2.5, size=160) * 5000 + 1000).round(0),
    name="claim_amount",
)
ax = lorenz_curve_static(
    claim_amounts,
    title="Lorenz Curve of Claim Amounts",
    color="navy",
    theme="minimal",
)
plt.show()''',
    "dataviz.univariate.tail.lorenz_curve_interactive": '''import numpy as np
import pandas as pd
from dataviz.univariate.tail import lorenz_curve_interactive

rng = np.random.default_rng(42)
claim_amounts = pd.Series(
    (rng.pareto(a=2.5, size=160) * 5000 + 1000).round(0),
    name="claim_amount",
)
fig = lorenz_curve_interactive(
    claim_amounts,
    title="Lorenz Curve of Claim Amounts",
    color="navy",
    height=550,
)
fig.show()''',
    "dataviz.univariate.text.BooleanSummary": '''from dataviz.univariate.text import BooleanSummary

result = BooleanSummary(count=120, true_count=50, false_count=70, true_rate=50 / 120)
print(result)''',
    "dataviz.univariate.text.BooleanRateInterval": '''from dataviz.univariate.text import BooleanRateInterval

result = BooleanRateInterval(
    true_rate=0.42,
    lower=0.33,
    upper=0.51,
    confidence_level=0.95,
)
print(result)''',
    "dataviz.univariate.text.boolean_summary": '''import numpy as np
import pandas as pd
from dataviz.univariate.text import boolean_summary

rng = np.random.default_rng(42)
subscribed = pd.Series(rng.random(120) < 0.42, name="newsletter_subscribed")
result = boolean_summary(subscribed)
print(result)''',
    "dataviz.univariate.text.boolean_wilson_interval": '''import numpy as np
import pandas as pd
from dataviz.univariate.text import boolean_wilson_interval

rng = np.random.default_rng(42)
subscribed = pd.Series(rng.random(120) < 0.42, name="newsletter_subscribed")
result = boolean_wilson_interval(subscribed, confidence_level=0.90)
print(result)''',
    "dataviz.univariate.text.string_length_summary": '''import numpy as np
import pandas as pd
from dataviz.univariate.text import string_length_summary

rng = np.random.default_rng(42)
vocab = ["battery", "screen", "delivery", "quality", "support", "price", "design", "fast"]
reviews = pd.Series(
    [" ".join(rng.choice(vocab, size=rng.integers(3, 9))) for _ in range(60)],
    name="review",
)
result = string_length_summary(reviews)
print(result)''',
    "dataviz.univariate.text.token_count_summary": '''import numpy as np
import pandas as pd
from dataviz.univariate.text import token_count_summary

rng = np.random.default_rng(42)
vocab = ["battery", "screen", "delivery", "quality", "support", "price", "design", "fast"]
reviews = pd.Series(
    [" ".join(rng.choice(vocab, size=rng.integers(3, 9))) for _ in range(60)],
    name="review",
)
result = token_count_summary(reviews)
print(result)''',
    "dataviz.univariate.text.top_terms": '''import numpy as np
import pandas as pd
from dataviz.univariate.text import top_terms

rng = np.random.default_rng(42)
vocab = ["battery", "screen", "delivery", "quality", "support", "price", "design", "fast"]
reviews = pd.Series(
    [" ".join(rng.choice(vocab, size=rng.integers(3, 9))) for _ in range(60)],
    name="review",
)
result = top_terms(reviews, top_n=8, lowercase=True)
print(result)''',
    "dataviz.univariate.text.boolean_bar_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.univariate.text import boolean_bar_static

rng = np.random.default_rng(42)
subscribed = pd.Series(rng.random(120) < 0.42, name="newsletter_subscribed")
ax = boolean_bar_static(
    subscribed,
    title="Newsletter Subscription Status",
    color="seagreen",
    theme="minimal",
)
ax.set_ylabel("Number of customers")
plt.show()''',
    "dataviz.univariate.text.boolean_bar_interactive": '''import numpy as np
import pandas as pd
from dataviz.univariate.text import boolean_bar_interactive

rng = np.random.default_rng(42)
subscribed = pd.Series(rng.random(120) < 0.42, name="newsletter_subscribed")
fig = boolean_bar_interactive(
    subscribed,
    title="Newsletter Subscription Status",
    color="seagreen",
    height=450,
)
fig.show()''',
    "dataviz.univariate.text.top_terms_bar_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.univariate.text import top_terms_bar_static

rng = np.random.default_rng(42)
vocab = ["battery", "screen", "delivery", "quality", "support", "price", "design", "fast"]
reviews = pd.Series(
    [" ".join(rng.choice(vocab, size=rng.integers(3, 9))) for _ in range(60)],
    name="review",
)
ax = top_terms_bar_static(
    reviews,
    top_n=8,
    title="Most Common Terms in Product Reviews",
    color="coral",
    theme="minimal",
)
ax.set_xlabel("Occurrences")
plt.show()''',
    "dataviz.univariate.text.top_terms_bar_interactive": '''import numpy as np
import pandas as pd
from dataviz.univariate.text import top_terms_bar_interactive

rng = np.random.default_rng(42)
vocab = ["battery", "screen", "delivery", "quality", "support", "price", "design", "fast"]
reviews = pd.Series(
    [" ".join(rng.choice(vocab, size=rng.integers(3, 9))) for _ in range(60)],
    name="review",
)
fig = top_terms_bar_interactive(
    reviews,
    top_n=8,
    title="Most Common Terms in Product Reviews",
    color="coral",
    height=500,
)
fig.show()''',
    "dataviz.univariate.transforms.TransformResult": '''import numpy as np
import pandas as pd
from dataviz.univariate.transforms import transform_series

rng = np.random.default_rng(42)
reaction_ms = pd.Series(
    rng.gamma(shape=3.0, scale=90.0, size=150).round(1),
    name="reaction_ms",
)
result = transform_series(reaction_ms, method="log")
print(result)''',
    "dataviz.univariate.transforms.transform_series": '''import numpy as np
import pandas as pd
from dataviz.univariate.transforms import transform_series

rng = np.random.default_rng(42)
reaction_ms = pd.Series(
    rng.gamma(shape=3.0, scale=90.0, size=150).round(1),
    name="reaction_ms",
)
result = transform_series(reaction_ms, method="sqrt")
print(result)''',
    "dataviz.univariate.transforms.transformation_summary": '''import numpy as np
import pandas as pd
from dataviz.univariate.transforms import transformation_summary

rng = np.random.default_rng(42)
reaction_ms = pd.Series(
    rng.gamma(shape=3.0, scale=90.0, size=150).round(1),
    name="reaction_ms",
)
result = transformation_summary(reaction_ms)
print(result)''',
    "dataviz.univariate.transforms.transformation_comparison_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.univariate.transforms import transformation_comparison_static

rng = np.random.default_rng(42)
reaction_ms = pd.Series(
    rng.gamma(shape=3.0, scale=90.0, size=150).round(1),
    name="reaction_ms",
)
fig = transformation_comparison_static(
    reaction_ms,
    bins=20,
    title="Reaction Time Under Common Transformations",
    color="mediumpurple",
)
plt.show()''',
    "dataviz.univariate.transforms.transformation_comparison_interactive": '''import numpy as np
import pandas as pd
from dataviz.univariate.transforms import transformation_comparison_interactive

rng = np.random.default_rng(42)
reaction_ms = pd.Series(
    rng.gamma(shape=3.0, scale=90.0, size=150).round(1),
    name="reaction_ms",
)
fig = transformation_comparison_interactive(
    reaction_ms,
    bins=20,
    title="Reaction Time Under Common Transformations",
    color="mediumpurple",
    height=600,
)
fig.show()''',
    "dataviz.univariate.treatment.OutlierTreatmentResult": '''import pandas as pd
from dataviz.univariate.treatment import OutlierTreatmentResult

original = pd.Series([98.0, 105.0, 102.0, 480.0], name="latency_ms")
treated = pd.Series([98.0, 105.0, 102.0, 180.0], name="latency_ms")
mask = pd.Series([False, False, False, True])
result = OutlierTreatmentResult(
    original=original,
    treated=treated,
    mask=mask,
    method="cap",
    rule="iqr",
)
print(result)''',
    "dataviz.univariate.treatment.outlier_mask": '''import numpy as np
import pandas as pd
from dataviz.univariate.treatment import outlier_mask

rng = np.random.default_rng(42)
latency = rng.normal(loc=120.0, scale=15.0, size=180).round(1)
latency[[9, 54, 121, 160]] = [520.0, 610.0, 480.0, 700.0]
latency_ms = pd.Series(latency, name="latency_ms")
result = outlier_mask(latency_ms, rule="iqr", multiplier=1.5)
print(result)''',
    "dataviz.univariate.treatment.cap_outliers": '''import numpy as np
import pandas as pd
from dataviz.univariate.treatment import cap_outliers

rng = np.random.default_rng(42)
latency = rng.normal(loc=120.0, scale=15.0, size=180).round(1)
latency[[9, 54, 121, 160]] = [520.0, 610.0, 480.0, 700.0]
latency_ms = pd.Series(latency, name="latency_ms")
result = cap_outliers(latency_ms, rule="iqr", multiplier=1.5)
print(result)''',
    "dataviz.univariate.treatment.remove_outliers": '''import numpy as np
import pandas as pd
from dataviz.univariate.treatment import remove_outliers

rng = np.random.default_rng(42)
latency = rng.normal(loc=120.0, scale=15.0, size=180).round(1)
latency[[9, 54, 121, 160]] = [520.0, 610.0, 480.0, 700.0]
latency_ms = pd.Series(latency, name="latency_ms")
result = remove_outliers(latency_ms, rule="mad", threshold=3.5)
print(result)''',
    "dataviz.univariate.treatment.flag_outliers": '''import numpy as np
import pandas as pd
from dataviz.univariate.treatment import flag_outliers

rng = np.random.default_rng(42)
latency = rng.normal(loc=120.0, scale=15.0, size=180).round(1)
latency[[9, 54, 121, 160]] = [520.0, 610.0, 480.0, 700.0]
latency_ms = pd.Series(latency, name="latency_ms")
result = flag_outliers(latency_ms, rule="zscore", threshold=3.0)
print(result)''',
    "dataviz.univariate.treatment.outlier_treatment_comparison_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.univariate.treatment import outlier_treatment_comparison_static

rng = np.random.default_rng(42)
latency = rng.normal(loc=120.0, scale=15.0, size=180).round(1)
latency[[9, 54, 121, 160]] = [520.0, 610.0, 480.0, 700.0]
latency_ms = pd.Series(latency, name="latency_ms")
ax = outlier_treatment_comparison_static(
    latency_ms,
    rule="iqr",
    treatment="cap",
    title="API Latency Before and After Capping",
    color="skyblue",
    theme="minimal",
)
ax.set_ylabel("Latency (ms)")
plt.show()''',
    "dataviz.univariate.treatment.outlier_treatment_comparison_interactive": '''import numpy as np
import pandas as pd
from dataviz.univariate.treatment import outlier_treatment_comparison_interactive

rng = np.random.default_rng(42)
latency = rng.normal(loc=120.0, scale=15.0, size=180).round(1)
latency[[9, 54, 121, 160]] = [520.0, 610.0, 480.0, 700.0]
latency_ms = pd.Series(latency, name="latency_ms")
fig = outlier_treatment_comparison_interactive(
    latency_ms,
    rule="iqr",
    treatment="cap",
    title="API Latency Before and After Capping",
    color="skyblue",
    height=500,
)
fig.show()''',
    "dataviz.univariate.violin_plot.violin_plot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.univariate.violin_plot import violin_plot_static

rng = np.random.default_rng(42)
carriers = rng.choice(["Aeris", "Boreal", "Cirrus"], size=180)
offsets = {"Aeris": 4.2, "Boreal": 5.1, "Cirrus": 3.6}
delivery = [rng.normal(offsets[c], 0.9) for c in carriers]
shipments = pd.DataFrame({"carrier": carriers, "delivery_days": np.round(delivery, 1)})
ax = violin_plot_static(
    shipments,
    x="carrier",
    y="delivery_days",
    title="Delivery Time by Carrier",
    xlabel="Carrier",
    ylabel="Delivery time (days)",
    palette="Set2",
    inner="quartile",
    theme="minimal",
)
plt.show()''',
    "dataviz.univariate.violin_plot.violin_plot_interactive": '''import numpy as np
import pandas as pd
from dataviz.univariate.violin_plot import violin_plot_interactive

rng = np.random.default_rng(42)
carriers = rng.choice(["Aeris", "Boreal", "Cirrus"], size=180)
offsets = {"Aeris": 4.2, "Boreal": 5.1, "Cirrus": 3.6}
delivery = [rng.normal(offsets[c], 0.9) for c in carriers]
shipments = pd.DataFrame({"carrier": carriers, "delivery_days": np.round(delivery, 1)})
fig = violin_plot_interactive(
    shipments,
    x="carrier",
    y="delivery_days",
    title="Delivery Time by Carrier",
    xlabel="Carrier",
    ylabel="Delivery time (days)",
    meanline=True,
    height=550,
)
fig.show()''',
    "dataviz.univariate.weighted.WeightedStats": '''from dataviz.univariate.weighted import WeightedStats

result = WeightedStats(
    count=250,
    weight_sum=372.5,
    mean=6.8,
    variance=5.1,
    std=2.26,
    q1=5.0,
    median=7.0,
    q3=9.0,
)
print(result)''',
    "dataviz.univariate.weighted.resolve_weighted_series": '''import numpy as np
import pandas as pd
from dataviz.univariate.weighted import resolve_weighted_series

rng = np.random.default_rng(42)
nps_score = pd.Series(rng.integers(0, 11, size=250), name="nps_score")
sample_weight = pd.Series(rng.uniform(0.5, 2.5, size=250).round(2), name="sample_weight")
result = resolve_weighted_series(nps_score, sample_weight)
print(result)''',
    "dataviz.univariate.weighted.weighted_quantile": '''import numpy as np
import pandas as pd
from dataviz.univariate.weighted import weighted_quantile

rng = np.random.default_rng(42)
nps_score = pd.Series(rng.integers(0, 11, size=250), name="nps_score")
sample_weight = pd.Series(rng.uniform(0.5, 2.5, size=250).round(2), name="sample_weight")
result = weighted_quantile(nps_score, sample_weight, quantile=0.75)
print(result)''',
    "dataviz.univariate.weighted.weighted_summary": '''import numpy as np
import pandas as pd
from dataviz.univariate.weighted import weighted_summary

rng = np.random.default_rng(42)
nps_score = pd.Series(rng.integers(0, 11, size=250), name="nps_score")
sample_weight = pd.Series(rng.uniform(0.5, 2.5, size=250).round(2), name="sample_weight")
result = weighted_summary(nps_score, sample_weight)
print(result)''',
    "dataviz.univariate.weighted.weighted_histogram_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.univariate.weighted import weighted_histogram_static

rng = np.random.default_rng(42)
nps_score = pd.Series(rng.integers(0, 11, size=250), name="nps_score")
sample_weight = pd.Series(rng.uniform(0.5, 2.5, size=250).round(2), name="sample_weight")
ax = weighted_histogram_static(
    nps_score,
    sample_weight,
    bins=11,
    title="Weighted NPS Distribution",
    xlabel="NPS score",
    color="goldenrod",
    theme="minimal",
)
ax.set_ylabel("Weighted count")
plt.show()''',
    "dataviz.univariate.weighted.weighted_histogram_interactive": '''import numpy as np
import pandas as pd
from dataviz.univariate.weighted import weighted_histogram_interactive

rng = np.random.default_rng(42)
nps_score = pd.Series(rng.integers(0, 11, size=250), name="nps_score")
sample_weight = pd.Series(rng.uniform(0.5, 2.5, size=250).round(2), name="sample_weight")
fig = weighted_histogram_interactive(
    nps_score,
    sample_weight,
    bins=11,
    title="Weighted NPS Distribution",
    xlabel="NPS score",
    color="goldenrod",
    height=500,
)
fig.show()''',
    "dataviz.univariate.weighted.weighted_ecdf_values": '''import numpy as np
import pandas as pd
from dataviz.univariate.weighted import weighted_ecdf_values

rng = np.random.default_rng(42)
nps_score = pd.Series(rng.integers(0, 11, size=250), name="nps_score")
sample_weight = pd.Series(rng.uniform(0.5, 2.5, size=250).round(2), name="sample_weight")
result = weighted_ecdf_values(nps_score, sample_weight)
print(result)''',
    "dataviz.univariate.weighted.weighted_ecdf_plot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.univariate.weighted import weighted_ecdf_plot_static

rng = np.random.default_rng(42)
nps_score = pd.Series(rng.integers(0, 11, size=250), name="nps_score")
sample_weight = pd.Series(rng.uniform(0.5, 2.5, size=250).round(2), name="sample_weight")
ax = weighted_ecdf_plot_static(
    nps_score,
    sample_weight,
    title="Weighted ECDF of NPS Scores",
    color="indigo",
    theme="minimal",
)
ax.set_xlabel("NPS score")
plt.show()''',
    "dataviz.univariate.weighted.weighted_ecdf_plot_interactive": '''import numpy as np
import pandas as pd
from dataviz.univariate.weighted import weighted_ecdf_plot_interactive

rng = np.random.default_rng(42)
nps_score = pd.Series(rng.integers(0, 11, size=250), name="nps_score")
sample_weight = pd.Series(rng.uniform(0.5, 2.5, size=250).round(2), name="sample_weight")
fig = weighted_ecdf_plot_interactive(
    nps_score,
    sample_weight,
    title="Weighted ECDF of NPS Scores",
    color="indigo",
    height=500,
)
fig.show()''',
}
