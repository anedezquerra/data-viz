dataviz.regression.gof.breusch_pagan_plot_static
================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.gof</p></div>

.. currentmodule:: dataviz.regression.gof

.. autofunction:: breusch_pagan_plot_static

Use case
--------

Use to check heteroscedasticity by plotting squared residuals against fitted values with the BP statistic.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.gof import breusch_pagan_plot_static

   rng = np.random.default_rng(42)
   n = 36
   machine_speed = rng.uniform(200.0, 900.0, n)
   tool_age_hrs = rng.uniform(10.0, 500.0, n)
   X = pd.DataFrame({"machine_speed_rpm": machine_speed,
                      "tool_age_hrs": tool_age_hrs})
   residuals = pd.Series(rng.normal(0.0, 0.5 + 0.002 * machine_speed, n),
                         name="roughness_residuals_um")

   ax = breusch_pagan_plot_static(X, residuals,
                                  title="Milling Line: Breusch-Pagan Test",
                                  color="#d62728")
   ax.set_ylabel("Squared residual")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/gof/breusch_pagan_plot_static.png" alt="breusch_pagan_plot_static example output"><figcaption>Example output</figcaption></figure></div>
