dataviz.univariate.violin_plot.violin_plot_interactive
======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.violin_plot</p></div>

.. currentmodule:: dataviz.univariate.violin_plot

.. autofunction:: violin_plot_interactive

Use case
--------

Use to show the full distribution shape with density width plus an inner box, revealing modality that a box plot hides.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.violin_plot import violin_plot_interactive

   rng = np.random.default_rng(42)
   carriers = rng.choice(["Aeris", "Boreal", "Cirrus"], size=180)
   offsets = {"Aeris": 4.2, "Boreal": 5.1, "Cirrus": 3.6}
   delivery = [rng.normal(offsets[c], 0.9) for c in carriers]
   shipments = pd.DataFrame({"carrier": carriers, "delivery_days": np.round(delivery, 1)})
   fig = violin_plot_interactive(
       shipments,
       x="carrier",
       y="delivery_days",
       title="Delivery Time by Carrier",
       xlabel="Carrier",
       ylabel="Delivery time (days)",
       meanline=True,
       height=550,
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/violin_plot/violin_plot_interactive.png" alt="violin_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
