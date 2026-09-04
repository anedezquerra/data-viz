dataviz.univariate.tail.survival_curve_static
=============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.tail</p></div>

.. currentmodule:: dataviz.univariate.tail

.. autofunction:: survival_curve_static

Use case
--------

Use to emphasize upper-tail behavior by plotting the probability of exceeding each value instead of a density.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.univariate.tail import survival_curve_static

   rng = np.random.default_rng(42)
   claim_amounts = pd.Series(
       (rng.pareto(a=2.5, size=160) * 5000 + 1000).round(0),
       name="claim_amount",
   )
   ax = survival_curve_static(
       claim_amounts,
       title="Insurance Claim Survival Curve",
       color="darkred",
       theme="minimal",
   )
   ax.set_xlabel("Claim amount (USD)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/tail/survival_curve_static.png" alt="survival_curve_static example output"><figcaption>Example output</figcaption></figure></div>
