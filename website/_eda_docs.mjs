// Curated EDA documentation content: real use-case descriptions and complete,
// copy-paste code samples per chart family. Consumed by
// _generate_function_docs.mjs to replace the auto-generated boilerplate on EDA
// function pages. Image galleries come from assets/examples/eda/manifest.json.
//
// Keys are chart-family base names (without the _static/_interactive suffix).
// Each entry provides:
//   useCase          - full description of when and why to use the chart.
//   setup            - shared data-preparation lines for the code sample.
//   staticCall       - call + display lines for the *_static form.
//   interactiveCall  - call + display lines for the *_interactive form.

export const EDA_OVERRIDES = {
  missing_data_plot: {
    useCase:
      "Use the missing data plot before any cleaning or modelling to see how many values are absent in every column. The bar heights make it obvious whether missingness is a scattered minor nuisance or concentrated in specific fields that need imputation, indicator flags, or upstream fixes. Checking this first prevents silent row loss when models drop incomplete cases.",
    setup:
      'rng = np.random.default_rng(11)\nn = 300\ndf = pd.DataFrame(\n    {\n        "age": rng.normal(40.0, 12.0, n),\n        "income": rng.normal(60000.0, 15000.0, n),\n        "score": rng.normal(0.5, 0.2, n),\n    }\n)\ndf.loc[rng.choice(n, 45, replace=False), "income"] = np.nan\ndf.loc[rng.choice(n, 12, replace=False), "score"] = np.nan',
    staticCall:
      'ax = dv.eda.missing_data_plot_static(df, title="Missing values per column")\nplt.show()',
    interactiveCall:
      'fig = dv.eda.missing_data_plot_interactive(df, title="Missing values per column")\nfig.show()',
  },
  distribution_summary: {
    useCase:
      "Use the distribution summary to review the shape of every numeric column in one figure before analysis. Placing the histograms side by side makes skewness, outliers, bimodality, and scale differences visible immediately, so you can decide on transforms, robust statistics, or per-column treatment rather than discovering problems mid-modelling.",
    setup:
      'rng = np.random.default_rng(13)\nn = 400\ndf = pd.DataFrame(\n    {\n        "age": rng.normal(40.0, 12.0, n),\n        "income": rng.gamma(2.0, 20000.0, n),\n        "visits": rng.poisson(4.0, n),\n    }\n)',
    staticCall:
      'fig = dv.eda.distribution_summary_static(df, title="Column distributions")\nplt.show()',
    interactiveCall:
      'fig = dv.eda.distribution_summary_interactive(df, title="Column distributions")\nfig.show()',
  },
  class_distribution: {
    useCase:
      "Use the class distribution plot to check the balance of a categorical target before training a classifier. Bars that differ wildly in height warn that accuracy alone will be misleading and that you may need stratified sampling, class weights, or resampling. It is a one-second check that prevents the classic mistake of modelling a rare class with default settings.",
    setup:
      'rng = np.random.default_rng(17)\nlabels = rng.choice(\n    ["approved", "review", "rejected"], size=500, p=[0.6, 0.3, 0.1]\n)\nclasses = pd.Series(labels, name="outcome")',
    staticCall:
      'ax = dv.eda.class_distribution_static(classes, title="Class balance")\nplt.show()',
    interactiveCall:
      'fig = dv.eda.class_distribution_interactive(classes, title="Class balance")\nfig.show()',
  },
};
