dataviz.regression.survival.cox_residual_plot_static
====================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.survival</p></div>

.. currentmodule:: dataviz.regression.survival

.. autofunction:: cox_residual_plot_static

Use case
--------

Use to diagnose a Cox model by plotting martingale, deviance, or Schoenfeld residuals against time; patterns indicate bad fit or violated assumptions.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.survival import cox_residual_plot_static

   rng = np.random.default_rng(42)
   n = 40
   follow_up = np.sort(rng.uniform(2, 60, n))  # months
   martingale = rng.normal(0, 0.45, n).clip(-1.0, 1.0)
   martingale[follow_up > 45] += 0.15          # mild lack of fit at long times

   ax = cox_residual_plot_static(
       follow_up, martingale, kind="martingale",
       title="Cardiology cohort: Cox martingale residuals vs follow-up time",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/survival/cox_residual_plot_static.png" alt="cox_residual_plot_static example output"><figcaption>Example output</figcaption></figure></div>
