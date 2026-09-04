dataviz.regression.selection.forward_selection_score_curve_static
=================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.selection</p></div>

.. currentmodule:: dataviz.regression.selection

.. autofunction:: forward_selection_score_curve_static

Use case
--------

Use to pick how many features to keep in forward selection by finding the point where adding more features stops improving the score.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.selection import forward_selection_score_curve_static

   num_features = np.arange(1, 9)
   adj_r2 = [0.42, 0.61, 0.70, 0.75, 0.78, 0.80, 0.807, 0.809]

   ax = forward_selection_score_curve_static(
       num_features, adj_r2, metric_name="Adjusted R-squared",
       title="Bike-share demand: forward selection score curve",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/selection/forward_selection_score_curve_static.png" alt="forward_selection_score_curve_static example output"><figcaption>Example output</figcaption></figure></div>
