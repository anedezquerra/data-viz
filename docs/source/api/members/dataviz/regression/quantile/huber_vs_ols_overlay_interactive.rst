dataviz.regression.quantile.huber_vs_ols_overlay_interactive
============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.quantile</p></div>

.. currentmodule:: dataviz.regression.quantile

.. autofunction:: huber_vs_ols_overlay_interactive

Use case
--------

Use to show how a robust Huber fit diverges from OLS on data containing outliers.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.quantile import huber_vs_ols_overlay_interactive

   rng = np.random.default_rng(42)
   x = np.linspace(0.0, 10.0, 60)
   y = 2 * x + rng.normal(0.0, 1.0, size=60)
   y_ols = 2 * x + 0.1
   y_huber = 2 * x - 0.05

   fig = huber_vs_ols_overlay_interactive(x, y, y_ols, y_huber)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/quantile/huber_vs_ols_overlay_interactive.png" alt="huber_vs_ols_overlay_interactive example output"><figcaption>Example output</figcaption></figure></div>
