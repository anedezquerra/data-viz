dataviz.univariate.charts.density_plot
======================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.charts</p></div>

.. currentmodule:: dataviz.univariate.charts

.. autofunction:: density_plot

Use case
--------

Use to view a smooth kernel density estimate of a numeric variable when bin edges of a histogram would distract.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.univariate.charts import density_plot

   # Commute times reported by employees in a hybrid-work survey
   rng = np.random.default_rng(42)
   commute_min = pd.Series(
       np.round(rng.gamma(shape=3.0, scale=8.0, size=55), 1),
       name="commute_min",
   )

   ax = density_plot(
       commute_min,
       title="Employee Commute Time Density",
       color="teal",
       linewidth=2.0,
   )
   ax.set_xlabel("Commute Time (min)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/charts/density_plot.png" alt="density_plot example output"><figcaption>Example output</figcaption></figure></div>
