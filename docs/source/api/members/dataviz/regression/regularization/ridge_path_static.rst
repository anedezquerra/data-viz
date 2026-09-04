dataviz.regression.regularization.ridge_path_static
===================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.regularization</p></div>

.. currentmodule:: dataviz.regression.regularization

.. autofunction:: ridge_path_static

Use case
--------

Use to see how coefficients shrink smoothly under ridge penalties when keeping all features in the model.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.regularization import ridge_path_static

   rng = np.random.default_rng(42)
   n = 32
   load = rng.normal(300, 55, n)
   sensors = pd.DataFrame({
       "bearing_temp_c": 55 + 0.09 * load + rng.normal(0, 1.5, n),
       "vibration_mms": 1.2 + 0.012 * load + rng.normal(0, 0.3, n),
       "oil_pressure_kpa": 420 - 0.35 * load + rng.normal(0, 9, n),
       "rpm": 1200 + 2.1 * load + rng.normal(0, 25, n),
       "ambient_c": rng.normal(22, 2.5, n),
   })
   energy_kwh = pd.Series(
       40 + 0.55 * sensors["bearing_temp_c"]
       + 6.0 * sensors["vibration_mms"] + rng.normal(0, 3, n),
       name="energy_kwh",
   )

   ax = ridge_path_static(
       sensors, energy_kwh, feature_names=list(sensors.columns), n_alphas=40,
       title="Turbine energy model: ridge coefficient path",
       cmap="tab10", theme="minimal",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/regularization/ridge_path_static.png" alt="ridge_path_static example output"><figcaption>Example output</figcaption></figure></div>
