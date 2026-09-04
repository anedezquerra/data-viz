dataviz.spc.control.control_chart_interactive
=============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.control</p></div>

.. currentmodule:: dataviz.spc.control

.. autofunction:: control_chart_interactive

Use case
--------

Use to plot process observations against computed control limits to judge whether a process is in statistical control.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.spc.control import control_chart_interactive

   rng = np.random.default_rng(42)
   # Oven temperature (deg C) logged every 15 minutes over one shift
   temps = rng.normal(180.0, 1.5, size=30)
   temps[22] = 186.4  # heating element surge

   fig = control_chart_interactive(
       temps,
       title="Oven Temperature Control Chart",
       ylabel="Temperature (deg C)",
       marker_size=6,
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/control/control_chart_interactive.png" alt="control_chart_interactive example output"><figcaption>Example output</figcaption></figure></div>
