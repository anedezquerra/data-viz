dataviz.classification.calibration.brier_score_bar_interactive
==============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.calibration</p></div>

.. currentmodule:: dataviz.classification.calibration

.. autofunction:: brier_score_bar_interactive

Use case
--------

Compare models or classes on Brier score to rank probability quality; lower bars are better.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   from dataviz.classification.calibration import brier_score_bar_interactive

   scores = {
       "Logistic regression": 0.142,
       "Random forest": 0.118,
       "Gradient boosting": 0.105,
       "Naive base rate": 0.210,
   }

   fig = brier_score_bar_interactive(
       scores, title="Churn models: Brier score on Q4 holdout",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/calibration/brier_score_bar_interactive.png" alt="brier_score_bar_interactive example output"><figcaption>Example output</figcaption></figure></div>
