dataviz.univariate.weighted.weighted_histogram_static
=====================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.weighted</p></div>

.. currentmodule:: dataviz.univariate.weighted

.. autofunction:: weighted_histogram_static

Use case
--------

Use to plot a histogram where rows carry unequal sample mass, such as weighted survey records.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.univariate.weighted import weighted_histogram_static

   rng = np.random.default_rng(42)
   nps_score = pd.Series(rng.integers(0, 11, size=250), name="nps_score")
   sample_weight = pd.Series(rng.uniform(0.5, 2.5, size=250).round(2), name="sample_weight")
   ax = weighted_histogram_static(
       nps_score,
       sample_weight,
       bins=11,
       title="Weighted NPS Distribution",
       xlabel="NPS score",
       color="goldenrod",
       theme="minimal",
   )
   ax.set_ylabel("Weighted count")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/weighted/weighted_histogram_static.png" alt="weighted_histogram_static example output"><figcaption>Example output</figcaption></figure></div>
