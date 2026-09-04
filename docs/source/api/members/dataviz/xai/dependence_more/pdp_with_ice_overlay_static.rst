dataviz.xai.dependence_more.pdp_with_ice_overlay_static
=======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.dependence_more</p></div>

.. currentmodule:: dataviz.xai.dependence_more

.. autofunction:: pdp_with_ice_overlay_static

Use case
--------

Use to show the average feature effect while revealing heterogeneous per-instance behavior hidden by a plain PDP.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.xai.dependence_more import pdp_with_ice_overlay_static

   rng = np.random.default_rng(42)
   grid = np.linspace(300, 850, 30)
   base = 1.0 / (1.0 + np.exp((grid - 600.0) / 70.0))
   offsets = rng.normal(0.0, 0.08, size=(40, 1))
   ice_curves = base[None, :] + offsets + rng.normal(0.0, 0.02, size=(40, grid.size))
   pdp = ice_curves.mean(axis=0)
   rug = rng.uniform(300, 850, size=25)

   ax = pdp_with_ice_overlay_static(
       grid,
       ice_curves,
       pdp,
       feature_name="Credit score",
       rug=rug,
       title="PDP + ICE: Default Risk vs Credit Score",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/dependence_more/pdp_with_ice_overlay_static.png" alt="pdp_with_ice_overlay_static example output"><figcaption>Example output</figcaption></figure></div>
