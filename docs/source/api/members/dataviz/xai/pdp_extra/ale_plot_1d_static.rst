dataviz.xai.pdp_extra.ale_plot_1d_static
========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.pdp_extra</p></div>

.. currentmodule:: dataviz.xai.pdp_extra

.. autofunction:: ale_plot_1d_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.xai.pdp_extra import ale_plot_1d_static

   bin_edges = np.linspace(20.0, 80.0, 7)
   ale = np.array([-0.12, -0.05, 0.01, 0.06, 0.10, 0.14])

   ax = ale_plot_1d_static(bin_edges, ale, feature_name="income")
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/pdp_extra/ale_plot_1d_static.png" alt="ale_plot_1d_static example output"><figcaption>Example output</figcaption></figure></div>
