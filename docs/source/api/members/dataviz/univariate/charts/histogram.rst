dataviz.univariate.charts.histogram
===================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.charts</p></div>

.. currentmodule:: dataviz.univariate.charts

.. autofunction:: histogram

Use case
--------

Use when profiling a numeric column for the first time to see shape, spread, and outliers at a glance.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.univariate.charts import histogram

   # Commute times reported by employees in a hybrid-work survey
   rng = np.random.default_rng(42)
   commute_min = pd.Series(
       np.round(rng.gamma(shape=3.0, scale=8.0, size=55), 1),
       name="commute_min",
   )

   ax = histogram(
       commute_min,
       bins=12,
       title="Employee Commute Times",
       color="darkseagreen",
       edgecolor="black",
   )
   ax.set_xlabel("Commute Time (min)")
   ax.set_ylabel("Employees")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/charts/histogram.png" alt="histogram example output"><figcaption>Example output</figcaption></figure></div>
