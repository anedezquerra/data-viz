// Curated SPC documentation content: real use-case descriptions and complete,
// copy-paste code samples per chart family. Consumed by
// _generate_function_docs.mjs to replace the auto-generated boilerplate on SPC
// function pages. Image galleries come from assets/examples/spc/manifest.json.
//
// Keys are chart-family base names (without the _static/_interactive suffix).
// Each entry provides:
//   useCase          - full description of when and why to use the chart.
//   setup            - shared data-preparation lines for the code sample.
//   staticCall       - call + display lines for the *_static form.
//   interactiveCall  - call + display lines for the *_interactive form.

export const SPC_OVERRIDES = {
  control_chart: {
    useCase:
      "Use the individuals (I) control chart when you measure one value per time period \u2014 a machined diameter, a batch yield, a daily cycle time \u2014 and want to know whether the process is stable or whether a point signals a special cause. Control limits are computed from the data at \u00b13\u03c3 (estimated from the average moving range), so points outside the limits or non-random patterns flag investigation-worthy events rather than normal variation.",
    setup:
      'rng = np.random.default_rng(0)\nvalues = pd.Series(rng.normal(10.0, 0.5, size=40), name="Diameter (mm)")',
    staticCall:
      'ax = dv.spc.control_chart_static(values, title="Individuals control chart")\nplt.show()',
    interactiveCall:
      'fig = dv.spc.control_chart_interactive(values, title="Individuals control chart")\nfig.show()',
  },
  x_range_chart: {
    useCase:
      "Use the X\u0304/R chart when measurements arrive in rational subgroups (for example five parts sampled each hour). It tracks the subgroup mean to detect shifts in the process centre and the subgroup range to detect changes in within-subgroup spread, giving an early, sensitive view of process stability for continuous data.",
    setup:
      'rng = np.random.default_rng(20)\n# 30 subgroups of five measurements flattened into one series\nvalues = pd.Series(rng.normal(10.0, 0.5, size=150), name="Value")',
    staticCall:
      'ax = dv.spc.x_range_chart_static(values, subgroup_size=5)\nplt.show()',
    interactiveCall:
      'fig = dv.spc.x_range_chart_interactive(values, subgroup_size=5)\nfig.show()',
  },
  moving_range_chart: {
    useCase:
      "Use the moving range (MR) chart alongside an individuals chart to monitor short-term, point-to-point variation when only one measurement is available per period. Each plotted value is the absolute difference between consecutive observations; an out-of-control moving range warns that the process spread \u2014 not just its centre \u2014 has changed.",
    setup:
      'rng = np.random.default_rng(0)\nvalues = pd.Series(rng.normal(10.0, 0.5, size=40), name="Value")',
    staticCall:
      'ax = dv.spc.moving_range_chart_static(values, span=2)\nplt.show()',
    interactiveCall:
      'fig = dv.spc.moving_range_chart_interactive(values, span=2)\nfig.show()',
  },
  xbar_r_chart: {
    useCase:
      "Use the X\u0304-R chart pair for small rational subgroups (roughly two to nine units each). The X\u0304 chart monitors the process average while the R chart monitors within-subgroup range; reading them together separates shifts in centring from changes in variation. The R chart should be assessed first because the X\u0304 limits depend on a stable range.",
    setup:
      'rng = np.random.default_rng(10)\n# 25 subgroups of five measurements arranged as rows\ndata = rng.normal(10.0, 0.5, size=(25, 5))',
    staticCall:
      'ax_mean, ax_range = dv.spc.xbar_r_chart_static(data)\nplt.show()',
    interactiveCall:
      'fig = dv.spc.xbar_r_chart_interactive(data)\nfig.show()',
  },
  xbar_s_chart: {
    useCase:
      "Use the X\u0304-S chart pair instead of X\u0304-R when subgroups are larger (about ten units or more), where the sample standard deviation estimates within-subgroup variation more efficiently than the range. The X\u0304 chart tracks the mean and the S chart tracks the standard deviation, so together they reveal both centring shifts and dispersion changes.",
    setup:
      'rng = np.random.default_rng(14)\n# 25 subgroups of eight measurements arranged as rows\ndata = rng.normal(10.0, 0.5, size=(25, 8))',
    staticCall:
      'ax_mean, ax_std = dv.spc.xbar_s_chart_static(data)\nplt.show()',
    interactiveCall:
      'fig = dv.spc.xbar_s_chart_interactive(data)\nfig.show()',
  },
  ewma_chart: {
    useCase:
      "Use the exponentially weighted moving average (EWMA) chart to detect small, sustained shifts in the process mean that an individuals chart would miss. Each point is a weighted average of the current and all prior observations (controlled by \u03bb), which smooths noise and makes gradual drifts easier to catch. Smaller \u03bb values give more memory and greater sensitivity to tiny shifts.",
    setup:
      'rng = np.random.default_rng(2)\nvalues = pd.Series(rng.normal(10.0, 0.5, size=40), name="Value")',
    staticCall:
      'ax = dv.spc.ewma_chart_static(values, lambda_=0.2)\nplt.show()',
    interactiveCall:
      'fig = dv.spc.ewma_chart_interactive(values, lambda_=0.2)\nfig.show()',
  },
  cusum_chart: {
    useCase:
      "Use the cumulative sum (CUSUM) chart to detect small, persistent deviations from a target value as quickly as possible. It accumulates the signed differences from target, so even a modest sustained shift produces a steep, unmistakable slope. Provide the target and tune the slack (k) and decision interval (h) to trade off sensitivity against false alarms.",
    setup:
      'rng = np.random.default_rng(3)\nvalues = pd.Series(rng.normal(10.0, 0.5, size=40), name="Value")',
    staticCall:
      'ax = dv.spc.cusum_chart_static(values, target=10.0, k=0.5, h=5.0)\nplt.show()',
    interactiveCall:
      'fig = dv.spc.cusum_chart_interactive(values, target=10.0, k=0.5, h=5.0)\nfig.show()',
  },
  p_chart: {
    useCase:
      "Use the p chart to monitor the proportion of nonconforming units when sample sizes vary from period to period (for example the fraction of defective items in daily production lots of differing size). Control limits adjust for each sample size, widening for small samples and tightening for large ones, so shifts in the underlying defect rate stand out.",
    setup:
      'rng = np.random.default_rng(33)\nsample_sizes = pd.Series(rng.integers(80, 140, size=20))\ndefectives = pd.Series(\n    [rng.binomial(int(n), 0.05) for n in sample_sizes]\n)',
    staticCall:
      'ax = dv.spc.p_chart_static(defectives, sample_sizes)\nplt.show()',
    interactiveCall:
      'fig = dv.spc.p_chart_interactive(defectives, sample_sizes)\nfig.show()',
  },
  np_chart: {
    useCase:
      "Use the np chart to monitor the count of nonconforming units when the sample size is constant. It plots the raw number of defectives per sample against limits derived from the binomial distribution, making it the most direct display when every inspection lot is the same size.",
    setup:
      'rng = np.random.default_rng(40)\nsample_size = 100\ndefectives = pd.Series(rng.binomial(sample_size, 0.04, size=20))',
    staticCall:
      'ax = dv.spc.np_chart_static(defectives, sample_size)\nplt.show()',
    interactiveCall:
      'fig = dv.spc.np_chart_interactive(defectives, sample_size)\nfig.show()',
  },
  c_chart: {
    useCase:
      "Use the c chart to monitor the count of defects per inspection unit when the inspection area or opportunity size is constant (for example the number of surface flaws per fixed-size panel). Limits are based on the Poisson distribution, so an unusually high or low defect count signals a change in the process.",
    setup:
      'rng = np.random.default_rng(50)\ndefects = pd.Series(rng.poisson(4.0, size=25))',
    staticCall:
      'ax = dv.spc.c_chart_static(defects)\nplt.show()',
    interactiveCall:
      'fig = dv.spc.c_chart_interactive(defects)\nfig.show()',
  },
  u_chart: {
    useCase:
      "Use the u chart to monitor defects per unit when the inspection size varies between samples (for example defects per square metre of fabric across rolls of different length). It normalises the defect count by the number of units inspected and adjusts the control limits for each sample size, so the defect rate is comparable across unequal samples.",
    setup:
      'rng = np.random.default_rng(60)\nunits = pd.Series(rng.integers(40, 60, size=20))\ndefects = pd.Series([rng.poisson(0.1 * u) for u in units])',
    staticCall:
      'ax = dv.spc.u_chart_static(defects, units)\nplt.show()',
    interactiveCall:
      'fig = dv.spc.u_chart_interactive(defects, units)\nfig.show()',
  },
  capability_histogram: {
    useCase:
      "Use the process capability histogram to compare the natural spread of a process against its specification limits. Overlaying the distribution with the lower and upper specification limits shows visually whether the process is centred and capable, and the accompanying capability indices (Cp, Cpk) quantify how much margin exists before parts fall out of spec.",
    setup:
      'rng = np.random.default_rng(100)\nvalues = pd.Series(rng.normal(10.0, 0.4, size=300), name="Value")',
    staticCall:
      'ax = dv.spc.capability_histogram_static(values, lsl=8.5, usl=11.5)\nplt.show()',
    interactiveCall:
      'fig = dv.spc.capability_histogram_interactive(values, lsl=8.5, usl=11.5)\nfig.show()',
  },
  run_chart: {
    useCase:
      "Use the run chart as a simple first look at how a measurement behaves over time before committing to full control limits. Plotting the series against its median makes trends, cycles, and shifts easy to spot with run-based tests, and it needs no assumptions about the distribution \u2014 ideal for early exploration or non-technical audiences.",
    setup:
      'rng = np.random.default_rng(0)\nvalues = pd.Series(rng.normal(10.0, 0.5, size=40), name="Value")',
    staticCall:
      'ax = dv.spc.run_chart_static(values, show_median=True)\nplt.show()',
    interactiveCall:
      'fig = dv.spc.run_chart_interactive(values, show_median=True)\nfig.show()',
  },
  rule_violation_chart: {
    useCase:
      "Use the rule violation chart to run the Western Electric / Nelson pattern rules automatically and highlight the exact points that break them. Beyond the basic \u201coutside \u00b13\u03c3\u201d test, it flags runs, trends, and zone patterns that indicate a process is no longer in statistical control, so reviewers can focus on the specific signals that need action.",
    setup:
      'rng = np.random.default_rng(1)\nvalues = pd.Series(rng.normal(10.0, 0.5, size=40), name="Value")\nvalues[20:] += 1.2  # introduce a shift to trigger rules',
    staticCall:
      'ax = dv.spc.rule_violation_chart_static(values)\nplt.show()',
    interactiveCall:
      'fig = dv.spc.rule_violation_chart_interactive(values)\nfig.show()',
  },
  pareto_chart: {
    useCase:
      "Use the Pareto chart to prioritise improvement effort by separating the \u201cvital few\u201d causes from the \u201ctrivial many\u201d. Sorting defect categories by frequency and overlaying the cumulative percentage line makes it immediately clear which handful of problems accounts for most of the impact, guiding where to focus root-cause work.",
    setup:
      'categories = ["Scratch", "Dent", "Misalign", "Color", "Crack", "Other"]\ncounts = [140, 90, 40, 20, 8, 4]',
    staticCall:
      'ax = dv.spc.pareto_chart_static(categories, counts)\nplt.show()',
    interactiveCall:
      'fig = dv.spc.pareto_chart_interactive(categories, counts)\nfig.show()',
  },
  process_distribution: {
    useCase:
      "Use the process distribution plot to inspect the shape of a measurement before applying control charts or capability analysis. Revealing skewness, bimodality, or heavy tails helps you check the normality assumption, spot mixed process streams, and choose the right analysis rather than trusting summary statistics alone.",
    setup:
      'rng = np.random.default_rng(110)\nvalues = pd.Series(rng.normal(10.0, 0.6, size=400), name="Value")',
    staticCall:
      'ax = dv.spc.process_distribution_static(values, bins=30)\nplt.show()',
    interactiveCall:
      'fig = dv.spc.process_distribution_interactive(values, bins=30)\nfig.show()',
  },
  zone_chart: {
    useCase:
      "Use the zone chart to make the Western Electric zone tests visible by dividing the region around the centre line into A, B, and C bands (one, two, and three sigma). Colour-coded zones make patterns such as \u201ctwo of three points in zone A\u201d easy to read directly off the chart, which is helpful for training operators to recognise out-of-control signals.",
    setup:
      'rng = np.random.default_rng(0)\nvalues = pd.Series(rng.normal(10.0, 0.5, size=40), name="Value")',
    staticCall:
      'ax = dv.spc.zone_chart_static(values)\nplt.show()',
    interactiveCall:
      'fig = dv.spc.zone_chart_interactive(values)\nfig.show()',
  },
  hotelling_t2_chart: {
    useCase:
      "Use the Hotelling T\u00b2 chart to monitor several correlated variables at once instead of running separate charts that ignore their relationships. The T\u00b2 statistic collapses the multivariate deviation into a single distance, so it flags points that are unusual jointly \u2014 including cases where each variable looks acceptable on its own but their combination does not.",
    setup:
      'rng = np.random.default_rng(120)\nx1 = rng.normal(10.0, 0.5, size=40)\nx2 = 0.6 * (x1 - 10.0) + rng.normal(20.0, 0.5, size=40)\ndata = pd.DataFrame({"x1": x1, "x2": x2})',
    staticCall:
      'ax = dv.spc.hotelling_t2_chart_static(data, limit_quantile=0.99)\nplt.show()',
    interactiveCall:
      'fig = dv.spc.hotelling_t2_chart_interactive(data, limit_quantile=0.99)\nfig.show()',
  },
  spc_dashboard: {
    useCase:
      "Use the SPC dashboard to review a process at a glance by combining the individuals chart, moving range chart, and distribution views in a single figure. It is well suited to reports and status reviews where one composite picture of stability, spread, and shape is more useful than a set of separate charts.",
    setup:
      'rng = np.random.default_rng(0)\nvalues = pd.Series(rng.normal(10.0, 0.5, size=40), name="Value")',
    staticCall:
      'fig = dv.spc.spc_dashboard_static(values)\nplt.show()',
    interactiveCall:
      'fig = dv.spc.spc_dashboard_interactive(values)\nfig.show()',
  },
};
