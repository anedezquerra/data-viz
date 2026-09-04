dataviz.regression.errors_loss.loss_distribution_violin_static
==============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.errors_loss</p></div>

.. currentmodule:: dataviz.regression.errors_loss

.. autofunction:: loss_distribution_violin_static

Use case
--------

Use to compare full per-observation loss distributions across models, catching heavy tails that mean error hides.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.errors_loss import loss_distribution_violin_static

   rng = np.random.default_rng(42)
   losses_per_model = [
       np.abs(rng.normal(0.0, 0.5, size=60)),
       np.abs(rng.normal(0.0, 0.8, size=60)),
   ]

   ax = loss_distribution_violin_static(["OLS", "Ridge"], losses_per_model, metric_name="MAE")
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/errors_loss/loss_distribution_violin_static.png" alt="loss_distribution_violin_static example output"><figcaption>Example output</figcaption></figure></div>
