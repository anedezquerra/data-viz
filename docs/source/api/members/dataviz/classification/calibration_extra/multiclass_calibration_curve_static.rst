dataviz.classification.calibration_extra.multiclass_calibration_curve_static
============================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.calibration_extra</p></div>

.. currentmodule:: dataviz.classification.calibration_extra

.. autofunction:: multiclass_calibration_curve_static

Use case
--------

Use to audit one-vs-rest calibration per class in a multiclass problem, one reliability panel per class.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.calibration_extra import (
       multiclass_calibration_curve_static,
   )

   rng = np.random.default_rng(3)
   n = 180
   y_true = rng.choice(3, size=n, p=[0.5, 0.3, 0.2])
   logits = rng.normal(0, 1.0, (n, 3))
   logits[np.arange(n), y_true] += 2.0
   y_prob_matrix = np.exp(logits) / np.exp(logits).sum(axis=1, keepdims=True)

   axes = multiclass_calibration_curve_static(
       y_true, y_prob_matrix,
       labels=["standard", "premium", "enterprise"], n_bins=6,
       title="Subscription tier classifier: per-class calibration",
   )
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/calibration_extra/multiclass_calibration_curve_static.png" alt="multiclass_calibration_curve_static example output"><figcaption>Example output</figcaption></figure></div>
