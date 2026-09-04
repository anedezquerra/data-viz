dataviz.xai.charts.partial_dependence
=====================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.charts</p></div>

.. currentmodule:: dataviz.xai.charts

.. autofunction:: partial_dependence

Use case
--------

Use to show how one feature affects the predicted outcome on average, holding other features constant.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.xai.charts import partial_dependence

   grid = np.linspace(300, 850, 40)
   pred_default = 1.0 / (1.0 + np.exp((grid - 580.0) / 60.0))

   ax = partial_dependence(
       grid,
       pred_default,
       feature_name="Credit score",
       title="Partial Dependence of Default Risk on Credit Score",
       color="darkred",
       linewidth=2,
   )
   ax.set_ylabel("P(default)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/charts/partial_dependence.png" alt="partial_dependence example output"><figcaption>Example output</figcaption></figure></div>
