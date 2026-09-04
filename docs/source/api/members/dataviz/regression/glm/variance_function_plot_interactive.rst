dataviz.regression.glm.variance_function_plot_interactive
=========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.glm</p></div>

.. currentmodule:: dataviz.regression.glm

.. autofunction:: variance_function_plot_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.glm import variance_function_plot_interactive

   mu = np.linspace(0.5, 5.0, 50)

   fig = variance_function_plot_interactive(mu, family="poisson")
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/glm/variance_function_plot_interactive.png" alt="variance_function_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
