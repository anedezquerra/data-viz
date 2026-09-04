dataviz.regression.validation.validation_curve_interactive
==========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.validation</p></div>

.. currentmodule:: dataviz.regression.validation

.. autofunction:: validation_curve_interactive

Use case
--------

Use to tune a hyperparameter by plotting train and validation scores against its values; widening gaps signal overfitting.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.validation import validation_curve_interactive

   rng = np.random.default_rng(42)
   alphas = np.logspace(-3, 2, 12)
   base_train = 0.55 + 0.40 * (1 - np.exp(-alphas))
   base_test = 0.88 - 0.0011 * (np.log10(alphas) + 1.2) ** 4
   train_scores = base_train[:, None] + rng.normal(0, 0.012, (12, 5))
   test_scores = base_test[:, None] + rng.normal(0, 0.020, (12, 5))

   fig = validation_curve_interactive(
       alphas, train_scores, test_scores,
       param_name="Ridge alpha", score_name="R-squared", log_x=True,
       title="Ridge regression on concrete strength: validation curve",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/validation/validation_curve_interactive.png" alt="validation_curve_interactive example output"><figcaption>Example output</figcaption></figure></div>
