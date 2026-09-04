dataviz.regression.comparison.residual_density_overlay_multi_static
===================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.comparison</p></div>

.. currentmodule:: dataviz.regression.comparison

.. autofunction:: residual_density_overlay_multi_static

Use case
--------

Use to compare residual distributions across models; tighter, zero-centered KDEs indicate better calibrated errors.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.comparison import residual_density_overlay_multi_static

   rng = np.random.default_rng(42)
   residuals = [rng.normal(0, 5, 40),
                rng.normal(0.5, 8, 40),
                rng.normal(-1.5, 12, 40)]
   labels = ["Ridge", "SVR", "KNN"]

   ax = residual_density_overlay_multi_static(
       residuals, labels,
       title="Energy Demand Models: Residual Density Overlay",
       cmap="viridis")
   ax.set_xlabel("Residual (MWh)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/comparison/residual_density_overlay_multi_static.png" alt="residual_density_overlay_multi_static example output"><figcaption>Example output</figcaption></figure></div>
