dataviz.spc.variable.levey_jennings_chart_interactive
=====================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.variable</p></div>

.. currentmodule:: dataviz.spc.variable

.. autofunction:: levey_jennings_chart_interactive

Use case
--------

Use in laboratories to monitor assay or instrument QC results against 1, 2, and 3 sigma zones around the mean.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   from dataviz.spc.variable import levey_jennings_chart_interactive

   values = pd.Series([12.1, 11.8, 13.0, 12.7, 14.2, 12.4], name="Value")

   fig = levey_jennings_chart_interactive(values)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/variable/levey_jennings_chart_interactive.png" alt="levey_jennings_chart_interactive example output"><figcaption>Example output</figcaption></figure></div>
