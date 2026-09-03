dataviz.multivariate.pairplot.pairplot_interactive
==================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.multivariate.pairplot</p></div>

.. currentmodule:: dataviz.multivariate.pairplot

.. autofunction:: pairplot_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.multivariate.pairplot import pairplot_interactive

   df = pd.DataFrame({"a": [1, 2, np.nan, 4], "b": [4, 3, 2, 1], "segment": ["A", "A", "B", "B"]})

   fig = pairplot_interactive(df)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/multivariate/pairplot/pairplot_interactive.png" alt="pairplot_interactive example output"><figcaption>Example output</figcaption></figure></div>
