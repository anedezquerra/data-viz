dataviz.classification.fairness.per_segment_metric_bar_static
=============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.fairness</p></div>

.. currentmodule:: dataviz.classification.fairness

.. autofunction:: per_segment_metric_bar_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python


   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.fairness import per_segment_metric_bar_static

   rng = np.random.default_rng(42)
   groups = rng.choice(["Group A", "Group B"], size=200)
   y_prob = rng.beta(2.0, 5.0, size=200)
   y_true = rng.binomial(1, y_prob)
   y_pred = (y_prob > 0.3).astype(int)

   ax = per_segment_metric_bar_static(y_true, y_pred, groups)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/classification/fairness/per_segment_metric_bar_static.png" alt="per_segment_metric_bar_static example output"><figcaption>Example output</figcaption></figure></div>
