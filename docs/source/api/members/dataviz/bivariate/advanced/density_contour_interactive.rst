dataviz.bivariate.advanced.density_contour_interactive
======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.advanced</p></div>

.. currentmodule:: dataviz.bivariate.advanced

.. autofunction:: density_contour_interactive

Use case
--------

Use to visualize the joint density of two variables as contour lines when individual points are too dense to read.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.bivariate.advanced import density_contour_interactive

   rng = np.random.default_rng(42)
   n = 800
   temperature = pd.Series(rng.normal(loc=22.0, scale=3.0, size=n), name="Temperature (C)")
   humidity = pd.Series(80.0 - 1.5 * temperature + rng.normal(loc=0.0, scale=5.0, size=n), name="Humidity (%)")

   fig = density_contour_interactive(
       temperature,
       humidity,
       title="Greenhouse Climate Density",
       colorscale="Cividis",
       contours_coloring="heatmap",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/advanced/density_contour_interactive.png" alt="density_contour_interactive example output"><figcaption>Example output</figcaption></figure></div>
