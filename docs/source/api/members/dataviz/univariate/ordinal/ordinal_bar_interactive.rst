dataviz.univariate.ordinal.ordinal_bar_interactive
==================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.ordinal</p></div>

.. currentmodule:: dataviz.univariate.ordinal

.. autofunction:: ordinal_bar_interactive

Use case
--------

Use to plot ordinal category counts or proportions in a fixed meaningful order, avoiding misleading frequency sorting.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   from dataviz.univariate.ordinal import ordinal_bar_interactive

   values = pd.Series([12.1, 11.8, 13.0, 12.7, 14.2, 12.4], name="Value")
   categories = pd.Series(["low", "medium", "high", "medium", "low"], name="Priority")

   fig = ordinal_bar_interactive(values)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/ordinal/ordinal_bar_interactive.png" alt="ordinal_bar_interactive example output"><figcaption>Example output</figcaption></figure></div>
