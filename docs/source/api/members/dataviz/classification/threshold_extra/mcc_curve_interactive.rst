dataviz.classification.threshold_extra.mcc_curve_interactive
============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.threshold_extra</p></div>

.. currentmodule:: dataviz.classification.threshold_extra

.. autofunction:: mcc_curve_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python


   import numpy as np
   from dataviz.classification.threshold_extra import mcc_curve_interactive

   rng = np.random.default_rng(42)
   y_prob = rng.beta(2.0, 5.0, size=200)
   y_true = rng.binomial(1, y_prob)

   fig = mcc_curve_interactive(y_true, y_prob)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/threshold_extra/mcc_curve_interactive.png" alt="mcc_curve_interactive example output"><figcaption>Example output</figcaption></figure></div>
