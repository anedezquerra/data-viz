dataviz.multivariate.parallel.parallel_coordinates_static
=========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.multivariate.parallel</p></div>

.. currentmodule:: dataviz.multivariate.parallel

.. autofunction:: parallel_coordinates_static

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
   from dataviz.multivariate.parallel import parallel_coordinates_static

   rng = np.random.default_rng(42)
   n = 60
   df = pd.DataFrame({
       "Battery (h)": rng.normal(loc=12.0, scale=2.0, size=n),
       "Weight (g)": rng.normal(loc=180.0, scale=25.0, size=n),
       "Screen (in)": rng.normal(loc=6.1, scale=0.4, size=n),
       "Price (USD)": rng.normal(loc=700.0, scale=150.0, size=n),
       "Rating": rng.uniform(low=3.0, high=5.0, size=n),
   })

   ax = parallel_coordinates_static(
       df,
       title="Smartphone Model Comparison",
       alpha=0.4,
       linewidth=1.2,
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/multivariate/parallel/parallel_coordinates_static.png" alt="parallel_coordinates_static example output"><figcaption>Example output</figcaption></figure></div>
