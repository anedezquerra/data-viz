dataviz.regression.uncertainty.jackknife_plus_band_interactive
==============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.uncertainty</p></div>

.. currentmodule:: dataviz.regression.uncertainty

.. autofunction:: jackknife_plus_band_interactive

Use case
--------

Use to visualize jackknife+ predictive bands around sorted predictions and see where actuals fall outside the interval.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.uncertainty import jackknife_plus_band_interactive

   rng = np.random.default_rng(42)
   n = 30
   load_mw = 450 + 120 * np.sin(np.linspace(0, 2 * np.pi, n)) + rng.normal(0, 18, n)
   pred_mw = 450 + 120 * np.sin(np.linspace(0, 2 * np.pi, n))
   half_width = 25 + 8 * np.abs(np.sin(np.linspace(0, np.pi, n)))
   lower, upper = pred_mw - half_width, pred_mw + half_width

   fig = jackknife_plus_band_interactive(
       load_mw, pred_mw, lower, upper,
       title="Grid load forecast: jackknife+ 90% predictive band",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/uncertainty/jackknife_plus_band_interactive.png" alt="jackknife_plus_band_interactive example output"><figcaption>Example output</figcaption></figure></div>
