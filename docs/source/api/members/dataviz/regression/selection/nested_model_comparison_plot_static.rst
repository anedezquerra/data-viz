dataviz.regression.selection.nested_model_comparison_plot_static
================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.selection</p></div>

.. currentmodule:: dataviz.regression.selection

.. autofunction:: nested_model_comparison_plot_static

Use case
--------

Use when adding terms step by step to see how log-likelihood improves across nested models and where extra parameters stop paying off.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import matplotlib.pyplot as plt
   from dataviz.regression.selection import nested_model_comparison_plot_static

   models = ["Intercept", "+ temp", "+ pressure", "+ catalyst", "+ temp:pressure"]
   log_lik = [-128.4, -102.7, -88.9, -80.2, -79.6]
   df_diff = [1, 1, 1, 1, 1]

   ax = nested_model_comparison_plot_static(
       models, log_lik, df_diff=df_diff,
       title="Chemical reactor study: nested model log-likelihoods",
   )
   ax.axhline(-80.2, color="#888", linestyle=":", linewidth=1)
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/selection/nested_model_comparison_plot_static.png" alt="nested_model_comparison_plot_static example output"><figcaption>Example output</figcaption></figure></div>
