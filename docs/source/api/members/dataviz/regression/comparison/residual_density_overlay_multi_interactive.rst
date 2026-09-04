dataviz.regression.comparison.residual_density_overlay_multi_interactive
========================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.comparison</p></div>

.. currentmodule:: dataviz.regression.comparison

.. autofunction:: residual_density_overlay_multi_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.comparison import residual_density_overlay_multi_interactive

   rng = np.random.default_rng(42)
   residuals_per_model = [
       rng.normal(0.0, 0.5, size=60),
       rng.normal(0.0, 0.8, size=60),
   ]

   fig = residual_density_overlay_multi_interactive(residuals_per_model, ["OLS", "Ridge"])
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/comparison/residual_density_overlay_multi_interactive.png" alt="residual_density_overlay_multi_interactive example output"><figcaption>Example output</figcaption></figure></div>
