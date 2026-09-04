dataviz.spc.diagnostics.pareto_chart_static
===========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.diagnostics</p></div>

.. currentmodule:: dataviz.spc.diagnostics

.. autofunction:: pareto_chart_static

Use case
--------

Use to rank defect categories by frequency so improvement teams target the vital few causes driving most nonconformances.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import matplotlib.pyplot as plt
   from dataviz.spc.diagnostics import pareto_chart_static

   # Surface defect tally from a quarter of final visual inspection
   categories = ["Scratch", "Dent", "Contamination", "Misprint", "Crack", "Discoloration"]
   counts = [87, 54, 38, 22, 11, 6]

   ax = pareto_chart_static(categories, counts, title="Q3 Surface Defect Pareto")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/diagnostics/pareto_chart_static.png" alt="pareto_chart_static example output"><figcaption>Example output</figcaption></figure></div>
