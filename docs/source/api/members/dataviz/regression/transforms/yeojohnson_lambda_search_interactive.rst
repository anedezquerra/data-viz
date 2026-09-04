dataviz.regression.transforms.yeojohnson_lambda_search_interactive
==================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.transforms</p></div>

.. currentmodule:: dataviz.regression.transforms

.. autofunction:: yeojohnson_lambda_search_interactive

Use case
--------

Use to pick a Yeo-Johnson transform for data that include zeros or negatives, reading the optimal lambda from the log-likelihood curve.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.transforms import yeojohnson_lambda_search_interactive

   rng = np.random.default_rng(42)
   profit_margin = rng.normal(4.0, 9.0, 55) - rng.gamma(1.5, 4.0, 55)  # mixed signs

   fig = yeojohnson_lambda_search_interactive(
       profit_margin, lambdas=np.linspace(-2, 2, 121),
       title="Store profit margins: Yeo-Johnson lambda search",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/transforms/yeojohnson_lambda_search_interactive.png" alt="yeojohnson_lambda_search_interactive example output"><figcaption>Example output</figcaption></figure></div>
