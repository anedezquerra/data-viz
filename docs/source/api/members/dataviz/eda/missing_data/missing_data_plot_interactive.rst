dataviz.eda.missing_data.missing_data_plot_interactive
======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.eda.missing_data</p></div>

.. currentmodule:: dataviz.eda.missing_data

.. autofunction:: missing_data_plot_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.eda.missing_data import missing_data_plot_interactive

   df = pd.DataFrame({"a": [1, 2, np.nan, 4], "b": [4, 3, 2, 1], "segment": ["A", "A", "B", "B"]})

   fig = missing_data_plot_interactive(df)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/eda/missing_data/missing_data_plot_interactive.png" alt="missing_data_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
