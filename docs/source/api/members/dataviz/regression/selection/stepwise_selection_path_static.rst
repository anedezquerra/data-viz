dataviz.regression.selection.stepwise_selection_path_static
===========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.selection</p></div>

.. currentmodule:: dataviz.regression.selection

.. autofunction:: stepwise_selection_path_static

Use case
--------

Use to trace a forward or backward stepwise search step by step, showing how the score evolves as features enter or leave the model.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import matplotlib.pyplot as plt
   from dataviz.regression.selection import stepwise_selection_path_static

   steps = ["start", "+ sqft", "+ bedrooms", "+ age", "+ garage",
            "+ baths", "- bedrooms", "+ lot_size"]
   cv_rmse = [95.2, 61.8, 55.4, 49.7, 47.3, 46.9, 45.8, 45.6]

   ax = stepwise_selection_path_static(
       steps, cv_rmse, metric_name="CV RMSE (k$)",
       title="Housing price model: stepwise selection path",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/selection/stepwise_selection_path_static.png" alt="stepwise_selection_path_static example output"><figcaption>Example output</figcaption></figure></div>
