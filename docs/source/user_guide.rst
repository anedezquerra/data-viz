User guide
==========

This guide explains how DataViz is organized, how to choose the right module
for a given analysis, how the static and interactive APIs are designed to
compose with the rest of the scientific Python stack, and how to cite the
project in academic or applied work.

.. contents::
   :local:
   :depth: 2

Scope and design principles
---------------------------

DataViz is organized around three principles:

* **Domain-first packaging.** Modules are named after analytical tasks
  (``univariate``, ``bivariate``, ``spc``, ``xai``, ``classification``,
  ``regression``, ``clustering``, ``multivariate``, ``eda``) rather than after
  rendering backends. Within each module, files are split by chart family so
  imports stay small and reviewable.
* **Dual rendering surfaces.** Every chart family exposes a Matplotlib/Seaborn
  static variant for publication and reporting workflows, and a Plotly
  interactive variant for exploratory and dashboard workflows. The two
  variants share parameter names and semantics so analyses can move between
  them with minimal friction.
* **Hand back control.** Functions return the underlying ``Axes`` or
  ``Figure`` instead of calling ``show()``, ``savefig()``, or ``write_html()``
  themselves. This keeps DataViz embeddable in notebooks, Streamlit/Dash apps,
  static reports, and CI image-diff pipelines.

Choosing a module
-----------------

The table below maps analytical questions to the module that owns the
relevant chart family.

.. list-table::
   :header-rows: 1
   :widths: 28 42 30

   * - Module
     - Use it when you need…
     - Representative entry points
   * - ``dataviz.univariate``
     - One-variable summaries: distributions, density, quality, outlier
       treatment, weighting, bootstrap inference, datetime and text profiling.
     - ``histogram``, ``density``, ``box_plot``, ``violin_plot``,
       ``auto_profile``
   * - ``dataviz.bivariate``
     - Two-variable relationships: scatter, regression overlays, joint
       histograms, agreement, rank correlation, lag analysis.
     - ``scatter_plot``, ``line_plot``, ``correlation_heatmap``,
       ``bivariate_histogram``
   * - ``dataviz.multivariate``
     - Many-variable overviews: pairplots, heatmaps, parallel coordinates.
     - ``pairplot``, ``heatmap``, ``parallel_coordinates``
   * - ``dataviz.eda``
     - Cross-cutting exploratory data analysis: missingness, distribution
       summaries, class-balance checks.
     - ``missing_data_plot``, ``distribution_summary``,
       ``class_distribution``
   * - ``dataviz.spc``
     - Statistical process control: variable and attribute control charts,
       capability analysis, Western Electric rules, Hotelling T², dashboards.
     - ``control_chart``, ``x_range_chart``, ``capability_histogram``,
       ``spc_dashboard_interactive``
   * - ``dataviz.regression``
     - Regression-model diagnostics: residual plots, prediction vs. actual,
       learning curves.
     - ``residual_plot``, ``prediction_plot``, ``learning_curve``
   * - ``dataviz.classification``
     - Classification-model evaluation: confusion matrices, ROC, PR curves.
     - ``confusion_matrix_plot``, ``roc_curve``,
       ``precision_recall_curve``
   * - ``dataviz.clustering``
     - Cluster diagnostics: 2-D cluster scatter, elbow plots, dendrograms.
     - ``scatter_clusters``, ``elbow_plot``, ``dendrogram``
   * - ``dataviz.xai``
     - Explainable AI: feature importance, SHAP-style contributions, partial
       dependence.
     - ``feature_importance``, ``shap_plot``, ``partial_dependence``
   * - ``dataviz.utils``
     - Shared helpers: theme application, input validation, plot setup.
     - ``setup_plot``, ``apply_theme``

Static and interactive APIs
---------------------------

Every chart family exposes up to three names:

* ``name_static`` — returns :class:`matplotlib.axes.Axes`.
* ``name_interactive`` — returns :class:`plotly.graph_objects.Figure`.
* ``name`` — convenience alias resolving to the static variant.

This indirection lets callers compose figures, restyle them, embed them in
reports, or hand them to Plotly's image/HTML exporters without DataViz
asserting any rendering policy.

