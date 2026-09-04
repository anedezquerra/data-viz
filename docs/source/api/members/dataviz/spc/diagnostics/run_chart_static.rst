dataviz.spc.diagnostics.run_chart_static
========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.diagnostics</p></div>

.. currentmodule:: dataviz.spc.diagnostics

.. autofunction:: run_chart_static

Use case
--------

Use to plot observations in time order against a median reference to spot runs, trends, and shifts before formal control charting.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.spc.diagnostics import run_chart_static

   rng = np.random.default_rng(42)
   # Changeover time (minutes) for 32 consecutive line changeovers
   changeover = rng.normal(45.0, 3.0, size=32)
   changeover[24:] -= 6.0  # improvement after SMED kaizen event

   ax = run_chart_static(changeover, title="Changeover Time Run Chart", show_median=True)
   ax.set_ylabel("Changeover time (min)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/diagnostics/run_chart_static.png" alt="run_chart_static example output"><figcaption>Example output</figcaption></figure></div>
