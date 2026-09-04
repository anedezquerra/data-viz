dataviz.xai.surrogate.counterfactual_change_bar_static
======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.surrogate</p></div>

.. currentmodule:: dataviz.xai.surrogate

.. autofunction:: counterfactual_change_bar_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import matplotlib.pyplot as plt
   from dataviz.xai.surrogate import counterfactual_change_bar_static

   original = {"income": 45.0, "debt": 30.0, "tenure": 2.0}
   counterfactual = {"income": 58.0, "debt": 22.0, "tenure": 2.0}

   ax = counterfactual_change_bar_static(original, counterfactual)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/surrogate/counterfactual_change_bar_static.png" alt="counterfactual_change_bar_static example output"><figcaption>Example output</figcaption></figure></div>
