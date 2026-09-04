dataviz.regression.metrics.metric_radar_interactive
===================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.metrics</p></div>

.. currentmodule:: dataviz.regression.metrics

.. autofunction:: metric_radar_interactive

Use case
--------

Use to compare normalized metric profiles of several models at a glance on a radar chart.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   from dataviz.regression.metrics import metric_radar_interactive

   model_metrics = {
       "OLS": {"mae": 0.40, "rmse": 0.55, "medae": 0.30, "r2": 0.93,
               "explained_variance": 0.94},
       "Ridge": {"mae": 0.42, "rmse": 0.57, "medae": 0.33, "r2": 0.92,
                 "explained_variance": 0.93},
   }

   fig = metric_radar_interactive(model_metrics)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/metrics/metric_radar_interactive.png" alt="metric_radar_interactive example output"><figcaption>Example output</figcaption></figure></div>
