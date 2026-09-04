dataviz.regression.residual_features.residual_vs_feature_static
===============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.residual_features</p></div>

.. currentmodule:: dataviz.regression.residual_features

.. autofunction:: residual_vs_feature_static

Use case
--------

Use to check whether a single feature still carries structure the model missed; a curved trend in residuals vs that feature signals nonlinearity or a missing interaction.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.residual_features import residual_vs_feature_static

   rng = np.random.default_rng(42)
   n = 40
   listings = pd.DataFrame({
       "sqft": rng.uniform(800, 3600, n),
   })
   noise = rng.normal(0, 18, n)
   price = 60 + 0.22 * listings["sqft"] + 0.00003 * listings["sqft"] ** 2 + noise
   y_pred = 70 + 0.26 * listings["sqft"]  # linear model misses curvature

   ax = residual_vs_feature_static(
       listings["sqft"], price, y_pred,
       feature_name="Living area (sqft)",
       title="Home pricing model: residuals vs living area",
       trend_color="#e45756",
   )
   ax.set_xlabel("Living area (sqft)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/residual_features/residual_vs_feature_static.png" alt="residual_vs_feature_static example output"><figcaption>Example output</figcaption></figure></div>
