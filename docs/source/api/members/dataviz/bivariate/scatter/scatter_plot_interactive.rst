dataviz.bivariate.scatter.scatter_plot_interactive
==================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.scatter</p></div>

.. currentmodule:: dataviz.bivariate.scatter

.. autofunction:: scatter_plot_interactive

Use case
--------

Use as a first look at the relationship between two numeric variables before choosing a more specialized view.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.bivariate.scatter import scatter_plot_interactive

   rng = np.random.default_rng(42)
   n = 75
   df = pd.DataFrame({
       "Engine size (L)": rng.uniform(low=1.0, high=5.5, size=n),
       "Body style": rng.choice(["Sedan", "SUV", "Truck"], size=n),
   })
   df["Fuel economy (mpg)"] = 42.0 - 4.0 * df["Engine size (L)"] + rng.normal(loc=0.0, scale=2.5, size=n)

   fig = scatter_plot_interactive(
       "Engine size (L)",
       "Fuel economy (mpg)",
       data=df,
       hue="Body style",
       title="Engine Size vs Fuel Economy",
       fit_degree=1,
       show_corr=True,
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/scatter/scatter_plot_interactive.png" alt="scatter_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
