dataviz.bivariate.scatter.scatter_plot_static
=============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.scatter</p></div>

.. currentmodule:: dataviz.bivariate.scatter

.. autofunction:: scatter_plot_static

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
   from dataviz.bivariate.scatter import scatter_plot_static

   rng = np.random.default_rng(42)
   n = 75
   df = pd.DataFrame({
       "Engine size (L)": rng.uniform(low=1.0, high=5.5, size=n),
       "Body style": rng.choice(["Sedan", "SUV", "Truck"], size=n),
   })
   df["Fuel economy (mpg)"] = 42.0 - 4.0 * df["Engine size (L)"] + rng.normal(loc=0.0, scale=2.5, size=n)

   ax = scatter_plot_static(
       "Engine size (L)",
       "Fuel economy (mpg)",
       data=df,
       hue="Body style",
       title="Engine Size vs Fuel Economy",
       fit_degree=1,
       diagonal=False,
       show_corr=True,
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/scatter/scatter_plot_static.png" alt="scatter_plot_static example output"><figcaption>Example output</figcaption></figure></div>
