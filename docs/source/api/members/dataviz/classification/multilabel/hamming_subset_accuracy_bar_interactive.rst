dataviz.classification.multilabel.hamming_subset_accuracy_bar_interactive
=========================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.multilabel</p></div>

.. currentmodule:: dataviz.classification.multilabel

.. autofunction:: hamming_subset_accuracy_bar_interactive

Use case
--------

Use to contrast lenient Hamming accuracy with strict exact-subset accuracy when summarizing a multilabel model.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.multilabel import hamming_subset_accuracy_bar_interactive

   rng = np.random.default_rng(42)
   # multilabel movie tagger: per-tag accuracy vs exact full-tag-set accuracy
   n, n_labels = 120, 5
   Y_true = (rng.random((n, n_labels)) < 0.3).astype(int)
   noise = rng.random((n, n_labels)) < 0.09
   Y_pred = np.where(noise, 1 - Y_true, Y_true)

   fig = hamming_subset_accuracy_bar_interactive(
       Y_true, Y_pred, title="Movie tagger: Hamming vs subset accuracy")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/multilabel/hamming_subset_accuracy_bar_interactive.png" alt="hamming_subset_accuracy_bar_interactive example output"><figcaption>Example output</figcaption></figure></div>
