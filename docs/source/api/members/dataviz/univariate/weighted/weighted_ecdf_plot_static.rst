dataviz.univariate.weighted.weighted_ecdf_plot_static
=====================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.weighted</p></div>

.. currentmodule:: dataviz.univariate.weighted

.. autofunction:: weighted_ecdf_plot_static

Use case
--------

Use to plot the empirical cumulative distribution when observations contribute unequal weight.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.univariate.weighted import weighted_ecdf_plot_static

   rng = np.random.default_rng(42)
   nps_score = pd.Series(rng.integers(0, 11, size=250), name="nps_score")
   sample_weight = pd.Series(rng.uniform(0.5, 2.5, size=250).round(2), name="sample_weight")
   ax = weighted_ecdf_plot_static(
       nps_score,
       sample_weight,
       title="Weighted ECDF of NPS Scores",
       color="indigo",
       theme="minimal",
   )
   ax.set_xlabel("NPS score")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/weighted/weighted_ecdf_plot_static.png" alt="weighted_ecdf_plot_static example output"><figcaption>Example output</figcaption></figure></div>
