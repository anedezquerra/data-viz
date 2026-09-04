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
   days = pd.Series(pd.date_range("2024-01-01", periods=90, freq="D"), name="Date")
   visitors = pd.Series(
       5000.0 + np.cumsum(rng.normal(loc=20.0, scale=150.0, size=90)),
       name="Daily visitors",
   )

   ax = line_plot(
       days,
       visitors,
       title="Website Traffic Trend",
       color="steelblue",
       rolling_window=7,
       hline=5000.0,
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/charts/line_plot.png" alt="line_plot example output"><figcaption>Example output</figcaption></figure></div>
