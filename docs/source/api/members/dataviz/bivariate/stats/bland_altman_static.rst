dataviz.bivariate.stats.bland_altman_static
===========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.stats</p></div>

.. currentmodule:: dataviz.bivariate.stats

.. autofunction:: bland_altman_static

Use case
--------

Use when comparing two measurement methods to assess their agreement and bias rather than their correlation.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.bivariate.stats import bland_altman_static

   rng = np.random.default_rng(42)
   n = 60
   lab_test = pd.Series(rng.normal(loc=120.0, scale=18.0, size=n), name="Lab assay (mg/dL)")
   home_test = pd.Series(lab_test + rng.normal(loc=2.0, scale=6.0, size=n), name="Home kit (mg/dL)")

   ax = bland_altman_static(
       lab_test,
       home_test,
       title="Bland-Altman: Lab vs Home Kit",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/stats/bland_altman_static.png" alt="bland_altman_static example output"><figcaption>Example output</figcaption></figure></div>
