dataviz.regression.multicollinearity.eigenvalue_scree_predictors_static
=======================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.multicollinearity</p></div>

.. currentmodule:: dataviz.regression.multicollinearity

.. autofunction:: eigenvalue_scree_predictors_static

Use case
--------

Use to see how much predictor variance concentrates in a few components, a sign of multicollinearity.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.multicollinearity import eigenvalue_scree_predictors_static

   rng = np.random.default_rng(42)
   n = 40
   size = rng.normal(2000, 500, n)
   homes = pd.DataFrame({
       "sqft": size,
       "bedrooms": size / 480 + rng.normal(0, 0.4, n),
       "bathrooms": size / 750 + rng.normal(0, 0.3, n),
       "garage_cars": np.clip(size / 900 + rng.normal(0, 0.3, n), 0, 4),
       "lot_sqft": rng.normal(7000, 1800, n),
   })

   ax = eigenvalue_scree_predictors_static(
       homes, title="Home appraisal model: predictor eigenvalue scree",
       color="#6acc64", theme="minimal",
   )
   ax.set_ylabel("Eigenvalue")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/multicollinearity/eigenvalue_scree_predictors_static.png" alt="eigenvalue_scree_predictors_static example output"><figcaption>Example output</figcaption></figure></div>
