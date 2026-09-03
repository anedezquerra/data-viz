dataviz.regression.bayesian.posterior_coefficient_density_static
================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.bayesian</p></div>

.. currentmodule:: dataviz.regression.bayesian

.. autofunction:: posterior_coefficient_density_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.bayesian import posterior_coefficient_density_static

   rng = np.random.default_rng(42)
   samples_per_coef = [
       rng.normal(2.0, 0.3, size=200),
       rng.normal(-1.0, 0.3, size=200),
       rng.normal(0.5, 0.3, size=200),
   ]

   ax = posterior_coefficient_density_static(
       samples_per_coef, coef_names=["beta0", "beta1", "beta2"]
   )
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/regression/bayesian/posterior_coefficient_density_static.png" alt="posterior_coefficient_density_static example output"><figcaption>Example output</figcaption></figure></div>
