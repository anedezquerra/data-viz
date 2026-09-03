dataviz.regression.errors_loss.loss_distribution_violin_static
==============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.errors_loss</p></div>

.. currentmodule:: dataviz.regression.errors_loss

.. autofunction:: loss_distribution_violin_static

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

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
