dataviz.spc.variable.xbar_s_chart_interactive
=============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.variable</p></div>

.. currentmodule:: dataviz.spc.variable

.. autofunction:: xbar_s_chart_interactive

Use case
--------

Use when monitoring larger subgroups where the standard deviation tracks within-subgroup spread more precisely than the range.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.spc.variable import xbar_s_chart_interactive

   rng = np.random.default_rng(42)
   # Viscosity readings (cP): 22 subgroups of 6 samples per batch
   viscosity = rng.normal(350.0, 4.0, size=132)
   viscosity[90:96] += 14.0  # raw-material change in subgroup 15

   fig = xbar_s_chart_interactive(
       viscosity, subgroup_size=6, title="Batch Viscosity Xbar-S Chart"
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/variable/xbar_s_chart_interactive.png" alt="xbar_s_chart_interactive example output"><figcaption>Example output</figcaption></figure></div>
