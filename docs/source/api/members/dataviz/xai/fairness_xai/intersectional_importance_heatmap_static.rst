dataviz.xai.fairness_xai.intersectional_importance_heatmap_static
=================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.fairness_xai</p></div>

.. currentmodule:: dataviz.xai.fairness_xai

.. autofunction:: intersectional_importance_heatmap_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.xai.fairness_xai import intersectional_importance_heatmap_static

   importance_cube = pd.DataFrame(
       {
           "age": [0.30, 0.24, 0.18, 0.27],
           "income": [0.22, 0.29, 0.31, 0.25],
           "tenure": [0.10, 0.08, 0.14, 0.09],
       },
       index=["young-a", "young-b", "senior-a", "senior-b"],
   )

   ax = intersectional_importance_heatmap_static(importance_cube)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
