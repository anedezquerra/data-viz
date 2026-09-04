dataviz.xai.fairness_xai.subgroup_shap_divergence_static
========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.fairness_xai</p></div>

.. currentmodule:: dataviz.xai.fairness_xai

.. autofunction:: subgroup_shap_divergence_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import matplotlib.pyplot as plt
   from dataviz.xai.fairness_xai import subgroup_shap_divergence_static

   divergence = {"age": 0.18, "income": 0.42, "tenure": 0.07, "debt": 0.25}

   ax = subgroup_shap_divergence_static(divergence)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/fairness_xai/subgroup_shap_divergence_static.png" alt="subgroup_shap_divergence_static example output"><figcaption>Example output</figcaption></figure></div>
