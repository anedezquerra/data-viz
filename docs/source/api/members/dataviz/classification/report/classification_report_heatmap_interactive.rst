dataviz.classification.report.classification_report_heatmap_interactive
=======================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.report</p></div>

.. currentmodule:: dataviz.classification.report

.. autofunction:: classification_report_heatmap_interactive

Use case
--------

Use to replace a text classification report with a scannable heatmap of per-class precision, recall, and F1.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.report import classification_report_heatmap_interactive

   rng = np.random.default_rng(42)
   # 4-class land-cover classifier on satellite tiles
   n = 160
   labels = ["forest", "water", "urban", "crops"]
   y_true = np.array([labels[i] for i in rng.integers(0, 4, n)])
   err = rng.random(n) < 0.15
   y_pred = y_true.copy()
   y_pred[err] = np.array([labels[i] for i in rng.integers(0, 4, err.sum())])

   fig = classification_report_heatmap_interactive(
       y_true, y_pred, labels=labels,
       title="Land-cover classifier: per-class report")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/report/classification_report_heatmap_interactive.png" alt="classification_report_heatmap_interactive example output"><figcaption>Example output</figcaption></figure></div>
