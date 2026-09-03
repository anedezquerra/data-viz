dataviz.xai.dependence_more.ale_plot_2d_interactive
===================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.dependence_more</p></div>

.. currentmodule:: dataviz.xai.dependence_more

.. autofunction:: ale_plot_2d_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.xai.dependence_more import ale_plot_2d_interactive

   rng = np.random.default_rng(19)
   x_edges = np.linspace(0.0, 5.0, 6)
   y_edges = np.linspace(0.0, 4.0, 5)
   ale_grid = rng.normal(0.0, 0.3, size=(5, 4))

   fig = ale_plot_2d_interactive(
       ale_grid, x_edges, y_edges, feature_x="income", feature_y="tenure",
   )
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/xai/dependence_more/ale_plot_2d_interactive.png" alt="ale_plot_2d_interactive example output"><figcaption>Example output</figcaption></figure></div>
