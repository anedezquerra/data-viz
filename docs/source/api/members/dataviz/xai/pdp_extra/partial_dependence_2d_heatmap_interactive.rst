dataviz.xai.pdp_extra.partial_dependence_2d_heatmap_interactive
===============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.pdp_extra</p></div>

.. currentmodule:: dataviz.xai.pdp_extra

.. autofunction:: partial_dependence_2d_heatmap_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.xai.pdp_extra import partial_dependence_2d_heatmap_interactive

   rng = np.random.default_rng(31)
   x_grid = np.linspace(0.0, 5.0, 6)
   y_grid = np.linspace(0.0, 4.0, 5)
   pdp = rng.normal(0.5, 0.1, size=(5, 6))

   fig = partial_dependence_2d_heatmap_interactive(
       x_grid, y_grid, pdp, feature_x="income", feature_y="tenure",
   )
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/pdp_extra/partial_dependence_2d_heatmap_interactive.png" alt="partial_dependence_2d_heatmap_interactive example output"><figcaption>Example output</figcaption></figure></div>
