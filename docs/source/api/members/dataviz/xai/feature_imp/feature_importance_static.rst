dataviz.xai.feature_imp.feature_importance_static
=================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.feature_imp</p></div>

.. currentmodule:: dataviz.xai.feature_imp

.. autofunction:: feature_importance_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.xai.feature_imp import feature_importance_static

   importances = pd.Series(
       [0.32, 0.21, 0.15, 0.09],
       index=["age", "income", "tenure", "region_score"],
   )

   ax = feature_importance_static(importances)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/feature_imp/feature_importance_static.png" alt="feature_importance_static example output"><figcaption>Example output</figcaption></figure></div>
