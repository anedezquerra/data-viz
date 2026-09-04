dataviz.regression.influence.cooks_distance_plot_static
=======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.influence</p></div>

.. currentmodule:: dataviz.regression.influence

.. autofunction:: cooks_distance_plot_static

Use case
--------

Use to flag influential observations whose removal would shift the fit, using a 4/n threshold.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.influence import cooks_distance_plot_static

   rng = np.random.default_rng(42)
   n = 28
   ad_spend = rng.uniform(5.0, 60.0, n)
   store_traffic = rng.uniform(100.0, 900.0, n)
   X = pd.DataFrame({"ad_spend_kusd": ad_spend,
                      "store_traffic_daily": store_traffic})
   X.loc[27, "ad_spend_kusd"] = 95.0  # an outlier campaign week
   y = pd.Series(20.0 + 1.8 * ad_spend + 0.05 * store_traffic
                 + rng.normal(0.0, 6.0, n), name="weekly_revenue_kusd")
   y.iloc[27] = 260.0
   beta = np.linalg.lstsq(np.column_stack([np.ones(n), X]), y, rcond=None)[0]
   y_pred = np.column_stack([np.ones(n), X]) @ beta

   ax = cooks_distance_plot_static(X, y, y_pred,
                                   title="Marketing Mix Model: Cook's Distance",
                                   color="#d62728")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/influence/cooks_distance_plot_static.png" alt="cooks_distance_plot_static example output"><figcaption>Example output</figcaption></figure></div>
