dataviz.bivariate.charts.line_plot
==================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.charts</p></div>

.. currentmodule:: dataviz.bivariate.charts

.. autofunction:: line_plot

Use case
--------

Use to show how a numeric variable changes across an ordered axis such as time or sequence index.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.bivariate.charts import line_plot

   rng = np.random.default_rng(42)
   x = pd.Series(np.arange(30), name="Day")
   y = pd.Series(np.cumsum(rng.normal(loc=0.1, scale=1.0, size=30)), name="Output")

   ax = line_plot(x, y, title="Output over time")
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/charts/line_plot.png" alt="line_plot example output"><figcaption>Example output</figcaption></figure></div>
