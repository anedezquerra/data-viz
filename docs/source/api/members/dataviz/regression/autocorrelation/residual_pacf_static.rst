dataviz.regression.autocorrelation.residual_pacf_static
=======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.autocorrelation</p></div>

.. currentmodule:: dataviz.regression.autocorrelation

.. autofunction:: residual_pacf_static

Use case
--------

Use to identify the direct lag order of residual dependence when choosing an AR term or diagnosing model misspecification.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.autocorrelation import residual_pacf_static

   rng = np.random.default_rng(42)
   week = np.arange(30)
   sales = pd.Series(1200 + 40 * np.sin(week / 2.5) + rng.normal(0, 25, 30),
                     name="weekly_units")
   fitted = pd.Series(1200 + 38 * np.sin(week / 2.5), name="fitted_units")

   ax = residual_pacf_static(sales, fitted, max_lag=10,
                             title="Weekly Demand Model: Residual PACF",
                             color="#8c5aa8")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/autocorrelation/residual_pacf_static.png" alt="residual_pacf_static example output"><figcaption>Example output</figcaption></figure></div>
