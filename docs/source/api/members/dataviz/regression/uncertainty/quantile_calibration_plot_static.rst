dataviz.regression.uncertainty.quantile_calibration_plot_static
===============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.uncertainty</p></div>

.. currentmodule:: dataviz.regression.uncertainty

.. autofunction:: quantile_calibration_plot_static

Use case
--------

Use to check whether predicted quantiles are calibrated by plotting nominal vs empirical coverage against the ideal diagonal.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.uncertainty import quantile_calibration_plot_static

   nominal = np.linspace(0.05, 0.95, 19)
   empirical = nominal + 0.04 * np.sin(2 * np.pi * nominal) - 0.015

   ax = quantile_calibration_plot_static(
       nominal, empirical,
       title="Rainfall quantile regression: nominal vs empirical coverage",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/uncertainty/quantile_calibration_plot_static.png" alt="quantile_calibration_plot_static example output"><figcaption>Example output</figcaption></figure></div>
