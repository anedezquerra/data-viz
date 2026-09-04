dataviz.spc.attribute.g_chart_interactive
=========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.attribute</p></div>

.. currentmodule:: dataviz.spc.attribute

.. autofunction:: g_chart_interactive

Use case
--------

Use when monitoring opportunities or units produced between rare events, such as defects on a high-yield line.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.spc.attribute import g_chart_interactive

   rng = np.random.default_rng(42)
   # Units produced between rare contamination events on a filling line
   counts = rng.geometric(p=0.03, size=25)
   counts[15] = 160  # unusually long clean run after filter upgrade

   fig = g_chart_interactive(counts, title="Contamination Events - Units Between Occurrences")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/attribute/g_chart_interactive.png" alt="g_chart_interactive example output"><figcaption>Example output</figcaption></figure></div>
