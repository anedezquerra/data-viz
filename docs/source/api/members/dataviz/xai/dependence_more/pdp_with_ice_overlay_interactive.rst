dataviz.xai.dependence_more.pdp_with_ice_overlay_interactive
============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.dependence_more</p></div>

.. currentmodule:: dataviz.xai.dependence_more

.. autofunction:: pdp_with_ice_overlay_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.xai.dependence_more import pdp_with_ice_overlay_interactive

   rng = np.random.default_rng(17)
   grid = np.linspace(0.0, 10.0, 20)
   ice_curves = (
       np.sin(grid)[None, :] * rng.uniform(0.5, 1.5, size=(15, 1))
       + rng.normal(0.0, 0.05, size=(15, 20))
   )
   pdp = ice_curves.mean(axis=0)

   fig = pdp_with_ice_overlay_interactive(grid, ice_curves, pdp, feature_name="income")
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/xai/dependence_more/pdp_with_ice_overlay_interactive.png" alt="pdp_with_ice_overlay_interactive example output"><figcaption>Example output</figcaption></figure></div>
