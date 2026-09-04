dataviz.univariate.advanced.rug_plot_static
===========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.advanced</p></div>

.. currentmodule:: dataviz.univariate.advanced

.. autofunction:: rug_plot_static

Use case
--------

Use to show every individual observation as ticks along an axis, revealing clustering and gaps that bins can hide.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.univariate.advanced import rug_plot_static

   # Packet round-trip times captured on a network link
   rng = np.random.default_rng(42)
   latency_ms = pd.Series(
       np.round(rng.lognormal(mean=3.4, sigma=0.35, size=45), 1),
       name="latency_ms",
   )

   ax = rug_plot_static(
       latency_ms,
       title="Round-Trip Latency Observations",
       xlabel="Latency (ms)",
       color="steelblue",
       height=0.6,
       alpha=0.6,
       theme="minimal",
   )
   ax.set_xlabel("Latency (ms)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/advanced/rug_plot_static.png" alt="rug_plot_static example output"><figcaption>Example output</figcaption></figure></div>
