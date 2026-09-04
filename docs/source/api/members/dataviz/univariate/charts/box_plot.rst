dataviz.univariate.charts.box_plot
==================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.charts</p></div>

.. currentmodule:: dataviz.univariate.charts

.. autofunction:: box_plot

Use case
--------

Use to summarize quartiles, spread, and outliers of a numeric variable in a compact box plot.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.univariate.charts import box_plot

   # Commute times reported by employees in a hybrid-work survey
   rng = np.random.default_rng(42)
   commute_min = pd.Series(
       np.round(rng.gamma(shape=3.0, scale=8.0, size=55), 1),
       name="commute_min",
   )

   ax = box_plot(
       commute_min,
       title="Employee Commute Time Spread",
       patch_artist=True,
   )
   ax.set_ylabel("Commute Time (min)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/charts/box_plot.png" alt="box_plot example output"><figcaption>Example output</figcaption></figure></div>
