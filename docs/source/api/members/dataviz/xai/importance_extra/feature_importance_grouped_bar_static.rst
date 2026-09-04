dataviz.xai.importance_extra.feature_importance_grouped_bar_static
==================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.importance_extra</p></div>

.. currentmodule:: dataviz.xai.importance_extra

.. autofunction:: feature_importance_grouped_bar_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import matplotlib.pyplot as plt
   from dataviz.xai.importance_extra import feature_importance_grouped_bar_static

   importances = {
       "permutation": {"age": 0.05, "income": 0.12, "tenure": 0.02},
       "gain": {"age": 0.08, "income": 0.15, "tenure": 0.03},
   }

   ax = feature_importance_grouped_bar_static(importances)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/importance_extra/feature_importance_grouped_bar_static.png" alt="feature_importance_grouped_bar_static example output"><figcaption>Example output</figcaption></figure></div>
