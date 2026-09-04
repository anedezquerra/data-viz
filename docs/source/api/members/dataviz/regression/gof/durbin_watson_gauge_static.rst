dataviz.regression.gof.durbin_watson_gauge_static
=================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.gof</p></div>

.. currentmodule:: dataviz.regression.gof

.. autofunction:: durbin_watson_gauge_static

Use case
--------

Use to read the Durbin-Watson statistic on a 0-4 gauge when checking residuals for autocorrelation.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.gof import durbin_watson_gauge_static

   rng = np.random.default_rng(42)
   residuals = rng.normal(0.0, 1.0, size=80)

   ax = durbin_watson_gauge_static(residuals)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/gof/durbin_watson_gauge_static.png" alt="durbin_watson_gauge_static example output"><figcaption>Example output</figcaption></figure></div>
