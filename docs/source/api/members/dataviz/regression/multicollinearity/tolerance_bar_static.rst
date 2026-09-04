dataviz.regression.multicollinearity.tolerance_bar_static
=========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.multicollinearity</p></div>

.. currentmodule:: dataviz.regression.multicollinearity

.. autofunction:: tolerance_bar_static

Use case
--------

Use to flag predictors with low tolerance (1/VIF), the reciprocal view of variance inflation.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.multicollinearity import tolerance_bar_static

   rng = np.random.default_rng(42)
   n = 36
   load = rng.normal(320, 60, n)
   plant = pd.DataFrame({
       "throughput_tph": load,
       "conveyor_speed": 0.9 * load / 60 + rng.normal(0, 0.15, n),
       "motor_current_a": 0.45 * load + rng.normal(0, 8, n),
       "ambient_temp_c": rng.normal(24, 3, n),
       "operator_experience_yr": rng.uniform(0.5, 20, n),
   })

   ax = tolerance_bar_static(
       plant, feature_names=list(plant.columns),
       title="Plant throughput model: predictor tolerance",
       threshold=0.2, color="#d65f5f", theme="minimal",
   )
   ax.set_ylabel("Tolerance (1/VIF)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/multicollinearity/tolerance_bar_static.png" alt="tolerance_bar_static example output"><figcaption>Example output</figcaption></figure></div>
