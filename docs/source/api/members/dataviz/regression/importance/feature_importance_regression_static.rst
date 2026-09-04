dataviz.regression.importance.feature_importance_regression_static
==================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.importance</p></div>

.. currentmodule:: dataviz.regression.importance

.. autofunction:: feature_importance_regression_static

Use case
--------

Use to rank regression features by the model's built-in importance scores in a descending bar chart.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.importance import feature_importance_regression_static

   feature_names = ["ram_gb", "storage_gb", "screen_inches", "battery_mah",
                    "weight_g", "camera_mp", "age_months"]
   importances = pd.Series([0.34, 0.22, 0.15, 0.11, 0.08, 0.06, 0.04],
                           index=feature_names, name="rf_importance")

   ax = feature_importance_regression_static(
       importances, feature_names=feature_names, top_n=6,
       title="Used Phone Price Model: Feature Importance",
       color="#1f77b4")
   ax.set_xlabel("Gini importance")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/importance/feature_importance_regression_static.png" alt="feature_importance_regression_static example output"><figcaption>Example output</figcaption></figure></div>
