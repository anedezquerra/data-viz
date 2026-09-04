dataviz.univariate.robust.robust_location_plot_static
=====================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.robust</p></div>

.. currentmodule:: dataviz.univariate.robust

.. autofunction:: robust_location_plot_static

Use case
--------

Use to see where the median, trimmed mean, and winsorized mean fall on the histogram and spot disagreement between centers.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.univariate.robust import robust_location_plot_static

   rng = np.random.default_rng(42)
   income_k = rng.gamma(shape=2.5, scale=22.0, size=150).round(1)
   income_k[[12, 77, 130]] = [950.0, 1200.0, 875.0]
   household_income = pd.Series(income_k, name="household_income_k")
   ax = robust_location_plot_static(
       household_income,
       title="Household Income with Robust Location Estimates",
       color="lightsteelblue",
       theme="minimal",
   )
   ax.set_xlabel("Household income (thousands)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/robust/robust_location_plot_static.png" alt="robust_location_plot_static example output"><figcaption>Example output</figcaption></figure></div>
