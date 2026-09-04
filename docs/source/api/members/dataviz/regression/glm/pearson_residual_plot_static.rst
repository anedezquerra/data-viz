dataviz.regression.glm.pearson_residual_plot_static
===================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.glm</p></div>

.. currentmodule:: dataviz.regression.glm

.. autofunction:: pearson_residual_plot_static

Use case
--------

Use to plot Pearson residuals against fitted means to check the assumed variance structure.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.glm import pearson_residual_plot_static

   rng = np.random.default_rng(42)
   dose_mg = rng.uniform(10.0, 100.0, 48)
   prob = pd.Series(1.0 / (1.0 + np.exp(-(dose_mg - 55.0) / 12.0)),
                    name="response_prob")
   responded = pd.Series(rng.binomial(1, prob), name="responded")

   ax = pearson_residual_plot_static(responded, prob, family="binomial",
                                     title="Clinical Trial Dose-Response: Pearson Residuals",
                                     color="#d62728")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/glm/pearson_residual_plot_static.png" alt="pearson_residual_plot_static example output"><figcaption>Example output</figcaption></figure></div>
