dataviz.xai.shap_extra.shap_dependence_plot_static
==================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.shap_extra</p></div>

.. currentmodule:: dataviz.xai.shap_extra

.. autofunction:: shap_dependence_plot_static

Use case
--------

Use to see how one feature's SHAP value varies with its raw value, optionally colored by a second feature to surface interactions.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.xai.shap_extra import shap_dependence_plot_static

   rng = np.random.default_rng(42)
   monthly_charges = rng.uniform(20, 130, size=60)
   tenure_months = rng.uniform(1, 72, size=60)
   shap_charges = (
       0.012 * (monthly_charges - 75)
       - 0.0004 * (monthly_charges - 75) * tenure_months / 10
       + rng.normal(0, 0.05, size=60)
   )
   ax = shap_dependence_plot_static(
       shap_charges, monthly_charges,
       interaction_values=tenure_months,
       feature_name="monthly_charges", interaction_name="tenure_months",
       title="SHAP dependence: charges effect weakens with tenure",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/shap_extra/shap_dependence_plot_static.png" alt="shap_dependence_plot_static example output"><figcaption>Example output</figcaption></figure></div>
