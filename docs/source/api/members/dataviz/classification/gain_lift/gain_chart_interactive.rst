dataviz.classification.gain_lift.gain_chart_interactive
=======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.gain_lift</p></div>

.. currentmodule:: dataviz.classification.gain_lift

.. autofunction:: gain_chart_interactive

Use case
--------

Use to show what fraction of positives is captured by targeting the top-scored fraction of the population.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.classification.gain_lift import gain_chart_interactive

   rng = np.random.default_rng(67)
   n_pos, n_neg = 40, 120
   y_true = np.concatenate([np.ones(n_pos, int), np.zeros(n_neg, int)])
   y_prob = np.concatenate([
       rng.normal(0.70, 0.16, n_pos),
       rng.normal(0.30, 0.15, n_neg),
   ]).clip(0.01, 0.99)

   fig = gain_chart_interactive(
       y_true, y_prob,
       title="Direct-mail campaign: cumulative gains of response model",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/gain_lift/gain_chart_interactive.png" alt="gain_chart_interactive example output"><figcaption>Example output</figcaption></figure></div>
