dataviz.xai.importance_extra.permutation_importance_bar_interactive
===================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.importance_extra</p></div>

.. currentmodule:: dataviz.xai.importance_extra

.. autofunction:: permutation_importance_bar_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   from dataviz.xai.importance_extra import permutation_importance_bar_interactive

   importances = {"age": 0.045, "income": 0.120, "tenure": 0.012, "debt": 0.067}
   std = {"age": 0.008, "income": 0.020, "tenure": 0.004, "debt": 0.011}

   fig = permutation_importance_bar_interactive(importances, std=std)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/importance_extra/permutation_importance_bar_interactive.png" alt="permutation_importance_bar_interactive example output"><figcaption>Example output</figcaption></figure></div>
