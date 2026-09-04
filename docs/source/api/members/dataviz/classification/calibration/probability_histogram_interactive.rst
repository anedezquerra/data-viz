dataviz.classification.calibration.probability_histogram_interactive
====================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.calibration</p></div>

.. currentmodule:: dataviz.classification.calibration

.. autofunction:: probability_histogram_interactive

Use case
--------

Use to inspect class separability in predicted probabilities; well-separated peaks indicate a discriminative classifier.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.classification.calibration import probability_histogram_interactive

   rng = np.random.default_rng(7)
   n_fraud, n_legit = 40, 120
   y_true = np.concatenate([np.ones(n_fraud, int), np.zeros(n_legit, int)])
   y_prob = np.concatenate([
       np.clip(rng.normal(0.72, 0.18, n_fraud), 0.01, 0.99),
       np.clip(rng.normal(0.18, 0.12, n_legit), 0.01, 0.99),
   ])

   fig = probability_histogram_interactive(
       y_true, y_prob, bins=25,
       title="Card fraud detector: score separation by class",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/calibration/probability_histogram_interactive.png" alt="probability_histogram_interactive example output"><figcaption>Example output</figcaption></figure></div>
