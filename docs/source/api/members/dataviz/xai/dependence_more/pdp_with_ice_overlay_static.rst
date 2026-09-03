dataviz.xai.dependence_more.pdp_with_ice_overlay_static
=======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.dependence_more</p></div>

.. currentmodule:: dataviz.xai.dependence_more

.. autofunction:: pdp_with_ice_overlay_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.xai.dependence_more import pdp_with_ice_overlay_static

   rng = np.random.default_rng(17)
   grid = np.linspace(0.0, 10.0, 20)
   ice_curves = (
       np.sin(grid)[None, :] * rng.uniform(0.5, 1.5, size=(15, 1))
       + rng.normal(0.0, 0.05, size=(15, 20))
   )
   pdp = ice_curves.mean(axis=0)

   ax = pdp_with_ice_overlay_static(grid, ice_curves, pdp, feature_name="income")
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
