dataviz.classification.calibration_extra.multiclass_calibration_curve_static
============================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.calibration_extra</p></div>

.. currentmodule:: dataviz.classification.calibration_extra

.. autofunction:: multiclass_calibration_curve_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python


   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.calibration_extra import multiclass_calibration_curve_static

   rng = np.random.default_rng(42)
   logits = rng.normal(size=(200, 3))
   exp_logits = np.exp(logits - logits.max(axis=1, keepdims=True))
   y_prob_matrix = exp_logits / exp_logits.sum(axis=1, keepdims=True)
   y_true = rng.choice(3, size=200, p=[0.4, 0.35, 0.25])

   ax = multiclass_calibration_curve_static(y_true, y_prob_matrix, labels=["A", "B", "C"])
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/classification/calibration_extra/multiclass_calibration_curve_static.png" alt="multiclass_calibration_curve_static example output"><figcaption>Example output</figcaption></figure></div>
