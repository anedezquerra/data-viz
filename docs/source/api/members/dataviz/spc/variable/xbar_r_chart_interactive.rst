dataviz.spc.variable.xbar_r_chart_interactive
=============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.variable</p></div>

.. currentmodule:: dataviz.spc.variable

.. autofunction:: xbar_r_chart_interactive

Use case
--------

Use when monitoring subgrouped measurements of small size (2-10) to track both process center and within-subgroup spread.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.spc.variable import xbar_r_chart_interactive

   rng = np.random.default_rng(42)
   # Shaft diameters (mm): 25 subgroups of 5 parts from a CNC lathe
   diameters = rng.normal(25.0, 0.08, size=125)
   diameters[100:105] += 0.25  # tool wear shift in subgroup 20

   fig = xbar_r_chart_interactive(
       diameters, subgroup_size=5, title="Shaft Diameter Xbar-R Chart"
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/variable/xbar_r_chart_interactive.png" alt="xbar_r_chart_interactive example output"><figcaption>Example output</figcaption></figure></div>
