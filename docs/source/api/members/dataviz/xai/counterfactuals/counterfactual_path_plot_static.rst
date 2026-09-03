dataviz.xai.counterfactuals.counterfactual_path_plot_static
===========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.counterfactuals</p></div>

.. currentmodule:: dataviz.xai.counterfactuals

.. autofunction:: counterfactual_path_plot_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.xai.counterfactuals import counterfactual_path_plot_static

   steps = pd.DataFrame(
       {
           "income": [45.0, 52.0, 52.0, 61.0],
           "debt": [30.0, 30.0, 22.0, 22.0],
           "tenure": [2.0, 2.0, 2.0, 3.5],
       }
   )
   predictions = [0.32, 0.41, 0.47, 0.58]

   ax = counterfactual_path_plot_static(steps, predictions)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
