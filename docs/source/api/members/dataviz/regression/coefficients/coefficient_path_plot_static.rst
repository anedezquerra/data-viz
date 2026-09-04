dataviz.regression.coefficients.coefficient_path_plot_static
============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.coefficients</p></div>

.. currentmodule:: dataviz.regression.coefficients

.. autofunction:: coefficient_path_plot_static

Use case
--------

Use to trace coefficient paths across a regularization parameter and see which features shrink out first in ridge or lasso fits.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.coefficients import coefficient_path_plot_static

   alphas = np.logspace(-3, 1, 20)
   features = ["income", "debt_ratio", "credit_age", "utilization"]
   true_betas = np.array([0.9, -1.4, 0.5, -0.8])
   paths = true_betas[None, :] * (1 - np.exp(-alphas[:, None] * 5))

   ax = coefficient_path_plot_static(alphas, paths, feature_names=features,
                                     log_x=True,
                                     title="Credit Risk Lasso: Coefficient Path",
                                     cmap="tab10")
   ax.set_xlabel("Regularization strength (log)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/coefficients/coefficient_path_plot_static.png" alt="coefficient_path_plot_static example output"><figcaption>Example output</figcaption></figure></div>
