dataviz.xai.counterfactuals.diverse_counterfactual_grid_interactive
===================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.counterfactuals</p></div>

.. currentmodule:: dataviz.xai.counterfactuals

.. autofunction:: diverse_counterfactual_grid_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   from dataviz.xai.counterfactuals import diverse_counterfactual_grid_interactive

   original = {"income": 45.0, "debt": 30.0, "tenure": 2.0}
   counterfactuals = pd.DataFrame(
       {
           "income": [55.0, 48.0, 62.0],
           "debt": [24.0, 26.0, 30.0],
           "tenure": [2.0, 3.0, 4.0],
       }
   )

   fig = diverse_counterfactual_grid_interactive(original, counterfactuals)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
