// Curated bivariate documentation content: real use-case descriptions and
// complete, copy-paste code samples per chart family. Consumed by
// _generate_function_docs.mjs to replace the auto-generated boilerplate on
// bivariate function pages. Image galleries come from
// assets/examples/bivariate/manifest.json.
//
// Keys are chart-family base names (without the _static/_interactive suffix).
// Each entry provides:
//   useCase          - full description of when and why to use the chart.
//   setup            - shared data-preparation lines for the code sample.
//   staticCall       - call + display lines for the *_static form.
//   interactiveCall  - call + display lines for the *_interactive form.

export const BIVARIATE_OVERRIDES = {
  scatter_plot: {
    useCase:
      "Use a scatter plot as the first look at any pairwise relationship \u2014 cycle time versus temperature, price versus demand \u2014 to judge direction, strength, and shape before modelling. Point clouds reveal correlation, clusters, curvature, and outliers that summary statistics hide, and optional fitted lines or correlation annotations quantify what the eye sees.",
    setup:
      'rng = np.random.default_rng(0)\nx = pd.Series(rng.normal(50, 10, 200), name="Temperature")\ny = pd.Series(2.5 * x + rng.normal(0, 15, 200), name="Cycle time")',
    staticCall:
      'ax = dv.bivariate.scatter_plot_static(x, y, show_corr=True)\nplt.show()',
    interactiveCall:
      'fig = dv.bivariate.scatter_plot_interactive(x, y, show_corr=True)\nfig.show()',
  },
  line_plot: {
    useCase:
      "Use a line plot when observations have a natural order \u2014 time, sequence, dose \u2014 and you want to trace how a value evolves along it. Connecting the points emphasises trends, cycles, and abrupt changes, and the optional rolling average overlay separates the underlying movement from point-to-point noise.",
    setup:
      'rng = np.random.default_rng(1)\nx = pd.Series(np.arange(60), name="Day")\ny = pd.Series(\n    100 + np.arange(60) * 0.4 + rng.normal(0, 3, 60), name="Throughput"\n)',
    staticCall:
      'ax = dv.bivariate.line_plot_static(x, y, rolling_window=7)\nplt.show()',
    interactiveCall:
      'fig = dv.bivariate.line_plot_interactive(x, y, rolling_window=7)\nfig.show()',
  },
  correlation_heatmap: {
    useCase:
      "Use the correlation heatmap to screen many numeric variables at once before modelling or root-cause work. Colour-coding the full pairwise correlation matrix makes strong linear relationships, redundant variables, and unexpected sign patterns visible in one glance, and Pearson, Kendall, or Spearman methods cover both linear and monotonic association.",
    setup:
      'rng = np.random.default_rng(2)\na = rng.normal(0, 1, 200)\ndf = pd.DataFrame({\n    "a": a,\n    "b": 0.8 * a + rng.normal(0, 0.5, 200),\n    "c": rng.normal(0, 1, 200),\n    "d": -0.6 * a + rng.normal(0, 0.7, 200),\n})',
    staticCall:
      'ax = dv.bivariate.correlation_heatmap_static(df)\nplt.show()',
    interactiveCall:
      'fig = dv.bivariate.correlation_heatmap_interactive(df)\nfig.show()',
  },
  bubble_plot: {
    useCase:
      "Use a bubble plot when a third (and optionally fourth) variable matters alongside the two positional axes \u2014 for example revenue versus margin with bubble size for volume and colour for growth. Encoding extra dimensions in size and colour lets one chart carry the information of several scatter plots while staying readable.",
    setup:
      'rng = np.random.default_rng(3)\nx = rng.normal(50, 12, 60)\ny = 0.7 * x + rng.normal(0, 8, 60)\nsize = rng.uniform(50, 500, 60)\ncolor = rng.uniform(0, 1, 60)',
    staticCall:
      'ax = dv.bivariate.bubble_plot_static(x, y, size, color)\nplt.show()',
    interactiveCall:
      'fig = dv.bivariate.bubble_plot_interactive(x, y, size, color)\nfig.show()',
  },
  hexbin_plot: {
    useCase:
      "Use a hexbin plot instead of a scatter plot when thousands of points overlap into an unreadable blob. Binning the plane into hexagons and colouring by count reveals where the density actually concentrates \u2014 hotspots, ridges, and empty regions \u2014 without the overplotting that hides structure in large samples.",
    setup:
      'rng = np.random.default_rng(4)\nx = rng.normal(0, 1, 5000)\ny = 0.6 * x + rng.normal(0, 0.8, 5000)',
    staticCall:
      'ax = dv.bivariate.hexbin_plot_static(x, y, gridsize=30)\nplt.show()',
    interactiveCall:
      'fig = dv.bivariate.hexbin_plot_interactive(x, y, gridsize=30)\nfig.show()',
  },
  regression_plot: {
    useCase:
      "Use a regression plot to overlay a fitted line or curve on raw observations so you can judge how well a simple model captures the relationship. The scatter shows the data, the fitted line shows the trend, and the gap between them \u2014 systematic curvature or funnel-shaped spread \u2014 tells you whether a linear model is adequate or a higher degree is needed.",
    setup:
      'rng = np.random.default_rng(5)\nx = rng.uniform(0, 10, 150)\ny = 3 + 2 * x + rng.normal(0, 3, 150)',
    staticCall:
      'ax = dv.bivariate.regression_plot_static(x, y, degree=1)\nplt.show()',
    interactiveCall:
      'fig = dv.bivariate.regression_plot_interactive(x, y, degree=1)\nfig.show()',
  },
  density_contour: {
    useCase:
      "Use a density contour plot to show the shape of a bivariate distribution when individual points would overlap. Contour lines trace regions of equal estimated density, so multiple modes, elongated correlation structure, and skew appear as terrain-like features rather than an undifferentiated point cloud.",
    setup:
      'rng = np.random.default_rng(6)\nx = rng.normal(0, 1, 1500)\ny = 0.7 * x + rng.normal(0, 0.7, 1500)',
    staticCall:
      'ax = dv.bivariate.density_contour_static(x, y)\nplt.show()',
    interactiveCall:
      'fig = dv.bivariate.density_contour_interactive(x, y)\nfig.show()',
  },
  grouped_bar: {
    useCase:
      "Use a grouped bar chart to compare an aggregated metric \u2014 mean, sum, or any custom function \u2014 across categories such as product lines, regions, or shifts. Bar height makes differences in level immediate, which suits ranked comparisons and presentations to audiences who read bars more easily than distributions.",
    setup:
      'rng = np.random.default_rng(7)\ncategory = pd.Series(rng.choice(["A", "B", "C", "D"], 400))\nvalues = pd.Series(rng.normal(100, 15, 400) + category.map(\n    {"A": 0, "B": 12, "C": -8, "D": 20}\n))',
    staticCall:
      'ax = dv.bivariate.grouped_bar_static(category, values)\nplt.show()',
    interactiveCall:
      'fig = dv.bivariate.grouped_bar_interactive(category, values)\nfig.show()',
  },
  box_by_category: {
    useCase:
      "Use box plots by category to compare the distribution of a continuous measure across groups \u2014 fill weight across machines, response time across servers. The median, quartiles, whiskers, and flier points expose shifts in location, differences in spread, and outliers per group without assuming any distribution shape.",
    setup:
      'rng = np.random.default_rng(8)\ncategory = pd.Series(rng.choice(["Line 1", "Line 2", "Line 3"], 300))\nvalues = pd.Series(rng.normal(50, 5, 300) + category.map(\n    {"Line 1": 0, "Line 2": 4, "Line 3": -3}\n))',
    staticCall:
      'ax = dv.bivariate.box_by_category_static(category, values)\nplt.show()',
    interactiveCall:
      'fig = dv.bivariate.box_by_category_interactive(category, values)\nfig.show()',
  },
  violin_by_category: {
    useCase:
      "Use violin plots by category when the box plot's five-number summary is too coarse \u2014 when you suspect bimodality, skew, or shoulder shapes within groups. The mirrored density trace shows the full estimated distribution per category, making multimodal or asymmetric groups obvious where a box plot would look identical.",
    setup:
      'rng = np.random.default_rng(9)\ncategory = pd.Series(rng.choice(["A", "B", "C"], 450))\nvalues = pd.Series(\n    np.where(\n        category == "B",\n        rng.normal(40, 4, 450),\n        rng.normal(50, 6, 450),\n    )\n)',
    staticCall:
      'ax = dv.bivariate.violin_by_category_static(category, values)\nplt.show()',
    interactiveCall:
      'fig = dv.bivariate.violin_by_category_interactive(category, values)\nfig.show()',
  },
  crosstab_heatmap: {
    useCase:
      "Use a crosstab heatmap to examine how two categorical variables co-occur \u2014 defect type by shift, segment by channel. Colour intensity over the contingency table highlights combinations that are unusually frequent or rare, and row or column normalisation converts raw counts into comparable rates when group sizes differ.",
    setup:
      'rng = np.random.default_rng(10)\nrows = pd.Series(rng.choice(["North", "South", "East"], 500, p=[0.5, 0.3, 0.2]))\ncols = pd.Series(rng.choice(["Pass", "Rework", "Scrap"], 500))',
    staticCall:
      'ax = dv.bivariate.crosstab_heatmap_static(rows, cols, normalize="index")\nplt.show()',
    interactiveCall:
      'fig = dv.bivariate.crosstab_heatmap_interactive(rows, cols, normalize="index")\nfig.show()',
  },
  binned_mean_plot: {
    useCase:
      "Use a binned mean plot to extract the trend from a noisy scatter by averaging y within equal-width bins of x. Binning suppresses point-level noise so the underlying shape \u2014 linear, saturating, U-shaped \u2014 stands out, which is especially useful for large datasets where the raw cloud is too dense to read.",
    setup:
      'rng = np.random.default_rng(11)\nx = rng.uniform(0, 10, 2000)\ny = 2 * x + rng.normal(0, 5, 2000)',
    staticCall:
      'ax = dv.bivariate.binned_mean_plot_static(x, y, bins=12)\nplt.show()',
    interactiveCall:
      'fig = dv.bivariate.binned_mean_plot_interactive(x, y, bins=12)\nfig.show()',
  },
  errorbar_plot: {
    useCase:
      "Use an errorbar plot when each point carries uncertainty \u2014 replicated measurements, survey estimates, simulation means. Drawing the error bars alongside the central values shows which differences between conditions are larger than their uncertainty and which could easily be noise, preventing over-reading of small gaps.",
    setup:
      'rng = np.random.default_rng(12)\nx = np.arange(1, 9)\ny = 10 + 2 * x + rng.normal(0, 0.5, 8)\nyerr = rng.uniform(0.5, 2.0, 8)',
    staticCall:
      'ax = dv.bivariate.errorbar_plot_static(x, y, yerr=yerr)\nplt.show()',
    interactiveCall:
      'fig = dv.bivariate.errorbar_plot_interactive(x, y, yerr=yerr)\nfig.show()',
  },
  area_between: {
    useCase:
      "Use an area-between plot to display a band bounded by two curves \u2014 a confidence interval around a forecast, tolerance limits around a nominal profile, or a min-max envelope from repeated runs. The shaded region communicates the range of plausible values directly, which is clearer than two separate boundary lines.",
    setup:
      'rng = np.random.default_rng(13)\nx = np.linspace(0, 10, 100)\nmid = np.sin(x)\ny_lower = mid - 0.3\ny_upper = mid + 0.3',
    staticCall:
      'ax = dv.bivariate.area_between_static(x, y_lower, y_upper)\nplt.show()',
    interactiveCall:
      'fig = dv.bivariate.area_between_interactive(x, y_lower, y_upper)\nfig.show()',
  },
  step_plot: {
    useCase:
      "Use a step plot for values that change discretely and hold until the next change \u2014 price tiers, setpoint adjustments, staffing levels, cumulative counts. The horizontal-then-vertical trace correctly shows that the value is constant between events, where a sloped line would falsely imply gradual transitions.",
    setup:
      'rng = np.random.default_rng(14)\nx = np.arange(0, 20)\ny = np.cumsum(rng.choice([-1, 0, 1, 2], 20, p=[0.2, 0.3, 0.3, 0.2])) + 20',
    staticCall:
      'ax = dv.bivariate.step_plot_static(x, y, where="post")\nplt.show()',
    interactiveCall:
      'fig = dv.bivariate.step_plot_interactive(x, y, where="post")\nfig.show()',
  },
  joint_scatter_hist: {
    useCase:
      "Use a joint scatter-histogram plot to see the bivariate relationship and both marginal distributions at once. The central scatter shows how the variables move together while the side histograms reveal skew, bimodality, or outliers in each variable alone \u2014 context that changes how the joint pattern should be interpreted.",
    setup:
      'rng = np.random.default_rng(15)\nx = rng.normal(0, 1, 500)\ny = 0.6 * x + rng.normal(0, 0.8, 500)',
    staticCall:
      'ax = dv.bivariate.joint_scatter_hist_static(x, y)\nplt.show()',
    interactiveCall:
      'fig = dv.bivariate.joint_scatter_hist_interactive(x, y)\nfig.show()',
  },
  bivariate_histogram: {
    useCase:
      "Use a bivariate histogram to map the joint density of two continuous variables as a gridded heatmap. Rectangular bin counts make concentration regions, correlation ridges, and sparse tails quantitatively readable, and the regular grid is easy to tune (bins) or export for further numeric analysis.",
    setup:
      'rng = np.random.default_rng(16)\nx = rng.normal(0, 1, 3000)\ny = 0.5 * x + rng.normal(0, 0.9, 3000)',
    staticCall:
      'ax = dv.bivariate.bivariate_histogram_static(x, y, bins=30)\nplt.show()',
    interactiveCall:
      'fig = dv.bivariate.bivariate_histogram_interactive(x, y, bins=30)\nfig.show()',
  },
  outlier_scatter: {
    useCase:
      "Use an outlier scatter plot to separate anomalous points from the bulk of the data using IQR fences or z-scores on both variables. Colour-coding flagged points shows immediately whether outliers are isolated data-entry errors, extreme but plausible values, or a distinct sub-population that deserves separate treatment.",
    setup:
      'rng = np.random.default_rng(17)\nx = rng.normal(50, 8, 300)\ny = 0.8 * x + rng.normal(0, 6, 300)\nx = np.r_[x, [95, 20, 105]]\ny = np.r_[y, [30, 90, 110]]',
    staticCall:
      'ax = dv.bivariate.outlier_scatter_static(x, y, method="iqr")\nplt.show()',
    interactiveCall:
      'fig = dv.bivariate.outlier_scatter_interactive(x, y, method="iqr")\nfig.show()',
  },
  residual_relationship: {
    useCase:
      "Use the residual relationship plot to diagnose how well a polynomial fit of a given degree captures the relationship between two variables. Plotting the fit residuals against the predictor exposes systematic curvature, fan-shaped heteroscedasticity, and influential points \u2014 patterns that mean the chosen degree or a linear model itself is inadequate.",
    setup:
      'rng = np.random.default_rng(18)\nx = rng.uniform(0, 10, 200)\ny = 2 * x + 0.3 * x**2 + rng.normal(0, 2, 200)',
    staticCall:
      'ax = dv.bivariate.residual_relationship_static(x, y, degree=1)\nplt.show()',
    interactiveCall:
      'fig = dv.bivariate.residual_relationship_interactive(x, y, degree=1)\nfig.show()',
  },
  quantile_bin_plot: {
    useCase:
      "Use a quantile bin plot to summarise how the mean or median of y changes across equal-count bins of x. Because each bin holds the same number of observations, every point is estimated with equal precision, giving a cleaner dose-response or trend curve than equal-width bins when x is unevenly distributed.",
    setup:
      'rng = np.random.default_rng(19)\nx = rng.gamma(2.0, 1.5, 1500)\ny = 5 + 3 * np.log1p(x) + rng.normal(0, 1.5, 1500)',
    staticCall:
      'ax = dv.bivariate.quantile_bin_plot_static(x, y, q=10)\nplt.show()',
    interactiveCall:
      'fig = dv.bivariate.quantile_bin_plot_interactive(x, y, q=10)\nfig.show()',
  },
  bland_altman: {
    useCase:
      "Use the Bland-Altman plot to assess agreement between two measurement methods \u2014 a new sensor against a reference instrument, one lab assay against another. Plotting the difference against the mean reveals systematic bias (the mean-difference line), the limits of agreement within which 95% of differences fall, and whether disagreement grows with magnitude.",
    setup:
      'rng = np.random.default_rng(20)\nmethod_a = rng.normal(100, 15, 150)\nmethod_b = method_a + rng.normal(2.0, 4.0, 150)',
    staticCall:
      'ax = dv.bivariate.bland_altman_static(method_a, method_b)\nplt.show()',
    interactiveCall:
      'fig = dv.bivariate.bland_altman_interactive(method_a, method_b)\nfig.show()',
  },
  rank_scatter: {
    useCase:
      "Use a rank scatter plot to visualise monotonic association after replacing raw values with their ranks, the basis of Spearman's correlation. Ranking removes the influence of outliers and non-linear scales, so the plot shows whether one variable consistently increases with the other even when the raw relationship is curved or heavy-tailed.",
    setup:
      'rng = np.random.default_rng(21)\nx = rng.uniform(0, 100, 200)\ny = np.sqrt(x) * 10 + rng.normal(0, 8, 200)',
    staticCall:
      'ax = dv.bivariate.rank_scatter_static(x, y)\nplt.show()',
    interactiveCall:
      'fig = dv.bivariate.rank_scatter_interactive(x, y)\nfig.show()',
  },
  lag_plot: {
    useCase:
      "Use a lag plot to check time-ordered data for autocorrelation by plotting each value against the value k periods earlier. Random scatter along no particular pattern indicates independence, while structure \u2014 a diagonal band, a curve, or an ellipse \u2014 reveals serial dependence that violates the assumptions of many control charts and time-series models.",
    setup:
      'rng = np.random.default_rng(22)\nnoise = rng.normal(0, 1, 300)\nseries = pd.Series(np.convolve(noise, [0.8, 0.2], mode="same")[:300])',
    staticCall:
      'ax = dv.bivariate.lag_plot_static(series, series, lag=1)\nplt.show()',
    interactiveCall:
      'fig = dv.bivariate.lag_plot_interactive(series, series, lag=1)\nfig.show()',
  },
  conditional_box: {
    useCase:
      "Use a conditional box plot to see how the full distribution of y changes as x increases by binning x and drawing a box plot per bin. Unlike a mean line, the boxes expose where spread widens, where medians shift non-linearly, and where outliers concentrate \u2014 a distribution-aware view of the conditional relationship.",
    setup:
      'rng = np.random.default_rng(23)\nx = rng.uniform(0, 10, 800)\ny = 3 * x + rng.normal(0, 1 + 0.4 * x, 800)',
    staticCall:
      'ax = dv.bivariate.conditional_box_static(x, y, bins=8)\nplt.show()',
    interactiveCall:
      'fig = dv.bivariate.conditional_box_interactive(x, y, bins=8)\nfig.show()',
  },
};
