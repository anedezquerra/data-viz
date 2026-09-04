dataviz.regression.bayesian.posterior_coefficient_density_static
================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.bayesian</p></div>

.. currentmodule:: dataviz.regression.bayesian

.. autofunction:: posterior_coefficient_density_static

Use case
--------

Use to inspect the full posterior distribution of each coefficient from MCMC samples instead of relying on a single point estimate.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.bayesian import posterior_coefficient_density_static

   rng = np.random.default_rng(42)
   samples = [rng.normal(2.1, 0.4, 600),
              rng.normal(-0.7, 0.25, 600),
              rng.normal(0.05, 0.5, 600),
              rng.normal(1.3, 0.3, 600)]
   names = ["sqft", "bedrooms", "age_years", "dist_transit_km"]

   ax = posterior_coefficient_density_static(
       samples, coef_names=names,
       title="Hedonic Pricing Model: Posterior Coefficient Densities",
       cmap="plasma")
   ax.axvline(0.0, color="#444", linestyle=":", linewidth=1)
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/bayesian/posterior_coefficient_density_static.png" alt="posterior_coefficient_density_static example output"><figcaption>Example output</figcaption></figure></div>
