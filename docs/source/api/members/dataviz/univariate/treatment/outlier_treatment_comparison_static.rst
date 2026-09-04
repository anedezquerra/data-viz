dataviz.univariate.treatment.outlier_treatment_comparison_static
================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.treatment</p></div>

.. currentmodule:: dataviz.univariate.treatment

.. autofunction:: outlier_treatment_comparison_static

Use case
--------

Use to review original versus capped or removed distributions side by side before approving a treatment.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.univariate.treatment import outlier_treatment_comparison_static

   rng = np.random.default_rng(42)
   latency = rng.normal(loc=120.0, scale=15.0, size=180).round(1)
   latency[[9, 54, 121, 160]] = [520.0, 610.0, 480.0, 700.0]
   latency_ms = pd.Series(latency, name="latency_ms")
   ax = outlier_treatment_comparison_static(
       latency_ms,
       rule="iqr",
       treatment="cap",
       title="API Latency Before and After Capping",
       color="skyblue",
       theme="minimal",
   )
   ax.set_ylabel("Latency (ms)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/treatment/outlier_treatment_comparison_static.png" alt="outlier_treatment_comparison_static example output"><figcaption>Example output</figcaption></figure></div>
