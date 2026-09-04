dataviz.univariate.distribution.pp_plot_static
==============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.distribution</p></div>

.. currentmodule:: dataviz.univariate.distribution

.. autofunction:: pp_plot_static

Use case
--------

Use to compare cumulative probabilities between data and a theoretical distribution to check fit near the center.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.univariate.distribution import pp_plot_static

   # Machine cycle times fitted against a gamma reference
   rng = np.random.default_rng(42)
   cycle_s = pd.Series(
       np.round(rng.gamma(shape=5.0, scale=2.1, size=52), 2),
       name="cycle_s",
   )

   ax = pp_plot_static(
       cycle_s,
       distribution="gamma",
       title="Cycle Time PP Plot (Gamma)",
       color="darkslategray",
       reference_color="crimson",
       theme="minimal",
   )
   ax.set_xlabel("Theoretical Probability")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/distribution/pp_plot_static.png" alt="pp_plot_static example output"><figcaption>Example output</figcaption></figure></div>
