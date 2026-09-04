dataviz.regression.transforms.log_log_diagnostic_static
=======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.transforms</p></div>

.. currentmodule:: dataviz.regression.transforms

.. autofunction:: log_log_diagnostic_static

Use case
--------

Use to test a power-law relationship between x and y; a straight line in log-log space justifies a log-log model and its slope is the exponent.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.transforms import log_log_diagnostic_static

   rng = np.random.default_rng(42)
   n = 38
   city_area = rng.uniform(20, 900, n)                    # km^2
   population = 4200 * city_area ** 0.85 * np.exp(rng.normal(0, 0.18, n))

   ax = log_log_diagnostic_static(
       city_area, population,
       title="Urban scaling study: log-log check of area vs population",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/transforms/log_log_diagnostic_static.png" alt="log_log_diagnostic_static example output"><figcaption>Example output</figcaption></figure></div>
