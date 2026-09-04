dataviz.spc.diagnostics.pareto_chart_interactive
================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.diagnostics</p></div>

.. currentmodule:: dataviz.spc.diagnostics

.. autofunction:: pareto_chart_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.spc.diagnostics import pareto_chart_interactive

   categories = ["Surface", "Dimension", "Assembly", "Packaging"]
   counts = [38, 24, 13, 7]

   fig = pareto_chart_interactive(categories, counts, title="Defect priorities")
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/diagnostics/pareto_chart_interactive.png" alt="pareto_chart_interactive example output"><figcaption>Example output</figcaption></figure></div>
