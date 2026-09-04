dataviz.xai.partial_dep.partial_dependence_interactive
======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.partial_dep</p></div>

.. currentmodule:: dataviz.xai.partial_dep

.. autofunction:: partial_dependence_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.xai.partial_dep import partial_dependence_interactive

   importances = np.array([0.42, 0.31, 0.18])
   feature_names = ["age", "income", "tenure"]
   shap_values = np.array([[0.1, -0.2, 0.3], [0.2, -0.1, 0.1]])
   feature_values = np.array([0, 1, 2, 3])
   pd_values = np.array([0.2, 0.25, 0.31, 0.34])

   fig = partial_dependence_interactive(feature_values, pd_values)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/xai/partial_dep/partial_dependence_interactive.png" alt="partial_dependence_interactive example output"><figcaption>Example output</figcaption></figure></div>
