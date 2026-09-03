dataviz.bivariate.charts.scatter_plot
=====================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.charts</p></div>

.. currentmodule:: dataviz.bivariate.charts

.. autofunction:: scatter_plot

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.bivariate.charts import scatter_plot

   rng = np.random.default_rng(42)
   x = pd.Series(rng.normal(loc=10.0, scale=2.0, size=30), name="Input")
   y = pd.Series(2.0 * x + rng.normal(loc=0.0, scale=1.0, size=30), name="Output")

   ax = scatter_plot(x, y, title="Input vs output")
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/bivariate/charts/scatter_plot.png" alt="scatter_plot example output"><figcaption>Example output</figcaption></figure></div>
