dataviz.xai.uncertainty.prediction_uncertainty_plot_static
==========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.uncertainty</p></div>

.. currentmodule:: dataviz.xai.uncertainty

.. autofunction:: prediction_uncertainty_plot_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.xai.uncertainty import prediction_uncertainty_plot_static

   rng = np.random.default_rng(53)
   feature_values = np.sort(rng.uniform(20.0, 80.0, 40))
   predictions = 1.0 / (1.0 + np.exp(-(feature_values - 50.0) / 10.0))
   uncertainty = 0.05 + 0.04 * np.abs(feature_values - 50.0) / 30.0

   ax = prediction_uncertainty_plot_static(
       feature_values, predictions, uncertainty, feature_name="income",
   )
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/xai/uncertainty/prediction_uncertainty_plot_static.png" alt="prediction_uncertainty_plot_static example output"><figcaption>Example output</figcaption></figure></div>
