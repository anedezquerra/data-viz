dataviz.regression.transforms.boxcox_likelihood_curve_static
============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.transforms</p></div>

.. currentmodule:: dataviz.regression.transforms

.. autofunction:: boxcox_likelihood_curve_static

Use case
--------

Use to choose a Box-Cox power for the response by reading the profile log-likelihood over lambda and its maximizer.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.transforms import boxcox_likelihood_curve_static

   rng = np.random.default_rng(42)
   claim_amount = rng.gamma(shape=2.0, scale=1800.0, size=60)  # right-skewed, > 0

   ax = boxcox_likelihood_curve_static(
       claim_amount, lambdas=np.linspace(-1.5, 1.5, 91),
       title="Auto insurance claims: Box-Cox profile log-likelihood",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/transforms/boxcox_likelihood_curve_static.png" alt="boxcox_likelihood_curve_static example output"><figcaption>Example output</figcaption></figure></div>
