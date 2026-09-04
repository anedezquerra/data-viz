dataviz.xai.local_explanations.shap_force_plot_interactive
==========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.local_explanations</p></div>

.. currentmodule:: dataviz.xai.local_explanations

.. autofunction:: shap_force_plot_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.xai.local_explanations import shap_force_plot_interactive

   shap_instance = np.array([0.25, -0.10, 0.05, -0.02])
   feature_names = ["age", "income", "tenure", "debt"]

   fig = shap_force_plot_interactive(shap_instance, feature_names, base_value=0.40)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/local_explanations/shap_force_plot_interactive.png" alt="shap_force_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
