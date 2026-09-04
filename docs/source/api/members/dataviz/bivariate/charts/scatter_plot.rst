dataviz.bivariate.charts.scatter_plot
=====================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.charts</p></div>

.. currentmodule:: dataviz.bivariate.charts

.. autofunction:: scatter_plot

Use case
--------

Use as a first look at the relationship between two numeric variables before choosing a more specialized view.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.bivariate.charts import scatter_plot

   rng = np.random.default_rng(42)
   n = 60
   df = pd.DataFrame({
       "Ad Spend (k USD)": rng.uniform(low=10.0, high=200.0, size=n),
       "Segment": rng.choice(["Retail", "Online"], size=n),
   })
   df["Revenue (k USD)"] = 80.0 + 2.5 * df["Ad Spend (k USD)"] + rng.normal(loc=0.0, scale=30.0, size=n)

   ax = scatter_plot(
       "Ad Spend (k USD)",
       "Revenue (k USD)",
       data=df,
       hue="Segment",
       title="Marketing Spend vs Revenue",
       fit_degree=1,
       show_corr=True,
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/charts/scatter_plot.png" alt="scatter_plot example output"><figcaption>Example output</figcaption></figure></div>
