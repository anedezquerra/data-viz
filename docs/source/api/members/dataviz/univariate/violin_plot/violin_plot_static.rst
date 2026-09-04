dataviz.univariate.violin_plot.violin_plot_static
=================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.violin_plot</p></div>

.. currentmodule:: dataviz.univariate.violin_plot

.. autofunction:: violin_plot_static

Use case
--------

Use to show the full distribution shape with density width plus an inner box, revealing modality that a box plot hides.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.univariate.violin_plot import violin_plot_static

   rng = np.random.default_rng(42)
   carriers = rng.choice(["Aeris", "Boreal", "Cirrus"], size=180)
   offsets = {"Aeris": 4.2, "Boreal": 5.1, "Cirrus": 3.6}
   delivery = [rng.normal(offsets[c], 0.9) for c in carriers]
   shipments = pd.DataFrame({"carrier": carriers, "delivery_days": np.round(delivery, 1)})
   ax = violin_plot_static(
       shipments,
       x="carrier",
       y="delivery_days",
       title="Delivery Time by Carrier",
       xlabel="Carrier",
       ylabel="Delivery time (days)",
       palette="Set2",
       inner="quartile",
       theme="minimal",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/violin_plot/violin_plot_static.png" alt="violin_plot_static example output"><figcaption>Example output</figcaption></figure></div>
