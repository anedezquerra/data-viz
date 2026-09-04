dataviz.xai.shap.shap_plot_interactive
======================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.shap</p></div>

.. currentmodule:: dataviz.xai.shap

.. autofunction:: shap_plot_interactive

Use case
--------

Use to rank features by mean signed SHAP value with direction-coded bars, a quick global read on which features push predictions up or down.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.xai.shap import shap_plot_interactive

   rng = np.random.default_rng(42)
   feature_names = [
       "credit_score", "debt_to_income", "loan_amount",
       "employment_years", "annual_income", "late_payments",
       "num_open_accounts", "age",
   ]
   coef = np.array([-0.6, 0.5, 0.3, -0.25, -0.2, 0.35, 0.1, -0.05])
   X = rng.normal(0, 1, size=(60, 8))
   shap_values = X * coef + rng.normal(0, 0.05, size=(60, 8))
   fig = shap_plot_interactive(
       shap_values, feature_names,
       title="Mean signed SHAP values - credit default model",
       xlabel="Mean SHAP value (log-odds)",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/shap/shap_plot_interactive.png" alt="shap_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
