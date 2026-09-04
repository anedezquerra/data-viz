dataviz.bivariate.charts.correlation_heatmap
============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.charts</p></div>

.. currentmodule:: dataviz.bivariate.charts

.. autofunction:: correlation_heatmap

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
   from dataviz.bivariate.charts import correlation_heatmap

   rng = np.random.default_rng(42)
   n = 80
   speed = rng.normal(loc=120.0, scale=6.0, size=n)
   df = pd.DataFrame({
       "Speed": speed,
       "Pressure": 40.0 + 0.3 * speed + rng.normal(loc=0.0, scale=2.0, size=n),
       "Temperature": rng.normal(loc=180.0, scale=5.0, size=n),
       "Yield": 95.0 - 0.2 * speed + rng.normal(loc=0.0, scale=1.5, size=n),
   })

   ax = correlation_heatmap(df, method="spearman", mask_upper=True, title="Process Variable Correlations")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/charts/correlation_heatmap.png" alt="correlation_heatmap example output"><figcaption>Example output</figcaption></figure></div>
