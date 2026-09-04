dataviz.regression.residual_features.partial_residual_plot_static
=================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.residual_features</p></div>

.. currentmodule:: dataviz.regression.residual_features

.. autofunction:: partial_residual_plot_static

Use case
--------

Use to inspect the marginal effect of one predictor in an OLS fit while adjusting for the others; curvature suggests the feature needs a nonlinear term.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.residual_features import partial_residual_plot_static

   rng = np.random.default_rng(42)
   n = 35
   cars = pd.DataFrame({
       "horsepower": rng.uniform(90, 320, n),
       "weight_kg": rng.uniform(900, 2100, n),
       "age_years": rng.uniform(0, 12, n),
   })
   mpg = (52 - 0.045 * cars["horsepower"] - 0.008 * cars["weight_kg"]
          - 0.6 * cars["age_years"] + rng.normal(0, 1.5, n))

   ax = partial_residual_plot_static(
       cars, mpg, feature_index=0, feature_name="horsepower",
       title="Fuel economy study: partial residual for horsepower",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/residual_features/partial_residual_plot_static.png" alt="partial_residual_plot_static example output"><figcaption>Example output</figcaption></figure></div>
