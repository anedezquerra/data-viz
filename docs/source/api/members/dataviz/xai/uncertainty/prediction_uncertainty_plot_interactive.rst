dataviz.xai.uncertainty.prediction_uncertainty_plot_interactive
===============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.uncertainty</p></div>

.. currentmodule:: dataviz.xai.uncertainty

.. autofunction:: prediction_uncertainty_plot_interactive

Use case
--------

Use to plot predictions against a feature with a plus/minus uncertainty band, locating regions where the model is unsure.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.xai.uncertainty import prediction_uncertainty_plot_interactive

   rng = np.random.default_rng(42)
   annual_income = np.linspace(20000, 150000, 50)
   logit = -2.5 + 2.0 * (annual_income - 20000) / 130000
   predictions = 1.0 / (1.0 + np.exp(-logit))
   uncertainty = 0.03 + 0.10 * np.abs(annual_income - 85000) / 65000
   fig = prediction_uncertainty_plot_interactive(
       annual_income, predictions, uncertainty, "annual_income",
       title="Approval probability with ensemble std band",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/uncertainty/prediction_uncertainty_plot_interactive.png" alt="prediction_uncertainty_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
