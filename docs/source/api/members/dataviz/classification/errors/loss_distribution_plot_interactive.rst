dataviz.classification.errors.loss_distribution_plot_interactive
================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.errors</p></div>

.. currentmodule:: dataviz.classification.errors

.. autofunction:: loss_distribution_plot_interactive

Use case
--------

Use to surface high-loss outlier samples driving log loss, split by true class with the mean marked.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.classification.errors import loss_distribution_plot_interactive

   rng = np.random.default_rng(43)
   n = 160
   signal = rng.normal(0, 1.3, n)
   y_prob = np.clip(1.0 / (1.0 + np.exp(-signal)), 1e-4, 1 - 1e-4)
   y_true = (signal + rng.normal(0, 0.9, n) > 0).astype(int)
   # a few hard mislabeled samples create high-loss outliers
   y_true[:4] = 1 - y_true[:4]
   y_prob[:4] = np.clip(y_prob[:4], 0.85, 0.98)

   fig = loss_distribution_plot_interactive(
       y_true, y_prob, bins=30,
       title="Document classifier: per-sample log loss outlier hunt",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/errors/loss_distribution_plot_interactive.png" alt="loss_distribution_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
