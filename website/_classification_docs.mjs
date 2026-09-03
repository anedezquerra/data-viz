// Curated classification documentation content: real use-case descriptions and
// complete, copy-paste code samples per chart family. Consumed by
// _generate_function_docs.mjs to replace the auto-generated boilerplate on
// classification function pages. Image galleries come from
// assets/examples/classification/manifest.json.
//
// Keys are chart-family base names (without the _static/_interactive suffix).
// Each entry provides:
//   useCase          - full description of when and why to use the chart.
//   setup            - shared data-preparation lines for the code sample.
//   staticCall       - call + display lines for the *_static form.
//   interactiveCall  - call + display lines for the *_interactive form.

export const CLASSIFICATION_OVERRIDES = {
  confusion_matrix_plot: {
    useCase:
      "Use the confusion matrix to see not just how often a classifier is wrong but exactly where the errors go \u2014 which classes are mistaken for which. Rows are the true classes and columns the predictions, so off-diagonal cells reveal systematic confusions that a single accuracy score would hide. It is especially valuable with imbalanced data, where high accuracy can mask poor performance on the minority class.",
    setup:
      'cm = [[48, 2, 0], [3, 44, 3], [0, 4, 46]]\nlabels = ["Setosa", "Versicolor", "Virginica"]',
    staticCall:
      'ax = dv.classification.confusion_matrix_plot_static(\n    cm, labels=labels, title="Confusion matrix"\n)\nplt.show()',
    interactiveCall:
      'fig = dv.classification.confusion_matrix_plot_interactive(\n    cm, labels=labels, title="Confusion matrix"\n)\nfig.show()',
  },
  roc_curve: {
    useCase:
      "Use the ROC curve to judge how well a classifier's scores separate the positive class from the negative across every possible decision threshold. Each point trades true positive rate against false positive rate, and the area under the curve (AUC) summarises ranking quality: 1.0 is perfect, 0.5 is no better than chance. Because it is threshold-independent, it is the standard way to compare models before choosing an operating point.",
    setup:
      'fpr = np.linspace(0.0, 1.0, 50)\ntpr = fpr ** 0.2\nauc = float(np.trapezoid(tpr, fpr))',
    staticCall:
      'ax = dv.classification.roc_curve_static(\n    fpr, tpr, auc=auc, title="ROC curve"\n)\nplt.show()',
    interactiveCall:
      'fig = dv.classification.roc_curve_interactive(\n    fpr, tpr, auc=auc, title="ROC curve"\n)\nfig.show()',
  },
  precision_recall_curve: {
    useCase:
      "Use the precision\u2013recall curve instead of ROC when the positive class is rare \u2014 fraud detection, defect screening, medical diagnosis. ROC can look optimistic on imbalanced data because the false positive rate stays low simply due to the huge number of negatives; precision\u2013recall focuses only on the positives and shows how much precision you sacrifice as you push recall higher. The average precision (AP) score summarises the curve in one number.",
    setup:
      'recall = np.linspace(0.0, 1.0, 50)\nprecision = 1.0 - 0.3 * recall ** 3\nap = float(np.trapezoid(precision, recall))',
    staticCall:
      'ax = dv.classification.precision_recall_curve_static(\n    precision, recall, ap=ap, title="Precision\u2013recall curve"\n)\nplt.show()',
    interactiveCall:
      'fig = dv.classification.precision_recall_curve_interactive(\n    precision, recall, ap=ap, title="Precision\u2013recall curve"\n)\nfig.show()',
  },
};
