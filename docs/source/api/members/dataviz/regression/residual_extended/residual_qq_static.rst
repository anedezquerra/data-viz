dataviz.regression.residual_extended.residual_qq_static
=======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.residual_extended</p></div>

.. currentmodule:: dataviz.regression.residual_extended

.. autofunction:: residual_qq_static

Use case
--------

Use to test the normality assumption by plotting residual quantiles against a normal reference line.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.residual_extended import residual_qq_static

   rng = np.random.default_rng(42)
   wells = pd.Series(np.arange(1, 31), name="well")
   actual_flow = pd.Series(rng.normal(540, 80, 30).round(1), name="actual_bpd")
   predicted_flow = pd.Series(
       actual_flow + rng.normal(0, 35, 30), name="predicted_bpd"
   )

   ax = residual_qq_static(
       actual_flow, predicted_flow,
       title="Oil well flow model: normal Q-Q of residuals",
       marker_color="#1b9e77", line_color="#d62728", theme="minimal",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/residual_extended/residual_qq_static.png" alt="residual_qq_static example output"><figcaption>Example output</figcaption></figure></div>
