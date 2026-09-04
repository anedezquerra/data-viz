dataviz.xai.fairness_xai.disparate_impact_by_segment_interactive
================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.fairness_xai</p></div>

.. currentmodule:: dataviz.xai.fairness_xai

.. autofunction:: disparate_impact_by_segment_interactive

Use case
--------

Use in fairness audits to see which features drive predictions per segment alongside each segment's outcome rate.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.xai.fairness_xai import disparate_impact_by_segment_interactive

   segment_metrics = pd.DataFrame(
       {
           "importance": [0.31, 0.24, 0.19, 0.15],
           "positive_rate": [0.78, 0.71, 0.63, 0.55],
       },
       index=["Age 25-34", "Age 35-44", "Age 45-54", "Age 55+"],
   )

   fig = disparate_impact_by_segment_interactive(
       segment_metrics,
       importance_col="importance",
       rate_col="positive_rate",
       reference_rate=0.70,
       title="Credit-Score Feature Reliance vs Approval Rate by Age Band",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/fairness_xai/disparate_impact_by_segment_interactive.png" alt="disparate_impact_by_segment_interactive example output"><figcaption>Example output</figcaption></figure></div>
