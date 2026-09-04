dataviz.spc.diagnostics.pareto_chart_interactive
================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.diagnostics</p></div>

.. currentmodule:: dataviz.spc.diagnostics

.. autofunction:: pareto_chart_interactive

Use case
--------

Use to rank defect categories by frequency so improvement teams target the vital few causes driving most nonconformances.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   from dataviz.spc.diagnostics import pareto_chart_interactive

   # Surface defect tally from a quarter of final visual inspection
   categories = ["Scratch", "Dent", "Contamination", "Misprint", "Crack", "Discoloration"]
   counts = [87, 54, 38, 22, 11, 6]

   fig = pareto_chart_interactive(categories, counts, title="Q3 Surface Defect Pareto")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/diagnostics/pareto_chart_interactive.png" alt="pareto_chart_interactive example output"><figcaption>Example output</figcaption></figure></div>
