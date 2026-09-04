dataviz.regression.residual_features.residual_vs_feature_interactive
====================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.residual_features</p></div>

.. currentmodule:: dataviz.regression.residual_features

.. autofunction:: residual_vs_feature_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.residual_features import residual_vs_feature_interactive

   rng = np.random.default_rng(42)
   feature = rng.normal(0.0, 1.0, size=60)
   y_true = 10 + 2 * feature + rng.normal(0.0, 1.0, size=60)
   y_pred = y_true + rng.normal(0.0, 0.5, size=60)

   fig = residual_vs_feature_interactive(feature, y_true, y_pred, feature_name="x1")
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/regression/residual_features/residual_vs_feature_interactive.png" alt="residual_vs_feature_interactive example output"><figcaption>Example output</figcaption></figure></div>
