dataviz.bivariate.categorical.grouped_bar_interactive
=====================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.categorical</p></div>

.. currentmodule:: dataviz.bivariate.categorical

.. autofunction:: grouped_bar_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.bivariate.categorical import grouped_bar_interactive

   rng = np.random.default_rng(42)
   category = pd.Series(np.repeat(["Line A", "Line B", "Line C"], 10), name="Line")
   values = pd.Series(rng.normal(loc=10.0, scale=1.0, size=30), name="Output")

   fig = grouped_bar_interactive(category, values, title="Mean output by line")
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/categorical/grouped_bar_interactive.png" alt="grouped_bar_interactive example output"><figcaption>Example output</figcaption></figure></div>
