dataviz.classification.fairness.segment_roc_overlay_static
==========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.fairness</p></div>

.. currentmodule:: dataviz.classification.fairness

.. autofunction:: segment_roc_overlay_static

Use case
--------

Use to expose ranking-performance disparity by overlaying one ROC curve per subgroup.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.fairness import segment_roc_overlay_static

   rng = np.random.default_rng(59)
   n = 180
   groups = rng.choice(["north", "south", "west"], size=n, p=[0.4, 0.35, 0.25])
   sep = {"north": 0.9, "south": 0.7, "west": 0.45}  # weaker signal out west
   y_true = (rng.uniform(size=n) < 0.35).astype(int)
   y_score = np.array([
       rng.normal(sep[g], 0.55) if t == 1 else rng.normal(0.0, 0.55)
       for g, t in zip(groups, y_true)
   ])

   ax = segment_roc_overlay_static(
       y_true, y_score, groups,
       title="Fraud model ROC by region: disparity check",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/fairness/segment_roc_overlay_static.png" alt="segment_roc_overlay_static example output"><figcaption>Example output</figcaption></figure></div>
