dataviz.bivariate.advanced.bubble_plot_interactive
==================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.advanced</p></div>

.. currentmodule:: dataviz.bivariate.advanced

.. autofunction:: bubble_plot_interactive

Use case
--------

Use when you need to show a third numeric dimension on a scatter plot by encoding it as point size.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.bivariate.advanced import bubble_plot_interactive

   rng = np.random.default_rng(42)
   n = 60
   gdp = pd.Series(rng.normal(loc=45.0, scale=12.0, size=n), name="GDP per capita (k USD)")
   life = pd.Series(60.0 + 0.4 * gdp + rng.normal(loc=0.0, scale=3.0, size=n), name="Life expectancy (years)")
   population = pd.Series(rng.uniform(low=2.0, high=300.0, size=n), name="Population (millions)")
   co2 = pd.Series(rng.uniform(low=1.0, high=20.0, size=n), name="CO2 per capita (t)")

   fig = bubble_plot_interactive(
       gdp,
       life,
       population,
       color=co2,
       title="Life Expectancy vs Wealth by Country",
       size_scale=55.0,
       colorscale="Plasma",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/advanced/bubble_plot_interactive.png" alt="bubble_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
