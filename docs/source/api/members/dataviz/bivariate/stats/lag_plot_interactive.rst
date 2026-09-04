dataviz.bivariate.stats.lag_plot_interactive
============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.stats</p></div>

.. currentmodule:: dataviz.bivariate.stats

.. autofunction:: lag_plot_interactive

Use case
--------

Use to check for delayed or leading-lag relationships between two ordered series, such as time-shifted signals.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   from dataviz.bivariate.stats import lag_plot_interactive

   x = pd.Series([1, 2, 3, 4, 5], name="Input")
   y = pd.Series([1.2, 1.9, 3.4, 3.7, 5.1], name="Output")

   fig = lag_plot_interactive(x, y)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/stats/lag_plot_interactive.png" alt="lag_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
