dataviz.spc.attribute.laney_p_chart_interactive
===============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.attribute</p></div>

.. currentmodule:: dataviz.spc.attribute

.. autofunction:: laney_p_chart_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.spc.attribute import laney_p_chart_interactive

   rng = np.random.default_rng(42)
   defects = rng.binomial(n=100, p=0.05, size=30)
   sample_sizes = rng.integers(low=80, high=150, size=30)

   fig = laney_p_chart_interactive(defects, sample_sizes, title="Defect rate (p')")
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/attribute/laney_p_chart_interactive.png" alt="laney_p_chart_interactive example output"><figcaption>Example output</figcaption></figure></div>
