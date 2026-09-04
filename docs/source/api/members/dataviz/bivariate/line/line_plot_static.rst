dataviz.bivariate.line.line_plot_static
=======================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.line</p></div>

.. currentmodule:: dataviz.bivariate.line

.. autofunction:: line_plot_static

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
   from dataviz.bivariate.line import line_plot_static

   rng = np.random.default_rng(42)
   df = pd.DataFrame({
       "Week": np.arange(1, 53),
       "Active users": 10000.0 + np.cumsum(rng.normal(loc=120.0, scale=300.0, size=52)),
   })

   ax = line_plot_static(
       "Week",
       "Active users",
       data=df,
       title="Weekly Active Users",
       marker="o",
       markersize=4,
       rolling_window=4,
       fill_to=9000.0,
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/line/line_plot_static.png" alt="line_plot_static example output"><figcaption>Example output</figcaption></figure></div>
