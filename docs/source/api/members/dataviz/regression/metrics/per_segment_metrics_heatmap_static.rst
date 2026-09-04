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
   import matplotlib.pyplot as plt
   from dataviz.regression.metrics import per_segment_metrics_heatmap_static

   rng = np.random.default_rng(42)
   y_true = rng.normal(10.0, 2.0, size=60)
   y_pred = y_true + rng.normal(0.0, 0.5, size=60)
   segments = rng.choice(["A", "B", "C"], size=60)

   ax = per_segment_metrics_heatmap_static(y_true, y_pred, segments)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/metrics/per_segment_metrics_heatmap_static.png" alt="per_segment_metrics_heatmap_static example output"><figcaption>Example output</figcaption></figure></div>
