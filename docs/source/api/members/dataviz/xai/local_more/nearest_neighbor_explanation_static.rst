dataviz.xai.local_more.nearest_neighbor_explanation_static
==========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.local_more</p></div>

.. currentmodule:: dataviz.xai.local_more

.. autofunction:: nearest_neighbor_explanation_static

Use case
--------

Use to justify a prediction by comparing the query row's feature values against its k nearest neighbors in a heatmap.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.xai.local_more import nearest_neighbor_explanation_static

   rng = np.random.default_rng(42)
   cols = [
       "credit_score", "debt_to_income", "loan_amount",
       "annual_income", "employment_years", "late_payments",
   ]
   query = {
       "credit_score": 612.0, "debt_to_income": 0.41, "loan_amount": 18500.0,
       "annual_income": 52000.0, "employment_years": 2.0, "late_payments": 2.0,
   }
   neighbors = pd.DataFrame(
       {
           "credit_score": 612 + rng.normal(0, 8, size=5),
           "debt_to_income": 0.41 + rng.normal(0, 0.03, size=5),
           "loan_amount": 18500 + rng.normal(0, 900, size=5),
           "annual_income": 52000 + rng.normal(0, 2500, size=5),
           "employment_years": 2 + rng.normal(0, 0.5, size=5),
           "late_payments": np.array([2, 1, 2, 3, 2], dtype=float),
       }
   )
   target = [1, 0, 1, 1, 0]
   ax = nearest_neighbor_explanation_static(
       query, neighbors, target=target,
       title="Denied applicant #2048 vs 5 most similar past decisions",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/local_more/nearest_neighbor_explanation_static.png" alt="nearest_neighbor_explanation_static example output"><figcaption>Example output</figcaption></figure></div>
