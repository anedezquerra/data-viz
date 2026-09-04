dataviz.regression.glm.variance_function_plot_static
====================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.glm</p></div>

.. currentmodule:: dataviz.regression.glm

.. autofunction:: variance_function_plot_static

Use case
--------

Use to visualize the mean-variance relationship V(mu) implied by the chosen GLM family.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.glm import variance_function_plot_static

   mu = np.linspace(0.5, 5.0, 50)

   ax = variance_function_plot_static(mu, family="poisson")
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/glm/variance_function_plot_static.png" alt="variance_function_plot_static example output"><figcaption>Example output</figcaption></figure></div>
