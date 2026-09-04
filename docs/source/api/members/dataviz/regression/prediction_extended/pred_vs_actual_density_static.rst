dataviz.regression.prediction_extended.pred_vs_actual_density_static
====================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.prediction_extended</p></div>

.. currentmodule:: dataviz.regression.prediction_extended

.. autofunction:: pred_vs_actual_density_static

Use case
--------

Use to compare the marginal distributions of actual and predicted values and expose systematic shift or shrinkage.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.prediction_extended import pred_vs_actual_density_static

   rng = np.random.default_rng(42)
   rides = pd.Series(np.arange(1, 61), name="ride")
   actual_fare = pd.Series(rng.lognormal(2.8, 0.45, 60), name="actual_fare_usd")
   predicted_fare = pd.Series(
       0.9 * actual_fare + 1.5 + rng.normal(0, 1.8, 60), name="predicted_fare_usd"
   )

   ax = pred_vs_actual_density_static(
       actual_fare, predicted_fare, bins=24,
       title="Ride-hailing fares: actual vs predicted distributions",
       actual_color="#4878d0", predicted_color="#ee854a",
       alpha=0.45, theme="minimal",
   )
   ax.set_xlabel("Fare (USD)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/prediction_extended/pred_vs_actual_density_static.png" alt="pred_vs_actual_density_static example output"><figcaption>Example output</figcaption></figure></div>
