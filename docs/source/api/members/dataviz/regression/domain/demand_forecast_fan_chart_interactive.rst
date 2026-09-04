dataviz.regression.domain.demand_forecast_fan_chart_interactive
===============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.domain</p></div>

.. currentmodule:: dataviz.regression.domain

.. autofunction:: demand_forecast_fan_chart_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.domain import demand_forecast_fan_chart_interactive

   rng = np.random.default_rng(42)
   time = np.arange(24)
   central = 100 + 2 * time + rng.normal(0.0, 1.0, size=24)
   quantile_bands = [(central - 5, central + 5), (central - 10, central + 10)]

   fig = demand_forecast_fan_chart_interactive(time, central, quantile_bands)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/domain/demand_forecast_fan_chart_interactive.png" alt="demand_forecast_fan_chart_interactive example output"><figcaption>Example output</figcaption></figure></div>
