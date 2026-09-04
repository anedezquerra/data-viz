dataviz.regression.influence.influence_bubble_plot_interactive
==============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.influence</p></div>

.. currentmodule:: dataviz.regression.influence

.. autofunction:: influence_bubble_plot_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.influence import influence_bubble_plot_interactive

   rng = np.random.default_rng(42)
   X = rng.normal(0.0, 1.0, size=(60, 3))
   y_true = rng.normal(10.0, 2.0, size=60)
   y_pred = y_true + rng.normal(0.0, 0.5, size=60)

   fig = influence_bubble_plot_interactive(X, y_true, y_pred)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/influence/influence_bubble_plot_interactive.png" alt="influence_bubble_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
