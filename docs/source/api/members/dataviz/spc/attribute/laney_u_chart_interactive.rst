dataviz.spc.attribute.laney_u_chart_interactive
===============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.attribute</p></div>

.. currentmodule:: dataviz.spc.attribute

.. autofunction:: laney_u_chart_interactive

Use case
--------

Use when a u chart shows over-dispersion from large or varying areas of opportunity; the Laney u' chart widens limits to match actual variation.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.spc.attribute import laney_u_chart_interactive

   rng = np.random.default_rng(42)
   # Cable defects per unit with varying production volumes and overdispersion
   units = rng.integers(20, 60, size=28)
   defects = rng.poisson(units * 0.6)
   defects[20] = 70  # extruder contamination event

   fig = laney_u_chart_interactive(defects, units, title="Cable Production - Defects per Unit (Laney u-prime)")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/attribute/laney_u_chart_interactive.png" alt="laney_u_chart_interactive example output"><figcaption>Example output</figcaption></figure></div>
