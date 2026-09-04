dataviz.regression.effects.ice_plot_regression_static
=====================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.effects</p></div>

.. currentmodule:: dataviz.regression.effects

.. autofunction:: ice_plot_regression_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.effects import ice_plot_regression_static

   rng = np.random.default_rng(42)
   grid = np.linspace(0.0, 1.0, 20)
   ice_matrix = np.stack(
       [grid**2 + rng.normal(0.0, 0.05, size=20) for _ in range(10)]
   )

   ax = ice_plot_regression_static(grid, ice_matrix, feature_name="x1")
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/regression/effects/ice_plot_regression_static.png" alt="ice_plot_regression_static example output"><figcaption>Example output</figcaption></figure></div>