When to prefer which
~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 32 34 34

   * - Context
     - Recommended variant
     - Why
   * - Publications, PDFs, LaTeX
     - ``*_static``
     - Vector / raster export through Matplotlib; reproducible typography.
   * - Notebooks for exploration
     - Either
     - Static for quick scans; interactive when you need hover or zoom.
   * - Dashboards (Dash / Streamlit)
     - ``*_interactive``
     - Returns a ``Figure`` ready for ``st.plotly_chart`` / ``dcc.Graph``.
   * - CI image-diff tests
     - ``*_static``
     - Deterministic pixel output; pair with a frozen Matplotlib style.
   * - Stakeholder presentations
     - ``*_interactive``
     - Hover tooltips, legend toggles, range sliders.

Data handling
-------------

Accepted input types
~~~~~~~~~~~~~~~~~~~~

All chart functions accept one of:

* :class:`pandas.Series` or :class:`pandas.DataFrame` columns,
* :class:`numpy.ndarray` of numeric or datetime dtype,
* plain Python sequences (``list``, ``tuple``) that NumPy can coerce.

Named ``pandas.Series`` produce labelled axes automatically; pass ``title=``
or set axis labels manually otherwise.

Missing data
~~~~~~~~~~~~

NaN handling follows the underlying backend's conventions:

* Matplotlib silently drops NaNs from line and scatter plots; histograms skip
  them.
* DataViz validation helpers raise :class:`ValueError` when an input is *all*
  NaN, empty, or shape-incompatible. The triggering condition is documented in
  each function's API reference page.

For explicit accounting of missingness, use ``dataviz.eda.missing_data_plot``
before applying transformations or imputing.

Dtypes and units
~~~~~~~~~~~~~~~~

* Datetime series are passed through unchanged to both backends; Plotly will
  render a range slider when appropriate.
* Categorical data should be supplied as ``pandas.Categorical`` to control
  ordering on box plots, violin plots, and bar charts.
* Mixed-dtype inputs are rejected early rather than coerced silently.

Theming and styling
-------------------

DataViz keeps styling explicit. There is no global theme switch that mutates
external libraries. Apply the bundled theme inside a context manager so the
rest of your code is unaffected:

.. code-block:: python

   from dataviz.utils import apply_theme

   with apply_theme("default"):
       ax = dv.histogram(values, title="Cycle-time distribution")

For Plotly figures, prefer:

.. code-block:: python

   fig = dv.histogram_interactive(values)
   fig.update_layout(template="plotly_white")

Composition and layout
----------------------

Because static functions return ``Axes``, you can compose subplot grids
without DataViz holding the matplotlib state machine:

.. code-block:: python

   import matplotlib.pyplot as plt
   import numpy as np
   import dataviz as dv

   rng = np.random.default_rng(0)
   values = rng.normal(size=500)

   fig, (left, right) = plt.subplots(1, 2, figsize=(10, 4))
   dv.histogram(values, ax=left, title="Distribution")
   dv.box_plot(values, ax=right, title="Spread")
   fig.tight_layout()

Plotly figures compose via :func:`plotly.subplots.make_subplots` or
``go.Figure(data=...)`` patterns; consult the Plotly documentation for the
exact incantation for the chart type you are combining.

Reproducibility
---------------

Reproducible plots require reproducible data, transformations, and styling:

* Pass an explicit ``seed=`` (or :class:`numpy.random.Generator`) to every
  bootstrap or sampling helper.
* Keep transformations (log, Box-Cox, winsorization) visible in analysis code
  rather than inside plotting calls.
* Inspect outlier flags before applying treatment.
* For SPC work, compute limits, detect rule violations, and render the chart
  in separate steps so each can be unit-tested and audited.
* Pin Matplotlib, Seaborn, and Plotly versions in your project's lockfile;
  default styling can shift between minor releases.

Performance
-----------

* Static rendering is typically faster than interactive rendering for
  ``n > 100_000`` because Matplotlib rasterizes inside the figure, whereas
  Plotly serializes the full dataset to JSON for the browser.
* For very large interactive scatter or line plots, consider downsampling or
  switching to ``plotly.graph_objects.Scattergl`` (WebGL backend).
* Heatmaps and pairplots scale super-linearly in column count; cap the number
  of columns or pre-compute correlations before plotting.

Error handling
--------------

DataViz raises standard Python exceptions:

