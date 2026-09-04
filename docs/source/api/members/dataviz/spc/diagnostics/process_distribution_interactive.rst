dataviz.spc.diagnostics.process_distribution_interactive
========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.diagnostics</p></div>

.. currentmodule:: dataviz.spc.diagnostics

.. autofunction:: process_distribution_interactive

Use case
--------

Use to check the shape, center, and sigma spread of process output with a histogram and sigma bands before assuming normality.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.spc.diagnostics import process_distribution_interactive

   rng = np.random.default_rng(42)
   # Fill weights (g) collected during a capability study on line 3
   weights = rng.normal(500.0, 1.1, size=40)
   weights[33] = 504.6  # overfill after valve wear

   fig = process_distribution_interactive(weights, bins=15, title="Line 3 Fill Weight Distribution")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/diagnostics/process_distribution_interactive.png" alt="process_distribution_interactive example output"><figcaption>Example output</figcaption></figure></div>
