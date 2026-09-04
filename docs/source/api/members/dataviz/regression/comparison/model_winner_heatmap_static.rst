dataviz.regression.comparison.model_winner_heatmap_static
=========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.comparison</p></div>

.. currentmodule:: dataviz.regression.comparison

.. autofunction:: model_winner_heatmap_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.comparison import model_winner_heatmap_static

   win_matrix = np.array([[3, 1], [1, 3]])

   ax = model_winner_heatmap_static(["OLS", "Ridge"], ["MAE", "RMSE"], win_matrix)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/regression/comparison/model_winner_heatmap_static.png" alt="model_winner_heatmap_static example output"><figcaption>Example output</figcaption></figure></div>
