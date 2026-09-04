dataviz.spc.attribute.t_chart_interactive
=========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.attribute</p></div>

.. currentmodule:: dataviz.spc.attribute

.. autofunction:: t_chart_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.spc.attribute import t_chart_interactive

   rng = np.random.default_rng(42)
   times = rng.exponential(scale=2.0, size=30)

   fig = t_chart_interactive(times, title="Hours between failures")
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/attribute/t_chart_interactive.png" alt="t_chart_interactive example output"><figcaption>Example output</figcaption></figure></div>
