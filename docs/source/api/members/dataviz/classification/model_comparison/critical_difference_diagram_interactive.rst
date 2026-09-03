dataviz.classification.model_comparison.critical_difference_diagram_interactive
===============================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.model_comparison</p></div>

.. currentmodule:: dataviz.classification.model_comparison

.. autofunction:: critical_difference_diagram_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python


   import numpy as np
   from dataviz.classification.model_comparison import critical_difference_diagram_interactive

   rank_table = {
       "Logistic regression": [2, 3, 1, 2, 3, 2],
       "Random forest": [1, 1, 2, 1, 1, 1],
       "Gradient boosting": [3, 2, 3, 3, 2, 3],
   }

   fig = critical_difference_diagram_interactive(rank_table, cd=1.2)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
