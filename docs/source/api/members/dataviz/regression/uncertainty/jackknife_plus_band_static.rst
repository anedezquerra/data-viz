dataviz.regression.uncertainty.jackknife_plus_band_static
=========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.uncertainty</p></div>

.. currentmodule:: dataviz.regression.uncertainty

.. autofunction:: jackknife_plus_band_static

Use case
--------

Use to visualize jackknife+ predictive bands around sorted predictions and see where actuals fall outside the interval.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.uncertainty import jackknife_plus_band_static

   rng = np.random.default_rng(42)
   n = 30
   load_mw = 450 + 120 * np.sin(np.linspace(0, 2 * np.pi, n)) + rng.normal(0, 18, n)
   pred_mw = 450 + 120 * np.sin(np.linspace(0, 2 * np.pi, n))
   half_width = 25 + 8 * np.abs(np.sin(np.linspace(0, np.pi, n)))
   lower, upper = pred_mw - half_width, pred_mw + half_width

   ax = jackknife_plus_band_static(
       load_mw, pred_mw, lower, upper,
       title="Grid load forecast: jackknife+ 90% predictive band",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/uncertainty/jackknife_plus_band_static.png" alt="jackknife_plus_band_static example output"><figcaption>Example output</figcaption></figure></div>
