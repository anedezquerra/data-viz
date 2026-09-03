dataviz.regression.metrics.metric_radar_interactive
===================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.metrics</p></div>

.. currentmodule:: dataviz.regression.metrics

.. autofunction:: metric_radar_interactive

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

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
