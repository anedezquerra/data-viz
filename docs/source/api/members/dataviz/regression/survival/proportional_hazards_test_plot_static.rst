dataviz.regression.survival.proportional_hazards_test_plot_static
=================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.survival</p></div>

.. currentmodule:: dataviz.regression.survival

.. autofunction:: proportional_hazards_test_plot_static

Use case
--------

Use to check the Cox proportional-hazards assumption per covariate; bars below the alpha line flag Schoenfeld test violations.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import matplotlib.pyplot as plt
   from dataviz.regression.survival import proportional_hazards_test_plot_static

   covariates = ["age", "bmi", "smoker", "stage", "treatment", "sex"]
   p_values = [0.62, 0.31, 0.08, 0.012, 0.44, 0.71]

   ax = proportional_hazards_test_plot_static(
       covariates, p_values, alpha=0.05,
       title="Schoenfeld test of the proportional-hazards assumption",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/survival/proportional_hazards_test_plot_static.png" alt="proportional_hazards_test_plot_static example output"><figcaption>Example output</figcaption></figure></div>
