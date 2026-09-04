dataviz.classification.threshold.det_curve_static
=================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.threshold</p></div>

.. currentmodule:: dataviz.classification.threshold

.. autofunction:: det_curve_static

Use case
--------

Use for detection or biometric systems; plots FNR vs FPR on a probit scale to spread out low-error operating regions.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.threshold import det_curve_static

   rng = np.random.default_rng(42)
   # biometric access system: DET curve on a probit scale
   n = 150
   y_true = (rng.random(n) < 0.4).astype(int)
   y_prob = np.clip(
       y_true * rng.beta(7, 2.5, n) + (1 - y_true) * rng.beta(2.5, 7, n), 0, 1)

   ax = det_curve_static(y_true, y_prob,
                         title="Access system: detection-error tradeoff")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/threshold/det_curve_static.png" alt="det_curve_static example output"><figcaption>Example output</figcaption></figure></div>
