dataviz.xai.uncertainty.epistemic_vs_aleatoric_plot_static
==========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.uncertainty</p></div>

.. currentmodule:: dataviz.xai.uncertainty

.. autofunction:: epistemic_vs_aleatoric_plot_static

Use case
--------

Use to decompose uncertainty into reducible epistemic (model) and irreducible aleatoric (data) components across bins.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.xai.uncertainty import epistemic_vs_aleatoric_plot_static

   bin_centers = np.linspace(0.0, 1.0, 20)
   epistemic = 0.05 + 0.12 * (bin_centers - 0.5) ** 2 * 4
   aleatoric = 0.08 + 0.05 * np.sin(np.pi * bin_centers)
   ax = epistemic_vs_aleatoric_plot_static(
       bin_centers, epistemic, aleatoric,
       title="Uncertainty decomposition across predicted-risk deciles",
   )
   ax.set_xlabel("Predicted default risk (binned)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/uncertainty/epistemic_vs_aleatoric_plot_static.png" alt="epistemic_vs_aleatoric_plot_static example output"><figcaption>Example output</figcaption></figure></div>
