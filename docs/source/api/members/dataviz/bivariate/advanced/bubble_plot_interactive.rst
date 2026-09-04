dataviz.bivariate.advanced.bubble_plot_interactive
==================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.advanced</p></div>

.. currentmodule:: dataviz.bivariate.advanced

.. autofunction:: bubble_plot_interactive

Use case
--------

Use when you need to show a third numeric dimension on a scatter plot by encoding it as point size.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.bivariate.advanced import bubble_plot_interactive

   rng = np.random.default_rng(42)
   x = rng.normal(loc=10.0, scale=2.0, size=30)
   y = 2.0 * x + rng.normal(loc=0.0, scale=1.0, size=30)
   size = rng.uniform(low=10.0, high=100.0, size=30)

   fig = bubble_plot_interactive(x, y, size, title="Bubble plot")
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/advanced/bubble_plot_interactive.png" alt="bubble_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
