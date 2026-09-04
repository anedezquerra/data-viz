dataviz.multivariate.charts.parallel_coordinates
================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.multivariate.charts</p></div>

.. currentmodule:: dataviz.multivariate.charts

.. autofunction:: parallel_coordinates

Use case
--------

Use to compare many observations across several numeric variables at once and spot multivariate outliers or clusters.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.multivariate.charts import parallel_coordinates

   rng = np.random.default_rng(42)
   n = 60
   df = pd.DataFrame({
       "Battery (h)": rng.normal(loc=12.0, scale=2.0, size=n),
       "Weight (g)": rng.normal(loc=180.0, scale=25.0, size=n),
       "Screen (in)": rng.normal(loc=6.1, scale=0.4, size=n),
       "Price (USD)": rng.normal(loc=700.0, scale=150.0, size=n),
       "Rating": rng.uniform(low=3.0, high=5.0, size=n),
   })

   ax = parallel_coordinates(df, title="Smartphone Model Comparison")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/multivariate/charts/parallel_coordinates.png" alt="parallel_coordinates example output"><figcaption>Example output</figcaption></figure></div>
