dataviz.xai.uncertainty.epistemic_vs_aleatoric_plot_interactive
===============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.uncertainty</p></div>

.. currentmodule:: dataviz.xai.uncertainty

.. autofunction:: epistemic_vs_aleatoric_plot_interactive

Use case
--------

Use to decompose uncertainty into reducible epistemic (model) and irreducible aleatoric (data) components across bins.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.xai.uncertainty import epistemic_vs_aleatoric_plot_interactive

   bin_centers = np.linspace(0.1, 0.9, 9)
   epistemic = np.array([0.08, 0.06, 0.05, 0.04, 0.04, 0.05, 0.05, 0.06, 0.08])
   aleatoric = np.array([0.03, 0.04, 0.05, 0.07, 0.08, 0.07, 0.05, 0.04, 0.03])

   fig = epistemic_vs_aleatoric_plot_interactive(bin_centers, epistemic, aleatoric)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/uncertainty/epistemic_vs_aleatoric_plot_interactive.png" alt="epistemic_vs_aleatoric_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
