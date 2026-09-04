dataviz.classification.fairness.fairness_disparity_heatmap_static
=================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.fairness</p></div>

.. currentmodule:: dataviz.classification.fairness

.. autofunction:: fairness_disparity_heatmap_static

Use case
--------

Use to spot which groups deviate from the population mean on fairness metrics such as TPR or selection rate.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.fairness import fairness_disparity_heatmap_static

   rng = np.random.default_rng(53)
   n = 180
   groups = rng.choice(["group A", "group B", "group C"], size=n,
                       p=[0.5, 0.3, 0.2])
   shift = {"group A": 0.08, "group B": 0.0, "group C": -0.10}
   y_prob = np.clip(0.5 + np.array([shift[g] for g in groups])
                    + rng.normal(0, 0.22, n), 0.02, 0.98)
   y_true = (rng.uniform(size=n) < y_prob).astype(int)
   y_pred = (y_prob >= 0.5).astype(int)

   ax = fairness_disparity_heatmap_static(
       y_true, y_pred, groups,
       title="Hiring screen: deviation from population mean per group",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/fairness/fairness_disparity_heatmap_static.png" alt="fairness_disparity_heatmap_static example output"><figcaption>Example output</figcaption></figure></div>
