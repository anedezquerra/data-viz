dataviz.regression.autocorrelation.residual_acf_static
======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.autocorrelation</p></div>

.. currentmodule:: dataviz.regression.autocorrelation

.. autofunction:: residual_acf_static

Use case
--------

Use to check whether regression residuals are autocorrelated across lags, which invalidates standard OLS inference for time-ordered data.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.autocorrelation import residual_acf_static

   rng = np.random.default_rng(42)
   batch = np.arange(36)
   fill = pd.Series(500 + 0.8 * np.sin(batch / 4.0) + rng.normal(0, 1.5, 36),
                    name="fill_volume_ml")
   pred = pd.Series(500 + 0.6 * np.sin(batch / 4.0), name="predicted_fill_ml")

   ax = residual_acf_static(fill, pred, max_lag=12,
                            title="Bottling Line Fill Model: Residual ACF",
                            color="#2a7f62", theme="minimal")
   ax.set_xlabel("Lag (batches)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/autocorrelation/residual_acf_static.png" alt="residual_acf_static example output"><figcaption>Example output</figcaption></figure></div>
