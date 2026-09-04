dataviz.regression.coefficients.coefficient_plot_static
=======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.coefficients</p></div>

.. currentmodule:: dataviz.regression.coefficients

.. autofunction:: coefficient_plot_static

Use case
--------

Use for a quick read of coefficient magnitude and sign, colored by direction, when communicating which drivers push predictions up or down.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.coefficients import coefficient_plot_static

   features = ["temperature_c", "pressure_bar", "catalyst_g", "residence_min",
               "humidity_pct"]
   coefs = np.array([1.85, -0.42, 2.30, 0.66, -0.12])

   ax = coefficient_plot_static(coefs, feature_names=features,
                                title="Polymer Yield Model: Coefficients",
                                positive_color="#2a7f62",
                                negative_color="#c0392b", sort=True)
   ax.set_xlabel("Coefficient (kg yield per unit)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/coefficients/coefficient_plot_static.png" alt="coefficient_plot_static example output"><figcaption>Example output</figcaption></figure></div>
