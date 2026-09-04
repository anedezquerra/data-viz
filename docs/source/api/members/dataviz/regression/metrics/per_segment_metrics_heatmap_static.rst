dataviz.regression.metrics.per_segment_metrics_heatmap_static
=============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.metrics</p></div>

.. currentmodule:: dataviz.regression.metrics

.. autofunction:: per_segment_metrics_heatmap_static

Use case
--------

Use to compare model performance across data segments with a metrics heatmap.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.metrics import per_segment_metrics_heatmap_static

   rng = np.random.default_rng(42)
   n = 24
   segments = pd.Series(np.repeat(["urban", "suburban", "rural"], 8),
                        name="store_region")
   y = pd.Series(100.0 + rng.normal(0.0, 15.0, n), name="monthly_sales_kusd")
   y_pred = y - rng.normal(0.0, 6.0, n) + np.where(segments == "rural", 8.0, 0.0)

   ax = per_segment_metrics_heatmap_static(
       y, y_pred, segments, metrics=("mae", "rmse", "r2"),
       title="Retail Sales Model: Metrics by Region", cmap="viridis")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/metrics/per_segment_metrics_heatmap_static.png" alt="per_segment_metrics_heatmap_static example output"><figcaption>Example output</figcaption></figure></div>
