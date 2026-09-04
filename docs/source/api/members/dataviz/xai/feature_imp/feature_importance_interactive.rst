dataviz.xai.feature_imp.feature_importance_interactive
======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.feature_imp</p></div>

.. currentmodule:: dataviz.xai.feature_imp

.. autofunction:: feature_importance_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   from dataviz.xai.feature_imp import feature_importance_interactive

   importances = pd.Series(
       [0.32, 0.21, 0.15, 0.09],
       index=["age", "income", "tenure", "region_score"],
   )

   fig = feature_importance_interactive(importances)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/feature_imp/feature_importance_interactive.png" alt="feature_importance_interactive example output"><figcaption>Example output</figcaption></figure></div>
