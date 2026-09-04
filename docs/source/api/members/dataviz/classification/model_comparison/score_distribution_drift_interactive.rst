dataviz.classification.model_comparison.score_distribution_drift_interactive
============================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.model_comparison</p></div>

.. currentmodule:: dataviz.classification.model_comparison

.. autofunction:: score_distribution_drift_interactive

Use case
--------

Use to monitor production models by overlaying reference vs. current score distributions for drift.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.classification.model_comparison import (
       score_distribution_drift_interactive,
   )

   rng = np.random.default_rng(79)
   scores_reference = np.clip(rng.beta(2, 4, 150), 0.01, 0.99)
   # production traffic shifted toward higher risk scores last month
   scores_current = np.clip(rng.beta(2.6, 3.6, 150), 0.01, 0.99)

   fig = score_distribution_drift_interactive(
       scores_reference, scores_current, bins=30,
       title="Fraud scoring service: training vs last-month traffic",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/model_comparison/score_distribution_drift_interactive.png" alt="score_distribution_drift_interactive example output"><figcaption>Example output</figcaption></figure></div>
