dataviz.regression.selection.aic_bic_bar_interactive
====================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.selection</p></div>

.. currentmodule:: dataviz.regression.selection

.. autofunction:: aic_bic_bar_interactive

Use case
--------

Compare candidate models on AIC and BIC side by side when picking a final specification; lower bars indicate better fit penalized for complexity.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.selection import aic_bic_bar_interactive

   models = ["Linear", "Quadratic", "Cubic", "Log terms", "Full kitchen-sink"]
   aic = np.array([412.3, 388.1, 390.6, 381.4, 397.9])
   bic = aic + np.array([6.2, 6.2, 9.4, 9.4, 15.7])

   fig = aic_bic_bar_interactive(
       models, aic, bic,
       title="Yield-curve regressors: AIC vs BIC per candidate model",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/selection/aic_bic_bar_interactive.png" alt="aic_bic_bar_interactive example output"><figcaption>Example output</figcaption></figure></div>
