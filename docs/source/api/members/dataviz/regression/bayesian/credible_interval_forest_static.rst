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

   coef_names = ["beta0", "beta1", "beta2"]
   means = np.array([2.0, -1.0, 0.5])
   lower = means - 0.4
   upper = means + 0.4

   ax = credible_interval_forest_static(coef_names, means, lower, upper)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/bayesian/credible_interval_forest_static.png" alt="credible_interval_forest_static example output"><figcaption>Example output</figcaption></figure></div>
