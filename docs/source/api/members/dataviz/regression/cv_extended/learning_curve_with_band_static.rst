dataviz.regression.cv_extended.learning_curve_with_band_static
==============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.cv_extended</p></div>

.. currentmodule:: dataviz.regression.cv_extended

.. autofunction:: learning_curve_with_band_static

Use case
--------

Use to show mean CV score versus training size with a plus/minus std band, revealing both bias and variance as data grows.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.cv_extended import learning_curve_with_band_static

   train_sizes = np.array([25, 50, 75, 100, 125, 150])
   mean_rmse = np.array([18.5, 14.2, 12.1, 11.0, 10.4, 10.1])
   std_rmse = np.array([3.1, 2.2, 1.7, 1.4, 1.2, 1.1])

   ax = learning_curve_with_band_static(
       train_sizes, mean_rmse, std_rmse,
       title="Cycle-Time Model: Learning Curve (5-fold CV)",
       metric_name="RMSE (seconds)", color="#1f6fb2")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/cv_extended/learning_curve_with_band_static.png" alt="learning_curve_with_band_static example output"><figcaption>Example output</figcaption></figure></div>
