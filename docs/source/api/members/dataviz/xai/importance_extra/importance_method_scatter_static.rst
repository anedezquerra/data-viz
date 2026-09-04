dataviz.xai.importance_extra.importance_method_scatter_static
=============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.importance_extra</p></div>

.. currentmodule:: dataviz.xai.importance_extra

.. autofunction:: importance_method_scatter_static

Use case
--------

Check agreement between two importance methods to validate that conclusions do not depend on one technique.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import matplotlib.pyplot as plt
   from dataviz.xai.importance_extra import importance_method_scatter_static

   permutation = {
       "credit_score": 0.142,
       "debt_to_income": 0.098,
       "utilization": 0.071,
       "payment_history": 0.055,
       "annual_income": 0.031,
       "loan_amount": 0.024,
       "account_age": 0.012,
       "inquiries_6m": 0.008,
   }
   shap_mean_abs = {
       "credit_score": 0.151,
       "debt_to_income": 0.090,
       "utilization": 0.078,
       "payment_history": 0.049,
       "annual_income": 0.036,
       "loan_amount": 0.020,
       "account_age": 0.015,
       "inquiries_6m": 0.006,
   }

   ax = importance_method_scatter_static(
       permutation,
       shap_mean_abs,
       a_name="Permutation (AUC drop)",
       b_name="SHAP (mean |phi|)",
       title="Importance Method Agreement - Default Model",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/importance_extra/importance_method_scatter_static.png" alt="importance_method_scatter_static example output"><figcaption>Example output</figcaption></figure></div>
