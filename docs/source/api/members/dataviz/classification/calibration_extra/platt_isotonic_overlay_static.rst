dataviz.classification.calibration_extra.platt_isotonic_overlay_static
======================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.calibration_extra</p></div>

.. currentmodule:: dataviz.classification.calibration_extra

.. autofunction:: platt_isotonic_overlay_static

Use case
--------

Use when choosing a recalibration method by comparing raw, Platt-scaled and isotonic mappings against binned observations.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.calibration_extra import platt_isotonic_overlay_static

   rng = np.random.default_rng(5)
   n = 150
   signal = rng.normal(0, 1.5, n)
   y_true = (signal + rng.normal(0, 0.8, n) > 0).astype(int)
   y_prob = 1.0 / (1.0 + np.exp(-2.5 * signal))  # over-confident raw scores
   y_prob = np.clip(y_prob, 1e-4, 1 - 1e-4)

   ax = platt_isotonic_overlay_static(
       y_true, y_prob, n_bins=10,
       title="SVM spam filter: Platt vs isotonic recalibration",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/calibration_extra/platt_isotonic_overlay_static.png" alt="platt_isotonic_overlay_static example output"><figcaption>Example output</figcaption></figure></div>
