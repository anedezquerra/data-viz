dataviz.xai.fairness_xai.subgroup_shap_divergence_interactive
=============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.fairness_xai</p></div>

.. currentmodule:: dataviz.xai.fairness_xai

.. autofunction:: subgroup_shap_divergence_interactive

Use case
--------

Check whether a model relies on features differently across protected subgroups by comparing SHAP distributions.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   from dataviz.xai.fairness_xai import subgroup_shap_divergence_interactive

   divergence = {"age": 0.18, "income": 0.42, "tenure": 0.07, "debt": 0.25}

   fig = subgroup_shap_divergence_interactive(divergence)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/fairness_xai/subgroup_shap_divergence_interactive.png" alt="subgroup_shap_divergence_interactive example output"><figcaption>Example output</figcaption></figure></div>
