dataviz.bivariate.stats.residual_relationship_static
====================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.stats</p></div>

.. currentmodule:: dataviz.bivariate.stats

.. autofunction:: residual_relationship_static

Use case
--------

Use to check whether a polynomial fit leaves structure in the residuals, signaling a poor model choice.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.bivariate.stats import residual_relationship_static

   rng = np.random.default_rng(42)
   n = 70
   experience = pd.Series(rng.uniform(low=0.0, high=20.0, size=n), name="Experience (years)")
   salary = pd.Series(40.0 + 4.0 * experience + 0.08 * experience**2 + rng.normal(loc=0.0, scale=6.0, size=n), name="Salary (k USD)")

   ax = residual_relationship_static(
       experience,
       salary,
       degree=1,
       title="Linear Fit Residuals: Salary vs Experience",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/stats/residual_relationship_static.png" alt="residual_relationship_static example output"><figcaption>Example output</figcaption></figure></div>
