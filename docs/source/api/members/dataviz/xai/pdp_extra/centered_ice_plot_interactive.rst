dataviz.xai.pdp_extra.centered_ice_plot_interactive
===================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.pdp_extra</p></div>

.. currentmodule:: dataviz.xai.pdp_extra

.. autofunction:: centered_ice_plot_interactive

Use case
--------

Use to compare ICE curves anchored at zero at the left endpoint, making differences in slope and shape easier to read than raw levels.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.xai.pdp_extra import centered_ice_plot_interactive

   rng = np.random.default_rng(33)
   feature_values = np.linspace(20.0, 80.0, 15)
   ice_curves = np.log(feature_values)[None, :] * rng.uniform(0.6, 1.4, size=(12, 1))

   fig = centered_ice_plot_interactive(feature_values, ice_curves, feature_name="income")
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/pdp_extra/centered_ice_plot_interactive.png" alt="centered_ice_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
