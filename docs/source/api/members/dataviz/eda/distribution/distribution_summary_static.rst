dataviz.eda.distribution.distribution_summary_static
====================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.eda.distribution</p></div>

.. currentmodule:: dataviz.eda.distribution

.. autofunction:: distribution_summary_static

Use case
--------

Use at the start of exploratory analysis to review the distribution of every dataframe column at once.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.eda.distribution import distribution_summary_static

   rng = np.random.default_rng(42)
   n = 120
   df = pd.DataFrame({
       "Order value (USD)": rng.lognormal(mean=4.0, sigma=0.5, size=n),
       "Items per order": rng.poisson(lam=3.0, size=n),
       "Discount (%)": rng.uniform(low=0.0, high=25.0, size=n),
       "Delivery days": rng.integers(1, 10, size=n).astype(float),
   })

   fig = distribution_summary_static(
       df,
       title="Order Metrics Distribution Summary",
       bins=25,
       color="slategray",
   )
   fig.legend(loc="lower center", bbox_to_anchor=(0.5, -0.05), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/eda/distribution/distribution_summary_static.png" alt="distribution_summary_static example output"><figcaption>Example output</figcaption></figure></div>
