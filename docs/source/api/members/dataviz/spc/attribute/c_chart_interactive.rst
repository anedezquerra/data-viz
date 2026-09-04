dataviz.spc.attribute.c_chart_interactive
=========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.attribute</p></div>

.. currentmodule:: dataviz.spc.attribute

.. autofunction:: c_chart_interactive

Use case
--------

Use when counting defects per inspection unit of constant size, such as flaws per painted panel or solder defects per board.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.spc.attribute import c_chart_interactive

   rng = np.random.default_rng(42)
   # Surface defects counted on 28 painted panels (constant inspection area)
   defects = rng.poisson(3.5, size=28)
   defects[21] = 14  # spray nozzle clog on panel 21

   fig = c_chart_interactive(defects, title="Painted Panels - Surface Defects per Panel")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/attribute/c_chart_interactive.png" alt="c_chart_interactive example output"><figcaption>Example output</figcaption></figure></div>
