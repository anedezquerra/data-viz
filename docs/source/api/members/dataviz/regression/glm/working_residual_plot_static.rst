dataviz.regression.glm.working_residual_plot_static
===================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.glm</p></div>

.. currentmodule:: dataviz.regression.glm

.. autofunction:: working_residual_plot_static

Use case
--------

Use to plot working residuals against the linear predictor when diagnosing the IRLS fit.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.glm import working_residual_plot_static

   rng = np.random.default_rng(42)
   dose_mg = rng.uniform(10.0, 100.0, 48)
   prob = pd.Series(1.0 / (1.0 + np.exp(-(dose_mg - 55.0) / 12.0)),
                    name="response_prob")
   responded = pd.Series(rng.binomial(1, prob), name="responded")

   ax = working_residual_plot_static(responded, prob, link="logit",
                                     title="Clinical Trial Dose-Response: Working Residuals",
                                     color="#9467bd")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/glm/working_residual_plot_static.png" alt="working_residual_plot_static example output"><figcaption>Example output</figcaption></figure></div>
