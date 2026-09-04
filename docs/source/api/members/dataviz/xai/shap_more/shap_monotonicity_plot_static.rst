dataviz.xai.shap_more.shap_monotonicity_plot_static
===================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.shap_more</p></div>

.. currentmodule:: dataviz.xai.shap_more

.. autofunction:: shap_monotonicity_plot_static

Use case
--------

Use to check whether a feature's SHAP values rise monotonically with its value, with an isotonic fit overlay for validation audits.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.xai.shap_more import shap_monotonicity_plot_static

   rng = np.random.default_rng(42)
   credit_score = rng.uniform(300, 850, size=80)
   shap_values = (
       -0.004 * (credit_score - 575)
       + rng.normal(0, 0.08, size=credit_score.size)
   )
   ax = shap_monotonicity_plot_static(
       credit_score, shap_values, "credit_score",
       title="Monotonicity check: higher score always lowers risk",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/shap_more/shap_monotonicity_plot_static.png" alt="shap_monotonicity_plot_static example output"><figcaption>Example output</figcaption></figure></div>
