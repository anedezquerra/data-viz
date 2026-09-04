dataviz.regression.cv_extended.learning_curve_with_band_interactive
===================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.cv_extended</p></div>

.. currentmodule:: dataviz.regression.cv_extended

.. autofunction:: learning_curve_with_band_interactive

Use case
--------

Use to show mean CV score versus training size with a plus/minus std band, revealing both bias and variance as data grows.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.cv_extended import learning_curve_with_band_interactive

   train_sizes = np.array([25, 50, 75, 100, 125, 150])
   mean_rmse = np.array([18.5, 14.2, 12.1, 11.0, 10.4, 10.1])
   std_rmse = np.array([3.1, 2.2, 1.7, 1.4, 1.2, 1.1])

   fig = learning_curve_with_band_interactive(
       train_sizes, mean_rmse, std_rmse,
       title="Cycle-Time Model: Learning Curve (5-fold CV)",
       metric_name="RMSE (seconds)", color="#1f6fb2",
       template="plotly_white")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/cv_extended/learning_curve_with_band_interactive.png" alt="learning_curve_with_band_interactive example output"><figcaption>Example output</figcaption></figure></div>
