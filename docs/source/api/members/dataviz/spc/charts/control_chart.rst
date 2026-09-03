dataviz.spc.charts.control_chart
================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.charts</p></div>

.. currentmodule:: dataviz.spc.charts

.. autofunction:: control_chart

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.spc.charts import control_chart

   rng = np.random.default_rng(42)
   data = rng.normal(loc=10.0, scale=0.4, size=30)
   data[24] = 11.8  # Deliberate special-cause signal

   ax = control_chart(data, title="Filling process")
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/spc/charts/control_chart.png" alt="control_chart example output"><figcaption>Example output</figcaption></figure></div>
