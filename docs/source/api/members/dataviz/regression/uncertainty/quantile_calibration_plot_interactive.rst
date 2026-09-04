dataviz.regression.uncertainty.quantile_calibration_plot_interactive
====================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.uncertainty</p></div>

.. currentmodule:: dataviz.regression.uncertainty

.. autofunction:: quantile_calibration_plot_interactive

Use case
--------

Use to check whether predicted quantiles are calibrated by plotting nominal vs empirical coverage against the ideal diagonal.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.uncertainty import quantile_calibration_plot_interactive

   nominal = np.linspace(0.05, 0.95, 19)
   empirical = nominal + 0.04 * np.sin(2 * np.pi * nominal) - 0.015

   fig = quantile_calibration_plot_interactive(
       nominal, empirical,
       title="Rainfall quantile regression: nominal vs empirical coverage",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/uncertainty/quantile_calibration_plot_interactive.png" alt="quantile_calibration_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
