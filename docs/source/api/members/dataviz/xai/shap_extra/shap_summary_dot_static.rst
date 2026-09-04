dataviz.xai.shap_extra.shap_summary_dot_static
==============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.shap_extra</p></div>

.. currentmodule:: dataviz.xai.shap_extra

.. autofunction:: shap_summary_dot_static

Use case
--------

Use as the canonical SHAP beeswarm: per-instance SHAP values per feature, colored by feature value to expose direction and spread.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.xai.shap_extra import shap_summary_dot_static

   rng = np.random.default_rng(37)
   shap_values = rng.normal(0.0, 0.2, size=(60, 4))
   feature_values = rng.normal(0.0, 1.0, size=(60, 4))
   feature_names = ["age", "income", "tenure", "debt"]

   ax = shap_summary_dot_static(shap_values, feature_values, feature_names)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/shap_extra/shap_summary_dot_static.png" alt="shap_summary_dot_static example output"><figcaption>Example output</figcaption></figure></div>
