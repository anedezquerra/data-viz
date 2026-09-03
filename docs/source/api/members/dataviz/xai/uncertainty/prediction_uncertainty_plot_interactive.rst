dataviz.xai.uncertainty.prediction_uncertainty_plot_interactive
===============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.uncertainty</p></div>

.. currentmodule:: dataviz.xai.uncertainty

.. autofunction:: prediction_uncertainty_plot_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.xai.uncertainty import prediction_uncertainty_plot_interactive

   rng = np.random.default_rng(53)
   feature_values = np.sort(rng.uniform(20.0, 80.0, 40))
   predictions = 1.0 / (1.0 + np.exp(-(feature_values - 50.0) / 10.0))
   uncertainty = 0.05 + 0.04 * np.abs(feature_values - 50.0) / 30.0

   fig = prediction_uncertainty_plot_interactive(
       feature_values, predictions, uncertainty, feature_name="income",
   )
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
