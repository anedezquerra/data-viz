User guide
==========

Choosing a module
-----------------

``dataviz.univariate``
   One-variable summaries, distributions, data quality, transformations,
   weighting, outlier treatment, bootstrap inference, text, and datetime data.

``dataviz.bivariate``
   Numeric relationships, categorical comparisons, paired diagnostics, trends,
   joint distributions, agreement, ranks, and lag analysis.

``dataviz.spc``
   Variable and attribute control charts, capability analysis, rules,
   diagnostics, dashboards, and Hotelling T2 monitoring.

``dataviz.multivariate`` and ``dataviz.eda``
   Pairwise overviews, heatmaps, parallel coordinates, missingness,
   distribution summaries, and class balance checks.

``dataviz.classification``, ``dataviz.regression``, and ``dataviz.clustering``
   Model evaluation and diagnostic visualizations.

``dataviz.xai``
   Feature importance, SHAP-style contribution, and partial-dependence plots.

Static and interactive APIs
---------------------------

Most chart families expose three names:

* ``*_static`` returns a Matplotlib ``Axes`` object.
* ``*_interactive`` returns a Plotly ``Figure`` object.
* The unsuffixed convenience alias usually selects the static implementation.

Keeping the return object lets callers continue styling, compose figures, save
images, or embed interactive charts without the library taking control of the
display lifecycle.

Data handling
-------------

Functions generally accept pandas objects, NumPy arrays, or Python sequences.
Named pandas Series produce better axis labels. Helpers reject empty or
incompatible inputs early and document the relevant ``ValueError`` or
``TypeError`` conditions in the API reference.

Reproducibility
---------------

Pass explicit seeds to bootstrap functions, keep transformations visible in
analysis code, and inspect outlier flags before changing data. For SPC work,
calculate limits and rule violations separately when results must be audited.
