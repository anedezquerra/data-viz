dataviz.regression.survival.km_predicted_vs_observed_interactive
================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.survival</p></div>

.. currentmodule:: dataviz.regression.survival

.. autofunction:: km_predicted_vs_observed_interactive

Use case
--------

Use to validate a survival model by overlaying predicted and observed Kaplan-Meier curves; divergence signals poor calibration of survival probabilities.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.survival import km_predicted_vs_observed_interactive

   months = np.arange(0, 37, 3)
   observed = np.array([1.00, 0.97, 0.93, 0.88, 0.82, 0.75, 0.68,
                        0.60, 0.53, 0.46, 0.39, 0.33, 0.27])
   predicted = np.array([1.00, 0.96, 0.91, 0.85, 0.79, 0.72, 0.65,
                         0.58, 0.51, 0.44, 0.38, 0.32, 0.26])

   fig = km_predicted_vs_observed_interactive(
       months, observed, predicted,
       title="Phase II oncology trial: KM observed vs Cox-predicted survival",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/survival/km_predicted_vs_observed_interactive.png" alt="km_predicted_vs_observed_interactive example output"><figcaption>Example output</figcaption></figure></div>
