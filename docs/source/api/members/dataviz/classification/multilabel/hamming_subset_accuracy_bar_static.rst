dataviz.classification.multilabel.hamming_subset_accuracy_bar_static
====================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.multilabel</p></div>

.. currentmodule:: dataviz.classification.multilabel

.. autofunction:: hamming_subset_accuracy_bar_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python


   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.multilabel import hamming_subset_accuracy_bar_static

   rng = np.random.default_rng(42)
   Y_true = rng.binomial(1, 0.4, size=(120, 4))
   Y_pred = rng.binomial(1, 0.4, size=(120, 4))

   ax = hamming_subset_accuracy_bar_static(Y_true, Y_pred)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/classification/multilabel/hamming_subset_accuracy_bar_static.png" alt="hamming_subset_accuracy_bar_static example output"><figcaption>Example output</figcaption></figure></div>
