dataviz.univariate.datetime.interarrival_plot_static
====================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.datetime</p></div>

.. currentmodule:: dataviz.univariate.datetime

.. autofunction:: interarrival_plot_static

Use case
--------

Use to histogram the gaps between consecutive events to spot burstiness or regularity in timing.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.univariate.datetime import interarrival_plot_static

   # Equipment failure timestamps from a fleet monitoring system
   rng = np.random.default_rng(42)
   failures = pd.Series(
       pd.Timestamp("2026-02-01")
       + pd.to_timedelta(np.sort(rng.uniform(0, 120 * 24, size=32)), unit="h"),
       name="failure_time",
   )

   ax = interarrival_plot_static(
       failures,
       unit="h",
       title="Time Between Equipment Failures",
       color="indianred",
       theme="minimal",
   )
   ax.set_xlabel("Hours Between Failures")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/datetime/interarrival_plot_static.png" alt="interarrival_plot_static example output"><figcaption>Example output</figcaption></figure></div>
