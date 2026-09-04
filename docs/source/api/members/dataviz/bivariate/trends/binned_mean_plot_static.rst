dataviz.bivariate.trends.binned_mean_plot_static
================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.trends</p></div>

.. currentmodule:: dataviz.bivariate.trends

.. autofunction:: binned_mean_plot_static

Use case
--------

Use to smooth noisy scatter data into mean y values per x bin and reveal the underlying trend.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.bivariate.trends import binned_mean_plot_static

   rng = np.random.default_rng(42)
   n = 160
   depth = pd.Series(rng.uniform(low=0.0, high=200.0, size=n), name="Depth (m)")
   temperature = pd.Series(25.0 - 0.08 * depth + rng.normal(loc=0.0, scale=1.5, size=n), name="Water temperature (C)")

   ax = binned_mean_plot_static(
       depth,
       temperature,
       bins=8,
       title="Mean Water Temperature by Depth Bin",
       color="darkcyan",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/trends/binned_mean_plot_static.png" alt="binned_mean_plot_static example output"><figcaption>Example output</figcaption></figure></div>
