dataviz.regression.prediction_extended.prediction_interval_plot_interactive
===========================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.prediction_extended</p></div>

.. currentmodule:: dataviz.regression.prediction_extended

.. autofunction:: prediction_interval_plot_interactive

Use case
--------

Use to show predictions with an empirical or Gaussian interval band and see which actuals fall outside it.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.regression.prediction_extended import prediction_interval_plot_interactive

   rng = np.random.default_rng(42)
   patients = pd.Series(np.arange(1, 31), name="patient")
   actual_charge = pd.Series(
       rng.uniform(8, 60, 30).round(1), name="actual_charge_kusd"
   ).sort_values().reset_index(drop=True)
   predicted_charge = pd.Series(
       actual_charge + rng.normal(0, 4.5, 30), name="predicted_charge_kusd"
   )

   fig = prediction_interval_plot_interactive(
       actual_charge, predicted_charge, confidence=0.90, method="empirical",
       title="Hospital charge model: 90% prediction intervals",
       point_color="#2a6f97", band_color="rgba(168,213,229,0.5)",
       line_color="#d62728", template="plotly_white",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/prediction_extended/prediction_interval_plot_interactive.png" alt="prediction_interval_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
