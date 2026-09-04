dataviz.regression.metrics.metric_comparison_bar_interactive
============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.metrics</p></div>

.. currentmodule:: dataviz.regression.metrics

.. autofunction:: metric_comparison_bar_interactive

Use case
--------

Use to compare regression metrics across multiple models with a grouped bar chart.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   from dataviz.regression.metrics import metric_comparison_bar_interactive

   model_metrics = {
       "OLS": {"mae": 0.40, "rmse": 0.55, "r2": 0.93},
       "Ridge": {"mae": 0.42, "rmse": 0.57, "r2": 0.92},
   }

   fig = metric_comparison_bar_interactive(model_metrics)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/metrics/metric_comparison_bar_interactive.png" alt="metric_comparison_bar_interactive example output"><figcaption>Example output</figcaption></figure></div>
