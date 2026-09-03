dataviz.spc.attribute.g_chart_interactive
=========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.attribute</p></div>

.. currentmodule:: dataviz.spc.attribute

.. autofunction:: g_chart_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.spc.attribute import g_chart_interactive

   rng = np.random.default_rng(42)
   counts = rng.geometric(p=0.02, size=30)

   fig = g_chart_interactive(counts, title="Units between defects")
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/spc/attribute/g_chart_interactive.png" alt="g_chart_interactive example output"><figcaption>Example output</figcaption></figure></div>
