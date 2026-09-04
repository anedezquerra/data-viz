dataviz.univariate.categorical.pareto_chart_static
==================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.categorical</p></div>

.. currentmodule:: dataviz.univariate.categorical

.. autofunction:: pareto_chart_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.univariate.categorical import pareto_chart_static

   values = pd.Series([12.1, 11.8, 13.0, 12.7, 14.2, 12.4], name="Value")
   categories = pd.Series(["low", "medium", "high", "medium", "low"], name="Priority")

   ax = pareto_chart_static(values)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/categorical/pareto_chart_static.png" alt="pareto_chart_static example output"><figcaption>Example output</figcaption></figure></div>
