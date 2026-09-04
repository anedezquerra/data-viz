dataviz.eda.charts.class_distribution
=====================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.eda.charts</p></div>

.. currentmodule:: dataviz.eda.charts

.. autofunction:: class_distribution

Use case
--------

Use to check target class balance before training a classifier and decide whether rebalancing is needed.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.eda.charts import class_distribution

   rng = np.random.default_rng(42)
   tickets = pd.Series(
       rng.choice(["Low", "Medium", "High", "Critical"], size=150, p=[0.45, 0.3, 0.18, 0.07]),
       name="Ticket priority",
   )

   ax = class_distribution(tickets, title="Support Ticket Priority Balance")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/eda/charts/class_distribution.png" alt="class_distribution example output"><figcaption>Example output</figcaption></figure></div>
