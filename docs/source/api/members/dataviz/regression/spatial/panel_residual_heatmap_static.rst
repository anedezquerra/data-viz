dataviz.regression.spatial.panel_residual_heatmap_static
========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.spatial</p></div>

.. currentmodule:: dataviz.regression.spatial

.. autofunction:: panel_residual_heatmap_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.spatial import panel_residual_heatmap_static

   y_true = np.array([3.0, 2.5, 4.2, 5.0, 4.7])
   y_pred = np.array([2.8, 2.7, 4.0, 5.1, 4.5])
   train_sizes = np.array([50, 100, 200])
   train_scores = np.array([0.82, 0.86, 0.89])
   validation_scores = np.array([0.76, 0.81, 0.84])
   matrix = pd.DataFrame({"x1": [1.0, 1.1, 0.9, 1.2], "x2": [2.0, 2.1, 1.8, 2.2]})

   ax = panel_residual_heatmap_static(matrix)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/spatial/panel_residual_heatmap_static.png" alt="panel_residual_heatmap_static example output"><figcaption>Example output</figcaption></figure></div>
