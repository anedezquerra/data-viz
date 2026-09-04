dataviz.regression.glm.glm_diagnostic_panel_static
==================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.glm</p></div>

.. currentmodule:: dataviz.regression.glm

.. autofunction:: glm_diagnostic_panel_static

Use case
--------

Use to review deviance, Pearson, working, and link diagnostics for a GLM in one panel.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.glm import glm_diagnostic_panel_static

   rng = np.random.default_rng(42)
   exposure = rng.uniform(0.5, 3.0, 60)
   mu = pd.Series(np.exp(0.8 + 0.4 * exposure), name="expected_claims")
   claims = pd.Series(rng.poisson(mu), name="observed_claims")

   fig = glm_diagnostic_panel_static(claims, mu, family="poisson", link="log",
                                     title="Auto Insurance Claims GLM: Diagnostic Panel")
   fig.legend(loc="lower center", bbox_to_anchor=(0.5, -0.05), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/glm/glm_diagnostic_panel_static.png" alt="glm_diagnostic_panel_static example output"><figcaption>Example output</figcaption></figure></div>
