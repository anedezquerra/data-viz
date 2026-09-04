dataviz.regression.var_engineering.feature_target_correlation_bar_static
========================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.var_engineering</p></div>

.. currentmodule:: dataviz.regression.var_engineering

.. autofunction:: feature_target_correlation_bar_static

Use case
--------

Use to rank features by Pearson correlation with the target, sorted by magnitude, as a quick univariate screen before modeling.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.var_engineering import feature_target_correlation_bar_static

   rng = np.random.default_rng(42)
   n = 50
   temp = rng.uniform(15, 35, n)
   humidity = rng.uniform(20, 95, n)
   wind = rng.uniform(0, 40, n)
   pressure = rng.uniform(1005, 1025, n)
   rentals = 30 + 4.2 * temp - 0.9 * humidity + rng.normal(0, 12, n)
   X = pd.DataFrame({
       "temperature": temp, "humidity": humidity,
       "wind_speed": wind, "pressure": pressure,
   })

   ax = feature_target_correlation_bar_static(
       X, rentals, feature_names=list(X.columns),
       title="Bike-share demand: feature-target Pearson correlations",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/var_engineering/feature_target_correlation_bar_static.png" alt="feature_target_correlation_bar_static example output"><figcaption>Example output</figcaption></figure></div>
