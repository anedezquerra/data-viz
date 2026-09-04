dataviz.univariate.advanced.ridgeline_plot_interactive
======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.advanced</p></div>

.. currentmodule:: dataviz.univariate.advanced

.. autofunction:: ridgeline_plot_interactive

Use case
--------

Use to stack density curves for several numeric dataframe columns to compare distribution shapes across variables at a glance.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.advanced import ridgeline_plot_interactive

   rng = np.random.default_rng(42)
   data = pd.DataFrame({
       "Line A": rng.normal(loc=10.0, scale=0.4, size=50),
       "Line B": rng.normal(loc=10.5, scale=0.5, size=50),
       "Line C": rng.normal(loc=9.8, scale=0.3, size=50),
   })

   fig = ridgeline_plot_interactive(data, title="Ridgeline plot")
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/advanced/ridgeline_plot_interactive.png" alt="ridgeline_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
