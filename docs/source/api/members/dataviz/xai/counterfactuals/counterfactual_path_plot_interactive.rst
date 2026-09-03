dataviz.xai.counterfactuals.counterfactual_path_plot_interactive
================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.counterfactuals</p></div>

.. currentmodule:: dataviz.xai.counterfactuals

.. autofunction:: counterfactual_path_plot_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   from dataviz.xai.counterfactuals import counterfactual_path_plot_interactive

   steps = pd.DataFrame(
       {
           "income": [45.0, 52.0, 52.0, 61.0],
           "debt": [30.0, 30.0, 22.0, 22.0],
           "tenure": [2.0, 2.0, 2.0, 3.5],
       }
   )
   predictions = [0.32, 0.41, 0.47, 0.58]

   fig = counterfactual_path_plot_interactive(steps, predictions)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/xai/counterfactuals/counterfactual_path_plot_interactive.png" alt="counterfactual_path_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
