dataviz.xai.charts.feature_importance
=====================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.charts</p></div>

.. currentmodule:: dataviz.xai.charts

.. autofunction:: feature_importance

Use case
--------

Use when presenting which features drive a model's predictions to non-technical stakeholders.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.xai.charts import feature_importance

   importances = pd.Series(
       [0.32, 0.21, 0.15, 0.09],
       index=["age", "income", "tenure", "region_score"],
   )

   ax = feature_importance(importances)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/charts/feature_importance.png" alt="feature_importance example output"><figcaption>Example output</figcaption></figure></div>
