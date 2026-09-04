dataviz.bivariate.stats.lag_plot_static
=======================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.stats</p></div>

.. currentmodule:: dataviz.bivariate.stats

.. autofunction:: lag_plot_static

Use case
--------

Use to check for delayed or leading-lag relationships between two ordered series, such as time-shifted signals.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.bivariate.stats import lag_plot_static

   rng = np.random.default_rng(42)
   n = 100
   noise = rng.normal(loc=0.0, scale=1.0, size=n)
   flow = pd.Series(np.zeros(n), name="River flow (m3/s)")
   for i in range(1, n):
       flow.iloc[i] = 0.85 * flow.iloc[i - 1] + noise[i]

   ax = lag_plot_static(
       flow,
       flow,
       lag=1,
       title="River Flow Lag-1 Autocorrelation",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/stats/lag_plot_static.png" alt="lag_plot_static example output"><figcaption>Example output</figcaption></figure></div>
