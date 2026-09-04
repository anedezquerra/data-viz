dataviz.xai.local_more.prototype_criticism_grid_static
======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.local_more</p></div>

.. currentmodule:: dataviz.xai.local_more

.. autofunction:: prototype_criticism_grid_static

Use case
--------

Use to contrast representative prototypes with atypical criticisms side by side, summarizing what is typical and what the model may mishandle.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.xai.local_more import prototype_criticism_grid_static

   rng = np.random.default_rng(42)
   cols = [
       "tenure_months", "monthly_charges", "num_support_calls",
       "avg_session_min", "late_payments", "age",
   ]
   prototypes = pd.DataFrame(
       np.array([
           [36, 65, 0, 42, 0, 45],
           [48, 82, 1, 35, 0, 52],
           [24, 55, 0, 50, 0, 31],
       ], dtype=float), columns=cols,
   )
   criticisms = pd.DataFrame(
       np.array([
           [2, 118, 7, 4, 4, 23],
           [60, 39, 5, 61, 3, 68],
       ], dtype=float), columns=cols,
   )
   ax = prototype_criticism_grid_static(
       prototypes, criticisms,
       title="Typical vs atypical retained customers (MMD critic)",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/local_more/prototype_criticism_grid_static.png" alt="prototype_criticism_grid_static example output"><figcaption>Example output</figcaption></figure></div>
