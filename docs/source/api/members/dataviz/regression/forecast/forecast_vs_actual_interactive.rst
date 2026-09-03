dataviz.regression.forecast.forecast_vs_actual_interactive
==========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.forecast</p></div>

.. currentmodule:: dataviz.regression.forecast

.. autofunction:: forecast_vs_actual_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.forecast import forecast_vs_actual_interactive

   rng = np.random.default_rng(42)
   time = np.arange(60)
   y_true = 10 + 0.1 * time + rng.normal(0.0, 1.0, size=60)
   y_pred = y_true + rng.normal(0.0, 0.5, size=60)

   fig = forecast_vs_actual_interactive(time, y_true, y_pred)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/regression/forecast/forecast_vs_actual_interactive.png" alt="forecast_vs_actual_interactive example output"><figcaption>Example output</figcaption></figure></div>
