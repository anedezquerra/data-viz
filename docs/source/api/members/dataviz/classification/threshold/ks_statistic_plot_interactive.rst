dataviz.classification.threshold.ks_statistic_plot_interactive
==============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.threshold</p></div>

.. currentmodule:: dataviz.classification.threshold

.. autofunction:: ks_statistic_plot_interactive

Use case
--------

Use in credit scoring to measure class separation; plots class CDFs and marks the maximum KS gap.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.threshold import ks_statistic_plot_interactive

   rng = np.random.default_rng(42)
   # credit scorecard: KS separation between defaulters and payers
   n = 150
   y_true = (rng.random(n) < 0.25).astype(int)
   y_prob = np.clip(
       y_true * rng.beta(6, 2.5, n) + (1 - y_true) * rng.beta(2.5, 6, n), 0, 1)

   fig = ks_statistic_plot_interactive(y_true, y_prob,
                                       title="Credit scorecard: KS plot")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/threshold/ks_statistic_plot_interactive.png" alt="ks_statistic_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
