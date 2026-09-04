dataviz.multivariate.charts.pairplot
====================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.multivariate.charts</p></div>

.. currentmodule:: dataviz.multivariate.charts

.. autofunction:: pairplot

Use case
--------

Use to survey all pairwise relationships and marginal distributions among several variables in one grid.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.multivariate.charts import pairplot

   rng = np.random.default_rng(42)
   n = 80
   horsepower = rng.normal(loc=150.0, scale=30.0, size=n)
   df = pd.DataFrame({
       "Horsepower": horsepower,
       "Weight (kg)": 1200.0 + 3.0 * horsepower + rng.normal(loc=0.0, scale=100.0, size=n),
       "Fuel economy (mpg)": 45.0 - 0.08 * horsepower + rng.normal(loc=0.0, scale=2.0, size=n),
       "Price (k USD)": 15.0 + 0.12 * horsepower + rng.normal(loc=0.0, scale=3.0, size=n),
   })

   fig = pairplot(df, title="Vehicle Specs Pairplot")
   fig.legend(loc="lower center", bbox_to_anchor=(0.5, -0.05), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/multivariate/charts/pairplot.png" alt="pairplot example output"><figcaption>Example output</figcaption></figure></div>
