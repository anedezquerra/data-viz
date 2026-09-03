dataviz.xai.comparison.rashomon_importance_band_interactive
===========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.comparison</p></div>

.. currentmodule:: dataviz.xai.comparison

.. autofunction:: rashomon_importance_band_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   from dataviz.xai.comparison import rashomon_importance_band_interactive

   importances_by_model = pd.DataFrame(
       {
           "age": [0.30, 0.26, 0.33, 0.28],
           "income": [0.25, 0.29, 0.22, 0.27],
           "tenure": [0.10, 0.12, 0.09, 0.11],
       },
       index=["model_1", "model_2", "model_3", "model_4"],
   )

   fig = rashomon_importance_band_interactive(importances_by_model)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
