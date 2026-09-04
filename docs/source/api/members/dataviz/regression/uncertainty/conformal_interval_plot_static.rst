dataviz.regression.uncertainty.conformal_interval_plot_static
=============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.uncertainty</p></div>

.. currentmodule:: dataviz.regression.uncertainty

.. autofunction:: conformal_interval_plot_static

Use case
--------

Use to audit conformal prediction intervals by viewing the band, predictions, and actuals sorted by prediction; uncovered points reveal weak coverage.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.uncertainty import conformal_interval_plot_static

   rng = np.random.default_rng(42)
   y_true = rng.normal(10.0, 2.0, size=60)
   y_pred = y_true + rng.normal(0.0, 0.5, size=60)
   lower = y_pred - 1.0
   upper = y_pred + 1.0

   ax = conformal_interval_plot_static(y_true, y_pred, lower, upper)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/uncertainty/conformal_interval_plot_static.png" alt="conformal_interval_plot_static example output"><figcaption>Example output</figcaption></figure></div>
