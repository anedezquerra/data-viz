dataviz.classification.calibration.calibration_curve_static
===========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.calibration</p></div>

.. currentmodule:: dataviz.classification.calibration

.. autofunction:: calibration_curve_static

Use case
--------

Use to check whether predicted probabilities match observed frequencies, e.g. before trusting scores as risk estimates.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.calibration import calibration_curve_static

   rng = np.random.default_rng(42)
   n = 160
   churn_risk = rng.normal(5.0, 1.5, n)
   y_prob = 1.0 / (1.0 + np.exp(-(churn_risk - 5.0)))
   y_true = (rng.uniform(size=n) < np.clip(y_prob + 0.08, 0, 1)).astype(int)

   ax = calibration_curve_static(
       y_true, y_prob, n_bins=8, strategy="quantile",
       title="Telco churn model: reliability diagram",
   )
   ax.set_xlabel("Predicted churn probability")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/calibration/calibration_curve_static.png" alt="calibration_curve_static example output"><figcaption>Example output</figcaption></figure></div>
