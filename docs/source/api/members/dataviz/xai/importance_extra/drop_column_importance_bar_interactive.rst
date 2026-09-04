dataviz.xai.importance_extra.drop_column_importance_bar_interactive
===================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.importance_extra</p></div>

.. currentmodule:: dataviz.xai.importance_extra

.. autofunction:: drop_column_importance_bar_interactive

Use case
--------

Use to measure each feature's contribution by retraining without it; signed values show helpful vs. harmful columns.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import matplotlib.pyplot as plt
   from dataviz.xai.importance_extra import drop_column_importance_bar_interactive

   deltas = {
       "credit_score": 0.118,
       "debt_to_income": 0.084,
       "utilization": 0.062,
       "payment_history": 0.047,
       "annual_income": 0.019,
       "loan_amount": 0.011,
       "account_age": -0.003,
       "inquiries_6m": -0.006,
   }

   fig = drop_column_importance_bar_interactive(
       deltas,
       top_n=8,
       title="Drop-Column Importance (ROC-AUC) - Default Model",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/importance_extra/drop_column_importance_bar_interactive.png" alt="drop_column_importance_bar_interactive example output"><figcaption>Example output</figcaption></figure></div>
