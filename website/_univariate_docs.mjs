// Curated univariate documentation content: real use-case descriptions and
// complete, copy-paste code samples per chart family. Consumed by
// _generate_function_docs.mjs to replace the auto-generated boilerplate on
// univariate function pages. Image galleries come from
// assets/examples/univariate/manifest.json.
//
// Keys are chart-family base names (without the _static/_interactive suffix).
// Each entry provides:
//   useCase          - full description of when and why to use the chart.
//   setup            - shared data-preparation lines for the code sample.
//   staticCall       - call + display lines for the *_static form.
//   interactiveCall  - call + display lines for the *_interactive form.

export const UNIVARIATE_OVERRIDES = {
  histogram: {
    useCase:
      "Use the histogram as the first look at any numeric variable \u2014 a cycle time, a transaction amount, a measurement \u2014 to see its centre, spread, and shape at a glance. Binned counts make skewness, bimodality, gaps, and outliers immediately visible, which tells you whether summary statistics like the mean are trustworthy and which analyses are appropriate next.",
    setup:
      'rng = np.random.default_rng(0)\nvalues = pd.Series(rng.normal(170, 10, size=500), name="Height (cm)")',
    staticCall:
      'ax = dv.univariate.histogram_static(values, bins=30, title="Height distribution")\nplt.show()',
    interactiveCall:
      'fig = dv.univariate.histogram_interactive(values, bins=30, title="Height distribution")\nfig.show()',
  },
  density: {
    useCase:
      "Use the density plot when you want a smooth estimate of a variable\u2019s distribution instead of blocky histogram bins. The kernel density curve makes it easier to compare shape \u2014 skew, tails, and modes \u2014 without the result depending on where bin edges happen to fall, which is helpful when presenting distributions to non-technical audiences.",
    setup:
      'rng = np.random.default_rng(0)\nvalues = pd.Series(rng.normal(170, 10, size=500), name="Height (cm)")',
    staticCall:
      'ax = dv.univariate.density_static(values, title="Height density")\nplt.show()',
    interactiveCall:
      'fig = dv.univariate.density_interactive(values, title="Height density")\nfig.show()',
  },
  box_plot: {
    useCase:
      "Use the box plot to compare the distribution of a measurement across groups \u2014 production lines, stores, cohorts \u2014 in a compact form. Each box summarises the median, the middle 50% (IQR), and whiskers with outlier points, so differences in centre, spread, and extreme values between groups stand out side by side.",
    setup:
      'rng = np.random.default_rng(5)\ndata = pd.DataFrame({\n    "Line A": rng.normal(10.0, 0.5, size=100),\n    "Line B": rng.normal(10.4, 0.5, size=100),\n    "Line C": rng.normal(9.8, 0.7, size=100),\n})',
    staticCall:
      'ax = dv.univariate.box_plot_static(data, ylabel="Measurement", title="By production line")\nplt.show()',
    interactiveCall:
      'fig = dv.univariate.box_plot_interactive(data, ylabel="Measurement", title="By production line")\nfig.show()',
  },
  violin_plot: {
    useCase:
      "Use the violin plot when a box plot hides too much \u2014 for example when a group is bimodal and the box alone looks unremarkable. Each violin mirrors the full density of a group around its summary statistics, so you can compare both the shape and the centre of several distributions at once.",
    setup:
      'rng = np.random.default_rng(5)\ndata = pd.DataFrame({\n    "Line A": rng.normal(10.0, 0.5, size=100),\n    "Line B": rng.normal(10.4, 0.5, size=100),\n    "Line C": rng.normal(9.8, 0.7, size=100),\n})',
    staticCall:
      'ax = dv.univariate.violin_plot_static(data, ylabel="Measurement", title="By production line")\nplt.show()',
    interactiveCall:
      'fig = dv.univariate.violin_plot_interactive(data, ylabel="Measurement", title="By production line")\nfig.show()',
  },
  frequency_bar: {
    useCase:
      "Use the frequency bar chart to see how often each category occurs \u2014 defect types, response codes, survey answers. Categories are sorted by count so the most and least common values are obvious, making it the standard first step when exploring a categorical column.",
    setup:
      'rng = np.random.default_rng(7)\ncategories = ["Scratch", "Dent", "Misalign", "Color", "Crack", "Other"]\nprobs = np.array([0.45, 0.25, 0.12, 0.08, 0.06, 0.04])\nvalues = pd.Series(rng.choice(categories, size=400, p=probs))',
    staticCall:
      'ax = dv.univariate.frequency_bar_static(values, title="Defect frequencies")\nplt.show()',
    interactiveCall:
      'fig = dv.univariate.frequency_bar_interactive(values, title="Defect frequencies")\nfig.show()',
  },
  pareto_chart: {
    useCase:
      "Use the Pareto chart to prioritise effort by separating the vital few categories from the trivial many. Bars are sorted by frequency with a cumulative percentage line overlaid, so you can read directly which handful of causes accounts for most of the impact \u2014 the classic 80/20 view for quality and operations work.",
    setup:
      'rng = np.random.default_rng(7)\ncategories = ["Scratch", "Dent", "Misalign", "Color", "Crack", "Other"]\nprobs = np.array([0.45, 0.25, 0.12, 0.08, 0.06, 0.04])\nvalues = pd.Series(rng.choice(categories, size=400, p=probs))',
    staticCall:
      'ax = dv.univariate.pareto_chart_static(values, title="Defect Pareto")\nplt.show()',
    interactiveCall:
      'fig = dv.univariate.pareto_chart_interactive(values, title="Defect Pareto")\nfig.show()',
  },
  ecdf_plot: {
    useCase:
      "Use the empirical cumulative distribution function (ECDF) when you want every observation represented without any binning choices. Reading across from a probability gives quantiles directly \u2014 for example the value below which 90% of orders fall \u2014 and the curve\u2019s shape makes it easy to compare against a theoretical distribution.",
    setup:
      'rng = np.random.default_rng(0)\nvalues = pd.Series(rng.normal(170, 10, size=500), name="Height (cm)")',
    staticCall:
      'ax = dv.univariate.ecdf_plot_static(values, title="Height ECDF")\nplt.show()',
    interactiveCall:
      'fig = dv.univariate.ecdf_plot_interactive(values, title="Height ECDF")\nfig.show()',
  },
  cumulative_histogram: {
    useCase:
      "Use the cumulative histogram to show how counts accumulate across the range of a variable. Where the ECDF plots exact proportions, the cumulative histogram keeps the familiar binned view, which works well for communicating \u201chow many observations fall below a threshold\u201d to audiences used to ordinary histograms.",
    setup:
      'rng = np.random.default_rng(0)\nvalues = pd.Series(rng.normal(170, 10, size=500), name="Height (cm)")',
    staticCall:
      'ax = dv.univariate.cumulative_histogram_static(values, bins=30, title="Cumulative heights")\nplt.show()',
    interactiveCall:
      'fig = dv.univariate.cumulative_histogram_interactive(values, bins=30, title="Cumulative heights")\nfig.show()',
  },
  qq_plot: {
    useCase:
      "Use the quantile-quantile (Q-Q) plot to judge whether a variable follows a theoretical distribution, most often the normal. Points that fall on the reference line indicate good agreement; systematic curves reveal skewness, while S-shaped ends reveal heavier or lighter tails. It is far more sensitive to departures in the tails than a histogram.",
    setup:
      'rng = np.random.default_rng(0)\nvalues = pd.Series(rng.normal(170, 10, size=500), name="Height (cm)")',
    staticCall:
      'ax = dv.univariate.qq_plot_static(values, distribution="norm")\nplt.show()',
    interactiveCall:
      'fig = dv.univariate.qq_plot_interactive(values, distribution="norm")\nfig.show()',
  },
  pp_plot: {
    useCase:
      "Use the probability-probability (P-P) plot as the CDF-level companion to the Q-Q plot when assessing fit to a theoretical distribution. Because it compares cumulative probabilities rather than quantiles, it emphasises agreement in the centre of the distribution, which is where the Q-Q plot is least sensitive.",
    setup:
      'rng = np.random.default_rng(0)\nvalues = pd.Series(rng.normal(170, 10, size=500), name="Height (cm)")',
    staticCall:
      'ax = dv.univariate.pp_plot_static(values, distribution="norm")\nplt.show()',
    interactiveCall:
      'fig = dv.univariate.pp_plot_interactive(values, distribution="norm")\nfig.show()',
  },
  outlier_plot: {
    useCase:
      "Use the outlier plot to flag unusual observations before they distort averages, models, or control limits. Points are coloured by whether they breach an IQR-fence or z-score rule, so you can see at a glance how many outliers exist, where they sit, and whether they are isolated events or a systematic cluster.",
    setup:
      'rng = np.random.default_rng(9)\nvalues = pd.Series(rng.normal(10.0, 0.5, size=200), name="Value")\nvalues.iloc[[25, 90, 150]] += [3.0, -2.8, 3.4]',
    staticCall:
      'ax = dv.univariate.outlier_plot_static(values, method="iqr")\nplt.show()',
    interactiveCall:
      'fig = dv.univariate.outlier_plot_interactive(values, method="iqr")\nfig.show()',
  },
  percentile_plot: {
    useCase:
      "Use the percentile plot to read quantiles directly \u2014 the value at the 50th, 90th, or 99th percentile \u2014 without fitting any distribution. It is the natural display for service-level questions such as \u201cwhat response time do 95% of requests beat?\u201d and for spotting where the distribution stretches.",
    setup:
      'rng = np.random.default_rng(0)\nvalues = pd.Series(rng.normal(170, 10, size=500), name="Height (cm)")',
    staticCall:
      'ax = dv.univariate.percentile_plot_static(values, step=5)\nplt.show()',
    interactiveCall:
      'fig = dv.univariate.percentile_plot_interactive(values, step=5)\nfig.show()',
  },
  univariate_diagnostic_panel: {
    useCase:
      "Use the diagnostic panel to run the standard battery of univariate checks in one figure \u2014 distribution shape, box-plot summary, and normality assessment side by side. It is ideal for exploratory reports where a single composite view answers \u201cwhat does this variable look like?\u201d without assembling separate charts by hand.",
    setup:
      'rng = np.random.default_rng(0)\nvalues = pd.Series(rng.normal(170, 10, size=500), name="Height (cm)")',
    staticCall:
      'fig = dv.univariate.univariate_diagnostic_panel_static(values)\nplt.show()',
    interactiveCall:
      'fig = dv.univariate.univariate_diagnostic_panel_interactive(values)\nfig.show()',
  },
  fitted_distribution_histogram: {
    useCase:
      "Use the fitted distribution histogram to check how well a named probability distribution describes your data. Overlaying the fitted curve on the histogram turns an abstract fit into a visual judgement \u2014 you can see immediately whether the model captures the centre, the tails, and any skew before relying on it for simulation or probability calculations.",
    setup:
      'rng = np.random.default_rng(0)\nvalues = pd.Series(rng.normal(170, 10, size=500), name="Height (cm)")',
    staticCall:
      'ax = dv.univariate.fitted_distribution_histogram_static(values, distribution="norm")\nplt.show()',
    interactiveCall:
      'fig = dv.univariate.fitted_distribution_histogram_interactive(values, distribution="norm")\nfig.show()',
  },
  robust_location_plot: {
    useCase:
      "Use the robust location plot to see how much your estimate of \u201ctypical value\u201d depends on extreme observations. It compares the ordinary mean against the median, trimmed mean, and winsorised mean on the raw data, so when the estimates disagree you know the mean is being pulled by outliers or skew and a robust alternative is safer to report.",
    setup:
      'rng = np.random.default_rng(11)\nvalues = pd.Series(rng.normal(10.0, 0.5, size=200), name="Value")\nvalues.iloc[:5] += 6.0  # a few extreme values',
    staticCall:
      'ax = dv.univariate.robust_location_plot_static(values)\nplt.show()',
    interactiveCall:
      'fig = dv.univariate.robust_location_plot_interactive(values)\nfig.show()',
  },
  rug_plot: {
    useCase:
      "Use the rug plot to show the exact position of every observation as tick marks along the axis. It adds the raw data footprint to distribution summaries \u2014 revealing clusters, gaps, and isolated points that smoothing can hide \u2014 and works well as a minimal standalone view for small samples.",
    setup:
      'rng = np.random.default_rng(21)\nvalues = pd.Series(rng.normal(170, 10, size=80), name="Height (cm)")',
    staticCall:
      'ax = dv.univariate.rug_plot_static(values, title="Observed heights")\nplt.show()',
    interactiveCall:
      'fig = dv.univariate.rug_plot_interactive(values, title="Observed heights")\nfig.show()',
  },
  strip_plot: {
    useCase:
      "Use the strip plot to display every observation of a single variable as a jittered one-dimensional scatter. Unlike a histogram it loses nothing to binning, so cluster structure, gaps, and exact outlier positions remain visible \u2014 most useful for small to medium samples where individual points matter.",
    setup:
      'rng = np.random.default_rng(21)\nvalues = pd.Series(rng.normal(170, 10, size=80), name="Height (cm)")',
    staticCall:
      'ax = dv.univariate.strip_plot_static(values, ylabel="Height (cm)")\nplt.show()',
    interactiveCall:
      'fig = dv.univariate.strip_plot_interactive(values, ylabel="Height (cm)")\nfig.show()',
  },
  dot_plot: {
    useCase:
      "Use the Cleveland dot plot for category counts when bar charts feel heavy or category names are long. A dot on a common scale is easier to compare than bar lengths, and the horizontal layout keeps labels readable, making it a clean choice for ranked frequency displays in reports.",
    setup:
      'rng = np.random.default_rng(7)\ncategories = ["Scratch", "Dent", "Misalign", "Color", "Crack", "Other"]\nprobs = np.array([0.45, 0.25, 0.12, 0.08, 0.06, 0.04])\nvalues = pd.Series(rng.choice(categories, size=400, p=probs))',
    staticCall:
      'ax = dv.univariate.dot_plot_static(values, title="Defect counts")\nplt.show()',
    interactiveCall:
      'fig = dv.univariate.dot_plot_interactive(values, title="Defect counts")\nfig.show()',
  },
  lollipop_chart: {
    useCase:
      "Use the lollipop chart as a lighter alternative to bars for category frequencies. A thin stem with a marker at the count reduces ink while preserving an accurate position judgement, which keeps ranked categorical summaries readable when there are many categories.",
    setup:
      'rng = np.random.default_rng(7)\ncategories = ["Scratch", "Dent", "Misalign", "Color", "Crack", "Other"]\nprobs = np.array([0.45, 0.25, 0.12, 0.08, 0.06, 0.04])\nvalues = pd.Series(rng.choice(categories, size=400, p=probs))',
    staticCall:
      'ax = dv.univariate.lollipop_chart_static(values, title="Defect counts")\nplt.show()',
    interactiveCall:
      'fig = dv.univariate.lollipop_chart_interactive(values, title="Defect counts")\nfig.show()',
  },
  reference_band_histogram: {
    useCase:
      "Use the reference band histogram when the question is not just \u201cwhat is the shape?\u201d but \u201chow much of the data sits in the normal range?\u201d. A shaded central band around the mean with the histogram overlaid makes it immediate to see what fraction of observations fall inside versus outside typical variation.",
    setup:
      'rng = np.random.default_rng(0)\nvalues = pd.Series(rng.normal(170, 10, size=500), name="Height (cm)")',
    staticCall:
      'ax = dv.univariate.reference_band_histogram_static(values, bins=30)\nplt.show()',
    interactiveCall:
      'fig = dv.univariate.reference_band_histogram_interactive(values, bins=30)\nfig.show()',
  },
  raincloud_plot: {
    useCase:
      "Use the raincloud plot to show a distribution honestly at three levels at once: the smooth density (cloud), the box-plot summary, and every raw observation (rain). It avoids the opacity of a lone box plot and the redundancy of a mirrored violin, which makes it a strong default for reporting a single sample.",
    setup:
      'rng = np.random.default_rng(21)\nvalues = pd.Series(rng.normal(170, 10, size=120), name="Height (cm)")',
    staticCall:
      'ax = dv.univariate.raincloud_plot_static(values, ylabel="Height (cm)")\nplt.show()',
    interactiveCall:
      'fig = dv.univariate.raincloud_plot_interactive(values, ylabel="Height (cm)")\nfig.show()',
  },
  ridgeline_plot: {
    useCase:
      "Use the ridgeline plot to compare how a distribution evolves across ordered groups \u2014 weeks, batches, age bands. Stacking partially overlapping density curves vertically makes gradual shifts in centre, widening spread, or emerging skew easy to follow in a way that side-by-side violins cannot.",
    setup:
      'rng = np.random.default_rng(13)\ndata = pd.DataFrame({\n    "Week 1": rng.normal(10.0, 0.5, size=120),\n    "Week 2": rng.normal(10.3, 0.5, size=120),\n    "Week 3": rng.normal(10.6, 0.5, size=120),\n    "Week 4": rng.normal(10.9, 0.5, size=120),\n})',
    staticCall:
      'ax = dv.univariate.ridgeline_plot_static(data, xlabel="Measurement")\nplt.show()',
    interactiveCall:
      'fig = dv.univariate.ridgeline_plot_interactive(data, xlabel="Measurement")\nfig.show()',
  },
  transformation_comparison: {
    useCase:
      "Use the transformation comparison to decide whether a log, square-root, or similar transform tames a skewed variable before modelling. Plotting the original and transformed distributions side by side shows which transform best symmetrises the data, replacing guesswork with a direct visual check.",
    setup:
      'rng = np.random.default_rng(29)\nvalues = pd.Series(rng.lognormal(0.0, 0.8, size=500), name="Value")',
    staticCall:
      'fig = dv.univariate.transformation_comparison_static(values)\nplt.show()',
    interactiveCall:
      'fig = dv.univariate.transformation_comparison_interactive(values)\nfig.show()',
  },
  event_frequency_plot: {
    useCase:
      "Use the event frequency plot to see how a stream of timestamped events \u2014 orders, failures, signups \u2014 is distributed over time. Resampling raw event times into daily, weekly, or monthly counts reveals surges, quiet periods, and growth trends that a list of timestamps cannot show.",
    setup:
      'rng = np.random.default_rng(15)\ngaps = rng.exponential(12.0, size=300)  # hours between events\ntimes = pd.Series(pd.Timestamp("2024-01-01") + pd.to_timedelta(gaps.cumsum(), unit="h"))',
    staticCall:
      'ax = dv.univariate.event_frequency_plot_static(times, freq="W")\nplt.show()',
    interactiveCall:
      'fig = dv.univariate.event_frequency_plot_interactive(times, freq="W")\nfig.show()',
  },
  interarrival_plot: {
    useCase:
      "Use the interarrival plot to examine the waiting times between consecutive events. The histogram of gaps distinguishes a steady Poisson-like process (exponential shape) from bursty or clockwork-regular arrivals, which determines whether queueing assumptions and rate-based forecasts are valid.",
    setup:
      'rng = np.random.default_rng(15)\ngaps = rng.exponential(12.0, size=300)  # hours between events\ntimes = pd.Series(pd.Timestamp("2024-01-01") + pd.to_timedelta(gaps.cumsum(), unit="h"))',
    staticCall:
      'ax = dv.univariate.interarrival_plot_static(times, unit="D")\nplt.show()',
    interactiveCall:
      'fig = dv.univariate.interarrival_plot_interactive(times, unit="D")\nfig.show()',
  },
  univariate_analysis_dashboard: {
    useCase:
      "Use the univariate analysis dashboard to profile a variable in one composite figure \u2014 distribution, cumulative view, summary statistics, and normality checks together. It is built for reports and handoffs where a single self-contained picture of a variable\u2019s behaviour is more useful than a folder of separate charts.",
    setup:
      'rng = np.random.default_rng(0)\nvalues = pd.Series(rng.normal(170, 10, size=500), name="Height (cm)")',
    staticCall:
      'fig = dv.univariate.univariate_analysis_dashboard_static(values)\nplt.show()',
    interactiveCall:
      'fig = dv.univariate.univariate_analysis_dashboard_interactive(values)\nfig.show()',
  },
  weighted_histogram: {
    useCase:
      "Use the weighted histogram when observations do not count equally \u2014 survey respondents with sampling weights, transactions weighted by amount, or records reweighted to match a population. Weighting each observation changes the apparent shape of the distribution, and this chart makes the corrected view visible instead of letting an unweighted histogram mislead.",
    setup:
      'rng = np.random.default_rng(17)\nvalues = pd.Series(rng.normal(50.0, 10.0, size=500), name="Score")\nweights = pd.Series(np.where(values > 55, 3.0, 1.0))',
    staticCall:
      'ax = dv.univariate.weighted_histogram_static(values, weights, bins=30)\nplt.show()',
    interactiveCall:
      'fig = dv.univariate.weighted_histogram_interactive(values, weights, bins=30)\nfig.show()',
  },
  quality_bar: {
    useCase:
      "Use the quality bar chart for a fast data-quality audit of a single column. It reports the missing, duplicate, zero, and negative rates as bars on a common 0\u20131 scale, so the problems that need cleaning \u2014 and their relative size \u2014 are visible before any analysis begins.",
    setup:
      'rng = np.random.default_rng(19)\nvalues = pd.Series(rng.normal(10.0, 1.0, size=300))\nvalues.iloc[:10] = np.nan\nvalues.iloc[10:20] = 0.0',
    staticCall:
      'ax = dv.univariate.quality_bar_static(values, title="Column quality")\nplt.show()',
    interactiveCall:
      'fig = dv.univariate.quality_bar_interactive(values, title="Column quality")\nfig.show()',
  },
  survival_curve: {
    useCase:
      "Use the empirical survival curve to show the probability that a duration \u2014 time to failure, customer lifetime, days to delivery \u2014 exceeds any given value. Reading the curve at a point answers \u201cwhat fraction survives past day 90?\u201d without assuming any parametric lifetime distribution.",
    setup:
      'rng = np.random.default_rng(31)\ntimes = pd.Series(rng.weibull(2.0, size=400) * 365, name="Days to failure")',
    staticCall:
      'ax = dv.univariate.survival_curve_static(times, title="Survival curve")\nplt.show()',
    interactiveCall:
      'fig = dv.univariate.survival_curve_interactive(times, title="Survival curve")\nfig.show()',
  },
  lorenz_curve: {
    useCase:
      "Use the Lorenz curve to quantify inequality or concentration \u2014 income across households, revenue across customers, defects across part numbers. Plotting the cumulative share of the total against the cumulative share of the population, with the equality line as reference, shows at a glance how far from even the distribution is; the area between the curves is half the Gini coefficient.",
    setup:
      'rng = np.random.default_rng(35)\nincomes = pd.Series(rng.lognormal(10.5, 0.6, size=1000), name="Income")',
    staticCall:
      'ax = dv.univariate.lorenz_curve_static(incomes, title="Income concentration")\nplt.show()',
    interactiveCall:
      'fig = dv.univariate.lorenz_curve_interactive(incomes, title="Income concentration")\nfig.show()',
  },
  bootstrap_distribution_plot: {
    useCase:
      "Use the bootstrap distribution plot to see the sampling variability of a statistic \u2014 mean, median, or standard deviation \u2014 without any distributional formula. Resampling the data with replacement builds the statistic\u2019s distribution empirically, so the histogram shows its uncertainty and skew directly, which is the honest basis for confidence intervals on small or non-normal samples.",
    setup:
      'rng = np.random.default_rng(0)\nvalues = pd.Series(rng.normal(170, 10, size=200), name="Height (cm)")',
    staticCall:
      'ax = dv.univariate.bootstrap_distribution_plot_static(values, statistic="mean", n_resamples=1000, seed=0)\nplt.show()',
    interactiveCall:
      'fig = dv.univariate.bootstrap_distribution_plot_interactive(values, statistic="mean", n_resamples=1000, seed=0)\nfig.show()',
  },
  boolean_bar: {
    useCase:
      "Use the boolean bar chart to show the split of a true/false flag \u2014 passed vs. failed, active vs. churned, fraud vs. legitimate. The two bars make class balance (or imbalance) immediately visible, which is a critical check before training classifiers or reporting conversion rates.",
    setup:
      'rng = np.random.default_rng(37)\nflags = pd.Series(rng.random(300) < 0.3)',
    staticCall:
      'ax = dv.univariate.boolean_bar_static(flags, title="Pass / fail split")\nplt.show()',
    interactiveCall:
      'fig = dv.univariate.boolean_bar_interactive(flags, title="Pass / fail split")\nfig.show()',
  },
  top_terms_bar: {
    useCase:
      "Use the top terms bar chart to profile a free-text column \u2014 review comments, ticket subjects, search queries \u2014 by its most frequent terms. Ranking the commonest words surfaces dominant themes and data-entry artefacts quickly, which guides both cleaning and downstream text analysis.",
    setup:
      'rng = np.random.default_rng(23)\nterms = ["delivery", "quality", "price", "support", "packaging", "refund", "shipping"]\nprobs = np.array([0.30, 0.22, 0.16, 0.12, 0.09, 0.06, 0.05])\nwords = pd.Series(rng.choice(terms, size=500, p=probs))',
    staticCall:
      'ax = dv.univariate.top_terms_bar_static(words, top_n=10)\nplt.show()',
    interactiveCall:
      'fig = dv.univariate.top_terms_bar_interactive(words, top_n=10)\nfig.show()',
  },
  weighted_ecdf_plot: {
    useCase:
      "Use the weighted ECDF when quantiles must reflect per-observation importance rather than raw counts \u2014 for example population percentiles from a survey with sampling weights. Each observation contributes its weight to the cumulative curve, so the quantiles you read off represent the reweighted population, not just the sample you happened to collect.",
    setup:
      'rng = np.random.default_rng(17)\nvalues = pd.Series(rng.normal(50.0, 10.0, size=500), name="Score")\nweights = pd.Series(np.where(values > 55, 3.0, 1.0))',
    staticCall:
      'ax = dv.univariate.weighted_ecdf_plot_static(values, weights)\nplt.show()',
    interactiveCall:
      'fig = dv.univariate.weighted_ecdf_plot_interactive(values, weights)\nfig.show()',
  },
  ordinal_bar: {
    useCase:
      "Use the ordinal bar chart for categories with a natural order \u2014 Likert ratings, severity levels, education bands. Supplying the explicit order keeps the bars in logical sequence instead of alphabetical, so shifts toward the positive or negative end of the scale read correctly.",
    setup:
      'rng = np.random.default_rng(25)\nscale = ["Poor", "Fair", "Good", "Very good", "Excellent"]\nprobs = np.array([0.05, 0.15, 0.35, 0.30, 0.15])\nratings = pd.Series(rng.choice(scale, size=400, p=probs))',
    staticCall:
      'ax = dv.univariate.ordinal_bar_static(ratings, order=scale, title="Satisfaction ratings")\nplt.show()',
    interactiveCall:
      'fig = dv.univariate.ordinal_bar_interactive(ratings, order=scale, title="Satisfaction ratings")\nfig.show()',
  },
  outlier_treatment_comparison: {
    useCase:
      "Use the outlier treatment comparison to see the effect of capping or removing outliers before committing to a cleaning rule. Showing the distribution before and after treatment makes the trade-off visible \u2014 how much of the tail was genuine signal versus noise \u2014 so the choice of rule is a reviewed decision, not an invisible preprocessing step.",
    setup:
      'rng = np.random.default_rng(27)\nvalues = pd.Series(rng.normal(10.0, 0.5, size=300), name="Value")\nvalues.iloc[[10, 120, 250]] += [4.0, -3.5, 4.5]',
    staticCall:
      'ax = dv.univariate.outlier_treatment_comparison_static(values, rule="iqr", treatment="cap")\nplt.show()',
    interactiveCall:
      'fig = dv.univariate.outlier_treatment_comparison_interactive(values, rule="iqr", treatment="cap")\nfig.show()',
  },
};
