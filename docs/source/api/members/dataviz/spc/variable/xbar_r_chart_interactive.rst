dataviz.spc.variable.xbar_r_chart_interactive
=============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.variable</p></div>

.. currentmodule:: dataviz.spc.variable

.. autofunction:: xbar_r_chart_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.spc.variable import xbar_r_chart_interactive

   rng = np.random.default_rng(42)
   data = rng.normal(loc=10.0, scale=0.35, size=(20, 5))

   fig = xbar_r_chart_interactive(data)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/spc/variable/xbar_r_chart_interactive.png" alt="xbar_r_chart_interactive example output"><figcaption>Example output</figcaption></figure></div>
