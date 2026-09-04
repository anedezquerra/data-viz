dataviz.eda.distribution.distribution_summary_interactive
=========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.eda.distribution</p></div>

.. currentmodule:: dataviz.eda.distribution

.. autofunction:: distribution_summary_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.eda.distribution import distribution_summary_interactive

   df = pd.DataFrame({"a": [1, 2, np.nan, 4], "b": [4, 3, 2, 1], "segment": ["A", "A", "B", "B"]})

   fig = distribution_summary_interactive(df)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/eda/distribution/distribution_summary_interactive.png" alt="distribution_summary_interactive example output"><figcaption>Example output</figcaption></figure></div>
