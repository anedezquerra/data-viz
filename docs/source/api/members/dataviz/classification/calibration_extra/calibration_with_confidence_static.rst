dataviz.classification.calibration_extra.calibration_with_confidence_static
===========================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.calibration_extra</p></div>

.. currentmodule:: dataviz.classification.calibration_extra

.. autofunction:: calibration_with_confidence_static

Use case
--------

Use when a plain reliability diagram is ambiguous on small data; bootstrap bands show whether deviations are significant.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.calibration_extra import (
       calibration_with_confidence_static,
   )

   rng = np.random.default_rng(21)
   n = 140
   y_prob = np.clip(rng.beta(2, 3, n), 0.01, 0.99)
   y_true = (rng.uniform(size=n) < y_prob).astype(int)

   ax = calibration_with_confidence_static(
       y_true, y_prob, n_bins=8, n_bootstrap=200, ci=0.90,
       title="Loan default model: calibration with 90% bootstrap CI",
       random_state=42,
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/calibration_extra/calibration_with_confidence_static.png" alt="calibration_with_confidence_static example output"><figcaption>Example output</figcaption></figure></div>
