dataviz.univariate.treatment.outlier_treatment_comparison_interactive
=====================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.treatment</p></div>

.. currentmodule:: dataviz.univariate.treatment

.. autofunction:: outlier_treatment_comparison_interactive

Use case
--------

Use to review original versus capped or removed distributions side by side before approving a treatment.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.treatment import outlier_treatment_comparison_interactive

   rng = np.random.default_rng(42)
   latency = rng.normal(loc=120.0, scale=15.0, size=180).round(1)
   latency[[9, 54, 121, 160]] = [520.0, 610.0, 480.0, 700.0]
   latency_ms = pd.Series(latency, name="latency_ms")
   fig = outlier_treatment_comparison_interactive(
       latency_ms,
       rule="iqr",
       treatment="cap",
       title="API Latency Before and After Capping",
       color="skyblue",
       height=500,
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/treatment/outlier_treatment_comparison_interactive.png" alt="outlier_treatment_comparison_interactive example output"><figcaption>Example output</figcaption></figure></div>
