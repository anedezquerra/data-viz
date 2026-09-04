dataviz.regression.importance.permutation_importance_regression_static
======================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.importance</p></div>

.. currentmodule:: dataviz.regression.importance

.. autofunction:: permutation_importance_regression_static

Use case
--------

Use to measure feature impact by permutation with mean and standard-deviation error bars.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.importance import permutation_importance_regression_static

   feature_names = ["dose_mg", "bmi", "age_years", "systolic_bp", "smoker"]
   perm_mean = pd.Series([0.28, 0.19, 0.12, 0.07, 0.03], index=feature_names,
                         name="perm_importance_mean")
   perm_std = pd.Series([0.04, 0.03, 0.03, 0.02, 0.01], index=feature_names,
                        name="perm_importance_std")

   ax = permutation_importance_regression_static(
       perm_mean, perm_std, feature_names=feature_names,
       title="Clinical Outcome Model: Permutation Importance (20 repeats)",
       color="#2ca02c", error_color="#444444")
   ax.set_xlabel("Decrease in CV R-squared")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/importance/permutation_importance_regression_static.png" alt="permutation_importance_regression_static example output"><figcaption>Example output</figcaption></figure></div>
