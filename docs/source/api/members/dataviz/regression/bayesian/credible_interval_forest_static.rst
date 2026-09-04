dataviz.regression.bayesian.credible_interval_forest_static
===========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.bayesian</p></div>

.. currentmodule:: dataviz.regression.bayesian

.. autofunction:: credible_interval_forest_static

Use case
--------

Use to compare credible intervals across coefficients at a glance, seeing which effects are credibly different from zero.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.bayesian import credible_interval_forest_static

   names = ["ad_spend", "price_index", "seasonality", "distribution"]
   means = np.array([0.42, -1.15, 0.28, 0.66])
   lower = means - np.array([0.18, 0.30, 0.22, 0.25])
   upper = means + np.array([0.20, 0.28, 0.24, 0.27])

   ax = credible_interval_forest_static(
       names, means, lower, upper,
       title="Marketing Mix Model: 94% Credible Intervals",
       color="#2a7f62")
   ax.set_xlabel("Effect on weekly sales (log units)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/bayesian/credible_interval_forest_static.png" alt="credible_interval_forest_static example output"><figcaption>Example output</figcaption></figure></div>
