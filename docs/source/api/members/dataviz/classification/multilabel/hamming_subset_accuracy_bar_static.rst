dataviz.classification.multilabel.hamming_subset_accuracy_bar_static
====================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.multilabel</p></div>

.. currentmodule:: dataviz.classification.multilabel

.. autofunction:: hamming_subset_accuracy_bar_static

Use case
--------

Use to contrast lenient Hamming accuracy with strict exact-subset accuracy when summarizing a multilabel model.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.multilabel import hamming_subset_accuracy_bar_static

   rng = np.random.default_rng(42)
   # multilabel movie tagger: per-tag accuracy vs exact full-tag-set accuracy
   n, n_labels = 120, 5
   Y_true = (rng.random((n, n_labels)) < 0.3).astype(int)
   noise = rng.random((n, n_labels)) < 0.09
   Y_pred = np.where(noise, 1 - Y_true, Y_true)

   ax = hamming_subset_accuracy_bar_static(
       Y_true, Y_pred, title="Movie tagger: Hamming vs subset accuracy")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/multilabel/hamming_subset_accuracy_bar_static.png" alt="hamming_subset_accuracy_bar_static example output"><figcaption>Example output</figcaption></figure></div>
