dataviz.regression.domain.demand_forecast_fan_chart_static
==========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.domain</p></div>

.. currentmodule:: dataviz.regression.domain

.. autofunction:: demand_forecast_fan_chart_static

Use case
--------

Use to present demand forecasts with nested quantile bands, communicating growing uncertainty the further out the horizon extends.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.domain import demand_forecast_fan_chart_static

   weeks = pd.Series(np.arange(1, 21), name="week_ahead")
   central = pd.Series(1000 * (1.02 ** weeks), name="central_forecast")
   spread = 30 * np.sqrt(weeks)
   bands = [(central - 1.96 * spread, central + 1.96 * spread),
            (central - 1.28 * spread, central + 1.28 * spread),
            (central - 0.67 * spread, central + 0.67 * spread)]

   ax = demand_forecast_fan_chart_static(
       weeks, central, bands,
       title="Grocery SKU: 20-Week Demand Forecast Fan",
       color="#c0392b", cmap="Blues")
   ax.set_xlabel("Weeks ahead")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/domain/demand_forecast_fan_chart_static.png" alt="demand_forecast_fan_chart_static example output"><figcaption>Example output</figcaption></figure></div>
