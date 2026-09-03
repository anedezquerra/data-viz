dataviz.regression.survival.km_predicted_vs_observed_static
===========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.survival</p></div>

.. currentmodule:: dataviz.regression.survival

.. autofunction:: km_predicted_vs_observed_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.survival import km_predicted_vs_observed_static

   times = np.linspace(0.0, 24.0, 25)
   km_observed = np.exp(-times / 18.0)
   km_predicted = np.exp(-times / 20.0)

   ax = km_predicted_vs_observed_static(times, km_observed, km_predicted)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/regression/survival/km_predicted_vs_observed_static.png" alt="km_predicted_vs_observed_static example output"><figcaption>Example output</figcaption></figure></div>
