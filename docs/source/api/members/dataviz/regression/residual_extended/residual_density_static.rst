dataviz.regression.residual_extended.residual_density_static
============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.residual_extended</p></div>

.. currentmodule:: dataviz.regression.residual_extended

.. autofunction:: residual_density_static

Use case
--------

Use to assess the shape of the residual distribution with a smooth kernel-density estimate.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.residual_extended import residual_density_static

   rng = np.random.default_rng(42)
   flights = pd.Series(np.arange(1, 51), name="flight")
   actual_delay = pd.Series(rng.normal(12, 18, 50).round(1), name="actual_delay_min")
   predicted_delay = pd.Series(
       actual_delay + rng.laplace(0, 6, 50), name="predicted_delay_min"
   )

   ax = residual_density_static(
       actual_delay, predicted_delay, bandwidth=4.0,
       title="Flight delay model: residual kernel density",
       color="#6a4c93", fill_alpha=0.35, theme="minimal",
   )
   ax.set_xlabel("Residual (min)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/residual_extended/residual_density_static.png" alt="residual_density_static example output"><figcaption>Example output</figcaption></figure></div>
