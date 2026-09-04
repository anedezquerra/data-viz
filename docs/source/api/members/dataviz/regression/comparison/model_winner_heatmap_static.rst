dataviz.regression.comparison.model_winner_heatmap_static
=========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.comparison</p></div>

.. currentmodule:: dataviz.regression.comparison

.. autofunction:: model_winner_heatmap_static

Use case
--------

Use to summarize which model wins on each metric in one matrix, avoiding cherry-picking a single score when selecting a champion.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.comparison import model_winner_heatmap_static

   models = ["Linear", "Random Forest", "XGBoost"]
   metrics = ["MAE", "RMSE", "MAPE", "R2"]
   wins = np.array([[0, 0, 0, 0],
                    [1, 0, 1, 0],
                    [0, 1, 0, 1]])

   ax = model_winner_heatmap_static(models, metrics, wins,
                                    title="Warranty Cost Models: Winner per Metric",
                                    cmap="YlGn")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/comparison/model_winner_heatmap_static.png" alt="model_winner_heatmap_static example output"><figcaption>Example output</figcaption></figure></div>
