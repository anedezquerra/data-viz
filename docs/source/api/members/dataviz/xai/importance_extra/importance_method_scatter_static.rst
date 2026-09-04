dataviz.xai.importance_extra.importance_method_scatter_static
=============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.importance_extra</p></div>

.. currentmodule:: dataviz.xai.importance_extra

.. autofunction:: importance_method_scatter_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import matplotlib.pyplot as plt
   from dataviz.xai.importance_extra import importance_method_scatter_static

   permutation = {"age": 0.05, "income": 0.12, "tenure": 0.02, "debt": 0.07}
   gain = {"age": 0.08, "income": 0.15, "tenure": 0.03, "debt": 0.05}

   ax = importance_method_scatter_static(
       permutation, gain, a_name="permutation", b_name="gain",
   )
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/importance_extra/importance_method_scatter_static.png" alt="importance_method_scatter_static example output"><figcaption>Example output</figcaption></figure></div>
