dataviz.regression.spatial.panel_residual_heatmap_interactive
=============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.spatial</p></div>

.. currentmodule:: dataviz.regression.spatial

.. autofunction:: panel_residual_heatmap_interactive

Use case
--------

Use to scan panel-data residuals across units and time periods at once, spotting unit-specific bias or temporal drift in the model.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.spatial import panel_residual_heatmap_interactive

   rng = np.random.default_rng(42)
   plants = ["Austin", "Boise", "Fresno", "Reno", "Tucson", "Tulsa"]
   months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
             "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
   resid = rng.normal(0, 1, (len(plants), len(months)))
   resid[2, 6:9] += 3.0   # Fresno summer overheating episodes
   resid[0, 0:2] -= 2.0   # Austin winter start-up issues

   fig = panel_residual_heatmap_interactive(
       resid, unit_labels=plants, time_labels=months,
       title="Manufacturing line OEE model: panel residuals by plant and month",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/spatial/panel_residual_heatmap_interactive.png" alt="panel_residual_heatmap_interactive example output"><figcaption>Example output</figcaption></figure></div>
