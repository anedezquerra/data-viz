dataviz.xai.shap_extra.shap_waterfall_plot_interactive
======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.shap_extra</p></div>

.. currentmodule:: dataviz.xai.shap_extra

.. autofunction:: shap_waterfall_plot_interactive

Use case
--------

Use to walk one prediction from base value to f(x) feature by feature; small contributions collapse into an 'other' bar via top_n.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.xai.shap_extra import shap_waterfall_plot_interactive

   feature_names = [
       "tenure_months", "monthly_charges", "contract_two_year",
       "num_support_calls", "avg_session_min", "late_payments",
       "plan_premium", "age",
   ]
   shap_values_instance = np.array(
       [0.85, 0.42, -0.61, 0.37, 0.12, 0.28, -0.15, -0.06]
   )
   fig = shap_waterfall_plot_interactive(
       shap_values_instance, feature_names, base_value=-1.10, top_n=6,
       title="SHAP waterfall - churn explanation for customer #417",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/shap_extra/shap_waterfall_plot_interactive.png" alt="shap_waterfall_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
