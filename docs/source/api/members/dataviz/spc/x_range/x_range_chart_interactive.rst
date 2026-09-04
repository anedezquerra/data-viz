dataviz.spc.x_range.x_range_chart_interactive
=============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.x_range</p></div>

.. currentmodule:: dataviz.spc.x_range

.. autofunction:: x_range_chart_interactive

Use case
--------

Use to plot individual values with their moving ranges for processes measured one part at a time.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.spc.x_range import x_range_chart_interactive

   rng = np.random.default_rng(42)
   # Shaft diameters (mm) sampled from a CNC lathe
   diameters = rng.normal(25.0, 0.08, size=30)
   diameters[19] = 25.42  # tool wear spike

   fig = x_range_chart_interactive(
       diameters, subgroup_size=5, title="Shaft Diameter X-Range Chart", ylabel="Diameter (mm)"
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/x_range/x_range_chart_interactive.png" alt="x_range_chart_interactive example output"><figcaption>Example output</figcaption></figure></div>
