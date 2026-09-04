dataviz.xai.shap_more.shap_monotonicity_plot_static
===================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.shap_more</p></div>

.. currentmodule:: dataviz.xai.shap_more

.. autofunction:: shap_monotonicity_plot_static

Use case
--------

Use to check whether a feature's SHAP values rise monotonically with its value, with an isotonic fit overlay for validation audits.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.xai.shap_more import shap_monotonicity_plot_static

   rng = np.random.default_rng(47)
   feature_values = np.sort(rng.uniform(20.0, 80.0, 60))
   shap_values = 0.015 * (feature_values - 50.0) + rng.normal(0.0, 0.02, 60)

   ax = shap_monotonicity_plot_static(feature_values, shap_values, feature_name="age")
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/shap_more/shap_monotonicity_plot_static.png" alt="shap_monotonicity_plot_static example output"><figcaption>Example output</figcaption></figure></div>
