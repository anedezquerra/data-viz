dataviz.classification.fairness.segment_roc_overlay_static
==========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.fairness</p></div>

.. currentmodule:: dataviz.classification.fairness

.. autofunction:: segment_roc_overlay_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python


   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.fairness import segment_roc_overlay_static

   rng = np.random.default_rng(42)
   groups = rng.choice(["Group A", "Group B"], size=200)
   y_score = rng.beta(2.0, 5.0, size=200)
   y_true = rng.binomial(1, y_score)

   ax = segment_roc_overlay_static(y_true, y_score, groups)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/classification/fairness/segment_roc_overlay_static.png" alt="segment_roc_overlay_static example output"><figcaption>Example output</figcaption></figure></div>
