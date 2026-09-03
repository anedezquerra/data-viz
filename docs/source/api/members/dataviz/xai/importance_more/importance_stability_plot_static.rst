dataviz.xai.importance_more.importance_stability_plot_static
============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.importance_more</p></div>

.. currentmodule:: dataviz.xai.importance_more

.. autofunction:: importance_stability_plot_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.xai.importance_more import importance_stability_plot_static

   rng = np.random.default_rng(27)
   fold_importances = pd.DataFrame(
       rng.normal([0.05, 0.12, 0.02], [0.01, 0.02, 0.005], size=(6, 3)),
       columns=["age", "income", "tenure"],
   )

   ax = importance_stability_plot_static(fold_importances)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/xai/importance_more/importance_stability_plot_static.png" alt="importance_stability_plot_static example output"><figcaption>Example output</figcaption></figure></div>
