dataviz.regression.spatial.moran_scatter_interactive
====================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.spatial</p></div>

.. currentmodule:: dataviz.regression.spatial

.. autofunction:: moran_scatter_interactive

Use case
--------

Use to test for spatial autocorrelation by plotting each standardized value against its spatial lag; the slope approximates Moran's I.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.regression.spatial import moran_scatter_interactive

   values = pd.Series([12.1, 11.8, 13.0, 12.7, 14.2, 12.4], name="Value")
   y_true = np.array([3.0, 2.5, 4.2, 5.0, 4.7])
   y_pred = np.array([2.8, 2.7, 4.0, 5.1, 4.5])
   train_sizes = np.array([50, 100, 200])
   train_scores = np.array([0.82, 0.86, 0.89])
   validation_scores = np.array([0.76, 0.81, 0.84])

   fig = moran_scatter_interactive(y_true, y_pred)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/spatial/moran_scatter_interactive.png" alt="moran_scatter_interactive example output"><figcaption>Example output</figcaption></figure></div>
