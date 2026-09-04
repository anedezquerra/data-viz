dataviz.regression.multicollinearity.vif_bar_static
===================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.multicollinearity</p></div>

.. currentmodule:: dataviz.regression.multicollinearity

.. autofunction:: vif_bar_static

Use case
--------

Use to flag predictors whose variance inflation factor exceeds a threshold before fitting a linear model.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.multicollinearity import vif_bar_static

   rng = np.random.default_rng(42)
   n = 36
   living_area = rng.normal(1800, 400, n)
   housing = pd.DataFrame({
       "living_area_sqft": living_area,
       "bedrooms": np.clip(living_area / 450 + rng.normal(0, 0.4, n), 1, 6),
       "bathrooms": np.clip(living_area / 700 + rng.normal(0, 0.3, n), 1, 4),
       "lot_size_sqft": rng.normal(6000, 1500, n),
       "age_years": rng.uniform(0, 60, n),
   })

   ax = vif_bar_static(
       housing, feature_names=list(housing.columns),
       title="Housing price model: variance inflation factors",
       threshold=5.0, color="#4878d0", theme="minimal",
   )
   ax.set_ylabel("VIF")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/multicollinearity/vif_bar_static.png" alt="vif_bar_static example output"><figcaption>Example output</figcaption></figure></div>
