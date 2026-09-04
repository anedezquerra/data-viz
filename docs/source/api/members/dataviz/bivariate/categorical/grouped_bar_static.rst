dataviz.bivariate.categorical.grouped_bar_static
================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.categorical</p></div>

.. currentmodule:: dataviz.bivariate.categorical

.. autofunction:: grouped_bar_static

Use case
--------

Use to compare an aggregated numeric value, such as a mean or sum, across the levels of a categorical variable.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.bivariate.categorical import grouped_bar_static

   rng = np.random.default_rng(42)
   n = 90
   region = pd.Series(np.repeat(["North", "South", "East", "West"], n // 4)[:n], name="Region")
   sales = pd.Series(rng.normal(loc=120.0, scale=25.0, size=n), name="Quarterly sales (k USD)")

   ax = grouped_bar_static(
       region,
       sales,
       aggfunc="median",
       title="Median Quarterly Sales by Region",
       color="seagreen",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/categorical/grouped_bar_static.png" alt="grouped_bar_static example output"><figcaption>Example output</figcaption></figure></div>
