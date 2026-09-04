dataviz.bivariate.stats.rank_scatter_interactive
================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.stats</p></div>

.. currentmodule:: dataviz.bivariate.stats

.. autofunction:: rank_scatter_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   from dataviz.bivariate.stats import rank_scatter_interactive

   x = pd.Series([1, 2, 3, 4, 5], name="Input")
   y = pd.Series([1.2, 1.9, 3.4, 3.7, 5.1], name="Output")

   fig = rank_scatter_interactive(x, y)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/bivariate/stats/rank_scatter_interactive.png" alt="rank_scatter_interactive example output"><figcaption>Example output</figcaption></figure></div>
