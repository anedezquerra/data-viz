dataviz.xai.uncertainty.confidence_attribution_bar_interactive
==============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.uncertainty</p></div>

.. currentmodule:: dataviz.xai.uncertainty

.. autofunction:: confidence_attribution_bar_interactive

Use case
--------

Use to attribute predictive uncertainty to individual features, identifying which inputs drive the model's lack of confidence.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   from dataviz.xai.uncertainty import confidence_attribution_bar_interactive

   attribution = {
       "thin_credit_history": 0.142,
       "num_open_accounts": 0.087,
       "employment_years": 0.064,
       "loan_amount": 0.031,
       "annual_income": -0.028,
       "credit_score": -0.052,
   }
   fig = confidence_attribution_bar_interactive(
       attribution,
       title="Which features drive predictive uncertainty - applicant #992",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/uncertainty/confidence_attribution_bar_interactive.png" alt="confidence_attribution_bar_interactive example output"><figcaption>Example output</figcaption></figure></div>
