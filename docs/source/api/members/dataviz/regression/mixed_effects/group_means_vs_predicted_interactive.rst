dataviz.regression.mixed_effects.group_means_vs_predicted_interactive
=====================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.mixed_effects</p></div>

.. currentmodule:: dataviz.regression.mixed_effects

.. autofunction:: group_means_vs_predicted_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.mixed_effects import group_means_vs_predicted_interactive

   group_labels = ["G1", "G2", "G3", "G4"]
   group_observed_means = np.array([9.5, 10.2, 10.8, 9.9])
   group_predicted_means = group_observed_means + np.array([0.1, -0.2, 0.15, -0.05])

   fig = group_means_vs_predicted_interactive(
       group_labels, group_observed_means, group_predicted_means
   )
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/regression/mixed_effects/group_means_vs_predicted_interactive.png" alt="group_means_vs_predicted_interactive example output"><figcaption>Example output</figcaption></figure></div>
