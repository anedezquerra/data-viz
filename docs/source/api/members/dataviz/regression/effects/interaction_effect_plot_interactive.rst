dataviz.regression.effects.interaction_effect_plot_interactive
==============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.effects</p></div>

.. currentmodule:: dataviz.regression.effects

.. autofunction:: interaction_effect_plot_interactive

Use case
--------

Use to show how the effect of one feature changes across levels of a second feature, exposing interactions.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.effects import interaction_effect_plot_interactive

   x_grid = np.linspace(0.0, 1.0, 20)
   curves = [x_grid**2, np.sqrt(x_grid), x_grid]

   fig = interaction_effect_plot_interactive(
       x_grid, curves, ["low", "mid", "high"], feature_name="x1"
   )
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/effects/interaction_effect_plot_interactive.png" alt="interaction_effect_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
