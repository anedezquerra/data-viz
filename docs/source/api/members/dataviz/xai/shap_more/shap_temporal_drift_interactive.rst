dataviz.xai.shap_more.shap_temporal_drift_interactive
=====================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.shap_more</p></div>

.. currentmodule:: dataviz.xai.shap_more

.. autofunction:: shap_temporal_drift_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.xai.shap_more import shap_temporal_drift_interactive

   rng = np.random.default_rng(49)
   timestamps = pd.Series(pd.date_range("2024-01-01", periods=56, freq="D"))
   shap_values = rng.normal(0.0, 0.2, size=(56, 4))
   feature_names = ["age", "income", "tenure", "debt"]

   fig = shap_temporal_drift_interactive(timestamps, shap_values, feature_names)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/shap_more/shap_temporal_drift_interactive.png" alt="shap_temporal_drift_interactive example output"><figcaption>Example output</figcaption></figure></div>
