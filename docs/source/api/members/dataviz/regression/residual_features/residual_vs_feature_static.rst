dataviz.regression.residual_features.residual_vs_feature_static
===============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.residual_features</p></div>

.. currentmodule:: dataviz.regression.residual_features

.. autofunction:: residual_vs_feature_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.residual_features import residual_vs_feature_static

   rng = np.random.default_rng(42)
   feature = rng.normal(0.0, 1.0, size=60)
   y_true = 10 + 2 * feature + rng.normal(0.0, 1.0, size=60)
   y_pred = y_true + rng.normal(0.0, 0.5, size=60)

   ax = residual_vs_feature_static(feature, y_true, y_pred, feature_name="x1")
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/regression/residual_features/residual_vs_feature_static.png" alt="residual_vs_feature_static example output"><figcaption>Example output</figcaption></figure></div>
