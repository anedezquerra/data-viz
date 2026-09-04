dataviz.bivariate.joint.joint_scatter_hist_static
=================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.joint</p></div>

.. currentmodule:: dataviz.bivariate.joint

.. autofunction:: joint_scatter_hist_static

Use case
--------

Use to see a two-variable relationship and each marginal distribution in one figure during exploratory analysis.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.bivariate.joint import joint_scatter_hist_static

   rng = np.random.default_rng(42)
   n = 250
   height_cm = pd.Series(rng.normal(loc=172.0, scale=9.0, size=n), name="Height (cm)")
   weight_kg = pd.Series(0.9 * height_cm - 85.0 + rng.normal(loc=0.0, scale=6.0, size=n), name="Weight (kg)")

   ax = joint_scatter_hist_static(
       height_cm,
       weight_kg,
       bins=20,
       title="Height vs Weight Joint Distribution",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/joint/joint_scatter_hist_static.png" alt="joint_scatter_hist_static example output"><figcaption>Example output</figcaption></figure></div>
