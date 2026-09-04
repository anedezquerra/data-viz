dataviz.xai.local_explanations.lime_explanation_bar_interactive
===============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.local_explanations</p></div>

.. currentmodule:: dataviz.xai.local_explanations

.. autofunction:: lime_explanation_bar_interactive

Use case
--------

Use to show a LIME-style signed bar of which feature conditions raised or lowered one instance's prediction.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   from dataviz.xai.local_explanations import lime_explanation_bar_interactive

   contributions = [
       ("tenure_months <= 6", 0.31),
       ("num_support_calls > 3", 0.22),
       ("contract_two_year = 0", 0.18),
       ("late_payments > 1", 0.09),
       ("plan_premium = 1", -0.07),
       ("monthly_charges <= 55", -0.14),
       ("avg_session_min > 40", -0.21),
       ("age > 45", -0.06),
   ]
   fig = lime_explanation_bar_interactive(
       contributions,
       title="LIME explanation - churn prediction for customer #417",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/local_explanations/lime_explanation_bar_interactive.png" alt="lime_explanation_bar_interactive example output"><figcaption>Example output</figcaption></figure></div>
