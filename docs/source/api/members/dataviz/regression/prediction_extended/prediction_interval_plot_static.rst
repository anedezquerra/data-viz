dataviz.regression.prediction_extended.prediction_interval_plot_static
======================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.prediction_extended</p></div>

.. currentmodule:: dataviz.regression.prediction_extended

.. autofunction:: prediction_interval_plot_static

Use case
--------

Use to show predictions with an empirical or Gaussian interval band and see which actuals fall outside it.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.prediction_extended import prediction_interval_plot_static

   rng = np.random.default_rng(42)
   patients = pd.Series(np.arange(1, 31), name="patient")
   actual_charge = pd.Series(
       rng.uniform(8, 60, 30).round(1), name="actual_charge_kusd"
   ).sort_values().reset_index(drop=True)
   predicted_charge = pd.Series(
       actual_charge + rng.normal(0, 4.5, 30), name="predicted_charge_kusd"
   )

   ax = prediction_interval_plot_static(
       actual_charge, predicted_charge, confidence=0.90, method="empirical",
       title="Hospital charge model: 90% prediction intervals",
       point_color="#2a6f97", band_color="#a8d5e5", line_color="#d62728",
       theme="minimal",
   )
   ax.set_ylabel("Charge (thousand USD)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/prediction_extended/prediction_interval_plot_static.png" alt="prediction_interval_plot_static example output"><figcaption>Example output</figcaption></figure></div>
