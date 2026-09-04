dataviz.univariate.tail.lorenz_curve_static
===========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.tail</p></div>

.. currentmodule:: dataviz.univariate.tail

.. autofunction:: lorenz_curve_static

Use case
--------

Use to visualize inequality in non-negative values against the perfect-equality reference line.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.univariate.tail import lorenz_curve_static

   rng = np.random.default_rng(42)
   claim_amounts = pd.Series(
       (rng.pareto(a=2.5, size=160) * 5000 + 1000).round(0),
       name="claim_amount",
   )
   ax = lorenz_curve_static(
       claim_amounts,
       title="Lorenz Curve of Claim Amounts",
       color="navy",
       theme="minimal",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/tail/lorenz_curve_static.png" alt="lorenz_curve_static example output"><figcaption>Example output</figcaption></figure></div>
