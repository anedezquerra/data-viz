dataviz.regression.helpers.jackknife_plus_intervals
===================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.helpers</p></div>

.. currentmodule:: dataviz.regression.helpers

.. autofunction:: jackknife_plus_intervals

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.helpers import jackknife_plus_intervals

   rng = np.random.default_rng(42)
   leave_one_out_predictions = rng.normal(5.0, 1.0, size=(50, 10))
   y_calibration = rng.normal(5.0, 1.0, size=50)
   new_predictions = rng.normal(5.0, 1.0, size=10)

   result = jackknife_plus_intervals(
       leave_one_out_predictions, y_calibration, new_predictions, alpha=0.1
   )
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
