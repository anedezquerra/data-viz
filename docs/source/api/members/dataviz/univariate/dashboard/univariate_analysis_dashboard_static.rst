dataviz.univariate.dashboard.univariate_analysis_dashboard_static
=================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.dashboard</p></div>

.. currentmodule:: dataviz.univariate.dashboard

.. autofunction:: univariate_analysis_dashboard_static

Use case
--------

Use to get a multi-panel overview of one variable combining several univariate views in a single figure.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.univariate.dashboard import univariate_analysis_dashboard_static

   # Quarterly revenue per store for a regional retail chain
   rng = np.random.default_rng(42)
   revenue_k = pd.Series(
       np.round(rng.lognormal(mean=11.2, sigma=0.4, size=46) / 1000.0, 1),
       name="revenue_kusd",
   )

   fig = univariate_analysis_dashboard_static(
       revenue_k,
       bins=12,
       title="Store Revenue Profile (USD thousands)",
       color="steelblue",
       theme="default",
   )
   fig.legend(loc="lower center", bbox_to_anchor=(0.5, -0.05), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/dashboard/univariate_analysis_dashboard_static.png" alt="univariate_analysis_dashboard_static example output"><figcaption>Example output</figcaption></figure></div>
