dataviz.xai.shap_extra.shap_violin_static
=========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.shap_extra</p></div>

.. currentmodule:: dataviz.xai.shap_extra

.. autofunction:: shap_violin_static

Use case
--------

Use to compare the full distribution of SHAP values per feature, revealing skew and outliers that bars hide.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.xai.shap_extra import shap_violin_static

   importances = np.array([0.42, 0.31, 0.18])
   feature_names = ["age", "income", "tenure"]
   shap_values = np.array([[0.1, -0.2, 0.3], [0.2, -0.1, 0.1]])
   feature_values = np.array([0, 1, 2, 3])
   pd_values = np.array([0.2, 0.25, 0.31, 0.34])

   ax = shap_violin_static(shap_values, feature_names)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/shap_extra/shap_violin_static.png" alt="shap_violin_static example output"><figcaption>Example output</figcaption></figure></div>
