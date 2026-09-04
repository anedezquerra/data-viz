dataviz.regression.diagnostics_panel.regression_dashboard_static
================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.diagnostics_panel</p></div>

.. currentmodule:: dataviz.regression.diagnostics_panel

.. autofunction:: regression_dashboard_static

Use case
--------

Use for a compact model overview combining predicted-vs-actual, residual scatter, error histogram, and summary metrics.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.diagnostics_panel import regression_dashboard_static

   rng = np.random.default_rng(42)
   n = 32
   actual = pd.Series(rng.uniform(15, 90, n), name="actual_wait_min")
   predicted = pd.Series(actual + rng.normal(0, 6, n), name="predicted_wait_min")

   fig = regression_dashboard_static(
       actual, predicted, n_features=4,
       title="Clinic Wait-Time Model: Performance Dashboard",
       color="#2a7f62", line_color="#c0392b")
   fig.legend(loc="lower center", bbox_to_anchor=(0.5, -0.05), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/diagnostics_panel/regression_dashboard_static.png" alt="regression_dashboard_static example output"><figcaption>Example output</figcaption></figure></div>
