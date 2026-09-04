dataviz.xai.pdp_extra.ale_plot_1d_static
========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.pdp_extra</p></div>

.. currentmodule:: dataviz.xai.pdp_extra

.. autofunction:: ale_plot_1d_static

Use case
--------

Use instead of PDP when features are correlated; ALE accumulates local effects within data-supported bins to avoid extrapolation bias.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.xai.pdp_extra import ale_plot_1d_static

   bin_edges = np.linspace(0.0, 0.6, 11)
   centers = (bin_edges[:-1] + bin_edges[1:]) / 2
   ale = 2.1 * centers - 0.9 * centers ** 2
   ale = ale - ale.mean()
   ax = ale_plot_1d_static(
       bin_edges, ale, feature_name="debt_to_income",
       title="ALE of debt-to-income on default log-odds",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/pdp_extra/ale_plot_1d_static.png" alt="ale_plot_1d_static example output"><figcaption>Example output</figcaption></figure></div>
