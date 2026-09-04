dataviz.xai.cohort.importance_by_segment_heatmap_interactive
============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.cohort</p></div>

.. currentmodule:: dataviz.xai.cohort

.. autofunction:: importance_by_segment_heatmap_interactive

Use case
--------

Use to compare which features matter across cohorts, e.g. regions or customer tiers, in one annotated heatmap.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import matplotlib.pyplot as plt
   from dataviz.xai.cohort import importance_by_segment_heatmap_interactive

   features = [
       "credit_score", "debt_to_income", "utilization",
       "annual_income", "loan_amount", "account_age",
   ]
   importances = {
       "Prime (score >= 740)": dict(zip(features, [0.34, 0.18, 0.16, 0.14, 0.10, 0.08])),
       "Near-prime (660-739)": dict(zip(features, [0.28, 0.24, 0.19, 0.11, 0.11, 0.07])),
       "Subprime (< 660)": dict(zip(features, [0.19, 0.30, 0.22, 0.09, 0.12, 0.08])),
       "Thin file": dict(zip(features, [0.12, 0.21, 0.18, 0.20, 0.17, 0.12])),
   }

   fig = importance_by_segment_heatmap_interactive(
       importances,
       title="Feature Importance by Applicant Segment",
       height=560,
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/cohort/importance_by_segment_heatmap_interactive.png" alt="importance_by_segment_heatmap_interactive example output"><figcaption>Example output</figcaption></figure></div>
