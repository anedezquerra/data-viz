dataviz.regression.multicollinearity.eigenvalue_scree_predictors_static
=======================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.multicollinearity</p></div>

.. currentmodule:: dataviz.regression.multicollinearity

.. autofunction:: eigenvalue_scree_predictors_static

Use case
--------

Use to see how much predictor variance concentrates in a few components, a sign of multicollinearity.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.multicollinearity import eigenvalue_scree_predictors_static

   rng = np.random.default_rng(42)
   x1 = rng.normal(0.0, 1.0, size=60)
   X = np.column_stack([x1, 0.9 * x1 + rng.normal(0.0, 0.1, size=60), rng.normal(0.0, 1.0, size=60)])

   ax = eigenvalue_scree_predictors_static(X)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/multicollinearity/eigenvalue_scree_predictors_static.png" alt="eigenvalue_scree_predictors_static example output"><figcaption>Example output</figcaption></figure></div>
