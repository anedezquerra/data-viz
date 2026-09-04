dataviz.xai.counterfactuals.diverse_counterfactual_grid_static
==============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.counterfactuals</p></div>

.. currentmodule:: dataviz.xai.counterfactuals

.. autofunction:: diverse_counterfactual_grid_static

Use case
--------

Compare several diverse counterfactuals at once to offer users multiple actionable ways to change an outcome.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.xai.counterfactuals import diverse_counterfactual_grid_static

   original = {
       "credit_score": 612,
       "debt_to_income": 0.48,
       "utilization": 0.81,
       "annual_income": 52000,
   }
   counterfactuals = pd.DataFrame(
       [
           [660, 0.48, 0.81, 52000],
           [612, 0.34, 0.60, 52000],
           [648, 0.40, 0.81, 61000],
           [612, 0.38, 0.62, 57500],
       ],
       columns=list(original),
   )

   ax = diverse_counterfactual_grid_static(
       original,
       counterfactuals,
       title="Diverse Counterfactuals for Denied Applicant #417",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/counterfactuals/diverse_counterfactual_grid_static.png" alt="diverse_counterfactual_grid_static example output"><figcaption>Example output</figcaption></figure></div>
