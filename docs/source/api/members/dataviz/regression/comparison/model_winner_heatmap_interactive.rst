dataviz.regression.comparison.model_winner_heatmap_interactive
==============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.comparison</p></div>

.. currentmodule:: dataviz.regression.comparison

.. autofunction:: model_winner_heatmap_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.comparison import model_winner_heatmap_interactive

   win_matrix = np.array([[3, 1], [1, 3]])

   fig = model_winner_heatmap_interactive(["OLS", "Ridge"], ["MAE", "RMSE"], win_matrix)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/comparison/model_winner_heatmap_interactive.png" alt="model_winner_heatmap_interactive example output"><figcaption>Example output</figcaption></figure></div>
