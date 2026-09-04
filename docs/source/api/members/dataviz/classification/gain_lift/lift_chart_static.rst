dataviz.classification.gain_lift.lift_chart_static
==================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.gain_lift</p></div>

.. currentmodule:: dataviz.classification.gain_lift

.. autofunction:: lift_chart_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python


   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.gain_lift import lift_chart_static

   rng = np.random.default_rng(42)
   y_prob = rng.beta(2.0, 5.0, size=200)
   y_true = rng.binomial(1, y_prob)

   ax = lift_chart_static(y_true, y_prob)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/gain_lift/lift_chart_static.png" alt="lift_chart_static example output"><figcaption>Example output</figcaption></figure></div>
