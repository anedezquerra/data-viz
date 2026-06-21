Examples gallery
================

A curated, copy-paste-ready gallery of **80 worked examples** covering every
sub-package of ``dataviz``. Each example page contains, for two charts:

* a plain-English **description** of the chart and what it is good for;
* the **situation** that motivates using the chart;
* a complete, **executable code block** (deterministic synthetic data, no
  external files required) you can copy-paste into a notebook or script;
* a **sample chart** rendered from that exact code;
* the **requirements** to reproduce the example;
* short **notes** with pitfalls, tuning hints and pointers to related charts.

The examples are organised by analytical theme so you can jump straight to the
section that matches your task.

.. tip::
   All examples seed ``numpy.random.default_rng(0)`` so the output is fully
   reproducible. Re-running the snippet produces the exact figure shown on
   the page.

Univariate analysis
-------------------

Single-variable visualisations for distribution shape, central tendency,
spread, outliers, ranking and inequality.

.. toctree::
   :maxdepth: 1

   examples/univariate_01
   examples/univariate_02
   examples/univariate_03
   examples/univariate_04
   examples/univariate_05
   examples/univariate_06
   examples/univariate_07

Bivariate analysis
------------------

Two-variable visualisations covering scatter, line, regression, density and
group-wise comparisons.

.. toctree::
   :maxdepth: 1

   examples/bivariate_01
   examples/bivariate_02
   examples/bivariate_03
   examples/bivariate_04
   examples/bivariate_05
   examples/bivariate_06

Multivariate analysis
---------------------

Helpers for exploring three or more variables simultaneously.

.. toctree::
   :maxdepth: 1

   examples/multivariate_01
   examples/mixed_01

Exploratory data analysis (EDA)
-------------------------------

Fast first-pass audits of a fresh dataset: missingness, per-column shape and
class balance.

.. toctree::
   :maxdepth: 1

   examples/eda_01

Statistical process control (SPC)
---------------------------------

Shewhart, EWMA and CUSUM charts, capability assessment and Western Electric
rule detection.

.. toctree::
   :maxdepth: 1

   examples/spc_01
   examples/spc_02
   examples/spc_03
   examples/spc_04

Regression diagnostics
----------------------

Residual analysis, calibration plots and learning curves for regression
models.

.. toctree::
   :maxdepth: 1

   examples/regression_01
   examples/mixed_02

Classification diagnostics
--------------------------

Confusion matrices, ROC and precision-recall curves, calibration, threshold
selection, gain / lift, multiclass and multilabel quality, fairness segments,
error analysis, model comparison, drift monitoring and training diagnostics.

.. toctree::
   :maxdepth: 1

   examples/classification_01
   examples/classification_02
   examples/classification_03
   examples/classification_04
   examples/classification_05
   examples/classification_06
   examples/classification_07
   examples/classification_08
   examples/classification_09
   examples/classification_10
   examples/classification_11
   examples/classification_12
   examples/classification_13
   examples/classification_14
   examples/classification_15
   examples/classification_16

Clustering
----------

Diagnostic views for partitional and hierarchical clustering: cluster
scatter, elbow plots and dendrograms.

.. toctree::
   :maxdepth: 1

   examples/clustering_01
   examples/mixed_03

Explainable AI (XAI)
--------------------

Per-feature and per-prediction interpretability views: SHAP summaries,
partial dependence and feature importance rankings.

.. toctree::
   :maxdepth: 1

   examples/xai_01

How to reproduce every example
------------------------------

The repository ships two helper scripts under ``docs/_tools/``:

* ``generate_examples.py`` regenerates every sample chart PNG used in this
  gallery from synthetic data.
* ``generate_example_pages.py`` regenerates the RST pages from the example
  registry, so the documentation stays in sync with the executable code.

Both scripts are deterministic and self-contained. Run them from the
repository root after activating the ``[dev,docs]`` extras::

   pip install -e ".[dev,docs]"
   python docs/_tools/generate_examples.py
   python docs/_tools/generate_example_pages.py
