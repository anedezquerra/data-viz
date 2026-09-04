dataviz.xai.counterfactuals.what_if_slider_plot_static
======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.counterfactuals</p></div>

.. currentmodule:: dataviz.xai.counterfactuals

.. autofunction:: what_if_slider_plot_static

Use case
--------

Use to sweep one feature and watch the predicted outcome change, answering what-if questions for end users.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.xai.counterfactuals import what_if_slider_plot_static

   grid = np.linspace(500, 800, 60)
   pred_default = 1.0 / (1.0 + np.exp((grid - 645.0) / 45.0))

   ax = what_if_slider_plot_static(
       grid,
       pred_default,
       feature_name="Credit score",
       current_value=612,
       threshold=0.5,
       title="What-If: Sweeping Credit Score for Applicant #417",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/counterfactuals/what_if_slider_plot_static.png" alt="what_if_slider_plot_static example output"><figcaption>Example output</figcaption></figure></div>
