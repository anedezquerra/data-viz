dataviz.xai.pdp_extra.partial_dependence_2d_heatmap_static
==========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.pdp_extra</p></div>

.. currentmodule:: dataviz.xai.pdp_extra

.. autofunction:: partial_dependence_2d_heatmap_static

Use case
--------

Use to inspect pairwise feature interactions on a precomputed 2-D partial dependence grid.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.xai.pdp_extra import partial_dependence_2d_heatmap_static

   rng = np.random.default_rng(31)
   x_grid = np.linspace(0.0, 5.0, 6)
   y_grid = np.linspace(0.0, 4.0, 5)
   pdp = rng.normal(0.5, 0.1, size=(5, 6))

   ax = partial_dependence_2d_heatmap_static(
       x_grid, y_grid, pdp, feature_x="income", feature_y="tenure",
   )
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/pdp_extra/partial_dependence_2d_heatmap_static.png" alt="partial_dependence_2d_heatmap_static example output"><figcaption>Example output</figcaption></figure></div>
