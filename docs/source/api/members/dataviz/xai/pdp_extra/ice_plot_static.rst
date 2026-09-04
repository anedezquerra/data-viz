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

   rng = np.random.default_rng(42)
   tenure = np.linspace(0, 72, 30)
   n_instances = 40
   offsets = rng.normal(0, 0.8, size=(n_instances, 1))
   curves = 1.6 - 0.035 * tenure + 0.0002 * tenure ** 2
   ice_curves = curves + offsets + rng.normal(0, 0.03, size=(n_instances, tenure.size))
   ax = ice_plot_static(
       tenure, ice_curves, feature_name="tenure_months",
       title="ICE curves - churn log-odds vs customer tenure",
       line_alpha=0.25,
   )
   ax.set_ylabel("Predicted churn log-odds")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/pdp_extra/ice_plot_static.png" alt="ice_plot_static example output"><figcaption>Example output</figcaption></figure></div>
