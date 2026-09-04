dataviz.xai.counterfactuals.counterfactual_path_plot_interactive
================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.counterfactuals</p></div>

.. currentmodule:: dataviz.xai.counterfactuals

.. autofunction:: counterfactual_path_plot_interactive

Use case
--------

Use to show the sequence of feature changes needed to flip a single prediction, e.g. a loan denial.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.xai.counterfactuals import counterfactual_path_plot_interactive

   cols = ["credit_score", "debt_to_income", "utilization"]
   steps = pd.DataFrame(
       [
           [612, 0.48, 0.81],
           [630, 0.46, 0.74],
           [655, 0.42, 0.66],
           [690, 0.37, 0.55],
           [718, 0.33, 0.44],
       ],
       columns=cols,
   )
   predictions = [0.71, 0.66, 0.58, 0.47, 0.39]

   fig = counterfactual_path_plot_interactive(
       steps,
       predictions,
       target_threshold=0.5,
       title="Counterfactual Path to Loan Approval (P(default) below 0.5)",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/counterfactuals/counterfactual_path_plot_interactive.png" alt="counterfactual_path_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
