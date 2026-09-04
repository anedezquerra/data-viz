dataviz.spc.capability.capability_histogram_interactive
=======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.capability</p></div>

.. currentmodule:: dataviz.spc.capability

.. autofunction:: capability_histogram_interactive

Use case
--------

Use to show a process histogram against specification limits with a fitted normal curve, for capability reviews with customers or auditors.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.spc.capability import capability_histogram_interactive

   rng = np.random.default_rng(42)
   # Fill weights (g) from a bottling line, spec 497-503 g
   weights = rng.normal(500.0, 1.2, size=60)
   weights[41] = 504.8  # overfilled bottle after valve wear

   fig = capability_histogram_interactive(
       weights, lsl=497.0, usl=503.0, bins=20, title="Fill Weight Capability"
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/capability/capability_histogram_interactive.png" alt="capability_histogram_interactive example output"><figcaption>Example output</figcaption></figure></div>
