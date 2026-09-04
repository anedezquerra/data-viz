dataviz.classification.threshold_extra.mcc_curve_static
=======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.threshold_extra</p></div>

.. currentmodule:: dataviz.classification.threshold_extra

.. autofunction:: mcc_curve_static

Use case
--------

Use to choose a threshold with a balanced single-number quality score; MCC vs threshold with the argmax marked.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.threshold_extra import mcc_curve_static

   rng = np.random.default_rng(42)
   # rare-event churn alert: MCC stays informative under imbalance
   n = 150
   y_true = (rng.random(n) < 0.15).astype(int)
   y_prob = np.clip(
       y_true * rng.beta(6, 2, n) + (1 - y_true) * rng.beta(2, 6, n), 0, 1)

   ax = mcc_curve_static(y_true, y_prob,
                         title="Churn alert: MCC vs threshold")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/threshold_extra/mcc_curve_static.png" alt="mcc_curve_static example output"><figcaption>Example output</figcaption></figure></div>
