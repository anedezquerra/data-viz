dataviz.regression.residual_features.ccpr_plot_interactive
==========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.residual_features</p></div>

.. currentmodule:: dataviz.regression.residual_features

.. autofunction:: ccpr_plot_interactive

Use case
--------

Use to judge where the linear component of one predictor fits well and where residuals spread out, helping spot nonlinearity or heteroscedasticity per feature.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.residual_features import ccpr_plot_interactive

   rng = np.random.default_rng(42)
   X = rng.normal(0.0, 1.0, size=(60, 3))
   y_true = 10 + X @ np.array([2.0, -1.0, 0.5]) + rng.normal(0.0, 0.5, size=60)

   fig = ccpr_plot_interactive(X, y_true, feature_index=0, feature_name="x1")
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/residual_features/ccpr_plot_interactive.png" alt="ccpr_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
