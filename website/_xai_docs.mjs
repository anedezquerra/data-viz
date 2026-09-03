// Curated XAI documentation content: real use-case descriptions and complete,
// copy-paste code samples per chart family. Consumed by
// _generate_function_docs.mjs to replace the auto-generated boilerplate on XAI
// function pages. Image galleries come from assets/examples/xai/manifest.json.
//
// Keys are chart-family base names (without the _static/_interactive suffix).
// Each entry provides:
//   useCase          - full description of when and why to use the chart.
//   setup            - shared data-preparation lines for the code sample.
//   staticCall       - call + display lines for the *_static form.
//   interactiveCall  - call + display lines for the *_interactive form.

export const XAI_OVERRIDES = {
  feature_importance: {
    useCase:
      "Use the feature importance chart to rank which inputs drive a model\u2019s predictions most. Comparing bar lengths separates the few features that carry the signal from the many that contribute little, which guides feature selection, debugging, and stakeholder communication. Impacts are most trustworthy when importances come from a held-out set (for example permutation importance) rather than training data.",
    setup:
      'features = ["Age", "Income", "Tenure", "Region", "Device", "Channel"]\nimportances = pd.Series(\n    [0.42, 0.21, 0.14, 0.09, 0.08, 0.06], index=features\n)',
    staticCall:
      'ax = dv.xai.feature_importance_static(importances, title="Permutation importance")\nplt.show()',
    interactiveCall:
      'fig = dv.xai.feature_importance_interactive(importances, title="Permutation importance")\nfig.show()',
  },
  shap_plot: {
    useCase:
      "Use the SHAP summary plot to see which features have the largest average effect on a model\u2019s output. Each feature is ranked by its mean absolute SHAP value \u2014 the average magnitude of its contribution per prediction \u2014 so the chart answers \u201cwhat does the model rely on overall?\u201d Pair it with per-observation plots when you also need to explain individual predictions.",
    setup:
      'rng = np.random.default_rng(7)\nfeature_names = ["Age", "Income", "Tenure", "Region"]\nshap_values = np.column_stack(\n    [\n        rng.normal(0.0, 0.9, 200),\n        rng.normal(0.0, 0.45, 200),\n        rng.normal(0.0, 0.2, 200),\n        rng.normal(0.0, 0.05, 200),\n    ]\n)',
    staticCall:
      'ax = dv.xai.shap_plot_static(shap_values, feature_names, title="SHAP feature impact")\nplt.show()',
    interactiveCall:
      'fig = dv.xai.shap_plot_interactive(shap_values, feature_names, title="SHAP feature impact")\nfig.show()',
  },
  partial_dependence: {
    useCase:
      "Use a partial dependence plot to see how a model\u2019s prediction changes as one feature varies, averaged over everything else. The curve reveals whether the learned relationship is linear, saturating, threshold-like, or non-monotonic \u2014 essential for sanity-checking that a black-box model behaves the way domain knowledge says it should before it goes into production.",
    setup:
      "grid = np.linspace(0.0, 10.0, 30)\npredictions = 2.0 + 1.5 * np.log1p(grid)",
    staticCall:
      'ax = dv.xai.partial_dependence_static(grid, predictions, feature_name="Income")\nplt.show()',
    interactiveCall:
      'fig = dv.xai.partial_dependence_interactive(grid, predictions, feature_name="Income")\nfig.show()',
  },
};
