dataviz.xai.pdp_extra.ice_plot_static
=====================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.pdp_extra</p></div>

.. currentmodule:: dataviz.xai.pdp_extra

.. autofunction:: ice_plot_static

Use case
--------

Use to reveal heterogeneous effects hidden by PDP: each ICE curve shows one instance's response as a feature sweeps its range.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.xai.pdp_extra import ice_plot_static

   rng = np.random.default_rng(33)
   feature_values = np.linspace(20.0, 80.0, 15)
   ice_curves = np.log(feature_values)[None, :] * rng.uniform(0.6, 1.4, size=(12, 1))

   ax = ice_plot_static(feature_values, ice_curves, feature_name="income")
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/pdp_extra/ice_plot_static.png" alt="ice_plot_static example output"><figcaption>Example output</figcaption></figure></div>
