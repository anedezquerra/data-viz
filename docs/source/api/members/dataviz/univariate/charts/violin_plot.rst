dataviz.univariate.charts.violin_plot
=====================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.charts</p></div>

.. currentmodule:: dataviz.univariate.charts

.. autofunction:: violin_plot

Use case
--------

Use to see the full distribution shape of a numeric variable, including multimodality that a box plot hides.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.univariate.charts import violin_plot

   # Commute times compared across three office locations
   rng = np.random.default_rng(42)
   commutes = pd.DataFrame({
       "Downtown": rng.gamma(shape=3.0, scale=8.0, size=40),
       "Suburban": rng.gamma(shape=2.5, scale=5.0, size=40),
       "Rural": rng.gamma(shape=4.0, scale=10.0, size=40),
   })

   ax = violin_plot(
       commutes,
       title="Commute Times by Office Location",
   )
   ax.set_ylabel("Commute Time (min)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/charts/violin_plot.png" alt="violin_plot example output"><figcaption>Example output</figcaption></figure></div>
