dataviz.xai.counterfactuals.diverse_counterfactual_grid_static
==============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.counterfactuals</p></div>

.. currentmodule:: dataviz.xai.counterfactuals

.. autofunction:: diverse_counterfactual_grid_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.xai.counterfactuals import diverse_counterfactual_grid_static

   original = {"income": 45.0, "debt": 30.0, "tenure": 2.0}
   counterfactuals = pd.DataFrame(
       {
           "income": [55.0, 48.0, 62.0],
           "debt": [24.0, 26.0, 30.0],
           "tenure": [2.0, 3.0, 4.0],
       }
   )

   ax = diverse_counterfactual_grid_static(original, counterfactuals)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/counterfactuals/diverse_counterfactual_grid_static.png" alt="diverse_counterfactual_grid_static example output"><figcaption>Example output</figcaption></figure></div>
