dataviz.bivariate.trends.errorbar_plot_static
=============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.trends</p></div>

.. currentmodule:: dataviz.bivariate.trends

.. autofunction:: errorbar_plot_static

Use case
--------

Use to compare group means with uncertainty intervals along an ordered or categorical x axis.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.bivariate.trends import errorbar_plot_static

   rng = np.random.default_rng(42)
   dose = pd.Series(np.arange(0, 11, 2), name="Fertilizer dose (kg/ha)")
   mean_yield = pd.Series(2.5 + 0.6 * dose - 0.03 * dose**2, name="Mean yield (t/ha)")
   yield_std = pd.Series(rng.uniform(low=0.15, high=0.35, size=len(dose)), name="Yield SD")

   ax = errorbar_plot_static(
       dose,
       mean_yield,
       yerr=yield_std,
       title="Crop Yield Response to Fertilizer",
       color="darkgreen",
       capsize=5.0,
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/trends/errorbar_plot_static.png" alt="errorbar_plot_static example output"><figcaption>Example output</figcaption></figure></div>
