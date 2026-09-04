dataviz.spc.diagnostics.rule_violation_chart_interactive
========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.diagnostics</p></div>

.. currentmodule:: dataviz.spc.diagnostics

.. autofunction:: rule_violation_chart_interactive

Use case
--------

Use to highlight Western Electric or Nelson rule violations on a control chart so operators see exactly where special causes occurred.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.spc.diagnostics import rule_violation_chart_interactive

   rng = np.random.default_rng(42)
   # Batch pH from a fermentation process with a shift after a recipe change
   ph = rng.normal(7.2, 0.05, size=30)
   ph[18:] += 0.25  # upward shift after cleaning-cycle change

   fig = rule_violation_chart_interactive(ph, title="Fermentation Batch pH - Rule Violations")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/diagnostics/rule_violation_chart_interactive.png" alt="rule_violation_chart_interactive example output"><figcaption>Example output</figcaption></figure></div>
