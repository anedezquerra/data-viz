dataviz.xai.counterfactuals.what_if_slider_plot_interactive
===========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.counterfactuals</p></div>

.. currentmodule:: dataviz.xai.counterfactuals

.. autofunction:: what_if_slider_plot_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.xai.counterfactuals import what_if_slider_plot_interactive

   feature_grid = np.linspace(20.0, 80.0, 25)
   predictions = 1.0 / (1.0 + np.exp(-(feature_grid - 50.0) / 8.0))

   fig = what_if_slider_plot_interactive(
       feature_grid, predictions, feature_name="income",
       current_value=45.0, threshold=0.5,
   )
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/xai/counterfactuals/what_if_slider_plot_interactive.png" alt="what_if_slider_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
