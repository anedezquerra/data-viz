dataviz.classification.calibration.probability_density_static
=============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.calibration</p></div>

.. currentmodule:: dataviz.classification.calibration

.. autofunction:: probability_density_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python


   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.calibration import probability_density_static

   rng = np.random.default_rng(42)
   y_prob = rng.beta(2.0, 5.0, size=200)
   y_true = rng.binomial(1, y_prob)

   ax = probability_density_static(y_true, y_prob)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/classification/calibration/probability_density_static.png" alt="probability_density_static example output"><figcaption>Example output</figcaption></figure></div>
