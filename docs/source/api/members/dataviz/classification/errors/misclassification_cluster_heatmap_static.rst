dataviz.classification.errors.misclassification_cluster_heatmap_static
======================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.errors</p></div>

.. currentmodule:: dataviz.classification.errors

.. autofunction:: misclassification_cluster_heatmap_static

Use case
--------

Use to localize errors by true class and score bin, revealing where in the score range mistakes concentrate.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.errors import (
       misclassification_cluster_heatmap_static,
   )

   rng = np.random.default_rng(41)
   n = 170
   y_prob = np.clip(rng.beta(2, 2.5, n), 0.01, 0.99)
   noise = rng.normal(0, 0.25, n)
   y_true = (y_prob + noise > 0.55).astype(int)

   ax = misclassification_cluster_heatmap_static(
       y_true, y_prob, n_score_bins=8, threshold=0.5,
       title="Claims triage model: mistake rate by score band",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/errors/misclassification_cluster_heatmap_static.png" alt="misclassification_cluster_heatmap_static example output"><figcaption>Example output</figcaption></figure></div>
