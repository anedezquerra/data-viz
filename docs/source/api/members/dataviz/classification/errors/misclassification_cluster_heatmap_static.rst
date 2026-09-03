dataviz.classification.errors.misclassification_cluster_heatmap_static
======================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.errors</p></div>

.. currentmodule:: dataviz.classification.errors

.. autofunction:: misclassification_cluster_heatmap_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python


   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.errors import misclassification_cluster_heatmap_static

   rng = np.random.default_rng(42)
   y_prob = rng.beta(2.0, 5.0, size=200)
   y_true = rng.binomial(1, y_prob)

   ax = misclassification_cluster_heatmap_static(y_true, y_prob)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/classification/errors/misclassification_cluster_heatmap_static.png" alt="misclassification_cluster_heatmap_static example output"><figcaption>Example output</figcaption></figure></div>
