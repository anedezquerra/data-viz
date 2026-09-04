dataviz.xai.counterfactuals.counterfactual_path_plot_static
===========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.counterfactuals</p></div>

.. currentmodule:: dataviz.xai.counterfactuals

.. autofunction:: counterfactual_path_plot_static

Use case
--------

Use to show the sequence of feature changes needed to flip a single prediction, e.g. a loan denial.

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

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/counterfactuals/counterfactual_path_plot_static.png" alt="counterfactual_path_plot_static example output"><figcaption>Example output</figcaption></figure></div>
