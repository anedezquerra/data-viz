dataviz.bivariate.correlation.correlation_heatmap_interactive
=============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.correlation</p></div>

.. currentmodule:: dataviz.bivariate.correlation

.. autofunction:: correlation_heatmap_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.bivariate.correlation import correlation_heatmap_interactive

   rng = np.random.default_rng(42)
   df = pd.DataFrame({
       "Speed": rng.normal(loc=100.0, scale=5.0, size=30),
       "Pressure": rng.normal(loc=50.0, scale=2.0, size=30),
       "Yield": rng.normal(loc=90.0, scale=3.0, size=30),
   })

   fig = correlation_heatmap_interactive(df, title="Process correlation")
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/bivariate/correlation/correlation_heatmap_interactive.png" alt="correlation_heatmap_interactive example output"><figcaption>Example output</figcaption></figure></div>
