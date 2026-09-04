dataviz.xai.shap_more.shap_temporal_drift_static
================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.shap_more</p></div>

.. currentmodule:: dataviz.xai.shap_more

.. autofunction:: shap_temporal_drift_static

Use case
--------

Use to track mean absolute SHAP per feature over time windows, detecting when the model's driving features drift.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.xai.shap_more import shap_temporal_drift_static

   rng = np.random.default_rng(49)
   timestamps = pd.Series(pd.date_range("2024-01-01", periods=56, freq="D"))
   shap_values = rng.normal(0.0, 0.2, size=(56, 4))
   feature_names = ["age", "income", "tenure", "debt"]

   ax = shap_temporal_drift_static(timestamps, shap_values, feature_names)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/shap_more/shap_temporal_drift_static.png" alt="shap_temporal_drift_static example output"><figcaption>Example output</figcaption></figure></div>
