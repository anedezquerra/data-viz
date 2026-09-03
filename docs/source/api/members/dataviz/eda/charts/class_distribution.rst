dataviz.eda.charts.class_distribution
=====================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.eda.charts</p></div>

.. currentmodule:: dataviz.eda.charts

.. autofunction:: class_distribution

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.eda.charts import class_distribution

   rng = np.random.default_rng(42)
   series = pd.Series(rng.choice(["Pass", "Fail", "Rework"], size=60, p=[0.8, 0.1, 0.1]), name="Result")

   ax = class_distribution(series, title="Class distribution")
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
