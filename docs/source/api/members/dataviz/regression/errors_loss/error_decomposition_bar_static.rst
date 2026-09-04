dataviz.regression.errors_loss.error_decomposition_bar_static
=============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.errors_loss</p></div>

.. currentmodule:: dataviz.regression.errors_loss

.. autofunction:: error_decomposition_bar_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.errors_loss import error_decomposition_bar_static

   values = pd.Series([12.1, 11.8, 13.0, 12.7, 14.2, 12.4], name="Value")
   y_true = np.array([3.0, 2.5, 4.2, 5.0, 4.7])
   y_pred = np.array([2.8, 2.7, 4.0, 5.1, 4.5])
   train_sizes = np.array([50, 100, 200])
   train_scores = np.array([0.82, 0.86, 0.89])
   validation_scores = np.array([0.76, 0.81, 0.84])

   ax = error_decomposition_bar_static(y_true, y_pred)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/errors_loss/error_decomposition_bar_static.png" alt="error_decomposition_bar_static example output"><figcaption>Example output</figcaption></figure></div>
