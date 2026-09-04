dataviz.regression.selection.stepwise_selection_path_interactive
================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.selection</p></div>

.. currentmodule:: dataviz.regression.selection

.. autofunction:: stepwise_selection_path_interactive

Use case
--------

Use to trace a forward or backward stepwise search step by step, showing how the score evolves as features enter or leave the model.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   from dataviz.regression.selection import stepwise_selection_path_interactive

   steps = ["start", "+ sqft", "+ bedrooms", "+ age", "+ garage",
            "+ baths", "- bedrooms", "+ lot_size"]
   cv_rmse = [95.2, 61.8, 55.4, 49.7, 47.3, 46.9, 45.8, 45.6]

   fig = stepwise_selection_path_interactive(
       steps, cv_rmse, metric_name="CV RMSE (k$)",
       title="Housing price model: stepwise selection path",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/selection/stepwise_selection_path_interactive.png" alt="stepwise_selection_path_interactive example output"><figcaption>Example output</figcaption></figure></div>
