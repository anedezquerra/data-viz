dataviz.spc.diagnostics.rule_violation_chart_static
===================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.diagnostics</p></div>

.. currentmodule:: dataviz.spc.diagnostics

.. autofunction:: rule_violation_chart_static

Use case
--------

Use to highlight Western Electric or Nelson rule violations on a control chart so operators see exactly where special causes occurred.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.spc.diagnostics import rule_violation_chart_static

   rng = np.random.default_rng(42)
   data = rng.normal(loc=10.0, scale=0.4, size=30)
   data[24] = 11.8  # Deliberate special-cause signal

   ax = rule_violation_chart_static(data, title="Process rule signals")
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/diagnostics/rule_violation_chart_static.png" alt="rule_violation_chart_static example output"><figcaption>Example output</figcaption></figure></div>
