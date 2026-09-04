dataviz.spc.attribute.u_chart_interactive
=========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.attribute</p></div>

.. currentmodule:: dataviz.spc.attribute

.. autofunction:: u_chart_interactive

Use case
--------

Use when tracking defects per unit across samples of varying size, such as scratches per square meter of rolled sheet.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.spc.attribute import u_chart_interactive

   rng = np.random.default_rng(42)
   # Defects per fabric roll with varying roll lengths
   units = rng.integers(8, 16, size=30)
   defects = rng.poisson(units * 0.4)
   defects[22] = 18  # loom tension fault on roll 22

   fig = u_chart_interactive(defects, units, title="Fabric Rolls - Defects per Unit")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/attribute/u_chart_interactive.png" alt="u_chart_interactive example output"><figcaption>Example output</figcaption></figure></div>
