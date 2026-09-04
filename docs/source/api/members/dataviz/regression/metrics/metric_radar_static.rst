dataviz.regression.metrics.metric_radar_static
==============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.metrics</p></div>

.. currentmodule:: dataviz.regression.metrics

.. autofunction:: metric_radar_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import matplotlib.pyplot as plt
   from dataviz.regression.metrics import metric_radar_static

   model_metrics = {
       "OLS": {"mae": 0.40, "rmse": 0.55, "medae": 0.30, "r2": 0.93,
               "explained_variance": 0.94},
       "Ridge": {"mae": 0.42, "rmse": 0.57, "medae": 0.33, "r2": 0.92,
                 "explained_variance": 0.93},
   }

   ax = metric_radar_static(model_metrics)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/regression/metrics/metric_radar_static.png" alt="metric_radar_static example output"><figcaption>Example output</figcaption></figure></div>
