dataviz.classification.gain_lift.cumulative_accuracy_profile_interactive
========================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.gain_lift</p></div>

.. currentmodule:: dataviz.classification.gain_lift

.. autofunction:: cumulative_accuracy_profile_interactive

Use case
--------

Use to compare the model CAP curve against perfect and random baselines and read the accuracy ratio.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.classification.gain_lift import (
       cumulative_accuracy_profile_interactive,
   )

   rng = np.random.default_rng(71)
   n_pos, n_neg = 35, 125
   y_true = np.concatenate([np.ones(n_pos, int), np.zeros(n_neg, int)])
   y_prob = np.concatenate([
       rng.normal(0.68, 0.17, n_pos),
       rng.normal(0.32, 0.15, n_neg),
   ]).clip(0.01, 0.99)

   fig = cumulative_accuracy_profile_interactive(
       y_true, y_prob,
       title="Credit default model: CAP curve and accuracy ratio",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/gain_lift/cumulative_accuracy_profile_interactive.png" alt="cumulative_accuracy_profile_interactive example output"><figcaption>Example output</figcaption></figure></div>
