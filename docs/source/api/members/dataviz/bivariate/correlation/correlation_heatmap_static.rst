dataviz.bivariate.correlation.correlation_heatmap_static
========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.correlation</p></div>

.. currentmodule:: dataviz.bivariate.correlation

.. autofunction:: correlation_heatmap_static

Use case
--------

Use to scan pairwise correlations among dataframe columns and quickly find strongly related variable pairs.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.bivariate.correlation import correlation_heatmap_static

   rng = np.random.default_rng(42)
   n = 80
   speed = rng.normal(loc=120.0, scale=6.0, size=n)
   df = pd.DataFrame({
       "Speed": speed,
       "Pressure": 40.0 + 0.3 * speed + rng.normal(loc=0.0, scale=2.0, size=n),
       "Temperature": rng.normal(loc=180.0, scale=5.0, size=n),
       "Yield": 95.0 - 0.2 * speed + rng.normal(loc=0.0, scale=1.5, size=n),
   })

   ax, corr = correlation_heatmap_static(
       df,
       method="spearman",
       mask_upper=True,
       return_corr=True,
       title="Process Variable Correlations",
   )
   print(corr.round(2))
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/correlation/correlation_heatmap_static.png" alt="correlation_heatmap_static example output"><figcaption>Example output</figcaption></figure></div>
