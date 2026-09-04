dataviz.regression.multicollinearity.condition_index_plot_static
================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.multicollinearity</p></div>

.. currentmodule:: dataviz.regression.multicollinearity

.. autofunction:: condition_index_plot_static

Use case
--------

Use to detect near-collinearity in the design matrix via condition indices, complementing per-feature VIF checks.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.multicollinearity import condition_index_plot_static

   rng = np.random.default_rng(42)
   n = 36
   engine_size = rng.normal(2.4, 0.6, n)
   vehicles = pd.DataFrame({
       "engine_l": engine_size,
       "horsepower": 95 * engine_size + rng.normal(0, 12, n),
       "weight_kg": 620 * engine_size + rng.normal(0, 90, n),
       "wheelbase_in": rng.normal(104, 6, n),
   })

   ax = condition_index_plot_static(
       vehicles, title="Fuel-efficiency model: condition indices",
       threshold=30.0, color="#ee854a", theme="minimal",
   )
   ax.set_ylabel("Condition index")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/multicollinearity/condition_index_plot_static.png" alt="condition_index_plot_static example output"><figcaption>Example output</figcaption></figure></div>
