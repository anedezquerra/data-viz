dataviz.classification.threshold_extra.f_beta_curve_static
==========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.threshold_extra</p></div>

.. currentmodule:: dataviz.classification.threshold_extra

.. autofunction:: f_beta_curve_static

Use case
--------

Use when recall matters more or less than precision; sweeps F-beta for several beta values across thresholds.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python


   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.threshold_extra import f_beta_curve_static

   rng = np.random.default_rng(42)
   y_prob = rng.beta(2.0, 5.0, size=200)
   y_true = rng.binomial(1, y_prob)

   ax = f_beta_curve_static(y_true, y_prob)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/threshold_extra/f_beta_curve_static.png" alt="f_beta_curve_static example output"><figcaption>Example output</figcaption></figure></div>
