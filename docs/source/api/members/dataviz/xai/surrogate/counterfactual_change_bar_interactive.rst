dataviz.xai.surrogate.counterfactual_change_bar_interactive
===========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.surrogate</p></div>

.. currentmodule:: dataviz.xai.surrogate

.. autofunction:: counterfactual_change_bar_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   from dataviz.xai.surrogate import counterfactual_change_bar_interactive

   original = {"income": 45.0, "debt": 30.0, "tenure": 2.0}
   counterfactual = {"income": 58.0, "debt": 22.0, "tenure": 2.0}

   fig = counterfactual_change_bar_interactive(original, counterfactual)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/xai/surrogate/counterfactual_change_bar_interactive.png" alt="counterfactual_change_bar_interactive example output"><figcaption>Example output</figcaption></figure></div>
