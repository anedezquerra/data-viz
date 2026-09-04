dataviz.regression.bayesian.posterior_predictive_check_static
=============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.bayesian</p></div>

.. currentmodule:: dataviz.regression.bayesian

.. autofunction:: posterior_predictive_check_static

Use case
--------

Use to compare posterior-predictive draws against observed y and confirm the fitted Bayesian model can reproduce the data it was trained on.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.bayesian import posterior_predictive_check_static

   rng = np.random.default_rng(42)
   recovery = pd.Series(rng.normal(14.0, 3.0, 40), name="recovery_days")
   draws = recovery.to_numpy()[None, :] + rng.normal(0, 1.2, (40, 40))

   ax = posterior_predictive_check_static(
       recovery, draws,
       title="Clinical Trial: Posterior Predictive Check (Recovery Days)",
       bins=25, true_color="#c0392b")
   ax.set_xlabel("Recovery time (days)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/bayesian/posterior_predictive_check_static.png" alt="posterior_predictive_check_static example output"><figcaption>Example output</figcaption></figure></div>
