dataviz.regression.coefficients.coefficient_plot_interactive
============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.coefficients</p></div>

.. currentmodule:: dataviz.regression.coefficients

.. autofunction:: coefficient_plot_interactive

Use case
--------

Use for a quick read of coefficient magnitude and sign, colored by direction, when communicating which drivers push predictions up or down.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.coefficients import coefficient_plot_interactive

   features = ["temperature_c", "pressure_bar", "catalyst_g", "residence_min",
               "humidity_pct"]
   coefs = np.array([1.85, -0.42, 2.30, 0.66, -0.12])

   fig = coefficient_plot_interactive(coefs, feature_names=features,
                                      title="Polymer Yield Model: Coefficients",
                                      positive_color="#2a7f62",
                                      negative_color="#c0392b", sort=True,
                                      template="plotly_white")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/coefficients/coefficient_plot_interactive.png" alt="coefficient_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