* :class:`TypeError` — wrong input type (e.g., dict where Series is expected).
* :class:`ValueError` — empty input, all-NaN input, mismatched lengths, or
  out-of-domain parameter values.
* :class:`ImportError` — optional backend dependency missing (e.g., ``kaleido``
  for Plotly image export).

Every public function documents the conditions that trigger each exception in
the generated API reference.

Saving and exporting figures
----------------------------

.. code-block:: python

   ax.figure.savefig("chart.png", dpi=150, bbox_inches="tight")
   ax.figure.savefig("chart.pdf")
   ax.figure.savefig("chart.svg")

   fig.write_html("chart.html", include_plotlyjs="cdn")
   fig.write_image("chart.png")   # requires kaleido
   fig.write_json("chart.json")   # round-trippable Plotly figure

Embedding in notebooks and applications
---------------------------------------

* **Jupyter / JupyterLab** — both backends render inline by default.
* **VS Code** — set ``plotly.io.renderers.default = "vscode"`` once per
  session if Plotly figures do not appear.
* **Streamlit** — pass interactive figures to ``st.plotly_chart(fig)`` and
  static figures to ``st.pyplot(ax.figure)``.
* **Dash** — wrap interactive figures in ``dash.dcc.Graph(figure=fig)``.
* **Sphinx documentation** — embed static charts with the ``matplotlib``
  sphinx extension or by saving to ``_static/`` and using ``.. image::``.

Extending DataViz
-----------------

To add a new chart type:

1. Pick the most specific module (e.g., ``dataviz/bivariate/``) and add a new
   file named for the chart family.
2. Implement both variants with consistent parameters:

   .. code-block:: python

      def my_chart_static(...) -> plt.Axes:
          ...

      def my_chart_interactive(...) -> go.Figure:
          ...

3. Re-export both names from the module's ``__init__.py``.
4. Add a convenience alias (``my_chart = my_chart_static``) when it is
   unambiguous to do so.
5. Add tests for both variants under ``tests/<module>/``.
6. If the chart is a likely top-level entry point, re-export it from
   ``dataviz/__init__.py``.

Versioning and API stability
----------------------------

DataViz follows `Semantic Versioning 2.0.0 <https://semver.org/>`_:

* **Patch** (``0.1.x``) — bug fixes and documentation changes only.
* **Minor** (``0.x.0``) — backwards-compatible additions and deprecations.
* **Major** (``x.0.0``) — backwards-incompatible API changes.

Pre-1.0 releases reserve the right to refactor the public API; pin to an
exact version in production workloads.

How to cite
-----------

If you use DataViz in academic publications, technical reports, regulated
submissions, or applied analyses, please cite the project. Citations help
sustain maintenance time and improve the package for the wider community.

Preferred citation (BibTeX)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: _static/dataviz.bib
   :language: bibtex
   :caption: docs/source/_static/dataviz.bib

:download:`Download dataviz.bib <_static/dataviz.bib>`

CITATION.cff
~~~~~~~~~~~~

A machine-readable :file:`CITATION.cff` file is committed at the repository
root. GitHub renders a "Cite this repository" widget from it, and tools such
as Zenodo and Zotero consume it automatically. See the
`Citation File Format specification <https://citation-file-format.github.io/>`_
for details.

Author and ORCID
~~~~~~~~~~~~~~~~

* **Author**: Aned Esquerra-Arguelles
* **ORCID**: `0000-0003-1448-0407 <https://orcid.org/0000-0003-1448-0407>`_
* **Repository**: https://github.com/anedezquerra/data-viz
* **Documentation**: https://anedezquerra.github.io/data-viz/

Plain-text citation
~~~~~~~~~~~~~~~~~~~

   Esquerra-Arguelles, A. (2026). *DataViz: A comprehensive Python
   visualization package with static and interactive APIs* (Version 0.1.0)
   [Computer software]. https://github.com/anedezquerra/data-viz

License
-------

DataViz is released under the MIT License. See the ``LICENSE`` file at the
repository root for the full text.

Further reading
---------------

* :doc:`getting_started` — installation, quickstart, and troubleshooting.
* :doc:`examples` — end-to-end snippets per analysis domain.
* :doc:`api/modules` — generated API reference.
* :doc:`development` — documentation-build workflow.
* :doc:`changelog` — release history.
