dataviz.regression.effects.partial_dependence_regression_static
===============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.effects</p></div>

.. currentmodule:: dataviz.regression.effects

.. autofunction:: partial_dependence_regression_static

Use case
--------

Use to show the marginal effect of one feature on the predicted target, averaged over all other features.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.effects import partial_dependence_regression_static

   grid = pd.Series(np.linspace(500, 4000, 25), name="sqft")
   pd_values = pd.Series(60 + 0.09 * grid + 12 * np.log(grid / 500),
                         name="pd_price_k")

   ax = partial_dependence_regression_static(
       grid, pd_values,
       title="Partial Dependence: Living Area on Price",
       feature_name="living area (sqft)", color="#1f6fb2")
   ax.set_ylabel("Predicted price (k USD)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/effects/partial_dependence_regression_static.png" alt="partial_dependence_regression_static example output"><figcaption>Example output</figcaption></figure></div>
