dataviz.xai.charts.partial_dependence
=====================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.charts</p></div>

.. currentmodule:: dataviz.xai.charts

.. autofunction:: partial_dependence

Use case
--------

Use to show how one feature affects the predicted outcome on average, holding other features constant.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.xai.charts import partial_dependence

   importances = np.array([0.42, 0.31, 0.18])
   feature_names = ["age", "income", "tenure"]
   shap_values = np.array([[0.1, -0.2, 0.3], [0.2, -0.1, 0.1]])
   feature_values = np.array([0, 1, 2, 3])
   pd_values = np.array([0.2, 0.25, 0.31, 0.34])

   result = partial_dependence(feature_values, pd_values)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/charts/partial_dependence.png" alt="partial_dependence example output"><figcaption>Example output</figcaption></figure></div>
