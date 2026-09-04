dataviz.classification.fairness.segment_calibration_overlay_static
==================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.fairness</p></div>

.. currentmodule:: dataviz.classification.fairness

.. autofunction:: segment_calibration_overlay_static

Use case
--------

Use to check whether probability calibration holds equally well across subgroups.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.fairness import segment_calibration_overlay_static

   rng = np.random.default_rng(61)
   n = 180
   groups = rng.choice(["app", "web", "branch"], size=n, p=[0.5, 0.3, 0.2])
   y_prob = np.clip(rng.beta(2, 3, n), 0.01, 0.99)
   bias = {"app": 0.0, "web": 0.05, "branch": -0.07}
   y_true = (rng.uniform(size=n)
             < np.clip(y_prob + np.array([bias[g] for g in groups]), 0, 1)
             ).astype(int)

   ax = segment_calibration_overlay_static(
       y_true, y_prob, groups, n_bins=6,
       title="Loan approval model: calibration by application channel",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/fairness/segment_calibration_overlay_static.png" alt="segment_calibration_overlay_static example output"><figcaption>Example output</figcaption></figure></div>
