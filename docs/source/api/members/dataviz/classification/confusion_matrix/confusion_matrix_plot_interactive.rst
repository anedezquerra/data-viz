dataviz.classification.confusion_matrix.confusion_matrix_plot_interactive
=========================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.confusion_matrix</p></div>

.. currentmodule:: dataviz.classification.confusion_matrix

.. autofunction:: confusion_matrix_plot_interactive

Use case
--------

Use for an explorable confusion matrix heatmap with hover values, e.g. in dashboards or notebooks.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.classification.confusion_matrix import (
       confusion_matrix_plot_interactive,
   )

   rng = np.random.default_rng(42)
   n = 160
   y_prob = np.clip(rng.beta(2, 4, n), 0.01, 0.99)
   y_true = (rng.uniform(size=n) < y_prob).astype(int)
   y_pred = (y_prob >= 0.35).astype(int)  # low threshold: fraud recall first
   cm = np.zeros((2, 2), dtype=int)
   for t, p in zip(y_true, y_pred):
       cm[t, p] += 1

   fig = confusion_matrix_plot_interactive(
       cm, labels=["legitimate", "fraud"],
       title="Fraud detector at 0.35 alert threshold",
       colorscale="Oranges",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/confusion_matrix/confusion_matrix_plot_interactive.png" alt="confusion_matrix_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
