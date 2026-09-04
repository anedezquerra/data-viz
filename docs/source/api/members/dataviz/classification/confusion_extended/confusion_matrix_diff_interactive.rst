dataviz.classification.confusion_extended.confusion_matrix_diff_interactive
===========================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.confusion_extended</p></div>

.. currentmodule:: dataviz.classification.confusion_extended

.. autofunction:: confusion_matrix_diff_interactive

Use case
--------

Compare two models by plotting the element-wise difference of their confusion matrices to see where errors shift.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.classification.confusion_extended import (
       confusion_matrix_diff_interactive,
   )

   rng = np.random.default_rng(19)
   n = 160
   true_labels = rng.choice(2, size=n, p=[0.7, 0.3])


   def make_cm(error_rate):
       preds = true_labels.copy()
       flips = rng.uniform(size=n) < error_rate
       preds[flips] = 1 - preds[flips]
       m = np.zeros((2, 2), dtype=int)
       for t, p in zip(true_labels, preds):
           m[t, p] += 1
       return m


   cm_new = make_cm(0.12)
   cm_baseline = make_cm(0.25)

   fig = confusion_matrix_diff_interactive(
       cm_new, cm_baseline, labels=["no-churn", "churn"],
       title="New churn model minus baseline (positive = improvement)",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/confusion_extended/confusion_matrix_diff_interactive.png" alt="confusion_matrix_diff_interactive example output"><figcaption>Example output</figcaption></figure></div>
