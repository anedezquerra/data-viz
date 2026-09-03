dataviz.xai.dependence_more.ale_plot_2d_static
==============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.dependence_more</p></div>

.. currentmodule:: dataviz.xai.dependence_more

.. autofunction:: ale_plot_2d_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.xai.dependence_more import ale_plot_2d_static

   rng = np.random.default_rng(19)
   x_edges = np.linspace(0.0, 5.0, 6)
   y_edges = np.linspace(0.0, 4.0, 5)
   ale_grid = rng.normal(0.0, 0.3, size=(5, 4))

   ax = ale_plot_2d_static(
       ale_grid, x_edges, y_edges, feature_x="income", feature_y="tenure",
   )
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
