dataviz.xai.importance_extra.permutation_importance_bar_static
==============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.importance_extra</p></div>

.. currentmodule:: dataviz.xai.importance_extra

.. autofunction:: permutation_importance_bar_static

Use case
--------

Use for model-agnostic importance estimates measured by the performance drop when each feature is shuffled.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import matplotlib.pyplot as plt
   from dataviz.xai.importance_extra import permutation_importance_bar_static

   importances = {
       "credit_score": 0.142,
       "debt_to_income": 0.098,
       "utilization": 0.071,
       "payment_history": 0.055,
       "annual_income": 0.031,
       "loan_amount": 0.024,
       "account_age": 0.012,
       "inquiries_6m": 0.008,
   }
   std = {
       "credit_score": 0.011,
       "debt_to_income": 0.009,
       "utilization": 0.008,
       "payment_history": 0.007,
       "annual_income": 0.006,
       "loan_amount": 0.005,
       "account_age": 0.004,
       "inquiries_6m": 0.003,
   }

   ax = permutation_importance_bar_static(
       importances,
       std=std,
       top_n=8,
       title="Permutation Importance (ROC-AUC Drop) - Default Model",
       color="seagreen",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/importance_extra/permutation_importance_bar_static.png" alt="permutation_importance_bar_static example output"><figcaption>Example output</figcaption></figure></div>
