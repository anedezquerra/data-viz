dataviz.xai.fairness_xai.subgroup_shap_divergence_static
========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.fairness_xai</p></div>

.. currentmodule:: dataviz.xai.fairness_xai

.. autofunction:: subgroup_shap_divergence_static

Use case
--------

Check whether a model relies on features differently across protected subgroups by comparing SHAP distributions.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import matplotlib.pyplot as plt
   from dataviz.xai.fairness_xai import subgroup_shap_divergence_static

   divergence = {
       "credit_score": 0.42,
       "debt_to_income": 0.35,
       "utilization": 0.28,
       "zip_region": 0.61,
       "annual_income": 0.19,
       "account_age": 0.11,
       "loan_amount": 0.08,
   }

   ax = subgroup_shap_divergence_static(
       divergence,
       metric="KL",
       title="SHAP Divergence Between Urban and Rural Subgroups",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/fairness_xai/subgroup_shap_divergence_static.png" alt="subgroup_shap_divergence_static example output"><figcaption>Example output</figcaption></figure></div>
