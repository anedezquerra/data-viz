dataviz.regression.selection.nested_model_comparison_plot_interactive
=====================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.selection</p></div>

.. currentmodule:: dataviz.regression.selection

.. autofunction:: nested_model_comparison_plot_interactive

Use case
--------

Use when adding terms step by step to see how log-likelihood improves across nested models and where extra parameters stop paying off.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   from dataviz.regression.selection import nested_model_comparison_plot_interactive

   models = ["Intercept", "+ temp", "+ pressure", "+ catalyst", "+ temp:pressure"]
   log_lik = [-128.4, -102.7, -88.9, -80.2, -79.6]
   df_diff = [1, 1, 1, 1, 1]

   fig = nested_model_comparison_plot_interactive(
       models, log_lik, df_diff=df_diff,
       title="Chemical reactor study: nested model log-likelihoods",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/selection/nested_model_comparison_plot_interactive.png" alt="nested_model_comparison_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
