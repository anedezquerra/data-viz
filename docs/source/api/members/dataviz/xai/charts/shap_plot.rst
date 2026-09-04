dataviz.xai.charts.shap_plot
============================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.charts</p></div>

.. currentmodule:: dataviz.xai.charts

.. autofunction:: shap_plot

Use case
--------

Use to explain individual and global predictions with SHAP values during model review or debugging.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.xai.charts import shap_plot

   importances = np.array([0.42, 0.31, 0.18])
   feature_names = ["age", "income", "tenure"]
   shap_values = np.array([[0.1, -0.2, 0.3], [0.2, -0.1, 0.1]])
   feature_values = np.array([0, 1, 2, 3])
   pd_values = np.array([0.2, 0.25, 0.31, 0.34])

   result = shap_plot(shap_values, feature_names)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/charts/shap_plot.png" alt="shap_plot example output"><figcaption>Example output</figcaption></figure></div>
