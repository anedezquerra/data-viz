dataviz.regression.var_engineering.target_encoding_curve_static
===============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.var_engineering</p></div>

.. currentmodule:: dataviz.regression.var_engineering

.. autofunction:: target_encoding_curve_static

Use case
--------

Use to sanity-check target encoding by plotting category mean target vs sample size; small-n categories far from the prior are unreliable.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.var_engineering import target_encoding_curve_static

   y_true = np.array([3.0, 2.5, 4.2, 5.0, 4.7])
   y_pred = np.array([2.8, 2.7, 4.0, 5.1, 4.5])
   train_sizes = np.array([50, 100, 200])
   train_scores = np.array([0.82, 0.86, 0.89])
   validation_scores = np.array([0.76, 0.81, 0.84])

   ax = target_encoding_curve_static(y_true, y_pred)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/var_engineering/target_encoding_curve_static.png" alt="target_encoding_curve_static example output"><figcaption>Example output</figcaption></figure></div>
