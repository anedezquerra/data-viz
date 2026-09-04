dataviz.classification.score_dist.score_distribution_by_class_static
====================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.score_dist</p></div>

.. currentmodule:: dataviz.classification.score_dist

.. autofunction:: score_distribution_by_class_static

Use case
--------

Use to check score separation between true classes; violin, box, or strip views reveal overlap that limits any threshold.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.score_dist import score_distribution_by_class_static

   rng = np.random.default_rng(42)
   # credit-default scorecard: score spread for defaulters vs payers
   n = 160
   is_default = (rng.random(n) < 0.25).astype(int)
   y_true = np.where(is_default == 1, "defaulter", "payer")
   y_score = np.clip(
       is_default * rng.beta(6, 3, n) + (1 - is_default) * rng.beta(3, 6, n), 0, 1)

   ax = score_distribution_by_class_static(
       y_true, y_score, labels=["payer", "defaulter"], kind="violin",
       title="Credit scorecard: score distribution by outcome")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/score_dist/score_distribution_by_class_static.png" alt="score_distribution_by_class_static example output"><figcaption>Example output</figcaption></figure></div>
