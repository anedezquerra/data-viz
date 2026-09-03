dataviz.xai.dependence_more.h_statistic_heatmap_interactive
===========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.dependence_more</p></div>

.. currentmodule:: dataviz.xai.dependence_more

.. autofunction:: h_statistic_heatmap_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   from dataviz.xai.dependence_more import h_statistic_heatmap_interactive

   h_matrix = pd.DataFrame(
       [[1.0, 0.32, 0.05], [0.32, 1.0, 0.11], [0.05, 0.11, 1.0]],
       index=["age", "income", "tenure"],
       columns=["age", "income", "tenure"],
   )

   fig = h_statistic_heatmap_interactive(h_matrix)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
