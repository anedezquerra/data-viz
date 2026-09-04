dataviz.spc.attribute.t_chart_interactive
=========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.attribute</p></div>

.. currentmodule:: dataviz.spc.attribute

.. autofunction:: t_chart_interactive

Use case
--------

Use when monitoring elapsed time between rare events, such as hours between equipment failures or safety incidents.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.spc.attribute import t_chart_interactive

   rng = np.random.default_rng(42)
   # Hours between recordable safety incidents across a plant
   times = rng.exponential(scale=12.0, size=25)
   times[14] = 85.0  # long incident-free stretch after retraining

   fig = t_chart_interactive(times, title="Safety Incidents - Hours Between Events")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/attribute/t_chart_interactive.png" alt="t_chart_interactive example output"><figcaption>Example output</figcaption></figure></div>
