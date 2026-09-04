dataviz.classification.calibration_extra.sharpness_resolution_decomposition_static
==================================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.calibration_extra</p></div>

.. currentmodule:: dataviz.classification.calibration_extra

.. autofunction:: sharpness_resolution_decomposition_static

Use case
--------

Use to decompose the Brier score into reliability, resolution and uncertainty to see why probability quality is poor.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.calibration_extra import (
       sharpness_resolution_decomposition_static,
   )

   rng = np.random.default_rng(9)
   n = 160
   y_prob = np.clip(rng.beta(2.5, 2.5, n), 0.01, 0.99)
   y_true = (rng.uniform(size=n) < y_prob).astype(int)

   ax = sharpness_resolution_decomposition_static(
       y_true, y_prob, n_bins=8,
       title="Readmission risk model: Murphy decomposition of Brier score",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/calibration_extra/sharpness_resolution_decomposition_static.png" alt="sharpness_resolution_decomposition_static example output"><figcaption>Example output</figcaption></figure></div>
