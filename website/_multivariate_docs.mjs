// Curated multivariate documentation content: real use-case descriptions and
// complete, copy-paste code samples per chart family. Consumed by
// _generate_function_docs.mjs to replace the auto-generated boilerplate on
// multivariate function pages. Image galleries come from
// assets/examples/multivariate/manifest.json.
//
// Keys are chart-family base names (without the _static/_interactive suffix).
// Each entry provides:
//   useCase          - full description of when and why to use the chart.
//   setup            - shared data-preparation lines for the code sample.
//   staticCall       - call + display lines for the *_static form.
//   interactiveCall  - call + display lines for the *_interactive form.

export const MULTIVARIATE_OVERRIDES = {
  pairplot: {
    useCase:
      "Use a pairplot to scan every pairwise relationship in a small set of numeric variables at once. The off-diagonal scatter plots expose correlations, clusters, and non-linear shapes, while the diagonal shows each variable\u2019s own distribution. It is the fastest way to spot redundant features and promising interactions before modelling.",
    setup:
      'rng = np.random.default_rng(3)\nx1 = rng.normal(0.0, 1.0, 200)\ndf = pd.DataFrame(\n    {\n        "length": x1,\n        "weight": 0.8 * x1 + rng.normal(0.0, 0.4, 200),\n        "age": rng.normal(5.0, 1.5, 200),\n    }\n)',
    staticCall:
      'fig = dv.multivariate.pairplot_static(df, title="Feature pairplot")\nplt.show()',
    interactiveCall:
      'fig = dv.multivariate.pairplot_interactive(df, title="Feature pairplot")\nfig.show()',
  },
  heatmap: {
    useCase:
      "Use a heatmap to read a whole matrix at a glance \u2014 most often a correlation matrix, where colour intensity turns dozens of coefficients into an instantly scannable pattern. Blocks of strong colour reveal groups of variables that move together, which helps detect multicollinearity, redundant features, and hidden structure in wide datasets.",
    setup:
      'rng = np.random.default_rng(5)\nx1 = rng.normal(0.0, 1.0, 300)\nx2 = 0.9 * x1 + rng.normal(0.0, 0.3, 300)\ndf = pd.DataFrame(\n    {\n        "length": x1,\n        "weight": x2,\n        "age": rng.normal(0.0, 1.0, 300),\n        "price": -0.6 * x1 + rng.normal(0.0, 0.8, 300),\n    }\n)\ncorr = df.corr()',
    staticCall:
      'ax = dv.multivariate.heatmap_static(corr, title="Correlation heatmap")\nplt.show()',
    interactiveCall:
      'fig = dv.multivariate.heatmap_interactive(corr, title="Correlation heatmap")\nfig.show()',
  },
  parallel_coordinates: {
    useCase:
      "Use a parallel coordinates plot to compare many multi-dimensional records at once by drawing each row as a line across one vertical axis per variable. Clusters of lines that travel together reveal shared profiles, while lines that cross the pack mark unusual combinations. It shines for spotting groups and outliers in medium-dimensional data where scatter plots run out of dimensions.",
    setup:
      'rng = np.random.default_rng(9)\nn = 60\ndf = pd.DataFrame(\n    {\n        "speed": rng.normal(50.0, 8.0, n),\n        "power": rng.normal(120.0, 15.0, n),\n        "weight": rng.normal(900.0, 80.0, n),\n        "range": rng.normal(300.0, 40.0, n),\n    }\n)',
    staticCall:
      'ax = dv.multivariate.parallel_coordinates_static(df, title="Vehicle profiles")\nplt.show()',
    interactiveCall:
      'fig = dv.multivariate.parallel_coordinates_interactive(df, color_col="speed")\nfig.show()',
  },
};
