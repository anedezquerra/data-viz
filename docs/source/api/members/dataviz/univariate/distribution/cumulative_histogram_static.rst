dataviz.univariate.distribution.cumulative_histogram_static
===========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.distribution</p></div>

.. currentmodule:: dataviz.univariate.distribution

.. autofunction:: cumulative_histogram_static

Use case
--------

Use to show cumulative counts across bins when the running total of observations matters more than per-bin frequency.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.univariate.distribution import cumulative_histogram_static

   # Order values processed by an online checkout during a sale
   rng = np.random.default_rng(42)
   order_usd = pd.Series(
       np.round(rng.lognormal(mean=4.2, sigma=0.6, size=54), 2),
       name="order_usd",
   )

   ax = cumulative_histogram_static(
       order_usd,
       bins=15,
       title="Cumulative Order Value Distribution",
       xlabel="Order Value (USD)",
       ylabel="Cumulative Orders",
       color="goldenrod",
       alpha=0.8,
       theme="default",
   )
   ax.set_ylabel("Cumulative Orders")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/distribution/cumulative_histogram_static.png" alt="cumulative_histogram_static example output"><figcaption>Example output</figcaption></figure></div>
