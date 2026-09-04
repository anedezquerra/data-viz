dataviz.regression.forecast.expanding_window_metric_curve_static
================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.forecast</p></div>

.. currentmodule:: dataviz.regression.forecast

.. autofunction:: expanding_window_metric_curve_static

Use case
--------

Use to see whether forecast accuracy improves as the training window expands.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.forecast import expanding_window_metric_curve_static

   rng = np.random.default_rng(42)
   window_sizes = np.arange(30, 211, 20)
   r2_curve = pd.Series(1.0 - np.exp(-window_sizes / 90.0) + rng.normal(0, 0.01, 10),
                        index=window_sizes, name="cv_r2")

   ax = expanding_window_metric_curve_static(
       window_sizes, r2_curve,
       title="Ticket Volume Model: R2 vs Expanding Training Window",
       metric_name="CV R-squared", color="#e377c2")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/forecast/expanding_window_metric_curve_static.png" alt="expanding_window_metric_curve_static example output"><figcaption>Example output</figcaption></figure></div>
