dataviz.classification.calibration.calibration_curve_interactive
================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.calibration</p></div>

.. currentmodule:: dataviz.classification.calibration

.. autofunction:: calibration_curve_interactive

Use case
--------

Use to check whether predicted probabilities match observed frequencies, e.g. before trusting scores as risk estimates.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.classification.calibration import calibration_curve_interactive

   rng = np.random.default_rng(42)
   n = 160
   churn_risk = rng.normal(5.0, 1.5, n)
   y_prob = 1.0 / (1.0 + np.exp(-(churn_risk - 5.0)))
   y_true = (rng.uniform(size=n) < np.clip(y_prob + 0.08, 0, 1)).astype(int)

   fig = calibration_curve_interactive(
       y_true, y_prob, n_bins=8, strategy="quantile",
       title="Telco churn model: reliability diagram",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/calibration/calibration_curve_interactive.png" alt="calibration_curve_interactive example output"><figcaption>Example output</figcaption></figure></div>
