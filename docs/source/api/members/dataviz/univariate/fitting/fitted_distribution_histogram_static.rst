dataviz.univariate.fitting.fitted_distribution_histogram_static
===============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.fitting</p></div>

.. currentmodule:: dataviz.univariate.fitting

.. autofunction:: fitted_distribution_histogram_static

Use case
--------

Use to overlay a fitted probability density on a histogram to visually judge how well the chosen distribution fits.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.univariate.fitting import fitted_distribution_histogram_static

   # Insurance claim severities recorded by an auto portfolio
   rng = np.random.default_rng(42)
   claims = pd.Series(
       np.round(rng.lognormal(mean=8.1, sigma=0.9, size=56), 0),
       name="claim_usd",
   )

   ax = fitted_distribution_histogram_static(
       claims,
       distribution="lognorm",
       bins=16,
       title="Claim Severity with Fitted Lognormal",
       xlabel="Claim Amount (USD)",
       color="lightsteelblue",
       fit_color="crimson",
       theme="default",
   )
   ax.set_ylabel("Density")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/fitting/fitted_distribution_histogram_static.png" alt="fitted_distribution_histogram_static example output"><figcaption>Example output</figcaption></figure></div>
