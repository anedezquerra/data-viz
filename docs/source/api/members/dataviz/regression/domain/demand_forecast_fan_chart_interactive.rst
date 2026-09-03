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

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
