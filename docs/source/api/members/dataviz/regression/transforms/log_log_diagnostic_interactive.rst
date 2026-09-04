dataviz.regression.transforms.log_log_diagnostic_interactive
============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.transforms</p></div>

.. currentmodule:: dataviz.regression.transforms

.. autofunction:: log_log_diagnostic_interactive

Use case
--------

Use to test a power-law relationship between x and y; a straight line in log-log space justifies a log-log model and its slope is the exponent.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.transforms import log_log_diagnostic_interactive

   rng = np.random.default_rng(42)
   n = 38
   city_area = rng.uniform(20, 900, n)                    # km^2
   population = 4200 * city_area ** 0.85 * np.exp(rng.normal(0, 0.18, n))

   fig = log_log_diagnostic_interactive(
       city_area, population,
       title="Urban scaling study: log-log check of area vs population",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/transforms/log_log_diagnostic_interactive.png" alt="log_log_diagnostic_interactive example output"><figcaption>Example output</figcaption></figure></div>
