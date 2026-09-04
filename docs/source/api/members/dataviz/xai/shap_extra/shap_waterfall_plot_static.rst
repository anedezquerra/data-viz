dataviz.xai.shap_extra.shap_waterfall_plot_static
=================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.shap_extra</p></div>

.. currentmodule:: dataviz.xai.shap_extra

.. autofunction:: shap_waterfall_plot_static

Use case
--------

Use to walk one prediction from base value to f(x) feature by feature; small contributions collapse into an 'other' bar via top_n.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.xai.shap_extra import shap_waterfall_plot_static

   shap_instance = np.array([0.18, -0.09, 0.05, -0.03, 0.02])
   feature_names = ["age", "income", "tenure", "debt", "region_score"]

   ax = shap_waterfall_plot_static(shap_instance, feature_names, base_value=0.35)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/shap_extra/shap_waterfall_plot_static.png" alt="shap_waterfall_plot_static example output"><figcaption>Example output</figcaption></figure></div>
