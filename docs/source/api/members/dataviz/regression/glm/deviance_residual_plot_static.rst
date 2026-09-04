dataviz.regression.glm.deviance_residual_plot_static
====================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.glm</p></div>

.. currentmodule:: dataviz.regression.glm

.. autofunction:: deviance_residual_plot_static

Use case
--------

Use to plot deviance residuals against fitted values to detect lack of fit in a GLM.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.glm import deviance_residual_plot_static

   rng = np.random.default_rng(42)
   exposure = rng.uniform(0.5, 3.0, 60)
   mu = pd.Series(np.exp(0.8 + 0.4 * exposure), name="expected_claims")
   claims = pd.Series(rng.poisson(mu), name="observed_claims")

   ax = deviance_residual_plot_static(claims, mu, family="poisson",
                                      title="Auto Insurance Claims: Deviance Residuals",
                                      color="#2ca02c")
   ax.set_xlabel("Fitted mean claims")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/glm/deviance_residual_plot_static.png" alt="deviance_residual_plot_static example output"><figcaption>Example output</figcaption></figure></div>
