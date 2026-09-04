dataviz.univariate.quality.quality_bar_static
=============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.quality</p></div>

.. currentmodule:: dataviz.univariate.quality

.. autofunction:: quality_bar_static

Use case
--------

Use to compare missing, duplicate, zero, and negative rates side by side when triaging data quality issues.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.univariate.quality import quality_bar_static

   rng = np.random.default_rng(42)
   readings = rng.normal(loc=55.0, scale=4.0, size=140).round(2)
   readings[[3, 27, 58, 91, 120]] = np.nan
   readings[[10, 66, 101]] = -999.0
   sensor = pd.Series(readings, name="temperature_c")
   ax = quality_bar_static(
       sensor,
       title="Sensor Feed Quality Rates",
       color="slategray",
       theme="minimal",
   )
   ax.set_ylabel("Rate of observations")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/quality/quality_bar_static.png" alt="quality_bar_static example output"><figcaption>Example output</figcaption></figure></div>
