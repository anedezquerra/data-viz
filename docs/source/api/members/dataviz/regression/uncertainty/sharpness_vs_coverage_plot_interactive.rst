dataviz.regression.uncertainty.sharpness_vs_coverage_plot_interactive
=====================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.uncertainty</p></div>

.. currentmodule:: dataviz.regression.uncertainty

.. autofunction:: sharpness_vs_coverage_plot_interactive

Use case
--------

Compare models on the interval-width vs coverage trade-off to find the one with the sharpest intervals that still cover the target rate.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   from dataviz.regression.uncertainty import sharpness_vs_coverage_plot_interactive

   models = ["Linear+conformal", "Quantile RF", "Bayesian ridge", "NGBoost"]
   sharpness = [58.2, 44.7, 49.5, 41.3]   # average interval width (k$)
   coverage = [0.901, 0.912, 0.887, 0.928]

   fig = sharpness_vs_coverage_plot_interactive(
       sharpness, coverage, model_labels=models,
       title="House price intervals: sharpness vs empirical coverage",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/uncertainty/sharpness_vs_coverage_plot_interactive.png" alt="sharpness_vs_coverage_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
