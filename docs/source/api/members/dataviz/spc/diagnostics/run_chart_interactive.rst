dataviz.spc.diagnostics.run_chart_interactive
=============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.diagnostics</p></div>

.. currentmodule:: dataviz.spc.diagnostics

.. autofunction:: run_chart_interactive

Use case
--------

Use to plot observations in time order against a median reference to spot runs, trends, and shifts before formal control charting.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.spc.diagnostics import run_chart_interactive

   rng = np.random.default_rng(42)
   # Changeover time (minutes) for 32 consecutive line changeovers
   changeover = rng.normal(45.0, 3.0, size=32)
   changeover[24:] -= 6.0  # improvement after SMED kaizen event

   fig = run_chart_interactive(changeover, title="Changeover Time Run Chart", show_median=True)
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/diagnostics/run_chart_interactive.png" alt="run_chart_interactive example output"><figcaption>Example output</figcaption></figure></div>
