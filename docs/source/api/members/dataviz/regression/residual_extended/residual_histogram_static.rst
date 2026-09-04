dataviz.regression.residual_extended.residual_histogram_static
==============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.residual_extended</p></div>

.. currentmodule:: dataviz.regression.residual_extended

.. autofunction:: residual_histogram_static

Use case
--------

Use to check whether residuals are roughly centered and symmetric, with an optional normal overlay.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.residual_extended import residual_histogram_static

   rng = np.random.default_rng(42)
   patients = pd.Series(np.arange(1, 41), name="patient")
   actual_bp = pd.Series(rng.normal(128, 14, 40).round(1), name="actual_sbp")
   predicted_bp = pd.Series(
       actual_bp + rng.normal(0, 6.5, 40), name="predicted_sbp"
   )

   ax = residual_histogram_static(
       actual_bp, predicted_bp, bins=12,
       title="Blood-pressure model: residual distribution",
       color="#4878d0", edgecolor="white", overlay_color="#d62728",
       theme="minimal",
   )
   ax.set_xlabel("Residual (mmHg)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/residual_extended/residual_histogram_static.png" alt="residual_histogram_static example output"><figcaption>Example output</figcaption></figure></div>
