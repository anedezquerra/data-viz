dataviz.xai.concept.attention_heatmap_interactive
=================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.concept</p></div>

.. currentmodule:: dataviz.xai.concept

.. autofunction:: attention_heatmap_interactive

Use case
--------

Use to visualize attention weights across tokens or features in transformer-style models during error analysis.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.xai.concept import attention_heatmap_interactive

   importances = np.array([0.42, 0.31, 0.18])
   feature_names = ["age", "income", "tenure"]
   shap_values = np.array([[0.1, -0.2, 0.3], [0.2, -0.1, 0.1]])
   feature_values = np.array([0, 1, 2, 3])
   pd_values = np.array([0.2, 0.25, 0.31, 0.34])

   fig = attention_heatmap_interactive(importances, feature_names)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/concept/attention_heatmap_interactive.png" alt="attention_heatmap_interactive example output"><figcaption>Example output</figcaption></figure></div>
