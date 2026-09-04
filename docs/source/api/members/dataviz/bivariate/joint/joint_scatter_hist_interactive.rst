dataviz.bivariate.joint.joint_scatter_hist_interactive
======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.joint</p></div>

.. currentmodule:: dataviz.bivariate.joint

.. autofunction:: joint_scatter_hist_interactive

Use case
--------

Use to see a two-variable relationship and each marginal distribution in one figure during exploratory analysis.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.bivariate.joint import joint_scatter_hist_interactive

   rng = np.random.default_rng(42)
   n = 250
   height_cm = pd.Series(rng.normal(loc=172.0, scale=9.0, size=n), name="Height (cm)")
   weight_kg = pd.Series(0.9 * height_cm - 85.0 + rng.normal(loc=0.0, scale=6.0, size=n), name="Weight (kg)")

   fig = joint_scatter_hist_interactive(
       height_cm,
       weight_kg,
       bins=20,
       title="Height vs Weight Joint Distribution",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/joint/joint_scatter_hist_interactive.png" alt="joint_scatter_hist_interactive example output"><figcaption>Example output</figcaption></figure></div>
