// Curated regression documentation content: real use-case descriptions and
// complete, copy-paste code samples per chart family. Consumed by
// _generate_function_docs.mjs to replace the auto-generated boilerplate on
// regression function pages. Image galleries come from
// assets/examples/regression/manifest.json.
//
// Keys are chart-family base names (without the _static/_interactive suffix).
// Each entry provides:
//   useCase          - full description of when and why to use the chart.
//   setup            - shared data-preparation lines for the code sample.
//   staticCall       - call + display lines for the *_static form.
//   interactiveCall  - call + display lines for the *_interactive form.

export const REGRESSION_OVERRIDES = {
  residual_plot: {
    useCase:
      "Use the residual plot to check whether a regression model's errors look like random noise or carry structure the model failed to capture. Plotting residuals against the fitted values should show a shapeless cloud around zero; a funnel shape signals heteroscedasticity, a curve signals a missed nonlinear effect, and isolated points flag outliers. It is the fastest visual test of whether the model assumptions hold.",
    setup:
      "rng = np.random.default_rng(0)\ny_true = rng.uniform(10.0, 50.0, size=120)\ny_pred = y_true + rng.normal(0.0, 3.0, size=120)",
    staticCall:
      'ax = dv.regression.residual_plot_static(\n    y_true, y_pred, title="Residual plot"\n)\nplt.show()',
    interactiveCall:
      'fig = dv.regression.residual_plot_interactive(\n    y_true, y_pred, title="Residual plot"\n)\nfig.show()',
  },
  prediction_plot: {
    useCase:
      "Use the prediction plot to see how closely predicted values track the observed ones by comparing both against the 45-degree identity line. Points hugging the line mean accurate predictions; systematic departure above or below it reveals bias, and widening scatter shows where the model loses precision. It communicates overall fit to non-technical audiences more directly than error metrics alone.",
    setup:
      "rng = np.random.default_rng(1)\ny_true = rng.uniform(10.0, 50.0, size=120)\ny_pred = y_true + rng.normal(0.0, 2.5, size=120)",
    staticCall:
      'ax = dv.regression.prediction_plot_static(\n    y_true, y_pred, title="Predicted vs. observed"\n)\nplt.show()',
    interactiveCall:
      'fig = dv.regression.prediction_plot_interactive(\n    y_true, y_pred, title="Predicted vs. observed"\n)\nfig.show()',
  },
  learning_curve: {
    useCase:
      "Use the learning curve to diagnose whether a model suffers from high bias, high variance, or simply needs more data. It plots training and validation scores against training-set size: converging curves mean more data will not help, a persistent wide gap signals overfitting that regularisation or more samples may close, and both curves plateauing low signal underfitting. It guides the next modelling decision instead of guesswork.",
    setup:
      "train_sizes = np.linspace(0.1, 1.0, 8)\ntrain_scores = np.array(\n    [0.98, 0.95, 0.92, 0.90, 0.89, 0.88, 0.87, 0.86]\n)\nval_scores = np.array(\n    [0.72, 0.78, 0.82, 0.84, 0.85, 0.86, 0.86, 0.86]\n)",
    staticCall:
      'ax = dv.regression.learning_curve_static(\n    train_sizes, train_scores, val_scores, title="Learning curve"\n)\nplt.show()',
    interactiveCall:
      'fig = dv.regression.learning_curve_interactive(\n    train_sizes, train_scores, val_scores, title="Learning curve"\n)\nfig.show()',
  },
};
