dataviz.spc.variable.imr_chart_interactive
==========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.variable</p></div>

.. currentmodule:: dataviz.spc.variable

.. autofunction:: imr_chart_interactive

Use case
--------

Use when monitoring individual measurements with no rational subgrouping, pairing the individuals and moving-range views.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.spc.variable import imr_chart_interactive

   rng = np.random.default_rng(42)
   # Product purity (%) measured once per batch (individuals data)
   purity = rng.normal(99.2, 0.15, size=30)
   purity[23] = 98.4  # contaminated raw-material drum

   fig = imr_chart_interactive(purity, span=2, title="Batch Purity I-MR Chart")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/variable/imr_chart_interactive.png" alt="imr_chart_interactive example output"><figcaption>Example output</figcaption></figure></div>
