dataviz.spc.variable.ewma_chart_interactive
===========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.variable</p></div>

.. currentmodule:: dataviz.spc.variable

.. autofunction:: ewma_chart_interactive

Use case
--------

Use to detect small sustained shifts in the process mean earlier than a Shewhart chart by weighting recent observations more heavily.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.spc.variable import ewma_chart_interactive

   rng = np.random.default_rng(42)
   data = rng.normal(loc=10.0, scale=0.4, size=30)
   data[24] = 11.8  # Deliberate special-cause signal

   fig = ewma_chart_interactive(data, lambda_=0.2)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/variable/ewma_chart_interactive.png" alt="ewma_chart_interactive example output"><figcaption>Example output</figcaption></figure></div>
