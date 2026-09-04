dataviz.regression.regularization.regularization_validation_plot_interactive
============================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.regularization</p></div>

.. currentmodule:: dataviz.regression.regularization

.. autofunction:: regularization_validation_plot_interactive

Use case
--------

Use to pick a penalty strength by comparing train and validation scores, with a fold std band when available.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.regression.regularization import regularization_validation_plot_interactive

   rng = np.random.default_rng(42)
   alphas = pd.Series(np.geomspace(1e-4, 10.0, 16), name="alpha")
   fold_scores = []
   for a in alphas:
       bias = 0.06 * np.log10(a / 1e-4) ** 2
       variance = 0.10 / (1 + 25 * a)
       fold_scores.append(0.92 - bias - variance + rng.normal(0, 0.015, 5))
   test_scores = np.array(fold_scores)
   train_scores = test_scores + 0.04 + rng.normal(0, 0.005, test_scores.shape)

   fig = regularization_validation_plot_interactive(
       alphas, train_scores, test_scores, score_name="R-squared",
       title="Pricing model: ridge validation curve (5-fold CV)",
       train_color="#4878d0", test_color="#d62728", template="plotly_white",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/regularization/regularization_validation_plot_interactive.png" alt="regularization_validation_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
