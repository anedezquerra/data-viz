dataviz.univariate.diagnostics.univariate_diagnostic_panel_static
=================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.diagnostics</p></div>

.. currentmodule:: dataviz.univariate.diagnostics

.. autofunction:: univariate_diagnostic_panel_static

Use case
--------

Use to run a four-panel diagnostic figure when you want a quick, broad health check of one variable in a single view.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.univariate.diagnostics import univariate_diagnostic_panel_static

   # Patient systolic blood pressure readings from a screening clinic
   rng = np.random.default_rng(42)
   systolic = pd.Series(
       np.round(rng.normal(loc=126.0, scale=14.0, size=50), 0),
       name="systolic_mmhg",
   )

   fig = univariate_diagnostic_panel_static(
       systolic,
       bins=14,
       title="Systolic Blood Pressure Diagnostics",
       color="cadetblue",
       theme="default",
   )
   fig.legend(loc="lower center", bbox_to_anchor=(0.5, -0.05), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/diagnostics/univariate_diagnostic_panel_static.png" alt="univariate_diagnostic_panel_static example output"><figcaption>Example output</figcaption></figure></div>
