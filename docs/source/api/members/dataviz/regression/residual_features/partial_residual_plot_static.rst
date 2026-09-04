dataviz.regression.residual_features.partial_residual_plot_static
=================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.residual_features</p></div>

.. currentmodule:: dataviz.regression.residual_features

.. autofunction:: partial_residual_plot_static

Use case
--------

Use to inspect the marginal effect of one predictor in an OLS fit while adjusting for the others; curvature suggests the feature needs a nonlinear term.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.residual_features import partial_residual_plot_static

   rng = np.random.default_rng(42)
   X = rng.normal(0.0, 1.0, size=(60, 3))
   y_true = 10 + X @ np.array([2.0, -1.0, 0.5]) + rng.normal(0.0, 0.5, size=60)

   ax = partial_residual_plot_static(X, y_true, feature_index=0, feature_name="x1")
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/residual_features/partial_residual_plot_static.png" alt="partial_residual_plot_static example output"><figcaption>Example output</figcaption></figure></div>
