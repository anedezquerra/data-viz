dataviz.univariate.quality.quality_bar_interactive
==================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.quality</p></div>

.. currentmodule:: dataviz.univariate.quality

.. autofunction:: quality_bar_interactive

Use case
--------

Use to compare missing, duplicate, zero, and negative rates side by side when triaging data quality issues.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.quality import quality_bar_interactive

   rng = np.random.default_rng(42)
   readings = rng.normal(loc=55.0, scale=4.0, size=140).round(2)
   readings[[3, 27, 58, 91, 120]] = np.nan
   readings[[10, 66, 101]] = -999.0
   sensor = pd.Series(readings, name="temperature_c")
   fig = quality_bar_interactive(
       sensor,
       title="Sensor Feed Quality Rates",
       color="slategray",
       height=450,
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/quality/quality_bar_interactive.png" alt="quality_bar_interactive example output"><figcaption>Example output</figcaption></figure></div>
