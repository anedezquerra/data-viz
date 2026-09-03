dataviz.spc.x_range.x_range_chart_interactive
=============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.x_range</p></div>

.. currentmodule:: dataviz.spc.x_range

.. autofunction:: x_range_chart_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.spc.x_range import x_range_chart_interactive

   rng = np.random.default_rng(42)
   data = rng.normal(loc=10.0, scale=0.4, size=30)
   data[24] = 11.8  # Deliberate special-cause signal

   fig = x_range_chart_interactive(data, subgroup_size=5)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/spc/x_range/x_range_chart_interactive.png" alt="x_range_chart_interactive example output"><figcaption>Example output</figcaption></figure></div>
