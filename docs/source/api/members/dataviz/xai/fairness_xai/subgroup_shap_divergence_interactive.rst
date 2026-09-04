dataviz.xai.fairness_xai.subgroup_shap_divergence_interactive
=============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.fairness_xai</p></div>

.. currentmodule:: dataviz.xai.fairness_xai

.. autofunction:: subgroup_shap_divergence_interactive

Use case
--------

Check whether a model relies on features differently across protected subgroups by comparing SHAP distributions.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import matplotlib.pyplot as plt
   from dataviz.xai.fairness_xai import subgroup_shap_divergence_interactive

   divergence = {
       "credit_score": 0.42,
       "debt_to_income": 0.35,
       "utilization": 0.28,
       "zip_region": 0.61,
       "annual_income": 0.19,
       "account_age": 0.11,
       "loan_amount": 0.08,
   }

   fig = subgroup_shap_divergence_interactive(
       divergence,
       metric="KL",
       title="SHAP Divergence Between Urban and Rural Subgroups",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/fairness_xai/subgroup_shap_divergence_interactive.png" alt="subgroup_shap_divergence_interactive example output"><figcaption>Example output</figcaption></figure></div>
