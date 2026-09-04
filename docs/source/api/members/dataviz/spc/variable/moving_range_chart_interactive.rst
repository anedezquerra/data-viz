dataviz.spc.variable.moving_range_chart_interactive
===================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.variable</p></div>

.. currentmodule:: dataviz.spc.variable

.. autofunction:: moving_range_chart_interactive

Use case
--------

Use to monitor short-term variation between consecutive individual measurements, companion to an individuals chart.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.spc.variable import moving_range_chart_interactive

   rng = np.random.default_rng(42)
   # Fill weights (g) from 30 consecutive bottles on a filling line
   weights = rng.normal(500.0, 1.1, size=30)
   weights[24] = 504.9  # overfill after valve wear

   fig = moving_range_chart_interactive(weights, span=2, title="Fill Weight Moving Range")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/variable/moving_range_chart_interactive.png" alt="moving_range_chart_interactive example output"><figcaption>Example output</figcaption></figure></div>
